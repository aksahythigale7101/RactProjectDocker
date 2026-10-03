import json, urllib.request

items = [
 ("Laptop", "Gaming laptop 16GB RAM", 75000, 10),
 ("Mouse", "Wireless optical mouse", 799, 50),
 ("Keyboard", "Mechanical keyboard RGB", 2499, 30),
 ("Monitor", "24 inch Full HD monitor", 11999, 15),
 ("Headphones", "Bluetooth over-ear headphones", 3499, 40),
 ("Webcam", "1080p USB webcam", 1999, 25),
 ("Printer", "Wireless inkjet printer", 8999, 8),
 ("Router", "Dual band WiFi router", 2199, 35),
 ("Pen Drive", "64GB USB 3.0 pen drive", 599, 100),
 ("Hard Disk", "1TB external hard disk", 4499, 20),
 ("SSD", "512GB NVMe SSD", 3999, 28),
 ("Power Bank", "20000mAh fast charging", 1799, 45),
 ("Smartphone", "6GB RAM 128GB storage", 18999, 22),
 ("Tablet", "10 inch Android tablet", 14999, 12),
 ("Smart Watch", "Fitness tracking watch", 2999, 33),
 ("Speaker", "Portable bluetooth speaker", 1499, 38),
 ("Charger", "65W fast charger", 1299, 60),
 ("USB Cable", "Type-C braided cable 1m", 299, 150),
 ("Laptop Bag", "Water resistant 15.6 inch bag", 1199, 42),
 ("Desk Lamp", "LED desk lamp dimmable", 899, 27),
 ("Office Chair", "Ergonomic mesh chair", 7499, 9),
 ("Study Table", "Wooden study table", 5999, 7),
 ("Notebook", "200 pages ruled notebook", 99, 300),
 ("Pen Set", "Pack of 10 gel pens", 149, 200),
 ("Backpack", "Casual 30L backpack", 1599, 36),
]

ok = 0
for name, desc, price, qty in items:
    data = json.dumps({"name": name, "description": desc,
                       "price": price, "quantity": qty}).encode()
    req = urllib.request.Request("http://127.0.0.1:8000/products/", data=data,
                                 headers={"Content-Type": "application/json"},
                                 method="POST")
    try:
        urllib.request.urlopen(req)
        ok += 1
    except Exception as e:
        print("FAILED:", name, e)
print("inserted:", ok, "of", len(items))