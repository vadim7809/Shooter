from PyQt6.QtWidgets import*
from PyQt6.QtGui import*



def show_window():
    window = QDialog()
    elements = [
        {
            "name": "test1",
            "img": "hero.png",
            "price": 100
        }
    ]

    main_line = QHBoxLayout()
    for element in elements:
        ver = QVBoxLayout()
        name_lb = QLabel(element["name"])
        img_lb = QLabel()
        img_pm = QPixmap(element["ing"])
        img_pm = img_pm.scaledToWidth(100)
        img_lb.setPixmap(img_pm)
        price_lb = QLabel(str(element["price"]))
        buy_btn = QPushButton("Купити")
        ver.addWidget(name_lb)
        ver.addWidget(img_lb)
        ver.addWidget(price_lb)
        ver.addWidget(buy_btn)
        main_line.addLayout(main_line)


    window.show()
    window.exec()