import random


def gen_player_achievements() -> set[str]:
    pool: list[str] = [
        "Crafting Genius", "World Savior", "Master Explorer",
        "Collector Supreme", "Untouchable", "Boss Slayer",
        "Strategist", "Unstoppable", "Speed Runner",
        "Survivor", "Treasure Hunter", "First Steps",
        "Sharp Mind", "Hidden Path Finder"
    ]
    count: int = random.randint(5, 10)
    return set(random.sample(pool, k=count))


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    pool_set: set[str] = {
        "Crafting Genius", "World Savior", "Master Explorer",
        "Collector Supreme", "Untouchable", "Boss Slayer",
        "Strategist", "Unstoppable", "Speed Runner",
        "Survivor", "Treasure Hunter", "First Steps",
        "Sharp Mind", "Hidden Path Finder"
    }

    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_distinct: set[str] = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {all_distinct}")

    common: set[str] = alice.intersection(bob, charlie, dylan)
    print(f"\nCommon achievements: {common}\n")

    only_alice: set[str] = alice.difference(bob, charlie, dylan)
    only_bob: set[str] = bob.difference(alice, charlie, dylan)
    only_charlie: set[str] = charlie.difference(alice, bob, dylan)
    only_dylan: set[str] = dylan.difference(alice, bob, charlie)

    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")

    miss_alice: set[str] = pool_set.difference(alice)
    miss_bob: set[str] = pool_set.difference(bob)
    miss_charlie: set[str] = pool_set.difference(charlie)
    miss_dylan: set[str] = pool_set.difference(dylan)

    print(f"\nAlice is missing: {miss_alice}")
    print(f"Bob is missing: {miss_bob}")
    print(f"Charlie is missing: {miss_charlie}")
    print(f"Dylan is missing: {miss_dylan}")


if __name__ == "__main__":
    main()
