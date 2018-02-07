from distutils.core import setup

setup(name='htm-models',
      version='1.0',
      description='HTM models using nupic',
      long_description=open('README.md').read(),
      author='Christopher Messier',
      license='BSD 3-Clause',
      author_email='messier.development@gmail.com',
      url='https://github.com/messiest/htm-models',
      packages=['htm_models'],
      classifiers=['Development Status :: 1 - Planning',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Topic :: Scientific/Engineering :: Artificial Intelligence'],
      )
