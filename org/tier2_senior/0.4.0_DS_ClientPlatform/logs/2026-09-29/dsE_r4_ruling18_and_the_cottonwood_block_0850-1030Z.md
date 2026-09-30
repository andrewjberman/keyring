# Ruling 18, and the law collision that stops Cottonwood — 0.4.0_DS_ClientPlatform~E

**archetype:** MIXED

**Date:** 2026-09-29, 08:50–10:30Z
**Task Order:** `IRPT_BCKEND.TO-IB-er-401` (round 4) — still `pending`
**Status:** `E4-AC3` **PASS** (step 0, the gate on the adapter switch). `E4-AC1` / `E4-AC2`
**NOT CLAIMED** — blocked on a registry row, row `IRPT_BCKEND-S203`.

## Objective

Step 0 first: implement PRD v0.21 ruling 18 (the trading day after an `IMPLAUSIBLE-RETURN` day is
itself NOT COMPUTABLE) and re-emit the 49F and Inflection gold, because the adapter switch waits
on it. Then build the Cottonwood channel.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| naming-gate.py | `--diff` on 4 synthetic new-file diffs | **REFUSE x4**, then PASS on `z09` | Used as a MEASUREMENT instrument, not just a gate — see Decisions. |
| surprise-row-gate.py | on the channel file | BLOCKED, then clean | My row used `class: "BLOCKER"`; the enum is `['OBSERVATION','BLOCKING']`. |
| deploy_ledger.py | `close-leg` x3, `hold` | L1–L3 closed; **hold REFUSED** | "a half-landed deploy cannot be HELD" while an apply leg is open. |
| commit-gate.sh | on both `.py` files | clean | py_compile + ds-precommit + ruff py39. |
| head_bucket / list_objects_v2 | on the COT gold prefixes | 0 objects, control 557 | Proves L4 never started. |

**What worked:** grading a *synthetic* declaration with `git diff --no-index -- /dev/null <trial>`
turned the naming gate from an obstacle into an instrument. Four candidate carriers were tested in
about five minutes, which is what let the blocker be reported with a printed denominator and a
working alternative instead of "Cottonwood doesn't fit".

**What failed:** after the first refused `safe-commit`, the bad bytes stayed in the **index**, so
re-running the row gate against the corrected working tree kept printing the old violation.
`git show :<path>` is what showed the split. Cost one cycle, and it cost another seat one too.

**Gap found:** no tool answers "which registry keys resolve to scope X and which of them would
survive the naming gate". That question is the whole of this blocker and I answered it by hand.

## Work Completed

### 1. Ruling 18

A sixth status, `FOLLOWS-DISCONTINUITY`, applied to a row that would otherwise read OK when the
account's previous trading day was `IMPLAUSIBLE-RETURN`. It does **not** cascade (only an
`IMPLAUSIBLE-RETURN` day triggers it) and never overwrites a row that already carries its own
named reason — that reason is the more specific statement about the day.

Mechanism: `ImplausibleIndex`, a memoised `(source, day) -> accounts` lookup. It is the only rule
in this producer that reaches across days; recursion terminates because `_frame_for()` grades
ruling 16 only, so asking for D−1's implausible set cannot ask for D−2's. The memo is what kept
the cost off 2x — 49F ran 1,832 cache hits against 1,508 misses.

| Re-emit | Result |
|---|---|
| 49F 2024-07-09..2026-09-25 | 557 of 557 days, 3,188,339 rows, 0 not computed |
| INF 2020-04-27..2026-09-25 | 1,609 of 1,609 computable days, 1,420,782 rows, 4 ABSENT and named |
| Rows flipped | exactly **2**, both 49F (2025-12-15, 2025-12-18) |

`E4-AC3 PASS`: 49F 2 `IMPLAUSIBLE-RETURN` rows / 0 follow-day violations; INF 0 / 0.
..0090 went −91.5% → **+10.2%**; ..4714 went −69.8% → **−65.4%**, over **226** OK days against
..0090's 249 — flagged to the issuer, because ruling 18 removed the reversion but did not make that
account's series complete.

### 2. The Cottonwood rules (everything not depending on the key)

- **Price by derivation** — `price_of()` reads a declared `price_column` when there is one and
  otherwise derives value/quantity. Selected **structurally**, so it is a declaration shape and
  never a firm branch.
- **The zero-`Units` trap** — absent *or zero* quantity yields a NULL price (ruling 4's
  price-missing). Measured: 1,605 of 19,784 rows carry `Units == 0`; a bare division would have
  handed each an infinity.
