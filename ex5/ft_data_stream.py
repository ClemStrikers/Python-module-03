import typing
import random


def gen_event() -> typing.Generator[typing.Tuple[str, str], None, None]:
    players: typing.List[str] = ["alice", "bob", "charlie", "dylan"]
    actions: typing.List[str] = [
        "run", "eat", "sleep", "grab", "move",
        "climb", "swim", "release", "use"
    ]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    items: typing.List[typing.Tuple[str, str]]
) -> typing.Generator[typing.Tuple[str, str], None, None]:
    while len(items) > 0:
        index: int = random.randrange(len(items))
        yield items.pop(index)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    stream = gen_event()

    for i in range(1000):
        event: typing.Tuple[str, str] = next(stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    event_list: typing.List[typing.Tuple[str, str]] = []
    for _ in range(10):
        event_list.append(next(stream))

    print(f"Built list of 10 events: {event_list}")

    for item in consume_event(event_list):
        print(f"Got event from list: {item}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
