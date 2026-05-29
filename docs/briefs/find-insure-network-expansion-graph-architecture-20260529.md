# FIND_INSURE — Network-Expansion Relationship Graph (NERG) Architecture

**Author:** 1.0.0_SA_CTO
**Date:** 2026-05-29
**Directive:** Andrew sovereign 2026-05-29 — multi-hop warm-path graph rooted at the IR team's LinkedIn connections, expanded via shared-employer-with-time-overlap, insurance-relevance-scanned, to surface targetable people we have a warm path to.
**Status:** ARCHITECTURE BRIEF v1.0 — design for review; hop-0 is buildable now, hop-1+ gated on the dependency in §6.
**Companion to:** `find-insure-person-enrichment-pipeline-canonical-20260529.md` (the enrichment substrate this rides on; `linkedin_slug` PK shared).

---

## 1. The process (Andrew's description, formalized)

A relevance-gated **breadth-first traversal** of the professional-relationship graph, rooted at the IR team's 1st-degree connections, expanding through shared-employer edges where tenures overlap:

```
HOP 0  IR team  --CONNECTED_TO-->  their 1st-degree connections        [free: CSV export]
         └─ insurance-scan hop-0 profiles → EASY WINS (warm + already in insurance)
HOP 1  connection  --EMPLOYED_AT-->  companies they worked at
         └─ at each company, find COLLEAGUES whose tenure OVERLAPS the connection's
            (real "they knew each other" edge, not just "both worked there")
HOP 2  those colleagues  --EMPLOYED_AT-->  where ELSE they work(ed)
         └─ pull those companies' org charts → expand the frontier
         (more complex/vast — aggressive pruning required)
```

The output is a **warm-path map**: for each surfaced insurance/AM person, the explainable chain back to an IR team member (IR-member → connection → shared-firm-with-overlap → colleague → …), scored by relevance × path-strength.

## 2. Why time-overlap is the load-bearing edge

"Worked at Company X" is a weak signal (thousands of people). "Worked at Company X **while our connection was there**" is a *relationship* — they plausibly knew each other, which is what makes a warm intro real. **COLLEAGUE_OF is defined only on tenure-interval intersection**, not co-employment-ever. This is the single most important precision lever in the whole design — without it, hop-1 explodes into noise.

## 3. Graph model (extends the canonical people/ store)

**Nodes:**
- `Person` — PK `linkedin_slug`. Attrs: name, current title/company, FINRA reg (brokercheck_client), insurance_relevance_score, source provenance.
- `Company` — PK `company_key` (domain ∥ Lusha company_id ∥ slug). Attrs: SEC AUM (secadv_client), AUM-band-fit, FINRA/SEC registration, IMO-universe-membership.

**Edges (typed, directional where it matters):**
- `CONNECTED_TO` (IR_member → Person) — from CSV. Attrs: connected_on date. **Hop-0 seed.**
- `EMPLOYED_AT` (Person → Company) — from Bright Data `experience` ∥ Lusha. Attrs: start_date, end_date, title. **The interval that powers overlap.**
- `COLLEAGUE_OF` (Person ↔ Person) — DERIVED. Exists iff ∃ Company where both have EMPLOYED_AT with **intersecting [start,end] intervals**. Attrs: company, overlap_months, both titles.

**Store:** `people/{slug}/` (existing) + `graph/edges/{type}/…` + `graph/companies/{key}.json`. Edge-list + adjacency, keyed for dedup. A node is visited once; re-encounter adds a path, never re-pulls.

## 4. Staged pipeline

### Stage 0 — Seed + insurance-scan (CHEAP, ship first)
1. Ingest each IR member's connections CSV → `Person` nodes + `CONNECTED_TO` edges (name, profile URL=`linkedin_slug`, company, position, connected_on).
2. **FREE insurance scan first:** regex the CSV `Company` + `Position` text for insurance/annuity/IMO/wealth/AM terms. Flag hits.
3. **EASY-WIN output:** IR-member ↔ connection-already-in-insurance. No further hops needed for these — they're directly warm + relevant. (This is the immediate-value slice; it needs nothing but the CSVs.)
4. (Optional) Bright Data scrape the flagged (or all) hop-0 connections for richer `about`/profile insurance signal + to seed their `EMPLOYED_AT` history for hop-1.

### Stage 1 — Colleague expansion (GATED)
For each hop-0 connection passing the frontier gate (§5):
1. Bright Data scrape → `EMPLOYED_AT` intervals (work history). **[hard dep: §6]**
2. For each company in history → Lusha org-chart prospect → company roster (people + their tenures).
3. Compute `COLLEAGUE_OF`: roster members whose tenure intersects the connection's tenure at that company.
4. **Prune before persisting:** keep a colleague only if it passes insurance/AM relevance AND its current company passes the AUM-band filter (secadv). Drop the rest (logged, not silently).

