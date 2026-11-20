from revenue.replays import count_replays


def test_repeated_delivery_is_counted_for_each_extra_delivery():
    # "A" is delivered three times: one original and two replays. "B" is new.
    assert count_replays(["A", "B", "A", "A"]) == 2


def test_empty_list_has_no_replays():
    assert count_replays([]) == 0


def test_unique_deliveries_have_no_replays():
    assert count_replays(["A", "B", "C"]) == 0


def test_each_repeat_of_each_event_id_is_counted():
    # "A" repeats once, "B" repeats twice, "C" is delivered once.
    assert count_replays(["A", "B", "A", "B", "B", "C"]) == 3


def test_any_iterable_of_event_ids_is_accepted():
    assert count_replays(event_id for event_id in ("A", "A", "B", "B", "B")) == 3
