from datetime import datetime, timezone

REQUIRED_FIELDS = {'room_id', 'user_id', 'title', 'start_time', 'end_time'}


def validate_booking_payload(data: dict):
    if missing := REQUIRED_FIELDS - data.keys():
        return None, f"Brak wymaganego pola: {missing}"

    try:
        s_time = datetime.fromisoformat(data["start_time"])
        e_time = datetime.fromisoformat(data["end_time"])
    except ValueError:
        return None, "Niepoprawny format daty. Użyj ISO format."

    if s_time >= e_time:
        return None, "Czas rozpoczęcia musi być przed czasem zakończenia"

    # Dodanie strefy UTC, jeśli format ISO jej nie dostarczył
    if s_time.tzinfo is None:
        s_time = s_time.replace(tzinfo=timezone.utc)
    if e_time.tzinfo is None:
        e_time = e_time.replace(tzinfo=timezone.utc)

    if s_time < datetime.now(timezone.utc):
        return None, "Nie można rezerwować w przeszłości"

    parsed_data = data.copy()
    parsed_data["start_time"] = s_time
    parsed_data["end_time"] = e_time

    return parsed_data, None
