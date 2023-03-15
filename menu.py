from email.charset import QP
from PyQt5.QtWidgets import QMainWindow,QApplication,QLineEdit,QPushButton,QMessageBox,QStackedWidget,QTableWidget,QTableWidgetItem,QComboBox
from PyQt5 import uic,QtCore

import sys
import mysql.connector
import logo_rc

from keras.models import load_model
import numpy as np
import cv2

mydb=mysql.connector.connect(host="localhost",user="root",password="9930416664@Adu",database="inventory")
cursor=mydb.cursor()
flag=-1

class Menu_page(QMainWindow):
    def __init__(self):
        super(Menu_page,self).__init__()
        uic.loadUi("assets/menu.ui",self)
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
  
        
        
        # def close_win(self):
        #     self.close()
        
        self.stck=self.findChild(QStackedWidget,"stackedWidget")
        self.stck.setCurrentIndex(0)
        
        # self.close=self.findChild(QPushButton,"closeButton")
        # self.close.clicked.connect(close_win)
        
        def BUY_CAM():
            # Load the model
            model = load_model('models/keras_model.h5')
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            url = "http://10.20.30.16:8080/video"
            global flag
            flag=-1

            #Get the labels from the classes
            labels=list()
            with open('models/labels.txt','r') as file:
                label_data=file.readlines()
                for line in label_data:
                    labels.append(line[2:].rstrip())
                                
            flag=flag*-1
            
            #Capturing Code
            cap = cv2.VideoCapture(url)
            while True:
                ret,image=cap.read()
                if not ret:
                    break
                
                key=cv2.waitKey(1)
                if key%256==27 or flag==-1:
                    print("User closed Program")
                    break
            
            
                #Loading the Image into the correct size and normalizing for proper detection
                image = cv2.resize(image,(224,224))
                image_array = np.asarray(image)
                normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
                    
                data[0] = normalized_image_array

                #Running predicton based on the model and image provided
                prediction = model.predict(data)
                index=np.argmax(prediction)
                text=labels[index]
                self.base_model_name.setText(text)
                
        def SELL_CAM():
            # Load the model
            model = load_model('models/keras_model.h5')
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            url = "http://10.20.30.16:8080/video"
            global flag
            flag=-1

            #Get the labels from the classes
            labels=list()
            with open('models/labels.txt','r') as file:
                label_data=file.readlines()
                for line in label_data:
                    labels.append(line[2:].rstrip())
                                
            flag=flag*-1
            
            #Capturing Code
            cap = cv2.VideoCapture(url)
            while True:
                ret,image=cap.read()
                if not ret:
                    break
                
                key=cv2.waitKey(1)
                if key%256==27 or flag==-1:
                    print("User closed Program")
                    break
            
            
                #Loading the Image into the correct size and normalizing for proper detection
                image = cv2.resize(image,(224,224))
                image_array = np.asarray(image)
                normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
                    
                data[0] = normalized_image_array

                #Running predicton based on the model and image provided
                prediction = model.predict(data)
                index=np.argmax(prediction)
                text=labels[index]
                self.base_model_name_sell.setText(text)


        def get_item_amt(item):
            cursor.execute("select * from package_tracking")
            res=cursor.fetchall()
            for i in res:
                if i[2]==item:
                    return i[3]
                
        def submit_data():
            
            try:
                if self.ven_name.text() or self.base_model.text()  or self.model_drop.currentText()!="" or self.quan_edit.text():
                    item=self.model_drop.currentText()
                    amt=get_item_amt(item)
                    amt=amt-int(self.quan_edit.text())
                    cursor.execute(f'''update package_tracking set 
                                vendor_name="{self.ven_name.text()}",
                                Unit_Onhand={amt} 
                                where model_variant="{self.model_drop.currentText()}"''')
                    
                    mydb.commit()
                    self.ven_name.setText("")
                    self.base_model.setText("")
                    self.model_drop.setCurrentText("")
                    self.quan_edit.setText("")
                    
                else:
                    raise Exception("All Fields Should Be Filled")
                
            except Exception as e:
                msg=QMessageBox()
                msg.setWindowTitle("Failed")
                msg.setText("All Fields should be Filled")
                x=msg.exec_()
            

        def submit_data_sell():
            try:
                if self.name.text() or self.base_mod.text()  or self.mod_drop.currentText()!="" or self.qn_edit.text() or self.price_edit.text():
                    item=self.mod_drop.currentText()
                    amt=get_item_amt(item)
                    amt=amt-int(self.qn_edit.text())
                    q='insert into sold_tracking values(%s,%s,%s,%s,%s)'
                    val=(self.name.text(),self.base_mod.text(),self.mod_drop.currentText(),self.qn_edit.text(),(float(self.qn_edit.text())*float(self.price_edit.text())))
                    cursor.execute(q,val)
                    mydb.commit()
                    cursor.execute(f'''update package_tracking set Unit_Onhand={amt} where model_variant="{self.mod_drop.currentText()}" ''')
                    mydb.commit()
                    self.name.setText("")
                    self.base_mod.setText("")
                    self.mod_drop.setCurrentText("")
                    self.qn_edit.setText("")
                    self.price_edit.setText("")
                else:
                    raise Exception("All Fields Should Be Filled")
                
            except Exception as e:
                msg=QMessageBox()
                msg.setWindowTitle("Failed")
                msg.setText("All Fields Should Be Filled")
                x=msg.exec_()
        


        def open_buy():
            global flag
            flag=flag*-1
            self.stck.setCurrentIndex(1)
            item_value=self.base_model_name.text()
            self.base_model.setText(item_value)
            
            self.model_drop.clear()
            self.model_drop.addItem("")
            cursor.execute(f'select model_variant from package_tracking where base_variant="{item_value}"')
            res=cursor.fetchall()
            for i in res:
                self.model_drop.addItem(i[0])
            
        def open_sell():
            global flag
            flag=flag*-1
            self.stck.setCurrentIndex(2)
            item_value=self.base_model_name_sell.text()
            self.base_mod.setText(item_value)
            
            self.mod_drop.clear()
            self.mod_drop.addItem("")
            cursor.execute(f'select model_variant from package_tracking where base_variant="{item_value}"')
            res=cursor.fetchall()
            for i in res:
                self.mod_drop.addItem(i[0])

        def HOME_btn():
            self.stck.setCurrentIndex(0)
        def BUY_btn():
            self.stck.setCurrentIndex(3)
            BUY_CAM()
        def SELL_btn():
            self.stck.setCurrentIndex(4)
            SELL_CAM()
        
        
        
        def drop_update():
            if self.Item_select.currentText()=='All':
                cursor.execute("Select * from package_tracking")
                res=cursor.fetchall()
                if res:
                    self.Item_table.setRowCount(len(res)+1)
                    for i in range(0,len(res)):
                        self.Item_table.setItem(i+1,0,QTableWidgetItem(f'{res[i][0]}'))
                        self.Item_table.setItem(i+1,1,QTableWidgetItem(f'{res[i][1]}'))
                        self.Item_table.setItem(i+1,2,QTableWidgetItem(f'{res[i][2]}'))
                        self.Item_table.setItem(i+1,3,QTableWidgetItem(f'{res[i][3]}'))
                        
            else:
                cursor.execute(f'Select * from package_tracking where base_variant="{self.Item_select.currentText()}"')
                res=cursor.fetchall()
                if res:
                    self.Item_table.setRowCount(len(res)+1)
                    for i in range(0,len(res)):
                        self.Item_table.setItem(i+1,0,QTableWidgetItem(f'{res[i][0]}'))
                        self.Item_table.setItem(i+1,1,QTableWidgetItem(f'{res[i][1]}'))
                        self.Item_table.setItem(i+1,2,QTableWidgetItem(f'{res[i][2]}'))
                        self.Item_table.setItem(i+1,3,QTableWidgetItem(f'{res[i][3]}'))
        
        
        #Buy model_choose
        self.base_model_name=self.findChild(QLineEdit,"base_model_name")
        self.base_model_name_sell=self.findChild(QLineEdit,"base_model_name_sell")
        self.store_btn=self.findChild(QPushButton,"store_btn")
        self.store_btn.clicked.connect(open_buy)
        self.store_btn_sell=self.findChild(QPushButton,"store_btn_sell")
        self.store_btn_sell.clicked.connect(open_sell)
        
        #Buy Page
        self.ven_name=self.findChild(QLineEdit,"ven_name")
        self.base_model=self.findChild(QLineEdit,"base_model")
        self.model_drop=self.findChild(QComboBox,"model_drop")
        self.quan_edit=self.findChild(QLineEdit,"quan_edit")
        # print(self.quan_edit)
        
        self.submit_btn=self.findChild(QPushButton,"submit_btn")
        self.submit_btn.clicked.connect(submit_data)
        
        #Sell Page
        self.name=self.findChild(QLineEdit,"name")
        self.base_mod=self.findChild(QLineEdit,"base_mod")
        self.mod_drop=self.findChild(QComboBox,"mod_drop")
        self.qn_edit=self.findChild(QLineEdit,"qn_edit")
        self.price_edit=self.findChild(QLineEdit,"price_edit")
        self.sub_btn=self.findChild(QPushButton,"sub_btn")
        self.sub_btn.clicked.connect(submit_data_sell)
        
                
        #Find table element
        self.Item_select=self.findChild(QComboBox,"Item_select")
        self.Item_table=self.findChild(QTableWidget,"Item_table")
            
        #Find Side bar element
        self.table_button=self.findChild(QPushButton,"table_button")
        self.table_button.clicked.connect(HOME_btn)
        
        self.buy_button=self.findChild(QPushButton,"buy_button")
        self.buy_button.clicked.connect(BUY_btn)
        
        self.sell_button=self.findChild(QPushButton,"sell_button")
        self.sell_button.clicked.connect(SELL_btn)
            
        #Set table attributes
        self.Item_table.setColumnCount(4)
        self.Item_table.setRowCount(1)
        self.Item_table.setItem(0,0,QTableWidgetItem("Vendor Name"))
        self.Item_table.setItem(0,1,QTableWidgetItem("Base Variant"))
        self.Item_table.setItem(0,2,QTableWidgetItem("Model Variant"))
        self.Item_table.setItem(0,3,QTableWidgetItem("Quantity"))
        self.Item_table.setRowCount(1)
        
        self.Item_select.addItem("Default")
        self.Item_select.addItem("All")
        cursor.execute('select product_name from base_model')
        res=cursor.fetchall()
        
        for val in res:
            self.Item_select.addItem(val[0])
            
        self.Item_select.currentTextChanged.connect(drop_update)    
        
        self.show()        
            
            
# app=QApplication(sys.argv)
# l=Menu_page()
# app.exec_()  