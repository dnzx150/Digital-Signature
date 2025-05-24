from flask import Blueprint, render_template, request, redirect, send_from_directory, flash
import os
from werkzeug.utils import secure_filename
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

main = Blueprint('main', __name__)
BASE = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(BASE, 'uploads')
SIGNED_FOLDER = os.path.join(BASE, 'signed_files')
RECEIVED_FOLDER = os.path.join(BASE, 'received_files')
KEY_FOLDER = os.path.join(BASE, 'keys')

def get_key_pair(user_prefix):
    priv_path = os.path.join(KEY_FOLDER, f"{user_prefix}_private.pem")
    pub_path = os.path.join(KEY_FOLDER, f"{user_prefix}_public.pem")
    return priv_path, pub_path

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/generate_keys')
def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    with open(os.path.join(KEY_FOLDER, 'sender_private.pem'), 'wb') as f:
        f.write(private_key)
    with open(os.path.join(KEY_FOLDER, 'sender_public.pem'), 'wb') as f:
        f.write(public_key)
    with open(os.path.join(KEY_FOLDER, 'receiver_private.pem'), 'wb') as f:
        f.write(private_key)
    with open(os.path.join(KEY_FOLDER, 'receiver_public.pem'), 'wb') as f:
        f.write(public_key)
    flash('Khóa đã được tạo thành công!')
    return redirect('/')

@main.route('/sender', methods=['GET', 'POST'])
def sender():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            with open(filepath, 'rb') as f:
                content = f.read()
            key_path, _ = get_key_pair('sender')
            with open(key_path, 'rb') as f:
                private_key = RSA.import_key(f.read())
            h = SHA256.new(content)
            signature = pkcs1_15.new(private_key).sign(h)
            sig_path = os.path.join(SIGNED_FOLDER, f"{filename}.info")
            with open(sig_path, 'wb') as f:
                f.write(signature)
            flash('Đã ký thành công và lưu chữ ký!')
            return redirect('/sender')
    return render_template('sender.html')

@main.route('/receiver', methods=['GET', 'POST'])
def receiver():
    if request.method == 'POST':
        file = request.files['file']
        sig = request.files['signature']
        if file and sig:
            filename = secure_filename(file.filename)
            filepath = os.path.join(RECEIVED_FOLDER, filename)
            file.save(filepath)
            sig_path = os.path.join(RECEIVED_FOLDER, f"{filename}.info")
            sig.save(sig_path)
            with open(filepath, 'rb') as f:
                content = f.read()
            with open(sig_path, 'rb') as f:
                signature = f.read()
            _, pub_path = get_key_pair('sender')
            with open(pub_path, 'rb') as f:
                public_key = RSA.import_key(f.read())
            h = SHA256.new(content)
            try:
                pkcs1_15.new(public_key).verify(h, signature)
                flash('Xác thực thành công!')
            except (ValueError, TypeError):
                flash('Chữ ký không hợp lệ!')
            return redirect('/receiver')
    return render_template('receiver.html')
