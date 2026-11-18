#! /usr/bin/python3

import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===")

    players = [
            'Alice', 'bob', 'Charlie',
            'dylan', 'Emma', 'Gregory',
            'john', 'kevin', 'Liam'
        ]
    print(f"Initial list of players: {players}")

    new_capitalized = [n.capitalize() for n in players]
    print(f"New list with all names capitalized: {new_capitalized}")

    only_capitalized = [n for n in players if n == n.capitalize()]
    print(f"New list of capitalized names only: {only_capitalized}")

    players_scores = {n: random.randint(0, 1000) for n in new_capitalized}
    average_score = sum(players_scores.values()) / len(players_scores)
    high_score = {n: s for n, s in players_scores.items() if s > average_score}
    print(f"Score dict: {players_scores}")
    print(f"Score average is: {round(average_score, 2)}")
    print(f"High scores: {high_score}")
