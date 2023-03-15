from PyQt5.QtWidgets import QApplication, QMainWindow,QProgressBar,QPushButton,QMessageBox
import requests
import sys
flag=0

while True:
    try:
        requests.get('https://www.google.com/').status_code
        break
    except:
        class qError(QMainWindow):
            def __init__(self):
                super(qError,self).__init__()
                self.msg=QMessageBox()
                self.msg.setWindowTitle("Error")
                self.msg.setText("Internet connection is required")
                self.x=self.msg.exec_()
                exit()
                
        app=QApplication(sys.argv)
        st=qError()
        app.exec_()
from PyQt5 import uic


import time
class start(QMainWindow):
    def __init__(self):
        super(start,self).__init__()
        uic.loadUi("assets/start.ui",self)
        
        def load_page():
            global flag
            if flag==0:
                msg=QMessageBox()
                msg.setWindowTitle("Fail")
                msg.setText("Please load model")
                x=msg.exec_()
                
            else:
                from log_reg import logReg
                reg=logReg()
                self.close()
            
        def load_model():
            global flag
            for i in range(0,26):
                time.sleep(0.05)
                self.prog.setValue(i)  
            try:
                open("models/labels.txt","r")
                open("models/keras_model.h5","r")
                flag=1
                for i in range(26,101):
                    time.sleep(0.01)
                    self.prog.setValue(i)
                msg=QMessageBox()
                msg.setWindowTitle("Success")
                msg.setText("Successfully model loaded")
                x=msg.exec_()
                
                # from login_page_final import log
                # lg=log()
                
            except:
                try:
                    model="https://gdurl.com/OdgQ/download"
                    label="https://gdurl.com/cRQa/download"
                    respone=requests.get(label)
                    open("models/labels.txt","wb").write(respone.content)
                    for i in range(26,51):
                        time.sleep(0.01)
                        self.prog.setValue(i)
                    respone =requests.get(model)
                    open("models/keras_model.h5","wb").write(respone.content)
                    for i in range(51,101):
                        time.sleep(0.01)
                        self.prog.setValue(i)
                    msg=QMessageBox()
                    msg.setWindowTitle("Success")
                    msg.setText("Successfully model downloaded")
                    x=msg.exec_()            
                    flag=1         
                    # from login_page_final import log
                    # lg=log()   
                except Exception as e:
                    msg=QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText(str(e))
                    msg.setIcon(QMessageBox.Warning)
                    x=msg.exec_()
                
                    
        self.prog=self.findChild(QProgressBar,"prog")  
        self.load_btn=self.findChild(QPushButton,"load")
        self.start_btn=self.findChild(QPushButton,"start_btn")
        
        self.start_btn.clicked.connect(load_page)
        self.load_btn.clicked.connect(load_model)
        self.show()
        
app=QApplication(sys.argv)
st=start()
app.exec_()