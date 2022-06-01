"""
Sample Controller - This is a sample controller built as part of the
configuration. This provides access as a simple english disctionary.

The routing for this controller is handled by the OpenAPI sepecification file.
"""

import logging
import connexion
from services import configuration_service as cs


async def get_section_key(section: str, key: str):
    """Get configuration based on section and key

    Args:
        section (str): The section to be used
        key (str): The key within the section
        entity (str, optional): Entity name, defaults to 'default'
        locale (key, optional): Language code, defaults to ''

    Returns:
        object: The given object
    """
    logging.info(f"A new call was made for: '{section}/{key}'")

    # fetch header values
    entity = connexion.request.headers.get('entity', cs.DEFAULT_ENTITY)
    accept_language = connexion.request.headers.get(
        'accept_language', cs.DEFAULT_LOCALE)

    data = cs.get_section(
        entity=str.lower(entity),
        locale=str.lower(accept_language),
        section=str.lower(section),
        key=str.lower(key)
    )

    return data


async def get_section(section: str):
    """Get configuration based on section

    Args:
        section (str): The section to be used
        entity (str, optional): Entity name, defaults to 'default'
        locale (key, optional): Language code, defaults to ''

    Returns:
        object: The given object
    """
    logging.info(f"A new call was made for: '{section}'")

    # fetch header values
    entity = connexion.request.headers.get('entity', cs.DEFAULT_ENTITY)
    accept_language = connexion.request.headers.get(
        'accept_language', cs.DEFAULT_LOCALE)

    data = cs.get_section(
        entity=str.lower(entity),
        locale=str.lower(accept_language),
        section=str.lower(section),
        key=None
    )

    return data
