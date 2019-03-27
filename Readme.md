Project Layout  
/home/ec2-user/FlaskS3Browser
├── flaskS3/
│   ├── __init__.py   # This contains the create_app Entry Point 
│   ├── buckets.py    # Blueprint for the bucket Code
│   ├── files.py      # Blueprint for the bucket Code
│   ├── S3config.py   # Class file that holds S3 Keys and boto3 related code 
│   ├── filters.py    # Custom functions for Jinja Filters 
│   ├── templates/
│   │   ├──buckets 
│   │         ├────index.html -- Html for the Bucket handling
│   │   ├── files 
                ├────files.html -- Html for the Files under each bucket
│   │   ├── layout.html -- Base layout
│   └── static/
│       └── style.css
├── venv/ -- Python Virtual Env
├── setup.py -- U need this only if u create a Wheel Distro
├── .gitignore 
├── requirements.txt -- List of Modules used 
└── MANIFEST.in      -- U need this only if u create a Wheel Distro

Step 1 --> Create a folder called FlaskS3Browser on AWS home folder of ec2-user
mkdir FlaskS3Browser

Step 2 --> Create a Virtual Env in this folder called venv
cd FlaskS3Browser
virtualenv -p python3 venv

Step 2.1 --> Start the Virtual Env
source venv/bin/activate

Step 3 -- install Dependencies
pip install -r requirements.txt

Step 4 -- Modify the contents of S3Config.py to your AWS Keys 
or Alternatively give your AWS EC2 instance S3 access via an IAM role -- This is the preferred Method
_S3_ACCESS_KEY = ' '
_S3_SECRET = ''

Step 5 --> Open AWS, Select the Security Group and Add a Custom Inbound Rule to open up port 5000


Step 6 -- Run the App Manually -- Command for Linux -- (Change export to set if AWS on Windows)
export FLASK_APP = app.py
export FLASK_ENV = development

OR

Run the runapp.sh 






