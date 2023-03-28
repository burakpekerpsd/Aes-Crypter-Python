from Crypto.Cipher import AES
import base64
import colorama
from colorama import Fore, Back, Style
import pyfiglet

# https://github.com/burakpekerpsd
# https://instagram.com/burakpeker.psd



print(pyfiglet.figlet_format("Aes Crypter"))

def sifrele(metin, anahtar):
    iv = b'1234567890123456'
    # iv Değişkeni 16 Bit Uzunluğunda Başlangıç Değeridir 
    # Şifreleme Anahtarı Gibidir Şifreleme Anahtarıyla Birlikte Kullanılır İkinci Bir Şifreleme Adımı Diyebiliriz
    # Başlangıç Değeri Nekadar Karmaşık Olursa Daha Güvenilir Bir Şifreleme Yapmış Olursunuz
    # Kodu Kullanmadan Önce Lütfen Tırnak İçindeki Başlangıç Değerini Kendinize Özel Olarak Belirleyiniz


    anahtar = anahtar.encode('utf-8')
    anahtar = anahtar + (b' ' * (16 - len(anahtar) % 16))
    cipher = AES.new(anahtar, AES.MODE_CBC, iv)
    metin = metin.encode('utf-8')
    metin = metin + (b' ' * (16 - len(metin) % 16))
    sifreli_metin = cipher.encrypt(metin)
    sifreli_metin = base64.b64encode(sifreli_metin).decode('utf-8')
    return sifreli_metin

def coz(sifreli_metin, anahtar):

    iv = b'1234567890123456'
    # iv Değişkeni 16 Bit Uzunluğunda Başlangıç Değeridir 
    # Şifreleme Anahtarı Gibidir Şifreleme Anahtarıyla Birlikte Kullanılır İkinci Bir Şifreleme Adımı Diyebiliriz
    # Başlangıç Değeri Nekadar Karmaşık Olursa Daha Güvenilir Bir Şifreleme Yapmış Olursunuz
    # Kodu Kullanmadan Önce Lütfen Tırnak İçindeki Başlangıç Değerini Kendinize Özel Olarak Belirleyiniz


    anahtar = anahtar.encode('utf-8')
    anahtar = anahtar + (b' ' * (16 - len(anahtar) % 16))
    sifreli_metin = base64.b64decode(sifreli_metin.encode('utf-8'))
    cipher = AES.new(anahtar, AES.MODE_CBC, iv)
    metin = cipher.decrypt(sifreli_metin)
    metin = metin.rstrip(b' ')
    metin = metin.decode('utf-8')
    return metin

while True:

    print(Fore.LIGHTGREEN_EX)
    print("1- Veri şifreleme işlemi")
    print("2- Veri şifresini çözme işlemi")
    print(Style.RESET_ALL)
    secim = input("Seçiminiz: ")

    if secim == '1':
        print(Fore.LIGHTRED_EX)
        metin = input("Şifrelenecek metin: ")
        anahtar = input("Şifreleme anahtarı: ")
        sifreli_metin = sifrele(metin, anahtar)
        print("Şifreli metin: ", sifreli_metin,Style.RESET_ALL)

    elif secim == '2':
        print(Fore.LIGHTGREEN_EX)
        sifreli_metin = input("Çözülecek şifreli metin: ")
        anahtar = input("Şifreleme anahtarı: ")
        metin = coz(sifreli_metin, anahtar)
        print()
        print("Çözülen metin: ", metin,Style.RESET_ALL)

    else:
        print("Geçersiz seçim, tekrar deneyin.")
