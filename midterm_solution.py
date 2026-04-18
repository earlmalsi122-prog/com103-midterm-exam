SPORTS = {
    1: ("Basketball", "Team"),
    2: ("Volleyball", "Team"),
    3: ("Badminton", "single_player"),
    4: ("Table Tennis", "single_player"),
    5: ("Soccer", "Team"),
}

WIN_POINTS = 3
LOSS_POINTS = 0
ENTRIES = 4

def get_standing(total):
    if total >= 9:
        return "GOLD CONTENDER"
    if total >= 6:
        return "SILVER PUSH"
    return "KEEP FIGHTING!"

def main():
    section = input("Section     : ").strip()
    coordinator = input("Coordinator : ").strip()

    print("\nSports events list:")
    for num, (name, cat) in SPORTS.items():
        print(f"  {num}. {name} ({cat})")

    games = []  
    total_points = 0

    for i in range(1, ENTRIES + 1):
        while True:
            try:
                s = int(input(f"\nGame {i} - sport number (0 to skip): "))
                if s in range(0, 6):
                    break
            except ValueError:
                pass
            print("  Invalid input. Enter 0 or 1-5.")
        if s == 0:
            games.append({"skipped": True})
            continue

        sport_name, sport_cat = SPORTS[s]
        opponent = input("  Opposing section: ").strip()
        while True:
            result = input("  Result (W/L): ").strip().upper()
            if result in ("W", "L"):
                break
            print("  Invalid. Enter W or L.")
        points = WIN_POINTS if result == "W" else LOSS_POINTS
        total_points += points
        games.append({
            "skipped": False,
            "sport_num": s,
            "sport": sport_name,
            "category": sport_cat,
            "opponent": opponent,
            "result": result,
            "points": points
        })

    standing = get_standing(total_points)

    
    print("\n" + "="*60)
    print(f"Section   : {section}")
    print(f"Coordinator: {coordinator}")
    print("-"*60)
    print(f"{'Game':<6}{'Sport (Category)':<30}{'Opponent':<15}{'Result':<8}{'Pts':<4}")
    print("-"*60)

    for idx, g in enumerate(games, start=1):
        if g.get("skipped"):
            print(f"Game {idx:<2} skipped (sport = 0)")
        else:
            sport_field = f"{g['sport']} ({g['category']})"
            print(f"Game {idx:<3}{sport_field:<30}{g['opponent']:<15}{g['result']:<8}{g['points']:<4}")

    print("-"*60)
    points_list = [str(g["points"]) for g in games if not g.get("skipped")]
    if not points_list:
        points_breakdown = "0"
    else:
        points_breakdown = " + ".join(points_list)
    print(f"Total: {points_breakdown} = {total_points}  ->  {standing}")
    print("="*60)

if __name__ == "__main__":
    main()
