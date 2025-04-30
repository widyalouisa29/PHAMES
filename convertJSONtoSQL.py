import json
import datetime
import mysql.connector

with open("dataset.json", "r") as jsonfile:
    dataset = json.load(jsonfile)["data"]

if __name__ == "__main__":
    try:
        conn = mysql.connector.connect(
            host="localhost",  
            user="root",  
            password="",  
            database="pharmacy_db" 
        )
        cursor = conn.cursor()
    except mysql.connector.Error as e:
        print(e)
    
    query = "INSERT INTO obat (nama_obat, tanggal_expiry_obat, jumlah_stok_obat, jenis_obat, minimum_stock) VALUES (%s, %s, %s, %s, %s)"
    for i, item in enumerate(dataset):
        date = [int(i) for i in item["expiration_date"].split("-")]
        expiration_date = datetime.datetime(date[0], date[1], date[2])
        cursor.execute(query, (item["name"], expiration_date.strftime("%Y-%m-%d"), item["stock"], item["Category"], item["min_stock"]))
    conn.commit() 


