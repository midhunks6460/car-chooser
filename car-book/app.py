from flask import Flask, render_template, request

app = Flask(__name__)

# Sample car data for demonstration
car_data = [
    {"company": "Company A", "model": "Model 1", "price": 15000, "mileage": 30, "safety": 5},
    {"company": "Company A", "model": "Model 2", "price": 20000, "mileage": 25, "safety": 4},
    {"company": "Company B", "model": "Model 3", "price": 18000, "mileage": 28, "safety": 4},
    # Add more car data as needed
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/select_car', methods=['POST'])
def select_car():
    user_budget = float(request.form['budget'])
    user_mileage = float(request.form['mileage'])
    user_safety = int(request.form['safety'])

    recommended_cars = []
    for car in car_data:
        if (
            car["price"] <= user_budget
            and car["mileage"] >= user_mileage
            and car["safety"] >= user_safety
        ):
            recommended_cars.append(car)

    return render_template('results.html', cars=recommended_cars)

if __name__ == '__main__':
    app.run(debug=True)
