```markdown
# Digital Signature - Ứng dụng Chữ Ký Số

Đây là một ứng dụng web đơn giản sử dụng **Flask** để:
- Tạo cặp khóa RSA (public/private)
- Ký số các tệp tin
- Xác minh chữ ký số

## 🧩 Cấu trúc thư mục

```

<h2 align="center">🔐 Digital Signature - Ứng dụng Chữ Ký Số</h2>

<pre>
📂 Digital_Signature/
├── 🐍 app/
│   ├── __init__.py           # Khởi tạo Flask app
│   ├── views.py              # Xử lý logic và routing
│   ├── 🌐 templates/         # Giao diện HTML (sử dụng Bootstrap)
│   ├── 🔑 keys/              # Chứa cặp khóa RSA
│   ├── 📤 uploads/           # File được tải lên để ký
│   ├── 📝 signed_files/      # Chữ ký số đã tạo
│   ├── 📩 received_files/    # File và chữ ký gửi đến để xác minh
│   └── 👤 user_keys/         # (Dự phòng cho việc mở rộng theo người dùng)
├── 🚀 run.py                 # Điểm khởi chạy ứng dụng
├── 📦 requirements.txt       # Danh sách thư viện Python cần cài đặt
└── 📖 README.md              # Tài liệu giới thiệu dự án
</pre>
````

## ⚙️ Tính năng

1. **Tạo khóa**: Sinh cặp khóa RSA (2048-bit)
2. **Người gửi ký file**: Tải lên tệp và tạo chữ ký bằng private key
3. **Người nhận xác minh**: Kiểm tra chữ ký với public key

## 🚀 Cách sử dụng

### Bước 1: Cài đặt thư viện cần thiết

```bash
pip install -r requirements.txt
````

### Bước 2: Khởi chạy ứng dụng

```bash
python run.py
```

### Bước 3: Truy cập trình duyệt

Mở trình duyệt và truy cập địa chỉ:

```
http://127.0.0.1:5000
```

## 📌 Ghi chú

* Mỗi lần ký file sẽ tạo ra một file `.info` chứa chữ ký số.
* Có thể sử dụng khóa được tạo sẵn trong thư mục `app/keys/` hoặc tạo mới.
* Chữ ký số sử dụng thuật toán **RSA + SHA256** (thư viện `pycryptodome`).

## 📚 Công nghệ sử dụng

* Python 3
* Flask
* PyCryptodome
* Bootstrap (cho giao diện)

---

🔒 **Digital Signature** giúp bạn kiểm chứng tính toàn vẹn và xác thực nguồn gốc của tệp tin thông qua chữ ký điện tử.
