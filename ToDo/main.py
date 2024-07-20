
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QMessageBox, QCheckBox, QLabel, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt


class TodoApp(QWidget):
    def __init__(self):
        super().__init__()


        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('To-Do List Application')
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


        self.layout = QVBoxLayout()
        
        self.inputLayout = QHBoxLayout()
        self.taskInput = QLineEdit(self)
        self.taskInput.setPlaceholderText('Enter a new task')
        self.addButton = QPushButton('Add Task', self)
        self.addButton.clicked.connect(self.addTask)
        self.inputLayout.addWidget(self.taskInput)
        self.inputLayout.addWidget(self.addButton)
        
        self.filterLayout = QHBoxLayout()
        self.filterLabel = QLabel('Filter Tasks:', self)
        self.filterComboBox = QComboBox(self)
        self.filterComboBox.addItems(['All', 'Completed', 'Pending'])
        self.filterComboBox.currentIndexChanged.connect(self.FilterTasks)
        self.filterLayout.addWidget(self.filterLabel)
        self.filterLayout.addWidget(self.filterComboBox)
        
        self.taskList = QListWidget(self)
        
        self.infoButton = QPushButton('Show Info', self)
        self.infoButton.clicked.connect(self.showInfo)
        
        self.layout.addLayout(self.inputLayout)
        self.layout.addLayout(self.filterLayout)
        self.layout.addWidget(self.taskList)
        self.layout.addWidget(self.infoButton)
        
        self.setLayout(self.layout)


    def addTask(self):
        taskDescription = self.taskInput.text()
        if taskDescription:
            item = QListWidgetItem(taskDescription)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.taskList.addItem(item)
            self.taskInput.clear()
        else:
            QMessageBox.warning(self, 'Warning', 'Task description cannot be empty')
    

    def showInfo(self):
        QMessageBox.information(self, 'Info', 'This is a simple To-Do List application.')


    def FilterTasks(self):

        option = self.filterComboBox.currentText()
        for i in range(self.taskList.count()):
            task = self.taskList.item(i)
            if option == "Pending" and task.checkState() == Qt.Unchecked:
                task.setHidden(False)
            elif option == "Completed" and task.checkState() == Qt.Checked:
                task.setHidden(False)
            elif option == "All":
                task.setHidden(False)
            else:
                task.setHidden(True)
                

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TodoApp()
    ex.show()
    sys.exit(app.exec_())
