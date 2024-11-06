from PyQt5.QtWidgets import QMainWindow,QApplication,QLineEdit,QPushButton,QMessageBox,QStackedWidget
from PyQt5 import uic
import sys
import mysql.connector

# Please make sure to add requirements.txt
# Add the elastic row on left for responsiveness
import logo_rc
from menu import Menu_page

mydb=mysql.connector.connect(host="localhost",user="root",password="9930416664@Adu",database="inventory")
cursor=mydb.cursor()

class logReg(QMainWindow):
    
    def __init__(self):
        super(logReg,self).__init__()
        ui=uic.loadUi("assets/log-reg.ui",self)
        
        # def CLOSE():
        #     QMainWindow.close()
        
        def verify_data():
            try:
                
                if self.reg_passC.text() and self.reg_pass.text() and self.user_edit_reg:
                    if self.reg_passC.text()==self.reg_pass.text():
                        sql='INSERT INTO accounts VALUES (%s,%s)'
                        val=(self.user_edit_reg.text(),self.reg_pass.text())
                        cursor.execute(sql,val)
                        mydb.commit()                
                        msg=QMessageBox()
                        msg.setWindowTitle("Success")
                        msg.setText("Successfully registered")
                        x=msg.exec_()
                        
                        self.reg_pass.setText("")
                        self.user_edit_reg.setText("")
                        self.reg_passC.setText("")
                        # self.close()
                        
                    else:
                        raise Exception("Passwords does not match")
                    
                        
                else:
                    raise Exception("Username/Password/Confirm Password is empty")
            except Exception as e:
                msg=QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText(str(e))
                msg.setIcon(QMessageBox.Warning)
                x=msg.exec_()
                
        def open_reg():
            self.stck.setCurrentIndex(1)
        
        def get_data():
            flag=0
            try:
                if self.log_id.text() and self.log_pass.text():
                    cursor.execute('select * from accounts')
                    res=cursor.fetchall()
                    if res:
                            for i in range(0,len(res)):
                                    if res[i][0]==self.log_id.text() and res[i][1]==self.log_pass.text():
                                            flag=1
                                            self.log_id.setText("")
                                            self.log_pass.setText("")
                                            msg=QMessageBox()
                                            msg.setWindowTitle("Success")
                                            msg.setText("Login Successfull")
                                            x=msg.exec_()
                                            mn=Menu_page()
                                            
                                            # self.close()
                                            break
                    if flag==0:
                        raise Exception("Account Unavailable, Please create account")
                else:
                    raise Exception("Username/Passsword is Empty")
                
            except Exception as e:
                msg=QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText(str(e))
                msg.setIcon(QMessageBox.Warning)
                x=msg.exec_()
            
            
            
        self.stck=self.findChild(QStackedWidget,"stackedWidget")
        self.stck.setCurrentIndex(0)
        #Register Page
        
        self.user_edit_reg=self.findChild(QLineEdit,"user_edit_reg")
        self.reg_pass=self.findChild(QLineEdit,"reg_pass")
        self.user_passC=self.findChild(QLineEdit,"reg_passC")
        self.reg_sub=self.findChild(QPushButton,"reg_sub")
        self.reg_sub.clicked.connect(verify_data)

        #breaking responsive nature here
        
        #Login Page
        self.log_id=self.findChild(QLineEdit,"log_id")
        self.log_pass=self.findChild(QLineEdit,"log_pass")
        self.log_sub=self.findChild(QPushButton,"log_sub")
        self.log_sub.clicked.connect(get_data)
        self.reg_btn=self.findChild(QPushButton,"reg_btn")
        self.reg_btn.clicked.connect(open_reg)
        
        #Control Buttons
        self.close=self.findChild(QPushButton,"close")
        # self.close.clicked.connect(CLOSE)
        self.min=self.findChild(QPushButton,"min")
        self.restore=self.findChild(QPushButton,"restore")
                
        ui.show()
        
# app=QApplication(sys.argv)
# l=logReg()
# app.exec_()    
