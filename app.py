from flask import Flask, render_template, request
import pickle as pkl

app = Flask(__name__)
model = pkl.load(open('heart_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form.get(key)) for key in request.form]
        prediction = model.predict([features])[0]
        result = 'Heart can Fail(1)' if prediction == 1 else 'Heart can not Fail(0)'
        return render_template('result.html', result=result)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
