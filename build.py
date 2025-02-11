import os
import shutil
import subprocess


def clean_build_artifacts():
    """Clean up build artifacts."""
    directories = ['dist', '.eggs', 'build', 'sppq.egg-info']
    for directory in directories:
        if os.path.exists(directory):
            shutil.rmtree(directory)


def build_package():
    """Build the package using build module."""
    try:
        subprocess.run(['python', '-m', 'build'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error building package: {e}")
        raise


if __name__ == '__main__':
    clean_build_artifacts()
    build_package()