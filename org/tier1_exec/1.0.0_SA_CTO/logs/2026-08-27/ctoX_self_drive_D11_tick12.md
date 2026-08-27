# /self-drive D11 — ticks 11-12 · WAVE 2 CLOSED, THE MATERIALIZER SURFACE MEASURED, ONE CLAIM OF MINE WITHDRAWN

**Driver:** `1.0.0_SA_CTO~X` · **Device:** LAPTOP · **Cadence:** 30m · **Job:** `29b44790`
**state: ARMED** · covering 01:30Z–01:54Z

---

## SCOPE

```
D11 "Substrate Analysis"   device LAPTOP (guard PASS)
  1 project: NFRA_SUBSTRATECARDING   status=active   dep_stage=EXECUTING   open TOs: 0
  denominator: 1 of 12 live directives
WAVE 2 FULLY CLOSED -- all four TO faces complete. 36 cards delivered, 8 subjects / 56 cells SCOPE-SUPERSEDED.
```

**Open calls in scope: 0 adjudicable · 2 RESERVED** (both at Andrew, printed below — a NEVER is not
pitched, and a pace decision is not adjudicable).

## THE MATERIALIZER SURFACE — Andrew's "find the ones that actually matter", measured

Four production-reachable trees, **four different reachability mechanisms**, and the L0 census swept
one:

```
  infra/aws/globgrph/                                 direct module            (the swept tree)
  infra/aws/lambda/globgrph/incremental_updater/      event-triggered Lambda   74281
  org/modules/graph/comp_aws_cli.py  158KB, 79 sites  SYS.PATH INSERTION       74303
  org/tier1_exec/3.0.0_SA_CVO/deliverables/kimi_...   FILESYSTEM-PROBE import  74333
```

⛔ **NO SINGLE SWEEP SHAPE FINDS ALL FOUR.** That is why every instrument tonight — a lane's, mine, the
census's — returned a clean, confident answer about a subset.

**The chain is TWO producers, not three.** `infrastructure-daily-snapshot` was ruled OUT by measurement
(74328): it carries the full describe surface (`ec2 iam lambda events dynamodb s3 sts`) and writes
**0** graph-table references. **A candidate matching on the most distinctive feature and still the wrong
object** — the discriminator was not the client list, it was asking what it WRITES.

**40 candidate graph-writers across seven trees** (74319), predicate **validated against two known
positives BEFORE use** after my first attempt returned 3 and missed a writer I had just read. Stated as
a **DISCOVERY FLOOR**, never a producer count — carried verbatim by the issuer.

**TWO UNTRACKED graph-writers found; `2.0.0_SA_COO~X` swept and found 19 estate-wide, NONE gitignored.**
Their own first sweep returned 7 (`org/**/*.py`) — a true count over a narrower population, caught by
widening before publishing.

## ⛔ ONE CLAIM OF MINE, WITHDRAWN — AND THE SELF-CHECK FOUND WORSE THAN CONTAMINATION

I claimed the C2C3 compose probe **"fails open"** (74333/74336). **FALSE.**
`0.8.0_AE_CloudComp~X` refuted it at source (74338) and **I verified independently** rather than
accepting their read: `c2c3_liveness_acceptance.py` discriminates instance from class grain (`:68-69`),
positive-controls its own predicate, and carries a mutant self-test that **MUST return NOT-LIVE**
(`:29-31`). Withdrawn 74346, struck from wave-3 input.

> **THE REFUTATION WAS THREE LINES ABOVE THE LINE I QUOTED.** `derive_runner.py:1583` — *"NOT SILENT
> ... those are different facts and the harness scores them differently."* I quoted `:1590`. And the
> WARN string **I pasted into my own message** ends *"acceptance will read NOT-LIVE, which is correct."*
> **The sentence disproving my claim was inside my own evidence.**

⛔ **THEN THE SELF-SUBJECT SWEEP FOUND THE REAL DEFECT.** 0 committed artifacts of mine carry the false
claim — but `ORPHANED_BY_THE_MSTR_COO_CVO_CLOSE_20260825.md:211`, **committed by this seat 26 hours
earlier**, states the OPPOSITE correctly: *"a four-way WARN taxonomy ... AUTHORED PRECISELY SO THAT 'no
instance layer' could never be mistaken for 'composition ran and found none'."*

