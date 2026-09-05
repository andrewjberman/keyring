# The BOUNDARY-b class run against this fabric, and the residual turned out to be live -- 0.0.0_AB_MSTR~Z

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, COORDINATE

**Date:** 2026-09-05 1336-1420Z (delta since session_0437-0540Z)
**Task Order:** none (standing MSTR fabric-infra duty)
**Status:** COMPLETE. Finding routed and accepted; the fix is CTO law surface and is NOT built here.

## Objective

The laptop MSTR landed BOUNDARY b -- merge exemptions had been deciding whether a row was the
integrator's by reading a field the integrator writes -- and asked whether the same
self-attestation shape exists in this fabric's gates. Run that class here rather than file it.
Secondary: close a prediction I had made publicly about Bloomberg.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-find | `'surfaced_by\|disarm_owner\|issued_to' --limit 30 --band SURFACED` | PASS | 6471 hits / 52561 files, SURFACED 276; most are routing/display, not permission |
| comp-find | `'<issued_to>' --files` / `'0\.9\.0_WK_' --files` | PASS | The control that exposed my broken git-grep zero |
| comp-read | `.tools/owned-paths-validate.py --for "how does it extract a worker's write surface"` | PASS | THE find: gave the real tree name and the real regex |
| comp-read | `.tools/to-pipeline-gate.py --enumerate 'NEVER REFUSES\|newly.added'` | PASS | Re-derived the severity limb by CONTENT, not by the peer's line numbers |
| comp-read | `.owned-paths.yaml`, `org/missions/DIRECTIVES.yaml` (earlier window) | PASS | worker_grant stanza; the D7 ON HOLD qualifiers |

**What worked:** `comp-read --for` on the RESOLVER rather than on a task order. I had spent two
census attempts guessing the format; the resolver DEFINES it, and one read gave both the real
directory name and the exact line-anchored regex. Reading the thing that parses beats reading the
thing parsed.

**What failed -- THREE broken matchers of mine in one window, every one a clean confident zero:**
1. `git grep -E '<issued_to>\s*0\.9\.0_WK_'` -> 0. POSIX ERE has no `\s`. There ARE worker orders.
2. Census over `task_orders` (UNDERSCORE). The real tree is `task-orders` (HYPHEN), read from
   owned-paths-validate.py's own `ls-files` call. 2243 files of the WRONG POPULATION.
3. My own `<paths>` extractor, hand-written before reading the format.
Every one was caught by the same instrument: A POSITIVE CONTROL READING ZERO WHEN IT COULD NOT
TRULY BE ZERO. Without the control, (2) would have shipped as "0 hits, residual is latent" -- the
exact opposite of the truth.

**Gap found:** `comp-which` has no curated rule for ownership questions; it declined honestly and
pointed at comp-find. Same gap as the earlier window, restated once, not filed twice.

## Work Completed

### 1. The class, run against this fabric's gates

Censused permission-deciding reads of `surfaced_by` / `issued_to` / `disarm_owner`. Claimed the
strongest structural candidate, NOT the population -- 276 SURFACED hits are mostly routing and
display. Candidate: `halt-gate-check.sh:142-161`, which admits a spine-v3 worker iff a
NON-TERMINAL order under `<CODE>` at HEAD is `issued_to` it, and derives `issued_by` from the same
file. On its face that is the boundary-b shape.

Initially graded NOT defective, because `.owned-paths.yaml:44-47` makes task orders lie outside a
worker's write surface -- so the granting field is authored by the issuing COO. That reasoning was
correct AND the conclusion was incomplete, which is why the residual mattered.

### 2. The residual, measured with the PRODUCTION instrument

Imported `owned-paths-validate.py` and graded with its own `_paths_block_entries` and
`_order_grants` -- deliberately NOT the peer's text-matcher, so the result corroborates instead of
repeating. Question asked of each order was the resolver's own: DOES THIS ORDER GRANT ITS OWN PATH.

```
DENOMINATOR            104 tracked files under org/missions/D*/*/*/task-orders/
positive control        43 carry a non-empty <paths> block
issued_to a worker      42
granting THEIR OWN path 12
  NON-TERMINAL (LIVE)    5   all status=pending, all NFRA_CLDGRPH
  terminal (grants none) 7
granting any OTHER path in that dir: 0   -- narrow, not a directory grant
control on status reader: complete 66, pending 28, staged 7, withdrawn 3
```

The five: TO-CG-D-7, D-8, D-9, D-10, D-11 (workers ~1/~2/~3). Each admits its worker to exactly one
extra path -- the order file itself, which carries the `<paths>` and `<issued_to>` that BOTH the
halt-gate admission and the commit lane read to decide what that worker may do.

### 3. The severity limb, answered by the peer and RE-DERIVED HERE INDEPENDENTLY

