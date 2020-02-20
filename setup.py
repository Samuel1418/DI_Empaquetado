from setuptools import setup

descripcion_longa = open('Readme.txt').read()
setup(
    name="Exemplo de empaquetado",
    version="0.12",
    author="Samuel",
    author_email="sgomezpintos@danielcastelao.org",
    url="https://www.danielcastelao.org",
    license="GLP",
    platforms="Unix",
    clasifiers=["Development Status :: 3 - Alpha",
                "Environment :: Console",
                "Topic :: Software Development :: Libraries",
                "License :: OSI Aproved :: GNU General Public License",
                "Programming Language :: Python :: 3.4",
                "Operating System :: Linux Ubuntu"
                ],
    description="Descripción breve del Ejemplo de empaquetado",
    long_description=descripcion_longa,
    keywords="empaquetado instalador paquetes",
    packages=['paquete', 'paquete/subPaquete'],
    # OTRA FORMA: packages = find_packages(exclude= ['*.test','*.test.*']) podemo excluír lo que queramos
    package_data={
        'paquete': 'notas.txt',
        'paquete/subPaquete': 'texto.txt'
    },
    #data_files=[('datos', ['dat/datos.txt'])],
    entry_points={'console_scripts': ['imprimeAlgo = paquete.moduloPaquete: main', ], }

)