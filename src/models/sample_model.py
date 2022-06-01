"""
This is the model for Words
"""
from src.models.base import base_model, dataclass


@dataclass
class new_word_response(base_model):
    """
    This class represents the New Word Response
    """
    input: str = ""
    message: str = ""
    word_count: int = 0

    def __init__(self, **kwargs) -> None:
        super().__init__()

        self.input = kwargs.get("input", "")
        self.message = kwargs.get("message", "")
        self.word_count = kwargs.get("word_count", 0)
