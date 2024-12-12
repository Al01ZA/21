import sys  
# Импорт модуля sys, который предоставляет доступ к параметрам и функциям системы, например, для работы с аргументами командной строки.

from PyQt5.QtWidgets import (  
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel,
    QLineEdit, QTableWidget, QTableWidgetItem, QHBoxLayout, QStackedWidget, QMessageBox, QInputDialog
)
# Импорт модулей из PyQt5 для создания интерфейсов.  
# - `QApplication`: основной класс для запуска приложения.  
# - `QMainWindow`: предоставляет каркас главного окна с меню, статусной строкой и т. д.  
# - `QWidget`: базовый класс для создания элементов пользовательского интерфейса.  
# - `QVBoxLayout` и `QHBoxLayout`: менеджеры компоновки для размещения элементов по вертикали и горизонтали.  
# - `QPushButton`: кнопка.  
# - `QLabel`: текстовый или графический ярлык.  
# - `QLineEdit`: однострочное текстовое поле.  
# - `QTableWidget` и `QTableWidgetItem`: таблица с ячейками для ввода данных.  
# - `QStackedWidget`: виджет, позволяющий переключаться между несколькими страницами.  
# - `QMessageBox`: всплывающее окно для вывода сообщений.  
# - `QInputDialog`: диалог для ввода текста.

from PyQt5.QtCore import Qt  
# Импорт модуля для управления основными аспектами приложения: выравнивание текста, события, клавиши и другие базовые функции.

from PyQt5.QtGui import QFont, QPalette, QLinearGradient, QColor, QBrush  
# Импорт графических инструментов.  
# - `QFont`: задаёт стиль и размер шрифта.  
# - `QPalette`: управляет цветовой палитрой приложения.  
# - `QLinearGradient`: создаёт линейные градиенты для раскраски объектов.  
# - `QColor`: определяет цвета (RGB, HSL и т. д.).  
# - `QBrush`: используется для заливки объектов цветом, градиентом или текстурой.



class LoginWindow(QWidget):  
    # Создаёт окно авторизации, которое является наследником `QWidget`.

    def __init__(self, main_window):  
        super().__init__()  
        # Вызывает конструктор родительского класса `QWidget`.  
        self.main_window = main_window  
        # Сохраняет ссылку на главное окно, чтобы взаимодействовать с ним после успешной авторизации.  
        self.init_ui()  
        # Инициализирует пользовательский интерфейс.

    def init_ui(self):  
        layout = QVBoxLayout()  
        # Создаёт вертикальный менеджер компоновки для упорядочивания элементов окна.

        self.label_username = QLabel("Логин:")  
        # Добавляет метку для поля ввода логина.  
        self.input_username = QLineEdit()  
        # Добавляет однострочное текстовое поле для ввода логина.

        self.label_password = QLabel("Пароль:")  
        # Добавляет метку для поля ввода пароля.  
        self.input_password = QLineEdit()  
        # Добавляет однострочное текстовое поле для ввода пароля.  
        self.input_password.setEchoMode(QLineEdit.Password)  
        # Устанавливает режим скрытия текста в поле пароля, чтобы отображались только символы типа "•••".

        self.btn_login = QPushButton("Войти")  
        # Создаёт кнопку для авторизации.  
        self.btn_login.clicked.connect(self.validate_login)  
        # Подключает метод `validate_login` для обработки нажатия на кнопку.

        layout.addWidget(self.label_username)  
        # Добавляет метку логина в компоновку.  
        layout.addWidget(self.input_username)  
        # Добавляет текстовое поле логина в компоновку.  
        layout.addWidget(self.label_password)  
        # Добавляет метку пароля в компоновку.  
        layout.addWidget(self.input_password)  
        # Добавляет текстовое поле пароля в компоновку.  
        layout.addWidget(self.btn_login)  
        # Добавляет кнопку авторизации в компоновку.

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
        # Устанавливает стиль для всех элементов окна.  
        # - `QLabel`: задаёт шрифт, цвет и размер текста.  
        # - `QLineEdit`: добавляет рамку, закруглённые края и отступы.  
        # - `QPushButton`: задаёт цвет фона, текста и стиль при наведении мыши.  

        self.setLayout(layout)  
        # Устанавливает основную компоновку для окна.


    def validate_login(self):  
    # Метод для проверки введённых логина и пароля.

    username = self.input_username.text()  
    # Получает текст из текстового поля логина.  
    password = self.input_password.text()  
    # Получает текст из текстового поля пароля.

    if username == "admin" and password == "password":  
        # Проверяет, совпадают ли введённые логин и пароль с заданными значениями ("admin" и "password").  
        
        self.main_window.show_main_window()  
        # Если данные корректны, вызывается метод главного окна, чтобы открыть основное окно программы.
    else:  
        QMessageBox.warning(self, "Ошибка входа", "Неправильный логин или пароль")  
        # Если логин или пароль неверны, отображается предупреждающее сообщение.
        # `QMessageBox.warning` показывает окно с заголовком "Ошибка входа" и текстом "Неправильный логин или пароль".



