# Secure Password Generator

Python tabanlı, kriptografik olarak güçlü rastgele şifreler üreten bir CLI aracı. 
Standart `random` kütüphanesi yerine, güvenlik odaklı `secrets` modülü kullanılmıştır.

## Özellikler
- **Güvenli:** `secrets` modülü ile tahmin edilemez şifreler.
- **Özelleştirilebilir:** Uzunluk, rakam ve sembol seçenekleri.
- **CLI Desteği:** Terminal argümanları ile hızlı kullanım.

## Kurulum ve Kullanım

Depoyu klonlayın:
git clone https://github.com/KULLANICI_ADIN/secure-pass-gen.git
cd secure-pass-gen

Kullanım:
python3 passgen.py -l 20 -s -n

## Öğrenilenler
Bu projeyi geliştirirken:
- Python `argparse` ile CLI araçları geliştirmeyi,
- `secrets` vs `random` modülleri arasındaki güvenlik farklarını,
- Python'da string manipülasyonunu öğrendim.
