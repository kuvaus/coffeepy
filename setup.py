from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='coffee',
    version='0.1.0',
    description='Coffee prevents the system from sleeping',
    long_description_content_type='text/markdown',
    long_description= readme(),
    url='https://github.com/kuvaus/coffee',
    author='Your Name',
    author_email='kuvaus@users.noreply.github.com',
    license='MIT',
    packages=find_packages(include=['coffee', 'coffee.*']),
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [
            'coffee=coffee.main:main',
        ],
    },
)

