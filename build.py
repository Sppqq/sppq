import os
import shutil

shutil.rmtree('dist')

os.system('python setup.py bdist_wheel')

shutil.rmtree('.eggs', ignore_errors=True)
shutil.rmtree('build', ignore_errors=True)
shutil.rmtree('Sppq.egg-info', ignore_errors=True)