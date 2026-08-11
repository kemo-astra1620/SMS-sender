# SMS-sender
# Python SMS Gönderme Aracı

Bu proje, Python kullanarak belirlenen numaralara otomatik SMS göndermeyi sağlayan basit ve işlevsel bir araçtır.

---

## Özellikler
- `.env` yapılandırma dosyası ile güvenli API anahtarı yönetimi.
- Kolay ve hızlı kurulum.

---

## Kurulum

1. **Repoyu klonlayın veya indirin:**
   ```bash
   git clone [https://github.com/kemo-astra1620/SMS-sender.git](https://github.com/kemo-astra1620/SMS-sender.git)
   cd SMS-sender
   
2. **Sanal ortamı oluşturup aktif edin:**
   python3 -m venv venv
   source venv/bin/activate

3. **Gerekli kütüphaneleri yükleyin:**
   pip3 install -r requirements.txt

4. **Yapılandırma:**
     1.  .env.example dosyasının adını .env olarak değiştirin:
  
            "" cp .env.example .env ""
       
     2.  .env dosyasını açıp kendi API / kullanıcı bilgilerinizi yazın.
    
5. **Kullanım:**

   python3 main.py
