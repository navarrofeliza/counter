from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def counter():
    print('*'*100)
    print('it is working!')
    if 'count' in session:
        session['count'] += 1
    else:    
        session['count'] = 0
    
    return render_template('index.html')

@app.route('/reset', methods = ['POST'])
def reset():
    print('*'*100)
    print('reset')
    session['count']= -1
    return redirect('/')

@app.route('/add1', methods = ['POST'])
def add1():
    print('*'*100)
    print('added 1')
    session['count']+=0
    return redirect('/')

@app.route('/add2', methods = ['POST'])
def add2():
    print('*'*100)
    print('added 2')
    session['count']+=1
    return redirect('/')

@app.route('/destroy', methods = ['POST'])
def destroy():
    print('*'*100)
    print('session')
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)