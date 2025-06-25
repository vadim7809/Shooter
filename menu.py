from PyQt6.QtWidgets import *
from main import *
from shop import *

app = QApplication([])
window = QWidget()
stat_btn = QPushButton("Почати")
shop_btn = QPushButton("Магазин")
exit_btn = QPushButton("Вийти")

main_line = QVBoxLayout()
main_line.addWidget(stat_btn)
main_line.addWidget(shop_btn)
main_line.addWidget(exit_btn)

window.setLayout(main_line)

stat_btn.clicked.connect(start_game)
shop_btn.clicked.connect(shop_window)


window.show()
app.exec()