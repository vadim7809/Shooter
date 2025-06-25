from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import threading
from main import start_game
from shop import shop_window
import sys

app = QApplication([])
window = QWidget()

start_btn = QPushButton("Почати")
shop_btn = QPushButton("Магазин")
exit_btn = QPushButton("Вийти")

layout = QVBoxLayout()
layout.addWidget(start_btn)
layout.addWidget(shop_btn)
layout.addWidget(exit_btn)

window.setLayout(layout)

window.resize(300, 200)


def run_game():
    threading.Thread(target=start_game).start()

start_btn.clicked.connect(run_game)
shop_btn.clicked.connect(shop_window)
exit_btn.clicked.connect(app.quit)

window.show()
sys.exit(app.exec())
