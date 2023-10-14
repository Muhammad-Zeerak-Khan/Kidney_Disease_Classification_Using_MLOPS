import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = '0.0.0'    

REPO_NAME = 'Kidney_Disease_Classification_Using_MLOPS'
AUTHOR_NAME = 'Muhammad Zeerak Khan'
SRC_REPO = 'Kidney_Tumor_Classification'
AUTHOR_EMAIL = 'zeerak1994@outlook.com'

setuptools.setup(
    name= REPO_NAME,
    version= __version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Kidney Disease Classification Using MLOps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
        },
    package_dir={"":"src"},
    packaeges=setuptools.find_packages(where="src")

)