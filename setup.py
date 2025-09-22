from setuptools import setup
import src.todotxt as todotxt

setup(
    name='todotxt-io',
    version=todotxt.__version__,
    description='A simple Python module to parse, manipulate and write Todo.txt data',
    long_description='Everything you need to know is located somewhere ...',
    url='https://github.com/nnako/todotxt-python-io',
    author='Nnako',
    author_email='nnako@web.de',
    license='DBAD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    keywords='todotxt todo.txt file parse parser read reader',
    package_dir={"": "src"},
    py_modules=[
        'todotxt',
        ],
    install_requires=[
        'regex',
        ],
    #download_url='https://github.com/EpocDotFr/todotxtio/archive/todotxt-python-io-{version}.tar.gz'.format(version=todotxt.__version__)
)
