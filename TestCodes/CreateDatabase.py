import os
import sqlite3

# データベース名
db_name = "TestDB.db"

# データベースファイルの存在チェック
if os.path.exists(db_name):
    # データベースファイルが存在する場合は、接続する
    conn = sqlite3.connect(db_name)
    print("データベースに接続しました。")

    # テーブル存在チェック
    cur = conn.cursor()
    table_exist_query = "SELECT count(*) FROM sqlite_master WHERE type='table' AND name='T_Test'"
    cur.execute(table_exist_query)
    table_exist = cur.fetchone()[0]

    if table_exist:
        # テーブルが存在する場合は、フィールドデータを取得する
        select_field_query = "PRAGMA table_info('T_Test')"
        cur.execute(select_field_query)
        fields = cur.fetchall()

        # フィールドデータがある場合は、テキストで表示する
        if fields:
            print("フィールドデータ:")
            for field in fields:
                print(f"Name: {field[1]}, Type: {field[2]}")
        else:
            # フィールドデータがない場合は、メッセージを表示する
            print("フィールドデータがありません。")

        # データが存在する場合は、テーブルデータを取得して表示する
        select_data_query = "SELECT * FROM T_Test"
        cur.execute(select_data_query)
        rows = cur.fetchall()

        if rows:
            print("テーブルデータ:")
            for row in rows:
                print(f"ID: {row[0]}, TestCode: {row[1]}, TestText: {row[2]}")
        else:
            print("データがありません。")
    else:
        # テーブルが存在しない場合は、テーブルを作成する
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS T_Test (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            TestCode TEXT,
            TestText TEXT
        );
        '''
        cur.execute(create_table_query)
        conn.commit()

        # データを追加するSQL文を定義する
        sql = "INSERT INTO T_Test (TestCode, TestText) VALUES (?, ?)"

        # データを追加する
        data = [
            ("C001", "サンプルデータ1"),
            ("C002", "サンプルデータ2"),
            ("C003", "サンプルデータ3"),
            ("C004", "サンプルデータ4")
        ]
        cur.executemany(sql, data)
        conn.commit()

        print("テーブルを作成しました。サンプルデータを追加しました。")

    # カーソルと接続を閉じる
    cur.close()
    conn.close()

else:
    # データベースファイルが存在しない場合は、作成して接続する
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    # テーブル作成のSQL文を定義
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS T_Test (
        ID INTEGER PRIMARY KEY,
        TestCode TEXT,
        TestText TEXT
    );
    '''
    # テーブル作成
    cur.execute(create_table_query)

    # データを追加するSQL文を定義する
    sql = "INSERT INTO T_Test (TestCode, TestText) VALUES (?, ?)"

    # データを追加する
    data = [
        ("C001", "サンプルデータ1"),
        ("C002", "サンプルデータ2"),
        ("C003", "サンプルデータ3"),
        ("C004", "サンプルデータ4")
    ]
    cur.executemany(sql, data)

    conn.commit()

    print("データベースを作成しました。")

    # カーソルと接続を閉じる
    cur.close()
    conn.close()
