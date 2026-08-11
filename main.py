import requests

def send_sms(phone_number: str, message: str):
    url = "https://textbelt.com/text"
    payload = {
        'phone': phone_number,
        'message': message,
        'key': 'text'
    }
    
    response = requests.post(url, data=payload)
    result = response.json()
    
    if result.get("success"):
        print("[+] SMS başarıyla gönderildi!")
        print(f"[i] Kalan ücretsiz SMS hakkınız: {result.get('quotaRemaining')}")
    else:
        print(f"[-] SMS gönderilemedi: {result.get('error')}")

if __name__ == "__main__":
    print("=== Textbelt SMS Tool ===")
    target = input("Telefon Numarası (+905XXXXXXXXX formatında): ")
    msg = input("Mesajınız: ")
    
    if target and msg:
        send_sms(target, msg)
    else:
        print("[-] Lütfen boş bırakmayın.")