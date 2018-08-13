from setuptools import setup

setup(
    name="hbmqtt-auth-home-assistant",
    version="1.0.0",
    description="HBMQTT Authentication plugin for Home Assistant",
    author="Paulus Schoutsen",
    author_email='paulus@home-assistant.io',
    url="https://github.com/home-assistant/hbmqtt-auth-home-assistant",
    license='Apache License 2.0',
    packages=['hbmqtt_auth_home_assistant'],
    platforms='all',
    install_requires=[
        'hbmqtt',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'hbmqtt.broker.plugins': [
            'auth_home_assistant = hbmqtt_auth_home_assistant:HassAuthPlugin',
        ],
    }
)
