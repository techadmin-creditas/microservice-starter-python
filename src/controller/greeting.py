import logging

word_list=[]

async def get_hello(word):
    logging.info(f"A new call was made with word '{word}'")
    if str.lower(word) in word_list:
        msg = "Hi, good try. I already have that word in my dictionary, could you give me something new."
    else:
        word_list.append(str.lower(word))
        msg = "Wow, I learn't a new word. Thanks for sharing, could you give me more."

    rt_obj = {'input': word, 'message': msg, 'word_count': len(word_list)}

    return rt_obj