from setuptools import setup, find_packages

setup(
    name='body_visualizer',
    version='1.1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    author=['Nima Ghorbani',],
    author_email=['nghorbani@tuebingen.mpg.de'],
    maintainer='Nima Ghorbani',
    maintainer_email='nghorbani@tuebingen.mpg.de',
    url='https://github.com/nghorbani/body_visualizer',
    description='Visualizer for SMPL body model family.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        # 이미지 처리
        "scikit-image",
        "imageio",
        "moviepy",
        "opencv-python==4.5.1.48",
        
        # 3D 렌더링
        "pyrender==0.1.45",
        "trimesh==3.9.29",
        "PyOpenGL @ git+https://github.com/mmatl/pyopengl.git",
        "PyOpenGL_accelerate",
        
        # 데이터 처리
        "numpy",
        "colour",
        "matplotlib==3.2.2",
        "tqdm",
        
        # 유틸리티
        "loguru"
    ],
    dependency_links=[],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Researchers",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)
