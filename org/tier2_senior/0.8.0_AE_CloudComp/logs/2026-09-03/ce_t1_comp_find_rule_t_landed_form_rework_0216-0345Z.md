# TO-CE-T-1 -- comp-find Rule T, interim fix then rework onto the landed FORM -- 0.8.0_AE_CloudComp

**Date:** 2026-09-03
**Task Order:** NFRA_COMPEFFICACY.TO-CE-T-1.comp-find-s4-audit
**Status:** COMPLETE (pending CVO grade + MSTR push)

---

## Objective

Deliver the s.4 per-tool audit for `comp-find` (row T-1) and the one code change this cell owed:
bring the `--corpus aws` pull's internal timeout under a caller-settable ceiling (Rule T), so a
600s internal constant stops silently outliving the harness's 120s outer ceiling.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-read | `.tools/comp-find --enumerate 'timeout'` (before write, and again post-rework) | PASS | 3 hits both times; located the two subprocess timeout sites exactly, pre- and post-edit |
| commit-gate.sh | on `.tools/comp-find`, `.tools/tests/test_comp_find_battery.py`, `.tools/_compbudget.py` | PASS | clean across all three commits |
| comp-passcraft | `recon comp-find` | PASS | MOVES 1-3 auto-observed; 4-8 hand-run in the deliverable |
| comp-adversary | preflight (per the TO's own `<preflight>` block) | PASS | rc 0, cited commits/paths verified at issuance |
| comp-schedule | preflight | PASS | 0 armed gates named this project/tool at issuance |
| proof-of-spec-check.py | on this instance | see below | validated before the `complete` flip |

**What worked:** comp-read's `--enumerate` located both timeout sites precisely on the first try, before and after the rework, so the code change was never made against a stale line number. comp-passcraft's MOVE 7 (a non-sharing instrument) caught a real cross-check win: an independent raw Cypher `count(n)` query matched comp-find's own DENOMINATOR exactly (2100), which is the kind of corroboration the estate's doctrine asks for.

**What failed:** nothing tool-side. A design assumption failed live (see Work Completed #3) -- not a tool defect.

**Gap found:** none new; two pre-existing gaps surfaced as findings in the deliverable (comp-find has no `--version`; the graph-call-manifest's subcommand list is stale) but neither blocked this TO.

---

## Work Completed

### 1. Interim fix (T-16 DEFERRED shape), commit `88e870b115`

Per the TO's own Grammar clause ("until [the form] lands, the T-16 DEFERRED shape as the stated
interim"), replaced the hard-coded `timeout=600` on the `--corpus aws` pull with a caller-settable
`--budget-s` (default 100s), a `DEFERRED` disclosure at expiry, and two new battery arms (F/G)
exercising the ceiling on the production binary directly and a red-first mutant control.

### 2. Mid-round spec landing -- surfaced as NFRA_COMPEFFICACY-S1

Minutes after committing #1, `1.0.0_SA_CTO` landed PRD v0.4 s.4.4 ("RULE T's FORM", commit
`19bf1c7322`) -- a materially different, project-wide grammar (`--budget` not `--budget-s`, env
`COMP_BUDGET_S`, 90s default, `--budget 0` = unbounded, exact `WITHIN BUDGET`/`BUDGET REACHED`
tokens, a `--cursor` resume mechanism, and ONE shared sibling module `.tools/_compbudget.py`).
This is exactly the trigger the TO's own Grammar clause named. Surfaced via the (then-still-MCP)
surprise channel as `NFRA_COMPEFFICACY-S1`; issuer `2.0.0_SA_COO` (92960) agreed the reading and
amended the TO's bound to admit the one shared module.

### 3. Rework onto the landed form, commit `2718cffc45`

Built `.tools/_compbudget.py` (the form's carrier: `resolve_budget`, the two terminal-token
builders, the always-printed `DEFERRED` bucket, a `Clock` for `remaining()`-derived timeouts).
Rewrote `_aws_corpus` around a genuine UNIT concept: an explicit `node_type` pathspec makes each
named type its own unit, queried separately in sorted order, with REAL `--cursor` resumability
(exercised live end-to-end: a 3-type pull forced to `BUDGET REACHED` at `--budget 15` named the
last-completed type as its cursor; resuming with that cursor skipped the completed units and
finished the remainder `WITHIN BUDGET`). An unscoped pull stays one indivisible "ALL" unit --
decided against decomposing it after measuring that a cheap-looking discovery step (enumerating
distinct node_types first) itself took **247.5s**, worse than the 600s constant this cell exists
to retire. Found and fixed a real bug live while testing the env-var precedence path: a SCOPED
call with zero completed units was mislabeled with the UNSCOPED branch's "one indivisible unit"
text; added a third, correctly-distinguished "NO CURSOR YET" branch. Also fixed a print-ordering
defect (a `NO HITS ... MEASURED zero` line could print even when the budget had been reached and
nothing was actually measured) and a pre-existing latent bug in the battery's own `_report()`
printer (a `None`/SKIP result rendered as `FAIL` in the per-row log line, though the aggregate
count was already correct) -- both caught by exercising the code, not by inspection.

### 4. Live finding mid-exercise -- surfaced as NFRA_COMPEFFICACY-S2

While exercising the forced-ceiling control, the live `--corpus aws` backend itself degraded: the
same unscoped query that had completed in 7.4-14s across five measurements over ~20 minutes took
>=90s (its own `BUDGET REACHED`) on three consecutive attempts, including one isolated,
non-concurrent run. The Kuzu DB file was unchanged in size/mtime, ruling out DB growth. It
self-resolved (a full 10-arm battery back to 19.68s). Root cause not chased (this seat's own rapid
`--mode inc` call volume is the leading, unconfirmed hypothesis) per CLAUDE.md's speed governor.
Filed as `NFRA_COMPEFFICACY-S2`; CVO's L8 read (93005) adjudicated `DISMISSED_WITH_REASON`
pending this commit landing, and caught a real grain error in the row's own evidence (this seat
quoted an `ls -la` LOCAL mtime with a trailing `Z` -- CLAUDE.md 22a's own named trap -- the
conclusion was unaffected, only the label). Consequence: redesigned battery arms F2/F3 to be
latency-tolerant (assert the discriminator contract, not "must complete fast" against a live
external dependency) rather than leave a flaky arm in the estate's primary search tool's battery.

### 5. Deliverable + this log + proof-of-spec

`comp-find.result.md` at the tree home, all 31 s.4 fields measured (not asserted), citing the
final commit `2718cffc45`. Battery: 10/10 PASS at file grain (direct and under pytest, confirmed
twice -- once mid-degradation with a diagnosed+fixed failure, once clean at 19.68s). Directory
grain unchanged (`test_fabric_check_classify.py:76`, CTO's F6 file, not this cell's).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Rework onto the landed form before reporting, rather than report the interim shape | The TO's own Grammar clause named this exact trigger ("until it lands"); the issuer (92960) agreed in-round; reporting a superseded grammar would cost more later than fixing it now |
| Do not decompose the unscoped "ALL" pull into per-node_type units | Measured: a discovery step (enumerate distinct types) costs 247.5s, worse than any sane budget -- decomposing would defeat Rule T's own purpose. Disclosed as a named non-application, never faked with a cursor that would not resolve to anything real |
| Make battery arms F2/F3 latency-tolerant instead of asserting "must complete within default budget" | A live external backend's latency is not a property this battery controls; NFRA_COMPEFFICACY-S2 showed the same query varying 7.4s to 90s+ with the underlying data unchanged. Asserting the discriminator contract (exactly one self-consistent outcome) is the sound test; hard-requiring the happy path on live infra is the "wrong arm" |
| Use the audited `system-current-override` on both fix commits rather than run `comp-system` regen | `infra/system/{00_synthesis,03_comp_tools,README}.md` already sat modified-uncommitted at this device from other in-flight work at session start; pulling a regen into this TO's scope would exceed its bound and risk laundering unrelated unlanded work |

---

## Push State (MEASURED, ls-remote + is-ancestor)

At 03:36Z: `origin/CLOUD @6e8805eb90`; `88e870b115` ON origin, `b89b0493e5` + `2718cffc45` LOCAL
only. RE-MEASURED at 03:43:18Z after a push-window close notification named `2718cff`:
`origin/CLOUD @2718cffc45`; `git merge-base --is-ancestor` returns rc=0 (ON origin) for BOTH
`b89b0493e5` and `2718cffc45`. All three of this cell's commits are now ON origin/CLOUD.

---

## Compiler Tools mandate discharge (per the TO's `<compiler_tools_mandate>`)

BEFORE WRITE: `comp-read .tools/comp-find --enumerate 'timeout'` -- run twice (pre-rework: 2 hits
at :158/:607; post-rework: 3 hits at :194/:205/:715, the new `remaining()` comment line counted as
a third). BEFORE COMMIT: `.tools/commit-gate.sh` on the tool and the battery, both direct and
under pytest at the file grain -- clean on both commits. AFTER COMMIT: a real `comp-find` run from
another seat is `3.0.0_SA_CVO`'s grade run (FWD-9), not yet observed by this seat as of this log.
