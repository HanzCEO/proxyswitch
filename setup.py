from setuptools import find_packages, setup

about = dict()
with open('proxyswitch/about.py') as fp:
        exec(fp.read, about)

setup(
        name='proxyswitch',
        version=about['__version__'],
        description='Python requests adapter for proxy stuff',
        author='Hanz',
        author_email='hanz@godot.id',
        url='https://github.com/HanzCEO/proxyswitch',
        packages=find_packages()
)