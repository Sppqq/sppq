import os
import shutil

if os.path.exists('dist'):
    shutil.rmtree('dist')
else:
    pass

os.system('python setup.py bdist_wheel')

shutil.rmtree('.eggs', ignore_errors=True)
shutil.rmtree('build', ignore_errors=True)
shutil.rmtree('Sppq.egg-info', ignore_errors=True)