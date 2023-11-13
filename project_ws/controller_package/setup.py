from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'controller_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vinicioslugli',
    maintainer_email='vinicioslugli@gmail.com',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node = controller_package.node:main'
        ],
    },
)
