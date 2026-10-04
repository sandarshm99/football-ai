def normalize_team_name(name: str) -> str:
    normalized = name.strip().lower()

    if normalized.startswith("afc "):
        normalized = normalized[4:]

    normalized = normalized.replace(" football club", "")
    normalized = normalized.replace(" fc", "")
    normalized = normalized.replace(" afc", "")

    return normalized
