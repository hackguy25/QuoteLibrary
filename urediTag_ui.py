# gumbi: btn_urediTag_izbrisi
#        btn_urediTag_shrani
#        btn_urediTag_preklici

# polja: field_urediTag_stari  // QLineEdit
#        field_urediTag_novi   // QLineEdit


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UrediTag(QtWidgets.QWidget):
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.field_urediTag_novi.textChanged.connect(self.spremembaTaga)
        self.idx = None
        self.listItem = None
    
    def spremembaTaga(self):
        if self.field_urediTag_novi.text() == "":
            self.btn_urediTag_shrani.setDisabled(True)
        else:
            self.btn_urediTag_shrani.setDisabled(False)
    
    def setupUi(self, UrediTag):
        UrediTag.setObjectName("UrediTag")
        UrediTag.resize(320, 99)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UrediTag.sizePolicy().hasHeightForWidth())
        UrediTag.setSizePolicy(sizePolicy)
        UrediTag.setMinimumSize(QtCore.QSize(320, 99))
        UrediTag.setMaximumSize(QtCore.QSize(16777215, 99))
        self.verticalLayout = QtWidgets.QVBoxLayout(UrediTag)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(UrediTag)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.field_urediTag_stari = QtWidgets.QLineEdit(UrediTag)
        self.field_urediTag_stari.setObjectName("field_urediTag_stari")
        self.horizontalLayout.addWidget(self.field_urediTag_stari)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(UrediTag)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(60, 0))
        self.label_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.field_urediTag_novi = QtWidgets.QLineEdit(UrediTag)
        self.field_urediTag_novi.setObjectName("field_urediTag_novi")
        self.horizontalLayout_2.addWidget(self.field_urediTag_novi)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_urediTag_izbrisi = QtWidgets.QPushButton(UrediTag)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_urediTag_izbrisi.sizePolicy().hasHeightForWidth())
        self.btn_urediTag_izbrisi.setSizePolicy(sizePolicy)
        self.btn_urediTag_izbrisi.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_urediTag_izbrisi.setObjectName("btn_urediTag_izbrisi")
        self.horizontalLayout_3.addWidget(self.btn_urediTag_izbrisi)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btn_urediTag_shrani = QtWidgets.QPushButton(UrediTag)
        self.btn_urediTag_shrani.setObjectName("btn_urediTag_shrani")
        self.horizontalLayout_3.addWidget(self.btn_urediTag_shrani)
        self.btn_urediTag_preklici = QtWidgets.QPushButton(UrediTag)
        self.btn_urediTag_preklici.setObjectName("btn_urediTag_preklici")
        self.horizontalLayout_3.addWidget(self.btn_urediTag_preklici)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(UrediTag)
        QtCore.QMetaObject.connectSlotsByName(UrediTag)

    def retranslateUi(self, UrediTag):
        _translate = QtCore.QCoreApplication.translate
        UrediTag.setWindowTitle(_translate("UrediTag", "Uredi tag"))
        self.label.setText(_translate("UrediTag", "Stari tag:"))
        self.label_2.setText(_translate("UrediTag", "Novi tag:"))
        self.btn_urediTag_izbrisi.setText(_translate("UrediTag", "Izbriši"))
        self.btn_urediTag_shrani.setText(_translate("UrediTag", "Shrani"))
        self.btn_urediTag_preklici.setText(_translate("UrediTag", "Prekliči"))

