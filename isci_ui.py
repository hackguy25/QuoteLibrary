# gumbi: btn_isci_nazaj
#        btn_isci_isci

# polja: field_isci_input    // QLineEdit
#        list_isci_rezultati // QListWidget

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Iskanje(QtWidgets.QWidget):
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
    
    def setupUi(self, Iskanje):
        Iskanje.setObjectName("Iskanje")
        Iskanje.resize(400, 180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Iskanje.sizePolicy().hasHeightForWidth())
        Iskanje.setSizePolicy(sizePolicy)
        Iskanje.setMinimumSize(QtCore.QSize(400, 180))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Iskanje)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_isci_nazaj = QtWidgets.QPushButton(Iskanje)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_isci_nazaj.sizePolicy().hasHeightForWidth())
        self.btn_isci_nazaj.setSizePolicy(sizePolicy)
        self.btn_isci_nazaj.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_isci_nazaj.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btn_isci_nazaj.setObjectName("btn_isci_nazaj")
        self.horizontalLayout_2.addWidget(self.btn_isci_nazaj)
        self.field_isci_input = QtWidgets.QLineEdit(Iskanje)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.field_isci_input.sizePolicy().hasHeightForWidth())
        self.field_isci_input.setSizePolicy(sizePolicy)
        self.field_isci_input.setMinimumSize(QtCore.QSize(0, 0))
        self.field_isci_input.setObjectName("field_isci_input")
        self.horizontalLayout_2.addWidget(self.field_isci_input)
        self.btn_isci_isci = QtWidgets.QPushButton(Iskanje)
        self.btn_isci_isci.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btn_isci_isci.setObjectName("btn_isci_isci")
        self.horizontalLayout_2.addWidget(self.btn_isci_isci)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.list_isci_rezultati = QtWidgets.QListWidget(Iskanje)
        self.list_isci_rezultati.setObjectName("list_isci_rezultati")
        self.verticalLayout.addWidget(self.list_isci_rezultati)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Iskanje)
        QtCore.QMetaObject.connectSlotsByName(Iskanje)

    def retranslateUi(self, Iskanje):
        _translate = QtCore.QCoreApplication.translate
        Iskanje.setWindowTitle(_translate("Iskanje", "Išči"))
        self.btn_isci_nazaj.setText(_translate("Iskanje", "Nazaj"))
        self.btn_isci_isci.setText(_translate("Iskanje", "Išči"))

