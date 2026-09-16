# ============================================================
#  db.py — ชั้นติดต่อฐานข้อมูล  ★★★ นิสิตเขียน SQL ในไฟล์นี้ ★★★
#  มองหาคำว่า  # TODO  ทุกฟังก์ชัน — ใช้ %s เป็น placeholder เสมอ (กัน SQL injection)
# ============================================================
import mysql.connector
import config


def get_connection():
    
    return mysql.connector.connect(
        host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASSWORD,
        database=config.DB_NAME, port=config.DB_PORT)


def run_query(sql, params=None):
    """รัน SELECT คืนผลเป็น list ของ dict"""
    conn = get_connection(); cur = conn.cursor(dictionary=True)
    cur.execute(sql, params or ()); rows = cur.fetchall()
    cur.close(); conn.close(); return rows


def run_command(sql, params=None):
    """รัน INSERT / UPDATE / DELETE แล้ว commit"""
    conn = get_connection(); cur = conn.cursor()
    cur.execute(sql, params or ()); conn.commit()
    out = {"new_id": cur.lastrowid, "affected": cur.rowcount}
    cur.close(); conn.close(); return out


def _todo(name):
    raise NotImplementedError(f"TODO: ยังไม่ได้เขียนฟังก์ชัน {name} ใน db.py")


# ---------- สมาชิก (member) ----------
def search_members(filters):
    sql = "SELECT * FROM member WHERE 1=1" 
    params = [] # gjj
    if filters.get("name"):
        sql += " AND name LIKE %s"
        params.append("%" + filters["name"] + "%")
    if filters.get("gender"):
        sql += " AND gender = %s"
        params.append(filters["gender"])
    if filters.get("member_type"):
        sql += " AND member_type = %s"
        params.append(filters["member_type"])
    sql += " ORDER BY member_id"
    return run_query(sql, params)




def get_member(member_id):
    rows = run_query("SELECT * FROM member WHERE member_id = %s", (member_id,))
    return rows[0] if rows else None


def create_member(data):
    """เพิ่ม สมาชิก ใหม่ — data มีคีย์: name, gender, email, phone, member_type"""
    
    sql = "INSERT INTO member (name, gender, email, phone, member_type) VALUES (%s, %s, %s, %s, %s)"
    params = (data["name"], data["gender"], data["email"], data["phone"], data["member_type"])
    return run_command(sql, params)



def update_member(member_id, data):
    """แก้ไข สมาชิก ตาม member_id"""
    return run_command("UPDATE member SET name=%s, gender=%s, email=%s, "
        "phone=%s, member_type=%s WHERE member_id=%s",
        (data["name"], data["gender"], data["email"],
         data["phone"], data["member_type"], member_id))
    


def delete_member(member_id):
    """ลบ สมาชิก ตาม member_id"""
    return run_command("DELETE FROM member WHERE member_id=%s", (member_id,))




# ---------- หนังสือ (book_title) ----------
def search_books(filters):
    sql = ("SELECT t.title_id, t.title, t.author, t.category, "
           "t.publish_year, COUNT(c.copy_id) AS copies "
           "FROM book_title t "
           "LEFT JOIN book_copy c ON t.title_id = c.title_id "
           "WHERE 1=1")
    
    params = []
    if filters.get("title"):
        sql += " AND t.title LIKE %s"; params.append("%"+filters["title"]+"%")
    sql += " GROUP BY t.title_id, t.title, t.author, t.category, t.publish_year"
    return run_query(sql, params)


def get_book(title_id):
    """ดึง หนังสือ 1 รายการตาม title_id (ใช้ตอนเปิดฟอร์มแก้ไข)"""
    # TODO: SELECT * FROM book_title WHERE title_id = %s แล้วคืนแถวเดียว
    rows = run_query("SELECT * FROM book_title WHERE title_id = %s", (title_id,))
    return rows[0] if rows else None

    


