# Aes Crypter
Bu Python programı, veri şifreleme ve şifre çözme işlemleri için AES (Advanced Encryption Standard) algoritmasını kullanır. AES, NIST tarafından belirlenen ve DES algoritmasının yerini almak için tasarlanmış bir şifreleme algoritmasıdır.

Bu programda, girilen metin ve anahtar kullanılarak veri şifrelenir ve şifreli metin oluşturulur. Daha sonra, şifreli metin ve aynı anahtar kullanılarak veri çözülür ve orijinal metin elde edilir.

Bu programın kullanımı oldukça basittir. Programı çalıştırdıktan sonra, kullanıcı veri şifreleme veya şifre çözme işlemlerinden birini seçer ve gerekli bilgileri girer.

Kullanıcılar, kodun daha iyi anlaşılması için yorum satırlarını okuyabilirler. Ayrıca, bu programı daha da geliştirebilir ve farklı amaçlar için kullanabilirler.


### AES Hakkında Daha Fazla Bilgi
AES, üç farklı anahtar boyutu olan **(128, 192 ve 256 bit)** blok şifrelemesi sağlayan bir algoritmadır. 128 bit anahtar boyutu en çok kullanılandır.

AES, veriyi bir blok boyutunda **(128 bit)** işler. Bu blok, şifreleme işlemi sırasında değişir ve çıktı olarak şifreli metin olarak üretilir.

AES, şifreleme işlemi sırasında farklı işlemler uygular. Bu işlemler arasında değiştirme (substitution), kaydırma (shift) ve karıştırma (mix) gibi işlemler vardır. Bu işlemler, verinin daha güvenli hale getirilmesine yardımcı olur.

AES algoritması, endüstride ve askeri alanda sıklıkla kullanılan bir şifreleme algoritmasıdır.


### IV Değişkeni Nedir ve Neden Önemlidir?
AES algoritması, blok şifreleme modunda çalışır. Bu modda, her blok önceki bloğun şifrelenmiş haliyle XOR işlemine tabi tutulur. İlk blok ise IV (Initialization Vector) ile XOR işlemine tabi tutulur. IV, rastgele bir değerdir ve şifreleme anahtarından ayrı olarak kullanılır. Bu, her şifreleme işlemi için farklı bir IV kullanıldığından, şifrelenen verinin tekrar eden bloklarının aynı şekilde şifrelenmesini engeller.

IV değişkeninin uzunluğu şifreleme bloğunun uzunluğu ile aynıdır **(16 byte)**. Bu nedenle, AES şifreleme modunda kullanıldığında, IV değişkeni şifreleme anahtarının yanı sıra şifreleme işleminin bir parçasıdır. Bu, aynı anahtar kullanılsa bile farklı IV'lerle şifreleme yapıldığında, şifrelenen verinin farklı olacağı anlamına gelir.

Bu nedenle, güvenli bir şifreleme için, IV değişkeninin öngörülemeyecek kadar rastgele olması ve her şifreleme işlemi için benzersiz olması gereklidir. Kullanıcıların farklı bir IV değişkeni belirleyebilmesi için bu örnekte sabit bir değer kullanılmıştır, ancak gerçek dünyada, rastgele oluşturulan bir IV değeri kullanılması önerilir.


## Kodun Kullanımı
#### Gerekli kütüphanelerin yüklenmesi :
Bu kodda **"Crypto.Cipher"**, **"base64"**, **"colorama"** ve **"pyfiglet"** kütüphaneleri kullanılmaktadır. Bu nedenle, kodu çalıştırmadan önce bu kütüphanelerin yüklenmesi gerekmektedir.

#### Şifreleme işlemi yapmak için :
- Programı çalıştırdığınızda, "1- Veri şifreleme işlemi" seçeneğini seçin.
- Şifrelenecek metni ve şifreleme anahtarını girin.
- Program, şifreli metni oluşturacak ve ekrana yazdıracaktır.

#### Şifreli metni çözmek için :
- Programı çalıştırdığınızda, "2- Veri şifresini çözme işlemi" seçeneğini seçin.
- Çözülecek şifreli metni ve şifreleme anahtarını girin.
- Program, çözülmüş metni ekrana yazdıracaktır.


[LinkedIn](https://www.linkedin.com/in/burakpekerr/), [Instagram](https://instagram.com/burakpeker.psd)
