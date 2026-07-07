from setuptools import setup, find_packages

setup(
    name='speedtest-cli-tool',
    version='1.0.0',
    description='Test your internet speed from the command line',
    author='0xsan7',
    author_email='santiagojerald734@gmail.com',
    url='https://github.com/0xsan7/speedtest-cli',
    py_modules=['speedtest_cli'],
    install_requires=[
        'speedtest-cli==2.1.3',
    ],
    entry_points={
        'console_scripts': [
            'speedtest=speedtest_cli:main',
        ],
    },
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
