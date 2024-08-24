# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:07:47 2024

@author: ACER
"""

N = int(input("Nhap so nguyen duong N co 2 chu so: "))
if 10<=N<=99:
    hang_chuc = N % 10
    hang_don_vi = N // 10
    tong_chu_so = hang_chuc + hang_don_vi
    print("Tong cac chu so cua N la: ", tong_chu_so)
else:
    print("So nhap vao khong phai la so nguyen duong co 2 chu so")
    