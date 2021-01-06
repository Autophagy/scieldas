# -*- coding: utf-8 -*-

from setuptools import setup

try:
    with open("README.rst", "r", encoding="utf-8") as f:
        readme = f.read()
except IOError:
    readme = ""


setup(
    name="scieldas",
    author="Mika Naylor (Autophagy)",
    author_email="mail@autophagy.io",
    description="Flask-based README badge service, inspired by shields.io",
    long_description=readme,
    packages=["scieldas"],
    install_requires=[
        "beautifulsoup4==4.7.1",
        "Flask==1.0",
        "requests==2.21.0",
        "svgwrite==1.1.11",
        "gunicorn==19.9.0",
        "CairoSVG==2.5.1",
        "requests-cache==0.4.13",
        "gevent==1.4.0",
        "SQLAlchemy==1.3.1",
        "Flask-SQLAlchemy==2.3.2",
        "psycopg2==2.8.1",
        "pydash==4.7.4",
    ],
    extras_require={
        "testing": ["black==19.10b0", "flake8==3.7.7", "mypy==0.781", "isort==4.3.15"]
    },
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    use_scm_version=True,
)
