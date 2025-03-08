from setuptools import setup, find_packages

setup(
    name='mcqgenerator',
    version='0.1',
    author='Maaz',
    author_email='ai.com',
    install_requires=[
        'openai',
        'langchain',
        'streamlit',
        'python-dotenv',
        'PyPDF2',
        'transformers',
        'pretty_midi'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'project-5=main:main'
        ]
    }
)