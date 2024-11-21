from flask import Flask, request, redirect, render_template, url_for
import os
import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        # 如果没有上传文件，跳转回主页
        return redirect(url_for('index'))

    file = request.files['file']

    if file.filename == '':
        # 如果文件名为空，跳转回主页
        return redirect(url_for('index'))

    # 保存上传的文件到指定文件夹
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    
    # 上传成功后可以跳转到新的页面或者显示成功信息
    return f"文件 {file.filename} 上传成功！"

if __name__ == '__main__':
    app.run(debug=True)
