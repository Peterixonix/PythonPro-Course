def is_nice_weather(temp: int, rain: bool) -> bool:
   
   if temp >= 15 and temp <= 25 and not rain:
      return True
   else:
      return False
  
temps = [12.5, 13.0, 15.2, 14.8, 16.1, 17.0, 18.3, 19.5, 20.0, 18.7, 17.2]
rains = [False, False, True, False, True, False, False, True, True, False, False]


weather_data = [
    {"temp": t, "rain": r}
    for t, r in zip(temps, rains)]


for day in weather_data:
    print(day)



nice_days_count = sum(1 for day in weather_data if is_nice_weather(day["temp"], day["rain"]))

print(f"Liczba ładnych dni: {nice_days_count}")