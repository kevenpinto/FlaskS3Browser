from setuptools import find_packages , setup

setup(
    name='FlaskS3Project',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'arrow',
        'flask_bootstrap',
        'boto3',
        'waitress'
    ],
)
