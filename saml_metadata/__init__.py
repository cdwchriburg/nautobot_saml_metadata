"""App declaration for nautobot_saml_metadata.
Based on example from: https://docs.nautobot.com/projects/core/en/stable/user-guide/administration/configuration/authentication/sso/#saml-metadata
"""

# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
#from importlib import metadata

from nautobot.apps import NautobotAppConfig

class SamlMetadata(NautobotAppConfig):
    """App configuration for the nautobot_saml_metadata app."""

    name = "saml_metadata"
    verbose_name = "SAML Metadata Viewer"
    version = 0.1
    author = "Chris Burger"
    author_email = "chriburg@cdw.com"
    description = "Generates SAML Metadata package"
    config_view_name = "plugins:saml_metadata:metadata"

config = SamlMetadata  # pylint:disable=invalid-name