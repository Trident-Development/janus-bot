import os


class OSEnvKeys:
    """
    Containing the names of the OS environment keys
    """

    DISCORD_TOKEN = "DISCORD_TOKEN"

    TRIDENT_IMG_URL = "TRIDENT_IMG_URL"
    LINKEDIN_IMG_URL = "LINKEDIN_IMG_URL"
    GLASSDOOR_IMG_URL = "GLASSDOOR_IMG_URL"

    LINKEDIN_ACCOUNT = "LINKEDIN_ACCOUNT"
    LINKEDIN_PASSWORD = "LINKEDIN_PASSWORD"

    @classmethod
    def to_list(cls):
        """Return a list of the OS environment keys"""

        def condition(attr) -> bool:
            return not callable(getattr(cls, attr)) and not attr.startswith("__")

        return [getattr(cls, attr) for attr in dir(cls) if condition(attr)]


# Discord credentials
DISCORD_TOKEN = os.environ.get(OSEnvKeys.DISCORD_TOKEN)

# Images URLs
TRIDENT_IMG_URL = os.environ.get(OSEnvKeys.TRIDENT_IMG_URL)
LINKEDIN_IMG_URL = os.environ.get(OSEnvKeys.LINKEDIN_IMG_URL)
GLASSDOOR_IMG_URL = os.environ.get(OSEnvKeys.GLASSDOOR_IMG_URL)

LINKEDIN_ACCOUNT = os.environ.get(OSEnvKeys.LINKEDIN_ACCOUNT)
LINKEDIN_PASSWORD = os.environ.get(OSEnvKeys.LINKEDIN_PASSWORD)
