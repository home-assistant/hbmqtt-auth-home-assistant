# HBMQTT auth plugin for Home Assistant

This is a plugin for the HBMQTT MQTT broker to allow authentication against the Home Assistant auth system.

```python
# Example broker configuration
# hass = Home Assistant instance
{
    'listeners': {
        'default': {
            'max-connections': 50000,
            'bind': '0.0.0.0:1883',
            'type': 'tcp',
        },
        'ws-1': {
            'bind': '0.0.0.0:8080',
            'type': 'ws',
        },
    },
    'topic-check': {},
    'auth': {
        'home-assistant': hass,
        'plugins': ['auth_home_assistant']
    },
}
```
