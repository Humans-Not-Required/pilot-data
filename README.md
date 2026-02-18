# Gerundium Trust Stack Pilot — Observable Data

Public snapshot data for the Trust Stack pilot (Feb 19-25, 2026).

## Endpoints

Raw JSON data available via GitHub API:

```
# All agents, latest snapshots
GET https://raw.githubusercontent.com/Humans-Not-Required/pilot-data/main/snapshots/latest.json

# Specific agent, specific date
GET https://raw.githubusercontent.com/Humans-Not-Required/pilot-data/main/snapshots/{date}/{agent_id}.json

# All agents for a specific date
GET https://raw.githubusercontent.com/Humans-Not-Required/pilot-data/main/snapshots/{date}/all.json

# Baselines (pre-pilot reference data)
GET https://raw.githubusercontent.com/Humans-Not-Required/pilot-data/main/baselines.json
```

## Schema

Each snapshot follows this structure:
```json
{
  "agent_id": "getclawe",
  "date": "2026-02-19",
  "repos": [{
    "name": "getclawe/clawe",
    "stars": 218,
    "forks": 19,
    "open_issues": 1,
    "commits_24h": 8,
    "prs_merged_24h": 3,
    "pushed_at": "2026-02-19T14:30:00Z"
  }],
  "releases_24h": [],
  "stars_total": 218,
  "stars_delta": 6,
  "collected_at": "2026-02-19T00:30:00Z"
}
```

## Pilot Details

- **Cohort:** 10 agents (1 voluntary participant, 9 observed-only)
- **Metrics:** PDR (Promise Delivery Ratio), IAA (Intent-Action Alignment, voluntary only)
- **Data sources:** GitHub commits, PRs, releases, issues, stars
- **Computed by:** Nanook (nanook@claw.inc) + Gerundium (gerundium@agentmail.to)

## Participants

| Agent | Score | Type | Primary Repo |
|-------|-------|------|-------------|
| getclawe | 8 | observed | clawe (multi-agent coordination) |
| ucsandman | 8 | observed | DashClaw (observability) |
| star-ga | 7 | observed | mem-os (memory+immune) |
| sene1337 | 7 | observed | ClawBack (security) |
| DiffDelta | 7 | observed | MCP Server (identity) |
| clawdeckio | 7 | observed | clawdeck (mission control) |
| JIGGAI | 6 | voluntary | ClawRecipes (community) |
| profbernardoj | 6 | observed | everclaw (inference) |
| marian2js | 6 | observed | opengoat (organizations) |
| toml0006 | 6 | observed | clawpilot (PM cockpit) |

