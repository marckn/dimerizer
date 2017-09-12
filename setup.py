from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='dimerizer',
      version='1.0',
      description='The dimerizer script for Dimer simulations in Gromacs',
      long_description=readme(),
      classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: GNU General Public License (GPL)',
      'Natural Language :: English',
      'Programming Language :: Python :: 2.7',
      'Topic :: Scientific/Engineering :: Bio-Informatics'
      ],
      keywords='protein simulation dimer gromacs forcefield',
      url='http://github.com/marckn/dimerizer',
      author='Marco Nava',
      author_email='mark.nava@gmail.com',
      license='GPL',
      packages=['dimerizer'],
      scripts=['bin/dimerize','bin/plread','bin/tune_replicas'],
      install_requires=['re', 'itertools'],
      include_package_data=True,
      zip_safe=False)
