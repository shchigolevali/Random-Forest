import sys
from PyQt5 import QtWidgets, QtCore
from program1 import Ui_MainWindow


def jump(max_jump, n, summ=0, str_v=None):
    if str_v is None:
        str_v = []
    result = []
    for i in range(1, max_jump + 1):
        if summ + i == n:
            result.append(str_v + [i])
            break
        else:
            result.extend(jump(max_jump, n, summ + i, str_v + [i]))
    return result


class AppWindow(QtWidgets.QMainWindow):
    step: int
    speed: int
    routes: list
    current_route: int
    position: int

    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.hares = 1
        self.speed = 0
        self.step_num = [self.ui.step2, self.ui.step4, self.ui.step6]
        self.colors = [self.ui.white, self.ui.yellow, self.ui.red]
        self.set_handlers()
        self.ui.hare_progress.setEnabled(False)
        self.step = 4
        # self.remove_head = False
        self.change_step_num()

    def set_handlers(self):
        for x in self.step_num:
            x.changed.connect(self.change_step)
        for x in self.colors:
            x.changed.connect(self.change_color)
        self.ui.up.clicked.connect(self.up)
        self.ui.down.clicked.connect(self.down)
        self.ui.auto.clicked.connect(self.auto)
        self.ui.polzunok.valueChanged.connect(self.change_speed)
        self.ui.action_3.triggered.connect(self.dialog)
        self.ui.route_select.currentIndexChanged.connect(self.select_route)

        self.step_num[1].setChecked(True)
        self.colors[0].setChecked(True)

    def select_route(self):
        self.current_route = self.ui.route_select.currentIndex()

    def change_step_num(self):
        self.routes = jump(3, self.step)
        self.ui.route_select.clear()
        for r in self.routes:
            self.ui.route_select.addItem('+'.join(map(str, r)))
        self.current_route = 0
        self.position = 0
        if self.ui.painter.hare > self.step:
            self.ui.painter.hare = self.step
        self.ui.painter.step = self.step
        self.ui.painter.update()

    def dialog(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Количество ступенек', 'Введите количество')
        if ok:
            try:
                self.step = int(text)
            except ValueError:
                pass
            else:
                self.change_step_num()
                for x in self.step_num:
                    x.changed.disconnect()
                    x.setChecked(False)
                    x.changed.connect(self.change_step)

    def change_speed(self):
        self.speed = self.ui.polzunok.value()
        self.ui.label.setText(str(self.speed))

    def change_step(self):
        action = self.sender()
        for x in self.step_num:
            x.changed.disconnect()
        for i, x in enumerate(self.step_num, 1):
            if x == action:
                self.step = i * 2
                x.setChecked(True)
            else:
                x.setChecked(False)
        self.change_step_num()
        for x in self.step_num:
            x.changed.connect(self.change_step)

    def change_color(self):
        action = self.sender()
        for x in self.colors:
            x.changed.disconnect()
        for x in self.colors:
            if x == action:
                self.ui.painter.hare_color = action.hare_color
                x.setChecked(True)
            else:
                x.setChecked(False)
        self.ui.painter.update()
        for x in self.colors:
            x.changed.connect(self.change_color)

    def move_hare(self, step):
        if 0 <= self.ui.painter.hare + step <= self.ui.painter.step:
            self.ui.painter.hare += step
            self.ui.hare_progress.setValue(int(99 / self.ui.painter.step * self.ui.painter.hare))
            self.ui.painter.update()

    def up(self):
        self.move_hare(1)

    def down(self):
        self.move_hare(-1)

    def auto(self):
        self.ui.painter.hare = 0
        self.position = 0
        self.ui.hare_progress.setValue(0)
        self.ui.painter.update()
        QtCore.QTimer.singleShot(int(1000 / 1.04 ** self.speed), self.auto_up)

    def auto_up(self):
        self.move_hare(self.routes[self.current_route][self.position])
        self.position += 1
        if self.ui.painter.hare < self.ui.painter.step:
            QtCore.QTimer.singleShot(int(1000 / 1.04 ** self.speed), self.auto_up)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
