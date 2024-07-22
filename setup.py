from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required_packages =  f.read().splitlines()

print(required_packages)

setup (
    name='real_weather_checker',
    version='1.0',
    description='Weather checker for chosen location which collates and averages weather from different sources',
    author='dylan',
    packages=find_packages(),
    install_requires=required_packages
)