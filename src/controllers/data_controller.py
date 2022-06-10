import logging
from models.sample_model import bank_data_account_info_model
from services.data_service import data_service



async def getUser(body, data_name):
    logging.info(f"body : {body}, data_name : {data_name}")
    user_details = data_service.bankdata_get_from_mobile(body, data_name)
    logging.info(f"user_details : {user_details}")
    return user_details