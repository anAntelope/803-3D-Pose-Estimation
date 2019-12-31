from setuptools import setup


setup(
    name="803-pos-estimation",
    version="0.0.0",
    description="",
    url="https://github.com/anAntelope/803-pos-estimation",
    author="surina",
    author_email="szhao5@ualberta.ca",
    license="MIT",
    packages=["src"],
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "opencv-python",
        "tensorflow-gpu",
        "keras",
        "black==19.10b0",
        "gitdir",
        "h5py",
        "jupyter",
        "tensorflow",
        "opencv-python",
    ],
    python_requires="==3.7.*",
)
