from django.core.cache import cache
import time

def get_very_complex_calculation_result():
    cache_key = 'complex_calculation'
    result = cache.get(cache_key)
    if result is None:
        print("Wykonuję skomplikowane obliczenia...")
        time.sleep(3)
        result = {"data": 42, "source": "Obliczone na żywo"}
        cache.set(cache_key, result, timeout=3600)
    else:
        print("Zwracam wynik cache!")
        result['sources'] = 'Pobrane z cache'
    return result