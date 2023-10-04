import io
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    about = {}
    with io.open(
            os.path.join(HERE, "tutoribl_openedx_tutor", "__about__.py"),
            "rt",
            encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()

setup(
    name="tutoribl_openedx_tutor",
    version=ABOUT["__version__"],
    url="https://github.com/AwuyaDaniel/IBL-openedx-tutor.git",
    project_urls={
        "Code": "https://github.com/AwuyaDaniel/IBL-openedx-tutor.git",
        "Issue tracker": "https://github.com/AwuyaDaniel/IBL-openedx-tutor.git/issues",
    },
    license="AGPLv3",
    author="Awuya Daniel",
    description="IBL-openedx-tutor plugin for Tutor",
    long_description=load_readme(),
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=["tutor"],
    keywords="Django, Open edX, Plugin",
    entry_points={
        "tutor.plugin.v1": [
            "IBL-openedx-tutor = tutoribl_openedx_tutor.plugin"
        ],
        "lms.djangoapp": [
            "tutoribl_openedx_tutor = tutoribl_openedx_tutor.apps:IblOpenedxAppConfig",
        ],
        "cms.djangoapp": [
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
