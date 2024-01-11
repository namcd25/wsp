from flask import Flask, request, render_template, redirect, url_for
import mysql.connector as mysql

app = Flask(__name__)
app.secret_key = "1234"

# Ganti dengan informasi koneksi MySQL Anda
db = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="checkout"
)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/products")
def products():
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM products"
    cursor.execute(query)
    products = cursor.fetchall()
    return render_template("products.html", products=products)

@app.route("/singlepage/<int:id>")
def singlepage(id):
    cursor = db.cursor(dictionary=True)
    query = f"SELECT item_id, nama_produk, harga_produk FROM products WHERE item_id = {id}"

    cursor.execute(query)
    data = cursor.fetchone()

    query = "SELECT * FROM products"
    cursor.execute(query)
    products = cursor.fetchall()

    cursor.close()
    return render_template("singlepage.html", products=products, data= data)



# @app.route("/display/Jersey-<int:id>", methods=["GET", "POST"])
# def display(id):
#     cursor = db.cursor(dictionary=True)

#     # MENGAMBIL DATA 
#     query = f"SELECT id_jersey, nama_jersey, id_kategori, harga, stok, gambar_model, gambar_jersey FROM db_jersey WHERE id_jersey = {id}"
#     cursor.execute(query)
#     data = cursor.fetchone()



    cursor.close() 
    return render_template("display.html", data=data, catalog2 = data2, catalog3 = data3 )




@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/checkout")
def checkout():
    try:
        if request.method == 'POST':
            # Mendapatkan data dari formulir HTML
            nama = request.form["nama"]
            email = request.form["Email"]
            alamat = request.form["alamat"]
            nama_sepatu = request.form["nama_sepatu"]
            ukuran_sepatu = request.form["ukuran_sepatu"]
            metode_pembayaran = request.form["metode_pembayaran"]

            cursor = db.cursor()
            query = "INSERT INTO checkout1 (nama, email, alamat, nama_sepatu, ukuran_sepatu, metode_pembayaran) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (nama, email, alamat, nama_sepatu, ukuran_sepatu, metode_pembayaran))
            db.commit()
            cursor.close()
            
            return redirect(url_for('home'))
        return render_template("checkout.html")
        

    except Exception as e:
        print(f"Error during checkout: {e}")
        db.rollback()
        print(f"Data yang dikirim: {nama}, {email}, {alamat}, {nama_sepatu}, {ukuran_sepatu}, {metode_pembayaran}")
        
    return render_template("checkout.html", success=False) 

if __name__ == "__main__":
    app.run(debug=True)
