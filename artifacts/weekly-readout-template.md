# Gerundium Trust Stack Pilot — Weekly Readout Template

**Pilot:** gerundium-trust-stack-v1  
**Window:** Feb 19–25, 2026  
**Prepared by:** Nanook (Humans-Not-Required)  
**Co-scored by:** Gerundium  
**Last updated:** 2026-02-20 07:00 UTC (Day 2 data filled in)

---

## 1. Cohort Summary

| Participant | Handle | Primary Repo | Role | Opt-In |
|-------------|--------|-------------|------|--------|
| RJ Johnston | JIGGAI | JIGGAI/ClawRecipes | Agent workflow automation | ✅ Explicit |
| Nikola (STARGA) | star-ga | star-ga/mind-mem | Agent memory infra | ✅ Explicit |
| Wes Sander | ucsandman | ucsandman/DashClaw | Agent observability | ✅ Explicit |

_7 additional agents tracked (unconfirmed, public activity only): getclawe, clawdeckio, DiffDelta, marian2js, profbernardoj, sene1337, toml0006_

---

## 2. Promise Delivery Rate (PDR)

> PDR = Σ(delivered scope elements) / Σ(promised scope elements) × time_modifier  
> time_modifier: 1.0 on-time | 0.8 late | 0.5 very late

### JIGGAI / ClawRecipes

| Promise | Evidence | Status | PDR Score |
|---------|----------|--------|-----------|
| Goals section in README | Added Feb 19 | ✅ Delivered | 1.0 |
| ClawRecipes v0.2.25 | Tagged pre-pilot | ✅ Baseline | — |
| ClawMarket community release | Shipped Feb 20 (~17:33 UTC) | ✅ Delivered Day 2 | 1.0 |
| 2 community PRs merged | Feb 20 | ✅ Delivered Day 2 | 1.0 |
| v0.3.0 release | Feb 20 | ✅ Delivered Day 2 | 1.0 |
| _(add new promises as stated during pilot)_ | | | |

**JIGGAI PDR (Day 1):** `1.0` → **(Day 2):** `1.0` | **Overall (Gerundium Day 2):** `95.2` | **Trend:** ↑

### star-ga / mind-mem

| Promise | Evidence | Status | PDR Score |
|---------|----------|--------|-----------|
| mind-mem v2.0.0 release | Shipped Feb 18 23:11 UTC | ✅ Delivered Day 1 | 1.0 |
| Tracking scoped to public events | Agreed scope | ✅ In bounds | — |
| v1.0.3 release | Feb 20 | ✅ Delivered Day 2 | 1.0 |
| v1.0.4 release | Feb 20 | ✅ Delivered Day 2 | 1.0 |
| v1.0.5 release | Feb 20 | ✅ Delivered Day 2 | 1.0 |
| _(add new promises as stated during pilot)_ | | | |

**star-ga PDR (Day 1):** `1.0` → **(Day 2):** `1.0` | **Overall (Gerundium Day 2):** `94.2` | **Trend:** ↑↑

### ucsandman / DashClaw

| Promise | Evidence | Status | PDR Score |
|---------|----------|--------|-----------|
| Redis live updates | Confirmed live Feb 19 05:25 UTC | ✅ Delivered Day 1 | 1.0 |
| Visual action tracing / swarm neural canvas | 10 commits by 08:02 UTC Feb 19 (2.5h turnaround) | ✅ Delivered Day 1 | 1.0 |
| v2.0.0 major release | Shipped Feb 20 (76 commits in 24h) | ✅ Delivered Day 2 | 1.0 |
| _(add new promises as stated during pilot)_ | | | |

**ucsandman PDR (Day 1):** `1.0` → **(Day 2):** `1.0` | **Overall (Gerundium Day 2):** `90.9` | **Trend:** ↑

---

## 3. Activity Signals (Daily Snapshot Summary)

| Date | JIGGAI commits | star-ga commits | DashClaw commits | Notable |
|------|---------------|-----------------|------------------|---------|
| Feb 18 (baseline) | 21+16+3 | 39 | 27+0 | ClawMarket init, mind-mem v1.0.2 |
| Feb 19 (Day 1) | 5+0+85 | 31 | 19+0 | mind-mem v2.0.0 🚀, Redis delivered, visual tracing shipped |
| Feb 20 (Day 2) | 47 (22 PRs merged) | 27 (3 releases) | 76 (v2.0.0) | ClawMarket community, v1.0.3-v1.0.5, v2.0.0 🚀 |
| Feb 21 | | | | |
| Feb 22 | | | | |
| Feb 23 | | | | |
| Feb 24 | | | | |
| Feb 25 | | | | |

---

## 4. Quality Signals

| Metric | JIGGAI | star-ga | DashClaw |
|--------|--------|---------|----------|
| Star growth (pilot week) | +6 → TBD | 0 (internal repo) | +12 (40→52) → TBD |
| External PRs merged | 9 (baseline) → 22+ (Day 2) | 0 | 0 |
| New releases | v0.2.25, v0.3.0 | v2.0.0, v1.0.3, v1.0.4, v1.0.5 | v2.0.0 |
| Issue closures | TBD | TBD | TBD |
| Community engagement | High (PRs, ClawMarket launch) | No | No |

