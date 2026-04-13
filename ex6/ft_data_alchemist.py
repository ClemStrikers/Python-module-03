import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    initial: list[str] = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam"
    ]
    print(f"Initial list of players: {initial}")

    all_cap: list[str] = [n.capitalize() for n in initial]
    print(f"New list with all names capitalized: {all_cap}")

    only_cap: list[str] = [n for n in initial if n[0].isupper()]
    print(f"New list of capitalized names only: {only_cap}")

    scores: dict[str, int] = {n: random.randint(1, 1000) for n in all_cap}
    print(f"Score dict: {scores}")

    total: int = sum(scores.values())
    avg: float = round(total / len(scores), 2)
    print(f"Score average is {avg}")

    high: dict[str, int] = {k: scores[k] for k in scores if scores[k] > avg}
    print(f"High scores: {high}")


if __name__ == "__main__":
    main()
