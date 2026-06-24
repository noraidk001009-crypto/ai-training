import csv

def clean_row(row):
    cmd = (row.get("command") or "").strip()
    if not cmd:
        return None
    try:
        ph = int(row["player_hp"])
        dh = int(row["dragon_hp"])
    except ValueError:
        return None
    return {"round": row["round"], "command": cmd, "player_hp": ph, "dragon_hp": dh, "note": row.get("note", "")}

# Demo only — see assignment for full file write
