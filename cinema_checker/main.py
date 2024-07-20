import csv
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout, 
                             QVBoxLayout, QComboBox, QSpinBox, QListWidget, QStackedLayout)


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Cinema Checker")
        self.setGeometry(300, 300, 550, 500)

        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()
        self.h_box5 = QHBoxLayout()
        self.v_box = QVBoxLayout()


        # Box1
        self.label = QLabel("Film Nomi:", self)
        self.edit1 = QLineEdit(self)
        self.edit1.setPlaceholderText("Film nomini kiriting:")

        self.h_box1.addWidget(self.label)
        self.h_box1.addWidget(self.edit1)

        # Box2
        self.label2 = QLabel("Film Janri:", self)
        self.combo_janr = QComboBox()
        self.combo_janr.addItems(["Drama", "Horror", "Adventure", "Fantastic", "Romantic"])

        self.h_box2.addWidget(self.label2)
        self.h_box2.addWidget(self.combo_janr)

        # Box3
        self.label3 = QLabel("Ishlab chiqarilgan yili:", self)
        self.year = QSpinBox(self)
        self.year.setMinimum(1800)
        self.year.setMaximum(2024)

        self.h_box3.addWidget(self.label3)
        self.h_box3.addWidget(self.year)

        # Box4
        self.label4 = QLabel("Kino boshlanish vaqti:", self)
        self.edit2 = QLineEdit(self)
        self.PMorAM = QComboBox()
        self.PMorAM.addItems(["AM", "PM"])

        self.h_box4.addWidget(self.label4)
        self.h_box4.addWidget(self.edit2)
        self.h_box4.addWidget(self.PMorAM)

        # Edit3
        self.search_button = QPushButton("Qidiruv")
        self.search_button.clicked.connect(self.search_film)

        # Box5
        self.label5 = QLabel("Natijalar:", self)
        self.result_films = QListWidget(self)

        self.h_box5.addWidget(self.label5)
        self.h_box5.addWidget(self.result_films)

        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)
        self.v_box.addWidget(self.search_button)
        self.v_box.addLayout(self.h_box5)

        self.setLayout(self.v_box)

#Backgound Picture ham qo`ymoqchi edim lekin ishlataolmadim
        self.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #333;
            }
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 5px;
                background-color: #fff;
            }
            QComboBox {
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 5px;
                background-color: #fff;
            }
            QSpinBox {
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 5px;
                background-color: #fff;
            }
            QPushButton {
                border: 1px solid #007BFF;
                border-radius: 4px;
                padding: 5px;
                background-color: #007BFF;
                color: #fff;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QListWidget {
                border: 1px solid #ccc;
                border-radius: 4px;
                background-color: #fff;
            }
        """)

    def search_film(self):
        film_name = self.edit1.text()
        film_genres = self.combo_janr.currentText()
        year = self.year.value()
        time = self.edit2.text() + " " + self.PMorAM.currentText()

        movies = read_file()
        result = search_film(movies, film_name, film_genres, year, time)

        self.result_films.clear()
        if result:
            for movie in result:
                film = f"Title: {movie['title']} Genre: {movie['genres']} Year: {movie['year']} Time: {movie['time']}"
                self.result_films.addItem(film)
        else:
            self.result_films.addItem("No Valid Movies Found")


def read_file():
    movies = []
    with open("cinema.txt", 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            movie = {
                "title": line[0].strip('\'"'),
                "genres": line[1].strip(),
                "year": line[2].strip(),
                "time": line[3].strip()
            }
            movies.append(movie)
    return movies


def search_film(movies, title=None, genre=None, year=None, time=None):
    result = []
    for movie in movies:
        if title and title.lower() not in movie["title"].lower():
            continue
        if genre and genre.lower() != movie["genres"].lower():
            continue
        if year and str(year) != movie["year"]:
            continue
        if time and time != movie["time"]:
            continue
        result.append(movie)
    return result


cinema_app = QApplication([])
window = Window()
window.show()
cinema_app.exec_()

#Cases
# Wolfman,Horror,2001,3:53 AM
# Bat,Mystery,2002,9:35 AM