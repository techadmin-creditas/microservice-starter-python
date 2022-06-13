"""
This module represents the Helth-Check controller end-point.

This end-point is not part of the specification and is configured
directly with Flask

Example:
    To open the end-point 'http://<host>:<port>/health'
"""
from flask import request
from services import configuration_service as cs


def health():
    """
    Get the health of the service.

    Returns:
        Ok response
    """
    # Get cached information
    configs = cs.get_config_info()
    return {
        'host': request.host_url,
        'cache_state': configs
    }, 200
