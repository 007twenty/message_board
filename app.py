from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# 初始化数据库
def init_db():
    try:
        with sqlite3.connect('messages.db') as conn:
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS messages
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         name TEXT NOT NULL,
                         content TEXT NOT NULL,
                         timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
            conn.commit()
    except sqlite3.Error as e:
        print(f"数据库初始化出错: {e}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        content = request.form.get('content')
        if name and content:
            try:
                with sqlite3.connect('messages.db') as conn:
                    c = conn.cursor()
                    c.execute("INSERT INTO messages (name, content) VALUES (?,?)", (name, content))
                    conn.commit()
                return redirect(url_for('index'))
            except sqlite3.Error as e:
                print(f"保存留言时出错: {e}")
    
    try:
        with sqlite3.connect('messages.db') as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM messages ORDER BY timestamp DESC")
            messages = c.fetchall()
        print(f"加载了 {len(messages)} 条留言")  # 调试输出
    except sqlite3.Error as e:
        print(f"加载留言时出错: {e}")
        messages = []
    
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    init_db()
    # 监听所有可用的网络接口，端口设为 5000
    app.run(host='0.0.0.0', port=5000, debug=False)