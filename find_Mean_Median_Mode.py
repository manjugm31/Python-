import statistics

def finding(list1):
    mean_value = statistics.mean(list1)
    median_value = statistics.median(list1)
    mode_value = statistics.mode(list1)
    return mode_value, mean_value, median_value

list1 = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8]
result = finding(list1)

print(result)
