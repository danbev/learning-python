from distutils.core import setup, Extension

setup(name = 'something', version = '1.0',  \
   ext_modules = [Extension('something', ['something.c'])])
