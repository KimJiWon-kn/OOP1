# ===== UML =====
HangHoa
- ma_hang
- ten_hang
- nha_sx
- gia

+ xuat()

   ↑ kế thừa

HangDienMay
- bao_hanh
- dien_ap
- cong_suat

HangSanhSu
- loai_nguyen_lieu

HangThucPham
- ngay_sx
- ngay_het_han


# ===== Lớp cha =====
class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.nha_sx = nha_sx
        self.gia = gia

    def xuat(self):
        print(f"Ma hang: {self.ma_hang}")
        print(f"Ten hang: {self.ten_hang}")
        print(f"Nha san xuat: {self.nha_sx}")
        print(f"Gia: {self.gia}")


# ===== Hàng điện máy =====
class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, bao_hanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.bao_hanh = bao_hanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

    def xuat(self):
        super().xuat()
        print(f"Bao hanh: {self.bao_hanh}")
        print(f"Dien ap: {self.dien_ap}")
        print(f"Cong suat: {self.cong_suat}")


# ===== Hàng sành sứ =====
class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.loai_nguyen_lieu = loai_nguyen_lieu

    def xuat(self):
        super().xuat()
        print(f"Loai nguyen lieu: {self.loai_nguyen_lieu}")


# ===== Hàng thực phẩm =====
class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_het_han):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.ngay_sx = ngay_sx
        self.ngay_het_han = ngay_het_han

    def xuat(self):
        super().xuat()
        print(f"Ngay san xuat: {self.ngay_sx}")
        print(f"Ngay het han: {self.ngay_het_han}")


# ===== Main: tạo mỗi loại 1 sản phẩm =====
if __name__ == "__main__":
    h1 = HangDienMay("DM01", "Tivi", "Sony", 10000000, 24, 220, 150)
    h2 = HangSanhSu("SS01", "Bat", "Bat Trang", 50000, "Dat set")
    h3 = HangThucPham("TP01", "Sua", "Vinamilk", 30000, "01/01/2024", "01/01/2025")

    print("=== Hang dien may ===")
    h1.xuat()

    print("=== Hang sanh su ===")
    h2.xuat()

    print("=== Hang thuc pham ===")
    h3.xuat()
    