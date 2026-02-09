def analyze_marks(marks):
    result = {}

    result["Total"] = sum(marks)
    result["Average"] = sum(marks) / len(marks)
    result["Highest"] = max(marks)
    result["Lowest"] = min(marks)

    passed = 0
    for m in marks:
        if m >= 40:
            passed += 1

    result["Passed Subjects"] = passed
    result["Failed Subjects"] = len(marks) - passed

    return result


marks = list(map(int, input("Enter marks separated by space: ").split()))

analysis = analyze_marks(marks)

for key, value in analysis.items():
    print(key, ":", value)


