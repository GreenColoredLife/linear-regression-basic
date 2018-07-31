import csv
import matplotlib.pyplot as plt
import functions

filename = "data.csv"

x = []
y = []
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        x.append(int(row[0]))
        y.append(int(row[1]))
print(x)
print(y)
print("----------------------------")
parameters = [0, 0]
learning_rate = 0.001
iterations = 0
previous_error = -1
while True:
    functions.simul_update(parameters, learning_rate,
                           functions.hypothesis(parameters, x), y, x)
    print("E:", functions.cost_function(functions.hypothesis(parameters, x),
                                        y))
    iterations += 1
    d = previous_error - functions.cost_function(functions.hypothesis(parameters, x), y)
    if d <= 0.001 and previous_error != -1:
        break
    print("diff: ", d)
    previous_error = functions.cost_function(functions.hypothesis(parameters, x),
                                             y)
print("parameters: ", parameters)
print("iterations: ", iterations)
plt.scatter(x, y, color="red", s=10)
plt.plot(x, functions.hypothesis(parameters, x))
msg = "Burger Calories"
plt.title(msg)
plt.xlabel(header_row[0])
plt.ylabel(header_row[1])
plt.show()
