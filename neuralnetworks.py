import math

# sigmoid function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# derivative of sigmoid
def sigmoid_derivative(y):
    return y * (1 - y)


# inputs
x1 = 0.35
x2 = 0.9

# weights (given in question)
w13 = 0.1
w23 = 0.8
w14 = 0.4
w24 = 0.6
w35 = 0.3
w45 = 0.9

# target output
target = 0.5

# learning rate
lr = 1


# ---------- FORWARD PASS ----------

a3 = x1*w13 + x2*w23
y3 = sigmoid(a3)

a4 = x1*w14 + x2*w24
y4 = sigmoid(a4)

a5 = y3*w35 + y4*w45
y5 = sigmoid(a5)

print("Output before training:", y5)


# ---------- BACKWARD PASS ----------

error = target - y5

delta5 = error * sigmoid_derivative(y5)

delta3 = sigmoid_derivative(y3) * (delta5 * w35)
delta4 = sigmoid_derivative(y4) * (delta5 * w45)

# update weights
w35 += lr * delta5 * y3
w45 += lr * delta5 * y4

w13 += lr * delta3 * x1
w23 += lr * delta3 * x2
w14 += lr * delta4 * x1
w24 += lr * delta4 * x2


# ---------- FORWARD PASS AGAIN ----------

a3 = x1*w13 + x2*w23
y3 = sigmoid(a3)

a4 = x1*w14 + x2*w24
y4 = sigmoid(a4)

a5 = y3*w35 + y4*w45
y5 = sigmoid(a5)

print("Output after training:", y5)
