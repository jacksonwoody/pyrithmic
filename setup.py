import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyrithmic',
    author='Jack Woodhead',
    author_email='jack.woodhead@pm.me',
    description='Python API Integration with Rithmic Protocol Buffer API',
    keywords='python rithmic',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tomchen/example_pypi_package',
    project_urls={
        'Documentation': 'https://github.com/jacksonwoody/pyrithmic',
        'Bug Reports':
        'https://github.com/jacksonwoody/pyrithmic/issues',
        'Source Code': 'https://github.com/jacksonwoody/pyrithmic',
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    # install_requires=['Pillow'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=config:main',
    # You can execute `run` in bash to run `main()` in src/config/__init__.py
    #     ],
    # },
)
