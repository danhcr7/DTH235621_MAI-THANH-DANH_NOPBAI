"""
1. Các loại lỗi khi lập trình trong Python

Trong Python (và lập trình nói chung), lỗi thường chia thành 3 loại chính:

a. Lỗi cú pháp (Syntax Error)

Xảy ra khi viết sai quy tắc ngôn ngữ Python.

Ví dụ:

print("Hello"  # quên đóng ngoặc


Chưa chạy được chương trình, Python báo lỗi ngay.

b. Lỗi logic (Logic Error)

Chương trình chạy không báo lỗi, nhưng kết quả sai vì cách viết sai ý định.

Ví dụ:

a = 5
b = 0
print(a + b)   # đáng lẽ cần chia, nhưng lại viết cộng

c. Lỗi khi chạy (Runtime Error / Exception)

Xảy ra trong lúc chạy chương trình, thường do dữ liệu hoặc tình huống không mong muốn.

Ví dụ:

x = 5 / 0   # lỗi chia cho 0

2. Cách bắt lỗi trong Python

Python cung cấp cơ chế try-except để “bắt” lỗi và xử lý thay vì để chương trình bị dừng đột ngột.

a. Cú pháp cơ bản
try:
    # Code có thể gây lỗi
    x = 5 / 0
except:
    # Code chạy khi có lỗi
    print("Có lỗi xảy ra rồi!")

b. Bắt lỗi cụ thể
try:
    x = int("abc")   # lỗi ValueError
except ValueError:
    print("Không thể ép chuỗi thành số!")

c. Dùng finally

Đảm bảo đoạn code trong finally luôn chạy, dù có lỗi hay không.

try:
    f = open("data.txt")
except FileNotFoundError:
    print("Không tìm thấy file")
finally:
    print("Đóng chương trình")

d. Tự tạo lỗi với raise
x = -5
if x < 0:
    raise ValueError("x không được âm!")


👉 Tóm gọn:

Syntax Error → Sai chính tả ngôn ngữ.

Logic Error → Code chạy nhưng sai kết quả.

Runtime Error → Chạy giữa chừng bị crash.

Dùng try-except-finally để xử lý.

"""