from setuptools import setup

setup(
    name='my_package',
    version='0.1',
    description='한 달 거래 내역을 통해 가계부를 작성하는 패키지입니다.',
    author='이병민',
    author_email='daylyt02@gmail.com',
    packages=['my_package'],
    install_requires=[
        "pandas",
        "numpy"
    ]
)
