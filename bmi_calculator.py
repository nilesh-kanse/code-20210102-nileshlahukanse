# The below function will calculate the total number of overweight BMI category people in json data.
def bmi_calculator():
    raw_data = [{"g": "M", "h": 171, "w": 91}, {"g": "M", "h": 161, "w": 85}, {"g": "M", "h": 180, "w": 77},
                {"g": "M", "h": 166, "w": 62}, {"g": "M", "h": 150, "w": 70}, {"g": "M", "h": 167, "w": 82}]
    bmi_list = []
    overweight = 0
    for data in raw_data:
        bmi_list.append(round(data['w'] / (data['h'] / 100 * data['h'] / 100), 2))
    for x in bmi_list:
        if 25 <= x <= 29.9:
            overweight += 1
    print("Count of total number of overweight people in given data :", overweight)


bmi_calculator()
