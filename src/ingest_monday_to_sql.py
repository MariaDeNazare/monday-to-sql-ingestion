import os
import requests
import pyodbc

MONDAY_URL = "https://api.monday.com/v2"
MONDAY_TOKEN = os.getenv("MONDAY_API_TOKEN")

SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USER = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")


def conectar_sql():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={SQL_SERVER};"
        f"DATABASE={SQL_DATABASE};"
        f"UID={SQL_USER};"
        f"PWD={SQL_PASSWORD};"
        "TrustServerCertificate=yes;"
    )


def consultar_monday(query):
    headers = {
        "Authorization": f"Bearer {MONDAY_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        MONDAY_URL,
        headers=headers,
        json={"query": query},
        timeout=60
    )

    response.raise_for_status()
    return response.json()


def get_value(nome_coluna, colunas):
    for coluna in colunas:
        if coluna["column"]["title"] == nome_coluna:
            return coluna.get("text") or None
    return None


def inserir_dados(cursor, items):
    for item in items:
        cursor.execute(
            """
            INSERT INTO dbo.ITEMS (ITEM_NAME)
            VALUES (?)
            """,
            item["name"]
        )

        for subitem in item.get("subitems", []):
            cursor.execute(
                """
                INSERT INTO dbo.SUBITEMS (
                    ITEM_NAME,
                    SUBITEM_NAME,
                    ACTIVITY,
                    WORK_DATE
                )
                VALUES (?, ?, ?, ?)
                """,
                item["name"],
                subitem["name"],
                get_value("Activity", subitem["column_values"]),
                get_value("Date", subitem["column_values"])
            )


def main():
    query = """
    query {
      boards(ids: 123456789) {
        items_page(limit: 50) {
          items {
            name
            column_values { column { title } text }
            subitems {
              name
              column_values { column { title } text }
            }
          }
        }
      }
    }
    """

    data = consultar_monday(query)
    items = data["data"]["boards"][0]["items_page"]["items"]

    with conectar_sql() as conn:
        cursor = conn.cursor()
        inserir_dados(cursor, items)
        conn.commit()

    print("Ingestão concluída com sucesso.")


if __name__ == "__main__":
    main()
