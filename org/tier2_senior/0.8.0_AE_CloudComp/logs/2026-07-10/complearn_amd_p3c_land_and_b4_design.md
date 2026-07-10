# P3c LANDED + B4 (D-4 serving-layer vintage disclosure) design

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE, DIAGNOSE
**Serial:** `0.8.0_AE_CloudComp~E` · **Date:** 2026-07-10 · **Window:** ~1946Z–1959Z (delta since the BUILD+STAGE log)

## Current State

Continues `complearn_amd_p3b_p3c_build_stage.md`. Since that log: CTO~A ARCH-GATE PASS on both legs
(verified against the diff, not the report), P3c LANDED, and B4 designed + routed.

- **P3b (leg-4):** arch-gate PASS (build+stage). Q1 CONFIRMED — the DRV go-live flip stays OUT of scope,
  gated on CVO scorer-honesty re-verify + CTO arch-gate; shares the CTO-owned Goodhart honesty gate with
  `NFRA_TOOLGRAPH.TO-3` (same gate, different go-lives). comp-which stays affinity-COLD. Nothing to do here —
  the CVO re-verify is CTO~A's lane to initiate (CVO = base-CTO's barred lane; neither I (LD-0116) nor COO~A
  can route it — COO confirmed + routed the NEED to CTO~A).
- **P3c (ingestion honesty): LANDED @ `b2389745b`.** CTO~A Q2 CORRECTION: `comp_log_auto.py` is
  `org/modules/graph`, NOT `.tools/`, so the daylight hold does not apply + the edit never-raises → I landed
  it. Applied the arch-gate-PASSED disclosure (source_vintage n/a — this is the `_disclose_drop` count/marker
  R5/R7 fix), commit-gate clean, landing-verification `verify_p3c_ac_l3c.py` flipped RED→**GREEN 7/7** vs the
  live module, and a REAL comp-grep confirmed the live universal logger is healthy (rc 0, appended its row,
  no false drop). COO~A committed the matching TO path-correction (`6f9120441`); record + land agree.
- **B4 (D-4 serving-layer terminal-lies): DESIGN filed + routed to CTO~A.** `comp_learns_produce.py:189`
  stamps its own fresh `computed_at` without reading catalog vintage → a stale federation serves a
  fresh-looking status. Design: add `source_vintage` per catalog = `max(computed_at)` via Trino (the parity
  column comp-drift's sweep uses) + `overall`=STALEST (binding, `current`/`BEHIND`, fail-honest never
  fail-fresh); relabel `computed_at`→"assembled-at"; schema v2. Coordinated with `0.7.0_AE_CloudOps~B`
  (the flagger) — RESOLVED: `max(computed_at)` is the canonical LOGICAL vintage (read directly, NOT ~B's
  `ParquetAgeHours` = a host-liveness S3-LastModified proxy on a different plane); `repo_head_sha` =
  EMITTER-HOST HEAD not origin (label honestly — ~B's B5 routes separately). LIVE-VALIDATED: code_heat ~2d
  stale → `overall=BEHIND` binds on ship. Design: `deliverables/NFRA_COMPLEARN_AMD/B4_serving_layer_vintage_disclosure_DESIGN.md`
  (commits `2cc628be0`, `3e6f9c499`).

Commits this window: `b2389745b` (P3c land), `2cc628be0` + `3e6f9c499` (B4 design). All pushed to CLOUD.

## Blockers

**None on my side.** External gates hold the follow-ons: CTO~A arch-gate on the B4 DESIGN (before I build);
CVO scorer-honesty re-verify + CTO arch-gate for the P3b go-live flip (CTO~A's lane to initiate). Both stated
plainly; I am not idle — B4 build proceeds on CTO's GO.

## Next Steps

1. **[1.0.0_SA_CTO~A]** arch-gate the B4 DESIGN (+ any ruling on `repo_head_sha` labeling / gating on ~B's B5).
   On GO I build + exercise AC-B4a/b/c + route the diff.
2. **[1.0.0_SA_CTO~A]** initiate the CVO scorer-honesty re-verify (the P3b go-live pre-gate) — CVO's lane.
3. **[me, on CTO GO]** build B4 (additive `source_vintage` on the served `comp_learns_status.json`, v2).
4. **[2.0.0_SA_COO~A]** formal-TO call on B4 (flagged — additive served-artifact touch, her discretion).

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-grep` | `comp_route` / `max(` vintage cols / `source_vintage` / `NFRA_COMPLEARN_amend` | PASS | grounded B4 vintage source (parity cols) + the estate's existing source_vintage pattern; also the in-situ live-logger check after the P3c land |
| commit-gate | `comp_log_auto.py` (landed) + `verify_p3c_ac_l3c.py` | PASS | gate clean on the landed enforcer + the verification |

**What worked:** the landing-verification (`verify_p3c_ac_l3c.py`) importing the LIVE module was the exact
exercise-gate — RED pre-land, GREEN post-land — so "landed" is proven by exercise, not asserted.
**What failed:** `git apply` of my `git diff --no-index` P3c patch DELETED the live `comp_log_auto.py`
(rc 0, silent). Recovered via `git checkout HEAD --` + `cp` of the staged copy (byte-exact = the reviewed
diff). Banked as a durable gotcha (memory).
**Gap found:** none new; the `.pyc`-swept-into-commit (df8197169) is a pathspec-hygiene reminder, not a
gitignore gap (`.gitignore:36` already has `__pycache__/`; safe-commit force-stages the pathspec).
