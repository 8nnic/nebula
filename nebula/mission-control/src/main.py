import sys

from widgets.card import Card
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QFrame,
    QGridLayout,
    QVBoxLayout,
    QWidget,
)


app = QApplication(sys.argv)

app.setStyleSheet("""

QWidget {
    background: #0B1020;
    color: white;
    font-family: Inter;
}

QLabel#title {
    font-size: 34px;
    font-weight: bold;
}

QLabel#subtitle {
    color: #7EF7FF;
    font-size: 15px;
}

QFrame#card {
    background: #171F35;
    border-radius: 16px;
    padding: 18px;
}

QFrame#card:hover {

    background:#233252;

    border:2px solid #7EF7FF;

}

QLabel#cardTitle {
    font-size: 20px;
    font-weight: bold;
}

QLabel#cardDesc {
    color: #B8C2E0;
}

""")

window = Window()
window.show()

sys.exit(app.exec())
