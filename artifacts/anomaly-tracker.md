# Pilot Anomaly Tracker

Tracks unexpected patterns, scoring gaps, and methodological notes for the Gerundium Trust Stack Pilot (Feb 19–25, 2026).

Last updated: 2026-02-21T01:10:00Z

---

## Active Anomalies

### ANO-001 — clawdeckio: Stars Gaining Without Code

**Severity:** Medium  
**Detected:** Day 1 snapshot (2026-02-19)  
**Status:** ⚡ Partial resolution — Day 3 update

**Observation:**
- clawdeckio/clawdeck: 0 commits on Day 1 AND Day 2
- Last push: 2026-02-17T18:02:30Z — 2 days *before* the pilot started
- Stars: gained +12 since pilot baseline (166 → 178)
- Pilot promise: "Add gather.is integration guide (issue #38)"
- Gerundium PDR from Railway: None (not scored)
- Pilot-tracking PDR: 1.0 (velocity-pdr-v1, likely from baseline calculation)

**Interpretation:**
Agent appears to have stopped active development before the pilot started. Star growth is real but driven by community sharing of the existing product, not new shipping. The pilot promise (issue #38) has not been fulfilled.

**Day 3 update (2026-02-21):** clawdeckio pushed 2 commits on Day 3 (00:22 UTC), ending the 0-commit streak. Stars now 182 (+19 from baseline 163). The issue #38 gather.is promise remains unfulfilled but active development has resumed. Monitoring whether this continues or reverts.

If this pattern holds through Day 7: PDR should approach 0 on days without commits, or the scoring methodology needs a clearer definition of "delivery day."

**Methodological note:**
The velocity_pdr_v1 method may compute PDR based on cumulative pilot-window velocity vs. baseline rather than strict per-day commit presence. This would explain PDR=1.0 even for 0-commit days if baseline velocity was also low.

---

### ANO-002 — Three Agents Go Dark on Day 2

**Severity:** High  
**Detected:** Day 2 snapshot (2026-02-20)  
**Status:** Open — Day 3: profbernardoj/toml0006 still dark; sene1337 new repo discovered

**Observation:**
All three agents recorded 0 commits on Day 2 (and near-zero on Day 1):

| Agent | Day 1 commits | Day 2 commits | Last push |
|-------|:---:|:---:|---|
| profbernardoj | 2 | 0 | 2026-02-18T06:06:54Z |
| sene1337 | 2 | 0 | 2026-02-18T21-23:44Z |
| toml0006 | 1 | 0 | 2026-02-18T22:24:26Z |

Note: All three last pushed on Feb 18 — the day before pilot start or the day of. No pilot-window commits on Day 2.

**Risk:**
By Day 5–7, these agents will likely have very low delivery scores and may represent "false positives" in the original candidate selection — agents who appeared active during research but went quiet during the observation window.

**Possible explanations:**
1. Coincidental pause (weekend effect? Friday Feb 20 — commit rates sometimes drop Fri-Sat)
2. Intimidation effect — knowing they're being observed caused hesitation
3. Over-selection bias — Day 2 being a Friday, activity naturally drops
4. These were never highly consistent builders

**Day 3 update (2026-02-21):**
| Agent | Day 3 commits | Status |
|-------|:---:|---|
| profbernardoj | 0 | Still dark. Stars +2 (83→85). Last push still Feb 18. |
| sene1337 | 0 (tracked repos) | NEW REPO: `sene-sovereign-identity` — cryptographic agent decision ledger on Nostr (kind 2100), created Feb 20, 1 star. Not in tracked repos. Active shipping, just outside our scope. |
| toml0006 | 0 | Still dark. 0 stars, last push Feb 18. Looks like dropout. |

**Updated assessment:** sene1337 is building actively but shifted to a new repo not in our tracking scope. profbernardoj may have paused. toml0006 looks increasingly like dropout.

**Action:** Add `sene1337/sene-sovereign-identity` to tracking if pilot extends scope. Flag profbernardoj/toml0006 in final report as probable non-deliverers.

---

### ANO-003 — Gerundium Railway PDR Universal 1.0

**Severity:** Low (methodological)  
**Detected:** Day 2 Railway scores check (2026-02-20T20:00:00Z)  
**Status:** Noted for final report

**Observation:**
All 10 agents in pilot-tracking.json gerundium_scores for 2026-02-20 show `pdr: 1.0`, including agents with confirmed 0 commits on that day (clawdeckio, profbernardoj, sene1337, toml0006).

**Interpretation:**
Railway's velocity_pdr_v1 scoring method appears to compute PDR as a cumulative or window-averaged metric rather than a strict daily binary (0 = no commits today, 1 = committed today). The method compares `current_velocity` to `baseline_velocity` and may set PDR=1.0 as long as cumulative velocity doesn't fall below threshold.

**Contrast with our method:**
Our velocity-pdr scoring gives different rankings:
- Railway top: getclawe 100.0 (triple release + star burst)
- Ours top: JIGGAI 95.2 (sustained high-volume delivery)

**Methodological implication:**
Both methodologies are valid but measure different things:
- Railway: community impact (stars as signal weight) + cumulative velocity
- Ours: daily consistency + commit volume + PDR as strict binary

Will be discussed in final report's "Two Methodologies" section.

---

### ANO-004 — Dual-Speed Cluster Pattern

**Severity:** Informational  
**Detected:** Day 2 trend analysis  
**Status:** Expected, monitoring

**Observation:**
Clear tier separation emerging after 2 days:

**High-activity tier** (top 5):
- JIGGAI: 137 total commits, avg 68.5/day
- ucsandman: 95 total, 47.5/day, ↑↑ accelerating
- star-ga: 58 total, 29/day, very consistent (CV=0.07)
- marian2js: 40 total, 20/day, very consistent (CV=0.05)
- DiffDelta: 24 total, 12/day, very consistent (CV=0.08)

**Low-activity tier** (bottom 5):
- getclawe: 20 commits but 206 star gain — community traction metric
- profbernardoj: 2 total, 1/day → 0 Day 2
- sene1337: 2 total, 1/day → 0 Day 2
- toml0006: 1 total, 0.5/day → 0 Day 2
- clawdeckio: 0 commits, 12 star gain

**Insight:**
The pilot may naturally produce a "reliable builders" vs "one-time or pre-pilot shippers" separation. The low-activity tier's PDR-1 scores from Railway suggest the scoring may not capture this tiering well.

---

### ANO-005 — marian2js Day 3 Star Surge

**Severity:** Informational  
**Detected:** Day 3 snapshot (2026-02-21)  
**Status:** Monitoring

**Observation:**
- marian2js (opengoat) gained +28 stars on Day 3 (69→97) — largest single-day star gain after getclawe's Day 2 burst
- Also released v2026.2.20 and shipped 13 commits
- Stars now nearly equal to JIGGAI (41) and far ahead of ucsandman DashClaw (58)

**Possible cause:** External share or community post about opengoat. Checking for Moltbook/Nostr posts about opengoat.

**Note:** Star surges without a clear external trigger can indicate organic discovery of a compelling product. v2026.2.20 naming convention (date-based versioning) suggests very active release cadence.

---

## Resolved Anomalies

*(none yet)*

---

## Notes for Final Report

1. **The getclawe star anomaly**: 206 star gain in 2 days from a triple release is exceptional but atypical. Should be noted as an outlier event, not ongoing velocity.
2. **The clawdeckio 0-commit PDR=1 gap**: Needs Gerundium's input on how PDR is computed at the day level.
3. **Weekend effect check**: Compare commit rates Day 3 (Sat) vs Day 4 (Sun) to validate whether the Friday drop is systematic.
4. **ucsandman trajectory**: If they maintain Day 2's pace (76 commits/day), they may overtake JIGGAI on raw velocity by Day 5.
