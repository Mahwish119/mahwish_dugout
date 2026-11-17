TEAM_SIZE = 11
MAX_CREDITS = 100
MAX_FROM_ONE_FRANCHISE = 7

# ROLE-> (Minimum, maximum )numbers of players allowed in a team
ROLE_LIMITS = {
    "Wicket Keeper": (1, 4),
    "Batter": (3, 6),
    "All Rounder": (1, 4),
    "Bowler": (3, 6)
}

def check_player_count(team):
    """ The team must have exactly TEAM_SIZE players."""

    if len(team.players) != TEAM_SIZE:
        return [f"Team must have exactly {TEAM_SIZE} players, but has {len(team.players)}"]
    return[]

def check_credits(team):
    """ The total credits of the team must not be exceed MAX_CREDITS."""

    total = team.total_credits()
    if total > MAX_CREDITS:
        return [f"Team has {total} credits, but must not exceed {MAX_CREDITS}"]
    return[]

def check_franchise_limit(team):
    """ No more than MAX_FROM_ONE_FRANCHISE players froma single franchise"""
    errors = []
    for franchise, count in team.count_by_franchise().items():
        if count > MAX_FROM_ONE_FRANCHISE:
            errors.append(
                f"Team has {count} players from {franchise},"
                f" but must not exceed {MAX_FROM_ONE_FRANCHISE}"
                )
    return errors