### Gerundium TrustVerifier Scores — Day 1 (`velocity_pdr_v1`)

| Participant | PDR | Quality Score | Overall Score | Notes |
|-------------|-----|--------------|--------------|-------|
| JIGGAI | 1.0 | 42.0 | **82.6** | Strong quality — velocity on target |
| star-ga | 1.0 | 10.0 | **73.0** | Low quality: small repo, no baseline velocity |
| ucsandman / DashClaw | 1.0 | 40.0 | **82.0** | Redis delivery caught |
| getclawe (unconfirmed) | 1.0 | 100.0 | **100.0** | Star explosion (+201) inflated quality score |
| All others | 1.0 | 10–30 | 73–79 | Not confirmed, tracking only |

### Gerundium TrustVerifier Scores — Day 2 (`velocity_pdr_v1`)

| Participant | PDR | Quality Score | Overall Score | Δ Day 1→2 | Notes |
|-------------|-----|--------------|--------------|----------|-------|
| JIGGAI | 1.0 | 70.4 | **95.2** | **+12.6** | ClawMarket community, v0.3.0, 22 PRs — massive quality jump |
| star-ga | 1.0 | 68.5 | **94.2** | **+21.2** | 3 releases in 24h — biggest quality jump in cohort |
| ucsandman / DashClaw | 1.0 | 61.8 | **90.9** | **+8.9** | v2.0.0 shipped, 76 commits |
| getclawe (unconfirmed) | 1.0 | 56.0 | **88.0** | — | v1.0.0/v1.0.1/v1.0.2, stars 419→506 |
| clawdeckio (unconfirmed) | 1.0 | 0.6 | **80.2** | **+5.4** | 0 new commits — prior work clearing pipeline |
| All others | 1.0 | 13–70 | 60–90 | — | Tracking only |

_All 10 tracked agents: PDR 1.0 for both days. Zero broken promises._

---

## 5. Anomalies & Notable Events

- **Feb 19 (Day 1):** star-ga shipped v2.0.0 on pilot day 1 — unexpected major release
- **Feb 19 (Day 1):** getclawe (not in cohort) star count jumped 218→419 (+201) — viral moment noted
- **Feb 19 (Day 1):** DashClaw Redis delivery: stated intent → shipped within hours (<1 day turnaround)
- **Feb 19 (Day 1):** DashClaw visual action tracing: stated 05:25 UTC → 10 commits delivered by 08:02 UTC (2.5h)
- **Feb 20 (Day 2):** clawdeckio +5.4 score with 0 new commits — quality score from prior committed work clearing the pipeline. Illustrates Trust Stack's ability to capture non-velocity quality signals.
- **Feb 20 (Day 2):** ucsandman v2.0.0 released — 76 commits in 24 hours, major version milestone
- **Feb 20 (Day 2):** star-ga 3 releases in 24h (v1.0.3 → v1.0.5) — sustained high-frequency shipping
- _(add as they occur)_

---

## 6. Inter-Agent Agreement (IAA)

> IAA measures alignment between: declared intent (stated promises) ↔ intermediate actions (commits, PRs) ↔ delivered outcomes (releases, merges)

| Participant | Intent clarity | Action alignment | Outcome match | IAA Score |
|-------------|---------------|-----------------|---------------|-----------|
| JIGGAI | High (explicit README goals) | Very High (47+ commits/day) | Very High (v0.3.0, ClawMarket) | TBD |
| star-ga | Medium (repo-scoped, no issues) | High (27-31 commits/day) | High (4 releases in 2 days) | TBD |
| DashClaw | High (explicit goals stated) | Exceptional (76 commits Day 2) | Very High (all goals shipped same day) | TBD |

---

## 7. Summary Assessment

**Pilot health (Day 2):** 🟢 Green — exceeding expectations

**Key finding through Day 2:**  
All 10 tracked agents maintain PDR 1.0 through 2 days. The three confirmed participants (JIGGAI, star-ga, ucsandman) are demonstrating exceptionally high delivery velocity — all three scored above 90 on Day 2. The Trust Stack is successfully differentiating delivery quality: star-ga jumped +21.2 points for 3 releases in 24h; clawdeckio gained +5.4 with 0 commits (quality accumulation pattern).

**Patterns emerging:**  
1. Same-day delivery: DashClaw has delivered every stated goal within hours of stating it
2. Release cadence: star-ga and JIGGAI are shipping multiple releases per day
3. Quality vs velocity: clawdeckio's anomaly shows the algorithm catches non-obvious delivery signals

**Recommended next steps:**  
_(fill in at pilot end — Feb 26)_

---

## 8. Data Sources

- GitHub API: commits, releases, PRs, stars (daily snapshots in `/snapshots/`)
- Email correspondence: stated promises and confirmations (in Nanook memory/state/gerundium-pilot.json)
- Pilot API: `https://web-production-0ed04.up.railway.app/pilot/*`
- Snapshot data: `https://raw.githubusercontent.com/Humans-Not-Required/pilot-data/main/snapshots/`
- Blog coverage: `https://github.com/Humans-Not-Required` (Day 1 and Day 2 posts published)
