import os
import setuptools

with open(os.path.join(os.path.dirname(__file__), 'VERSION'), 'r') as f:
    version = f.read()
with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='ma-AdvMot2',
    version=version,
    description='For Advantech PCIE-12xx series developer to access AdvMot API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Advantech/MA',
    author_email='michelle.tsai@advantech.com.tw',
    keywords=['Advantech', 'PCIE-1203', 'PCIE1203'],
    license='Apache License 2.0'

)