Peer measured that `to-pipeline-gate` never refuses an existing TO. I re-derived it BY CONTENT
rather than by their line numbers -- on purpose, because this tree is 189 behind and their `:699`
does not resolve here (their tree: `:1573-1579`). Confirmed: the gate's domain is newly-added TO
files (`:119`, `:1120`, `:1404`, `:1410`).

Then found the piece neither of us had: **`:1433-1439`, LAYER 1 half B -- `check_complete_flip`
runs over `dispatched`, on EVERY staged TO, added OR modified.** So the declared control set
resolves as:

```
layers 2/3      newly-added scope   -> ISSUANCE
layer 1 half B  modify scope        -> TERMINAL FLIP
   nothing                          -> a MODIFY to <paths>/<issued_to> on a NON-TERMINAL order
```

That is the finding, and it is stronger than "the gate is issuance-scoped by design", because the
gate ALREADY reaches modifications. The author's own comment (`:1434-1436`) records the scope
choice verbatim -- "Different question, different scope, stated so the asymmetry reads as
deliberate rather than as an oversight" -- which proves the uncovered member is NOT a rejected
case but a third question nobody asked.

### 4. Bloomberg prediction closed

I predicted publicly that DAPI would self-heal at the scheduled fallback without intervention. It
did: port 8194 has a listener and the ledger carries `2026-09-05T11:01:41Z
SUBMITTED-UNATTENDED-FALLBACK`, the 6th consecutive. `0.0.3_BG_BBGTerminal`'s refusal to burn the
fire-once budget at 01:00 was correct. D7 intake moved exit 5 -> exit 2, still failing under the
hold, cursor still unmoved.

## Decisions Made

1. **Did NOT duplicate the peer's census.** Same subject, different instrument (production parser
   + production predicate vs text match). Their 4 vs my 5 diverged on their status classifier;
   they said so and named mine the number of record.
2. **Did NOT claim severity before measuring it.** Sent the population and named the unmeasured
   limb explicitly rather than implying exploitability.
3. **Did NOT append the durable surprise row to NFRA_CLDGRPH's channel.** This tree is 189 behind,
   so an append lands at a stale offset -- CLAUDE.md 14b's guaranteed-conflict shape on an
   append-only shared file. THIS LOG IS SITE Z'S DURABLE CARRIER until leg 1 runs; the row lands
   after that, or from whoever holds the current tree.
4. **Did NOT build the control.** Proposing is legal, implementing an unasked gate is not, and
   this is CTO law surface.
5. **Revised my own proposed control after the origin became clear.** Refusing any order whose
   `<paths>` names the task-orders tree would BREAK the worker `<status>` flip those five rely on
   (`.owned-paths.yaml` ~:916 records that loose end). The correct predicate is FIELD-scoped: let a
   worker write its own `<status>`, never its own `<paths>` or `<issued_to>`.

## Files Modified

None in the repo this window. This log is the only artifact. Memory (outside the repo) extended:
`a-taxonomy-does-not-protect-the-rung-you-left-out` with the declared-control-set variant.

## Blockers

**NOT BLOCKED.** Nothing at this seat waits on another seat; the cross-fabric thread is closed by
both sides with nothing owed either way.

**AT ANDREW (unchanged, four):** fleet relaunch composition; `/integrate merge` leg 1; the
memory-index design call; whether `Ticket Center` falls inside the 2026-08-25 order.

## Current State

`origin/SITEZ` = `0f5480ed51`, `origin/CLOUD` = `76c5f90155`, CLOUD 189 ahead, SITEZ 2 ahead, both
ls-remote. Finding is with `1.0.0_SA_CTO` at 94374 plus addendum 94377 (also to `3.0.0_SA_CVO` and
`2.0.0_SA_COO`), credited to site Z, count of 5 accepted as the number of record.

The five self-granting orders are UNCHANGED and UNTOUCHED -- I measured them and did not edit them.
Their workers are dead (the fabric is down), so nothing is exercising the path right now. The
escalation requires two commits, each individually legal and each visible in the log under the
worker's author line; what is missing is a gate that grades the first one.

Live on this device: this seat and `0.0.3_BG_BBGTerminal`. Zero crons. Both Monitors running.

## Next Steps

1. **[Andrew]** The four calls above; leg 1 now carries three reasons (hook-fix precondition, the
   189-commit gap, and landing the surprise row where it belongs).
2. **[`1.0.0_SA_CTO`]** The field-scoped predicate at the L6 neck, if accepted. Not this seat's build.
3. **[`0.0.0_AB_MSTR~Z`]** After leg 1: re-verify `38a37be871` against own HEAD, apply BOTH
   pre-commit hook lines, re-exercise and REQUIRE the input-source line to be observed; then append
   the NFRA_CLDGRPH surprise row.
