#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Yannick Schwarz",
    author_email='yannick.schwarz@kvg.org',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Style defaults for plotly, css and more.",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='py_plot_ge',
    name='py_plot_ge',
    packages=find_packages(include=['py_plot_ge', 'py_plot_ge.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/yannickschwarz/py_plot_ge',
    version='0.1.0',
    zip_safe=False,
)
