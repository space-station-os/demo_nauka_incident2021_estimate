from setuptools import setup

package_name = 'demo_nauka_incident2021_estimate'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=[],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your-email@example.com',
    description='Description of your package',
    license='License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'demo_crisis = demo_nauka_incident2021_estimate.demo_crisis:main',
        ],
    },
)

