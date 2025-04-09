from flask import Flask, render_template, request, jsonify
import psycopg2

app = Flask(__name__)

# Veritabanı bağlantı bilgileri
host = "localhost"
database = "demopost"
user = "postgres"
password = "Adana123oguz"
port = "4343"

@app.route('/', methods=['GET', 'POST'])
def index():
    basari_mesaji = None

    if request.method == 'POST':
        id_deger = request.form['id']
        number_deger = request.form['number']
        name_deger = request.form['name']

        try:
            conn = psycopg2.connect(host=host, database=database, user=user, password=password, port=port)
            cur = conn.cursor()

            sorgu = "INSERT INTO ornektablo (id, number, name) VALUES (%s, %s, %s)"
            cur.execute(sorgu, (id_deger, number_deger, name_deger))
            conn.commit()
            basari_mesaji = "Kayıt Başarıyla Eklendi!"

        except (Exception, psycopg2.DatabaseError) as error:
            print("Veritabanı hatası:", error)
            basari_mesaji = f"Kayıt Başarısız! Hata: {error}"

        finally:
            if 'conn' in locals() and conn:
                cur.close()
                conn.close()
                print('Veritabanı bağlantısı kapatıldı.')

    return render_template('index.html', basari_mesaji=basari_mesaji)

# ✅ JSON ile POST kayıt
@app.route('/api/kayit', methods=['POST'])
def api_kayit():
    data = request.get_json()
    if not data:
        return jsonify({"basari": False, "mesaj": "Geçersiz veri"}), 400

    id_deger = data.get('id')
    number_deger = data.get('number')
    name_deger = data.get('name')

    if not all([id_deger, number_deger, name_deger]):
        return jsonify({"basari": False, "mesaj": "Tüm alanlar gerekli"}), 400

    try:
        conn = psycopg2.connect(host=host, database=database, user=user, password=password, port=port)
        cur = conn.cursor()

        sorgu = "INSERT INTO ornektablo (id, number, name) VALUES (%s, %s, %s)"
        cur.execute(sorgu, (id_deger, number_deger, name_deger))
        conn.commit()

        return jsonify({"basari": True, "mesaj": "Kayıt başarıyla eklendi!"})

    except (Exception, psycopg2.DatabaseError) as error:
        return jsonify({"basari": False, "mesaj": f"Kayıt başarısız: {error}"}), 500

    finally:
        if 'conn' in locals() and conn:
            cur.close()
            conn.close()

# ✅ GET ile veritabanından tüm kayıtları al
@app.route('/api/kayitlar', methods=['GET'])
def api_kayitlar():
    try:
        conn = psycopg2.connect(host=host, database=database, user=user, password=password, port=port)
        cur = conn.cursor()

        sorgu = "SELECT id, number, name FROM ornektablo"
        cur.execute(sorgu)
        kayitlar = cur.fetchall()

        # Liste halinde JSON objesine dönüştür
        sonuc = [{"id": row[0], "number": row[1], "name": row[2]} for row in kayitlar]

        return jsonify(sonuc)

    except (Exception, psycopg2.DatabaseError) as error:
        return jsonify({"basari": False, "mesaj": f"Veri alınamadı: {error}"}), 500

    finally:
        if 'conn' in locals() and conn:
            cur.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
