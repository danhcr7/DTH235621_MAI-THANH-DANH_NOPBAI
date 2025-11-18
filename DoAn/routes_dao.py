import db

def list_all():
    sql = "SELECT MaTuyen, TenTuyen, KhuVuc, SoNgay, MoTa FROM TuyenDuLich ORDER BY IDTuyen DESC"
    return db.fetch_all(sql)

def insert_into_database(ma, ten, kv, songay, mota):
    sql = """
        INSERT INTO TuyenDuLich (MaTuyen, TenTuyen, KhuVuc, SoNgay, MoTa)
        VALUES (?, ?, ?, ?, ?)
    """
    return db.execute_query(sql, (ma, ten, kv, songay, mota))

def delete_by_ma(ma):
    sql = "DELETE FROM TuyenDuLich WHERE MaTuyen = ?"
    return db.execute_query(sql, (ma,))

def delete_all():
    sql = "DELETE FROM TuyenDuLich"
    return db.execute_query(sql)

def search(keyword):
    sql = """
        SELECT MaTuyen, TenTuyen, KhuVuc, SoNgay, MoTa
        FROM TuyenDuLich
        WHERE MaTuyen LIKE ? OR TenTuyen LIKE ? OR KhuVuc LIKE ? OR MoTa LIKE ?
    """
    p = f"%{keyword}%"
    return db.fetch_all(sql, (p, p, p, p))
