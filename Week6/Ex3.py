import math


class MauSoBangKhong(Exception):
    pass


class PhanSo:
    def __init__(self, tu, mau):
        self.tu_so = tu
        self.mau_so = mau

    @property
    def tu_so(self):
        return self._tu

    @tu_so.setter
    def tu_so(self, value):
        self._tu = value

    @property
    def mau_so(self):
        return self._mau

    @mau_so.setter
    def mau_so(self, value):
        if value == 0:
            raise MauSoBangKhong("Mẫu số không được bằng 0!")
        self._mau = value


    def __add__(self, other):
        return PhanSo(self.tu_so * other.mau_so + other.tu_so * self.mau_so,
                      self.mau_so * other.mau_so)

    def __sub__(self, other):
        return PhanSo(self.tu_so * other.mau_so - other.tu_so * self.mau_so,
                      self.mau_so * other.mau_so)

    def __mul__(self, other):
        return PhanSo(self.tu_so * other.tu_so, self.mau_so * other.mau_so)

    def __truediv__(self, other):
        return PhanSo(self.tu_so * other.mau_so, self.mau_so * other.tu_so)


    def __eq__(self, other):
        return self.tu_so * other.mau_so == other.tu_so * self.mau_so

    def __lt__(self, other):
        return self.tu_so * other.mau_so < other.tu_so * self.mau_so

    def __gt__(self, other):
        return self.tu_so * other.mau_so > other.tu_so * self.mau_so


    def is_toi_gian(self):
        return math.gcd(self.tu_so, self.mau_so) == 1

    def toi_gian(self):
        ucln = math.gcd(self.tu_so, self.mau_so)
        return PhanSo(self.tu_so // ucln, self.mau_so // ucln)


    def __str__(self):
        ps = self.toi_gian()
        if ps.mau_so == 1:
            return str(ps.tu_so)
        return f"{ps.tu_so}/{ps.mau_so}"

    def __repr__(self):
        return f"PhanSo({self.tu_so}, {self.mau_so})"

    def __hash__(self):
        ps = self.toi_gian()
        return hash((ps.tu_so, ps.mau_so))



if __name__ == "__main__":
    ds = [PhanSo(2, 4), PhanSo(3, 9), PhanSo(5, 10), PhanSo(7, 1)]

    print("Danh sách phân số (tối giản):")
    for ps in ds:
        print(ps)

    print("\nSắp xếp tăng dần:")
    for ps in sorted(ds):
        print(ps)


    ps1 = PhanSo(1, 2)
    ps2 = PhanSo(1, 3)
    print("\nPhép toán:")
    print(f"{ps1} + {ps2} = {ps1 + ps2}")
    print(f"{ps1} - {ps2} = {ps1 - ps2}")
    print(f"{ps1} * {ps2} = {ps1 * ps2}")
    print(f"{ps1} / {ps2} = {ps1 / ps2}")