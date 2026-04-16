# FastAPI Template

FastAPI + SQLAlchemy + Pydantic + Alembic kullanılarak hazırlanmış minimal ve ölçeklenebilir backend proje şablonu.

## 🚀 Amaç

Bu template, yeni bir backend projesine başlarken tekrar eden kurulumları ortadan kaldırmak için oluşturulmuştur.

Hazır gelen yapı:

* FastAPI uygulama başlangıcı
* Katmanlı mimari (router, service, repository)
* SQLAlchemy veritabanı altyapısı
* Pydantic veri doğrulama
* Alembic migration sistemi
* Environment (.env) desteği
* Health check endpoint

---

## 📦 Kullanım

### 1. Template'ten yeni proje oluştur

GitHub üzerinden:

* "Use this template" butonuna tıkla
* Yeni repository oluştur

---

### 2. Projeyi klonla

```bash
git clone <your-repo-url>
cd <your-project>
```

---

### 3. Sanal ortam oluştur

```bash
python -m venv .venv
```

### Windows:

```bash
.venv\Scripts\activate
```

---

### 4. Bağımlılıkları yükle

```bash
pip install -r requirements.txt
```

---

### 5. Environment ayarları

`.env.example` dosyasını kopyala:

```bash
cp .env.example .env
```

Gerekli değerleri düzenle.

---

### 6. Uygulamayı çalıştır

```bash
uvicorn app.main:app --reload
```

---

## 📡 API

### Health Check

```http
GET /api/v1/health
```

Response:

```json
{
  "status": "ok"
}
```

---

## 📁 Proje Yapısı

```
app/
├── api/            # Router (endpoint) katmanı
├── core/           # Config ve ayarlar
├── db/             # Database bağlantı ve session
├── models/         # SQLAlchemy modelleri
├── schemas/        # Pydantic şemaları
├── repositories/   # Veri erişim katmanı
├── services/       # İş mantığı katmanı
└── main.py         # Uygulama giriş noktası

alembic/            # Migration dosyaları
```

---

## 🧱 Mimari

Proje katmanlı mimari kullanır:

* **Router** → HTTP isteklerini karşılar
* **Schema (Pydantic)** → Veri doğrulama
* **Service** → İş kuralları
* **Repository** → Veritabanı işlemleri
* **Model (SQLAlchemy)** → Veritabanı yapısı
* **Alembic** → Şema değişiklik yönetimi

---

## 🛠️ Kullanılan Teknolojiler

* FastAPI
* SQLAlchemy
* Pydantic
* Alembic
* Uvicorn

---

## 🔄 Migration (Alembic)

Yeni migration oluştur:

```bash
alembic revision --autogenerate -m "init"
```

Migration uygula:

```bash
alembic upgrade head
```

---

## ⚠️ Notlar

* `.env` dosyası versiyon kontrolüne dahil edilmemelidir
* Template sade tutulmuştur, ihtiyaca göre genişletilmelidir
* Domain (örnek: user, product vs.) bu template içinde bulunmaz

---

## 📌 Geliştirme

Yeni bir modül eklerken:

1. model oluştur
2. schema oluştur
3. repository yaz
4. service ekle
5. router bağla
6. migration oluştur

---

## 📄 Lisans

İsteğe bağlı olarak eklenebilir.
