# 留言板应用

这是一个使用 Flask 和 SQLite 构建的简单留言板应用。

## 功能特点

- 用户可以发布留言
- 显示所有留言，按时间倒序排列
- 使用 SQLite 数据库存储数据
- 简洁的用户界面

## 技术栈

- Python 3.x
- Flask
- SQLite3
- HTML/CSS

## 安装和运行

1. 克隆仓库：
```bash
git clone https://github.com/007twenty/message_board.git
cd message_board
```

2. 安装依赖：
```bash
pip install flask
```

3. 运行应用：
```bash
python app.py
```

4. 在浏览器中访问：`http://localhost:5000`

## 项目结构

- `app.py` - 主应用文件
- `templates/` - HTML 模板目录
- `messages.db` - SQLite 数据库文件（首次运行时会自动创建） 