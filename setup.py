from setuptools import find_packages, setup


if __name__ == '__main__':
    setup(
        name='gazetr',
        version='0.1.3',
        description='GazeTR by yihuacheng',
        long_description='This repo is a fork from https://github.com/yihuacheng/GazeTR',
        # long_description_content_type='text/markdown',
        author='Akmal Mukhsimov',
        author_email='aka.mukhsimov@gmail.com',
        keywords='computer vision, object detection, eye tracking',
        url='https://github.com/amukhsimov/GazeTR',
        packages=['gazetr'],
        include_package_data=True,
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
        ],
        license='Apache License 2.0',
        install_requires=[
        ],
    )
