from PyQt5 import QtWidgets, QtCore
from mainMenu_ui import Ui_MainMenu
from isci_ui import Ui_Iskanje
from uredi_ui import Ui_Uredi
import sys, json, atexit

db_file = "quotes.json"
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

def idxInDb(quote: str, db: list) -> int:
    for i in range(len(db)):
        if db[i]["quote"] == quote: return i
    return len(db)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Quote Library")
        self.popup = None
        self.startMainMenu()
    
    def closeEvent(self, event):
        if self.popup != None:
            self.popup.close()
    
    # Widgeti glavnega okna
    def startMainMenu(self):
        self.uiMainMenu = Ui_MainMenu()
        self.setCentralWidget(self.uiMainMenu)
        self.uiMainMenu.btn_mainMenu_dodaj.clicked.connect(self.startDodajanje)
        self.uiMainMenu.btn_mainMenu_isci.clicked.connect(self.startIskanje)
        self.show()
    
    def startIskanje(self):
        self.uiIskanje = Ui_Iskanje()
        self.setCentralWidget(self.uiIskanje)
        self.uiIskanje.btn_isci_nazaj.clicked.connect(self.startMainMenu)
        self.uiIskanje.btn_isci_isci.clicked.connect(self.isciPoQuotih)
        self.uiIskanje.field_isci_input.returnPressed.connect(self.isciPoQuotih)
        self.uiIskanje.list_isci_rezultati.setSelectionMode(1) # 1 == SingleSelection
        self.uiIskanje.list_isci_rezultati.itemDoubleClicked.connect(self.startUrejanje)
        self.show()
        for entry in db:
            self.uiIskanje.list_isci_rezultati.addItem(entry["quote"])
    
    # Funkcije za delo s quoti
    def startDodajanje(self):
        self.popup = Ui_Uredi()
        self.popup.btn_uredi_preklici.clicked.connect(self.popup.close)
        self.popup.btn_uredi_shrani.clicked.connect(self.shraniSpremembo)
        self.popup.idx = len(db)
        self.popup.entry = {"quote": "", "naslov": "", "avtor": "", "tags": []}
        self.popup.btn_uredi_shrani.setDisabled(True)
        self.popup.btn_uredi_izbrisi.setDisabled(True)
        self.popup.list_uredi_tags.setSelectionMode(1) # 1 == SingleSelection
        self.popup.list_uredi_tags.insertItems(0, self.popup.entry["tags"])
        self.popup.list_uredi_tags.itemDoubleClicked.connect(self.popup.startUrediTag)
        self.popup.show()
    
    def startUrejanje(self, izbraniQuote):
        self.popup = Ui_Uredi()
        self.popup.btn_uredi_preklici.clicked.connect(self.popup.close)
        self.popup.btn_uredi_shrani.clicked.connect(self.shraniSpremembo)
        self.popup.btn_uredi_izbrisi.clicked.connect(self.izbrisiQuote)
        self.popup.idx = idxInDb(izbraniQuote.text(), db)
        self.popup.entry = db[self.popup.idx]
        self.popup.field_uredi_quote.setPlainText(self.popup.entry["quote"])
        self.popup.field_uredi_naslov.setText(self.popup.entry["naslov"])
        self.popup.field_uredi_avtor.setText(self.popup.entry["avtor"])
        self.popup.list_uredi_tags.setSelectionMode(1) # 1 == SingleSelection
        self.popup.list_uredi_tags.insertItems(0, self.popup.entry["tags"])
        self.popup.list_uredi_tags.itemDoubleClicked.connect(self.popup.startUrediTag)
        self.popup.show()
    
    def shraniSpremembo(self):
        if self.popup != None:
            self.popup.entry["quote"] = self.popup.field_uredi_quote.toPlainText()
            self.popup.entry["naslov"] = self.popup.field_uredi_naslov.text()
            self.popup.entry["avtor"] = self.popup.field_uredi_avtor.text()
            if self.popup.idx >= len(db):
                db.append(self.popup.entry)
            else:
                db[self.popup.idx] = self.popup.entry
            self.popup.close()
    
    def izbrisiQuote(self):
        if self.popup != None:
            item = self.centralWidget().list_isci_rezultati.takeItem(self.popup.idx)
            item = None
            db.remove(self.popup.entry)
            self.popup.close()
    
    def isciPoQuotih(self):
        uiIskanje = self.centralWidget()
        uiIskanje.list_isci_rezultati.clear()
        uiIskanje.field_isci_input.setDisabled(True)
        uiIskanje.btn_isci_isci.setDisabled(True)
        iskaniIzraz = uiIskanje.field_isci_input.text()
        
        for entry in db:
            if (iskaniIzraz in entry["quote"] or iskaniIzraz in entry["naslov"] or
                    iskaniIzraz in entry["avtor"] or any(iskaniIzraz in s for s in entry["tags"])):
                quote = entry["quote"].replace("\n", "; ").replace("\t", "; ");
                uiIskanje.list_isci_rezultati.addItem(quote)
        
        uiIskanje.field_isci_input.setDisabled(False)
        uiIskanje.btn_isci_isci.setDisabled(False)
    
def shrani():
    with open(db_file, "w") as f:
        json.dump(db, f, indent = 4)

if __name__ == "__main__":
    
    atexit.register(shrani)
    db = None
    try:
        f = open(db_file)
        db = json.load(f)
        f.close()
    except FileNotFoundError:
        f = open(db_file, "w+")
        f.write("[]")
        f.close()
        db = []
    except json.decoder.JSONDecodeError:
        db = []
    
    
    
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
