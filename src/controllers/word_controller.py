"""
Sample Controller - This is a sample controller built as part of the
starter-kit. This provides access as a simple english disctionary.

The routing for this controller is handled by the OpenAPI sepecification file.
"""

import logging
from models.sample_model import new_word_response
from services.word_service import word_service


async def get_word(word: str) -> new_word_response:
    """Get more information about the given word

    Args:
        word (str): The word to be looked up

    Returns:
        object (new_word_response): The description about the given work
    """
    logging.info(f"A new call was made with word '{word}'")
    word_detail, is_new = word_service.detail(word)

    rt_code = 200
    if is_new:
        rt_code = 201

    return word_detail, rt_code
    
    
