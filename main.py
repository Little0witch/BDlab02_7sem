import sys
import psycopg2
import os
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QSplitter, \
    QTableWidget, QTableWidgetItem, QMessageBox, QAction, QComboBox, QLineEdit, QCheckBox, QHBoxLayout, QPushButton, \
    QHeaderView, QDialog, QFormLayout, QFileDialog, QInputDialog, QDialogButtonBox
from PyQt5.QtWidgets import QDialog, QShortcut, QToolBar
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QIcon, QPixmap, QColor, QKeySequence


class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lab02")
        # self.setWindowIcon(QIcon("54320.png"))
        self.setFixedSize(500, 300)

        # Устанавливаем цвет фона окна
        self.setStyleSheet("background-color: #ff5733;")

        layout = QVBoxLayout()
        info_button = QPushButton()
        # info_button.setIcon(QIcon("2.png"))
        info_button.clicked.connect(self.show_info_dialog)
        info_button.setStyleSheet("border: none;")  # Убираем границу кнопки
        layout.addWidget(info_button, alignment=Qt.AlignTop | Qt.AlignRight)
        layout.setSpacing(5)

        label = QLabel("Выберите необходимый вам режим работы:")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 12pt;")  # Установка размера шрифта
        layout.addWidget(label)

        button1 = QPushButton("Редактирование")
        button1.setStyleSheet(
            """
            font-size: 11pt;                /* Размер шрифта */
            border-radius: 10px;            /* Закругление краев */
            background-color: #5cb85c;      /* Цвет фона кнопки */
            padding: 10;
            color: white;                   /* Цвет текста */
            border: none;                   /* Убираем границу кнопки */
            """
        )
        button1.setMaximumWidth(250)  # Устанавливаем максимальную ширину в 250 пикселей
        layout.addWidget(button1, alignment=Qt.AlignHCenter)  # Выравниваем кнопку по центру строки
        button1.clicked.connect(self.show_main1_window)
        # layout.addWidget(button1)

        button2 = QPushButton("Просмотр")
        # button2.setStyleSheet("font-size: 11pt;")
        button2.setStyleSheet(
            """
            font-size: 11pt;                /* Размер шрифта */
            border-radius: 10px;            /* Закругление краев */
            padding: 10;
            background-color: #5cb85c;      /* Цвет фона кнопки */
            color: white;                   /* Цвет текста */
            border: none;                   /* Убираем границу кнопки */
            """
        )
        button2.setMaximumWidth(250)  # Устанавливаем максимальную ширину в 250 пикселей
        layout.addWidget(button2, alignment=Qt.AlignHCenter)  # Выравниваем кнопку по центру строки
        button2.clicked.connect(self.show_main2_window)
        # layout.addWidget(button2)

        button3 = QPushButton("Удаления")
        # button3.setStyleSheet("font-size: 11pt;")
        button3.setStyleSheet(
            """
            font-size: 11pt;                /* Размер шрифта */
            border-radius: 10px;            /* Закругление краев */
            padding: 10;
            background-color: #5cb85c;      /* Цвет фона кнопки */
            color: white;                   /* Цвет текста */
            border: none;                   /* Убираем границу кнопки */
            """
        )
        button3.setMaximumWidth(250)  # Устанавливаем максимальную ширину в 250 пикселей
        layout.addWidget(button3, alignment=Qt.AlignHCenter)  # Выравниваем кнопку по центру строки
        button3.clicked.connect(self.show_main3_window)
        # layout.addWidget(button3)

        # button4 = QPushButton("Выбор записи")
        # button4.clicked.connect(self.show_main4_window)
        # layout.addWidget(button4)

        button5 = QPushButton("Пакетный режим")
        # button5.setStyleSheet("font-size: 11pt;")
        # button5.setStyleSheet("")
        button5.setStyleSheet(
            """
            font-size: 11pt;                /* Размер шрифта */
            border-radius: 10px;            /* Закругление краев */
            padding: 10;
            background-color: #5cb85c;      /* Цвет фона кнопки */
            color: white;                   /* Цвет текста */
            border: none;                   /* Убираем границу кнопки */
            """
        )
        button5.setMaximumWidth(250)  # Устанавливаем максимальную ширину в 250 пикселей
        layout.addWidget(button5, alignment=Qt.AlignHCenter)  # Выравниваем кнопку по центру строки
        button5.clicked.connect(self.show_main5_window)
        # layout.addWidget(button5)

        button6 = QPushButton("Выход")
        # button6.setStyleSheet("background-color: #ff2000; font-size: 11pt;")
        button6.setStyleSheet(
            """
            font-size: 11pt;                /* Размер шрифта */
            border-radius: 10px;            /* Закругление краев */
            padding: 10;
            background-color: #ff2000;      /* Цвет фона кнопки */
            color: white;                   /* Цвет текста */
            border: none;                   /* Убираем границу кнопки */
            """
        )
        button6.setMaximumWidth(250)  # Устанавливаем максимальную ширину в 250 пикселей
        layout.addWidget(button6, alignment=Qt.AlignHCenter)  # Выравниваем кнопку по центру строки
        button6.clicked.connect(self.show_main6_window)
        # layout.addWidget(button6)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Установка фокуса на кнопках для активации клавишей Enter
        button1.setFocus()
        button1.setDefault(True)
        button1.setAutoDefault(True)
        info_button.setAutoDefault(True)
        button2.setAutoDefault(True)
        button3.setAutoDefault(True)
        # button4.setAutoDefault(True)
        button5.setAutoDefault(True)
        button6.setAutoDefault(True)

    def show_info_dialog(self):
        QMessageBox.information(self, "Hot-keys", "Ctrl+Q - выход из Pull-Down меню\n"
                                                  "Ctrl+T - навигация по таблице\n"
                                                  "Ctrl+↑ или Ctrl+↓ - навигация по виджетам ")

    def show_main1_window(self):
        self.main_window = MainWindow1()
        self.main_window.show()
        self.close()

    def show_main2_window(self):
        self.main_window = (MainWindow2())
        self.main_window.show()
        self.close()

    def show_main3_window(self):
        self.main_window = (MainWindow3())
        self.main_window.show()
        self.close()

    def show_main4_window(self):
        self.main_window = (MainWindow4())
        self.main_window.show()
        self.close()

    def show_main5_window(self):
        self.main_window = (MainWindow5())
        self.main_window.show()
        self.close()

    def show_main6_window(self):
        reply = QMessageBox.warning(self, 'Вы точно хотите выйти?', 'Вы уверены, что хотите закрыть программу?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()


class MainWindow1(QMainWindow):
    def __init__(self):
        try:
            super().__init__()
            self.setWindowTitle("Редактирование")
            self.setWindowIcon(QIcon("54320.png"))
            self.setFixedSize(800, 800)

            self.setStyleSheet("background-color: #ff5733;")

            self.table = None
            self.row = None
            self.columns = None
            self.old_data = None
            self.new_data = None
            self.last_operation = None

            # Create a QSplitter to divide the window into two parts
            self.splitter = QSplitter(Qt.Vertical)
            self.setCentralWidget(self.splitter)

            # Top part of the splitter - Table view
            top_widget = QWidget()
            top_layout = QVBoxLayout()
            self.combo_box = QComboBox()
            top_layout.addWidget(self.combo_box)
            self.combo_box.currentIndexChanged.connect(self.load_data)
            top_widget.setLayout(top_layout)
            self.splitter.addWidget(top_widget)

            # Populate the top part with the table
            self.table_widget = QTableWidget()
            columns = self.add_pull_down()
            self.table_widget.setRowCount(0)
            top_layout.addWidget(self.table_widget)
            self.table_widget.setMinimumHeight(400)
            self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.table_widget.horizontalHeader().sectionClicked.connect(self.sort_table_by_column)

            # Bottom part of the splitter
            bottom_widget = QWidget()
            bottom_layout = QVBoxLayout()
            bottom_widget.setLayout(bottom_layout)
            self.splitter.addWidget(bottom_widget)

            # Create a QHBoxLayout for input field, Button 2, and a search button
            hbox1 = QHBoxLayout()
            self.input_field = QLineEdit()
            self.input_field.setFixedWidth(385)  # Set fixed width for input field
            button2 = QPushButton("Выход из режима")
            button2.setStyleSheet(
                """
                font-size: 11pt;                /* Размер шрифта */
                border-radius: 10px;            /* Закругление краев */
                background-color: #ff2000;      /* Цвет фона кнопки */
                padding: 10;
                color: white;                   /* Цвет текста */
                border: none;                   /* Убираем границу кнопки */
                """
            )
            button2.setMaximumWidth(250)  # Устанавливаем максимальную ширину в 250 пикселей
            button2.clicked.connect(self.show_start_window)
            self.hot_key = QPushButton("Горячие клавиши")
            self.hot_key.clicked.connect(self.inform_action)
            self.hot_key.setStyleSheet(
                """
                font-size: 11pt;                /* Размер шрифта */
                border-radius: 10px;            /* Закругление краев */
                background-color: #5cb85c;      /* Цвет фона кнопки */
                padding: 10px;                  /* Внутренний отступ */
                color: white;                   /* Цвет текста */
                border: none;                   /* Убираем границу кнопки */
                """
            )
            # Установка максимальной ширины кнопки
            self.hot_key.setMaximumWidth(250)
            hbox1.addWidget(self.input_field)
            self.input_field.textChanged.connect(self.highlight_matches)
            hbox1.addWidget(self.hot_key)
            hbox1.addWidget(button2)
            bottom_layout.addLayout(hbox1)

            # Add spacing between the two rows
            bottom_layout.addSpacing(10)

            # Create QHBoxLayout for buttons 3, 4, and 5
            hbox2 = QHBoxLayout()
            button3 = QPushButton(f"Редактирование")
            button3.setStyleSheet(
                """
                font-size: 11pt;                /* Размер шрифта */
                border-radius: 10px;            /* Закругление краев */
                background-color: #5cb85c;      /* Цвет фона кнопки */
                padding: 10;
                color: white;                   /* Цвет текста */
                border: none;                   /* Убираем границу кнопки */
                """
            )
            button3.setMaximumWidth(250)
            button4 = QPushButton(f"Вставка")
            button4.setStyleSheet(
                """
                font-size: 11pt;                /* Размер шрифта */
                border-radius: 10px;            /* Закругление краев */
                background-color: #5cb85c;      /* Цвет фона кнопки */
                padding: 10;
                color: white;                   /* Цвет текста */
                border: none;                   /* Убираем границу кнопки */
                """
            )
            button4.setMaximumWidth(250)
            button5 = QPushButton(f"Удаление")
            button5.setStyleSheet(
                """
                font-size: 11pt;                /* Размер шрифта */
                border-radius: 10px;            /* Закругление краев */
                background-color: #5cb85c;      /* Цвет фона кнопки */
                padding: 10;
                color: white;                   /* Цвет текста */
                border: none;                   /* Убираем границу кнопки */
                """
            )
            button5.setMaximumWidth(250)
            button6 = QPushButton(f"Отмена")
            button6.setStyleSheet(
                """
                font-size: 11pt;                /* Размер шрифта */
                border-radius: 10px;            /* Закругление краев */
                background-color: #5cb85c;      /* Цвет фона кнопки */
                padding: 10;
                color: white;                   /* Цвет текста */
                border: none;                   /* Убираем границу кнопки */
                """
            )
            button6.setMaximumWidth(250)
            button3.clicked.connect(self.editing)
            button4.clicked.connect(self.insert)
            button5.clicked.connect(self.delete)
            button6.clicked.connect(self.cancel)
            hbox2.addWidget(button3)
            hbox2.addWidget(button4)
            hbox2.addWidget(button5)
            hbox2.addWidget(button6)
            bottom_layout.addLayout(hbox2)

            self.hot_key.setAutoDefault(True)
            button2.setAutoDefault(True)
            button3.setAutoDefault(True)
            button4.setAutoDefault(True)
            button5.setAutoDefault(True)
            button6.setAutoDefault(True)

            self.splitter.setStretchFactor(0, 2)
            self.splitter.setStretchFactor(1, 1)
            self.load_data()

            # Connect event filter for handling key events
            QApplication.instance().installEventFilter(self)
            self.pull_down_mode = False

            self.combo_box.setFocus()

        except Exception as e:
            print(f"Ошибка 707: {e}")

    def show_start_window(self):
        self.main_window = StartWindow()
        self.main_window.show()
        self.close()

    def inform_action(self):
        info_text = ("Ctrl+Q - выход из Pull-Down меню\n"
                     "Ctrl+T - навигация по таблице\n"
                     "Ctrl+↑ или Ctrl+↓ - навигация по виджетам ")
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Горячие клавиши")
        msg_box.setText(info_text)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowIcon(QIcon("54320.png"))
        msg_box.exec_()

    def editing(self):
        try:
            selected_row = self.table_widget.currentRow()  # Получаем индекс выбранной строки
            if selected_row >= 0:  # Проверяем, что строка выбрана
                old_data = []
                for column in range(self.table_widget.columnCount()):
                    item = self.table_widget.item(selected_row, column)
                    if item is not None:
                        old_data.append(item.text())  # Добавляем текст элемента в список

                column_names = []
                for column in range(self.table_widget.columnCount()):
                    header_item = self.table_widget.horizontalHeaderItem(column)
                    if header_item is not None:
                        column_names.append(header_item.text())

                dialog = EditDialog(old_data, self)
                if dialog.exec_() == QDialog.Accepted:
                    new_data = dialog.get_new_data()  # Получаем новые данные

                    selected_table = self.combo_box.currentText()
                    result = self.update_database_edit(column_names, old_data, new_data, selected_table)
                    if result == "OK":
                        self.table = self.combo_box.currentText()
                        self.row = selected_row
                        self.columns = column_names
                        self.old_data = old_data
                        self.new_data = new_data
                        self.last_operation = "EDIT"
                        for column, new_value in enumerate(new_data):
                            self.table_widget.setItem(selected_row, column, QTableWidgetItem(new_value))
            else:
                return None  # Если строка не выбрана, возвращаем None
        except Exception as e:
            print(f"Ошибка 303: {e}")

    def update_database_edit(self, column_names, old_data, new_data, selected_table):
        try:
            # Устанавливаем соединение с базой данных
            connection = psycopg2.connect(
                dbname="bank",
                user="postgres",
                password="1234",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()

            sql_query = """UPDATE public.""" + selected_table + """ SET """
            for index, (column, new) in enumerate(zip(column_names, new_data)):
                sql_query += f"{column} = '{new}'"
                if index < len(column_names) - 1:
                    sql_query += ", "
            sql_query += " WHERE "
            for index, (column, old) in enumerate(zip(column_names, old_data)):
                sql_query += f"{column} = '{old}'"
                if index < len(column_names) - 1:
                    sql_query += " AND "

            cursor.execute(sql_query)  # Обновляем данные

            # Сохраняем изменения и закрываем соединение
            connection.commit()
            connection.close()
            return "OK"
        except Exception as e:
            print(f"Ошибка 404: {e}")
            return "ERROR"

    def insert(self):
        try:
            column_names = []
            for column in range(self.table_widget.columnCount()):
                header_item = self.table_widget.horizontalHeaderItem(column)
                if header_item is not None:
                    column_names.append(header_item.text())

            dialog = InsertDialog(column_names, self)
            if dialog.exec_() == QDialog.Accepted:
                new_data = dialog.get_values()  # Получаем новые данные

                selected_table = self.combo_box.currentText()
                result = self.update_database_insert(column_names, new_data, selected_table)
                if result == "OK":
                    self.table = self.combo_box.currentText()
                    self.columns = column_names
                    self.new_data = new_data
                    self.last_operation = "INSERT"
                    row_position = self.table_widget.rowCount()
                    self.table_widget.insertRow(row_position)
                    self.row = row_position
                    for column, value in enumerate(new_data.values()):
                        self.table_widget.setItem(row_position, column, QTableWidgetItem(value))

        except Exception as e:
            print(f"Ошибка 303: {e}")

    def update_database_insert(self, column_names, new_data, selected_table):
        try:
            # Устанавливаем соединение с базой данных
            connection = psycopg2.connect(
                dbname="bank",
                user="postgres",
                password="1234",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()

            # Формируем SQL-запрос с помощью конкатенации
            sql_query = "INSERT INTO public." + selected_table + " ("
            sql_query += ", ".join(column_names) + ") VALUES ("

            # Конкатенируем значения для SQL-запроса
            values = []
            for value in new_data.values():
                # Приводим значение к строке и экранируем одинарные кавычки
                values.append("'" + str(value).replace("'", "''") + "'")

            sql_query += ", ".join(values) + ");"

            # Выполняем запрос без параметров
            cursor.execute(sql_query)

            # Сохраняем изменения и закрываем соединение
            connection.commit()
            connection.close()
            return "OK"
        except Exception as e:
            print(f"Ошибка 404: {e}")
            return "ERROR"

    def delete(self):
        try:
            selected_row = self.table_widget.currentRow()  # Получаем индекс выбранной строки
            if selected_row >= 0:  # Проверяем, что строка выбрана
                old_data = []
                for column in range(self.table_widget.columnCount()):
                    item = self.table_widget.item(selected_row, column)
                    if item is not None:
                        old_data.append(item.text())  # Добавляем текст элемента в список

                column_names = []
                for column in range(self.table_widget.columnCount()):
                    header_item = self.table_widget.horizontalHeaderItem(column)
                    if header_item is not None:
                        column_names.append(header_item.text())

                selected_table = self.combo_box.currentText()
                result = self.update_database_delete(column_names, old_data, selected_table)
                if result == "OK":
                    self.table = self.combo_box.currentText()
                    self.columns = column_names
                    self.row = self.table_widget.currentRow()
                    self.old_data = old_data
                    self.last_operation = "DELETE"
                    self.table_widget.removeRow(selected_row)
            else:
                return None  # Если строка не выбрана, возвращаем None
        except Exception as e:
            print(f"Ошибка 303: {e}")

    def update_database_delete(self, column_names, old_data, selected_table):
        try:
            # Устанавливаем соединение с базой данных
            connection = psycopg2.connect(
                dbname="bank",
                user="postgres",
                password="1234",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()

            # Создаем условие для поиска записи
            sql_query = f"""
                SELECT *
                FROM public.{selected_table}
                WHERE
            """
            for index, (column, old) in enumerate(zip(column_names, old_data)):
                sql_query += f"public.{selected_table}.{column} = '{old}'"
                if index < len(column_names) - 1:
                    sql_query += " AND "
            sql_query += ";"

            # Выполняем запрос для получения записи
            cursor.execute(sql_query)
            record = cursor.fetchone()

            if record is None:
                print("Запись не найдена.")
                return "ERROR"

            # Запрос для получения первичного ключа
            primary_key_query = f"""
                SELECT kcu.column_name
                FROM information_schema.table_constraints AS tc
                JOIN information_schema.key_column_usage AS kcu ON tc.constraint_name = kcu.constraint_name
                WHERE tc.constraint_type = 'PRIMARY KEY' AND tc.table_name = '{selected_table}' AND tc.table_schema = 'public';
            """

            cursor.execute(primary_key_query)
            primary_key_column = cursor.fetchone()

            if primary_key_column is None:
                print("Первичный ключ не найден.")
                return "ERROR"

            primary_key_column_name = primary_key_column[0]

            # Запрос для получения внешних ключей, связанных с таблицей
            foreign_keys_query = f"""
                SELECT kcu.table_name AS child_table, kcu.column_name AS child_column
                FROM information_schema.table_constraints AS tc
                JOIN information_schema.key_column_usage AS kcu ON tc.constraint_name = kcu.constraint_name
                JOIN information_schema.constraint_column_usage AS ccu ON ccu.constraint_name = tc.constraint_name
                WHERE tc.constraint_type = 'FOREIGN KEY' AND ccu.table_name = '{selected_table}';
            """

            cursor.execute(foreign_keys_query)
            foreign_keys = cursor.fetchall()

            has_relationships = False

            # Проверяем наличие связанных записей для каждого внешнего ключа
            for child_table, child_column in foreign_keys:
                check_relationships_query = f"""
                    SELECT COUNT(*) > 0
                    FROM public.{child_table}
                    WHERE {child_column} IN (
                        SELECT {primary_key_column_name} FROM public.{selected_table} WHERE
                """
                for index, (column, old) in enumerate(zip(column_names, old_data)):
                    check_relationships_query += f"{column} = '{old}'"
                    if index < len(column_names) - 1:
                        check_relationships_query += " AND "
                check_relationships_query += ");"

                cursor.execute(check_relationships_query)
                if cursor.fetchone()[0]:
                    has_relationships = True
                    break

            if has_relationships:
                print("Запись не может быть удалена, так как существуют связанные записи.")
                return "ERROR"
            else:
                conditions = []
                for col, value in zip(column_names, old_data):
                    # Приводим значение к строке и экранируем одинарные кавычки
                    escaped_value = "'" + str(value).replace("'", "''") + "'"
                    conditions.append(f"{col} = {escaped_value}")

                conditions_str = " AND ".join(conditions)
                sql_query = "DELETE FROM public." + selected_table + " WHERE " + conditions_str + ";"
                print(sql_query)
                # Выполняем запрос без параметров
                cursor.execute(sql_query)

                # Сохраняем изменения и закрываем соединение
                connection.commit()
                connection.close()
                return "OK"

        except Exception as e:
            print(f"Ошибка 404: {e}")
            return "ERROR"

    def cancel(self):
        try:
            need_update_table = None

            if self.table == self.combo_box.currentText():
                need_update_table = 1

            if self.last_operation == "EDIT":
                result = self.update_database_edit(self.columns, self.new_data, self.old_data, self.table)
                if need_update_table == 1:
                    for column_index, old_value in enumerate(self.old_data):  # Изменяем на old_value
                        self.table_widget.setItem(self.row, column_index, QTableWidgetItem(
                            old_value))  # Используем old_value вместо self.old_data
            elif self.last_operation == "INSERT":
                result = self.update_database_delete(self.columns, self.new_data.values(), self.table)
                if need_update_table == 1:
                    self.table_widget.removeRow(self.row)
            elif self.last_operation == "DELETE":
                data_dict = {self.columns[i]: self.old_data[i] for i in range(len(self.old_data))}
                result = self.update_database_insert(self.columns, data_dict, self.table)  # Исправлено на delete
                if need_update_table == 1:
                    self.table_widget.insertRow(self.row)  # Вставляем новую строку
                    for column_index, value in enumerate(self.old_data):  # Исправлено на old_data
                        self.table_widget.setItem(self.row, column_index,
                                                  QTableWidgetItem(value))  # Используем column_index

            self.table = None
            self.row = None
            self.columns = None
            self.old_data = None
            self.new_data = None
            self.last_operation = None
        except Exception as e:
            print(f"Ошибка 303: {e}")

    def highlight_matches(self):
        try:
            search_text = self.input_field.text().lower()  # Получаем текст из поля ввода
            for row in range(self.table_widget.rowCount()):
                for column in range(self.table_widget.columnCount()):
                    item = self.table_widget.item(row, column)
                    if item is not None:
                        # Сбрасываем цвет фона для всех ячеек
                        item.setBackground(QColor("white"))

                        # Проверяем на совпадение, если текст для поиска не пустой
                        if search_text and search_text in item.text().lower():
                            item.setBackground(QColor("yellow"))  # Подсвечиваем совпадения
        except Exception as e:
            print(f"Ошибка 707: {e}")

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Down:
                if self.pull_down_mode:
                    self.focusNextChild()
                    return True

            elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Up:
                if self.pull_down_mode:
                    self.focusPreviousChild()
                    return True

            elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_T:
                if not self.table_widget.hasFocus():
                    self.table_widget.setFocus()

                current_row = self.table_widget.currentRow()
                total_rows = self.table_widget.rowCount()

                if obj == self.table_widget and event.key() in (Qt.Key_Up, Qt.Key_Down):
                    if total_rows > 0:
                        if event.key() == Qt.Key_Down:
                            next_row = (current_row + 1) % total_rows
                        elif event.key() == Qt.Key_Up:
                            next_row = (current_row - 1) % total_rows

                        self.table_widget.setCurrentCell(next_row, 0)
                        return True

            elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Q:
                self.pull_down_mode = not self.pull_down_mode
                if not self.pull_down_mode:
                    self.combo_box.setFocus()
                else:
                    self.setFocus()
                return True

            elif event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
                focused_widget = QApplication.focusWidget()
                if isinstance(focused_widget, QPushButton):
                    focused_widget.click()
                elif self.pull_down_mode:
                    self.pull_down_mode = False
                    self.combo_box.setFocus()
                return True

        return super().eventFilter(obj, event)

    def add_pull_down(self):
        try:
            connection = psycopg2.connect(
                dbname="bank",
                user="postgres",
                password="1234",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()
            # Запрос для получения всех таблиц в схеме 'public'
            query = """
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public';
            """

            cursor.execute(query)
            tables = cursor.fetchall()

            valid_tables = []

            for table in tables:
                table_name = table[0]

                # Запрос для проверки, есть ли столбцы, отличные от внешних ключей
                column_query = f"""
                    SELECT COUNT(*) 
                    FROM information_schema.columns
                    WHERE table_name = %s
                    AND column_name NOT IN (
                        SELECT kcu.column_name
                        FROM information_schema.table_constraints tc
                        JOIN information_schema.key_column_usage kcu
                        ON tc.constraint_name = kcu.constraint_name
                        AND tc.table_name = kcu.table_name
                        WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name = %s
                    );
                """
                cursor.execute(column_query, (table_name, table_name))
                column_count = cursor.fetchone()[0]

                # Если есть хотя бы один столбец, отличный от FK, добавляем таблицу в результат
                if column_count > 0:
                    valid_tables.append(table_name)

            self.combo_box.addItems(valid_tables)
            return valid_tables
        except Exception as e:
            print(f"Ошибка подключения к базе данных: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def load_data(self):
        try:
            connection = psycopg2.connect(
                dbname="bank",
                user="postgres",
                password="1234",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()

            selected_table = self.combo_box.currentText()
            # Запрос для получения названий столбцов таблицы
            query1 = f"""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = %s
            AND column_name NOT IN (
                -- Имена столбцов, которые являются частью первичного ключа
                SELECT kcu.column_name
                FROM information_schema.table_constraints tc
                JOIN information_schema.key_column_usage kcu
                ON tc.constraint_name = kcu.constraint_name
                AND tc.table_name = kcu.table_name
                WHERE tc.constraint_type = 'PRIMARY KEY' AND tc.table_name = %s
            )
            AND column_name NOT IN (
                -- Имена столбцов, которые являются частью внешнего ключа
                SELECT kcu.column_name
                FROM information_schema.table_constraints tc
                JOIN information_schema.key_column_usage kcu
                ON tc.constraint_name = kcu.constraint_name
                AND tc.table_name = kcu.table_name
                WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name = %s
            );
            """
            cursor.execute(query1, (selected_table, selected_table, selected_table))
            columns = cursor.fetchall()
            column_names = [column[0] for column in columns]
            self.table_widget.setColumnCount(len(column_names))
            self.table_widget.setHorizontalHeaderLabels(column_names)
            self.table_widget.setRowCount(0)

            columns_string = ", ".join(column_names)
            query2 = f"SELECT {columns_string} FROM public.{selected_table};"
            cursor.execute(query2)
            rows = cursor.fetchall()

            for row in rows:
                row_position = self.table_widget.rowCount()
                self.table_widget.insertRow(row_position)
                for column in range(len(row)):
                    self.table_widget.setItem(row_position, column, QTableWidgetItem(str(row[column])))

        except Exception as e:
            print(f"Ошибка подключения к базе данных: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def sort_table_by_column(self, logical_index):
        self.table_widget.sortItems(logical_index)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            reply = QMessageBox.warning(self, 'Вы точно хотите выйти?', 'Вы уверены, что хотите закрыть программу?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
                self.close()
            else:
                event.ignore()


class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Просмотр")
        self.setWindowIcon(QIcon("54320.png"))
        self.setFixedSize(800, 800)

        self.setStyleSheet("background-color: #ff5733;")

        # Create a QSplitter to divide the window into two parts
        self.splitter = QSplitter(Qt.Vertical)
        self.setCentralWidget(self.splitter)

        # Top part of the splitter - Table view
        top_widget = QWidget()
        top_layout = QVBoxLayout()
        self.combo_box = QComboBox()
        top_layout.addWidget(self.combo_box)
        self.combo_box.currentIndexChanged.connect(self.load_data)
        top_widget.setLayout(top_layout)
        self.splitter.addWidget(top_widget)

        # Populate the top part with the table
        self.table_widget = QTableWidget()
        columns = self.add_pull_down()
        self.table_widget.setRowCount(0)
        top_layout.addWidget(self.table_widget)
        self.table_widget.setMinimumHeight(400)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.horizontalHeader().sectionClicked.connect(self.sort_table_by_column)
        # Bottom part of the splitter
        bottom_widget = QWidget()
        bottom_layout = QVBoxLayout()
        bottom_widget.setLayout(bottom_layout)
        self.splitter.addWidget(bottom_widget)

        # Create a QHBoxLayout for input field, Button 2, and a search button
        hbox1 = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setFixedWidth(385)  # Set fixed width for input field
        button2 = QPushButton("Выход из режима")
        button2.setStyleSheet(
            """
            font-size: 11pt;                /* Размер шрифта */
            border-radius: 10px;            /* Закругление краев */
            background-color: #ff2000;      /* Цвет фона кнопки */
            padding: 10;
            color: white;                   /* Цвет текста */
            border: none;                   /* Убираем границу кнопки */
            """
        )
        # button2.setMaximumWidth(250)
        button2.clicked.connect(self.show_start_window)
        # Создаем кнопку как атрибут класса
        self.hot_key = QPushButton("Горячие клавиши")

        # Применяем стиль к кнопке
        self.hot_key.setStyleSheet(
            """
            font-size: 11pt;                /* Размер шрифта */
            border-radius: 10px;            /* Закругление краев */
            background-color: #5cb85c;      /* Цвет фона кнопки */
            padding: 10px;                  /* Внутренний отступ */
            color: white;                   /* Цвет текста */
            border: none;                   /* Убираем границу кнопки */
            """
        )
        # Устанавливаем максимальную ширину кнопки
        self.hot_key.setMaximumWidth(250)
        self.hot_key.clicked.connect(self.inform_action)
        self.input_field.textChanged.connect(self.highlight_matches)
        hbox1.addWidget(self.input_field)
        hbox1.addWidget(self.hot_key)
        hbox1.addWidget(button2)
        bottom_layout.addLayout(hbox1)

        # Add spacing between the two rows
        bottom_layout.addSpacing(10)

        self.splitter.setStretchFactor(0, 2)
        self.splitter.setStretchFactor(1, 1)

        button2.setAutoDefault(True)
        self.hot_key.setAutoDefault(True)
        self.load_data()

        # Connect event filter for handling key events
        QApplication.instance().installEventFilter(self)
        self.pull_down_mode = False

        self.combo_box.setFocus()

    def inform_action(self):
        info_text = ("Ctrl+Q - выход из Pull-Down меню\n"
                     "Ctrl+T - навигация по таблице\n"
                     "Ctrl+↑ или Ctrl+↓ - навигация по виджетам ")
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Горячие клавиши")
        msg_box.setText(info_text)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowIcon(QIcon("54320.png"))
        msg_box.exec_()

    def show_start_window(self):
        self.main_window = StartWindow()
        self.main_window.show()
        self.close()

    def highlight_matches(self):
        try:
            search_text = self.input_field.text().lower()  # Получаем текст из поля ввода
            for row in range(self.table_widget.rowCount()):
                for column in range(self.table_widget.columnCount()):
                    item = self.table_widget.item(row, column)
                    if item is not None:
                        # Сбрасываем цвет фона для всех ячеек
                        item.setBackground(QColor("white"))

                        # Проверяем на совпадение, если текст для поиска не пустой
                        if search_text and search_text in item.text().lower():
                            item.setBackground(QColor("yellow"))  # Подсвечиваем совпадения
        except Exception as e:
            print(f"Ошибка 707: {e}")

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Down:
                if self.pull_down_mode:
                    self.focusNextChild()
                    return True

            elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Up:
                if self.pull_down_mode:
                    self.focusPreviousChild()
                    return True

            elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_T:
                if not self.table_widget.hasFocus():
                    self.table_widget.setFocus()

                current_row = self.table_widget.currentRow()
                total_rows = self.table_widget.rowCount()

                if obj == self.table_widget and event.key() in (Qt.Key_Up, Qt.Key_Down):
                    if total_rows > 0:
                        if event.key() == Qt.Key_Down:
                            next_row = (current_row + 1) % total_rows
                        elif event.key() == Qt.Key_Up:
                            next_row = (current_row - 1) % total_rows

                        self.table_widget.setCurrentCell(next_row, 0)
                        return True

            elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Q:
                self.pull_down_mode = not self.pull_down_mode
                if not self.pull_down_mode:
                    self.combo_box.setFocus()
                else:
                    self.setFocus()
                return True

            elif event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
                focused_widget = QApplication.focusWidget()
                if isinstance(focused_widget, QPushButton):
                    focused_widget.click()
                elif self.pull_down_mode:
                    self.pull_down_mode = False
                    self.combo_box.setFocus()
                return True

        return super().eventFilter(obj, event)

    def add_pull_down(self):
        try:
            connection = psycopg2.connect(
                dbname="bank",
                user="postgres",
                password="1234",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()
            # Запрос для получения всех таблиц в схеме 'public'
            query = """
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public';
            """

            cursor.execute(query)
            tables = cursor.fetchall()

            valid_tables = []

            for table in tables:
                table_name = table[0]

                # Запрос для проверки, есть ли столбцы, отличные от внешних ключей
                column_query = f"""
                    SELECT COUNT(*) 
                    FROM information_schema.columns
                    WHERE table_name = %s
                    AND column_name NOT IN (
                        SELECT kcu.column_name
                        FROM information_schema.table_constraints tc
                        JOIN information_schema.key_column_usage kcu
                        ON tc.constraint_name = kcu.constraint_name
                        AND tc.table_name = kcu.table_name
                        WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name = %s
                    );
                """
                cursor.execute(column_query, (table_name, table_name))
                column_count = cursor.fetchone()[0]

                # Если есть хотя бы один столбец, отличный от FK, добавляем таблицу в результат
                if column_count > 0:
                    valid_tables.append(table_name)

            self.combo_box.addItems(valid_tables)
            return valid_tables
        except Exception as e:
            print(f"Ошибка подключения к базе данных: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def load_data(self):
        try:
            connection = psycopg2.connect(
                dbname="bank",
                user="postgres",
                password="1234",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()

            selected_table = self.combo_box.currentText()
            # Запрос для получения названий столбцов таблицы
            query1 = f"""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = %s
            AND column_name NOT IN (
                -- Имена столбцов, которые являются частью первичного ключа
                SELECT kcu.column_name
                FROM information_schema.table_constraints tc
                JOIN information_schema.key_column_usage kcu
                ON tc.constraint_name = kcu.constraint_name
                AND tc.table_name = kcu.table_name
                WHERE tc.constraint_type = 'PRIMARY KEY' AND tc.table_name = %s
            )
            AND column_name NOT IN (
                -- Имена столбцов, которые являются частью внешнего ключа
                SELECT kcu.column_name
                FROM information_schema.table_constraints tc
                JOIN information_schema.key_column_usage kcu
                ON tc.constraint_name = kcu.constraint_name
                AND tc.table_name = kcu.table_name
                WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name = %s
            );
            """
            cursor.execute(query1, (selected_table, selected_table, selected_table))
            columns = cursor.fetchall()
            column_names = [column[0] for column in columns]
            self.table_widget.setColumnCount(len(column_names))
            self.table_widget.setHorizontalHeaderLabels(column_names)
            self.table_widget.setRowCount(0)

            columns_string = ", ".join(column_names)
            query2 = f"SELECT {columns_string} FROM public.{selected_table};"
            cursor.execute(query2)
            rows = cursor.fetchall()

            for row in rows:
                row_position = self.table_widget.rowCount()
                self.table_widget.insertRow(row_position)
                for column in range(len(row)):
                    self.table_widget.setItem(row_position, column, QTableWidgetItem(str(row[column])))

        except Exception as e:
            print(f"Ошибка подключения к базе данных: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def sort_table_by_column(self, logical_index):
        self.table_widget.sortItems(logical_index)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            reply = QMessageBox.warning(self, 'Вы точно хотите выйти?', 'Вы уверены, что хотите закрыть программу?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
                self.close()
            else:
                event.ignore()


class MainWindow3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.good_delete = 0
        self.table = None
        self.row = None
        self.columns = None
        self.old_data = None
        self.new_data = None
        self.last_operation = None
        self.setWindowTitle("Удаление")
        # self.setWindowIcon(QIcon("54320.png"))
        self.setFixedSize(800, 800)

        self.setStyleSheet("background-color: #ff5733;")

        # Create a QSplitter to divide the window into two parts
        self.splitter = QSplitter(Qt.Vertical)
        self.setCentralWidget(self.splitter)

        # Top part of the splitter - Table view
        top_widget = QWidget()
        top_layout = QVBoxLayout()
        self.combo_box = QComboBox()
        top_layout.addWidget(self.combo_box)
        self.combo_box.currentIndexChanged.connect(self.load_data)
        top_widget.setLayout(top_layout)
        self.splitter.addWidget(top_widget)

        # Populate the top part with the table
        self.table_widget = QTableWidget()
        columns = self.add_pull_down()
        self.table_widget.setRowCount(0)
        top_layout.addWidget(self.table_widget)
        self.table_widget.setMinimumHeight(400)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.horizontalHeader().sectionClicked.connect(self.sort_table_by_column)

        # Bottom part of the splitter
        bottom_widget = QWidget()
        bottom_layout = QVBoxLayout()
        bottom_widget.setLayout(bottom_layout)
        self.splitter.addWidget(bottom_widget)

        # Create a QHBoxLayout for input field, Button 2, and a search button
        hbox1 = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setFixedWidth(385)  # Set fixed width for input field
        button2 = QPushButton("Выход из режима")
        button2.setStyleSheet(
            """
            font-size: 11pt;                /* Размер шрифта */
            border-radius: 10px;            /* Закругление краев */
            background-color: #ff2000;      /* Цвет фона кнопки */
            padding: 10;
            color: white;                   /* Цвет текста */
            border: none;                   /* Убираем границу кнопки */
            """
        )
        button2.setMaximumWidth(250)
        button2.clicked.connect(self.show_start_window)
        self.hot_key1 = QPushButton("Горячие клавиши")
        self.hot_key1.setStyleSheet(
            """
            font-size: 11pt;                /* Размер шрифта */
            border-radius: 10px;            /* Закругление краев */
            background-color: #5cb85c;      /* Цвет фона кнопки */
            padding: 10px;                  /* Внутренний отступ */
            color: white;                   /* Цвет текста */
            border: none;                   /* Убираем границу кнопки */
            """
        )
        # Установка максимальной ширины кнопки
        self.hot_key1.setMaximumWidth(250)
        self.hot_key1.clicked.connect(self.inform_action)
        # Применяем стиль к кнопке
        self.hot_key1.setStyleSheet(
            """
            font-size: 11pt;                /* Размер шрифта */
            border-radius: 10px;            /* Закругление краев */
            background-color: #5cb85c;      /* Цвет фона кнопки */
            padding: 10px;                  /* Внутренний отступ */
            color: white;                   /* Цвет текста */
            border: none;                   /* Убираем границу кнопки */
            """
        )
        self.input_field.textChanged.connect(self.highlight_matches)
        hbox1.addWidget(self.input_field)
        hbox1.addWidget(self.hot_key1)
        hbox1.addWidget(button2)
        bottom_layout.addLayout(hbox1)

        # Add spacing between the two rows
        bottom_layout.addSpacing(10)
        hbox2 = QHBoxLayout()
        self.checkbox = QCheckBox("Каскадное удаление")  # Creating a checkbox
        self.button5 = QPushButton("Удаление")
        self.button5.setStyleSheet(
            """
            font-size: 11pt;                /* Размер шрифта */
            border-radius: 10px;            /* Закругление краев */
            background-color: #5cb85c;      /* Цвет фона кнопки */
            padding: 10;
            color: white;                   /* Цвет текста */
            border: none;                   /* Убираем границу кнопки */
            """
        )
        self.button5.setMaximumWidth(250)
        self.button5.clicked.connect(self.delete)
        self.checkbox.stateChanged.connect(self.checkbox_changed)
        self.button6 = QPushButton("Отмена")
        self.button6.setStyleSheet(
            """
            font-size: 11pt;                /* Размер шрифта */
            border-radius: 10px;            /* Закругление краев */
            background-color: #5cb85c;      /* Цвет фона кнопки */
            padding: 10;
            color: white;                   /* Цвет текста */
            border: none;                   /* Убираем границу кнопки */
            """
        )
        self.button6.setMaximumWidth(250)
        self.button6.clicked.connect(self.cancel)
        hbox2.addWidget(self.checkbox)
        hbox2.addWidget(self.button5)
        hbox2.addWidget(self.button6)
        # Add button 5 and checkbox to the bottom layout
        bottom_layout.addLayout(hbox2)
        self.splitter.setStretchFactor(0, 2)
        self.splitter.setStretchFactor(1, 1)

        button2.setAutoDefault(True)
        self.hot_key1.setAutoDefault(True)
        self.button5.setAutoDefault(True)
        self.button6.setAutoDefault(True)
        self.load_data()
        QApplication.instance().installEventFilter(self)
        self.pull_down_mode = False
        self.combo_box.setFocus()

    def show_start_window(self):
        self.main_window = StartWindow()
        self.main_window.show()
        self.close()

    def inform_action(self):
        info_text = ("Ctrl+Q - выход из Pull-Down меню\n"
                     "Ctrl+T - навигация по таблице\n"
                     "Ctrl+↑ или Ctrl+↓ - навигация по виджетам ")
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Горячие клавиши")
        msg_box.setText(info_text)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowIcon(QIcon("54320.png"))
        msg_box.exec_()

    def checkbox_changed(self, state):
        if state == 2:  # Checked
            self.good_delete = 1
        else:  # Unchecked
            self.good_delete = 0
        print(self.good_delete)

    def update_database_insert(self, column_names, new_data, selected_table):
        try:
            # Устанавливаем соединение с базой данных
            connection = psycopg2.connect(
                dbname="bank",
                user="postgres",
                password="1234",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()

            # Формируем SQL-запрос с помощью конкатенации
            sql_query = "INSERT INTO public." + selected_table + " ("
            sql_query += ", ".join(column_names) + ") VALUES ("

            # Конкатенируем значения для SQL-запроса
            values = []
            for value in new_data.values():
                # Приводим значение к строке и экранируем одинарные кавычки
                values.append("'" + str(value).replace("'", "''") + "'")

            sql_query += ", ".join(values) + ");"
            print(sql_query)
            # Выполняем запрос без параметров
            cursor.execute(sql_query)

            # Сохраняем изменения и закрываем соединение
            connection.commit()
            connection.close()
            return "OK"
        except Exception as e:
            print(f"Ошибка 404: {e}")
            return "ERROR"

    def delete(self):
        try:
            selected_row = self.table_widget.currentRow()  # Получаем индекс выбранной строки
            if selected_row >= 0:  # Проверяем, что строка выбрана
                old_data = []
                for column in range(self.table_widget.columnCount()):
                    item = self.table_widget.item(selected_row, column)
                    if item is not None:
                        old_data.append(item.text())  # Добавляем текст элемента в список

                column_names = []
                for column in range(self.table_widget.columnCount()):
                    header_item = self.table_widget.horizontalHeaderItem(column)
                    if header_item is not None:
                        column_names.append(header_item.text())

                selected_table = self.combo_box.currentText()

                result = self.update_database_delete(column_names, old_data, selected_table)
                if result == "OK":
                    self.table = self.combo_box.currentText()
                    self.columns = column_names
                    self.row = self.table_widget.currentRow()
                    self.old_data = old_data
                    self.last_operation = "DELETE"
                    self.table_widget.removeRow(selected_row)
            else:
                return None  # Если строка не выбрана, возвращаем None
        except Exception as e:
            print(f"Ошибка 303: {e}")

    def update_database_delete(self, column_names, old_data, selected_table):
        try:
            # Устанавливаем соединение с базой данных
            connection = psycopg2.connect(
                dbname="bank",
                user="postgres",
                password="1234",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()

            # Создаем условие для поиска записи
            sql_query = f"""
                SELECT *
                FROM public.{selected_table}
                WHERE
            """
            for index, (column, old) in enumerate(zip(column_names, old_data)):
                sql_query += f"public.{selected_table}.{column} = '{old}'"
                if index < len(column_names) - 1:
                    sql_query += " AND "
            sql_query += ";"

            # Выполняем запрос для получения записи
            cursor.execute(sql_query)
            record = cursor.fetchone()

            if record is None:
                print("Запись не найдена.")
                return "ERROR"

            # Запрос для получения первичного ключа
            primary_key_query = f"""
                SELECT kcu.column_name
                FROM information_schema.table_constraints AS tc
                JOIN information_schema.key_column_usage AS kcu ON tc.constraint_name = kcu.constraint_name
                WHERE tc.constraint_type = 'PRIMARY KEY' AND tc.table_name = '{selected_table}' AND tc.table_schema = 'public';
            """

            cursor.execute(primary_key_query)
            primary_key_column = cursor.fetchone()

            if primary_key_column is None:
                print("Первичный ключ не найден.")
                return "ERROR"

            primary_key_column_name = primary_key_column[0]

            # Запрос для получения внешних ключей, связанных с таблицей
            foreign_keys_query = f"""
                SELECT kcu.table_name AS child_table, kcu.column_name AS child_column
                FROM information_schema.table_constraints AS tc
                JOIN information_schema.key_column_usage AS kcu ON tc.constraint_name = kcu.constraint_name
                JOIN information_schema.constraint_column_usage AS ccu ON ccu.constraint_name = tc.constraint_name
                WHERE tc.constraint_type = 'FOREIGN KEY' AND ccu.table_name = '{selected_table}';
            """

            cursor.execute(foreign_keys_query)
            foreign_keys = cursor.fetchall()

            has_relationships = False

            # Проверяем наличие связанных записей для каждого внешнего ключа
            for child_table, child_column in foreign_keys:
                check_relationships_query = f"""
                    SELECT COUNT(*) > 0
                    FROM public.{child_table}
                    WHERE {child_column} IN (
                        SELECT {primary_key_column_name} FROM public.{selected_table} WHERE
                """
                for index, (column, old) in enumerate(zip(column_names, old_data)):
                    check_relationships_query += f"{column} = '{old}'"
                    if index < len(column_names) - 1:
                        check_relationships_query += " AND "
                check_relationships_query += ");"

                cursor.execute(check_relationships_query)
                if cursor.fetchone()[0]:
                    has_relationships = True
                    break

            if self.good_delete == 1:
                conditions = []
                for col, value in zip(column_names, old_data):
                    # Приводим значение к строке и экранируем одинарные кавычки
                    escaped_value = "'" + str(value).replace("'", "''") + "'"
                    conditions.append(f"{col} = {escaped_value}")

                conditions_str = " AND ".join(conditions)
                sql_query = "DELETE FROM public." + selected_table + " WHERE " + conditions_str + ";"
                print(sql_query)
                # Выполняем запрос без параметров
                cursor.execute(sql_query)

                # Сохраняем изменения и закрываем соединение
                connection.commit()
                connection.close()
                return "OK"
            elif has_relationships:
                print("Запись не может быть удалена, так как существуют связанные записи.")
                return "ERROR"
            else:
                conditions = []
                for col, value in zip(column_names, old_data):
                    # Приводим значение к строке и экранируем одинарные кавычки
                    escaped_value = "'" + str(value).replace("'", "''") + "'"
                    conditions.append(f"{col} = {escaped_value}")

                conditions_str = " AND ".join(conditions)
                sql_query = "DELETE FROM public." + selected_table + " WHERE " + conditions_str + ";"
                print(sql_query)
                # Выполняем запрос без параметров
                cursor.execute(sql_query)

                # Сохраняем изменения и закрываем соединение
                connection.commit()
                connection.close()
                return "OK"

        except Exception as e:
            print(f"Ошибка 404: {e}")
            return "ERROR"

    def cancel(self):
        try:
            need_update_table = None

            if self.table == self.combo_box.currentText():
                need_update_table = 1

            if self.last_operation == "DELETE":
                data_dict = {self.columns[i]: self.old_data[i] for i in range(len(self.old_data))}
                result = self.update_database_insert(self.columns, data_dict, self.table)  # Исправлено на delete
                if need_update_table == 1:
                    self.table_widget.insertRow(self.row)  # Вставляем новую строку
                    for column_index, value in enumerate(self.old_data):  # Исправлено на old_data
                        self.table_widget.setItem(self.row, column_index,
                                                  QTableWidgetItem(value))  # Используем column_index

            self.table = None
            self.row = None
            self.columns = None
            self.old_data = None
            self.new_data = None
            self.last_operation = None
        except Exception as e:
            print(f"Ошибка 303: {e}")

    def insert(self):
        try:
            column_names = []
            for column in range(self.table_widget.columnCount()):
                header_item = self.table_widget.horizontalHeaderItem(column)
                if header_item is not None:
                    column_names.append(header_item.text())

            dialog = InsertDialog(column_names, self)
            if dialog.exec_() == QDialog.Accepted:
                new_data = dialog.get_values()  # Получаем новые данные

                selected_table = self.combo_box.currentText()
                result = self.update_database_insert(column_names, new_data, selected_table)
                if result == "OK":
                    self.table = self.combo_box.currentText()
                    self.columns = column_names
                    self.new_data = new_data
                    self.last_operation = "INSERT"
                    row_position = self.table_widget.rowCount()
                    self.table_widget.insertRow(row_position)
                    self.row = row_position
                    for column, value in enumerate(new_data.values()):
                        self.table_widget.setItem(row_position, column, QTableWidgetItem(value))

        except Exception as e:
            print(f"Ошибка 303: {e}")

    def highlight_matches(self):
        try:
            search_text = self.input_field.text().lower()  # Получаем текст из поля ввода
            for row in range(self.table_widget.rowCount()):
                for column in range(self.table_widget.columnCount()):
                    item = self.table_widget.item(row, column)
                    if item is not None:
                        # Сбрасываем цвет фона для всех ячеек
                        item.setBackground(QColor("white"))

                        # Проверяем на совпадение, если текст для поиска не пустой
                        if search_text and search_text in item.text().lower():
                            item.setBackground(QColor("yellow"))  # Подсвечиваем совпадения
        except Exception as e:
            print(f"Ошибка 707: {e}")

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Down:
                if self.pull_down_mode:
                    self.focusNextChild()
                    return True

            elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Up:
                if self.pull_down_mode:
                    self.focusPreviousChild()
                    return True

            elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_T:
                if not self.table_widget.hasFocus():
                    self.table_widget.setFocus()

                current_row = self.table_widget.currentRow()
                total_rows = self.table_widget.rowCount()

                if obj == self.table_widget and event.key() in (Qt.Key_Up, Qt.Key_Down):
                    if total_rows > 0:
                        if event.key() == Qt.Key_Down:
                            next_row = (current_row + 1) % total_rows
                        elif event.key() == Qt.Key_Up:
                            next_row = (current_row - 1) % total_rows

                        self.table_widget.setCurrentCell(next_row, 0)
                        return True

            elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Q:
                self.pull_down_mode = not self.pull_down_mode
                if not self.pull_down_mode:
                    self.combo_box.setFocus()
                else:
                    self.setFocus()
                return True
            elif event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
                focused_widget = QApplication.focusWidget()
                if focused_widget == self.checkbox:  # Проверяем, является ли фокусированный виджет кнопкой "Удаление"
                    self.checkbox.setChecked(not self.checkbox.isChecked())
        return super().eventFilter(obj, event)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            print(3)
            focused_widget = QApplication.focusWidget()
            if isinstance(focused_widget, QPushButton):
                focused_widget.click()
            elif self.pull_down_mode and not isinstance(focused_widget, QMessageBox) and not isinstance(focused_widget,
                                                                                                        QDialogButtonBox):
                self.pull_down_mode = False
                self.combo_box.setFocus()
            event.accept()
        else:
            super().keyPressEvent(event)

    def add_pull_down(self):
        try:
            connection = psycopg2.connect(
                dbname="bank",
                user="postgres",
                password="1234",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()
            # Запрос для получения всех таблиц в схеме 'public'
            query = """
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public';
            """

            cursor.execute(query)
            tables = cursor.fetchall()

            valid_tables = []

            for table in tables:
                table_name = table[0]

                # Запрос для проверки, есть ли столбцы, отличные от внешних ключей
                column_query = f"""
                    SELECT COUNT(*) 
                    FROM information_schema.columns
                    WHERE table_name = %s
                    AND column_name NOT IN (
                        SELECT kcu.column_name
                        FROM information_schema.table_constraints tc
                        JOIN information_schema.key_column_usage kcu
                        ON tc.constraint_name = kcu.constraint_name
                        AND tc.table_name = kcu.table_name
                        WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name = %s
                    );
                """
                cursor.execute(column_query, (table_name, table_name))
                column_count = cursor.fetchone()[0]

                # Если есть хотя бы один столбец, отличный от FK, добавляем таблицу в результат
                if column_count > 0:
                    valid_tables.append(table_name)

            self.combo_box.addItems(valid_tables)
            return valid_tables
        except Exception as e:
            print(f"Ошибка подключения к базе данных: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def load_data(self):
        try:
            connection = psycopg2.connect(
                dbname="bank",
                user="postgres",
                password="1234",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()

            selected_table = self.combo_box.currentText()
            # Запрос для получения названий столбцов таблицы
            query1 = f"""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = %s
            AND column_name NOT IN (
                -- Имена столбцов, которые являются частью первичного ключа
                SELECT kcu.column_name
                FROM information_schema.table_constraints tc
                JOIN information_schema.key_column_usage kcu
                ON tc.constraint_name = kcu.constraint_name
                AND tc.table_name = kcu.table_name
                WHERE tc.constraint_type = 'PRIMARY KEY' AND tc.table_name = %s
            )
            AND column_name NOT IN (
                -- Имена столбцов, которые являются частью внешнего ключа
                SELECT kcu.column_name
                FROM information_schema.table_constraints tc
                JOIN information_schema.key_column_usage kcu
                ON tc.constraint_name = kcu.constraint_name
                AND tc.table_name = kcu.table_name
                WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name = %s
            );
            """
            cursor.execute(query1, (selected_table, selected_table, selected_table))
            columns = cursor.fetchall()
            column_names = [column[0] for column in columns]
            self.table_widget.setColumnCount(len(column_names))
            self.table_widget.setHorizontalHeaderLabels(column_names)
            self.table_widget.setRowCount(0)

            columns_string = ", ".join(column_names)
            query2 = f"SELECT {columns_string} FROM public.{selected_table};"
            cursor.execute(query2)
            rows = cursor.fetchall()

            for row in rows:
                row_position = self.table_widget.rowCount()
                self.table_widget.insertRow(row_position)
                for column in range(len(row)):
                    self.table_widget.setItem(row_position, column, QTableWidgetItem(str(row[column])))

        except Exception as e:
            print(f"Ошибка подключения к базе данных: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def sort_table_by_column(self, logical_index):
        self.table_widget.sortItems(logical_index)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            reply = QMessageBox.warning(self, 'Вы точно хотите выйти?', 'Вы уверены, что хотите закрыть программу?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
                self.close()
            else:
                event.ignore()


class MainWindow4(QMainWindow):
    def __init__(self):
        try:
            super().__init__()
            self.setWindowTitle("Выбор записи")
            self.setWindowIcon(QIcon("54320.png"))
            self.setFixedSize(800, 800)

            # Create a QSplitter to divide the window into two parts
            self.splitter = QSplitter(Qt.Vertical)
            self.setCentralWidget(self.splitter)

            # Top part of the splitter - Table view
            top_widget = QWidget()
            top_layout = QVBoxLayout()
            self.combo_box = QComboBox()
            top_layout.addWidget(self.combo_box)
            self.combo_box.currentIndexChanged.connect(self.load_data)
            top_widget.setLayout(top_layout)
            self.splitter.addWidget(top_widget)

            # Populate the top part with the table
            self.table_widget = QTableWidget()
            columns = self.add_pull_down()
            self.table_widget.setRowCount(0)
            top_layout.addWidget(self.table_widget)
            self.table_widget.setMinimumHeight(400)
            self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.table_widget.horizontalHeader().sectionClicked.connect(self.sort_table_by_column)

            # Bottom part of the splitter
            bottom_widget = QWidget()
            bottom_layout = QVBoxLayout()
            bottom_widget.setLayout(bottom_layout)
            self.splitter.addWidget(bottom_widget)

            # Create a QHBoxLayout for input field, Button 2, and a search button
            hbox1 = QHBoxLayout()
            self.input_field = QLineEdit()
            self.input_field.setFixedWidth(385)  # Set fixed width for input field
            self.button2 = QPushButton("Выход из режима")
            self.button2.clicked.connect(self.show_start_window)
            self.hot_key = QPushButton("Горячие клавиши")
            self.input_field.textChanged.connect(self.highlight_matches)
            hbox1.addWidget(self.input_field)
            hbox1.addWidget(self.hot_key)
            hbox1.addWidget(self.button2)
            bottom_layout.addLayout(hbox1)

            # Add spacing between the two rows
            bottom_layout.addSpacing(10)

            # Create QHBoxLayout for buttons 3, 4, and 5
            hbox2 = QHBoxLayout()
            self.button3 = QPushButton(f"Выбор строки")
            hbox2.addWidget(self.button3)
            bottom_layout.addLayout(hbox2)

            self.splitter.setStretchFactor(0, 2)
            self.splitter.setStretchFactor(1, 1)

            self.button2.setAutoDefault(True)
            self.hot_key.setAutoDefault(True)
            self.button3.setAutoDefault(True)
            self.load_data()

            # Connect event filter for handling key events
            QApplication.instance().installEventFilter(self)

            # Connect button click events

            self.button3.clicked.connect(self.edit_action)
            self.hot_key.clicked.connect(self.inform_action)
            self.pull_down_mode = False

            self.combo_box.setFocus()
        except Exception as e:
            print(f"Ошибка 909: {e}")

    def show_start_window(self):
        self.main_window = StartWindow()
        self.main_window.show()
        self.close()

    def highlight_matches(self):
        try:
            search_text = self.input_field.text().lower()  # Получаем текст из поля ввода
            for row in range(self.table_widget.rowCount()):
                for column in range(self.table_widget.columnCount()):
                    item = self.table_widget.item(row, column)
                    if item is not None:
                        # Сбрасываем цвет фона для всех ячеек
                        item.setBackground(QColor("white"))

                        # Проверяем на совпадение, если текст для поиска не пустой
                        if search_text and search_text in item.text().lower():
                            item.setBackground(QColor("yellow"))  # Подсвечиваем совпадения
        except Exception as e:
            print(f"Ошибка 707: {e}")

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Down:
                if self.pull_down_mode:
                    self.focusNextChild()
                    return True

            elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Up:
                if self.pull_down_mode:
                    self.focusPreviousChild()
                    return True

            elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_V:
                self.edit_action()
                return True

            elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_T:
                if not self.table_widget.hasFocus():
                    self.table_widget.setFocus()

                current_row = self.table_widget.currentRow()
                total_rows = self.table_widget.rowCount()

                if obj == self.table_widget and event.key() in (Qt.Key_Up, Qt.Key_Down):
                    if total_rows > 0:
                        if event.key() == Qt.Key_Down:
                            next_row = (current_row + 1) % total_rows
                        elif event.key() == Qt.Key_Up:
                            next_row = (current_row - 1) % total_rows

                        self.table_widget.setCurrentCell(next_row, 0)
                        return True

            elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Q:
                self.pull_down_mode = not self.pull_down_mode
                if not self.pull_down_mode:
                    self.combo_box.setFocus()
                else:
                    self.setFocus()
                return True

            elif event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
                focused_widget = QApplication.focusWidget()
                if isinstance(focused_widget, QPushButton):
                    focused_widget.click()
                elif self.pull_down_mode:
                    self.pull_down_mode = False
                    self.combo_box.setFocus()
                return True

        return super().eventFilter(obj, event)

    def edit_action(self):
        if self.table_widget.currentItem() is not None:
            current_row = self.table_widget.currentItem().row()
            self.table_widget.selectRow(current_row)

    def inform_action(self):
        info_text = ("Ctrl+Q - выход из Pull-Down меню\n"
                     "Ctrl+T - навигация по таблице\n"
                     "Ctrl+V - выбор целой строки\n"
                     "Ctrl+↑ или Ctrl+↓ - навигация по виджетам ")
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Горячие клавиши")
        msg_box.setText(info_text)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec_()

    def add_pull_down(self):
        try:
            connection = psycopg2.connect(
                dbname="bank",
                user="postgres",
                password="1234",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()
            # Запрос для получения всех таблиц в схеме 'public'
            query = """
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public';
            """

            cursor.execute(query)
            tables = cursor.fetchall()

            valid_tables = []

            for table in tables:
                table_name = table[0]

                # Запрос для проверки, есть ли столбцы, отличные от внешних ключей
                column_query = f"""
                    SELECT COUNT(*) 
                    FROM information_schema.columns
                    WHERE table_name = %s
                    AND column_name NOT IN (
                        SELECT kcu.column_name
                        FROM information_schema.table_constraints tc
                        JOIN information_schema.key_column_usage kcu
                        ON tc.constraint_name = kcu.constraint_name
                        AND tc.table_name = kcu.table_name
                        WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name = %s
                    );
                """
                cursor.execute(column_query, (table_name, table_name))
                column_count = cursor.fetchone()[0]

                # Если есть хотя бы один столбец, отличный от FK, добавляем таблицу в результат
                if column_count > 0:
                    valid_tables.append(table_name)

            self.combo_box.addItems(valid_tables)
            return valid_tables
        except Exception as e:
            print(f"Ошибка подключения к базе данных: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def load_data(self):
        try:
            connection = psycopg2.connect(
                dbname="bank",
                user="postgres",
                password="1234",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()

            selected_table = self.combo_box.currentText()
            # Запрос для получения названий столбцов таблицы
            query1 = f"""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = %s
            AND column_name NOT IN (
                -- Имена столбцов, которые являются частью первичного ключа
                SELECT kcu.column_name
                FROM information_schema.table_constraints tc
                JOIN information_schema.key_column_usage kcu
                ON tc.constraint_name = kcu.constraint_name
                AND tc.table_name = kcu.table_name
                WHERE tc.constraint_type = 'PRIMARY KEY' AND tc.table_name = %s
            )
            AND column_name NOT IN (
                -- Имена столбцов, которые являются частью внешнего ключа
                SELECT kcu.column_name
                FROM information_schema.table_constraints tc
                JOIN information_schema.key_column_usage kcu
                ON tc.constraint_name = kcu.constraint_name
                AND tc.table_name = kcu.table_name
                WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name = %s
            );
            """
            cursor.execute(query1, (selected_table, selected_table, selected_table))
            columns = cursor.fetchall()
            column_names = [column[0] for column in columns]
            self.table_widget.setColumnCount(len(column_names))
            self.table_widget.setHorizontalHeaderLabels(column_names)
            self.table_widget.setRowCount(0)
            columns_string = ", ".join(column_names)
            query2 = f"SELECT {columns_string} FROM public.{selected_table};"
            cursor.execute(query2)
            rows = cursor.fetchall()

            for row in rows:
                row_position = self.table_widget.rowCount()
                self.table_widget.insertRow(row_position)
                for column in range(len(row)):
                    self.table_widget.setItem(row_position, column, QTableWidgetItem(str(row[column])))

        except Exception as e:
            print(f"Ошибка подключения к базе данных: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def sort_table_by_column(self, logical_index):
        self.table_widget.sortItems(logical_index)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            reply = QMessageBox.warning(self, 'Вы точно хотите выйти?', 'Вы уверены, что хотите закрыть программу?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
                self.close()
            else:
                event.ignore()


class MainWindow5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пакетный режим")
        self.setWindowIcon(QIcon("54320.png"))
        self.setFixedSize(500, 300)
        self.splitter = QSplitter(Qt.Vertical)
        self.setCentralWidget(self.splitter)
        # Create a QVBoxLayout for the main layout
        main_layout = QVBoxLayout()
        self.setStyleSheet("background-color: #ff5733;")
        # Add a button to select multiple files or items
        select_button = QPushButton("Выбрать файл")
        select_button.setStyleSheet(
            """
            font-size: 11pt;                /* Размер шрифта */
            border-radius: 10px;            /* Закругление краев */
            background-color: #5cb85c;      /* Цвет фона кнопки */
            padding: 10;
            color: white;                   /* Цвет текста */
            border: none;                   /* Убираем границу кнопки */
            """
        )
        select_button.setMaximumWidth(250)
        main_layout.addWidget(select_button)

        # Add a list or table to display selected files or items
        self.selected_items_table = QTableWidget()
        self.selected_items_table.setColumnCount(1)
        header = self.selected_items_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        self.selected_items_table.setHorizontalHeaderLabels(["Выбранные элементы"])
        main_layout.addWidget(self.selected_items_table)

        # Add a button for batch processing
        process_button = QPushButton("Импортировать данные")
        process_button.setStyleSheet(
            """
            font-size: 11pt;                /* Размер шрифта */
            border-radius: 10px;            /* Закругление краев */
            background-color: #5cb85c;      /* Цвет фона кнопки */
            padding: 10;
            color: white;                   /* Цвет текста */
            border: none;                   /* Убираем границу кнопки */
            """
        )
        process_button.setMaximumWidth(250)
        main_layout.addWidget(process_button)
        process2_button = QPushButton("Экспортировать данные")
        process2_button.setStyleSheet(
            """
            font-size: 11pt;                /* Размер шрифта */
            border-radius: 10px;            /* Закругление краев */
            background-color: #5cb85c;      /* Цвет фона кнопки */
            padding: 10;
            color: white;                   /* Цвет текста */
            border: none;                   /* Убираем границу кнопки */
            """
        )
        process2_button.setMaximumWidth(250)
        main_layout.addWidget(process2_button)
        button3 = QPushButton("Выход из режима")
        button3.setStyleSheet(
            """
            font-size: 11pt;                /* Размер шрифта */
            border-radius: 10px;            /* Закругление краев */
            background-color: #ff2000;      /* Цвет фона кнопки */
            padding: 10px;                  /* Внутренний отступ */
            color: white;                   /* Цвет текста */
            border: none;                   /* Убираем границу кнопки */
            """
        )
        button3.clicked.connect(self.show_start_window)
        main_layout.addWidget(button3)

        select_button.setFocus()
        select_button.setDefault(True)
        select_button.setAutoDefault(True)
        process_button.setAutoDefault(True)
        process2_button.setAutoDefault(True)
        button3.setAutoDefault(True)
        # Set up the central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Connect button signals to appropriate slots
        select_button.clicked.connect(self.select_files)
        process_button.clicked.connect(self.import_data)
        process2_button.clicked.connect(self.export_data)

    def show_start_window(self):
        self.main_window = StartWindow()
        self.main_window.show()
        self.close()

    def select_files(self):
        try:
            # Open a file dialog to select multiple files
            options = QFileDialog.Options()
            self.files, _ = QFileDialog.getOpenFileNames(self, "Выбрать файлы", "",
                                                         "Все файлы (*);;Текстовые файлы (*.txt);;CSV файлы (*.csv)",
                                                         options=options)

            # Clear the table before adding new items
            self.selected_items_table.setRowCount(0)

            for file in self.files:
                # Add each selected file to the table
                row_position = self.selected_items_table.rowCount()
                self.selected_items_table.insertRow(row_position)
                self.selected_items_table.setItem(row_position, 0, QTableWidgetItem(file))
        except Exception as e:
            print(f"Ошибка в выборе файла: {e}")

    def import_data(self):
        """Импорт данных из Excel в базу данных PostgreSQL"""

        try:
            for file in self.files:
                # Чтение данных из Excel
                excel_data = pd.read_excel(file)
                print("Данные из Excel успешно прочитаны.")

                selected_table = None
                # Запрос имени таблицы у пользователя
                selected_table, ok = QInputDialog.getText(self, "Имя таблицы",
                                                          f"Введите имя таблицы для импорта данных из {file}:")
                if not ok or not selected_table:
                    print("Имя таблицы не введено или отменено.")
                    return

                connection = psycopg2.connect(
                    dbname="bank",
                    user="postgres",
                    password="1234",
                    host="localhost",
                    port="5432"
                )
                cursor = connection.cursor()

                print(f"Вы выбрали таблицу: {selected_table}")
                # Запрос для получения названий столбцов таблицы
                query1 = f"""
                SELECT column_name
                FROM information_schema.columns
                WHERE table_name = %s
                AND column_name NOT IN (
                    -- Имена столбцов, которые являются частью первичного ключа
                    SELECT kcu.column_name
                    FROM information_schema.table_constraints tc
                    JOIN information_schema.key_column_usage kcu
                    ON tc.constraint_name = kcu.constraint_name
                    AND tc.table_name = kcu.table_name
                    WHERE tc.constraint_type = 'PRIMARY KEY' AND tc.table_name = %s
                )
                AND column_name NOT IN (
                    -- Имена столбцов, которые являются частью внешнего ключа
                    SELECT kcu.column_name
                    FROM information_schema.table_constraints tc
                    JOIN information_schema.key_column_usage kcu
                    ON tc.constraint_name = kcu.constraint_name
                    AND tc.table_name = kcu.table_name
                    WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name = %s
                );
                """
                cursor.execute(query1, (selected_table, selected_table, selected_table))
                columns = cursor.fetchall()
                column_names = [column[0] for column in columns]  # Получаем имена столбцов в виде строк

                # Перебор строк и вставка данных в базу данных
                for index, row in excel_data.iterrows():
                    # Проверяем соответствие между row и column_names
                    values_to_insert = [row[column] for column in column_names if column in row]

                    if len(values_to_insert) != len(column_names):
                        print(
                            f"Количество значений ({len(values_to_insert)}) не совпадает с количеством столбцов ({len(column_names)}) для строки {index}. Пропускаем строку.")
                        continue

                    sql_query = f"INSERT INTO public.{selected_table} ("
                    sql_query += ", ".join(column_names) + ") VALUES ("
                    sql_query += ", ".join("%s" for _ in column_names) + ");"

                    # Выполняем вставку с параметрами
                    cursor.execute(sql_query, tuple(values_to_insert))  # Передаем значения как кортеж

                # Подтверждение изменений
                connection.commit()
                cursor.close()
                connection.close()
                print("Данные успешно импортированы в базу данных.")

            QMessageBox.information(self, "Импорт", f"Данные успешно импортированы.")
        except Exception as e:
            print(f"Ошибка при импорте данных: {e}")

    def export_data(self):
        # Connect to the PostgreSQL database
        try:
            connection = psycopg2.connect(
                dbname="bank",
                user="postgres",
                password="1234",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()
            # Запрос для получения всех таблиц в схеме 'public'
            query = """
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public';
            """

            cursor.execute(query)
            tables = cursor.fetchall()

            valid_tables = []

            for table in tables:
                table_name = table[0]

                # Запрос для проверки, есть ли столбцы, отличные от внешних ключей
                column_query = f"""
                    SELECT COUNT(*) 
                    FROM information_schema.columns
                    WHERE table_name = %s
                    AND column_name NOT IN (
                        SELECT kcu.column_name
                        FROM information_schema.table_constraints tc
                        JOIN information_schema.key_column_usage kcu
                        ON tc.constraint_name = kcu.constraint_name
                        AND tc.table_name = kcu.table_name
                        WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name = %s
                    );
                """
                cursor.execute(column_query, (table_name, table_name))
                column_count = cursor.fetchone()[0]

                # Если есть хотя бы один столбец, отличный от FK, добавляем таблицу в результат
                if column_count > 0:
                    valid_tables.append(table_name)
            for table in valid_tables:
                query = "SELECT * FROM public." + table  # Замените на ваш запрос
                df = pd.read_sql_query(query, connection)

                # Получение пути к директории, в которой находится скрипт
                current_directory = os.path.dirname(os.path.abspath(__file__))
                # Формирование пути к файлу
                default_file_name = table + ".xlsx"
                file_path = os.path.join(current_directory, default_file_name)

                if file_path:
                    # Save the DataFrame to an Excel file
                    df.to_excel(file_path, index=False)

            QMessageBox.information(self, "Экспорт", f"Данные успешно экспортированы.")
            connection.close()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при экспорте данных:\n{str(e)}")

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Down:
            self.focusNextChild()
        elif key == Qt.Key_Up:
            self.focusPreviousChild()


class EditDialog(QDialog):
    def __init__(self, row_data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Редактирование")
        self.layout = QVBoxLayout(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        # Создаем поля для ввода
        self.inputs = []
        for data in row_data:
            input_field = QLineEdit(data)
            self.layout.addWidget(input_field)
            self.inputs.append(input_field)

        # Кнопка для подтверждения изменений
        self.save_button = QPushButton("Сохранить изменения")
        self.save_button.clicked.connect(self.save_data)
        self.save_button.setDefault(True)
        self.layout.addWidget(self.save_button)

        enter_shortcut = QShortcut(QKeySequence(Qt.Key_Return), self.save_button)
        enter_shortcut.activated.connect(self.save_data)

        if self.inputs:
            self.inputs[0].setFocus()

        for idx, input_field in enumerate(self.inputs):
            input_field.installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == Qt.Key_Up:
            idx = self.inputs.index(source)
            if idx > 0:
                self.inputs[idx - 1].setFocus()
            return True
        elif event.type() == Qt.Key_Down:
            idx = self.inputs.index(source)
            if idx < len(self.inputs) - 1:
                self.inputs[idx + 1].setFocus()
            return True
        return super().eventFilter(source, event)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Up:
            current_index = self.inputs.index(self.focusWidget())
            if current_index > 0:
                self.inputs[current_index - 1].setFocus()
        elif key == Qt.Key_Down:
            current_index = self.inputs.index(self.focusWidget())
            if current_index < len(self.inputs) - 1:
                self.inputs[current_index + 1].setFocus()
        else:
            super().keyPressEvent(event)

    def save_data(self):
        self.accept()  # Закрываем диалог и возвращаем данные

    def get_new_data(self):
        return [input_field.text() for input_field in self.inputs]  # Возвращаем новые данные из полей ввода


from PyQt5.QtWidgets import QDialog, QFormLayout, QLabel, QLineEdit, QPushButton, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt, QEvent  # Добавляем QEvent в импорт


class InsertDialog(QDialog):
    def __init__(self, column_names, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Вставка")

        self.layout = QFormLayout(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        # Словарь для хранения введённых значений
        self.input_values = {}

        # Создание поля ввода для каждой колонки
        for column in column_names:
            label = QLabel(column)
            line_edit = QLineEdit()
            self.layout.addRow(label, line_edit)
            self.input_values[column] = line_edit

        # Кнопка для подтверждения ввода
        self.submit_button = QPushButton("Сохранить изменения")
        self.submit_button.clicked.connect(self.accept)
        self.submit_button.setDefault(True)
        self.layout.addWidget(self.submit_button)

        enter_shortcut = QShortcut(QKeySequence(Qt.Key_Return), self.submit_button)
        enter_shortcut.activated.connect(self.accept)

        for index, line_edit in enumerate(self.input_values.values()):
            line_edit.installEventFilter(self)
            line_edit.setFocusPolicy(Qt.StrongFocus)
            line_edit.next_in_tab = list(self.input_values.values())[(index + 1) % len(self.input_values)]
            line_edit.prev_in_tab = list(self.input_values.values())[index - 1]

    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress:  # Исправляем здесь
            key = event.key()
            if key == Qt.Key_Up:
                source.prev_in_tab.setFocus()
                return True
            elif key == Qt.Key_Down:
                source.next_in_tab.setFocus()
                return True
        return super().eventFilter(source, event)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Up:
            current_index = list(self.input_values.values()).index(self.focusWidget())
            if current_index > 0:
                list(self.input_values.values())[current_index - 1].setFocus()
        elif key == Qt.Key_Down:
            current_index = list(self.input_values.values()).index(self.focusWidget())
            if current_index < len(self.input_values) - 1:
                list(self.input_values.values())[current_index + 1].setFocus()
        else:
            super().keyPressEvent(event)

    def get_values(self):
        # Получение введённых значений
        return {column: line_edit.text() for column, line_edit in self.input_values.items()}


if __name__ == "__main__":
    app = QApplication(sys.argv)
    start_window = StartWindow()
    start_window.show()
    sys.exit(app.exec_())
