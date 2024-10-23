from flask import Flask, render_template, request, redirect, session, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # 用于session和flash消息

# 初始化购物车
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'cart' not in session:
        session['cart'] = []

    if request.method == 'POST':
        item = request.form['item']
        session['cart'].append(item)
        session.modified = True  # 标记 session 被修改
        flash(f'"{item}" 已添加到购物车！')
        return redirect(url_for('cart'))

    return render_template('index.html')

# 展示购物车页面
@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if request.method == 'POST':
        item_to_remove = request.form.get('item_to_remove')
        if item_to_remove in session['cart']:
            session['cart'].remove(item_to_remove)
            session.modified = True
            flash(f'"{item_to_remove}" 已从购物车删除！')
        return redirect(url_for('cart'))

    return render_template('cart.html', cart=session.get('cart', []))

# 启动应用
if __name__ == '__main__':
    app.run(debug=True)
