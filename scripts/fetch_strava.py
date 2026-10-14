import json
import os
import urllib.parse
import urllib.request
from datetime import date, datetime
from pathlib import Path

TOKEN_URL = "https://www.strava.com/oauth/token"
ACTIVITIES_URL = "https://www.strava.com/api/v3/athlete/activities?per_page=50"
OUTPUT = Path(__file__).resolve().parent.parent / "_data" / "strava.json"
SECRET_NAMES = ["STRAVA_CLIENT_ID", "STRAVA_CLIENT_SECRET", "STRAVA_REFRESH_TOKEN"]
RUN_TYPES = {"Run", "TrailRun", "VirtualRun"}
METERS_PER_MILE = 1609.344
MIN_DISTANCE_M = 1000
# A treadmill class and a watch often record the same run a minute or two apart.
DUPLICATE_WINDOW_S = 300
RUNS_SHOWN = 5


def get_access_token(client_id, client_secret, refresh_token):
    data = urllib.parse.urlencode({
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
    }).encode()
    with urllib.request.urlopen(TOKEN_URL, data=data, timeout=30) as response:
        token = json.load(response)
    if token["refresh_token"] != refresh_token:
        print("::warning::Strava issued a new refresh token. Update the STRAVA_REFRESH_TOKEN secret.")
    return token["access_token"]


def get_activities(access_token):
    request = urllib.request.Request(ACTIVITIES_URL, headers={"Authorization": f"Bearer {access_token}"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def start_time(activity):
    return datetime.fromisoformat(activity["start_date_local"].removesuffix("Z"))


def drop_duplicates(runs):
    kept = []
    for run in sorted(runs, key=lambda r: r["distance"], reverse=True):
        if all(abs((start_time(run) - start_time(k)).total_seconds()) > DUPLICATE_WINDOW_S for k in kept):
            kept.append(run)
    return sorted(kept, key=start_time, reverse=True)


def format_duration(seconds):
    hours, rest = divmod(round(seconds), 3600)
    minutes, secs = divmod(rest, 60)
    return f"{hours}:{minutes:02d}:{secs:02d}" if hours else f"{minutes}:{secs:02d}"


def format_run(run):
    miles = run["distance"] / METERS_PER_MILE
    return {
        "name": run["name"],
        "date": start_time(run).date().isoformat(),
        "distance": f"{miles:.2f} mi",
        "time": format_duration(run["moving_time"]),
        "pace": f"{format_duration(run['moving_time'] / miles)} /mi",
    }


def summarize_runs(activities, today):
    runs = [a for a in activities if a["sport_type"] in RUN_TYPES and a["distance"] >= MIN_DISTANCE_M]
    recent = drop_duplicates(runs)[:RUNS_SHOWN]
    return {"updated": today.isoformat(), "runs": [format_run(r) for r in recent]}


def write_summary(summary, path=OUTPUT):
    path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main():
    if not all(os.environ.get(name) for name in SECRET_NAMES):
        print("Strava secrets are not set; keeping the committed run list.")
        return
    access_token = get_access_token(*(os.environ[name] for name in SECRET_NAMES))
    summary = summarize_runs(get_activities(access_token), date.today())
    if not summary["runs"]:
        print("No runs found; keeping the committed run list.")
        return
    write_summary(summary)
    print(f"Wrote {len(summary['runs'])} runs to {OUTPUT}")


if __name__ == "__main__":
    main()
