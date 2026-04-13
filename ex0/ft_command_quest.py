import sys


def run_command_quest() -> None:
    print("=== Command Quest ===")

    args: list[str] = sys.argv
    total_len: int = len(args)

    print(f"Program name: {args[0]}")

    if total_len <= 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {total_len - 1}")
        for i in range(1, total_len):
            print(f"Argument {i}: {args[i]}")

    print(f"Total arguments: {total_len}")


if __name__ == "__main__":
    run_command_quest()
