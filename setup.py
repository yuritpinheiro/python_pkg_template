from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='example_pkg',
      version='0.1',
      description='Example Package',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='alarm',
      url='http://github.com/jonh-doe',
      author='Jonh Doe',
      author_email='jonh_doe@email.com',
      license='MIT',
      packages=['example_pkg'],
      install_requires=[
          'numpy',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['example-command=example_pkg.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
