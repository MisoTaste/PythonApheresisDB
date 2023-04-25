import sqlite3
import tkinter as tk
from tkinter import filedialog

# データベース ファイルを選択する関数を作成します。 
def select_database_file():
    database_file_name = tk.filedialog.askopenfilename(filetypes=[("SQLite Databases", "*.db")])
    entry_database_file_name.insert(0, database_file_name)


# データを表示する関数を作成します。 
def display_data():
    database_file_name = entry_database_file_name.get()
    database_table_name = entry_database_table_name.get()

    # Connect to the database.
    connection = sqlite3.connect(database_file_name)
    cursor = connection.cursor()

    # Create a query to select all rows from the table.
    query = "SELECT * FROM {}".format(database_table_name)

    # Execute the query.
    cursor.execute(query)

    # Get the results.
    results = cursor.fetchall()

    # Display the results.
    for row in results:
        print(row)

    # Close the connection.
    connection.close()

# 新しいウィンドウを作成します。 
root = tk.Tk()

# データベース ファイル名のラベルを作成します。 
label_database_file_name = tk.Label(root, text="Database File Name")
# データベース ファイル名のテキスト入力ボックスを作成します。 
entry_database_file_name = tk.Entry(root)
# データベースファイルを選択するボタンを作成します。
button_select_database_file = tk.Button(root, text="Select Database File", command=select_database_file)
# データベース テーブル名のラベルを作成します。 
label_database_table_name = tk.Label(root, text="Database Table Name")
# データベース テーブル名のテキスト入力ボックスを作成します。 
entry_database_table_name = tk.Entry(root)
# データを表示するボタンを作成します。
button_display_data = tk.Button(root, text="Display Data", command=display_data)

# ウィジェットのグリッド レイアウトを作成します。 
label_database_file_name.grid(row=0, column=0)
entry_database_file_name.grid(row=0, column=1)
button_select_database_file.grid(row=0, column=2)
label_database_table_name.grid(row=1, column=0)
entry_database_table_name.grid(row=1, column=1)
button_display_data.grid(row=1, column=2)

# メインループを開始します。 
root.mainloop()
