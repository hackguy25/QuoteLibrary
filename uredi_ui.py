# gumbi: btn_uredi_dodajTag
#        btn_uredi_izbrisi
#        btn_uredi_shrani
#        btn_uredi_preklici

# polja: field_uredi_quote   // QPlainTextEdit
#        field_uredi_naslov  // QLineEdit
#        field_uredi_avtor   // QLineEdit
#        list_uredi_tags     // QListWidget

from PyQt5 import QtCore, QtGui, QtWidgets
from urediTag_ui import Ui_UrediTag

class Ui_Uredi(QtWidgets.QWidget):
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.field_uredi_quote.textChanged.connect(self.spremembaQuota)
        self.btn_uredi_dodajTag.clicked.connect(self.startDodajTag)
        self.popup = None
        self.idx = None
        self.entry = None
    
    def closeEvent(self, event):
        if self.popup != None:
            self.popup.close()
    
    def spremembaQuota(self):
        if self.field_uredi_quote.toPlainText() == "":
            self.btn_uredi_shrani.setDisabled(True)
        else:
            self.btn_uredi_shrani.setDisabled(False)
    
    def startDodajTag(self):
        self.popup = Ui_UrediTag()
        self.popup.field_urediTag_stari.setDisabled(True)
        self.popup.btn_urediTag_izbrisi.setDisabled(True)
        self.popup.btn_urediTag_shrani.setDisabled(True)
        self.popup.btn_urediTag_preklici.clicked.connect(self.popup.close)
        self.popup.btn_urediTag_shrani.clicked.connect(self.shraniTag)
        self.popup.idx = len(self.entry["tags"])
        self.popup.show()
    
    def startUrediTag(self, tag):
        self.popup = Ui_UrediTag()
        self.popup.field_urediTag_stari.setText(tag.text())
        self.popup.field_urediTag_stari.setDisabled(True)
        self.popup.btn_urediTag_izbrisi.clicked.connect(self.izbrisiTag)
        self.popup.btn_urediTag_preklici.clicked.connect(self.popup.close)
        self.popup.btn_urediTag_shrani.clicked.connect(self.shraniTag)
        self.popup.idx = self.entry["tags"].index(tag.text())
        self.popup.listItem = tag
        self.popup.show()
    
    def shraniTag(self):
        if self.popup.idx >= len(self.entry["tags"]):
            self.entry["tags"].append(self.popup.field_urediTag_novi.text())
            self.list_uredi_tags.addItem(self.popup.field_urediTag_novi.text())
        else:
            self.entry["tags"][self.popup.idx] = self.popup.field_urediTag_novi.text()
            self.popup.listItem.setText(self.popup.field_urediTag_novi.text())
        self.popup.close()
    
    def izbrisiTag(self):
        self.entry["tags"].remove(self.popup.listItem.text())
        item = self.list_uredi_tags.takeItem(self.list_uredi_tags.row(self.popup.listItem))
        item = None
        self.popup.close()
    
    def setupUi(self, Uredi):
        Uredi.setObjectName("Uredi")
        Uredi.resize(400, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Uredi.sizePolicy().hasHeightForWidth())
        Uredi.setSizePolicy(sizePolicy)
        Uredi.setMinimumSize(QtCore.QSize(400, 240))
        self.verticalLayout = QtWidgets.QVBoxLayout(Uredi)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Uredi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 60))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.field_uredi_quote = QtWidgets.QPlainTextEdit(Uredi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.field_uredi_quote.sizePolicy().hasHeightForWidth())
        self.field_uredi_quote.setSizePolicy(sizePolicy)
        self.field_uredi_quote.setMinimumSize(QtCore.QSize(0, 60))
        self.field_uredi_quote.setMaximumSize(QtCore.QSize(16777215, 60))
        self.field_uredi_quote.setObjectName("field_uredi_quote")
        self.horizontalLayout.addWidget(self.field_uredi_quote)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(Uredi)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.field_uredi_naslov = QtWidgets.QLineEdit(Uredi)
        self.field_uredi_naslov.setObjectName("field_uredi_naslov")
        self.horizontalLayout_3.addWidget(self.field_uredi_naslov)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(Uredi)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.field_uredi_avtor = QtWidgets.QLineEdit(Uredi)
        self.field_uredi_avtor.setObjectName("field_uredi_avtor")
        self.horizontalLayout_4.addWidget(self.field_uredi_avtor)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(Uredi)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.list_uredi_tags = QtWidgets.QListWidget(Uredi)
        self.list_uredi_tags.setObjectName("list_uredi_tags")
        self.horizontalLayout_5.addWidget(self.list_uredi_tags)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_uredi_dodajTag = QtWidgets.QPushButton(Uredi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_uredi_dodajTag.sizePolicy().hasHeightForWidth())
        self.btn_uredi_dodajTag.setSizePolicy(sizePolicy)
        self.btn_uredi_dodajTag.setObjectName("btn_uredi_dodajTag")
        self.horizontalLayout_2.addWidget(self.btn_uredi_dodajTag)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_uredi_izbrisi = QtWidgets.QPushButton(Uredi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_uredi_izbrisi.sizePolicy().hasHeightForWidth())
        self.btn_uredi_izbrisi.setSizePolicy(sizePolicy)
        self.btn_uredi_izbrisi.setObjectName("btn_uredi_izbrisi")
        self.horizontalLayout_2.addWidget(self.btn_uredi_izbrisi)
        self.btn_uredi_shrani = QtWidgets.QPushButton(Uredi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_uredi_shrani.sizePolicy().hasHeightForWidth())
        self.btn_uredi_shrani.setSizePolicy(sizePolicy)
        self.btn_uredi_shrani.setObjectName("btn_uredi_shrani")
        self.horizontalLayout_2.addWidget(self.btn_uredi_shrani)
        self.btn_uredi_preklici = QtWidgets.QPushButton(Uredi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_uredi_preklici.sizePolicy().hasHeightForWidth())
        self.btn_uredi_preklici.setSizePolicy(sizePolicy)
        self.btn_uredi_preklici.setObjectName("btn_uredi_preklici")
        self.horizontalLayout_2.addWidget(self.btn_uredi_preklici)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Uredi)
        QtCore.QMetaObject.connectSlotsByName(Uredi)

    def retranslateUi(self, Uredi):
        _translate = QtCore.QCoreApplication.translate
        Uredi.setWindowTitle(_translate("Uredi", "Uredi"))
        self.label.setText(_translate("Uredi", "Quote:"))
        self.label_2.setText(_translate("Uredi", "Naslov knjige:"))
        self.label_3.setText(_translate("Uredi", "Avtor: "))
        self.label_4.setText(_translate("Uredi", "Tags:"))
        self.btn_uredi_dodajTag.setText(_translate("Uredi", "Dodaj tag"))
        self.btn_uredi_izbrisi.setText(_translate("Uredi", "Izbriši"))
        self.btn_uredi_shrani.setText(_translate("Uredi", "Shrani"))
        self.btn_uredi_preklici.setText(_translate("Uredi", "Prekliči"))

