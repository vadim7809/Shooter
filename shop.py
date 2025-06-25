from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

def shop_window():
    window = QDialog()

    elements = [
        {
            "name": "test1",
            "img":  "rocket.png",
            "price": 100,
            "name2": "test2",
            "img2": "завантаження.png",
            "price2": 200,
            "name3": "test3",
            "img3": "png-clipart-white-spaceship-rocket-rocket-photography-spacecraft.png",
            "price3": 300


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
        price_lbl = QLabel(str(element["price"]))
        buy_btn = QPushButton("Купити")
        ver.addWidget(name_lbl)
        ver.addWidget(img_lbl)
        ver.addWidget(price_lbl)
        ver.addWidget(buy_btn)
        main_line.addLayout(ver)




    window.setLayout(main_line)
    window.show()
    window.exec()