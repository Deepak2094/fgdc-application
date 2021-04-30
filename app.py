from flask import Flask, request, jsonify, render_template
from Multiple_Files import FGDC_Meta_Data_Automation


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('GMU_Libraries.html')


@app.route('/FGDC_data', methods=["post"])
def FGDC_data():
    data = request.form
    FGDC_Meta_Data_Automation(data)
    return "The files have been succesfully Updated"


if __name__ == "__main__":
    app.run(debug=True)
