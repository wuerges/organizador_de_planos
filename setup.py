from distutils.core import setup

setup(
    name='OrganizadorDePlanos',
    version='0.1.0',
    author='Emilio Wuerges',
    author_email='wuerges@gmail.com',
    packages=['organizador'],
    scripts=['bin/organizador.py'],
    url='http://pypi.python.org/pypi/OrganizadorDePlanos/',
    license='LICENSE.txt',
    description='Organizador de Planos de ensino da UFFS.',
    long_description=open('README.md').read(),
    install_requires=[
        "odfpy >= 1.3.0",
    ],
)
