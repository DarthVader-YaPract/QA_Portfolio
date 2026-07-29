import pytest

from miles import HobbitsPriorityStatus


class TestHobbitsPriorityStatus:

    @pytest.mark.parametrize(
        'miles, expected_status',
        [
            [299, 'Classic'],
            [300, 'Silver']
        ]
    )
    def test_add_miles_and_check_status(self, miles, expected_status):
        hobbits_priority = HobbitsPriorityStatus()

        hobbit = 'Голлум'
        hobbits_priority.add_new_hobbit(hobbit)
        hobbits_priority.add_miles_to_hobbit(hobbit, miles)

        assert hobbits_priority.get_status(hobbit) == expected_status