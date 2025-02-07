from xmlrpc.client import boolean


def filter_by_state(operations: list, status: str = "EXECUTED") -> list:
    """Функция выбирает операции с указанным статусом"""
    res = []
    for z in operations:
        if z.get("state") == status:
            res.append(z)
    return res


def sort_by_date(operations: list, decrease: bool = True) -> list:
    """Функция сортирует операции по их дате"""
    res = sorted(operations, key=lambda d: d.get("date"), reverse=decrease)

    return res
