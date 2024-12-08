from sqlalchemy import Column, Integer, String, Float, Enum, Boolean, DateTime, ForeignKey
from mybookapp import db,app
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as UserEnum


class UserRole(UserEnum):
    ADMIN = 1
    USER = 2
class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

class TaiKhoan(BaseModel):
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100))
    email = Column(String(50))
    active = Column(Boolean, default=True)
    joined_date = Column(DateTime, default=datetime.now())
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.username


class Sach(BaseModel):
    __tablename__ = 'sach'
    tenSach = Column(String(50), nullable=False)
    theLoai = Column(String(30), nullable=False)
    soLuong = Column(Integer, nullable=False)
    donGia = Column(Float, nullable=False)
    maTheLoai = Column(Integer, ForeignKey('loai_sach.id'), nullable=False)
    loai = relationship("LoaiSach", back_populates="sach")

class LoaiSach(BaseModel):
    __tablename__ = 'loai_sach'
    tenTheLoai = Column(String(50), nullable=False)
    sach = relationship("Sach", back_populates="loai")

class NguoiDung(BaseModel):
    __tablename__ = 'nguoi_dung'
    hoTen = Column(String(100), nullable=False)
    gioiTinh = Column(Boolean, nullable=False)
    SDT = Column(String(10), nullable=False)
    email = Column(String(50), nullable=False)

class ChiTietDatSach(BaseModel):
    __tablename__ = 'chi_tiet_dat_sach'
    maKhachHang = Column(Integer, ForeignKey('nguoi_dung.id'), nullable=False)
    maSach = Column(Integer, ForeignKey('sach.id'), nullable=False)
    ngayDat = Column(DateTime, nullable=False)
    soLuong = Column(Integer, nullable=False)
    giaTien = Column(Float, nullable=False)

class HoaDon(BaseModel):
    __tablename__ = 'hoa_don'
    maChiTiet = Column(Integer, ForeignKey('chi_tiet_dat_sach.id'), nullable=False)
    ngayLapHoaDon = Column(DateTime, nullable=False)


class QuyDinh(BaseModel):
    __tablename__ = 'quy_dinh'
    tenQD = Column(String(100), nullable=False)
    ngayTao = Column(DateTime, nullable=False)
    ngaySua = Column(DateTime, nullable=False)
    moTaQD = Column(String(255), nullable=False)

class BaoCaoThang(BaseModel):
    __tablename__ = 'bao_cao_thang'
    doanhThu = Column(Float, nullable=False)
    tiLe = Column(Float, nullable=False)
    thang = Column(Integer, nullable=False)

class BaoCaoDoanhThu(BaoCaoThang):
    __tablename__ = 'bao_cao_doanh_thu'
    soLuongThue = Column(Integer, nullable=False)

class BaoCaoTanSuat(BaoCaoThang):
    __tablename__ = 'bao_cao_tan_suat'
    tenSach = Column(String(100), nullable=False)
    soLuong = Column(Integer, nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()