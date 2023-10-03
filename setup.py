from setuptools import setup, find_packages

setup(
    name="nombre-de-tu-biblioteca",
    version="0.1.0",
    description="Una descripción corta de tu biblioteca",
    author="Tu Nombre",
    author_email="tu@email.com",
    packages=find_packages(),
    install_requires=[
        "sub paquetes de pipy", "otro subpaquete y sigue asu"],
)
