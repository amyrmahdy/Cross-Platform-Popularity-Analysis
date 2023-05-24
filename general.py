def convert_metric(x):
    last_character = x[-1]
    if last_character == "K":
        without_last = x[:-1]
        return float(without_last) * 1000
    elif last_character == "M":
        without_last = x[:-1]
        return float(without_last) * 1000000
    else:
        return x