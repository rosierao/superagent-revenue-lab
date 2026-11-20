"""Helpers for detecting repeated payment event deliveries."""


def count_replays(event_ids):
    """Return how many deliveries repeat an event ID that was already seen.

    The first delivery of each event ID is the original; every later delivery
    of the same ID is a replay. For example, ["A", "B", "A", "A"] has two
    replays and an empty iterable has none.
    """
    seen = set()
    replays = 0
    for event_id in event_ids:
        if event_id in seen:
            replays += 1
        else:
            seen.add(event_id)
    return replays
