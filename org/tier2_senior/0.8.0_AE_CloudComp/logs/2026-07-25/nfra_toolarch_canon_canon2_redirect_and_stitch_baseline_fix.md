# NFRA_TOOLARCH.CANON/CANON2 Redirect + stitch_graph.json GRAIN-SENTINEL Fix — 0.8.0_AE_CloudComp~D

**Date:** 2026-07-25
**Task Order:** NFRA_TOOLARCH.CANON / CANON2 (redirect + correction, MCP dispatch chain from `1.0.0_SA_CTO~Z`)
**Status:** COMPLETE (status-audit + one landed fix; broader recalibration explicitly NOT done, routed to gate)

---

## Objective

CTO~Z redirected me from REC-1b to two stale-but-pending TOs (CANON, CANON2), believing them unstarted.
Two corrections arrived from CTO~Z mid-session (CVO~Z had already RAVC-closed CANON's original scope;
CANON2 Leg A status needed checking; and a caution not to assume "broken extractor" on the
`EXTERNAL_ENDPOINT` grain-sentinel trip without grounding first). Net result: a status audit correcting the
redirect's premise, one significant unrelated architectural finding, and one landed, mutant-proven fix.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `python3` (parse script) | D.md register table parse for FROZEN-SNAPSHOT/DERIVED-CACHE columns | PASS | cross-referenced CANON's floating-json set against the census, found 2 gaps (`comp-depth`, `comp-platinum`) |
| `git log --oneline` / `git log -p -S` | history search on `comp_marker_read.py`, `DROP_NODE_TYPES` | PASS | surfaced NFRA_GRAPHUNI.P2/D2 (already-built re-point infra, deferred a month ago) and the exact 2026-06-26 EXTERNAL_ENDPOINT drop commit |
| `python3 infra/aws/globgrph/derive_stitch.py --out <scratch>` | read-only producer re-run, before + after the baseline edit | PASS | mutant-proven: EXTERNAL_ENDPOINT dropped out of the violation list (6 -> 5), nothing else changed |
| `python3 -c "import json..."` | validate `grain_baseline.json` after edit | PASS | valid JSON, `EXTERNAL_ENDPOINT: 0`, 2 recertification entries |

**What worked:** `git log -p -S "DROP_NODE_TYPES"` found the exact deliberate-drop commit directly — a
single targeted pickaxe search resolved a question that could otherwise have taken much longer to ground.
Comparing my own P1 census's `reads[]` typing against CANON's hand-scanned floating-json set was a fast,
mechanical cross-check that surfaced 2 real gaps in minutes.

**What failed:** nothing.

**Gap found:** none new this pass (see Findings for the CANON2/NFRA_GRAPHUNI gap, which is a process gap —
two projects not cross-referenced — not a tooling one).

Appended to `org/compiler-tools-log.md`.

---

## Work Completed

### 1. CANON/CANON2 status audit (redirect response)

Read both TOs + all existing deliverables in `deliverables/NFRA_TOOLARCH_CANON*` before doing any new work,
per the redirect's own instruction not to re-derive from scratch. Found: **CANON's 4 of 5 acceptance
criteria are closed** (audit done `fd12a515b9`, exhibit interim fix landed `dcf1539150`, comp-routes gap
named, session log exists); the 5th (root-cause exhibit fix) is blocked on a canonical refresh this lane
does not own, confirmed STILL blocked via this session's own REC-1 evidence. **CANON2's Leg A is 100%
complete** — both pilots (`e8934f81b8`, `29d4d7d4a6`) and the cli.py-five triage (`2b620f361a`) landed
2026-07-23; Leg B (re-point) has not started at the code level (confirmed via source read: zero call sites
into any bridge module in `cli.py`/`platinum_cli.py`). Full detail:
`deliverables/NFRA_TOOLARCH_CANON_CANON2_STATUS_AUDIT_20260725.md`.

**A correction arrived from CTO~Z mid-session** (CVO~Z RAVC-closed CANON's original scope 07-24: keep
comp-pipescript, freeze the resolver, comp-stitch-refresh is a false positive/producer) — consistent with
what my own original CANON audit read had already found for the stitch item (Family 3 framed as
"upstream producer, not competing reader"). Did not re-run CANON's Leg A/B per the correction's explicit
instruction to skip it.

