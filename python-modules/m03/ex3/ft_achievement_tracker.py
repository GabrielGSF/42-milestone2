#! /usr/bin/python3

import random


ACHIEVEMENTS: list[str] = [
    'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
    'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
    'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
    'Boss Slayer', 'Hidden Path Finder', 'Night Owl', 'Dragon Tamer',
    'Pacifist', 'Sharpshooter', 'Lucky Streak', 'Iron Will',
    'Merchant King', 'Lore Keeper', 'Fearless', 'Speed Demon',
    'Monster Hunter', 'Stealth Master', 'Puzzle Solver', 'Legendary Hero',
    'Explorer of Depths', 'Perfectionist', 'Comeback King', 'Team Player',
    'Lone Wolf', 'Potion Brewer', 'Beast Rider', 'Sky Walker',
    'Gold Hoarder', 'Relic Seeker', 'Arena Champion', 'Completionist'
]


def gen_player_achievements() -> set[str]:
    amount = random.randint(6, 12)
    return set(random.sample(ACHIEVEMENTS, amount))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")

    players: dict[str, set[str]] = {
        'Alice': gen_player_achievements(),
        'Bob': gen_player_achievements(),
        'Charlie': gen_player_achievements(),
        'Dylan': gen_player_achievements(),
    }

    for name in players:
        print(f"Player {name}: {players[name]}")

    distinct: set[str] = set()
    for name in players:
        distinct = distinct.union(players[name])
    print(f"All distinct achievements: {distinct}")

    common: set[str] = set(ACHIEVEMENTS)
    for name in players:
        common = common.intersection(players[name])
    print(f"Common achievements: {common}")

    for name in players:
        others: set[str] = set()
        for other in players:
            if other != name:
                others = others.union(players[other])
        print(f"Only {name} has: {players[name].difference(others)}")

    all_achievements: set[str] = set(ACHIEVEMENTS)
    for name in players:
        missing = all_achievements.difference(players[name])
        print(f"{name} is missing: {missing}")
