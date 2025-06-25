

from PyQt6.QtWidgets import*

from main import window

start_btn = QPushButton("Почати")
shop_btn = QPushButton("shop")

main_line =QVBoxLayout()
main_line.addWidget(start_btn)
main_line.addWidget(shop_btn)

window.setLayout(main_line)

start_btn.clicked.connect(start_game)
shop_btn.clicked.connect(shop_window)


window.show()
window.exec()
