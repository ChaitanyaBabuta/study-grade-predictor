study_hours = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
sleep_hours = [5, 6, 7, 6, 8, 7, 8, 7, 8, 4]
attendance  = [60, 65, 70, 75, 80, 85, 90, 92, 95, 50]
grades      = [45, 50, 58, 63, 70, 75, 82, 88, 93, 35]

def average(lst):
    total = 0
    for num in lst:
        total += num
    return total / len(lst)

def multiply_lists(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] * list2[i])
    return result

def simple_linear_regression(X, y):
    n = len(X)

    avg_x = average(X)
    avg_y = average(y)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator += (X[i] - avg_x) * (y[i] - avg_y)
        denominator += (X[i] - avg_x) ** 2

    slope = numerator / denominator
    intercept = avg_y - slope * avg_x

    return slope, intercept

slope, intercept = simple_linear_regression(study_hours, grades)

print(f"Slope     : {slope:.2f}")
print(f"Intercept : {intercept:.2f}")
print(f"Formula   : grade = {slope:.2f} × study_hours + {intercept:.2f}")

def predict(study_hour, slope, intercept):
    return slope * study_hour + intercept

print("\nActual vs Predicted:")
print("-" * 35)

predicted_grades = []

for i in range(len(study_hours)):
    pred = predict(study_hours[i], slope, intercept)
    predicted_grades.append(pred)
    print(f"Study: {study_hours[i]}hrs | Actual: {grades[i]} | Predicted: {pred:.1f}")


def mean_absolute_error(actual, predicted):
    total_error = 0
    for i in range(len(actual)):
        error = actual[i] - predicted[i]
        if error < 0:
            error = -error
        total_error += error
    return total_error / len(actual)

def r2_score(actual, predicted):
    avg_actual = average(actual)

    total_variance = 0
    explained_variance = 0

    for i in range(len(actual)):
        total_variance += (actual[i] - avg_actual) ** 2
        explained_variance += (actual[i] - predicted[i]) ** 2

    return 1 - (explained_variance / total_variance)


mae = mean_absolute_error(grades, predicted_grades)
r2 = r2_score(grades, predicted_grades)

print(f"\nAverage Error (MAE) : {mae:.2f} marks")
print(f"Accuracy (R²)       : {r2:.2f}")

print("\n--- Predict Your Grade ---")

my_hours = float(input("How many hours do you study per day? "))
my_grade = predict(my_hours, slope, intercept)

if my_grade > 100:
   my_grade = 100

print(f"\nPredicted Grade: {my_grade:.1f} / 100")

if my_grade >= 80:
    print("Great job! Keep it up ")
elif my_grade >= 60:
    print("Decent! A bit more effort will help ")
else:
    print("You might want to study a bit more ")


def draw_bar_chart(study_hrs, actual_grades):
    print("\n📊 Study Hours vs Grade (each █ = 5 marks)")
    print("-" * 45)

    for i in range(len(study_hrs)):
        bars = "█" * (actual_grades[i] // 5)
        print(f"Study {study_hrs[i]:2}hrs | {bars} {actual_grades[i]}")

draw_bar_chart(study_hours, grades)