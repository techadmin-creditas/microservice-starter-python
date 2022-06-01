"""
This module represents the configuration service.

provides configuration data to other services.
"""

import os
import logging

from helper import file_util as futil

ENV_CONFIG_ENTITY = 'config_entity'
ENV_CONFIG_LOCALE = 'config_locale'
ENV_CONFIG_SECTION = 'config_section'

DEFAULT_ENTITY = 'default'
DEFAULT_LOCALE = 'all'
DEFAULT_CONFIG_FOLDER = f"{os.getcwd()}\\configs"

config_cache = dict()


def load_config_settings() -> None:
    """Load the configuration section

    The list is picked up from an environment variable:
    - config_entity: Entity list, including 'default'
    - config_locale: Local code, including 'all'
    - config_section: Configuration sections.
    """
    global config_cache

    env_entities = __load_env_variable(ENV_CONFIG_ENTITY, [DEFAULT_ENTITY])
    env_locale = __load_env_variable(ENV_CONFIG_LOCALE, [DEFAULT_LOCALE])
    env_sections = __load_env_variable(ENV_CONFIG_SECTION)
    
    if env_sections == None:
        raise Exception(
            f"Could not load configuration from environment variable, ensure '{ENV_CONFIG_SECTION}' is set")

    if len(config_cache) > 0:
        config_cache.clear()

    for en in env_entities:
        if futil.folder_path_exists(os.path.join(DEFAULT_CONFIG_FOLDER, en)):
            for lo in env_locale:
                if futil.folder_path_exists(os.path.join(DEFAULT_CONFIG_FOLDER, en, lo)):
                    for se in env_sections:
                        if futil.file_path_exists(os.path.join(DEFAULT_CONFIG_FOLDER, en, lo, se+".json")):
                            key_name = f"{en}-{lo}-{se}"
                            config_cache[key_name] = None
                        else:
                            logging.info(
                                f"No configuration found for entity/locale/section '{en}/{lo}/{se}'")
                else:
                    logging.info(
                        f"No configuration found for entity/locale '{en}/{lo}'")
        else:
            logging.info(f"No configuration found for entity '{en}'")


def get_config_info() -> dict:
    """Get information about the cached data

    Returns:
        dict: Cache information
    """
    global config_cache
    return {c: "empty" if config_cache[c] == None else "cached" for c in config_cache}


def get_section(entity: str, locale: str, section: str, key: str) -> object:
    """Get the configuration based on section and key

    Args:
        section (str): The section or file to be looked at
        key (str, optional): The key with the description

    Returns:
        object: The section /key value from cache.
    """
    global config_cache

    config_key = __identify_config(entity, locale, section, key)
    # Check if section is available
    if config_key == None:
        logging.info(
            f'Could not find any configuration for {entity}/{locale}/{section}')
        return None

    section_data = __get_section(config_key)

    # If key is 'None' then return the entire section
    if key == None:
        return section_data

    # Check if key is present
    if key not in section_data:
        return None

    return section_data[key]


def __load_env_variable(name, additional: list = None) -> list:
    env_variable = os.environ.get(name, None)
    logging.info(
        f"Environment configuration found for '{name}', '{env_variable}'")

    if env_variable == None:
        return additional

    lst = [x.strip() for x in str.split(env_variable, ',')]

    if additional is not None:
        lst = additional+lst

    return lst


def __get_section(config_key) -> object:
    # Check if data is cached, if not load it and return
    data = config_cache.get(config_key, None)
    if data == None:
        paths = [DEFAULT_CONFIG_FOLDER] + str.split(config_key, '-')
        file_location = os.path.join(*paths)
        config_cache[config_key] = futil.read_json(f'{file_location}.json')
        data = config_cache[config_key]

    return data


def __identify_config(entity: str, locale: str, section: str, key: str) -> str:
    possible_list = [
        f"{entity}-{locale}-{section}",
        f"{entity}-{DEFAULT_LOCALE}-{section}",
        f"{DEFAULT_ENTITY}-{locale}-{section}",
        f"{DEFAULT_ENTITY}-{DEFAULT_LOCALE}-{section}",
    ]

    for p in possible_list:
        if p in config_cache:
            return p

    return None


# Load the config as the service initilises
load_config_settings()
