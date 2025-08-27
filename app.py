from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tip-calculator')
def tip_calculator():
    return render_template('tip_calculator.html')

@app.route('/plant-identifier')
def plant_identifier():
    return render_template('plant_identifier.html')

@app.route('/CrushVid')
def crushvid():
    return render_template('crushvid.html')

@app.route('/CrushVid-iphone')
def crushvid_iphone():
    return render_template('crushvid-iphone.html')

@app.route('/excuseme-privacy')
def excuseme_privacy():
    return render_template('excuseme-privacy.html')

@app.route('/voicemaster-privacy')
def voicemaster_privacy():
    return render_template('voicemaster-privacy.html')

@app.route('/tasktalk')
def tasktalk_privacy():
    return render_template('tasktalk-privacy.html')

@app.route('/app-ads.txt')
def serve_ads_txt():
    return send_from_directory('static', 'app-ads.txt')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
