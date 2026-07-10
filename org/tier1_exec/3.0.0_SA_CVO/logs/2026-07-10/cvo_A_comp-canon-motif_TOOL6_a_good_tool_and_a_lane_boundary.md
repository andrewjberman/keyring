# CVO~A — comp-canon-motif TOOL-6: a GOOD tool (deepened its blind self-test), a refuted perf lead, and the AE-lane boundary that made the fix land through someone else's hand.

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, COORDINATE

**Date:** 2026-07-10 ~19:26–20:16Z · **Agent:** 3.0.0_SA_CVO~A (lane A)
**Task:** CTO GO 192604Z (NFRA_TOOLPASS tool-6, comp-canon-motif). Do-er role, NOT verifier.
**Landed:** `4e3c939d0` (author 0.7.0_AE_CloudOps~C, trailer-credited to me). CTO gate GREEN 200948Z. On origin/CLOUD.

## The tool was GOOD — the job was to sharpen it, not rebuild it
CTO's front pass: SEMANTIC PASS, one real declarative defect (two-file drift), a perf finding. My leads to re-run: CM1, CM2, U1–U3. Every finding re-derived on my own evidence.

## Findings (re-run, not trusted)
- **CM1 (two-file drift) — confirmed, then REFINED by ~C.** `debtscan_canon_scorer.py` has 0 live callers (8 refs / denom 6; only a stale comment `_canonical.py:94` + its own tool-string; nothing execs it; the wrapper runs the thin `canon_motif_scorer.py`). It is 0.7.0's uncommitted WIP → I proposed removal, flagged "reconcile revive-vs-abandon first," did NOT touch it. ~C then caught the FORWARD dependency a caller-scan cannot see: its +29 WIP is a CVO-dispatched (07-07) `score_reachability_canon()` revival, and 0.8.0's NFRA_MSGRAPH names `debtscan_scorecard_latest.json` a convergence input. **"No live caller" ≠ "safe to delete" when planned work depends on it.** CM1-as-delete retired; ~C escalated to CTO+0.8.0.
- **CM2 (perf) — REFUTED, and this was the one to profile.** I *inferred* the `CONTAINS` scans were slow; profiling (off-rail, §6) killed it: warm queries 0.077s, scans 3–6ms, DB load 0.035s, whole tool <4s. Could not reproduce the >2min. Grounded the real cost at source: `_canonical.ensure_fresh` rebuilds when BEHIND (up to 356s) / MUTEX_WAIT 180s — SHARED comp-kuzu machinery, not canon-motif's code. CTO accepted in full ("my error, caught the right way"). SUB-FINDING (actionable): `freshness_assert:61` calls `ensure_fresh` unconditionally; `--allow-stale` gates only the REFUSE (:78), so it still eats the rebuild. Routed to ~C (freshness semantics).
- **U2 (delegation) — confirmed unwired.** DEPLOY/PIPELINE return `kuzu_scorable:False`, "DELEGATED", but neither reads the deploy-ledger nor calls comp-pipescript (source+exec). 2 of 4 canon classes structurally unscored behind an over-claiming label. Routed to ~C.
- **U3 / sovereign:** 49f is a graph edge-string-count (=0), metadata like comp-kuzu, no bd data read.

## The fix (landed 4e3c939d0)
Deepened `--self-test` from "the YAMLs LOAD" to "the scorers are CORRECT": a `_CannedConn` runs the real scorers against canned answers (no graph read), asserting dominant_pct math, the >=0.60 gate, the AC4 firm-asymmetry catch (asymmetric→1 novel; symmetric→0), AC3 suppression (not vacuous), and pinning 49f-count=0 as a regression anchor. Plus CM3: atomic `--ledger` write (mkstemp+os.replace), exercised both arms. **Mutant-proven, not run-green:** 4 scorer mutations each → self-test RED; the OLD structural test stays GREEN under a broken scorer (the comp_route:761 shallowness demonstrated). §2a satisfied.

## The lane boundary — the part that made this pass different
`canon_motif_scorer.py` is the AE lane (`infra/aws/globgrph`). I HELD the commit (didn't pre-commit into a lane with 0.7.0's active WIP) — and the owned-paths gate then BLOCKED me: CVO is not in `CLOUD_OPS_OR_ETL`. **I did NOT `--force`** — that bypass is for index contention, not a lane-authority gap; forcing it is acting-on-their-lane against the enforcement. The gate fired on exactly the boundary I'd flagged. Andrew brought on `0.7.0_AE_CloudOps~C` as the AE committer; I handed off, it landed under its own author crediting me, CTO gated.

Two disclosures I made rather than papered over:
1. My blocked `--only` attempt reset the shared index and unstaged base-CVO's cluster staging (work intact; CTO told base-CVO). I did NOT re-stage another's lane.
2. Source-grounded (`owned-paths-check.sh:37-38`) that the gate keys on `GIT_AUTHOR_NAME`, not session — so `--author "3.0.0_SA_CVO~A"` would have blocked ~C too. ~C commits under its own author + a credit trailer. Sent before ~C fired.

## Two self-corrections banked (the point of the sweep is to catch these on yourself)
- **CM2:** inferred cause from symptom; profiling refuted it. (CTO's own error too — he'd stated CM2 the same way.)
- **Push-ordering:** I read `4e3c939d0`'s COMMIT timestamp (16:07, TZ-ambiguous) and treated it as a PUSH time to question whether the push preceded CTO's gate. Right question (verify-don't-infer), WRONG LAYER: git records no push time, so a commit stamp is invariant under when-the-push-happened — the "line-citation-without-a-vintage" class, my own Rule 22a failing on me. The sound oracle was the message sequence + ~C's not-pushed attestation (CTO+~C both confirmed: gate 20:09:48Z → push ~20:12Z). Banked: a commit stamp is not a push receipt.

## Coordination outcome
Clean multi-agent close: front-pass (CTO) → fix (me) → content-gate (CTO) → land (~C) → commit-gate GREEN (CTO 200948Z) → push → RAVC-4 faithful (me). Semantics (CM1/CM2-sub/U2) are ~C's lane, gated as separate commits. COO FYI'd: no COO implementation leg (tool already registered).

## Compiler Tools
| Tool | Call | Result | Note |
|---|---|---|---|
| comp-symbols | `canon_motif_scorer.py` | 12 fns, 299 lines | oriented before editing |
| comp-grep | `debtscan_canon_scorer` / delegation / callers | CM1 falsifier + U2 | denom 6; only a comment + tool-string reference the dead file; neither delegation reads its target |
| off-rail (§6) | kuzu profiler; `git log/show`; `owned-paths-check.sh` read | CM2 refutation, push-sequence, gate-keying | assurance oracle must not share the tool's predicate; marker carried; each with denominators |
| comp-canon-motif | `--allow-stale --json`, `--self-test` | U2 confirm + fix verify | ran the tool itself (sovereign-clear, metadata) |

Off-rail was structural per §6 (ground truth ≠ the tool's predicate). Profiling REFUTED my own CM2 inference — the highest-value off-rail use this pass. Caught my own `/tmp` MSYS-vs-native path bug twice and a `head`-swallowed rc; each corrected, not papered.

— 3.0.0_SA_CVO~A
