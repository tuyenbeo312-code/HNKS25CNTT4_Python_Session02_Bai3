      
name = input("Nhập vào tên của bệnh nhân: ")
if name == "":
    print(f"Tên không được để trống" )
elif name == " ":
    print(f"Tên không được chứa khoảng trắng" )
else :
    age = int(input("Nhập vào tuổi của bệnh nhân: "))
    if age < 0 or age > 150 :
        print(f"LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
    else :
        if age > 80 :
            result = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
        elif age < 6:
            result = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
        else :
            result = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."
        print(result)

        print("--- PHIẾU KHÁM BỆNH ĐIỆN TỬ ---")
        print(f"Họ và tên: {name}")
        print(f"Tuổi: {age}")
        print(f"Phân luồng: {result}")

    # Phân tích và thiết kế giải pháp
# Input 
# name: chuỗi ký tự, nhập từ bàn phím.
# age: số nguyên, nhập từ bàn phím.

# Output
# Thông báo lỗi nếu:
# Tên rỗng.
# Tuổi < 0 hoặc > 150.

# Nếu không lỗi:
# Thông báo phân luồng khám:
# Người cao tuổi (>80)
# Trẻ em (<6)
# Khám thường (6–79)

# 2. Đề xuất giải pháp
# Chương trình dùng:

# if–elif–else để kiểm tra lỗi đầu vào.
# Điều kiện logic (or, <, >) để xác định tuổi hợp lệ.
# Điều kiện lồng nhau để phân luồng khám sau khi dữ liệu hợp lệ.

# Luồng xử lý:
# Kiểm tra tên → báo lỗi nếu rỗng.
# Kiểm tra tuổi → báo lỗi nếu không hợp lệ.
# Nếu hợp lệ → phân loại theo nhóm tuổi → in phiếu hướng dẫn.

    