class MainWindow(QWidget):  
    # Класс представляет основное окно приложения, отображающее расписание с ценами.

    def __init__(self, main_app):  
        super().__init__()  
        self.main_app = main_app  
        # Сохраняет ссылку на основное приложение, чтобы при необходимости взаимодействовать с ним.  
        self.init_ui()  
        # Вызывает метод для инициализации пользовательского интерфейса.

    def init_ui(self):  
        layout = QVBoxLayout()  
        # Основной вертикальный макет для размещения виджетов в окне.

        self.label_title = QLabel("Расписание с ценами")  
        # Создаёт текстовую метку для заголовка окна.  
        self.label_title.setAlignment(Qt.AlignCenter)  
        # Устанавливает выравнивание текста по центру.  
        self.label_title.setStyleSheet("font-size: 24px; color: #ffffff; font-weight: bold;")  
        # Настраивает стиль заголовка: крупный белый жирный текст.

        self.table = QTableWidget(0, 2)  
        # Создаёт таблицу с нулевым количеством строк и двумя столбцами.  
        self.table.setHorizontalHeaderLabels(["Время", "Цена"])  
        # Устанавливает названия столбцов таблицы: "Время" и "Цена".  
        self.table.horizontalHeader().setStretchLastSection(True)  
        # Настраивает последний столбец таблицы так, чтобы он занимал оставшееся пространство.  
        self.table.setStyleSheet("""  
            QTableWidget {  
                background-color: rgba(255, 255, 255, 0.8);  
                # Устанавливает полупрозрачный белый фон.  
                border: 1px solid #ffffff;  
                # Белая рамка вокруг таблицы.  
                font-family: 'Arial';  
                font-size: 14px;  
                # Настраивает шрифт содержимого таблицы.  
            }  
        """)  
        # Устанавливает стиль таблицы.


        self.load_data()  
        # Вызывает метод `load_data`, который загружает данные в таблицу.  

        # Кнопки управления  
        self.btn_add = QPushButton("Добавить")  
        # Кнопка для добавления новой строки в таблицу.  
        self.btn_edit = QPushButton("Редактировать")  
        # Кнопка для редактирования выбранной строки таблицы.  
        self.btn_delete = QPushButton("Удалить")  
        # Кнопка для удаления выбранной строки таблицы.  
        self.btn_sort = QPushButton("Сортировать")  
        # Кнопка для сортировки данных в таблице.  
        self.btn_back = QPushButton("Назад")  
        # Кнопка для возврата к предыдущему окну.  

        # Связываем кнопки с соответствующими методами обработки событий.  
        self.btn_add.clicked.connect(self.add_row)  
        # При нажатии на кнопку "Добавить" вызывается метод `add_row`.  
        self.btn_edit.clicked.connect(self.edit_row)  
        # При нажатии на кнопку "Редактировать" вызывается метод `edit_row`.  
        self.btn_delete.clicked.connect(self.delete_row)  
        # При нажатии на кнопку "Удалить" вызывается метод `delete_row`.  
        self.btn_sort.clicked.connect(self.sort_table)  
        # При нажатии на кнопку "Сортировать" вызывается метод `sort_table`.  
        self.btn_back.clicked.connect(self.go_back)  
        # При нажатии на кнопку "Назад" вызывается метод `go_back`.  

        # Макет для кнопок  
        button_layout = QHBoxLayout()  
        # Создаёт горизонтальный макет для размещения кнопок в одном ряду.  

        button_layout.addWidget(self.btn_add)  
        # Добавляет кнопку "Добавить" в макет.  
        button_layout.addWidget(self.btn_edit)  
        # Добавляет кнопку "Редактировать" в макет.  
        button_layout.addWidget(self.btn_delete)  
        # Добавляет кнопку "Удалить" в макет.  
        button_layout.addWidget(self.btn_sort)  
        # Добавляет кнопку "Сортировать" в макет.  
        button_layout.addWidget(self.btn_back)  
        # Добавляет кнопку "Назад" в макет.  

        layout.addWidget(self.label_title)  
        # Добавляет заголовок в основной макет.  
        layout.addWidget(self.table)  
        # Добавляет таблицу в основной макет.  
        layout.addLayout(button_layout)  
        # Добавляет макет с кнопками в основной макет.


        self.setStyleSheet("""  
            QPushButton {  
                background-color: #007BFF;  
                # Задает синий цвет фона для кнопок.  
                color: white;  
                # Устанавливает белый цвет текста кнопок.  
                border-radius: 5px;  
                # Скругляет углы кнопок.  
                padding: 10px;  
                # Устанавливает отступы внутри кнопок для более приятного внешнего вида.  
                font-family: 'Arial';  
                # Определяет шрифт текста кнопок.  
                font-size: 14px;  
                # Устанавливает размер шрифта кнопок.  
            }  
            QPushButton:hover {  
                background-color: #0056b3;  
                # Изменяет цвет фона кнопок при наведении мыши.  
            }  
        """)  
        # Устанавливает стили кнопок, применяя единый дизайн ко всем кнопкам окна.  

    self.setLayout(layout)  
    # Применяет вертикальный макет `layout` к главному виджету окна.  

    def load_data(self):  
        data = [  
            # Предопределенный список данных для заполнения таблицы.  
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
        # Содержит данные расписания с ценами: время и соответствующая стоимость.  

        for time, price in data:  
            row_position = self.table.rowCount()  
            # Определяет текущую позицию для добавления новой строки в таблицу.  
            self.table.insertRow(row_position)  
            # Вставляет новую строку в таблицу на позицию `row_position`.  
            self.table.setItem(row_position, 0, QTableWidgetItem(time))  
            # Добавляет значение времени в первый столбец новой строки.  
            self.table.setItem(row_position, 1, QTableWidgetItem(price))  
            # Добавляет значение цены во второй столбец новой строки.  


    def add_row(self):  
        row_position = self.table.rowCount()  
        # Получает текущее количество строк в таблице, чтобы определить позицию для новой строки.  

        self.table.insertRow(row_position)  
        # Вставляет новую строку в таблицу на позицию `row_position`.  

        self.table.setItem(row_position, 0, QTableWidgetItem("Новое время"))  
        # Добавляет в первый столбец новой строки значение "Новое время".  
        # Это временный текст, который пользователь может заменить.  

        self.table.setItem(row_position, 1, QTableWidgetItem("Новая цена"))  
        # Добавляет во второй столбец новой строки значение "Новая цена".  
        # Аналогично, пользователь может отредактировать эту ячейку позже.  

    def edit_row(self):  
        current_row = self.table.currentRow()  
        # Получает индекс текущей выбранной строки в таблице.  
        # Если строка не выбрана, возвращается -1.  

        if current_row == -1:  
            QMessageBox.warning(self, "Ошибка", "Выберите строку для редактирования")  
            # Если строка не выбрана, выводится предупреждение с помощью QMessageBox.  
            # Метод `return` завершает выполнение функции.  
            return  

        time, ok_time = QInputDialog.getText(self, "Редактировать", "Введите новое время:")  
        # Открывает диалоговое окно для ввода нового значения времени.  
        # Если пользователь нажимает "OK", `ok_time` становится True и возвращает введенное значение.  

        price, ok_price = QInputDialog.getText(self, "Редактировать", "Введите новую цену:")  
        # Аналогично, запрашивается новое значение для цены.  

        if ok_time and ok_price:  
            self.table.setItem(current_row, 0, QTableWidgetItem(time))  
            # Если оба значения введены и подтверждены, обновляет ячейку в текущей строке для столбца "Время".  

            self.table.setItem(current_row, 1, QTableWidgetItem(price))  
            # Аналогично, обновляет ячейку в текущей строке для столбца "Цена".  


    def delete_row(self):  
    current_row = self.table.currentRow()  
    # Получает индекс текущей выбранной строки в таблице.  

        if current_row == -1:  
            QMessageBox.warning(self, "Ошибка", "Выберите строку для удаления")  
            # Если строка не выбрана, выводится предупреждение через QMessageBox.  
            return  
            # Завершает выполнение метода, если строка не выбрана.  

        self.table.removeRow(current_row)  
        # Удаляет выбранную строку из таблицы.  

        def sort_table(self):  
            self.table.sortItems(0, Qt.AscendingOrder)  
            # Сортирует строки таблицы по первому столбцу ("Время") в порядке возрастания.  
            # `Qt.AscendingOrder` означает сортировку от меньшего к большему.  

        def go_back(self):  
            """Возврат к экрану авторизации."""  
            self.main_app.show_login_window()  
            # Вызывает метод `show_login_window` основного приложения,  
            # чтобы перейти обратно к окну авторизации.  



class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Приложение с расписанием и ценами")
        # Устанавливает заголовок главного окна приложения.

        self.setGeometry(200, 200, 800, 600)
        # Устанавливает положение окна на экране (200, 200) и размер (800x600).

        gradient = QLinearGradient(0, 0, 0, 1)
        gradient.setColorAt(0.0, QColor(0, 128, 255))
        gradient.setColorAt(1.0, QColor(0, 64, 128))
        # Создает градиентный фон: от светло-голубого (сверху) до темно-голубого (снизу).

        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(palette)
        # Применяет градиентный фон как палитру для главного окна.

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        # Создает `QStackedWidget` для переключения между окнами приложения 
        # и устанавливает его как центральный виджет главного окна.

        self.login_window = LoginWindow(self)
        self.main_window = MainWindow(self)
        # Инициализирует окна: авторизации (`LoginWindow`) и главного интерфейса (`MainWindow`).

        self.stacked_widget.addWidget(self.login_window)
        self.stacked_widget.addWidget(self.main_window)
        # Добавляет окна в стек виджетов для управления их отображением.

    def show_main_window(self):
        self.stacked_widget.setCurrentWidget(self.main_window)
        # Переключает отображение на главное окно приложения (`MainWindow`).

    def show_login_window(self):
        self.stacked_widget.setCurrentWidget(self.login_window)
        # Переключает отображение на окно авторизации (`LoginWindow`).


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Создает объект приложения PyQt.

    main_app = MainApp()
    main_app.show()
    # Инициализирует и показывает главное окно приложения.

    sys.exit(app.exec_())
    # Запускает основной цикл событий приложения и завершает программу после его окончания.

