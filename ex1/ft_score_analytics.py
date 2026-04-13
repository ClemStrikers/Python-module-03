import sys


def process_scores() -> None:
    print("=== Player Score Analytics ===")

    args: list[str] = sys.argv[1:]
    scores: list[int] = []

    for arg in args:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if not scores:
        print("No scores provided. Usage: python3"
              "ft_score_analytics.py <score1> <score2> ...")
        return

    count: int = len(scores)
    total: int = sum(scores)
    avg: float = total / count
    high: int = max(scores)
    low: int = min(scores)
    score_range: int = high - low

    print(f"Scores processed: {scores}")
    print(f"Total players: {count}")
    print(f"Total score: {total}")
    print(f"Average score: {avg}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    process_scores()
