"""
===================================================================
TÀI LIỆU THIẾT KẾ LỚP BISTROTABLE
===================================================================
1. Class Attributes:
   - _vat_rate: Tỷ lệ thuế VAT áp dụng chung cho toàn bộ nhà hàng (float).

2. Instance Attributes:
   - Quyền Public: capacity (Sức chứa tối đa của bàn).
   - Quyền Private (__): __table_id (Mã bàn), __current_bill (Số tiền tạm tính).

3. Methods:
   - __init__(self, table_id, capacity): Khởi tạo mã bàn và sức chứa, __current_bill = 0.
   - @property status: Trạng thái bàn dựa trên __current_bill (>0 là Có khách, ngược lại là Trống).
   - @property total_payment: Tính tổng tiền sau thuế (hóa đơn * (1 + _vat_rate)).
   - order_dish(amount): Cộng thêm tiền vào __current_bill.
   - cancel_dish(amount): Trừ tiền khỏi __current_bill (check lỗi âm).
   - checkout(): Trả về tổng tiền, reset __current_bill về 0.
   - @classmethod update_vat_rate(new_rate): Cập nhật thuế suất chung.
   - @staticmethod is_valid_id(table_id): Kiểm tra mã bàn bắt đầu bằng "TB" và độ dài >= 3.
===================================================================
"""

class BistroTable:
    _vat_rate = 0.08  # Class Attribute: Thuế VAT 8% mặc định

    def __init__(self, table_id, capacity):
        self.__table_id = table_id.upper()
        self.capacity = capacity
        self.__current_bill = 0

    @property
    def table_id(self): return self.__table_id

    @property
    def current_bill(self): return self.__current_bill

    @property
    def status(self):
        return "Có khách (Occupied)" if self.__current_bill > 0 else "Đang trống (Available)"

    @property
    def total_payment(self):
        return self.__current_bill * (1 + BistroTable._vat_rate)

    def order_dish(self, amount):
        if amount <= 0: return False
        self.__current_bill += amount
        return True

    def cancel_dish(self, amount):
        if amount <= 0 or amount > self.__current_bill: return False
        self.__current_bill -= amount
        return True

    def checkout(self):
        total = self.total_payment
        self.__current_bill = 0
        return total

    @classmethod
    def update_vat_rate(cls, new_rate):
        cls._vat_rate = new_rate

    @staticmethod
    def is_valid_id(tid):
        return tid.upper().startswith("TB") and len(tid) >= 3

# --- Dữ liệu khởi tạo ---
table_records = [BistroTable("TB01", 4), BistroTable("TB02", 2), BistroTable("TB03", 8)]

def main():
    while True:
        print("\n===== HỆ THỐNG ĐIỀU PHỐI BÀN ĂN - RIKKEI BISTRO =====")
        print("1. Hiển thị sơ đồ & Trạng thái bàn ăn")
        print("2. Gọi món mới")
        print("3. Hủy món / Giảm trừ hóa đơn")
        print("4. Cập nhật thuế suất VAT")
        print("5. Thanh toán hóa đơn & Trả bàn")
        print("6. Thoát")
        choice = input("Chọn chức năng (1-6): ")

        if choice == '1':
            print("\n--- SƠ ĐỒ BÀN ĂN RIKKEI BISTRO ---")
            for t in table_records:
                print(f"Mã bàn: {t.table_id:<5} | Sức chứa: {t.capacity} | Tạm tính: {t.current_bill:,.0f}đ | Trạng thái: {t.status}")
        
        elif choice == '2':
            tid = input("Nhập mã bàn gọi món: ").upper()
            table = next((t for t in table_records if t.table_id == tid), None)
            if table:
                try:
                    amt = int(input("Nhập giá tiền món ăn mới: "))
                    if table.order_dish(amt): print(f">> Thành công: Đã ghi nhận {amt:,.0f}đ vào Bàn '{table.table_id}'.")
                    else: print(">> Lỗi: Vui lòng nhập số tiền là một số nguyên dương!")
                except: print(">> Lỗi: Giá trị nhập vào không hợp lệ!")
            else: print(">> Lỗi: Mã bàn không tồn tại!")

        elif choice == '3':
            tid = input("Nhập mã bàn cần hủy món: ").upper()
            table = next((t for t in table_records if t.table_id == tid), None)
            if table:
                try:
                    amt = int(input("Nhập giá trị món muốn giảm trừ: "))
                    if table.cancel_dish(amt):
                        print(f">> Thành công: Đã giảm {amt:,.0f}đ khỏi Bàn '{table.table_id}'.")
                        if table.current_bill == 0: print(">> Bàn đã chuyển về trạng thái Đang trống.")
                    else: print(">> Lỗi: Số tiền giảm trừ vượt quá giá trị hóa đơn hoặc không hợp lệ!")
                except: print(">> Lỗi: Giá trị nhập vào không hợp lệ!")
            else: print(">> Lỗi: Mã bàn không tồn tại!")

        elif choice == '4':
            print(f"[HỆ THỐNG] Thuế suất VAT hiện tại là: {BistroTable._vat_rate*100}%")
            try:
                new_vat = float(input("Nhập thuế suất mới (ví dụ 0.1 cho 10%): "))
                if 0 <= new_vat <= 0.2:
                    BistroTable.update_vat_rate(new_vat)
                    print(f">> Thông báo: Cập nhật VAT {new_vat*100}% thành công!")
                else: print(">> Lỗi: Tỷ lệ thuế không hợp lệ (0.0 - 0.2)!")
            except: print(">> Lỗi: Giá trị không hợp lệ!")

        elif choice == '5':
            tid = input("Nhập mã bàn thanh toán: ").upper()
            table = next((t for t in table_records if t.table_id == tid), None)
            if table and table.current_bill > 0:
                print(f"\n--- HÓA ĐƠN BÀN {table.table_id} ---")
                print(f"Tiền món: {table.current_bill:,.0f}đ | VAT: {BistroTable._vat_rate*100}%")
                print(f"Tổng thanh toán: {table.checkout():,.0f}đ")
                print(">> Thanh toán thành công! Bàn đã được dọn sạch.")
            elif table and table.current_bill == 0:
                print(">> Lỗi: Bàn này hiện đang trống, không có hóa đơn để thanh toán!")
            else: print(">> Lỗi: Mã bàn không tồn tại!")

        elif choice == '6':
            print("Cảm ơn bạn đã sử dụng hệ thống điều phối bàn ăn Rikkei Bistro!")
            break
        else: print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()