### Stage 2 — Secondary expansion (HEAVILY GATED)
For surviving hop-1 colleagues:
1. Where else did they work (their `EMPLOYED_AT`) → pull those companies' org charts.
2. Same overlap + relevance + dedup pruning, **threshold raised** (relevance decay per hop).
3. Hop cap default = 2 (configurable; 3+ is research-only).

### Stage 3 — Score + path
- Each surfaced Person: `relevance_score` (insurance/AM title + FINRA series reg + firm AUM-band-fit + IMO-universe membership) × `path_strength` (decays per hop; boosted by overlap_months + connection recency).
- Emit `graph/warm_paths/{target_slug}.json`: the ranked target + its explainable path chain back to the IR member.

## 5. Combinatorial control — THE make-or-break

Hop-2 is potentially millions of nodes. Every expansion is relevance-gated or it blows up:

- **Frontier gate:** a node expands only if `relevance_score ≥ hop_threshold`. Threshold **rises each hop** (hop-1 permissive, hop-2 strict) — relevance-decay.
- **Dedup graph store:** a `linkedin_slug` / `company_key` is expanded once. Re-encounter = add a path edge, never re-pull. (Hard requirement — without it, cycles re-pull forever.)
- **Budget gate:** per-hop ceilings on Lusha credits + Bright Data scrapes. When exhausted, STOP and **log exactly what was dropped** (no silent truncation — a frontier cut must be visible, per the no-silent-caps discipline).
- **Hop cap:** default 2.
- **Company-fanout cap:** an org-chart pull is capped (top-N by seniority) and skipped entirely for out-of-band giants (a $104B firm's roster is noise for a $6-10B-target search).

Without §5, this is a money-incinerator. With it, it's a focused warm-path finder.

## 6. The hard dependency — `experience` / work-history

Hops 1–2 are **entirely dependent on per-person work history with tenure dates** (the EMPLOYED_AT intervals). Bright Data dataset `gd_l1viktl72bvl7bjuj0` returned **`experience: null`** on all 4+ test profiles (incl. real contact Chris Surrichio). **This must be solved before hop-1 is feasible:**
- Test a Bright Data dataset that includes full `experience` (their "LinkedIn profiles - experience" variant may differ), OR
- Test whether high-visibility profiles populate it (our tests were low-profile), OR
- Accept Lusha `previousEmployment` (the contacts/enrich payload had the field, empty on our 25 — same question), OR
- Fall back to company-co-membership WITHOUT precise overlap (much weaker — degrades the §2 precision lever).

**Hop-0 (insurance-scan on direct connections) does NOT need this** — it ships independent of the experience-field resolution. Recommend: ship hop-0, resolve experience in parallel, gate hop-1 on it.

## 7. Build sequence

| Slice | Needs | Status |
|---|---|---|
| **`connections_graph.py` (hop-0 + insurance-scan + company cross-ref)** | CSVs only | BUILDABLE NOW — the immediate-value win |
| experience-field resolution | Bright Data dataset test ∥ Lusha previousEmployment test | PROBE NEEDED (gates hop-1) |
| `employment_intervals.py` (EMPLOYED_AT + overlap calc) | experience field | after probe |
| `colleague_expand.py` (hop-1, gated) | intervals + Lusha org-charts + relevance gate | after intervals |
| `network_expand.py` (hop-2, BFS frontier + budget) | hop-1 + §5 governance | after hop-1 proven |
| `score_warm_paths.py` (relevance × path-strength + FINRA/AUM overlay) | all edges | final |

## 8. Reuses already-built machinery

- `secadv_client` — company AUM-band filter (drop out-of-band giants from expansion). DONE.
- `brokercheck_client` — FINRA series-license relevance boost on surfaced people. DONE.
- firm-name strong-match (`_norm_tokens`, subset∥≥2-token) — company cross-reference + CSV `Company` normalization. DONE.
- canonical `people/{slug}/` store + `linkedin_slug` PK. DONE.
- Lusha prospecting org-chart pull (the `.024` LIVE-DISPATCH machinery). DONE.

## 9. Open decisions for Andrew

1. **Ship hop-0 now?** (connections_graph + free insurance-scan on direct connections) — immediate easy-wins, needs only the CSVs. My strong recommend: yes, decouple from the rest.
2. **experience-field probe** — want me to test the Bright Data experience-dataset + Lusha previousEmployment against a known-good profile to confirm hop-1 is feasible before designing further?
3. **Budget model** — what per-run Lusha-credit + Bright-Data-scrape ceiling is acceptable for hop-1/2? (Sets the §5 budget gate.)
4. **Hop cap** — 2 (recommend) or deeper for a research pass?
5. **Insurance-scan scope** — just the 99-IMO-universe overlap, or any-insurance-mention (broader, more easy-wins, more noise)?
6. **ToS posture on volume** — hop-0 CSV is clean (own data). Hop-1/2 Bright Data at volume is bulk-scrape; confirm acceptable / within Bright Data plan terms.
