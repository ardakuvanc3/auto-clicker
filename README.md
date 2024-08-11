# Koordinat Uygulaması

Bu proje, kullanıcıların bir dosyadaki (koordinat.txt) X ve Y koordinatlarını okuyup yazabilmelerini sağlayan basit bir Python uygulamasıdır. `koordinat.py` modülü, koordinatları okumak, yazmak ve göstermek için gerekli fonksiyonları içerir. `main.py` ise bu fonksiyonları kullanarak kullanıcı ile etkileşime girer.

## Özellikler

- `koordinat_oku`: `koordinat.txt` dosyasından X ve Y koordinatlarını okur.
- `koordinat_yaz`: Kullanıcının girdiği X ve Y koordinatlarını `koordinat.txt` dosyasına yazar.
- `koordinatlari_goster`: `koordinat.txt` dosyasından okunan koordinatları ekrana yazdırır.
- Kullanıcı dostu arayüz ile koordinatları görüntüleme, güncelleme ve çıkış yapma seçenekleri sunar.

## Kurulum ve Çalıştırma

1. Projeyi klonlayın:
    ```bash
    git clone https://github.com/kullanici_adi/koordinat-uygulamasi.git
    cd koordinat-uygulamasi
    ```

2. Gerekli Python sürümünün yüklü olduğundan emin olun (3.x).

3. Uygulamayı çalıştırın:
    ```bash
    python main.py
    ```

## Kullanım

1. Uygulama çalıştığında, kullanıcının seçimine göre:
   - `g`: Koordinatları gösterir.
   - `y`: Yeni X ve Y koordinatlarını girmenizi sağlar.
   - `ç`: Uygulamadan çıkar.

2. Koordinatlar `koordinat.txt` dosyasına kaydedilir ve buradan okunur.

## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir **fork** yapın ve değişikliklerinizi bir **pull request** ile gönderin.

1. Fork yapın (`https://github.com/kullanici_adi/koordinat-uygulamasi/fork`).
2. Bir özellik dalı oluşturun (`git checkout -b ozellik-isim`).
3. Değişikliklerinizi işleyin (`git commit -am 'Yeni bir özellik ekledim'`).
4. Dalınıza push yapın (`git push origin ozellik-isim`).
5. Bir **pull request** açın.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyin.
