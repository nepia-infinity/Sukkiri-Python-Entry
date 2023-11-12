from flask import Flask
import datetime
app = Flask(__name__)
@app.route('/')
def hello():
    dt    = datetime.datetime.now()
    html  = '<!DOCTYPE html>'
    html += '<html>'
    html += '<head><title>Flask Sample</title></head>'
    html += '<body>'
    html += '今日の日付：{}/{}/{}' .format(dt.year, dt.month, dt.day)
    html += '</body></html>'
    return html

if __name__ == '__main__':
    app.run()
