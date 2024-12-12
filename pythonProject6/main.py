import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel,
    QLineEdit, QTableWidget, QTableWidgetItem, QHBoxLayout, QStackedWidget, QMessageBox, QInputDialog
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QLinearGradient, QColor, QBrush


class LoginWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label_username = QLabel("Логин:")
        self.input_username = QLineEdit()
        self.label_password = QLabel("Пароль:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)

        self.btn_login = QPushButton("Войти")
        self.btn_login.clicked.connect(self.validate_login)

        layout.addWidget(self.label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.btn_login)

        self.setStyleSheet("""
            QLabel {
                font-family: 'Arial';
                font-size: 14px;
                color: #ffffff;
            }
            QLineEdit {
                border: 1px solid #ffffff;
                border-radius: 5px;
                padding: 5px;
                font-family: 'Arial';
                font-size: 14px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-family: 'Arial';
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.setLayout(layout)

    def validate_login(self):
        username = self.input_username.text()
        password = self.input_password.text()

        if username == "admin" and password == "password":
            self.main_window.show_main_window()
        else:
            QMessageBox.warning(self, "Ошибка входа", "Неправильный логин или пароль")


class MainWindow(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label_title = QLabel("Расписание с ценами")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setStyleSheet("font-size: 24px; color: #ffffff; font-weight: bold;")

        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(["Время", "Цена"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: rgba(255, 255, 255, 0.8);
                border: 1px solid #ffffff;
                font-family: 'Arial';
                font-size: 14px;
            }
        """)

        self.load_data()

        # Кнопки управления
        self.btn_add = QPushButton("Добавить")
        self.btn_edit = QPushButton("Редактировать")
        self.btn_delete = QPushButton("Удалить")
        self.btn_sort = QPushButton("Сортировать")
        self.btn_back = QPushButton("Назад")  # Кнопка назад

        self.btn_add.clicked.connect(self.add_row)
        self.btn_edit.clicked.connect(self.edit_row)
        self.btn_delete.clicked.connect(self.delete_row)
        self.btn_sort.clicked.connect(self.sort_table)
        self.btn_back.clicked.connect(self.go_back)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_add)
        button_layout.addWidget(self.btn_edit)
        button_layout.addWidget(self.btn_delete)
        button_layout.addWidget(self.btn_sort)
        button_layout.addWidget(self.btn_back)

        layout.addWidget(self.label_title)
        layout.addWidget(self.table)
        layout.addLayout(button_layout)

        self.setStyleSheet("""
            QPushButton {
                background-color: #007BFF;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-family: 'Arial';
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        self.setLayout(layout)

    def load_data(self):
        data = [
            ("9:00", "5500₽ за 4-х"),
            ("10:20", "5500₽ за 4-х"),
            ("11:40", "5500₽ за 4-х (6000₽ по субботам и воскресеньям)"),
            ("13:00", "6000₽ за 4-х"),
            ("14:20", "6000₽ за 4-х"),
            ("15:40", "6000₽ за 4-х (6500₽ по субботам и воскресеньям)"),
            ("17:00", "6500₽ за 4-х"),
            ("18:20", "6500₽ за 4-х"),
            ("19:40", "6500₽ за 4-х"),
            ("21:00", "7000₽ за 4-х"),
            ("22:20", "7000₽ за 4-х"),
            ("23:40", "7500₽ за 4-х"),
            ("1:00", "7500₽ за 4-х"),
            ("2:20", "8000₽ за 4-х"),
            ("3:40", "8000₽ за 4-х"),
        ]
        for time, price in data:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(time))
            self.table.setItem(row_position, 1, QTableWidgetItem(price))

    def add_row(self):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem("Новое время"))
        self.table.setItem(row_position, 1, QTableWidgetItem("Новая цена"))

    def edit_row(self):
        current_row = self.table.currentRow()
        if current_row == -1:
            QMessageBox.warning(self, "Ошибка", "Выберите строку для редактирования")
            return

        time, ok_time = QInputDialog.getText(self, "Редактировать", "Введите новое время:")
        price, ok_price = QInputDialog.getText(self, "Редактировать", "Введите новую цену:")

        if ok_time and ok_price:
            self.table.setItem(current_row, 0, QTableWidgetItem(time))
            self.table.setItem(current_row, 1, QTableWidgetItem(price))

    def delete_row(self):
        current_row = self.table.currentRow()
        if current_row == -1:
            QMessageBox.warning(self, "Ошибка", "Выберите строку для удаления")
            return
        self.table.removeRow(current_row)

    def sort_table(self):
        self.table.sortItems(0, Qt.AscendingOrder)

    def go_back(self):
        """Возврат к экрану авторизации."""
        self.main_app.show_login_window()


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Приложение с расписанием и ценами")
        self.setGeometry(200, 200, 800, 600)

        gradient = QLinearGradient(0, 0, 0, 1)
        gradient.setColorAt(0.0, QColor(0, 128, 255))
        gradient.setColorAt(1.0, QColor(0, 64, 128))

        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(palette)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.login_window = LoginWindow(self)
        self.main_window = MainWindow(self)

        self.stacked_widget.addWidget(self.login_window)
        self.stacked_widget.addWidget(self.main_window)

    def show_main_window(self):
        self.stacked_widget.setCurrentWidget(self.main_window)

    def show_login_window(self):
        self.stacked_widget.setCurrentWidget(self.login_window)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())
