#! /usr/bin/python3

import sys


def parse_players_score(args: list[str]) -> list[int]:
    scores: list[int] = []
    i = 1
    while i < len(args):
        try:
            scores += [int(args[i])]
        except ValueError:
            print(f"Invalid parameter: '{args[i]}'")
        i += 1
    if len(scores) == 0:
        raise ValueError(f"No scores provided. Usage: python3 {args[0]} "
                         f"<score1> <score2> ...")
    return scores


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    try:
        scores = parse_players_score(sys.argv)
        total = sum(scores)
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {total}")
        print(f"Average score: {total / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    except ValueError as e:
        print(e)
