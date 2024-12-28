from setuptools import setup, find_packages

setup(
    name='lab_ml',
    version='0.1.0',
    description='A package for data visualization and machine learning helper functions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Rohit Iyengar',
    author_email='rohitiyengar8@gmail.com',
    url='https://github.com/yourusername/your_package_name',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
        'seaborn',
        'numpy',
        'matplotlib',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
