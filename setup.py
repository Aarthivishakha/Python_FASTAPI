from setuptools import find_packages, setup


setup(
    name="fastapi-microservice",
    version="1.0.0",
    description="FastAPI REST API starter for Python 3.6",
    packages=find_packages(),
    python_requires=">=3.6,<3.7",
    install_requires=[
        "fastapi==0.83.0",
        "pydantic==1.9.2",
        "python-dotenv==0.20.0",
        "uvicorn[standard]==0.15.0",
    ],
)
