# comp-kuzu n.id fix + first end-to-end residue-clearing cycle — 0.8.0_AE_CloudComp~C

**archetype:** IMPLEMENT
**Date:** 2026-07-25
**Task Order:** CTO~Z dispatch 20260725T112804Z + scope ruling 113225Z (off-main-fabric group)
**Status:** COMPLETE (closure claim PENDING-VERIFY at CVO~Z)
**Cycle wall:** ~11:28Z dispatch → ~11:40Z committed

---

## Objective

Fix comp-kuzu's broken canonical examples (`n.id` → `n.node_id`) at every teaching site, then prove
closure by re-running ~E's item-1b sensor — sensor detects → fix lands → sensor confirms: the program's
first end-to-end residue-clearing cycle (PENDING-VERIFY framing per dispatch, verbatim in the memo).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| bound-var `.id` sweep | grep over the sensor's 7 LAYER_FILES | 8 sites / 3 files | denominator printed; my first `n.id` grep missed a.id/b.id/p.id — predicate widened, disclosed |
| live repro (pre-fix) | `:190` query text, direct read_only kuzu conn (~E's pattern) | Binder exception verbatim | grounds the scope extension: executed sites broken-live |
| `~E sensor` (as-committed) | bare run | **CLEAN rc=0, N=12 = 12+0+0** | CLOSURE: pre-fix N=13 = 11+1+1 rc=2 (committed JSON); orphan→0, member→covered, both movements explained by the fix |
| live repro (post-fix) | corrected example + Q1 form + two-var form, read_only | ALL CLEAN | 2 rows / 5 rows / 2 rows real data |
| `run_validation` (revived) | first-ever execution, read_only conn | Q1 CLEAN (342 edges) / **Q2 FINDING** | 1 of 34 EC2 without IAM instance profile (i-06376c11d8b3c3443) — reported as a finding, not smoothed |
| `commit-gate` | kuzu_cli.py + kuzu_load.py | PASS | clean |
| COMPRAIL HUD | denied one raw grep under infra/ mid-task | rerouted | targeted known-file read → native Read (correct per Rule 21; no marker needed) |

**What worked:** exercising the brokenness BEFORE fixing (the pre-fix Binder repro) turned the scope
fork from an argument into a measurement — CTO~Z's ruling endorsed on exactly that grounding. Reading
the sensor's committed JSON rather than ~E's memo prose caught the member-cell identity discrepancy
(props in prose, node_id in the artifact) and made the post-fix accounting fully explainable.

**What failed:** nothing this cycle (the narrow first grep was widened before any claim rested on it).

**Gap found:** ~E memo §3 prose-vs-JSON discrepancy (member = node_id, not props) — routed, one line.
Plus the revived Q2's WARN (EC2 instance without profile) — routed to CTO~Z for 0.7.0 ownership.

Session line appended to `org/compiler-tools-log.md`.

---

## Work Completed

1. Swept all 7 sensor LAYER_FILES for bound-var `.id`: 8 sites (5 teaching + 3 executed), residual
   sweep 0 post-fix with HEAD positive control (3).
2. Surfaced the executed-sites scope fork mid-execution with disposition; proceeded per ALWAYS-PROCEED;
   CTO~Z ENDORSED (113225Z) + added the run_validation verdict-delta limb.
3. Fixed all 8 sites (one word each). DB + query engine untouched.
4. Acceptance: corrected examples exercised clean read-only; run_validation revived with first-ever
   verdicts disclosed honestly (Q1 clean w/ numbers; Q2 = a real WARN finding); sensor re-run CLEAN
   rc=0 with every cell movement explained; gate clean.
5. Memo `COMP_KUZU_TEACHING_FIX_C.md` at the census path (PENDING-VERIFY framing verbatim).

## Files Modified

| File | Change | Committed |
|---|---|---|
| `.tools/comp-kuzu` | 1 word (usage comment) | This session, this lane |
| `infra/aws/globgrph/kuzu_cli.py` | 4 sites (docstring + 3 help lines) | This session, this lane |
| `infra/aws/globgrph/kuzu_load.py` | 3 sites (run_validation queries) | This session, this lane |
| `.../NFRA_TOOLUNIFY_CENSUS/COMP_KUZU_TEACHING_FIX_C.md` | New memo | No — CTO~Z tree, on disk |
| this log + `org/compiler-tools-log.md` | log + session line | This session, this lane |

## Blockers

None. Task #12 (version_pin coverage derivation) queued next per CTO~Z sequencing.

## Current State

First end-to-end residue-clearing cycle demonstrated at unit scale, PENDING-VERIFY at CVO~Z (sensor +
closure verified as one story). Two routed findings: the EC2-without-profile WARN; ~E's memo prose-vs-
JSON member identity.

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Verify the pair: ~E's sensor one-command re-run (CLEAN rc=0) + the pre/post
   accounting vs the committed JSON; the broken-live grounding re-derivable read-only.
2. **[1.0.0_SA_CTO~Z]** Route the Q2 WARN (0.7.0 territory) + ~E's one-line memo correction; commit the
   census-path memo.
3. **[0.8.0_AE_CloudComp~C]** Task #12 (version_pin coverage) executing next.
