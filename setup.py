from setuptools import setup, find_packages

setup(
    name='youtubetotext-sdk',
    version='0.1.0',
    description='Minimal Python client for YouTube-to-Text API',
    url='https://github.com/you/youtubetotext-sdk',
    author='Your Name',
    author_email='you@example.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
