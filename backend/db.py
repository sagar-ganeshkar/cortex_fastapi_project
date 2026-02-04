import snowflake.connector
from config import SNOWFLAKE_CONFIG


def get_connection():

    return snowflake.connector.connect(
        user=SNOWFLAKE_CONFIG["user"],
        password=SNOWFLAKE_CONFIG["password"],
        account=SNOWFLAKE_CONFIG["account"],
        warehouse=SNOWFLAKE_CONFIG["warehouse"],
        database=SNOWFLAKE_CONFIG["database"],
        schema=SNOWFLAKE_CONFIG["schema"]
    )
