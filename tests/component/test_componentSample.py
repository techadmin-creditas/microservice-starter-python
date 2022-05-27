import pytest
from src.controllers.health import health
from src.controllers.word_controller import get_word

#validates the status code and JSONresponse for health
def test_health():
    #act
    response = health()
    status_code=response[1]
    status_msg=response[0]
    #assert
    assert status_code == 200
    assert status_msg == {'msg': 'ok'}
    
#validates if entered word is a string    
def test_greetings_wordValidate():
    #arrange
    word="One"
    #assert
    assert isinstance(word,str)

#validates the status code and responseOutput when a new word is entered
def test_greetings_newWord():
    #arrange
    word="One"
    #act
    response = get_word(word)
    status_code=response[1]
    response_output = str(response[0]).replace("new_word_response","")
    expected_output="""(input='One', message="Wow, I learn't a new word. Thanks for sharing, could you give me more.", word_count=1)"""
    #assert
    assert response_output==expected_output
    assert status_code == 201
   
#validates the status code and responseOutput when an already existing word is entered
def test_greetings_sameWord():
    #arrange
    word="One"
    #act
    response = get_word(word)
    status_code=response[1]
    response_output = str(response[0]).replace("new_word_response","")
    expected_output="(input='One', message='Hi, good try. I already have that word in my dictionary, could you give me something new.', word_count=1)"
    #assert
    assert response_output==expected_output
    assert status_code == 200
    

    

    
