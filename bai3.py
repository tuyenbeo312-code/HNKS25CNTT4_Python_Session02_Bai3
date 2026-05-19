name = input("Nhập vào tên của bệnh nhân: ")
age = int(input("Nhập vào tuổi của bệnh nhân: "))

if name == "" :
    print(f"Tên không được để trống" )
elif age < 0 or age > 150 :
    print(f"LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
else :
    if age > 80 :
        print(f"ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa.")
    elif age < 6:
        print(f"ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi.")
    else :
        print(f"KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh.")


# Phân tích chương trình

# đầu vào
# name: tên bệnh nhân 
# age: tuổi bệnh nhân 

# đầu ra
# Báo lỗi nếu tên rỗng hoặc tuổi không hợp lệ.
# Nếu hợp lệ thì phân loại bệnh nhân theo độ tuổi.

# Giải pháp
# Dùng if-elif-else để:
# - Kiểm tra dữ liệu nhập vào
# - Phân loại bệnh nhân

# Luồng xử lý
# 1. Nhập tên và tuổi
# 2. Kiểm tra dữ liệu
# 3. Nếu hợp lệ thì phân luồng khám
