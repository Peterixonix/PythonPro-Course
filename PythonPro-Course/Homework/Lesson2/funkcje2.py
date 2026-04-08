def desc_temp(temp_value):
    
    if temp_value >= 20:
        return "warm"
    elif temp_value <= 10:
        return "cold"
    else:
        return "med_warm"

temps = [12, 15, 14, 18, 20, 19, 24, 21, 18, 17, 24]
for temp in temps:
    print(desc_temp(temp))