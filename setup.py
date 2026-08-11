from setuptools import find_packages, setup


setup(
    name="fastapi-microservice",
    version="1.0.0",
    description="FastAPI REST API starter for Python 3.7",
    packages=find_packages(),
    python_requires=">=3.7,<3.8",
    install_requires=[
        "fastapi==0.103.2",
        "pydantic==1.10.13",
        "python-dotenv==0.21.1",
        "uvicorn[standard]==0.22.0",
    ],
)
