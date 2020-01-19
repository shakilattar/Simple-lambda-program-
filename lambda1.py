def func():
    f_temperatures = [90, 12, 34, 56, 95]
    c_temperatures = list(map(lambda t: (t-32) * (5/9), f_temperatures))
    print(f"c_temperatures = {c_temperatures}")


func()
