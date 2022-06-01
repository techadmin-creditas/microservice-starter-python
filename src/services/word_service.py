"""
This module represents a sample Servcie class
"""

from src.models.sample_model import new_word_response

word_list = []


class word_service():
    """
    This class represents a simple word service
    """

    def __init__(self) -> None:
        pass

    def detail(word: str) -> tuple[new_word_response, bool]:
        """Get detail for the given word

        Args:
            word (str): The word to be processed

        Returns:
            tuple(new_word_response, bool): Word response and if word existed or not.
        """
        flg: bool = False
        if str.lower(word) in word_list:
            msg = "Hi, good try. I already have that word in my dictionary, could you give me something new."
        else:
            word_list.append(str.lower(word))
            msg = "Wow, I learn't a new word. Thanks for sharing, could you give me more."
            flg = True

        rt_obj = new_word_response(
            input=word,
            message=msg,
            word_count= len(word_list)
        )

        return rt_obj, flg
