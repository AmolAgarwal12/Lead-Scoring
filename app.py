import pickle
from typing import MutableMapping
# from typing_extensions import Required
from flask import Flask, render_template, request, jsonify
from more_itertools import last
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('modelsvm.pkl', 'rb'))


@app.route("/")
def hello():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if request.method == 'POST':
        # Donotemail
        Do_Not_Email = request.form['DoNotEmail']
        Do_Not_Email = int(Do_Not_Email)
        # Lead Origin
        Lead_Origin = request.form['leadOrigin']
        Lead_Origin = int(Lead_Origin)
        # Lead Source
        Lead_Source = request.form['leadSource']
        Lead_Source = int(Lead_Source)
        # lastactivity
        Last_Activity = request.form['lastActivity']
        Last_Activity = int(Last_Activity)
        # Specialization
        Specialization = request.form['specialization']
        Specialization = int(Specialization)
        # Whatisyourcurrentoccupation
        Current_Occupation = request.form['currentoccupation']
        Current_Occupation = int(Current_Occupation)
        # tags
        Tags = request.form['tags']
        Tags = int(Tags)
        # leadquality
        Lead_Quality = request.form['leadQuality']
        Lead_Quality = int(Lead_Quality)
        # city
        City = request.form['city']
        City = int(City)
        # lastnotableactivity
        Last_Notable_Activity = request.form['lastnotableactivity']
        Last_Notable_Activity = int(Last_Notable_Activity)
        Total_Visits = request.form.get('TotalVisits')
        Total_Visits = np.float32(Total_Visits)/251.0
        Total_Time_Spent_on_Website = request.form.get(
            'Total Time Spent on Website')
        Total_Time_Spent_on_Website = np.float32(
            Total_Time_Spent_on_Website)/2272
        Page_Views_Per_Visit = request.form.get('Page Views Per Visit')
        Page_Views_Per_Visit = np.float32(Page_Views_Per_Visit)/55.0
        # totalvisits = totalvisits/251

        # Total_Time_Spent_on_Website = Total_Time_Spent_on_Website/22741

        # Page_Views_Per_Visit = Page_Visited_on_Website/55
        prediction = model.predict([np.array([Lead_Origin, Lead_Source, Do_Not_Email,
                                    Total_Visits,
                                    Total_Time_Spent_on_Website,
                                    Page_Views_Per_Visit,
                                    Last_Activity,
                                    Specialization,
                                    Current_Occupation,
                                    Tags,
                                    Lead_Quality,
                                    City,
                                    Last_Notable_Activity])])

        output = round(prediction[0], 1)

        return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