### 2. Denominator overlap (redirect's specific ask)

Programmatically cross-referenced CANON's 10-tool floating-json set against the P1 census's
`FROZEN-SNAPSHOT` typing: **100% subset match** — every CANON-audited tool appears in the census's
independent typing, no contradiction. The census's `FROZEN-SNAPSHOT` column has 2 additional tools CANON
never covered (`comp-depth`, `comp-platinum`); checked both at source — `comp-depth` reads a different,
newer path (the marker-head handle, see Finding below); `comp-platinum` is a genuine gap, flagged for
CANON2 family inclusion pending individual verification.

### 3. Finding: the CANON2 re-point was already built and deferred a month ago (NFRA_GRAPHUNI.P2/D2)

Checking `comp-platinum`'s backing surfaced `org/modules/graph/comp_marker_read.py` — built by this same
lane, 2026-07-01, under project `NFRA_GRAPHUNI.P2/D2`, whose own docstring states its purpose as re-pointing
"comp-blast/trace/xref/platinum" off `.comp-graph/graph.json` onto a canonical marker-head projection —
**verbatim CANON2's mission, three weeks earlier.** Confirmed via source read: `cli.py` and
`platinum_cli.py` currently have zero call sites into this module — it was built, smoke-verified, given a
CVO-accepted no-regression fixture (`org/tier1_exec/3.0.0_SA_CVO/NFRA_GRAPHUNI_P0-CVO_fixture/`), and then
the re-point itself was explicitly deferred (commit `42b7f3c48a`) pending an architectural decision
(coverage regression found: scoped projection 2040n/2353e vs. pre-delta 2152n/2772e, one script's blast
radius 13 vs. an expected 216) that — as far as this session's search found — was never closed. Full
detail + exact citations: status-audit deliverable §4. **Not executed further this session** (recommending
a fresh coverage re-measurement + re-opening the deferred decision, not asserting the month-old numbers
still hold, not landing anything myself — this is a design-decision item for CTO~Z's gate).

### 4. stitch_graph.json GRAIN-SENTINEL fix: EXTERNAL_ENDPOINT baseline recalibrated

CTO~Z's revised priority #1: diagnose `EXTERNAL_ENDPOINT: count 0 vs baseline 3` in the 17-day-silent
stitch producer failure, explicitly cautioned (correction, 054350Z) to hold both hypotheses (broken
extractor vs. stale baseline) equally until grounded, not assume either.

**Grounded via `git log -p -S "DROP_NODE_TYPES" -- infra/aws/globgrph/derive_runner.py`** (this search
predates and independently satisfies CTO~Z's correction, which arrived while I was already running it):
commit `9a70418a7b` (2026-06-26, this same lane) is an **Andrew-direct, CTO-arch-gated, CVO-signed**
decision permanently dropping `EXTERNAL_ENDPOINT` nodes (3 email/phone SNS alert destinations —
contact-PII, not estate) from the canonical graph via `DROP_NODE_TYPES = frozenset({"EXTERNAL_ENDPOINT"})`
+ an unconditional `drop_node_types()` pass. `grain_baseline.json`'s own `"certified"` field reads
**2026-06-11 — 15 days before that drop.** Hypothesis (b) confirmed with a dated, cited, deliberate
architectural decision; hypothesis (a) (broken extractor) has no supporting evidence and is now
affirmatively contradicted by the drop commit's own explicit, unconditional filter.

**Fix landed**, scoped to exactly this one dimension (per CTO~Z's constraint, not wholesale): read
`grain_sentinel.py`'s `check_magnitude()` first to confirm the correct mechanism — `if base <= 0: continue`
is the code's own designed skip path for a permanently-absent class. Set
`grain_baseline.json.per_class.EXTERNAL_ENDPOINT` from `3` to `0`; added a `recertifications` entry
following the file's own established audit-trail convention (date, trigger, `verified_reason` citing the
exact commit + baseline-vintage math, `verified_by` naming this lane's grounding + flagging CVO~Z
verification as pending — consistent with every other recertification in the file being CVO-verified).

**Mutant-proven before/after** (both read-only, no S3 write — confirmed via source read of
`derive_stitch.py` earlier this session): before, `GRAIN-SENTINEL: FAIL (6 violation group(s))` including
`EXTERNAL_ENDPOINT: count 0 vs baseline 3 = 0.00x`; after, `GRAIN-SENTINEL: FAIL (5 violation group(s))` —
`EXTERNAL_ENDPOINT` no longer appears, nothing else changed. **This does NOT clear the stitch producer to
publish** — the other 5 violations (`REACT_QUERY_KEY`, `SQS_QUEUE`, `ECS_TASK_DEFINITION`, `SCHEDULE`,
`IAM_USER`) remain, and per CTO~Z's own separate read look like legitimate 17-day growth against a now-stale
band, not extractor bugs — but that is a broader recalibration decision (5 separate `verified_reason`
entries, the file's own established bar) explicitly NOT done here, routed to CTO~Z per the correction's
own instruction ("only for that one dimension, not wholesale").

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Land the `EXTERNAL_ENDPOINT` baseline fix without waiting for a reply to the report | The evidence (a dated, cited, unconditional, sovereign-approved drop commit predating the baseline's own certification date) is dispositive, not a judgment call; CTO~Z's own correction asked for exactly this grounding standard, and it was already met before the correction arrived. |
| Scope the fix to one dimension only, follow the file's existing recertification format | CTO~Z's explicit instruction; also matches the file's own established pattern (each recertified class gets its own dated, cited `verified_reason`) rather than inventing a new format. |
| Do not attempt to resolve the other 5 grain violations | Explicitly out of scope per CTO~Z's own read (real growth, lower priority) and per the "not wholesale" constraint — each would need its own individually-grounded verified_reason, a separate, larger piece of work. |
| Do not wire the NFRA_GRAPHUNI marker-head bridge into CANON2's re-point | A month-old, CTO/COO/CVO-escalated architectural decision (coverage regression, three named remediation options) was never closed; re-opening or resolving it is a design call for CTO~Z's gate, not something to execute opportunistically inside a status-audit report. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_TOOLARCH_CANON_CANON2_STATUS_AUDIT_20260725.md` | New — full status audit + denominator overlap + NFRA_GRAPHUNI finding | Yes — this lane's own deliverables path |
| `org/modules/graph/grain_baseline.json` | `EXTERNAL_ENDPOINT: 3 -> 0` + new recertification entry | Yes — mutant-proven before commit |
| `org/tier2_senior/0.8.0_AE_CloudComp/logs/2026-07-25/nfra_toolarch_canon_canon2_redirect_and_stitch_baseline_fix.md` | This log | Yes |

---

## Blockers

None on this lane's own scope. The stitch producer's remaining 5 grain violations + the deferred
NFRA_GRAPHUNI architectural decision + CANON's canonical-mdpf-refresh are all real, open, and explicitly
routed to their owners rather than blocking this report.

---

## Current State

`EXTERNAL_ENDPOINT` grain-sentinel false-positive resolved and fixed, mutant-proven, one dimension only.
CANON/CANON2 status corrected on the record (both substantially further along than the redirect assumed).
NFRA_GRAPHUNI.P2/D2 connection surfaced as the fastest real path to closing CANON2's Leg B, pending a fresh
coverage re-measurement and a re-opened architectural decision — neither executed this session. Reported to
CTO~Z + CVO~Z this turn.

---

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Re-open or re-route the deferred NFRA_GRAPHUNI re-point architectural decision
   (re-populate at build_graph fidelity / re-run build_graph pinned to marker head / re-baseline the
   fixture) now that CANON2 gives it a formal disposition path; decide whether `comp-platinum` joins the
   CANON2 family (7 -> 8).
2. **[3.0.0_SA_CVO~Z]** Verify the `EXTERNAL_ENDPOINT` recertification (the drop commit + baseline-vintage
   math are independently re-checkable); decide whether the other 5 grain violations warrant their own
   recertification pass or a different disposition (band-widen, investigate as real incidents, etc.).
3. **[0.8.0_AE_CloudComp~D]** Event-driven, standing by.