**I had already measured that property, on that function, and stated it right. Tonight I re-derived it
from a smaller sample and did not consult my own record.** `0.8.0_AE_CloudComp~X` caught it in minutes
because it was their subject — **it was mine too; I did not know that when I claimed otherwise.**

> **A contaminated artifact is findable by any token grep. A CORRECT PRIOR FINDING THAT A LATER CLAIM
> SILENTLY OVERWRITES LEAVES NO TRACE ANYWHERE.** Both statements are mine, both in the record, they
> contradict, and nothing joins them. The same shape as the two rule banks — **a claim and its own
> author's prior measurement, with nothing joining them either.**

⚠ Limit stated: token sweep. It would not catch a paraphrase in my own words. Residual real, not zero.

## DRIVER ACTS, ticks 11-12

| act | receipt |
|---|---|
| Triaged the 40 into PRODUCTION / TOOL / LANE / STRAY, two untracked named | 74333 |
| Ruled out the third producer by measurement (checked-clean recorded at equal weight) | 74328 |
| **Withdrew Finding 1**, verified the refutation independently first | 74346 |
| Self-subject sweep of own artifacts + the 26-hour-old contradiction | 74357 |
| **Wave-3 scope settled to the limit of my authority** — population rule, 2 preconditions, card fields | 74353 |
| Adopted `2.0.0_SA_COO~X`'s TRACKED precondition as a carding gate, not hygiene | 74353 |

`2.0.0_SA_COO~X` has wave-3 PREP running with both preconditions `@a07beb06eb`. **No TO cut, no seat
dispatched, no apply — none of that is this loop's act.**

## COMPLETION TEST

**NOT DONE — 0 of 1 complete** (`NFRA_SUBSTRATECARDING: active`). **REACHABLE 1 / UNREACHABLE 0.**
Nothing structurally stuck: wave 2 closed clean, wave-3 prep is live, and the two open calls are
sovereign-class rather than blockers the driver could move.

## RESERVED — AT ANDREW (2 in scope, printed not pitched)

```
+-- CALL 1 of 2 -------------------------------------------------------+
  **Directive home for the materializer inventory: D11, or a new one?**
  D11 is "Substrate Analysis"; "build the canonical materializer inventory" is a
  different INTENT (Rule 24(iii) mixed axis). Same call as D12 for NFRA_C3MATERIALIZE.
  ----------------------------------------------------------------------
  **REC —** Answer once for both. Blocks cutting TOs, not preparing a derivation.
+----------------------------------------------------------------------+

+-- CALL 2 of 2 -------------------------------------------------------+
  **Does wave 3 run tonight?**
  Four lanes have been carding since 21:00Z. Wave 2 closed at 01:0xZ.
  ----------------------------------------------------------------------
  **REC —** His pace call, not mine. I will not convert "surgical mode" into a
  same-night dispatch. Prep continues either way.
+----------------------------------------------------------------------+
```

**Also carried, not D11 scope:** cover-vs-partition · identity grain · two CLAUDE.md fixes ·
vantage-vs-world. Wave-boundary residuals (f) containment · (g) `parts_registered` · (h) rule-bank
join — ratified in direction, none authorized.

⚠ **CARRIER CLAUSE STILL NOT LANDED.** Cron `29b44790` is session-only; **this loop dies with the
session and no successor re-arms it.** Law-file edit held under Andrew's standing instruction.

## Compiler Tools

`.tools/directives-check.py --json` · `aws events` + `aws scheduler` (**both planes**) ·
`git ls-files --error-unmatch` with a positive control for the tracked test · a write-predicate
**validated against known positives before use** · `org/mcp/agent_telemetry/*.jsonl` (four seats all
inside 90s) · `.tools/safe-commit.sh` · **Write tool** for the log and message file after a
`python -c` heredoc died at parse time last tick.

**state: ARMED** · next tick :17
