from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
    
if __name__ == "__main__":
    # Below line of code also works
    # app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
    
    # Fix for Changes in templates not reflected on refresh unless server is restarted
    # 1. app.jinja_env.auto_reload = True
    # 2. app.config['TEMPLATES_AUTO_RELOAD'] = True
    # 3. set debug = True which enables reloader and debugger
    app.run(host='0.0.0.0', port=8080, debug = True)
    

