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
   git clone https://github.com/kemo-astra1620/SMS-sender.git
   cd SMS-sender
   
2. **Sanal ortamı oluşturup aktif edin:**
   
         python3 -m venv venv
    
         source venv/bin/activate

4. **Gerekli kütüphaneleri yükleyin:**

         pip3 install -r requirements.txt

6. **Yapılandırma:**

   .env.example dosyasının adını .env olarak değiştirin:
  
       cp .env.example .env
       
   .env dosyasını açıp kendi API / kullanıcı bilgilerinizi yazın.

7. **.env dosyasının içine:**

       # SMS Servisi API Bilgileri
         SMS_API_KEY=buraya_api_anahtarinizi_yazin
         SMS_API_SECRET=buraya_api_gizli_anahtarinizi_yazin
         SENDER_TITLE=BAŞLIK

         # Kullanıcı / Gönderici Bilgileri
         PHONE_NUMBER=+905XXXXXXXXX
    
8. **Kullanım:**

   python3 main.py
