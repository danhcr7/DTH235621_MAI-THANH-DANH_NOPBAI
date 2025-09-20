"""
 Nhóm hàm kiểm tra

s.isalpha() → toàn chữ cái?

s.isdigit() → toàn số?

s.isalnum() → chữ + số?

s.isspace() → toàn khoảng trắng?

s.isupper() / s.islower() → in hoa / in thường?

🔑 Nhóm chuyển đổi

s.upper() → thành in hoa.

s.lower() → thành in thường.

s.title() → viết hoa đầu mỗi từ.

s.capitalize() → viết hoa chữ đầu, còn lại thường.

s.swapcase() → đảo hoa ↔ thường.

s.strip() → bỏ khoảng trắng 2 đầu (có thể truyền ký tự).

s.lstrip() / s.rstrip() → bỏ bên trái / bên phải.

🔑 Nhóm tìm kiếm & thay thế

s.find(sub) / s.rfind(sub) → vị trí con (hoặc -1).

s.index(sub) / s.rindex(sub) → giống find nhưng lỗi nếu không thấy.

s.count(sub) → đếm số lần xuất hiện.

s.replace(old, new) → thay thế.

sub in s → kiểm tra tồn tại.

🔑 Nhóm cắt/chia/gộp

s.split(sep) → cắt thành list.

s.rsplit(sep, n) → cắt từ phải.

sep.join(list) → ghép list thành chuỗi.

s.partition(sep) → tách thành (trước, sep, sau).

s.rpartition(sep) → tách từ phải.

Slicing: s[start:stop:step].

🔑 Nhóm định dạng

s.format(...) → format chuỗi.

f"{var}" → f-string (cách hiện đại).

s.zfill(width) → thêm số 0 phía trước.

s.center(width), s.ljust(width), s.rjust(width) → căn giữa/trái/phải.
"""