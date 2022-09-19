import sys
from  PyQt5.QtWidgets import QMainWindow, QApplication
from test2 import Ui_MainWindow
import pandas as pd
import numpy as np
import functions as func

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        self.ui.pushButton.clicked.connect(self.showpage2)
        self.ui.pushButton_2.clicked.connect(self.showpage1)
    
    def uncheckallcols(self):
        self.ui.comboBox.uncheckall()
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit_3.setText("")
        self.ui.lineEdit_4.setText("")
        self.ui.lineEdit_5.setText("")
        self.ui.lineEdit_6.setText("")
        self.ui.comboBox2.uncheckall()
        self.ui.label_9.setText("")
    
    def checkcols(self):
        filters=[]
        filters.append(self.ui.comboBox.check_items())
            
        if self.ui.lineEdit_2.text():
            if self.ui.lineEdit_2.text().isdigit() and int(self.ui.lineEdit_2.text())>0:
                filters.append(int(self.ui.lineEdit_2.text()))
            else:
                self.ui.label_9.setText("Enter a valid number in Stipend column")
                self.ui.label_9.adjustSize()
                return False
        else:
            filters.append(0)
        
        if self.ui.lineEdit_3.text():
            if self.ui.lineEdit_3.text().isdigit() and int(self.ui.lineEdit_3.text())>0:
                filters.append(int(self.ui.lineEdit_3.text()))
            else:
                self.ui.label_9.setText("Enter a valid number in No of apllications column")
                self.ui.label_9.adjustSize()
                return False
        else:
            filters.append(0)
        
        if self.ui.lineEdit_4.text():
            if self.ui.lineEdit_4.text().isdigit() and int(self.ui.lineEdit_4.text())>0:
                filters.append(int(self.ui.lineEdit_4.text()))
            else:
                self.ui.label_9.setText("Enter a valid number in Duration column")
                self.ui.label_9.adjustSize()
                return False
        else:
            filters.append(0)
        
        if self.ui.lineEdit_5.text():
            if self.ui.lineEdit_5.text().isdigit() and int(self.ui.lineEdit_5.text())>0:
                filters.append(int(self.ui.lineEdit_5.text()))
            else:
                self.ui.label_9.setText("Enter a valid number in No of openings column")
                self.ui.label_9.adjustSize()
                return False
        else:
            filters.append(0)
        
        if self.ui.lineEdit_6.text():
            if self.ui.lineEdit_6.text().isdigit() and int(self.ui.lineEdit_6.text())>0:
                filters.append(int(self.ui.lineEdit_6.text()))
            else:
                self.ui.label_9.setText("Enter a valid number in Candidates hired column")
                self.ui.label_9.adjustSize()
                return False
        else:
            filters.append(0)
        
        filters.append(self.ui.comboBox2.check_items())
        return filters
    
    def preprocessing(self,fil):
        df = pd.read_excel('C:/Users/prasanth/mini/output2.xlsx',usecols = "A:O")
        df['Skills_required']=list(df['Skills_required'].fillna("None").str.lower().str.split(","))
        df['perks']=list(df['perks'].fillna("None").str.lower().str.split(","))
        df['location']=list(df['location'].fillna("None").str.lower().str.split(","))
        df['no_of_applications']=df['no_of_applications'].replace({'Be an early applicant':'0', ' applicants':'','\D+':''}, regex=True)
        df["no_of_applications"] = pd.to_numeric(df["no_of_applications"])
        skills=list(set(sum(df['Skills_required'].tolist(),[])))
        skl_set=pd.DataFrame(columns=skills,index=np.array(range(0,df.shape[0])))
        for i in range(0,df.shape[0]):
            for j in df['Skills_required'].iloc[i]:
                skl_set.at[i,j]=1
        skl_set=skl_set.fillna(0)
        df['Skills_required'].str.get_dummies(",")
        func.freaquent_patterns(skl_set,skills)
        D=func.to_1D(df['Skills_required']).value_counts().to_dict()
        D=dict(sorted(D.items(), key=lambda x: x[1], reverse=True))
        filtered_df=func.filtering(df,fil)
        aa=func.freaquent_patterns(skl_set,skills)
        y_pred_class,skill_set=func.multinomiannb(df,fil[0])
        #func.graphs(df,D)
        func.convert_to_excel(filtered_df,y_pred_class,skill_set)
    
    def show(self):
        self.main_win.show()

    def showpage2(self):
        if self.checkcols():
            self.ui.pushButton.setEnabled(False)
            self.preprocessing(self.checkcols())
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        
    def showpage1(self):
        self.ui.pushButton.setEnabled(True)
        self.uncheckallcols()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

if __name__ == "__main__":  
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())