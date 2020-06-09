"""Standard library"""
import configparser

"""Third party modules"""
import yaml


"""Example of how to parse and extract values from .conf and .yaml files."""


# create configparser object and read configuration data from config.conf
config = configparser.ConfigParser()
config.read("config.conf")

# set variables equal to the configs sections and keys:
# regular value = config[section_name][key_name]
# nested value = config[section_name.nested_section_name][nested_key_name]
print("CONFIG.CONF PARSED VALUES -")
print("============================")
print("Username: ", config["user_information"]["username"])
print("Email: ", config["user_information"]["email"])
print("Verified: ", config["user_information.verification"]["verified"])


# open config.yaml to parse and create a dictionary
config = open("config.yaml")
parsed_config = yaml.load(config, Loader=yaml.FullLoader)

# set variables equal to the configs sections and keys:
# regular value = config[section_name][key_name]
# nested value = config[section_name][nested_section_name][nested_key_name]
print("\nCONFIG.YAML PARSED VALUES -")
print("============================")
print("Username: ", parsed_config["user_information"]["username"])
print("Email: ", parsed_config["user_information"]["email"])
print("Verified: ", parsed_config["user_information"]["verification"]["verified"])
