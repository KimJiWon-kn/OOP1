from abc import ABC, abstractmethod


class TuoiKhongHopLe(Exception):
    pass

class BacKhongHopLe(Exception):
    pass


class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    @property
    def tuoi(self):
        return self._tuoi

    @tuoi.setter
    def tuoi(self, value):
        if not (18 <= value <= 65):
            raise TuoiKhongHopLe("Tuổi phải từ 18 đến 65")
        self._tuoi = value

    @abstractmethod
    def mo_ta(self):
        pass

    def __str__(self):
        return f"{self.loai_cb():<12s} | {self.ho_ten}, {self.tuoi} tuổi"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (self.ho_ten == other.ho_ten) and (self.tuoi == other.tuoi)

    def __lt__(self, other):
        return self.ho_ten < other.ho_ten



class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac

    @property
    def bac(self):
        return self._bac

    @bac.setter
    def bac(self, value):
        if not (1 <= value <= 10):
            raise BacKhongHopLe("Bậc công nhân phải từ 1 đến 10")
        self._bac = value

    def loai_cb(self):
        return "Công nhân"

    def mo_ta(self):
        return f"Công nhân {self.ho_ten}, bậc {self.bac}"


class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dt):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dt = nganh_dt

    def loai_cb(self):
        return "Kỹ sư"

    def mo_ta(self):
        return f"Kỹ sư {self.ho_ten}, ngành {self.nganh_dt}"


class NhanVienSX(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def loai_cb(self):
        return "Nhân viên SX"

    def mo_ta(self):
        return f"Nhân viên SX {self.ho_ten}, công việc: {self.cong_viec}"


class QLCB:
    def __init__(self, filename):
        self.filename = filename
        self.ds_can_bo = []

    def them_cb(self, cb):
        self.ds_can_bo.append(cb)

    def tim_kiem(self, ten):
        return [cb for cb in self.ds_can_bo if ten.lower() in cb.ho_ten.lower()]

    def hien_thi(self):
        for cb in self.ds_can_bo:
            print(cb.mo_ta())

    def __enter__(self):
        self.file = open(self.filename, "w", encoding="utf-8")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for cb in self.ds_can_bo:
            self.file.write(str(cb) + "\n")
        self.file.close()



if __name__ == "__main__":
    cn = CongNhan("Nguyễn Văn Tuấn", 30, "Nam", "Hà Nội", 5)
    ks = KySu("Trần Thị Bưởi", 40, "Nữ", "Đà Nẵng", "Xây dựng")
    nv = NhanVienSX("Lê Văn Công", 25, "Nam", "HCM", "Kế toán")

    with QLCB("canbo.txt") as ql:
        ql.them_cb(cn)
        ql.them_cb(ks)
        ql.them_cb(nv)
        ql.hien_thi()
    print(cn)
    print(ks)
    print(nv)