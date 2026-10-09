#1
def inventory_summary(dic):
    total_count = 0
    for item in dic:
        total_count += dic[item][0]
    return total_count


#2
def print_args_kwargs(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")