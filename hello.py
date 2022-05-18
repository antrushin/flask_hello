from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    print(1+2)
    return '<h1>Hello, MY very best friend!!!</h1>'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

@app.route('/avg/<nums>')
def avg(nums):
    # show the user profile for that user
    nums = nums.split(',')
    nums = [float(num) for num in nums]
    nums_mean = mean(nums)
    print(nums_mean)
    return str(nums_mean)