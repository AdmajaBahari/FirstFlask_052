from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route untuk halaman utama (index/home)
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk menampilkan form input
@app.route('/form')
def form():
    return render_template('form.html')

# Route untuk memproses form (Method POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        # Mengambil data dari form
        nama = request.form.get('nama')
        nim = request.form.get('nim')
        
        # Mengirim data ke template result
        return render_template('result.html', nama=nama, nim=nim)
    else:
        # Jika diakses dengan GET, redirect ke form
        return redirect(url_for('form'))

if __name__ == '__main__':
    app.run(debug=True)
# LINK AKSES = http://127.0.0.1:5000/form
