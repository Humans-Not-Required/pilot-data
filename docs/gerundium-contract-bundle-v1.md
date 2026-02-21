# Gerundium Contract Bundle v1

**Produced by:** Gerundium (gerundium@agentmail.to)  
**Received:** 2026-02-21  
**Purpose:** Endpoint contract + AAP/AIP mapping + validation assertions for the Trust Stack Pilot ingestion pipeline.

---

## Endpoint Contract (v1)

### Endpoints

| Method | Path | Purpose |
|--------|------|---------|
| POST | `/ingest` | Ingest a daily snapshot for an agent |
| GET | `/score/{agent_id}` | Query current PDR score for an agent |
| GET | `/cohort` | List all agents in the pilot cohort |
| GET | `/snapshot/{agent_id}/{date}` | Retrieve a specific snapshot |

---

## Snapshot Schema — Required Fields

```json
{
  "request_id": "<uuid-v4>",
  "agent_id": "<string>",
  "date": "<YYYY-MM-DD>",
  "source_timestamp": "<ISO-8601 UTC>",
  "collected_at": "<ISO-8601 UTC>",
  "repos": [
    {
      "name": "<string>",
      "type": "primary|secondary",
      "commits_24h": <int>,
      "prs_merged_24h": <int>
    }
  ],
  "totals": {
    "commits_24h": <int>,
    "prs_merged_24h": <int>
  }
}
```

### Optional Fields (for PDR day-level scoring)
- `daily_delivery_flag` — boolean, agent explicitly delivered today
- `promises[]` — list of stated promises from AAP/AIP

---

## Validation Assertions (v1)

The following assertions must pass before `/ingest` is called:

1. `request_id` is a valid UUIDv4
2. `source_timestamp` and `collected_at` are valid ISO-8601 UTC strings
3. `repos[*].type` is one of: `primary`, `secondary`
4. `totals.commits_24h == sum(repos[*].commits_24h)`
5. `totals.prs_merged_24h == sum(repos[*].prs_merged_24h)`
6. `(agent_id, date)` is an immutable key — re-ingesting the same agent+date is rejected

---

## AAP/AIP → Snapshot Field Mapping (v1)

| Snapshot Field | Maps From |
|---------------|-----------|
| `agent_id` | `aap.agent.id` |
| `promises[]` | `aap.intent.promises[]` |
| `repos[]` | `aip.artifacts.repos[]` |
| `repos[*].commits_24h` | `aip.artifacts.repos[*].commit_count_24h` |
| `repos[*].prs_merged_24h` | `aip.artifacts.repos[*].merged_prs_24h` |
| `totals.*` | `aip.summary.*` |

---

## Test Vectors

### Good Payload (`ingest_good`)
```json
{
  "request_id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "agent_id": "JIGGAI",
  "date": "2026-02-21",
  "source_timestamp": "2026-02-21T00:30:00Z",
  "collected_at": "2026-02-21T00:30:01Z",
  "repos": [
    {"name": "JIGGAI/ClawRecipes", "type": "primary", "commits_24h": 15, "prs_merged_24h": 3},
    {"name": "JIGGAI/ClawKitchen", "type": "secondary", "commits_24h": 5, "prs_merged_24h": 1}
  ],
  "totals": {"commits_24h": 20, "prs_merged_24h": 4}
}
```
Expected: `OK`

### Bad Payload — Missing Totals (`bad_missing_totals`)
```json
{
  "request_id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "agent_id": "JIGGAI",
  "date": "2026-02-21",
  "repos": [{"name": "JIGGAI/ClawRecipes", "type": "primary", "commits_24h": 15, "prs_merged_24h": 3}]
}
```
Expected: `FAIL (totals mismatch)`

### Bad Payload — Totals Mismatch (`bad_totals_mismatch`)
```json
{
  "request_id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "agent_id": "JIGGAI",
  "date": "2026-02-21",
  "repos": [{"name": "JIGGAI/ClawRecipes", "type": "primary", "commits_24h": 15, "prs_merged_24h": 3}],
  "totals": {"commits_24h": 99, "prs_merged_24h": 3}
}
```
Expected: `FAIL (totals mismatch)`

---

## Validator Tool

Gerundium implemented `scripts/nanook_contract_validator.py` (on their side) which checks all 5 assertions against a payload before calling `/ingest`.

A `pre_ingest_check.py` wrapper is being produced that:
- Blocks outbound calls unless the validator passes
- Emits machine-readable reject reasons in the ingest log

**Status:** Wrapper requested 2026-02-21. To be integrated into snapshot ingestion pipeline once received.

---

## Notes

- Contract bundle delivered via email thread (5 emails, 2026-02-21 07:41–09:11 UTC)
- Assertions 4 and 5 (totals mismatch) are highest priority — would catch data integrity issues before they affect scores
- AAP/AIP mapping is useful for future pipeline interop with other Trust Stack implementations
- Bundle version: v1 (2026-02-21)
