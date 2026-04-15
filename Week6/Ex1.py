from abc import ABC, abstractmethod


class GiaKhongHopLe(Exception):
    pass

class MaHangTrungLap(Exception):
    pass



class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, gia):
        self._ma_hang = ma_hang
        self._ten_hang = ten_hang
        self.gia = gia

    @property
    def ma_hang(self):
        return self._ma_hang

    @property
    def ten_hang(self):
        return self._ten_hang

    @property
    def gia(self):
        return self._gia

    @gia.setter
    def gia(self, value):
        if value < 0:
            raise GiaKhongHopLe("Giá phải >= 0")
        self._gia = value

    @abstractmethod
    def loai_hang(self):
        pass

    @abstractmethod
    def inTTin(self):
        pass

    def __str__(self):
        return f"{self.ma_hang} - {self.ten_hang} - {self.gia} VND"

    def __eq__(self, other):
        return self.ma_hang == other.ma_hang

    def __lt__(self, other):
        return self.gia < other.gia

    def __hash__(self):
        return hash(self.ma_hang)


class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, bao_hanh, cong_suat):
        super().__init__(ma_hang, ten_hang, gia)
        self.bao_hanh = bao_hanh
        self.cong_suat = cong_suat

    def loai_hang(self):
        return "Điện máy"

    def inTTin(self):
        return f"[Điện máy] {self.ten_hang} - {self.gia} VND - BH: {self.bao_hanh} tháng"


class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, xuat_xu):
        super().__init__(ma_hang, ten_hang, gia)
        self.xuat_xu = xuat_xu

    def loai_hang(self):
        return "Sành sứ"

    def inTTin(self):
        return f"[Sành sứ] {self.ten_hang} - {self.gia} VND - Xuất xứ: {self.xuat_xu}"


class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, ngay_sx, han_sd):
        super().__init__(ma_hang, ten_hang, gia)
        self.ngay_sx = ngay_sx
        self.han_sd = han_sd

    def loai_hang(self):
        return "Thực phẩm"

    def inTTin(self):
        return f"[Thực phẩm] {self.ten_hang} - {self.gia} VND - HSD: {self.han_sd}"



class QuanLyHangHoa:
    def __init__(self, filename):
        self.filename = filename
        self.ds_hang = []

    def them_hang(self, hang):
        if any(h.ma_hang == hang.ma_hang for h in self.ds_hang):
            raise MaHangTrungLap("Mã hàng bị trùng!")
        self.ds_hang.append(hang)

    def __enter__(self):
        self.file = open(self.filename, "w", encoding="utf-8")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for h in self.ds_hang:
            self.file.write(str(h) + "\n")
        self.file.close()



if __name__ == "__main__":
    dm = HangDienMay("DM01", "Máy giặt LG", 5000000, 24, "2000W")
    ss = HangSanhSu("SS01", "Bát sứ Minh Long", 150000, "Việt Nam")
    tp = HangThucPham("TP01", "Sữa Vinamilk", 30000, "01/04/2026", "01/06/2026")

    with QuanLyHangHoa("hanghoa.txt") as ql:
        ql.them_hang(dm)
        ql.them_hang(ss)
        ql.them_hang(tp)
print(dm.inTTin())
print(ss.inTTin())
print(tp.inTTin())