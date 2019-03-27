from flask import render_template, request, redirect, url_for, flash, Response,session, Blueprint
from S3config import S3

bp = Blueprint('files', __name__, url_prefix='/files')

@bp.route('/files/<bucket>',methods = ['GET','POST'])
def files(bucket):
    if bucket == 'DUMMY':
        return render_template('files/files.html', my_bucket='', files='')
    session['bucket'] = bucket
    s3_resource = S3.get_resource()
    my_bucket = s3_resource.Bucket(bucket)
    summaries = my_bucket.objects.all()
    return render_template('files/files.html', my_bucket=my_bucket, files=summaries)

@bp.route('/upload', methods = ['GET','POST'])
def upload():
    try:
        file = request.files['filename']
    except KeyError:
        flash('No File Selected')
        return redirect(url_for('files.files', bucket = session.get('bucket','DUMMY')))
    except:
        flash('No File Selected')
        return redirect(url_for('files.files', bucket = session.get('bucket','DUMMY')))

    s3_resource = S3.get_resource()
    my_bucket = s3_resource.Bucket(session.get('bucket'))
    my_bucket.Object(file.filename).put(Body=file)
    flash('Files Uploaded Sucessfully')

    return redirect(url_for('files.files', bucket = session.get('bucket','DUMMY')))


@bp.route('/delete', methods = ['POST'])
def delete():
    key = request.form['key']
    s3_resource = S3.get_resource()
    my_bucket = s3_resource.Bucket(session.get('bucket'))
    my_bucket.Object(key).delete()
    flash('File deleted successfully')

    return redirect(url_for('files.files' , bucket = session.get('bucket','DUMMY')))


@bp.route('/download', methods = ['POST'])
def download():
    key = request.form['key']
    print('Download File Name ----> {}').format(key)
    s3_resource = S3.get_resource()
    my_bucket   = s3_resource.Bucket(session.get('bucket'))

    file_obj = my_bucket.Object(key).get()


    return Response(
        file_obj['Body'].read(),
        mimetype='text/plain',
        headers={"Content-Disposition": "attachment;filename={}".format(key)}
        )