def create_book(data):
    """เพิ่ม หนังสือ ใหม่ — data มีคีย์: title, author, category, publish_year"""
    
    sql = "INSERT INTO book_title (title, author, category, publish_year) VALUES (%s, %s, %s, %s)"
    params = (data["title"], data["author"], data["category"], data["publish_year"])
    return run_command(sql, params)

    # TODO: INSERT INTO book_title (...) VALUES (%s, ...)
    


def update_book(title_id, data):
    """แก้ไข หนังสือ ตาม title_id"""
    # TODO: UPDATE book_title SET ... WHERE title_id=%s
    return run_command("UPDATE book_title SET title=%s, author=%s, category=%s, publish_year=%s WHERE title_id=%s",
            (data["title"], data["author"], data["category"], data["publish_year"], title_id))

    


def delete_book(title_id):
    """ลบ หนังสือ ตาม title_id"""
    # TODO: DELETE FROM book_title WHERE title_id=%s
    return run_command("DELETE FROM book_title WHERE title_id=%s", (title_id,))
    
    

# ---------- การยืม (loan) ----------
def search_loans(filters):
    sql = ("SELECT l.loan_id, m.name AS member_name, t.title, "
           "l.loan_date, l.due_date, l.return_date "
           "FROM loan l "
           "INNER JOIN member m     ON l.member_id = m.member_id "
           "INNER JOIN book_copy c  ON l.copy_id   = c.copy_id "
           "INNER JOIN book_title t ON c.title_id  = t.title_id "
           "WHERE 1=1 ORDER BY l.loan_id")
    return run_query(sql, [])


def get_loan(loan_id):
    """ดึง การยืม 1 รายการตาม loan_id (ใช้ตอนเปิดฟอร์มแก้ไข)"""
    # TODO: SELECT * FROM loan WHERE loan_id = %s แล้วคืนแถวเดียว
    _todo("get_loan")


def create_loan(data):
    """เพิ่ม การยืม ใหม่ — data มีคีย์: member_id, copy_id, loan_date, due_date, return_date"""
    # TODO: INSERT INTO loan (...) VALUES (%s, ...)
    _todo("create_loan")


def update_loan(loan_id, data):
    """แก้ไข การยืม ตาม loan_id"""
    # TODO: UPDATE loan SET ... WHERE loan_id=%s
    _todo("update_loan")


def delete_loan(loan_id):
    """ลบ การยืม ตาม loan_id"""
    # TODO: DELETE FROM loan WHERE loan_id=%s
    _todo("delete_loan")


# ============================================================
#  REPORT (รายงาน — ใช้ JOIN + GROUP BY + subquery)
# ============================================================
def report_summary():
    """ตัวเลขสรุปบนการ์ด dashboard — คืน dict เช่น {"members": 10, ...}
    คำใบ้: ใช้ COUNT(*) หลายครั้ง"""
    # TODO: นับจำนวนรวมต่าง ๆ เพื่อแสดงบนการ์ด
    _todo("report_summary")

def report_popular_books():
    """📈 หนังสือยอดนิยม (Most Borrowed)
    คำใบ้: JOIN loan→book_copy→book_title, GROUP BY title, COUNT, ORDER BY DESC, LIMIT 5"""
    # TODO: เขียน SQL รายงานนี้ (เขียน JOIN แบบ explicit INNER JOIN ... ON ...)
    _todo("report_popular_books")

def report_overdue():
    """⏰ สมาชิกค้างคืน (Overdue)
    คำใบ้: JOIN loan→member, loan→book_copy→book_title, WHERE return_date IS NULL AND due_date < CURDATE(), DATEDIFF"""
    # TODO: เขียน SQL รายงานนี้ (เขียน JOIN แบบ explicit INNER JOIN ... ON ...)
    _todo("report_overdue")

def report_members_above_avg():
    """🏅 สมาชิกที่ยืมมากกว่าค่าเฉลี่ย (Above Average)
    คำใบ้: GROUP BY member, HAVING COUNT(*) > (subquery หา AVG ของจำนวนการยืมต่อคน)"""
    # TODO: เขียน SQL รายงานนี้ (เขียน JOIN แบบ explicit INNER JOIN ... ON ...)
    _todo("report_members_above_avg")
