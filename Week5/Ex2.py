# ===== UML =====
NhanVien
- ma_nv
- ho_ten
- nam_sinh
- gioi_tinh
- dia_chi
- he_so_luong

+ nhap()
+ xuat()
+ tinh_luong()

        ↑ kế thừa

CongTacVien
- thoi_han_hop_dong
- phu_cap

NhanVienChinhThuc
- vi_tri_cong_viec
- thuong

TruongPhong
- ngay_bat_dau
- phu_cap_quan_ly



# ===== Lớp cha =====
class NhanVien:
    def __init__(self):
        self.ma_nv = ""
        self.ho_ten = ""
        self.nam_sinh = 0
        self.gioi_tinh = ""
        self.dia_chi = ""
        self.he_so_luong = 0

    def nhap(self):
        self.ma_nv = input("Ma NV: ")
        self.ho_ten = input("Ho ten: ")
        self.nam_sinh = int(input("Nam sinh: "))
        self.gioi_tinh = input("Gioi tinh: ")
        self.dia_chi = input("Dia chi: ")
        self.he_so_luong = float(input("He so luong: "))

    def tinh_luong(self):
        return self.he_so_luong * 1000  # đơn giản

    def xuat(self):
        print(f"Ma NV: {self.ma_nv}")
        print(f"Ho ten: {self.ho_ten}")
        print(f"Nam sinh: {self.nam_sinh}")
        print(f"Gioi tinh: {self.gioi_tinh}")
        print(f"Dia chi: {self.dia_chi}")
        print(f"He so luong: {self.he_so_luong}")
        print(f"Luong: {self.tinh_luong()}")


# ===== Công tác viên =====
class CongTacVien(NhanVien):
    def __init__(self):
        super().__init__()
        self.thoi_han_hop_dong = ""
        self.phu_cap = 0

    def nhap(self):
        super().nhap()
        self.thoi_han_hop_dong = input("Thoi han hop dong (3 thang / 6 thang / 1 nam): ")
        self.phu_cap = float(input("Phu cap: "))

    def tinh_luong(self):
        return super().tinh_luong() + self.phu_cap


# ===== Nhân viên chính thức =====
class NhanVienChinhThuc(NhanVien):
    def __init__(self):
        super().__init__()
        self.vi_tri = ""
        self.thuong = 0

    def nhap(self):
        super().nhap()
        self.vi_tri = input("Vi tri cong viec: ")
        self.thuong = float(input("Thuong: "))

    def tinh_luong(self):
        return super().tinh_luong() + self.thuong


# ===== Trưởng phòng =====
class TruongPhong(NhanVien):
    def __init__(self):
        super().__init__()
        self.ngay_bat_dau = ""
        self.phu_cap_quan_ly = 0

    def nhap(self):
        super().nhap()
        self.ngay_bat_dau = input("Ngay bat dau quan ly: ")
        self.phu_cap_quan_ly = float(input("Phu cap quan ly: "))

    def tinh_luong(self):
        return super().tinh_luong() + self.phu_cap_quan_ly


# ===== Main =====
if __name__ == "__main__":
    print("=== Nhap cong tac vien ===")
    ctv = CongTacVien()
    ctv.nhap()

    print("=== Nhap nhan vien chinh thuc ===")
    nvct = NhanVienChinhThuc()
    nvct.nhap()

    print("=== Nhap truong phong ===")
    tp = TruongPhong()
    tp.nhap()

    print("=== Xuat thong tin ===")
    print("--- Cong tac vien ---")
    ctv.xuat()

    print("--- Nhan vien chinh thuc ---")
    nvct.xuat()

    print("--- Truong phong ---")
    tp.xuat()