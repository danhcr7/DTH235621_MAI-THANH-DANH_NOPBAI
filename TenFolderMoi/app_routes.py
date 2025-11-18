from tkinter import *
from tkinter import ttk, messagebox
import routes_dao

root = Tk()
root.title("Quản lý Tuyến Du Lịch")
root.geometry("1200x650")
root.resizable(True, True)

# ====================== HÀM XỬ LÝ ==========================

def xoa_form():
    entry_ma.delete(0, END)
    entry_ten.delete(0, END)
    cbb_kv.set("")
    entry_songay.delete(0, END)
    entry_mota.delete(0, END)
    entry_ma.focus()

def them_moi():
    xoa_form()
    entry_ma.focus()

def load_data():
    for item in tree.get_children():
        tree.delete(item)
    rows = routes_dao.list_all()
    for r in rows:
        tree.insert("", END, values=r)

def luu_du_lieu():
    ma = entry_ma.get()
    ten = entry_ten.get()
    kv = cbb_kv.get()
    songay = entry_songay.get()
    mota = entry_mota.get()

    if ma == "" or ten == "":
        messagebox.showwarning("Thiếu dữ liệu", "Mã Tuyến và Tên Tuyến không được để trống!")
        return

    if not songay.isdigit() or int(songay) <= 0:
        messagebox.showwarning("Sai dữ liệu", "Số Ngày phải là số nguyên dương!")
        entry_songay.focus()
        return

    ok = routes_dao.insert_into_database(ma, ten, kv, int(songay), mota)
    if ok:
        messagebox.showinfo("Đã lưu", "Dữ liệu đã lưu vào CSDL!")
        load_data()
    else:
        messagebox.showerror("Lỗi", "Không thể lưu dữ liệu!")

def xoa_1_dong():
    ma = entry_ma.get()
    if ma == "":
        messagebox.showwarning("Thiếu mã", "Hãy nhập Mã Tuyến cần xóa!")
        return

    if messagebox.askyesno("Xóa?", f"Bạn chắc chắn muốn xóa {ma}?"):
        routes_dao.delete_by_ma(ma)
        load_data()
        xoa_form()

def xoa_sach_CSDL():
    if messagebox.askyesno("Xóa sạch?", "Bạn có chắc muốn xóa TẤT CẢ CSDL không?"):
        routes_dao.delete_all()
        load_data()
        xoa_form()

def clear_tree():
    for item in tree.get_children():
        tree.delete(item)

def tim_kiem(event=None):
    key = entry_search.get()
    rows = routes_dao.search(key)

    clear_tree()
    for r in rows:
        tree.insert("", END, values=r)

# ====================== GIAO DIỆN ==========================

# FRAME 1 – FORM
frm1 = Frame(root, bg="red", height=200)
frm1.pack(fill="x")

Label(frm1, text="Mã Tuyến:", bg="red", fg="white").place(x=20, y=20)
entry_ma = Entry(frm1, width=40)
entry_ma.place(x=120, y=20)

Label(frm1, text="Tên Tuyến:", bg="red", fg="white").place(x=600, y=20)
entry_ten = Entry(frm1, width=40)
entry_ten.place(x=700, y=20)

Label(frm1, text="Khu Vực:", bg="red", fg="white").place(x=20, y=80)
cbb_kv = ttk.Combobox(frm1, values=["Miền Nam", "Miền Trung", "Miền Bắc"], state="readonly", width=37)
cbb_kv.place(x=120, y=80)

Label(frm1, text="Số Ngày:", bg="red", fg="white").place(x=600, y=80)
entry_songay = Entry(frm1, width=40)
entry_songay.place(x=700, y=80)

Label(frm1, text="Mô Tả:", bg="red", fg="white").place(x=20, y=140)
entry_mota = Entry(frm1, width=100)
entry_mota.place(x=120, y=140)

# FRAME 2 – BUTTON
frm2 = Frame(root, bg="lightblue", height=100)
frm2.pack(fill="x")

btn_w = 150
btn_h = 40
space = 20

Button(frm2, text="Thêm Mới", command=them_moi).place(x=20, y=30, width=btn_w, height=btn_h)
Button(frm2, text="Lưu", command=luu_du_lieu).place(x=20+1*(btn_w+space), y=30, width=btn_w, height=btn_h)
Button(frm2, text="Cập Nhật").place(x=20+2*(btn_w+space), y=30, width=btn_w, height=btn_h)
Button(frm2, text="Xóa", command=xoa_1_dong).place(x=20+3*(btn_w+space), y=30, width=btn_w, height=btn_h)
Button(frm2, text="Tải Lại", command=load_data).place(x=20+4*(btn_w+space), y=30, width=btn_w, height=btn_h)
Button(frm2, text="Xóa CSDL", command=xoa_sach_CSDL).place(x=20+5*(btn_w+space), y=30, width=btn_w, height=btn_h)

Label(frm2, text="Tìm:", bg="lightblue").place(x=20+6*(btn_w+space), y=15)
entry_search = Entry(frm2, width=25)
entry_search.place(x=20+6*(btn_w+space), y=45, height=30)
entry_search.bind("<KeyRelease>", tim_kiem)

# FRAME 3 – TREEVIEW
frm3 = Frame(root)
frm3.pack(fill="both", expand=True)

columns = ("Mã Tuyến", "Tên Tuyến", "Khu Vực", "Số Ngày", "Mô Tả")
tree = ttk.Treeview(frm3, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)

tree.column("Mã Tuyến", width=100)
tree.column("Tên Tuyến", width=250)
tree.column("Khu Vực", width=150)
tree.column("Số Ngày", width=80)
tree.column("Mô Tả", width=350)

scroll_y = Scrollbar(frm3, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scroll_y.set)

tree.pack(side="left", fill="both", expand=True)
scroll_y.pack(side="right", fill="y")

load_data()
entry_ma.focus()

root.mainloop()
