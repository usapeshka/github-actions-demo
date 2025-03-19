from setuptools import setup, find_packages

setup(
    name="github_actions_demo",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
