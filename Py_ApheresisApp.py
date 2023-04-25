
from multiprocessing import connection
import os
import sqlite3
import tkinter as tk
import tkinter.ttk as ttk

Aapheresis_category = aphe_category = ['CHDF','PMX-DHP','CART','PE']

Select_DataBase = "\Py_APheresisData.db"
TITLE_NAME_LABEL="アフェレーシス機材管理"

ROW_DATA_TITLE_LABEL="選択データ"
ROW_DATA_UPDATE_BUTTON_LABEL="更新"
ROW_DATA_INSERT_BUTTON_LABEL="追加"
ROW_DATA_SAVE_BUTTON_LABEL="保存"
INSERT_MESSAGE_DIALOG_TITLE="追加"
INSERT_MESSAGE_SUCCEED="追加成功"
INSERT_MESSAGE_FAILED="追加出来ません"
UPDATE_MESSAGE_DIALOG_TITLE="更新"
UPDATE_MESSAGE_SUCCEED="更新成功"
SAVE_MESSAGE_DIALOG_TITLE="保存"
SAVE_MESSAGE_SUCCEED="保存成功"
SAVE_MESSAGE_FAILED="保存できません"
SELECT_CLEAR_BUTTUN_LABEL="取消"

#class base():

# メイン画面の構成
class Application(ttk.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.master.title("IMH Aphresis DataBase System")
        self.master.geometry("900x600")
        self.menubar()
        self.createframe()
        # self.create_widgets()


    def menubar(self):
        """メニューバーの設定 """
        # menubarのコンテナの作成
        menubar = tk.Menu(self)
        self.master.config(menu=menubar)
        # ファイルメニュー
        menu_file = tk.Menu(menubar,tearoff=False)
        menubar.add_cascade(label="ファイル", menu=menu_file)
        # ファイルメニューにプルダウンメニューを追加
        # menu_file.add_command(label="保存", command=self.menu_file_save_click, accelerator="Ctrl+S")
        menu_file.add_separator() # 仕切り線
        menu_file.add_command(label="終了", command=self.master.destroy)
        menu_file.bind_all("<Control-s>", self.menu_file_save_click)

        # menubarを親として編集メニュー
        menu_edit = tk.Menu(menubar,tearoff=0,)
        menubar.add_cascade(label="  編集  ",menu=menu_edit)

        # 編集メニューにプルダウンメニューを追加
        menu_edit.add_command(label="設定")

        """ メニューバーの設定終了 """
    def createframe(self):

        # フレームの作成
        self.frame_upper = tk.Frame(self.master,width=900,height=25,bg="#E6E6E6")
        self.frame_upper.grid_propagate(False)
        self.frame_upper.place(x=0,y=0)

        self.frame_left1 = tk.LabelFrame(self.master,text="治療選択",width=120,height=250,padx=5,pady=5,bg="#E6E6E6")
        self.frame_left1.grid_propagate(False)
        self.frame_left1.place(x=5,y=20)

        # self.frame_right1 = tk.Frame(self.master,width=280,height=100,padx=5,pady=5,bg="#E6E6E6")
        # self.frame_right1.grid_propagate(False)
        # self.frame_right1.place(x=300,y=30)

        self.frame_center1 = tk.LabelFrame(self.master,text="最終治療患者リスト",width=470,height=250,padx=5,pady=5,bg="#E6E6E6")
        self.frame_center1.grid_propagate(False)
        self.frame_center1.place(x=125,y=25)

        self.frame_right2 = tk.LabelFrame(self.master,text="治療履歴リスト",width=500,height=290,padx=5,pady=5,bg="#E6E6E6")
        self.frame_right2.grid_propagate(False)
        self.frame_right2.place(x=380,y=305)
        '''
        # 治療ボタンの表示
        self.carebutton = SelectCare(self.frame_left1)
        self.carebutton.grid(row=2,column=0)
        '''
        # 患者リスト表示
        self.PtTree = PtSelectTree(self.frame_center1) 
        self.PtTree.grid(row=3,column=0,sticky=tk.W)

        # 治療リストの表示
        self.TreatTree = PtTreatTree(self.frame_right2)
        self.TreatTree.grid(row=2,column=0,sticky=tk.W)
    

    def create_widgets(self):
        #self.label_category = tk.Label(self.frame_left1,text="治療選択")
        #self.label_category.grid(row=0,column=0,sticky=tk.W)

        self.label = tk.Label(self.frame_left1,text="Select Care")
        self.label.grid(row=5,column=0,sticky=tk.W)
        self.select_care_entry = tk.Entry(self.frame_left1,width=15)
        self.select_care_entry.grid(row=6,column=0,sticky=tk.W)

        # ボタンを押したときのエントリーへの表示
        def click_button(care_name):
            def bt():
                self.select_care_entry.delete("0","end")
                self.select_care_entry.insert(0,str(care_name))
            return bt
        
        # ボタンの作成
        self.buttons = []
        for i,care_name in enumerate(aphe_category):
            self.buttons.append(str(care_name))
            self.button = tk.Button(self.frame_left1,text=care_name,width=10,height=1,command=click_button(care_name))
            self.button.grid(row=i+1,column=0,pady=5)
            

    # 関数群

    def menu_file_save_click(self,event=None):
        print("保存しました。")

class SelectCare(ttk.Frame):
    # 治療選択のボタングループ
    def __init__(self,master, frame_left1):
        super().__init__(master)
        self.tree = None
        self.createwidget()
        self.frame_left1 = frame_left1
        self.pack()

    def createwidget(self):
        # self.label = tk.Label(self.frame_left1,text="Select Care")
        # self.label.grid(row=5,column=0,sticky=tk.W)
        self.select_care_entry = tk.Entry(self.frame_left1,width=15)
        self.select_care_entry.grid(row=6,column=0,sticky=tk.W)

        # ボタンを押したときのエントリーへの表示
        def click_button(care_name):
            def bt():
                self.select_care_entry.delete("0","end")
                self.select_care_entry.insert(0,str(care_name))
            return bt
        
        # ボタンの作成
        self.buttons = []
        for i,care_name in enumerate(aphe_category):
            self.buttons.append(str(care_name))
            self.button = tk.Button(self.frame_left1,text=care_name,width=10,height=1,command=click_button(care_name))
            self.button.grid(row=i+1,column=0,pady=5)
        

class PtSelectTree(ttk.Frame):
    # 患者選択用のツリービュー
    def __init__(self,master):
        super().__init__(master)
        self.tree = None
        self.createWidget()
        self.pack()
    
    def createWidget(self):
        apheresis_category = ['CHDF','PMX-DHP','CART','PE']
        self.createButton(apheresis_category)
        self.createTree()
 
    def createButton(self, apheresis_category):
        self.apheresis_category = apheresis_category
        
        # クリックしたボタンのタイトルを取得して、ボタンの下に表示
        for button_title in self.apheresis_category:
            button = tk.Button(self, 
                               text=button_title,
                               width=10,
                               height=1, 
                               command=lambda button_title=button_title: self.button_clicked(button_title))
            button.pack()
            
        self.label = tk.Label(self, text="")
        self.label.pack()
      
    def button_clicked(self, button_title):
        self.label.configure(text=button_title)

   
    def setTableCommand(self,func):
        self.select_button1['command'] = func
    
    def createTree(self):
        self.tree = ttk.Treeview(self)
        self.tree["columns"] = (1,2,3,4)
        self.tree["show"] = "headings"

        self.tree.column(1,width=75)
        self.tree.column(2,width=100)
        self.tree.column(3,width=75)
        self.tree.column(4,width=100)

        self.tree.heading(1,text="患者ID")
        self.tree.heading(2,text="患者氏名")
        self.tree.heading(3,text="治療区分")
        self.tree.heading(4,text="最終治療日")

        
        for buf in self.getPtlist():
            self.tree.insert("","end",values=buf)

        #self.getSelectAction()
        self.tree.bind("<<TreeviewSelect>>",self.select_row)
        self.tree.pack()

    def select_row(self,event):
        self.selected_iid = self.tree.focus()
        self.select_pt = self.tree.item(self.selected_iid,'values')[0]

        PtTreatTree.self.select_care_entry(tk.END.self.select_pt)
        

    def setColums(self,columns):
        # テーブルの列名を指定
        self.columns = self.getPtLsitColumns(columns)
        self.tree["columns"] = self.columns
        for col in columns:
            self.tree.heading(col,text=col)


    def getSelectAction(self):
        # 患者を選択されたときに呼ばれるイベントを登録
        self.tree.bind("<<TreeviewSelect>>",self.getItem)
        #print("リストを選択しました")
        self.selected_iid = self.tree.focus()
        return self.tree.item(self.selected_iid,'values')

    def getItem(self):
        # 現在選択のレコードの取得
        self.selected_iid = self.tree.focus()
        return self.tree.item(self.selected_iid,"values")

    def getPtlist(self):
        # 患者リスト取得
        try:
            dbname = os.path.dirname(__file__) + "\Py_APheresisData.db"
            connection = sqlite3.connect(dbname)
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_keys = 1")
            
            Ptlist = []
            
            # 患者リスト取得
            sql = """
            SELECT P.Pt_ID,P.Pt_Name,P.TreatCode,MAX(P.StartDate) 
            FROM V_Patient_Apheresis AS P
            GROUP BY P.Pt_ID , TreatCode
            ORDER BY StartDate DESC
            """
            for r in cursor.execute(sql):
                Ptlist.append(r)
            connection.close()

        except sqlite3.Error as error:
            print(error)
        #print(Ptlist)
        return Ptlist


class PtTreatTree(ttk.Frame):
    # 患者リストのツリービュー
    def __init__(self,master):
        super().__init__(master)
        self.tree = None
        self.columns =[]
        self.createWidget()
        self.pack()
        self.setSampleData()

    def createWidget(self):
        self.select_table = select_tabel = tk.Entry(self,width=50)
        self.select_table.grid(row=0,column=0,sticky=tk.W)
        self.select_button1 = select_button1 = ttk.Button(self,text="Read")
        self.select_button1.grid(row=0,column=2,sticky=tk.W)

        self.tree = ttk.Treeview(self)
        self.tree["show"] = "headings"
        self.tree.grid(row=1,column=0,columnspan=2,sticky=tk.W)

        self.table = "V_Patient_Apheresis"

    def setColumns(self,columns):
        # テーブルの列名を指定
        self.columns = columns
        self.tree["columns"] = self.columns
        for col in columns:
            self.tree.heading(col,text=col)

    def setRow(self,index ="",row_data=[]):
        # 新規レコードの挿入
        self.tree.insert("",index="end",text=index,values = row_data)

    def setRows(self,rows_data):
        # 複数のレコードの挿入
        for i,row_data in enumerate(rows_data):
            self.setRow(index = i,row_data = row_data)

    def setSampleData(self):
        # 起動時のサンプルデータ
        column_data = ("Name","Value")
        rows_data = [("None","None")]
        self.deleteRows()
        self.setColumns(column_data)
        self.setRows(rows_data)

    def deleteRows(self):
        # レコードの全削除
        children = self.tree.get_children("")
        for child in children:
            self.tree.delete(child)

    def addSelectAction(self,func):
        # レコードが選択されたときに呼ばれるイベントを登録
        self.tree.bind("<<TreeviewSelect>>",func)

    def getItem(self):
        # 現在選択のレコードの取得
        self.selected_iid = self.tree.focus()
        return self.tree.item(self.selected_iid,"values")

    def getRows(self):
        # 全レコードの取得
        rows =[]
        children = self.tree.get_children("")
        for child in children:
            item = self.tree.item(child,"values")
            rows.append(item)
        return rows 

    def getColumn(self):
        # 列名の取得
        return self.columns

    def getDataMap(self):
        # 現在選択されているレコードの列名と値のマップを取得
        item = self.getItem()
        if len(self.columns) != len(item):
            return {"none":"none"}
        else:
            data_map = {}
            for i,column in enumerate(self.columns):
                data_map[column] = item[i]
            return data_map

    def updateValue(self,new_values):
        # 現在選択されている値の更新
        self.tree.item(self.selected_iid,values=new_values)

    def update(self,value_dict):
        # マップからリストに変更して値の更新
        data=[]
        for column in self.columns:
            data.append(value_dict[column])
        self.updateValue(data)

    def insert(self,value_dict):
        # マップからリストに変換して新規レコードの挿入
        data = []
        for column in self.columns:
            data.append(value_dict[column])
        children = self.tree.get_children("")
        index = len(children)
        self.setRow(index = str(index),row_data=data)

    #################################################
    def setNewColumnAndData(self,columns,rows):
        # 新しい列名とレコードをを設定する。プロパティのWidgetも更新する
        self.tree.deleteRows()
        self.tree.setColumns(columns)
        self.tree.setRows(rows)
        #self.property.createWidget(self.tree.getColumn())

    def setTableCommand(self,func):
        # テーブル名を決定した時のコマンドを登録する。
        self.select_button1.setTableCommand(func)


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':

    main()