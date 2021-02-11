from flask import Flask, request, session, url_for, redirect
from urllib import parse
app = Flask(__name__)

app.secret_key = 'eadasecret_key'

@app.route('/in')
def index3():
    if 'username' in session:
        return '''
            session: %s <br><br><br>
            headers: %s <br><br><br>
            Logged in as %s'
        ''' % (session, request.headers, parse.quote(session['username']))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index3'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
