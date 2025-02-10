def filter_by_state(operations: list, status: str = "EXECUTED") -> list:
    """Функция выбирает из списка операции с заданным статусом"""
    filtered_operations = []
    for operation in operations:
        if operation.get("state") == status:
            filtered_operations.append(operation)
    return filtered_operations


def sort_by_date(operations: list, decrease: bool = True) -> list:
    """Функция сортирует список операции по их дате"""
    sorted_operations = sorted(operations, key=lambda d: d.get("date"), reverse=decrease)

    return sorted_operations
