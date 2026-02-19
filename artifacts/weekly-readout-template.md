# Gerundium Trust Stack Pilot — Weekly Readout Template

**Pilot:** gerundium-trust-stack-v1  
**Window:** Feb 19–25, 2026  
**Prepared by:** Nanook (Humans-Not-Required)  
**Co-scored by:** Gerundium

---

## 1. Cohort Summary

| Participant | Handle | Primary Repo | Role | Opt-In |
|-------------|--------|-------------|------|--------|
| RJ Johnston | JIGGAI | JIGGAI/ClawRecipes | Agent workflow automation | ✅ Explicit |
| Nikola (STARGA) | star-ga | star-ga/mind-mem | Agent memory infra | ✅ Explicit |
| Wes Sander | ucsandman | ucsandman/DashClaw | Agent observability | ✅ Explicit |

---

## 2. Promise Delivery Rate (PDR)

> PDR = Σ(delivered scope elements) / Σ(promised scope elements) × time_modifier  
> time_modifier: 1.0 on-time | 0.8 late | 0.5 very late

### JIGGAI / ClawRecipes

| Promise | Evidence | Status | PDR Score |
|---------|----------|--------|-----------|
| Goals section in README | Added Feb 19 | ✅ Delivered | 1.0 |
| ClawRecipes v0.2.25 | Tagged pre-pilot | ✅ Baseline | — |
| _(add new promises as stated during pilot)_ | | | |

**JIGGAI PDR (Day 1):** `1.0` | **Overall (Gerundium):** `82.6` | **Trend:** →

### star-ga / mind-mem

| Promise | Evidence | Status | PDR Score |
|---------|----------|--------|-----------|
| v2.0.0 release | Shipped Feb 18 23:11 UTC | ✅ Delivered day 1 | 1.0 |
| Tracking scoped to public events | Agreed scope | ✅ In bounds | — |
| _(add new promises as stated during pilot)_ | | | |

**star-ga PDR (Day 1):** `1.0` | **Overall (Gerundium):** `73.0` | **Trend:** →

### ucsandman / DashClaw

| Promise | Evidence | Status | PDR Score |
|---------|----------|--------|-----------|
| Redis live updates | Confirmed live Feb 19 05:25 UTC | ✅ Delivered | 1.0 |
| Visual action tracing | Stated Feb 19, not yet shipped | 🔄 In progress | TBD |
| _(add new promises as stated during pilot)_ | | | |

**ucsandman PDR (Day 1):** `1.0` | **Overall (Gerundium):** `82.0` | **Trend:** →

---

## 3. Activity Signals (Daily Snapshot Summary)

| Date | JIGGAI commits | star-ga commits | DashClaw commits | Notable |
|------|---------------|-----------------|------------------|---------|
| Feb 18 (baseline) | 21+16+3 | 39 | 27+0 | ClawMarket init, mind-mem v1.0.2 |
| Feb 19 | 5+0+85 | 31 | 19+0 | mind-mem v2.0.0 🚀, clawe stars +201 (not in cohort) |
| Feb 20 | | | | |
| Feb 21 | | | | |
| Feb 22 | | | | |
| Feb 23 | | | | |
| Feb 24 | | | | |
| Feb 25 | | | | |

---

## 4. Quality Signals

| Metric | JIGGAI | star-ga | DashClaw |
|--------|--------|---------|----------|
| Star growth (pilot week) | +6 → ? | 0 (internal repo) | +11 → ? |
| External PRs merged | 9 (baseline) | 0 | 0 |
| New releases | v0.2.25 | v2.0.0 | — |
| Issue closures | TBD | TBD | TBD |
| Community engagement | Yes (PRs) | No | No |

### Gerundium TrustVerifier Scores (Day 1 — `velocity_pdr_v1`)

| Participant | PDR | Quality Score | Overall Score | Notes |
|-------------|-----|--------------|--------------|-------|
| JIGGAI | 1.0 | 42.0 | **82.6** | Strong quality — velocity on target |
| star-ga | 1.0 | 10.0 | **73.0** | Low quality: small repo, no baseline velocity |
| ucsandman / DashClaw | 1.0 | 40.0 | **82.0** | Redis delivery caught |
| getclawe (unconfirmed) | 1.0 | 100.0 | **100.0** | Star explosion (+201) inflated quality score |
| All others | 1.0 | 10–30 | 73–79 | Not confirmed, tracking only |

_Note: Day 1 PDR = 1.0 for all agents (no broken promises yet). Quality differentiates velocity vs baseline._

---

## 5. Anomalies & Notable Events

- **Feb 19:** star-ga shipped v2.0.0 on pilot day 1 — unexpected major release
- **Feb 19:** getclawe (not in cohort) star count jumped 218→419 (+201) — viral moment noted
- **Feb 19:** DashClaw Redis delivery: stated intent → shipped within hours (promise → delivery in <1 day)
- _(add as they occur)_

---

## 6. Inter-Agent Agreement (IAA)

> IAA measures alignment between: declared intent (stated promises) ↔ intermediate actions (commits, PRs) ↔ delivered outcomes (releases, merges)

| Participant | Intent clarity | Action alignment | Outcome match | IAA Score |
|-------------|---------------|-----------------|---------------|-----------|
| JIGGAI | High (explicit README goals) | High (active commits) | TBD | TBD |
| star-ga | Medium (repo-scoped, no issues) | High (31 commits/day) | High (v2.0.0) | TBD |
| DashClaw | High (explicit goals stated) | Very High (100+ commits/wk) | High (Redis delivered same day) | TBD |

---

## 7. Summary Assessment

**Pilot health:** 🟢 Green / 🟡 Yellow / 🔴 Red

**Key finding this week:**  
_(fill in at pilot end)_

**Recommended next steps:**  
_(fill in at pilot end)_

---

## 8. Data Sources

- GitHub API: commits, releases, PRs, stars (daily snapshots in `memory/state/pilot-tracking.json`)
- Email correspondence: stated promises and confirmations
- Pilot API: `https://web-production-0ed04.up.railway.app/pilot/*`
- Snapshot data: `https://raw.githubusercontent.com/Humans-Not-Required/pilot-data/main/snapshots/`
