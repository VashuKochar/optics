from setuptools import setup, find_packages

setup(
    name="optics",
    version="0.1.1",
    author="Vashishtha",
    description="Simulator for quantum optics",
    package_dir={'optics': 'src'},
    install_requires=[
        'wheel',
        'scipy',
        'sympy',
        'numpy',
	    'matplotlib',
        'qutip'
    ],
)
