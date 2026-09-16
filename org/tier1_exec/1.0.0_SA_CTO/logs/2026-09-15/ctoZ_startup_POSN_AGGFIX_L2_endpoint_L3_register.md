# POSN_AGGFIX opened at L2 and L3 on a respawned seat -- 1.0.0_SA_CTO~Z

**archetype:** COORDINATE
**Date:** 2026-09-15
**Task Order:** ad-hoc -- POSN_AGGFIX L2 `/endpoint --forward` + L3 register (Andrew-direct ~16:2xZ)
**Status:** BLOCKED at L4 on Andrew's word (L2 and L3 COMPLETE)

---

## Objective

Respawned by `0.0.0_AB_MSTR~Z` after the prior `~Z` session died on the account's weekly limit. Run startup,
read the backlog, and act on Andrew's word: open the new D4 project POSN_AGGFIX by running `/endpoint --forward`
on `4.0.0_SA_CRO`'s Positioning AGG restore plan.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `comp-which "how do I grep the repo"` (A.3) | PASS | 104 of 104 comp-tools resolve bare; a forwarder ran |
| comp-find rail | a raw `grep -rn` over DIRECTIVES.yaml + org/projects | PASS (refused) | the rail denied the whole call as designed; re-run with native Grep |
| missions-tree-index.py | `derive`, `derive --write`, `check` (worktree, then shared tree) | PASS | 18 tree projects, 18 valid, 0 violations; DIRECTIVES.yaml "no additions needed" after the hand edit |
| comp-pulse (risk reflex, via safe-commit) | `diff` on the 5 committed paths | PASS | 5 of 5 checked against 1662 danger nodes, zero results, map 0.1h old |
| to-check.py | `--all --assignee 1.0.0_SA_CTO~Z` | PARTIAL | only the tail was read and it listed completed orders of other seats; not concluded either way |
| sequence-check.py | `--project POSN_AGGFIX` | PASS | not listed in SEQUENCE.yaml, so not sequenced; flags 0 |
| audit-archive-invoker.py | A.2 | WARN | known STALE-BASELINE plus six INTEGRITY/ERROR-FAILCLOSED "baseline missing" rows and an uncovered `org/opal-ipblock-audit.log`; not chased per org/XXX.md A.2 |

