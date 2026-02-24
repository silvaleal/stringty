from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='stringty',
    version='0.0.2.2',
    license='MIT License',
    author='silvaleal',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='lealsilva.ctt@outlook.com',
    keywords='redacty',
    description=u'Uma biblioteca PYTHON para editar conteúdo de arquivos, substitua todo o conteúdo ou adicione algo a mais.',
    packages=['stringty'],
    install_requires=[''],
    )