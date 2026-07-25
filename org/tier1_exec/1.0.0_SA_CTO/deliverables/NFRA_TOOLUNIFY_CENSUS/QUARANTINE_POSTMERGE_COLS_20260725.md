# Quarantine record — 6 orphaned postmerge-cols YAMLs (2026-07-25, `1.0.0_SA_CTO~Z`)

**What:** `org/modules/graph/postmerge-cols/{C_02.client_performance, C_06.client_mix_timeseries,
D_00.portal_aggregates, D_02.advisor_client_detail, D_03.composition_artifacts,
D_04.client_portal_summary}.yaml` — moved OUT of the working tree to the session scratchpad quarantine
(`.../scratchpad/quarantine_postmerge_cols_20260725/`). **Reversible move, not a deletion.**

**Why:** all six were **untracked (`??`), dated 2026-07-01 15:16 — 24 days old** — orphaned derived
artifacts from a dead July-1 session (their `INF_*` siblings from the same family ARE tracked in HEAD;
these six never were, and no current lane owns them — `~D` explicitly disclaimed them, no other live lane
touches `postmerge-cols/`). They were tripping the new BLOCKED-ON-PEER-LANDING guard (correctly — the
guard cannot distinguish in-flight peer work from debris), blocking `~D`'s GATEBOUND Stage-A landing and
base's queued Rule-22a patch behind the same clearing event. The census's own orphaned-artifact class,
live, blocking the census's own program.

**Why quarantine and not the alternatives:** adopt-commit would land 24-day-old derived outputs of
unknown vintage as authoritative (the stale-artifact class that cost this program a wrong GRAPHUNI
override today); delete is destructive and needs no urgency; quarantine is reversible, auditable, and
unblocks now. If a future lane needs them, they are preserved byte-identical at the quarantine path.

**Banked design input, not actioned:** the guard treats `M`-modified and `??`-untracked sources
identically as "peer in flight." A 24-day-old untracked file is debris, not in-flight work. A
staleness-aware refinement (e.g. untracked + older-than-N-days ⇒ named DEBRIS-CANDIDATE verdict rather
than BLOCKED-ON-PEER-LANDING) is a candidate follow-on — recorded here as input, deliberately not rushed
into the guard the same day it landed.

## Second quarantine, same session (~0847Z): 5 types-index files

After postmerge-cols cleared, the gate re-fired naming a NEW non-overlapping set: 5 untracked
`types-index/` files (`BenchmarkHeatmapProps.yaml`, `BenchmarkModelData{,.fields}.yaml`,
`BenchmarkPeriodReturn{,.fields}.yaml`) — **dated Jun 17 / Jul 1 (24–38 days old), never committed ever**
(`git log` empty per `~D`'s grounding). This is the SAME debris population Lane-E's census finding
documented (`comp-types` persists garbage/derived YAMLs into `types-index/`; 20/25 untracked at count
time). Quarantined to the same scratchpad dir, same reversible-move reasoning; tracked files explicitly
skipped by `git ls-files` check. **The remaining ~13 untracked types-index files were NOT gate-named this
run and are left in place** — their disposition belongs to the comp-types debris fix (synthesis §2f), not
to per-incident quarantines. If the gate names more later, same procedure. **The two back-to-back
incidents strengthen the DEBRIS-CANDIDATE guard-refinement case: both blocking sets were month-old
never-committed files, zero were live peer work.**
