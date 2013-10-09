from setuptools import setup
try:
    import multiprocessing
except ImportError:
    pass


setup(
    name='httpie-negotiate',
    description='SPNEGO (GSS Negotiate) auth plugin for HTTPie.',
    long_description=open('README.rst').read().strip(),
    version='1.0.0',
    author='Nan Zou',
    author_email='nanzou@gmail.com',
    license='BSD',
    url='https://github.com/ndzou/httpie-negotiate',
    download_url='https://github.com/ndzou/httpie-negotiate',
    py_modules=['httpie_negotiate'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_negotiate = httpie_negotiate:NegotiateAuthPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.7.0',
        'requests_kerberos'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Environment :: Plugins',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
