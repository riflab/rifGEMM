from PyQt5 import QtWidgets
import numpy as np


def error_dialog(error_list):
    temp = []
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    msg.setWindowTitle("Error Message")
    msg.setText("Fix the following issue")
    for i in error_list:
        temp.append(i + error_list[i])
    msg.setDetailedText("\n".join(temp))
    msg.exec_()


def check_error(val, text, error_list):
    if val == "":
        error_list[text] = " is blank"
    elif text == "Period per Decade" or text == "Maximum Period" or text == "Number of Decade":
        try:
            val = int(val)
        except Exception:
            error_list[text] = " must be an integer"
    else:
        try:
            val = list(map(int, val.split(',')))
        except ValueError:
            error_list[text] = " must be an integer and separate by comma"

    return error_list, val


def compute(period_per_decade,
            maximum_period,
            number_of_decade,
            thickness,
            resistivity):
    # compute period and frequency

    number_of_frequency = number_of_decade * period_per_decade + 1
    constant = np.exp(np.log(10) / period_per_decade)

    frequency = [1 / maximum_period]
    period = [maximum_period]

    for i in range(1, number_of_frequency):
        a = frequency[i - 1] * constant
        b = 1 / a
        frequency.append(a)
        period.append(b)

    # compute depth

    depth = [1.0]

    a = 0
    for i in range(len(thickness)):
        a += thickness[i]
        depth.append(a)
        depth.append(a)
    depth.append(a * 1000000)  # 1000000 denotes infinity

    # compute resistivity

    temp = resistivity
    resistivity = []
    for i in range(len(temp)):
        resistivity.append(temp[i])
        resistivity.append(temp[i])

    return frequency, period, depth, resistivity


def plot_curve(figure, widgetCanvas, resistivity1, depth, period, rho, pha):
    # create an axis
    ax1 = figure.add_subplot(1, 4, 1)
    ax2 = figure.add_subplot(2, 4, (2, 4))
    ax3 = figure.add_subplot(2, 4, (6, 8))

    # discards the old graph
    ax1.clear()
    ax2.clear()
    ax3.clear()

    # plot data
    ax1.loglog(resistivity1, depth, '-', linewidth=0.7)
    ax1.set_xlabel('Resistivity (ohm meter)', fontsize=8)
    ax1.set_ylabel('Depth (m)', fontsize=8)
    ax1.set_title('Model', fontsize=8)
    ax1.set_ylim(1, max(depth) / 100000)
    ax1.invert_yaxis()

    ax2.loglog(period, rho, '*-', linewidth=0.7, markersize=4)
    ax2.set_ylim(1, 1000)
    ax2.set_xlabel('Period (s)', fontsize=8)
    ax2.set_ylabel('Ohm meter', fontsize=8)
    ax2.set_title('Apparent Resistivity', fontsize=8)

    ax3.semilogx(period, pha, '*-', linewidth=0.7, markersize=4)
    ax3.set_ylim(0, 90)
    ax3.set_xlabel('Period (s)', fontsize=8)
    ax3.set_ylabel('Degree', fontsize=8)
    ax3.set_title('Phase', fontsize=8)

    figure.tight_layout()
    widgetCanvas.draw()
