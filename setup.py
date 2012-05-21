from distutils.core import setup

VERSION = "0.1"

setup(
    name="jab",
    description="Just A Blog",
    long_description=open("README").read(),
    author='PythonAnywhere',
    author_email='developers@pythonanywhere.com',
    license="MIT",

    url='http://jab.pythonanywhere.com/',
    version=VERSION,
    download_url="http://jab.pythonanywhere.com/static/downloads/jab-%s.tar.gz" % (VERSION,),

    packages=["jab",],

    install_requires=[
        'south>=0.7.5',
        'django>=1.3.0'
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
