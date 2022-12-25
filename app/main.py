from rocketry import Rocketry
from rocketry.conds import daily

app = Rocketry()

@app.task('every 10 seconds')
def do_constantly():
    print('do constantly')

@app.task('every 1 minute')
def do_minutely():
    print('do minutely')

@app.task('every 1 hour')
def do_hourly():
    print('do hourly')

@app.task('every 1 day')
def do_daily():
    print('do daily')

@app.task('every 2 days 2 hours 20 seconds')
def do_custom():
    print('do custom')

if __name__ == "__main__":
    app.run()