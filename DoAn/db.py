import pyodbc

def get_connection():
    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"
            "DATABASE=QL_Tuyen_DuLich;"
            "Trusted_Connection=yes;"
        )
        return conn
    except Exception as e:
        print("❌ Lỗi kết nối:", e)
        return None

def close_connection(conn):
    if conn:
        conn.close()

def execute_query(sql, params=None):
    conn = get_connection()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)

        conn.commit()
        close_connection(conn)
        return True
    except Exception as e:
        print("❌ Lỗi execute_query:", e)
        close_connection(conn)
        return False

def fetch_all(sql, params=None):
    conn = get_connection()
    if conn is None:
        return []

    try:
        cursor = conn.cursor()
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)

        rows = cursor.fetchall()
        close_connection(conn)
        converted = []
        for row in rows:
            converted.append(tuple(str(col) for col in row))

        return converted

    except Exception as e:
        print("❌ Lỗi fetch_all:", e)
        close_connection(conn)
        return []
