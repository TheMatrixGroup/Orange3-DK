from AnyQt.QtWidgets import QLabel
from Orange.widgets.widget import OWWidget
from Orange.data import Table
from orangewidget.widget import OWBaseWidget, Output, Input
from orangewidget.settings import Setting
from orangewidget import gui
from dynamikontrol import Module
import time


class Angle(OWWidget):
    name = 'Angle'
    icon = 'icons/angle.png'
    description = '''Control the motor by angle by degree. If the input is DataTable, use the value of first row and first column by control angle. 모터를 각도로 제어합니다 (단위: 도). 입력값이 데이터테이블이면 테이블의 1행 1열의 값을 각도로 사용합니다.'''
    want_main_area = False

    module = None
    angle = Setting(0)
    period = Setting(0)

    def __init__(self):
        super().__init__()

        self.optionsBox = gui.widgetBox(self.controlArea, 'Controller')
        gui.spin(self.optionsBox, self, 'angle',
            minv=-80, maxv=80, step=1, label='Angle (-80 ~ 80 degrees)',
            callback=self.commit)
        gui.doubleSpin(self.optionsBox, self, 'period',
            minv=0, maxv=5, step=0.1, label='Period (0.0 ~ 5.0 seconds)')

        self.Outputs.module.send(self.module)

    class Inputs:
        module = Input('Module', object, auto_summary=False)
        angle = Input('Angle', object, auto_summary=False)

    class Outputs:
        module = Output('Module', object, auto_summary=False)

    def commit(self):
        if self.module is None:
            return

        period = self.period
        if period < 0.1:
            period = None

        self.module.motor.angle(int(self.angle), period=period)
        if period is not None:
            time.sleep(period)

        self.Outputs.module.send(self.module)

    @Inputs.module
    def set_module(self, module):
        if self.module is None:
            self.module = module

        self.commit()

    @Inputs.angle
    def set_angle(self, data):
        if type(data) == Table:
            if len(data) == 0 or len(data[0]) == 0:
                return

            self.angle = int(data[0][0].value)
        elif type(data) in [int, float]:
            self.angle = int(data)
        else:
            return

        self.commit()

if __name__ == '__main__':
    from Orange.widgets.utils.widgetpreview import WidgetPreview  # since Orange 3.20.0
    WidgetPreview(Angle).run()
