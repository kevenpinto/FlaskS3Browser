from flask import render_template, request, flash, session, Blueprint
from S3config import S3

bp = Blueprint('buckets', __name__, url_prefix='/')

@bp.route('/')
def index():
    session.clear()
    buckets = S3.get_buckets_list()
    return render_template("buckets/index.html", buckets=buckets)

@bp.route('/delete/<bucket>',methods = ['GET','POST'])
def delete(bucket):
    s3_resource = S3.get_resource()
    my_bucket = s3_resource.Bucket(bucket)
    if len(list(my_bucket.objects.all())) > 0:
        flash("Bucket Not Empty -- Cannot Be Deleted")
    else:
        flash("Bucket Sucessfully Deleted!")
        my_bucket.delete()
    buckets = S3.get_buckets_list()
    return render_template("buckets/index.html", buckets=buckets)


@bp.route('/create', methods = ['POST'])
def create():
    bucketName = request.form['bucketName']
    s3_resource = S3.get_resource()
    s3_resource.create_bucket(Bucket=bucketName
                            , CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})
    flash("Bucket Created Successfully!!")
    buckets = S3.get_buckets_list()
    return render_template("buckets/index.html", buckets=buckets)