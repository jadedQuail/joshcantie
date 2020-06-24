from flask import Flask, url_for, render_template, request

#############################
###     Start the app     ###
#############################

app = Flask(__name__)

#############################
###       Home Page       ###
#############################

@app.route('/')
def index():
    return render_template('index.html')

#############################
###       Blog Page       ###
#############################

@app.route('/blog')
def blog():
    return render_template('blog.html')
    
#############################
###     Portfolio Page    ###
#############################

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

#############################
###    FruitNShoot Page   ###
#############################   
 
@app.route('/fruitnshoot')
def fruit():
    return render_template('fruit.html')

#############################
###      Run the app      ###
#############################

if __name__ == '__main__':
    app.run(debug="True")