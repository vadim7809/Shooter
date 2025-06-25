from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from file_helper import read_file, save_file

def buy_item(price, img):
    data = read_file()
    if data["money"] >= price:
        data["skin"] = img
        data["money"] -= price
        save_file(data)
        QMessageBox.information(None, "Успіх", "Покупку здійснено!")
    else:
        QMessageBox.warning(None, "Помилка", "Недостатньо грошей!")

def shop_window():
    window = QDialog()
    window.setWindowTitle("Магазин")
    window.resize(500, 300)

    elements = [
        {"name": "Базовий", "img": "rocket (1).png", "price": 0},
        {"name": "Синя ракета", "img": "rocket.png", "price": 100},
        {"name": "Червона ракета", "img": "rocket_red.png", "price": 200}
    ]

    current_skin = read_file()["skin"]

    main_line = QHBoxLayout()
    for element in elements:
        ver = QVBoxLayout()

        name_lbl = QLabel(element["name"])
        if current_skin == element["img"]:
            name_lbl.setStyleSheet("color: green; font-weight: bold;")

        img_lbl = QLabel()
        img_pm = QPixmap(element["img"])
        img_pm = img_pm.scaledToWidth(100)
        img_lbl.setPixmap(img_pm)

        price_lbl = QLabel(f"{element['price']}")

        buy_btn = QPushButton("Купити")
        buy_btn.clicked.connect(lambda _, price=element["price"], img=element["img"]: buy_item(price, img))

        ver.addWidget(name_lbl)
        ver.addWidget(img_lbl)
        ver.addWidget(price_lbl)
        ver.addWidget(buy_btn)
        main_line.addLayout(ver)

    window.setLayout(main_line)
    window.exec()
