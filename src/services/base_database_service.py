from dataclasses import dataclass
import logging
import mysql.connector
from mysql.connector import Error


@dataclass
class base_database_service_class():
    """
    This is the base database service, this class will house various sql methods needed
    for various sql operations
    """

    @staticmethod
    def sql_execute_select(sql):
        logging.info(f"sql : {sql}")
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='indusindcollection',
                                                 user='root',
                                                 password='root')
            if connection.is_connected():
                cursor = connection.cursor(sql)
                cursor.execute(sql)
                columns = cursor.description
                result = [{columns[index][0]:column for index, column in enumerate(
                    value)} for value in cursor.fetchall()]
        except Error as e:
            logging.info("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
        return result


    @staticmethod
    def generate_sql(body, data_name):
        logging.info(f"body : {body}, data_name : {data_name}")
        table_name = data_name
        columns = ", ".join(body.get("columns"))
        conditions = body.get("conditions")
        condition_values = body.get("condition_values")
        operation = body.get("operation")
        join = body.get("join")
        where_clause = []

        if join is not None:
            join_table = body.get("join")
            join_column = body.get("joinon")
            for i in range(len(conditions)):
                where_clause.append(conditions[i])
                where_clause.append("=")
                where_clause.append(f"'{condition_values[i]}'")
                where_clause.append(operation)

            where_condition = (" ".join(where_clause[:-1]))

            sql = f"SELECT {columns} FROM {table_name} JOIN {join_table} ON {table_name}.{join_column} = {join_table}.{join_column} WHERE {where_condition}"

        else:
            for i in range(len(conditions)):
                where_clause.append(conditions[i])
                where_clause.append("=")
                where_clause.append(f"'{condition_values[i]}'")
                where_clause.append(operation)

            where_condition = (" ".join(where_clause[:-1]))

            sql = f"SELECT {columns} FROM {table_name} WHERE {where_condition}"

        return sql
