


def read_rows(lines: list[str]) -> list[dict]:
    header = None
    rows = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        fields = [part.strip() for part in line.split(',')]
        if header is None:
            header = fields
            continue
        if len(fields) != len(header):
            continue
        rows.append(dict(zip(header, fields)))
    return rows

def count_types(rows: list[dict]) -> dict:
    counts = {}
    for row in rows:
        kind = row.get("тип")
        if kind is None:
            continue
        counts[kind] = counts.get(kind, 0) + 1
    return counts

def total_minutes(rows: list[dict], kind: str) -> float:
    total = 0.0
    for row in rows:
        if row.get("тип") != kind:
            continue
        try:
            total += float(row.get("минуты", "").replace(",", "."))
        except ValueError:
            continue
    return round(total, 1)

def to_csv(counts: dict) -> str:
    text = "тип,количество\n"
    for kind in sorted(counts):
        text += f"{kind},{counts[kind]}\n"
    return text
