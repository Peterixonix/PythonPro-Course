
temps = [12.5, 13.0, 15.2, 14.8, 16.1, 17.0, 18.3, 19.5, 20.0, 18.7, 17.2]
rains = [False, False, True, False, True, False, False, True, True, False, False]


weather_data = [
    {"temp": t, "rain": r}
    for t, r in zip(temps, rains)]


for day in weather_data:
    print(day)
