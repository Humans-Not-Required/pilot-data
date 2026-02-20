#!/usr/bin/env python3
"""
pilot-trend-analysis.py — Day-over-day trend analysis for Gerundium Trust Stack pilot.

Reads snapshot data from snapshots/ directory and computes:
  - Per-agent daily commit/PR/star trends
  - Velocity direction (accelerating/stable/decelerating)
  - Stars gained since baseline (2026-02-18)
  - Consistency score (coefficient of variation, lower = more consistent)

Usage:
  python3 scripts/pilot-trend-analysis.py [--json] [--agent AGENT_ID]

Output: formatted table (default) or JSON (--json flag)
"""

import argparse
import json
import math
import os
import sys

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SNAPSHOTS_DIR = os.path.join(BASE_DIR, "snapshots")
BASELINE_DATE = "2026-02-18"
PILOT_START = "2026-02-19"


def load_snapshot(date: str, agent_id: str) -> dict | None:
    path = os.path.join(SNAPSHOTS_DIR, date, f"{agent_id}.json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return None


def get_pilot_dates() -> list[str]:
    """Return sorted list of all available snapshot dates."""
    dates = sorted(
        d for d in os.listdir(SNAPSHOTS_DIR)
        if d.startswith("2026-") and os.path.isdir(os.path.join(SNAPSHOTS_DIR, d))
    )
    return dates


def get_all_agents(dates: list[str]) -> list[str]:
    """Return sorted list of all agent IDs seen across any date."""
    agents = set()
    for date in dates:
        dpath = os.path.join(SNAPSHOTS_DIR, date)
        for fname in os.listdir(dpath):
            if fname.endswith(".json") and fname != "all.json":
                agents.add(fname.replace(".json", ""))
    return sorted(agents)


def extract_metrics(snapshot: dict) -> dict:
    """Extract aggregated metrics from a snapshot."""
    repos = snapshot.get("repos", [])
    commits = sum(r.get("commits_24h", 0) for r in repos)
    prs = sum(r.get("prs_merged_24h", 0) for r in repos)
    stars = sum(r.get("stars", 0) for r in repos)
    releases_today = sum(
        len(r.get("recent_releases", [])) for r in repos
    )
    return {
        "commits_24h": commits,
        "prs_merged_24h": prs,
        "stars_total": stars,
        "releases_today": releases_today,
    }


def trend_arrow(values: list[float]) -> str:
    """Return trend direction arrow based on sequence of values."""
    if len(values) < 2:
        return "→"
    # Compare second half to first half (or last to first)
    if len(values) == 2:
        diff = values[1] - values[0]
    else:
        mid = len(values) // 2
        avg_early = sum(values[:mid]) / mid
        avg_late = sum(values[mid:]) / (len(values) - mid)
        diff = avg_late - avg_early

    pct = (diff / max(values[0], 1)) * 100
    if pct > 20:
        return "↑↑" if pct > 50 else "↑"
    elif pct < -20:
        return "↓↓" if pct < -50 else "↓"
    else:
        return "→"


def coefficient_of_variation(values: list[float]) -> float:
    """Lower = more consistent delivery."""
    if len(values) < 2:
        return 0.0
    mean = sum(values) / len(values)
    if mean == 0:
        return 0.0
    variance = sum((v - mean) ** 2 for v in values) / len(values)
    return math.sqrt(variance) / mean


def analyze_agent(agent_id: str, dates: list[str]) -> dict:
    """Build full trend analysis for one agent across all dates."""
    baseline = load_snapshot(BASELINE_DATE, agent_id)
    baseline_stars = 0
    if baseline:
        m = extract_metrics(baseline)
        baseline_stars = m["stars_total"]

    pilot_dates = [d for d in dates if d >= PILOT_START]
    day_data = []

    for date in pilot_dates:
        snap = load_snapshot(date, agent_id)
        if snap is None:
            continue
        m = extract_metrics(snap)
        m["date"] = date
        m["day_num"] = pilot_dates.index(date) + 1
        m["stars_gained"] = m["stars_total"] - baseline_stars
        day_data.append(m)

    if not day_data:
        return {"agent_id": agent_id, "days": 0, "error": "no data"}

    commit_series = [d["commits_24h"] for d in day_data]
    pr_series = [d["prs_merged_24h"] for d in day_data]
    stars_gained = day_data[-1]["stars_gained"] if day_data else 0
    total_commits = sum(commit_series)
    total_prs = sum(pr_series)
    avg_commits = total_commits / len(commit_series)
    consistency = coefficient_of_variation(commit_series)

    return {
        "agent_id": agent_id,
        "days_tracked": len(day_data),
        "pilot_dates": [d["date"] for d in day_data],
        "commits_by_day": commit_series,
        "prs_by_day": pr_series,
        "stars_by_day": [d["stars_total"] for d in day_data],
        "releases_by_day": [d["releases_today"] for d in day_data],
        "total_commits": total_commits,
        "total_prs": total_prs,
        "stars_gained_since_baseline": stars_gained,
        "avg_commits_per_day": round(avg_commits, 1),
        "commit_trend": trend_arrow(commit_series),
        "pr_trend": trend_arrow(pr_series),
        "consistency_cv": round(consistency, 2),
        "consistency_label": (
            "very consistent" if consistency < 0.3
            else "consistent" if consistency < 0.6
            else "variable" if consistency < 1.0
            else "highly variable"
        ),
        "day_data": day_data,
    }


def format_table(results: list[dict]) -> str:
    lines = []
    lines.append("=" * 90)
    lines.append("Gerundium Trust Stack Pilot — Day-over-Day Trend Analysis")
    lines.append(f"Generated: (run at any time — reads available snapshots)")
    lines.append("=" * 90)
    lines.append("")

    # Sort by total commits (descending)
    results = sorted(results, key=lambda r: r.get("total_commits", 0), reverse=True)

    # Header
    lines.append(f"{'Agent':<16} {'Days':>4} {'Commits':>8} {'Trend':>6} {'PRs':>6} {'Stars+':>7} {'Avg/day':>8} {'Consistency':<16}")
    lines.append("-" * 90)

    for r in results:
        if "error" in r:
            lines.append(f"{r['agent_id']:<16} {'—':>4} (no data)")
            continue
        lines.append(
            f"{r['agent_id']:<16}"
            f" {r['days_tracked']:>4}"
            f" {r['total_commits']:>8}"
            f" {r['commit_trend']:>6}"
            f" {r['total_prs']:>6}"
            f" {r['stars_gained_since_baseline']:>+7}"
            f" {r['avg_commits_per_day']:>8.1f}"
            f"  {r['consistency_label']}"
        )

    lines.append("")
    lines.append("Day-by-day commit breakdown:")
    lines.append("-" * 90)

    # Find all pilot dates across results
    all_dates = sorted(set(
        date
        for r in results if "pilot_dates" in r
        for date in r["pilot_dates"]
    ))
    date_labels = [f"Day {i+1} ({d[5:]})" for i, d in enumerate(all_dates)]

    # Header row
    agent_col = 16
    header = f"{'Agent':<{agent_col}}" + "".join(f"{lbl:>14}" for lbl in date_labels)
    lines.append(header)
    lines.append("-" * 90)

    for r in sorted(results, key=lambda r: r.get("total_commits", 0), reverse=True):
        if "error" in r:
            continue
        date_to_commits = dict(zip(r["pilot_dates"], r["commits_by_day"]))
        row = f"{r['agent_id']:<{agent_col}}"
        for date in all_dates:
            val = date_to_commits.get(date)
            if val is not None:
                row += f"{val:>14}"
            else:
                row += f"{'—':>14}"
        lines.append(row)

    lines.append("")
    lines.append("Stars gained since baseline (2026-02-18):")
    lines.append("-" * 90)

    for r in sorted(results, key=lambda r: r.get("stars_gained_since_baseline", 0), reverse=True):
        if "error" in r:
            continue
        stars = r.get("stars_gained_since_baseline", 0)
        bar_len = min(int(stars / 5), 40)
        bar = "█" * bar_len
        lines.append(f"  {r['agent_id']:<14} {stars:>+6}  {bar}")

    lines.append("")
    lines.append("Consistency (coefficient of variation on commit series):")
    lines.append("  Lower = more predictable daily delivery | Higher = burst pattern")
    lines.append("-" * 90)
    for r in sorted(results, key=lambda r: r.get("consistency_cv", 999)):
        if "error" in r:
            continue
        lines.append(f"  {r['agent_id']:<14}  CV={r['consistency_cv']:.2f}  ({r['consistency_label']})")

    lines.append("")
    lines.append(f"Total agents tracked: {len([r for r in results if 'error' not in r])}")
    lines.append(f"Pilot dates with data: {', '.join(all_dates)}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Pilot trend analysis")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of table")
    parser.add_argument("--agent", help="Analyze only this agent ID")
    args = parser.parse_args()

    dates = get_pilot_dates()
    if not dates:
        print("No snapshot dates found.", file=sys.stderr)
        sys.exit(1)

    agents = get_all_agents(dates)
    if args.agent:
        agents = [args.agent] if args.agent in agents else []

    results = [analyze_agent(agent_id, dates) for agent_id in agents]

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print(format_table(results))


if __name__ == "__main__":
    main()
