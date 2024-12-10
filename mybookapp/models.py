from sqlalchemy import Column, Integer, String, Float, Enum, Boolean, DateTime, ForeignKey
from mybookapp import db,app
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as UserEnum
from flask_login import UserMixin


class UserRole(UserEnum):
    ADMIN = 1
    USER = 2

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

class TaiKhoan(BaseModel, UserMixin):
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
    active = Column(Boolean, default=True)
    image = Column(String(250), nullable=True)
    ngayTao = Column(DateTime, default=datetime.now())
    maTheLoai = Column(Integer, ForeignKey('loai_sach.id'), nullable=False)
    loaiSach = relationship("LoaiSach", back_populates="sach")

class LoaiSach(BaseModel):
    __tablename__ = 'loai_sach'
    tenTheLoai = Column(String(50), nullable=False)
    sach = relationship("Sach", back_populates="loaiSach")

class QuyDinh(BaseModel):
    __tablename__ = 'quy_dinh'
    tenQD = Column(String(100), nullable=False)
    ngayTao = Column(DateTime, nullable=False)
    ngaySua = Column(DateTime, nullable=False)
    moTaQD = Column(String(255), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()