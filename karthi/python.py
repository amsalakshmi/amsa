import statistics

def analyze_data(numbers):
    if len(numbers) == 0:
        return "No data provided"

    result = {}
    result["Total Count"] = len(numbers)
    result["Sum"] = sum(numbers)
    result["Average"] = sum(numbers) / len(numbers)
    result["Median"] = statistics.median(numbers)
    result["Maximum"] = max(numbers)
    result["Minimum"] = min(numbers)
    result["Standard Deviation"] = statistics.stdev(numbers) if len(numbers) > 1 else 0

    return result


# Sample Input
data = [12, 45, 23, 67, 34, 89, 21, 56]

output = analyze_data(data)

for key, value in output.items():
    print(f"{key} : {value}")