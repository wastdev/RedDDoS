# 🚀 RedDDoS v1 Yakında vs v1.1 Gelecektir.

Bu proje **Termux**, **Pydroid 3 (Android)** ve **Windows/Linux** sistemlerinde sorunsuz çalışacak şekilde optimize edilmiştir.

---

## 👤 Geliştirici

- **Wast**
- 🌐 [https://github.com/wastdev](https://github.com/wastdev)

---

## ⚠️ Yasal Uyarı

> ❗ **UYARI:** Bu araç yalnızca test ve eğitim amacıyla kullanılmalıdır. Gerçek sunuculara izinsiz saldırı yasadışıdır. Geliştirici sorumluluk kabul etmez.

---

## 📦 Gereksinimler

Python 3 kurulu olmalıdır.

### Gerekli Python kütüphaneleri:
- `tqdm`
- `pyfiglet`

Kurulum (ortama göre aşağıda belirtilmiştir):

---

## 🖥️ PC (Windows / Linux)

1. Python 3 kurulu değilse indir: https://www.python.org/downloads/
2. Komut satırını aç
3. Kütüphaneleri kur:
   ```bash
   pip install tqdm pyfiglet
   ```
4. Dosyanın bulunduğu dizine git:
   ```bash
   cd reddos
   python reddos.py
   ```

---

## 📱 Android (Pydroid 3)

1. [Pydroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3) uygulamasını indir
2. Uygulama içinde "PIP" kısmına girip şu kütüphaneleri sırayla yükle:
   ```bash
   pip install tqdm
   pip install pyfiglet
   ```
3. `reddos.py` dosyasını Pydroid editöründen açıp çalıştır.

---

## 📱 Android (Termux)

1. Termux'u aç ve aşağıdaki komutları sırayla çalıştır:
   ```bash
   pkg update -y
   pkg install python -y
   pip install tqdm pyfiglet
   ```

2. Dosyayı indirdikten sonra çalıştırmak için:
   ```bash
   python reddos.py
   ```

**Alternatif olarak GitHub üzerinden klonlamak istersen:**
```bash
git clone https://github.com/wastdev/reddos.git
cd reddos
python reddos.py
```

---

## ✅ Kullanım

Program başlatıldığında şu menü gelir:

```
1. Web Sitesi Alan Adı
2. IP Adresi
3. Hakkında
4. Çıkış
```

- 1: Alan adını IP'ye çevirerek hedef alır.  
- 2: Direkt IP adresiyle çalışır.  
- 3: Program hakkında bilgi verir.  
- 4: Programdan çıkar.

Sonrasında belirli bir port seçip seçmemek istediğiniz sorulur. Ardından sonsuz döngüde UDP paket gönderimi başlar.

---

## 🧪 Örnek Çalıştırma (Terminal)

```bash
python reddos.py
```

---

## 🔗 GitHub’a Yükleme (isteğe bağlı)

```bash
git init
git remote add origin https://github.com/wastdev/reddos.git
git add .
git commit -m "İlk sürüm"
git push -u origin master
```

---

## 📃 Lisans

Bu proje [MIT Lisansı](https://opensource.org/licenses/MIT) ile lisanslanmıştır.
