from hbmqtt.plugins.authentication import BaseAuthPlugin


class HassAuthPlugin(BaseAuthPlugin):
    def __init__(self, context):
        super().__init__(context)
        try:
            self.hass = self.auth_config['home-assistant']
        except KeyError:
            self.context.logger.warning(
                "'home-assistant' key not found in auth configuration")

        if _find_provider(self.hass, 'homeassistant') is None:
            self.context.logger.warning(
                "'homeassistant' auth provider needs to be loaded in Home "
                "Assistant")

    async def authenticate(self, *args, **kwargs):
        authenticated = super().authenticate(*args, **kwargs)

        if not authenticated:
            return authenticated

        session = kwargs.get('session', None)

        if (session is None or
                session.username is None or
                session.password is None):
            return False

        # Backwards compat
        if session.username == 'homeassistant':
            legacy_prov = _find_provider(self.hass, 'legacy_api_password')

            if legacy_prov is not None:
                try:
                    legacy_prov.async_validate_login(session.password)
                    return True
                except Exception:
                    pass

        hass_prov = _find_provider(self.hass, 'homeassistant')

        if hass_prov is None:
            return False

        await hass_prov.async_initialize()

        try:
            await hass_prov.async_validate_login(
                session.username, session.password)
            return True
        except Exception:
            return False


def _find_provider(hass, prov_type):
    """Return provider for type."""
    for provider in hass.auth.auth_providers:
        if provider.type == prov_type:
            return provider
    return None
