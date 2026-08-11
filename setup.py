from setuptools import find_packages, setup


setup(
    name="fastapi-microservice",
    version="1.0.0",
    description="FastAPI REST API starter for Python 3.8",
    packages=find_packages(),
    python_requires=">=3.8,<3.9",
    install_requires=[
        "fastapi==0.115.14",
        "pydantic==1.10.24",
        "python-dotenv==1.0.1",
        "uvicorn[standard]==0.30.6",
    ],
)
