from setuptools import setup

setup(
    name="gfwlist2pac",
    version="1.0",
    license='MIT',
    description="convert gfwlist2pac to pac",
    author='clowwindy',
    author_email='clowwindy42@gmail.com',
    url='https://github.com/clowwindy/json_to_model',
    packages=['gfwlist2pac', 'gfwlist2pac'],
    package_data={
        'gfwlist2pac': ['LICENSE', 'templates/*']
    },
    install_requires=['setuptools'],
    entry_points="""
    [console_scripts]
    gfwlist2pac = gfwlist2pac.main
    """,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)