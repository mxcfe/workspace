import datetime
import json
import sqlite3
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QTableWidget, QWidget, \
    QFileDialog
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import Qt, QUrl, QFileInfo
from mainWindow import Ui_mainWindow

from paperDetailsWindow import Ui_paperDetailsWindow
from kgWindow import Ui_kgWindow

userinfo = []


def getInfo(title):
    global userinfo
    key = title
    conn = sqlite3.connect("static/data/kg.sqlite")
    if userinfo:
        create_time = str(datetime.datetime.today())[5:-7]

        conn.execute('''INSERT INTO history (userId ,context, type ,    time  ) VALUES( \'''' + str(
            userinfo[0]) + '''\',\'''' + str(title) + '''\','1',\'''' + create_time + '''\')''')
        conn.commit()

    cursor = conn.execute(f"select * from relation where s = '{key}' or t = '{key}' or r = '{key}'")
    values = cursor.fetchall()
    conn.close()

    links = []
    nodes = {}
    node = [(value[0], 'title') for value in values]
    for value in values:
        if '作' in value[1]:
            type = "author"
        elif '属于' in value[1]:
            type = "tab"
        elif '发表年份' in value[1]:
            type = "year"


        elif '类型' in value[1]:
            type = "type"

        elif '发布于' in value[1]:
            type = "publish_name"

        elif '特点' in value[1]:
            type = "keywords"
        node.append((value[2], type))
    node = list(set(node))
    for idx, n in enumerate(node):
        nodes[str(idx + 1)] = {"name": str(n[0]), "type": n[1]}
    for value in values:
        ids = [i[0] for i in node]

        links.append({"source": ids.index(value[0]) + 1, "target": ids.index(value[2]) + 1, "rela": value[1]})

    data = {'nodes': nodes, 'links': links}
    if links:
        with open('static/json/kg.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(data))
        return True
    return False


class KG(QWidget, Ui_kgWindow):
    def __init__(self):
        super(KG, self).__init__()
        self.setupUi(self)
        appIcon = QIcon("icon/logo.jpg")
        self.setWindowIcon(appIcon)
        self.widget.load(QUrl(QFileInfo("static/html/kg.html").absoluteFilePath()))

    def select(self):
        input_txt = self.lineEdit_2.text()
        if input_txt:
            if getInfo(input_txt):
                self.widget.load(QUrl(QFileInfo("static/html/kg.html").absoluteFilePath()))
            else:
                QMessageBox.warning(self, '提示', '未查询到内容！！！')
        else:
            QMessageBox.warning(self, '提示', '未输入内容！！！')


class paperDetails(QWidget, Ui_paperDetailsWindow):
    def __init__(self, values):
        super(paperDetails, self).__init__()
        appIcon = QIcon("icon/logo.jpg")
        self.setWindowIcon(appIcon)

        self.setupUi(self)

        getInfo(values[1])

        title = str(values[1])

        if eval(values[2]) != []:
            self.label_4.setText(eval(values[2])[0])
            if len(eval(values[2])) > 1:
                self.label_5.setText(eval(values[2])[1])

        self.label_3.setText(title)

        self.label_2.setText(f'<a href="{values[10]}">阅读原文</a>')
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.widget.load(QUrl(QFileInfo("static/html/kg.html").absoluteFilePath()))
        self.textBrowser.setText(values[8])

        self.new_window = None

    def output(self):
        if userinfo:
            reply = QMessageBox.question(self, '提示', '是否导出图谱图片？', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)

            if reply == QMessageBox.Yes:
                pixmap = QPixmap(2000, 2000)

                t = pixmap.grabWidget(self.widget)
                fileName2, ok2 = QFileDialog.getSaveFileName(self, "导出", f"./{self.label_3.text()}_节点图谱.png",
                                                             "Files (*.png)")
                t.save(fileName2)
        else:
            QMessageBox.warning(self, '提示', '未登录，请登录后使用！！！')

    def select(self):
        input_txt = self.lineEdit.text()
        if input_txt:
            if getInfo(input_txt):
                if self.new_window is not None:
                    self.new_window.close()

                self.new_window = KG()

                self.new_window.setWindowModality(Qt.ApplicationModal)
                self.new_window.show()
            else:
                QMessageBox.warning(self, '提示', '未查询到内容！！！')
        else:
            QMessageBox.warning(self, '提示', '未输入内容！！！')


def updateUser():
    global userinfo
    conn = sqlite3.connect("static/data/kg.sqlite")
    sql = f'UPDATE user SET  last_time = \"{userinfo[3]}\" WHERE id=\"{userinfo[0]}\";'

    conn.execute(sql)
    conn.commit()
    conn.close()


class MainProgram(QMainWindow):
    def __init__(self):
        super(MainProgram, self).__init__()
        self.ui = Ui_mainWindow()

        self.ui.setupUi(self)

        self.ui.tabWidget.setCurrentIndex(0)
        self.setWindowTitle("藏医药论文知识图谱 V1.0")

        appIcon = QIcon("icon/logo.jpg")
        self.setWindowIcon(appIcon)

        self.show()
        self.ui.userinfo.setVisible(False)

        self.ui.btn_kg_all.clicked.connect(self.go_to_kg_all)
        self.ui.btn_find_paper.clicked.connect(self.go_to_find_paper)
        self.ui.btn_find_node.clicked.connect(self.go_to_find_node)
        self.ui.btn_history.clicked.connect(self.go_history)

    def input(self):
        if userinfo:
            reply = QMessageBox.question(self, '提示', '是否导入数据？', QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                fileName1, filetype = QFileDialog.getOpenFileName(self,"选取文件", "./", "Text Files (*.csv)")
                print(fileName1)
                with open(fileName1, 'r', encoding='utf-8') as f:
                    x = f.readlines()

                for i in x[1:]:
                    data = i.split(',')
                    conn = sqlite3.connect("static/data/kg.sqlite")
                    sql = f"INSERT INTO history (userId,context ,time ,type) VALUES(\'{userinfo[0]}\',\'{data[1]}\',\'{data[2]}\',\'{0 if '论文' in data[3] else 1}\')"
                    conn.execute(sql)
                    conn.commit()
                    conn.close()
                QMessageBox.information(self, '提示', '导入成功')
        else:
            QMessageBox.warning(self, '提示', '未登录，请登录后使用！！！')

    def output(self):
        if userinfo:
            reply = QMessageBox.question(self, '提示', '是否导出全部检索数据？', QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)

            if reply == QMessageBox.Yes:
                create_time = str(datetime.datetime.today())[5:-7].replace(':', '').replace(' ', '').replace('-', '')

                fileName2, ok2 = QFileDialog.getSaveFileName(self, "导出", f"./{userinfo[1]}_{create_time}.csv","Files (*.csv)")

                conn = sqlite3.connect("static/data/kg.sqlite")
                sql = f"SELECT * FROM history where userId='{userinfo[0]}'"
                cursor = conn.execute(sql)
                values = cursor.fetchall()
                conn.close()

                with open(fileName2, 'a', encoding='utf-8') as f:
                    f.write(f'序号,检索内容,检索时间,类型\n')
                    for index, i in enumerate(values):
                        f.write(f'{index},{i[2]},{i[4]},{"论文检索" if i[3] == 0 else "节点检索"}\n')
                QMessageBox.information(self, '提示', '导出成功')
        else:
            QMessageBox.warning(self, '提示', '未登录，请登录后使用！！！')

    def saveImg(self):
        if self.ui.lineEdit_2.text():
            reply = QMessageBox.question(self, '提示', '是否导出图谱图片？', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

            if reply == QMessageBox.Yes:
                pixmap = QPixmap(2000, 2000)

                t = pixmap.grabWidget(self.ui.widget_2)
                fileName2, ok2 = QFileDialog.getSaveFileName(self, "导出", f"./{self.ui.lineEdit_2.text()}_节点图谱.png", "Files (*.png)")
                t.save(fileName2)
        else:
            QMessageBox.warning(self, '提示', '请搜索后使用！！！')

    def history(self):

        conn = sqlite3.connect("static/data/kg.sqlite")
        if userinfo:

            sql1 = f"SELECT * FROM history where userId='{userinfo[0]}' and type='0'"
            sql2 = f"SELECT * FROM history where userId='{userinfo[0]}' and type='1'"
            cursor1 = conn.execute(sql1)
            cursor2 = conn.execute(sql2)
            values1 = cursor1.fetchall()
            values2 = cursor2.fetchall()
            conn.close()

            rows1 = len(values1)
            rows2 = len(values2)

            self.ui.tableWidget1.setRowCount(rows1)
            self.ui.tableWidget2.setRowCount(rows2)
            for idx, value in enumerate(values1):
                text = str(value[2])
                item = QTableWidgetItem(text)
                self.ui.tableWidget1.setItem(idx, 0, item)
                text = str(value[4])
                item = QTableWidgetItem(text)
                self.ui.tableWidget1.setItem(idx, 1, item)
            self.values1 = values1
            self.ui.tableWidget1.cellClicked.connect(self.sendData1)
            self.ui.tableWidget1.setSelectionBehavior(QTableWidget.SelectRows)

            for idx, value in enumerate(values2):
                text = str(value[2])
                item = QTableWidgetItem(text)
                self.ui.tableWidget2.setItem(idx, 0, item)

                text = str(value[4])
                item = QTableWidgetItem(text)
                self.ui.tableWidget2.setItem(idx, 1, item)
            self.values2 = values2
            self.ui.tableWidget2.cellClicked.connect(self.sendData2)
            self.ui.tableWidget2.setSelectionBehavior(QTableWidget.SelectRows)

    def sendData1(self, row, column):

        self.ui.lineEdit.setText(str(self.values1[row][2]))
        self.ui.tabWidget.setCurrentIndex(2)
        self.find_paper()

    def sendData2(self, row, column):

        self.ui.lineEdit_2.setText(str(self.values2[row][2]))
        self.ui.tabWidget.setCurrentIndex(3)
        self.find_node()

    def login(self):
        global userinfo

        username = self.ui.lineEdit_3.text()
        password = self.ui.lineEdit_4.text()
        if username and password:
            conn = sqlite3.connect("static/data/kg.sqlite")
            sql = f'SELECT * FROM user where username= \"{username}\"'

            cursor = conn.execute(sql)
            values = cursor.fetchall()
            conn.close()
            rows = len(values)
            if rows == 0:

                reply = QMessageBox.question(self, '提示', '未查询到用户，是否注册？', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    create_time = str(datetime.datetime.today())[5:-7]
                    conn = sqlite3.connect("static/data/kg.sqlite")
                    conn.execute('''INSERT INTO user (username,password,last_time)VALUES( \'''' + str(
                        username) + '''\',\'''' + str(password) + '''\',\'''' + create_time + '''\')''')
                    conn.commit()
                    conn.close()
                    QMessageBox.information(self, '提示', '注册成功！！！')
            else:
                conn = sqlite3.connect("static/data/kg.sqlite")
                sql = f'SELECT * FROM user where username= \"{username}\" and password=\"{password}\"'

                cursor = conn.execute(sql)
                values = cursor.fetchall()
                conn.close()
                rows = len(values)

                if rows == 0:
                    QMessageBox.warning(self, '提示', '用户名或密码错误！！！')

                else:
                    QMessageBox.information(self, '提示', '登录成功！！！')
                    self.ui.userinfo.setVisible(True)
                    self.ui.userlogin.setVisible(False)
                    userinfo = list(values[0])

                    self.ui.label_4.setText('用户名：' + str(userinfo[1]))
                    self.ui.label_8.setText('上次登录时间：\n' + str(userinfo[3]))

                    userinfo[3] = str(datetime.datetime.today())[5:-7]

                    updateUser()
                    self.history()
        else:
            QMessageBox.information(self, '提示', '用户名或密码不能为空！！！')

    def find_node(self):

        input_txt = self.ui.lineEdit_2.text()
        if input_txt:
            if getInfo(input_txt):
                self.ui.widget_2.load(QUrl(QFileInfo("static/html/kg.html").absoluteFilePath()))

            else:
                QMessageBox.warning(self, '提示', '未查询到内容！！！')
        else:
            QMessageBox.warning(self, '提示', '未输入内容！！！')

    def find_paper(self):
        global userinfo

        input_txt = self.ui.lineEdit.text()

        if input_txt:
            conn = sqlite3.connect("static/data/kg.sqlite")
            if userinfo:
                create_time = str(datetime.datetime.today())[5:-7]
                conn.execute('''INSERT INTO history (userId,context,type,time)VALUES( \'''' + str(
                    userinfo[0]) + '''\',\'''' + str(input_txt) + '''\','0',\'''' + create_time + '''\')''')
                conn.commit()

            sql = f"SELECT * FROM paper where 标题 like '%{input_txt}%'"

            cursor = conn.execute(sql)
            values = cursor.fetchall()

            conn.close()

            rows = len(values)
            if rows == 0:
                QMessageBox.warning(self, '提示', '未查到内容！！！')

            else:
                self.ui.tableWidget.setVisible(True)
                self.ui.tableWidget.setRowCount(rows)
                for idx, value in enumerate(values):

                    text = value[1]
                    item = QTableWidgetItem(text)
                    self.ui.tableWidget.setItem(idx, 0, item)

                    text = ''

                    for i in eval(value[3]).keys():
                        text += i + ','
                    item = QTableWidgetItem(text[:-1])
                    self.ui.tableWidget.setItem(idx, 1, item)

                    text = value[4]
                    item = QTableWidgetItem(text)
                    self.ui.tableWidget.setItem(idx, 2, item)

                    text = value[5]
                    item = QTableWidgetItem(text)
                    self.ui.tableWidget.setItem(idx, 3, item)
                    text = value[6]
                    item = QTableWidgetItem(text)
                    self.ui.tableWidget.setItem(idx, 4, item)
                    text = value[7]
                    item = QTableWidgetItem(text)
                    self.ui.tableWidget.setItem(idx, 5, item)

                    text = ''

                    for i in value[9][2:-2].split('\', \''):
                        text += i + ','
                    item = QTableWidgetItem(text[:-1])
                    self.ui.tableWidget.setItem(idx, 6, item)
                self.values = values
                self.ui.tableWidget.cellClicked.connect(self.open_new_window)
                self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)

                self.new_window = None
        else:
            QMessageBox.warning(self, '提示', '未输入内容！！！')

    def open_new_window(self, row, column):
        if self.new_window is not None:
            self.new_window.close()

        self.new_window = paperDetails(self.values[row])
        self.id = row

        self.new_window.setWindowModality(Qt.ApplicationModal)
        self.new_window.show()

    def go_to_kg_all(self):
        self.ui.widget.load(QUrl(QFileInfo("static/html/index.html").absoluteFilePath()))

        self.ui.tabWidget.setCurrentIndex(1)

    def go_to_find_paper(self):
        self.ui.tabWidget.setCurrentIndex(2)

    def go_to_find_node(self):
        self.ui.tabWidget.setCurrentIndex(3)

    def go_history(self):
        if userinfo:
            self.history()
            self.ui.tabWidget.setCurrentIndex(4)
        else:
            QMessageBox.warning(self, '提示', '未登录，请登录后查看历史搜索')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainProgram()
    sys.exit(app.exec_())
