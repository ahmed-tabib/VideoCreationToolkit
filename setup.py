from setuptools import find_packages, setup

setup(
    name='vctk',
    version='0.1.0',    
    description='video creation toolkit',
    url='https://github.com/ahmed-tabib/VideoCreationToolkit',
    author='Ahmed Tabib',
    packages=find_packages(where='src'),
    package_dir={"":"src"},
    install_requires=['ffmpeg-python'],

    classifiers=[
        'Development Status :: 1 - Planning',
    ],
)
