"""REAding a real match file """

import json



def load_match(path):
    """Return one match file as a dict."""

    with open(path, encoding="utf-8") as f:
        return json.load(f)


def deliveries(match):
    """yield every deliveries as (batting_tem, over_number, delivery)"""

    for innings in match["innings"]:
        for over in innings["overs"]:
            for delivery in over["deliveries"]:
                yield innings["team"], over["over"], delivery


# then, in m1.py
match = load_match("data\\matches\\match_01.json")
print(list(match.keys()))
print(match["info"]["teams"])
print(len(match["innings"]), "innings")

#then   
count = 0 
for team, over, ball in deliveries(match):
    count = count + 1
print(count, "delliveries in the match")


def is_ball_faced(delivery):
    """Wides and no-balls are not balls faced, by our league rules."""
 
    extras = delivery.get("extras", {})
 
    return "wides" not in extras and "noballs" not in extras
 
 
def batter_runs(match, batter):
    """Return the runs this batter scored with the bat in this match."""
 
    runs = 0
 
    for team, over, delivery in deliveries(match):
        if delivery["batter"] == batter:
            runs = runs + delivery["runs"]["batter"]
 
    return runs
 
 
def batter_card(match, batter):
    """Return runs, balls faced, fours and sixes for one batter."""
 
    runs = 0
    balls = 0
    fours = 0
    sixes = 0
 
    for team, over, delivery in deliveries(match):
        if delivery["batter"] != batter:
            continue
 
        off_the_bat = delivery["runs"]["batter"]
        runs = runs + off_the_bat
 
        if is_ball_faced(delivery):
            balls = balls + 1
        if off_the_bat == 4:
            fours = fours + 1
        if off_the_bat == 6:
            sixes = sixes + 1
 
    return {"runs": runs, "balls": balls, "fours": fours, "sixes": sixes}