- **The text cash flag** — `Cash Equivalent` arrives as `'true'`/`'false'`, and `astype(bool)` on
  `'false'` is **True**: every holding would have become cash, every account would have read
  0.00%, and nothing would have raised. `_flag()` REFUSES an unparseable value.

45 tests pass (was 41). The 49F and INF paths are untouched — all 41 prior tests pass unchanged.

## Decisions Made

1. **I stopped rather than working around the naming limb.** PRD v0.19 ruling 1 and LGIC_ENFORCE
   DEC-6 have no common satisfying move for Cottonwood. Four carriers graded, all REFUSED: the
   entry key, `registry_key: cottonwood`, the registry's own bucket for the firm, and the `F-COT`
   tenant code the registry publishes and `lookup()` resolves. The gate's remedy on each is
   `lookup()`, permitted only in Python — the code branch ruling 1 forbids.
2. **I did not take the structural dodge that was available.** Under `blackdiamond`, 49financial
   has masters and cottonwood has none, so "the master-less blackdiamond scope" would have
   selected it with no token anywhere. I rejected it: that encodes an accident of the current
   registry as a firm's identity, which fails rule 24 (iii) — the axis would be "has masters",
   not identity. Rule 30 says a builder refusal **is** a missing registry row.
3. **I converted the blocker into one actionable row.** Black Diamond issues a firm-instance
   prefix: 19,784/19,784 COT account ids are `z09`, 6,202/6,202 49F are `z08`, zero overlap, and
   `registry_key: "z09"` grades NAMING-GATE **PASS**. Only `lookup('z09')` is missing.
4. **The ledger stays RED deliberately.** L4 was never started — 0 objects under both COT
   prefixes against a 557-object positive control — so nothing is half-landed. `hold` is refused
   while an apply leg is open, so the deliverable record is the loud escalation NEVER-2 asks for.

## Files Modified

| File | Commit |
|---|---|
| `holdings_performance.py` (ruling 18) | `bf1683f172` |
| `holdings_performance.py` + tests (the COT rules) | `e79dd684bf` |
| `surprise-channel/.../INVESTIGATION_v1.md` (row S203) | `b88b92c57b` |
| `deliverables/.../TO-IB-er-401_STEP0_DONE_COTTONWOOD_BLOCKED_20260929.md` | `66bc8e5003` |

**Workspace CLOUD commit:** merged `7e8a32fe21`. Push state: LOCAL — `git ls-remote origin CLOUD`
read `15655f4a25` at 10:20Z; `CLOUD` is pushed by `0.0.0_AB_MSTR` only.

## Blockers

**One, owned elsewhere.** `E4-AC1` / `E4-AC2` need a registry row resolving a non-token key to the
Cottonwood scope. `infra/logic/registry/` is outside this order's `<paths>` grant, and the order's
own refusal clause names "a missing registry row" as a stop condition. Row `IRPT_BCKEND-S203`
(class BLOCKING, INERT, `disarm_owner 1.0.0_SA_CTO`), ask routed to `2.0.0_SA_COO~P`.

**A mistake of mine, fixed within the cycle:** row S203 was first filed with `class: "BLOCKER"`,
which is not in the ratified enum. Because the channel is append-only and shared, that refused
*every* seat's commit of the file — `0.6.2_AE_PartnerETL~S` was holding row S202 behind it and
messaged rather than taking the override. Corrected to `BLOCKING` and committed; I passed back the
index-vs-working-tree detail that had cost me the extra attempt.

## Current State

Step 0 is delivered and the adapter switch's gate is green. The Cottonwood channel is one registry
row away: the rules, the traps and the tests are all built and merged, so when
`lookup('<key>')` resolves, the entry is about six declared fields and the run is one command.

## Next Steps

1. **[`1.0.0_SA_CTO`]** Add the registry row — `z09` → `cottonwood`, parallel to
   `08335338` → `49financial`. Or, better for the class, admit the declaration's `registry_key`
   field as a permitted `lookup()` context in LGIC_ENFORCE, which stops this recurring at the next
   firm that shares a monolith and has no master.
2. **[`1.0.0_SA_CTO`]** Separately and smaller: the Cottonwood registry row's alias note says
   *"opal-data-cottonwood does not exist yet"*. Measured with `head_bucket` — it exists and is
   reachable. That note is stale.
3. **[`2.0.0_SA_COO~P`]** The adapter switch. ..4714 still serves −65.4% over 226 of ~250 days;
   worth deciding whether the page may serve a chain that partial before it does.
4. **[`0.4.0_DS_ClientPlatform~E`]** BLOCKED. On the row landing: declare the entry, run
   2026-06-10..2026-09-25, grade E4-AC1/E4-AC2, close L4/L5, write the proof.
