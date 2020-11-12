class YearConverter:
    regex = r"20\d{2}"

    def to_python(self, value):
        return int(value)  # 문자열을 정수로 바꿔주는것

    def to_url(self, value):
        return str(value)  # 문자를 url 문자열로 리버싱

class MonthConverter(YearConverter):
    regex = r"\d{1,2}"
class DayConverter(YearConverter):
    regex = r"[0123]\d"   