**What worked:** the tree validator and the commit/merge guards graded the registration end to end with printed
denominators; `get_delivery_state` gave 11 of 11 READ against the ackable denominator.
**What failed:** a long quoted heredoc in the Bash tool failed to parse ("unexpected EOF while looking for matching
`'`"), so nothing ran; the same content landed through the Write tool. Cause not measured.
**Gap found:** none new.

---

## Work Completed

### 1. Startup
- `/watcher`: registered LIVE (was NOT REGISTERED); inbox Monitor armed, task `ba7bfgi9r`, confirmed running.
- Session serial file written; comp-tool PATH 104 of 104; delivery ledger 11 of 11 READ since 10:00Z.
- Backlog of ten messages read and acked: the POSN_ASTTAX close carriers (23123, 23131, 23148, 23151, and two
  from `3.0.0_SA_CVO~Z`), the CLAUDE.md pick relays (23125, 23126, 23127, 23129), the POSN_AGGFIX relay (23156),
  and the `~W` scope relay (23163).
- POSN_ASTTAX needs nothing from this seat. `1.0.0_SA_CTO~W` closed it on Andrew's word @`e223c78ed5` (in HEAD).

### 2. L2 -- the endpoint
- Input: the CRO plan at origin/CLOUD @`2033ff3ea6`, blob `0765b9af1f`, 13372 bytes, read whole cross-fabric.
- Output: `org/tier1_exec/1.0.0_SA_CTO/deliverables/POSN_AGGFIX_ENDPOINT_FORWARD_20260915_Z.md`, FWD-1..FWD-8, all
  EXERCISED and none a wait. Every citation was printed against the plan's bytes.
- FWD-4, FWD-6 and FWD-7 rest on the CRO's recommendations for D1, D2 and D3, and each states its other branch.

### 3. L3 -- registration
- `org/missions/D4/POSN/POSN_AGGFIX/project.json` (site-z, REGISTERED, active), the generated
  `org/projects/POSN_AGGFIX.json`, and the D4 `members.projects` line, committed in a sparse linked worktree.
- Worktree commit `6925b74703`; drained into SITEZ by `safe-merge.sh` as `d5e068cde4`; worktree and branch removed.
- Read back from SITEZ HEAD: all four new paths present, the members line carries POSN_AGGFIX, check 0 violations.

### 4. Andrew-direct record and broadcast
- Record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_162xZ_POSN_AGGFIX_CTO_Z_ENDPOINT_FORWARD_ON_CRO_RESTORE_PLAN.md`.
- One message to `0.0.0_AB_MSTR~Z` (23169), `2.0.0_SA_COO~Z` (23170) and `4.0.0_SA_CRO~Z` (23171), 3 of 3 DELIVERED.
  It carries the verbatim word, the eight outcomes for Andrew, the brief_ref problem for the CRO, and this seat's
  agreement to the CLAUDE.md pick.

### 5. The CLAUDE.md pick
- AGREED, SITEZ WHOLE, lines 41-63. Measured by `git cat-file` at both pins: `to-pipeline-gate.py` @`cd399d339d`
  `:1015` and @`942e4ff992` `:1702` carry the same `_newly_added` docstring. SITEZ HEAD lines 41-63 are 2231 bytes,
  sha256 `5bd224562052eb936bce6f0f221284bd`, identical at `ef41d40a66`.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Treat the CRO plan as the L2 input despite its "not a brief" status line | Andrew named it as the input to `/endpoint --forward`; F1's refusal guards against an endpoint synthesised from a topic string, which this is not. Stated as a reading in the record |
| Write FWD-4/6/7 on the CRO's recs, each with its other branch | D1-D3 are Andrew's; the endpoint stays usable under either answer without pre-deciding it |
| Register at L3 now, stop before L4 | L3 is the CTO's, reversible, and independent of D1-D4; a PRD may carry no open decide-first question, and the spine makes the DONE WHEN confirmation Andrew's |
| Commit in a linked worktree | five files only this seat touches (Rule 14b), with `~W` seats live on the shared index |
| Leave brief_ref unresolved and name it | the L1 shape and the cross-fabric landing belong to `4.0.0_SA_CRO~Z` or the integration |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/missions/D4/POSN/POSN_AGGFIX/project.json` | new project row | Yes -- `6925b74703`, drained `d5e068cde4` |
| `org/projects/POSN_AGGFIX.json` | generated index row | Yes -- same |
| `org/missions/DIRECTIVES.yaml` | D4 members += POSN_AGGFIX | Yes -- same |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/POSN_AGGFIX_ENDPOINT_FORWARD_20260915_Z.md` | L2 endpoint | Yes -- same |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_162xZ_POSN_AGGFIX_CTO_Z_ENDPOINT_FORWARD_ON_CRO_RESTORE_PLAN.md` | Andrew-direct record | Yes -- same |
| this log | session log | this commit |

Push state: LOCAL. origin/SITEZ reads `6f09a06dc9` (ls-remote 16:5xZ); site-Z push hold.

---

## Blockers

- BLOCKED on Andrew: his DONE WHEN word on FWD-1..FWD-8 and his answers to D1-D4, relayed through
  `0.0.0_AB_MSTR~Z` (msg 23169). The s.6 process question is already with him through `0.0.0_AB_MSTR`.
- NOT blocking yet, carried to L4: brief_ref has no SITEZ-resolvable, admitted-shape target (`4.0.0_SA_CRO~Z`, msg 23171).

---

## Current State

POSN_AGGFIX is registered under `org/missions/D4/POSN/POSN_AGGFIX/` at dep_stage REGISTERED, drained into SITEZ at
`d5e068cde4` (LOCAL). Its endpoint FWD-1..FWD-8 sits in this seat's deliverables, emitted and not confirmed, and is
with Andrew through `0.0.0_AB_MSTR~Z`. No PRD exists. The inbox Monitor is armed and caps at 30 minutes, so it is
re-armed on each expiry notice. No loop is armed.

---

## Next Steps

1. **[Andrew, via 0.0.0_AB_MSTR~Z] Confirm or change each DONE WHEN line and answer D1-D4** -- unblocks L4.
2. **[1.0.0_SA_CTO~Z] Write `prd/POSN_AGGFIX_PRD.md` the turn his word lands** -- PRD_HEADER, the endpoint section
   verbatim as confirmed, arc, surface manifest; then the L4-R halves route to `3.0.0_SA_CVO~Z` and `4.0.0_SA_CRO~Z`.
3. **[4.0.0_SA_CRO~Z] Land the brief on SITEZ in an admitted shape** -- so brief_ref resolves at the PRD header.
