# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_1Dmod.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OneDmod(object):
    def setupUi(self, OneDmod):
        OneDmod.setObjectName("OneDmod")
        OneDmod.resize(729, 562)
        self.verticalLayout = QtWidgets.QVBoxLayout(OneDmod)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonLoadData = QtWidgets.QPushButton(OneDmod)
        self.buttonLoadData.setObjectName("buttonLoadData")
        self.horizontalLayout_3.addWidget(self.buttonLoadData)
        self.buttonSaveData = QtWidgets.QPushButton(OneDmod)
        self.buttonSaveData.setObjectName("buttonSaveData")
        self.horizontalLayout_3.addWidget(self.buttonSaveData)
        self.buttonSaveModel = QtWidgets.QPushButton(OneDmod)
        self.buttonSaveModel.setObjectName("buttonSaveModel")
        self.horizontalLayout_3.addWidget(self.buttonSaveModel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_1 = QtWidgets.QLabel(OneDmod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setObjectName("label_1")
        self.verticalLayout_6.addWidget(self.label_1)
        self.lineEditPeriodePerDecade = QtWidgets.QLineEdit(OneDmod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditPeriodePerDecade.sizePolicy().hasHeightForWidth())
        self.lineEditPeriodePerDecade.setSizePolicy(sizePolicy)
        self.lineEditPeriodePerDecade.setObjectName("lineEditPeriodePerDecade")
        self.verticalLayout_6.addWidget(self.lineEditPeriodePerDecade)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(OneDmod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.lineEditMaximumPeriode = QtWidgets.QLineEdit(OneDmod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditMaximumPeriode.sizePolicy().hasHeightForWidth())
        self.lineEditMaximumPeriode.setSizePolicy(sizePolicy)
        self.lineEditMaximumPeriode.setObjectName("lineEditMaximumPeriode")
        self.verticalLayout_5.addWidget(self.lineEditMaximumPeriode)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(OneDmod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.lineEditNumberOfDecade = QtWidgets.QLineEdit(OneDmod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditNumberOfDecade.sizePolicy().hasHeightForWidth())
        self.lineEditNumberOfDecade.setSizePolicy(sizePolicy)
        self.lineEditNumberOfDecade.setObjectName("lineEditNumberOfDecade")
        self.verticalLayout_4.addWidget(self.lineEditNumberOfDecade)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_4 = QtWidgets.QLabel(OneDmod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_9.addWidget(self.label_4)
        self.lineEditThickness = QtWidgets.QLineEdit(OneDmod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditThickness.sizePolicy().hasHeightForWidth())
        self.lineEditThickness.setSizePolicy(sizePolicy)
        self.lineEditThickness.setObjectName("lineEditThickness")
        self.verticalLayout_9.addWidget(self.lineEditThickness)
        self.verticalLayout_8.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_5 = QtWidgets.QLabel(OneDmod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_10.addWidget(self.label_5)
        self.lineEditResistivity = QtWidgets.QLineEdit(OneDmod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditResistivity.sizePolicy().hasHeightForWidth())
        self.lineEditResistivity.setSizePolicy(sizePolicy)
        self.lineEditResistivity.setObjectName("lineEditResistivity")
        self.verticalLayout_10.addWidget(self.lineEditResistivity)
        self.verticalLayout_8.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem2)
        self.verticalLayout_8.addLayout(self.verticalLayout_11)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        self.commandLinkButtonRun = QtWidgets.QCommandLinkButton(OneDmod)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButtonRun.sizePolicy().hasHeightForWidth())
        self.commandLinkButtonRun.setSizePolicy(sizePolicy)
        self.commandLinkButtonRun.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButtonRun.setCheckable(False)
        self.commandLinkButtonRun.setObjectName("commandLinkButtonRun")
        self.horizontalLayout.addWidget(self.commandLinkButtonRun)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.widgetCanvas = QtWidgets.QWidget(OneDmod)
        self.widgetCanvas.setObjectName("widgetCanvas")
        self.verticalLayout.addWidget(self.widgetCanvas)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 50)

        self.retranslateUi(OneDmod)
        QtCore.QMetaObject.connectSlotsByName(OneDmod)

    def retranslateUi(self, OneDmod):
        _translate = QtCore.QCoreApplication.translate
        OneDmod.setWindowTitle(_translate("OneDmod", "1D Modelling"))
        self.buttonLoadData.setText(_translate("OneDmod", "Load Data"))
        self.buttonSaveData.setText(_translate("OneDmod", "Save Data"))
        self.buttonSaveModel.setText(_translate("OneDmod", "Save Model"))
        self.label_1.setText(_translate("OneDmod", "Periode per Decade:"))
        self.label_2.setText(_translate("OneDmod", "Maximum Periode:"))
        self.label_3.setText(_translate("OneDmod", "Number of Decade:"))
        self.label_4.setText(_translate("OneDmod", "Thickness"))
        self.label_5.setText(_translate("OneDmod", "Resistivity"))
        self.commandLinkButtonRun.setText(_translate("OneDmod", "Run"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OneDmod = QtWidgets.QWidget()
    ui = Ui_OneDmod()
    ui.setupUi(OneDmod)
    OneDmod.show()
    sys.exit(app.exec_())

