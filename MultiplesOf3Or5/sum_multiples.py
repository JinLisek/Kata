from functools import reduce


def sum_multiples_below_limit(multiple: int, limit: int):
    highest_multiple = limit - limit % multiple
    count_of_multiples = highest_multiple / multiple
    return (multiple + highest_multiple) * count_of_multiples / 2


def solution(limit: int):
    if limit <= 0:
        return 0

    limit -= 1

    return (
        sum_multiples_below_limit(multiple=3, limit=limit)
        + sum_multiples_below_limit(multiple=5, limit=limit)
        - sum_multiples_below_limit(multiple=15, limit=limit)
    )
