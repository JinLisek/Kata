import pytest

from sum_multiples import solution


class TestMultiplesOf3Or5:
    @pytest.mark.parametrize(
        "input, expected_output",
        [
            (0, 0),
            (-33, 0),
            (3, 0),
            (4, 3),
            (5, 3),
            (7, 3 + 5 + 6),
            (11, 3 + 5 + 6 + 9 + 10),
            (16, 3 + 5 + 6 + 9 + 10 + 12 + 15),
        ],
    )
    def test_given_limit_then_sum_multiples_solution_should_return_sum_of_multiples(
        self, input, expected_output
    ):
        assert solution(input) == expected_output
