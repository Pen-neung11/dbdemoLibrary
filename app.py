# ============================================================
#  app.py — เว็บแอป Flask (ทำให้เสร็จแล้ว ★ ไม่ต้องแก้)
#  รัน:  python app.py  แล้วเปิด http://127.0.0.1:5000
# ============================================================
from flask import Flask, request, jsonify, render_template
import db

app = Flask(__name__)


def safe(fn, *args, **kwargs):
    try:
        return jsonify({"ok": True, "data": fn(*args, **kwargs)})
    except NotImplementedError as e:
        return jsonify({"ok": False, "todo": True, "error": str(e)}), 501
    except Exception as e:
        return jsonify({"ok": False, "error": f"{type(e).__name__}: {e}"}), 500


@app.route("/")
def page_home():
    return render_template("index.html")

@app.route("/report")
def page_report():
    return render_template("report.html")


# ---- สมาชิก ----
@app.route("/api/members", methods=["GET"])
def members_list():
    
    filters = {k: v for k, v in request.args.items() if v}
    return safe(db.search_members, filters)

@app.route("/api/members/<int:_id>", methods=["GET"])
def member_get(_id):
    return safe(db.get_member, _id)

@app.route("/api/members", methods=["POST"])
def member_create():
    return safe(db.create_member, request.json)

@app.route("/api/members/<int:_id>", methods=["PUT"])
def member_update(_id):
    return safe(db.update_member, _id, request.json)

@app.route("/api/members/<int:_id>", methods=["DELETE"])
def member_delete(_id):
    return safe(db.delete_member, _id)

# ---- หนังสือ ----
@app.route("/api/books", methods=["GET"])
def books_list():
    filters = {k: v for k, v in request.args.items() if v}
    return safe(db.search_books, filters)

@app.route("/api/books/<int:_id>", methods=["GET"])
def book_get(_id):
    return safe(db.get_book, _id)

@app.route("/api/books", methods=["POST"])
def book_create():
    return safe(db.create_book, request.json)

@app.route("/api/books/<int:_id>", methods=["PUT"])
def book_update(_id):
    return safe(db.update_book, _id, request.json)

@app.route("/api/books/<int:_id>", methods=["DELETE"])
def book_delete(_id):
    return safe(db.delete_book, _id)

# ---- การยืม ----
@app.route("/api/loans", methods=["GET"])
def loans_list():
    filters = {k: v for k, v in request.args.items() if v}
    return safe(db.search_loans, filters)

@app.route("/api/loans/<int:_id>", methods=["GET"])
def loan_get(_id):
    return safe(db.get_loan, _id)

@app.route("/api/loans", methods=["POST"])
def loan_create():
    return safe(db.create_loan, request.json)

@app.route("/api/loans/<int:_id>", methods=["PUT"])
def loan_update(_id):
    return safe(db.update_loan, _id, request.json)

@app.route("/api/loans/<int:_id>", methods=["DELETE"])
def loan_delete(_id):
    return safe(db.delete_loan, _id)


@app.route("/api/reports/summary")
def report_summary():
    return safe(db.report_summary)

@app.route("/api/reports/popular-books")
def route_report_popular_books():
    return safe(db.report_popular_books)

@app.route("/api/reports/overdue")
def route_report_overdue():
    return safe(db.report_overdue)

@app.route("/api/reports/active-members")
def route_report_members_above_avg():
    return safe(db.report_members_above_avg)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
