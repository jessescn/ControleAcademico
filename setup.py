from setuptools import setup, find_packages

setup(
    name='controle acadêmico CLI',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'scrapy'
    ],
    entry_points='''
        [console_scripts]
        controle=run:cli
    ''',
    python_requires='>=3',
)