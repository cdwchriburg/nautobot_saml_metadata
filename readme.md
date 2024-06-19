# nautobot_saml_metadata

This is a basic plugin that gives a user-friendly way to generate SAML metadata for Nautobot.
The actual generation of this data is based on the example in nautobot documentation:

https://docs.nautobot.com/projects/core/en/stable/user-guide/administration/configuration/authentication/sso/#saml-metadata


## Installation
1. Install from git using pip
```
pip3 install git+https://github.com/cdwchriburg/nautobot_saml_metadata
```

2. Add to `local_requirements.txt`:
```
nautobot_saml_metadata @ git+https://github.com/cdwchriburg/nautobot_saml_metadata
```

3. Edit `nautobot_config.py` and add `saml_metadata` to plugins list:
```
PLUGINS = ['foo', 'bar', 'saml_metadata']
```

4. Configure the SAML parameters, certificate, etc as per the Nautobot SSO/SAML config guide & `python-social-auth` documentation


## Usage
To generate the XML metadata to setup SAML on an authentication provider:
1. Login to Nautobot
2. Navigate to Apps > Installed Apps
3. Click the configure icon next to SAML Metadata Viewer app
4. Save the metadata page as an XML file.
