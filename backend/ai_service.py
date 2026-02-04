from db import get_connection


def generate_ai_answer(question: str):

    conn = get_connection()
    cur = conn.cursor()

    try:

        query = f"""
        SELECT
        snowflake.cortex.complete(
          'claude-3-7-sonnet',
          '
          You are a business analyst.

          Answer clearly using data.

          Question:
          {question}

          Data:
          ' || LISTAGG(
              OBJECT_CONSTRUCT(
                'ORDER_ID', ORDER_ID,
                'AMOUNT', AMOUNT,
                'PROFIT', PROFIT,
                'QUANTITY', QUANTITY,
                'CATEGORY', CATEGORY,
                'SUBCATEGORY', SUBCATEGORY
              )::STRING,
              '\\n'
          )
        )
        FROM OUR_FIRST_DB.PUBLIC.ORDERS
        """

        cur.execute(query)

        row = cur.fetchone()

        if not row:
            return "No AI response"

        return row[0]

    finally:
        cur.close()
        conn.close()
