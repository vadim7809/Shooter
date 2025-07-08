from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *
from file_helper import *

def buy_item(price, img):
    data = read_file()
    if data["money"] >= price:
        data["skin"] = img
        data["money"] -= price
        save_file(data)
        print("Куплено: " + img)
    else:
        print("Немає грошей")

def shop_window():
    window = QDialog()
    window.setWindowTitle("Магазин")

    elements = [
        {
            "name": "Тестова ракета",
            "img": "rocket (1).png",
            "price": 0
        },
        {
            "name": "Космічний корабель",
            "img": "roket.200.png",
            "price": 200
        },
        {
            "name": "Швидкий зореліт",
            "img": "rocket3.png",
            "price": 500
        }
    ]

    main_line = QHBoxLayout()

    for element in elements:
        ver = QVBoxLayout()

        name_lbl = QLabel(element["name"])

        img_lbl = QLabel()
        img_pm = QPixmap(element["img"])
        img_pm = img_pm.scaledToWidth(100)
        img_lbl.setPixmap(img_pm)

        price_lbl = QLabel("Ціна: " + str(element["price"]) + " монет")

        buy_btn = QPushButton("Купити")
        buy_btn.clicked.connect(
            lambda _, price=element["price"], img=element["img"]: buy_item(price, img)
        )

        ver.addWidget(name_lbl)
        ver.addWidget(img_lbl)
        ver.addWidget(price_lbl)
        ver.addWidget(buy_btn)

        main_line.addLayout(ver)

    window.setLayout(main_line)
    window.exec()
