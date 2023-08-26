"""defines how year is addeed """

def add_years_to_date(original_date: int, years_to_add: int) -> int:
    """gets the original date and adds correct year amount"""
    result = original_date.replace(year=original_date.year + years_to_add)
    return result
