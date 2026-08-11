# THE c3_cover MECHANISM (4 -> 1,255) + THE COMPLETE-COVERAGE MODEL (C3.i + C3.ii x substrates, daily)

**Author:** `4.0.0_SA_CRO~B` · Andrew-direct: understand the corp_localize/anatomy decomposition (4 -> many),
establish complete C3.i + C3.ii coverage global over AWS + codebase (ajb_workspace + portal), model the
two-repo boundary as a deterministic barrier, refresh daily with the Kimi SVP.

## 1. THE MECHANISM (answered) -- anchor-NODE overlapping-domain-cover
`org/tier1_exec/3.0.0_SA_CVO/deliverables/kimi_subdivision_harness/c3_cover.py`. Andrew-ruled 2026-08-07
(*"I would absolutely say B"*): a C3.i structure keys on the **anchor NODE, not the anchor TYPE**.
- anchor TYPE -> **5 systems, fixed forever** (why materialization showed 4). Two firms' refineries
  (sys-bd-medallion, sys-inf-medallion) collapse into ONE `object-data` system -- useless for a per-firm
  risk surface.
- anchor NODE -> **1,255 structures, scaling with the estate** (measured, this harness run).
- It is OVERLAPPING-DOMAIN-COVER (overlap allowed), explicitly NOT union-find/connected-components (the
  KNOWN-FAILED model that over-merges to one supersystem). Domain = anchor-type category; each anchor
  NODE within a domain is its own C3System. Measured `by_domain`: pipeline 847 · object-data 242 ·
  identity 149 · table-data 16 · compute-orchestration 1.
- So "how did C3.i get to 14?" -- it didn't. The DETERMINISTIC cover is 1,255; the 14 was a legislated
  summary; the 4 was the over-merged type-keyed materialization. All three are different objects.

## 2. THE COVERAGE GAPS THIS EXPOSES (the real work)
1. **SUBSTRATE COVERAGE IS AWS-BACKEND ONLY.** All 1,255 carry `substrate_side: ['BACKEND']`. The cover
   has NOT run over PORTAL (the portal repo) or the ajb_workspace codebase. **Complete coverage requires
   the cover across ALL substrates** -- exactly Andrew's global AWS + codebase(x2 repos) requirement.
2. **ANCHOR GAPS inside AWS-backend:** 1,103 instances have NO catalog anchor (unanchored -> uncovered);
   617 single-motif domains unpromoted (< PROMOTE_MIN 2). Of 6,138 instances considered, ~1,720 are not
   in a promoted structure. Coverage is not yet 100% even where it ran.
3. **HARNESS != PRODUCTION.** This 1,255-cover is in the kimi_subdivision_harness; the production daily
   derive (`derive_runner.py`) still emits `FROZEN_CONTROL {C2Motif 19, C3System 4}`. **Complete coverage
   = promote the anchor-node cover into the daily derive.**

## 3. THE SUBSTRATE / TERRITORY MODEL (the two-repo deterministic barrier)
Already partially modeled: `layer` = SUBSTRATE `aws | portal | ms | pipeline | semctl`
(LAYER_FIELD_ANATOMY:90); C2C3_NAMING_AND_DOMAINS:80 already states *"AWS / ajb_workspace / portal = code;
MS = content."* And the anatomy notes **"C3 union-find cannot compose across [a substrate]"** -- i.e. the
substrate boundary IS a deterministic barrier by construction. **Andrew's ask makes it explicit + complete:**
- **ajb_workspace and portal are TWO REPOS = a hard deterministic barrier** (different git roots; no edge
  composes across). Model them as distinct substrate_sides/territories so the cover is computed PER
  substrate and never merges a portal structure with an ajb_workspace one.
- Territories to cover completely: **AWS (backend) · ajb_workspace (codebase) · portal (codebase)** at
  minimum (ms/pipeline/semctl as they mature). Each is a deterministic partition; C3.i cover runs within
  each; C3.ii verticals declared across them.

## 4. COMPLETE-COVERAGE MODEL (what "done" is)
- **C3.i (deterministic floor):** anchor-node overlapping-domain-cover, run PER SUBSTRATE (AWS + both
  repos), anchor gaps closed (every instance either anchored or explicitly counted as unanchored-residue
  with its denominator). Scales with the estate; ~1,255 today on AWS-backend alone.
- **C3.ii (declared ceiling):** the 28 verticals, reconciled DAILY against the C3.i cover + the census
  (the 29->28 merge propagated; residue verticals placed or declared).
- **Global:** the union of substrates = AWS + ajb_workspace + portal (codebase = both repos, per Andrew).
- **Daily:** the whole reconciliation (cover -> census -> declared roster -> drift flags) refreshes with
  the Kimi SVP, so "how many verticals / structures / are they covered" is answered from a same-day
  measurement, never a 2-month-old aggregation.

## 5. PATH (proposed; CRO measures + recommends, CTO gates, CVO owns the derive)
1. Run c3_cover across PORTAL + ajb_workspace substrates (today it is AWS-backend only) -> the first
   complete cross-substrate C3.i count.
2. Close the anchor gaps (1,103 unanchored) or declare them counted-residue.
3. Reconcile the declared 28 against the full cover + census; propagate the 29->28 merge to yaml + matrix.
4. Promote into the daily derive + wire the coverage reconciliation into the Kimi SVP.
