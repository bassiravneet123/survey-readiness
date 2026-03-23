"""
Facility Survey Readiness Assessment
Combined Flask app serving all CMS LTC Survey Pathways.
Deploy to Render, Railway, or PythonAnywhere.
"""

from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/restraints')
def restraints():
    return render_template('restraints.html')

@app.route('/respiratory')
def respiratory():
    return render_template('respiratory.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5060))
    app.run(debug=True, host='0.0.0.0', port=port)
