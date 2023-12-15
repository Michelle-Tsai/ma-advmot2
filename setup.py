import os
import setuptools

# with open(os.path.join(os.path.dirname(__file__), 'VERSION'), 'r') as f:
#     version = f.read()
with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r') as f:
    long_description = f.read()

setuptools.setup(
    # name = 名稱，盡量不要包含"-","_"
    name='maAdvMot2',
    version='0.0.1',
    description='For developers of Advantech PCIE-12xx series access to the AdvMot API.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Advantech/MA',
    author_email='michelle.tsai@advantech.com.tw',
    license='Apache License 2.0',
    keywords=['Advantech', 'PCIE-1203', 'PCIE1203']
)