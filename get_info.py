def some_function(x):
    return x+1


def get_info(item):
    return [type(item), len(item), sorted(item)]


get_info(some_function)
