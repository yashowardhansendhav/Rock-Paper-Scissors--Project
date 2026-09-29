history = []

def add_history(player, computer, result):
    history.append({
        "player": player,
        "computer": computer,
        "result": result
    })

def show_history():
    print("\n===== GAME HISTORY =====")

    for i, game in enumerate(history, 1):
        print(
            "Round", i,
            ":", "You =", game["player"],
            "| Computer =", game["computer"],
            "| Result =", game["result"]
        )