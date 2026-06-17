class Drink:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.__price = price  # Đóng gói dữ liệu giá
        self.is_available = True

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print(">> Giá không hợp lệ!")

    def toggle_available(self):
        self.is_available = not self.is_available

    def __str__(self):
        status = "Đang bán" if self.is_available else "Ngừng bán"
        return f"{self.code:<6} | {self.name:<15} | {self.price:<7} | {status}"

# --- Dữ liệu khởi tạo ---
menu = [
    Drink("CF01", "Cà phê sữa", 35000),
    Drink("TS01", "Trà sữa matcha", 45000),
    Drink("TD01", "Trà đào cam sả", 40000)
]

# --- Các hàm chức năng ---
def show_menu():
    print("\n--- DANH SÁCH ĐỒ UỐNG ---")
    print(f"{'Mã món':<6} | {'Tên món':<15} | {'Giá bán':<7} | {'Trạng thái'}")
    print("-" * 50)
    for drink in menu:
        print(drink)

def add_drink():
    code = input("Nhập mã món: ")
    if any(d.code == code for d in menu):
        print("Mã món đã tồn tại trong hệ thống!")
        return
    
    name = input("Nhập tên món: ")
    try:
        price = int(input("Nhập giá bán: "))
        if price <= 0:
            print("Giá bán không hợp lệ!")
        else:
            menu.append(Drink(code, name, price))
            print(f"Thành công: Đã thêm món {name} vào thực đơn!")
    except ValueError:
        print("Giá bán phải là số!")

def toggle_status():
    code = input("Nhập mã món cần cập nhật: ")
    for drink in menu:
        if drink.code == code:
            drink.toggle_available()
            print(f"Đã cập nhật trạng thái món {code}.")
            print(f"Trạng thái hiện tại: {'Đang bán' if drink.is_available else 'Ngừng bán'}")
            return
    print("Không tìm thấy món có mã này!")

# --- Chạy chương trình ---
if __name__ == "__main__":
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===")
        print("1. Xem danh sách đồ uống")
        print("2. Thêm đồ uống mới")
        print("3. Cập nhật trạng thái kinh doanh")
        print("4. Thoát chương trình")
        
        choice = input("Chọn chức năng (1-4): ")
        
        if choice == '1': show_menu()
        elif choice == '2': add_drink()
        elif choice == '3': toggle_status()
        elif choice == '4':
            print("Cảm ơn bạn đã sử dụng hệ thống quản lý thực đơn Rikkei Coffee!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")