#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import secrets  # Güvenlik için 'random' yerine 'secrets' kullanıyoruz
import string
import argparse

def generate_password(length, use_symbols, use_numbers):
    """
    Belirtilen kriterlere göre güvenli şifre oluşturur.
    """
    # 1. Harf havuzunu oluştur (a-z ve A-Z)
    characters = string.ascii_letters
    
    # Eğer kullanıcı rakam istediyse havuza ekle
    if use_numbers:
        characters += string.digits
    
    # Eğer kullanıcı sembol istediyse havuza ekle
    if use_symbols:
        characters += string.punctuation

    # 2. Şifreyi oluştur
    # secrets.choice() fonksiyonu kriptografik olarak güvenli seçim yapar
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password

def main():
    # 3. Terminalden gelen komutları (argümanları) ayarla
    parser = argparse.ArgumentParser(description="Guvenli Sifre Olusturucu Araci")
    
    parser.add_argument("-l", "--length", type=int, default=12, help="Sifre uzunlugu (Varsayilan: 12)")
    parser.add_argument("-s", "--symbols", action="store_true", help="Ozel karakterleri dahil et")
    parser.add_argument("-n", "--numbers", action="store_true", help="Rakamlari dahil et")
    
    args = parser.parse_args()

    # 4. Sonucu ekrana yazdır
    print(f"--- Guvenli Sifre Olusturuluyor ---")
    pwd = generate_password(args.length, args.symbols, args.numbers)
    
    # Terminalde yeşil renkli çıktı vermek için renk kodları
    print(f"\nGenerated Password: \033[92m{pwd}\033[0m") 
    print(f"Detaylar: {args.length} karakter | Rakam: {args.numbers} | Sembol: {args.symbols}")

if __name__ == "__main__":
    main()
