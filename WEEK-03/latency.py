latency_samples = [12.3, 9.7, 15.0, 11.6, 10.0, 20.2, 8.4]

def calculate_average(data):
    return sum(data) / len(data)

def get_summary(data):
    return {
        "min": min(data),
        "max": max(data),
        "average": calculate_average(data)
    }

def show_latency_summary():
    re = get_summary(latency_samples)
    print(re)

show_latency_summary()
