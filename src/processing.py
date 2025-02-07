def filter_by_state(operations, status="EXECUTED"):
    res = []
    for z in operations:
        if z.get('state') == status:
            res.append(z)
    return res


def sort_by_date(operations, decrease=True):

    res = sorted(operations, key=lambda d: d.get('date'), reverse=decrease)

    return res
