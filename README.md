# Miel & Mug

Küçük bir kahve ve seramik dükkanı konsepti için yaptığım web projesi. Ön yüzde ürün vitrini ve mesajlaşma kutusu var; arka yüzde FastAPI ve Gemini API ile çalışan bir chatbot bulunuyor.

## Nasıl Çalıştırılır?

1. Gerekli paketler kurulur:
   pip install -r requirements.txt

2. Proje klasöründe `.env` adında bir dosya oluşturup içine API key'inizi yazınız:
   GEMINI_API_KEY=your_api_key_here

3. Backend sunucusunu başlatınız:
   python -m uvicorn app:app --reload

4. `index.html` dosyasını tarayıcıda açınız.
