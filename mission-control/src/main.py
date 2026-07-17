import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QGridLayout,
    QFrame,
)

from PySide6.QtCore import Qt


class Card(QFrame):
    def __init__(self, title, description):
        super().__init__()

        self.setObjectName("card")

        layout = QVBoxLayout()

        titleLabel = QLabel(title)
        titleLabel.setObjectName("cardTitle")

        descLabel = QLabel(description)
        descLabel.setObjectName("cardDesc")

        layout.addWidget(titleLabel)
        layout.addWidget(descLabel)

        self.setLayout(layout)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mission Control")
        self.resize(1100, 700)

        mainLayout = QVBoxLayout()

        title = QLabel("Mission Control")
        title.setObjectName("title")

        subtitle = QLabel("Customize Your Universe.")
        subtitle.setObjectName("subtitle")

        grid = QGridLayout()

        grid.addWidget(Card("🎨 Appearance", "Themes, colors and fonts"), 0, 0)
        grid.addWidget(Card("🛰 Widgets", "Desktop widgets"), 0, 1)
        grid.addWidget(Card("🖥 Desktop", "Panels and layouts"), 1, 0)
        grid.addWidget(Card("⚡ Performance", "System tweaks"), 1, 1)

        mainLayout.addWidget(title)
        mainLayout.addWidget(subtitle)
        mainLayout.addSpacing(25)
        mainLayout.addLayout(grid)

        self.setLayout(mainLayout)


app = QApplication(sys.argv)

app.setStyleSheet("""

QWidget{
    background:#0B1020;
    color:white;
    font-family:Inter;
}

QLabel#title{
    font-size:34px;
    font-weight:bold;
}

QLabel#subtitle{
    color:#7EF7FF;
    font-size:15px;
}

QFrame#card{

    background:#171F35;

    border-radius:16px;

    padding:18px;

}

QFrame#card:hover{

    background:#1E2945;

    border:2px solid #7EF7FF;

}

QLabel#cardTitle{

    font-size:20px;
    font-weight:bold;

}

QLabel#cardDesc{

    color:#B8C2E0;

}

""")

window = Window()
window.show()

sys.exit(app.exec())
