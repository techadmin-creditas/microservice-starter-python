
import logging
from services.base_database_service import base_database_service_class
from models.sample_model import sql_response_model


class data_service(base_database_service_class):

    def __init__(self) -> None:
        pass

    def bankdata_get_from_mobile(body, data_name):
        """
        This method is used to get user account data via mobile number
        """
        logging.info(f"body : {body}, data_name : {data_name}")
        sqlquery = base_database_service_class.generate_sql(body, data_name)
        result = base_database_service_class.sql_execute_select(sqlquery)
        logging.info(f"result : {result}")
        rt_obj = sql_response_model(
            kwargs= result[0]
        )
        logging.info(f"rt_obj : {rt_obj}")
        return rt_obj

    