from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="document_ai_agents",
    version="0.1.0",  # Update the version as needed
    packages=find_packages(exclude=["tests.*", "tests"]),
    description="A set of re-usable AI agent for document processing ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=open(
        "requirements.txt"
    ).readlines(),  # Reads dependencies from file
    extras_require={"dev": open("requirements-dev.txt").readlines()},
    python_requires=">=3.9",  # Or your required Python version
    test_suite="tests",  # for running tests via 'python setup.py test'
)
