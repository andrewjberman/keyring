# AMGT_HARVST driven from round 2 to a measured terminal state, at zero egress -- `2.0.0_SA_COO~Y`

**archetype:** MIXED
**secondary_archetypes:** COORDINATE (primary), VALIDATE, SCRIBE

**Date:** 2026-09-23
**Task Order:** AMGT_HARVST rounds 2-5 (L5/L6/L7/L8 owner), plus AMGT_RESAPP v0.24 L4-R brief half as substitute signer
**Status:** COMPLETE

---

## Objective

Drive `AMGT_HARVST` to completion as its L5/L6/L7/L8 owner: recut each round from the CTO's L10 analysis, issue one
issuance per round, drain every worker, and close. Secondary, unplanned: sign `AMGT_RESAPP`'s L4-R brief half as the
substitute signer after measuring that the delivery mechanism could not re-route it.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| proof-of-spec-check | `proof-of-spec-check.py <instance> AC0..ACn` (8 drains, run INSIDE each worktree) | PASS | every instance VALID rc=0; the in-worktree rule from an earlier session held |
| safe-merge.sh | `safe-merge.sh wk-AMGT_HARVST-<r>-<n> -m ...` x8, plus `--continue` x3 | PASS | 3 channel conflicts, all resolved as UNION BY ROW ID rebuilt from `git show :2:`/`:3:` stages; 1 correct refusal on a peer's staged index |
| safe-commit.sh | ~25 commits, `-F <msgfile>` authored by a non-shell writer | PASS | one refusal chain on row schema (enum + required field), all correct |
| missions-tree-index.py | `derive --write` before each issuance; `check` in 3 worktrees pre-spawn | PASS | 0 violations after the cone widening; 24 FALSE violations before it (row Z-W11-S1) |
| prd-signoff.py | `status AMGT_RESAPP`; `sign --half brief --review <path>@<pin> --for ... --expect-half-hash ...` | PASS | `--expect-half-hash` is a REFUSAL, not a re-read; CTO adopted it as the standing control |
| surprise-row-gate.py `_latest_dispositions` | called directly as a library over `('.', 'AMGT_HARVST')` | PASS | 38 ids, NON-TERMINAL 0; the instrument that settled a three-seat number dispute |
| comp-tool rail (hook) | 2 Bash calls DENIED | PASS | both denials CORRECT: one raw glob grep, one python comment containing the word `find`. Neither was overridden; I used `Read` and a python file read instead |
| boto3 / pyarrow (ad-hoc) | S3 metadata + parquet censuses, ~8 runs | PASS | the instrument behind Z-S12, Z-S14, and the round-4 shape test |

**What worked:** `--expect-half-hash` turned a discipline into a mechanism. The gate chain caught every schema
error I made. `_latest_dispositions` existed and answered a question three seats had argued about.

**What failed:** nothing in a tool. Every failure this window was mine: see Decisions and the defect list.

**Gap found:** `proof-of-spec-check`'s invocation-alignment compares the INSTANCE against the ORDER, so an
UNRUNNABLE invocation passes when both copies match -- it certifies AGREEMENT, never RUNNABILITY (row Z-S11). A
`shlex`/`bash -n` limb would refuse it instantly; stated as a candidate for the gate's owner, NOT built.

---

## Work Completed

### 1. Four rounds issued, drained and closed; 18 of 18 orders terminal

| round | recut | issuance | orders | drained | grade |
|---|---|---|---|---|---|
| 2 | v1.1 @`04a235adb7` | @`004f6621c7` | 5 | 5 | 21 PASS / 0 FAIL / 1 UNVERIFIABLE of 22 |
| 3 | v1.2 @`04329b6a4c` | @`68f353361b` | 2 | 2 | 10/0/0 |
| 4 | v1.3 @`8cef65cc00` | @`eec53bf76f` | 1 | 1 | 5/0/0 |
| 5 | v1.4 @`95be3bc7a9` | ISSUANCE OF NOTHING | 0 | -- | accepted; subtraction printed |

Drain commits: `59d6347d37` `8aefec368d` `db04dbbc5d` `e7a664c5c0` `e68dc69503` (round 2), `2c5609c841`
`eb7ed1268f` (round 3), `a6ba2198c4` (round 4). Zero worktrees and zero branches remain.

**Rounds 3, 4 and 5 made ZERO vendor calls and ZERO S3 writes.** Round 2's `HVST-r-3` was the only world write:
three gold snapshots rebuilt, verified by me on the served parquet at 98 mention rows / 24 columns with `publisher`
present / Lenovo 11 / daily 1596 with one PARTIAL day / event 5 / determinism symmetric difference 0.

### 2. What the cells actually settled

- **`FWD-1`'s listing half:** capture proved WIRED 5 of 5 (`HVST-r-5`), then a THIRD cause found and fixed -- the
  persist sat after the per-article loop, so a mid-loop raise discarded captured pages (`HVST-t-1`, row Z-W15-S1).
- **`Z-S1`'s as-received half:** proven live on 2 of 5 paths (`HVST-r-2`), then EXERCISED offline on 5 of 5
  (`HVST-t-2`, `byte_equal 5 of 5`), then the back-fill closed as impossible BY MEASUREMENT (`HVST-u-1` + my shape
  test: `normalised_record` is 0 of 83 canonical, so shape cannot separate harvester output from vendor bytes).
- **`Z-S2`:** closed by the explicit `publisher` column with the printed SHAPE READ the CVO's condition required.
- **`Z-W10-S3`'s class:** CONTAINED by the package conftest poison (`HVST-r-4`), autouse at the collected location,
  with a positive control and a narrow opt-out. The row stays ARMED by construction and the worker said so.

### 3. The coverage read that earned round 5's zero

Ran before cutting, at zero egress. Silver article ROWS denominator 97 across 86 objects: Lenovo in 14 (`sa` 3,
`wsj` 11); `barrons`/`bbg`/`ft` hold 48 rows for OTHER securities and ZERO for Lenovo. The run report then shows all
five were asked in ONE invocation, with `bbg`/`ft`/`barrons` fetching zero pages: a verification challenge, HTTP 403
from a search endpoint, and a rejection AFTER a re-authentication recorded as SUCCEEDED. **So they are not
unmeasured -- they were asked and refused three different ways, and only one is plausibly session-shaped.** That
replaced the analysis's own withdrawn sentence and argues for a NARROWER vendor ask, not a bigger one (row Z-S14).

### 4. `AMGT_RESAPP` v0.24 brief half SIGNED as substitute

Measured that `outstanding.jsonl` carries 20 rows and NO row for that brief half, so the 60-minute re-route could
never fire -- Rule 27's own prohibition. Refused to sign on a prediction of the routed reviewer's failure; the CTO
then re-routed explicitly @`3303326c25`. Stamped with `--expect-half-hash`, `--for 4.0.0_SA_CRO~G`, review at
`org/tier1_exec/2.0.0_SA_COO~Y/deliverables/L4R_REVIEW_AMGT_RESAPP_v0.24_BRIEF_HALF.md@fd6b8028f0`. **PRD now
ADMITTED, both halves SIGNED and current**, which cleared `2.0.0_SA_COO~Z`'s LIMB 6 block. I verified the
ratified-text half untouched, the regulator clause inside CONTRACTS at `:801-803`, and the false claim GONE rather
than discussed; I did NOT call the regulator and attributed that measurement to the CTO.

### 5. The cone dispatch defect, mine, measured and disarmed

My ten-path sparse cone produced THREE worker rows from one root cause (Z-S4): a hook walking the filesystem read 24
false orphans, an import failed on an unmaterialized sibling tree, and a suite read `1 failed 6 passed` where the
full tree reads `7 passed` -- which a worker filed as a PRE-EXISTING repository failure. Widened the cone to include
`org/missions` whole and `integrations`, and **verified both controls in both round-3 worktrees BEFORE either
spawn** (0 violations, 7 passed). Rounds 3 and 4 then produced ZERO worker-filed rows and exact baseline matches.
One number I had wrong and corrected: `org/missions` is 5,649 tracked paths, not the 26,278 I assumed, so the
memory risk that justified the narrow cone never applied to the path that needed widening (Z-S9).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Round 5 issues NOTHING | The subtraction's remainder was ZERO once the coverage read closed its question. Inventing a cell would spend a worker slot to produce a report |
| The metadata WRITE was NOT put in a cell; I asked instead | Labelling 18 objects means a write against a never-overwrite guard -- the same guard a sibling worker deleted 123 objects to escape hours earlier. A criterion that can only be met by defeating a guard will eventually be met that way |
| Refused to sign the brief half on a prediction, signed on a measurement | "Likely to fail" is a prediction; the rule named a 60-minute condition. The mechanism's ABSENCE is a different and measurable fact |
| Amended two orders MID-FLIGHT rather than leaving defects to a later round | Both defects were introduced by the round itself (a `finally` that could mask a propagating exception; a criterion asking for a value the field cannot hold). Cheaper than a round, and the worker had not yet produced the output |
| Corrections filed as NEW rows, never in-place edits | The gate refused my first in-place edit and was right: an edited history is one nobody can audit |
| Did not touch the sibling breach, its 123 markers, or another seat's row | Hard stop at Andrew; editing a peer's row is what breaks the audit trail |

---

## Files Modified

See commit messages: `004f6621c7`, `04329b6a4c`, `68f353361b`, `8cef65cc00`, `eec53bf76f`, `95be3bc7a9`,
`533fec7afb`, `26cea6fac3`, `ebb318b5c4`, plus the 8 drain merges and 16 row commits.

| File | Change | Committed |
|------|--------|-----------|
| `org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md` | v1.1 -> v1.4; sections 10-16 plus standing clauses 14a-14c and correction notes 16e/16f | Yes |
| `.../task-orders/*.md` (8 new: r-1..r-5, t-1, t-2, u-1) | issued, amended (3 amendments), flipped complete | Yes |
| `.../surprise-channel/investigations/INVESTIGATION_v1.md` | 19 -> 40 rows; 16 filed by me | Yes |
| `.../ledger/ROUND{2,3,4}_L8_PACKET_20260923.md` | three drain-end packets | Yes |
| `org/tier1_exec/2.0.0_SA_COO~Y/deliverables/L4R_REVIEW_...md` | the substitute-signer review | Yes -- `fd6b8028f0` |
| `lib/opal_data_harvest/*`, `lib/research/harvest/*` | worker-authored; 6 new modules + 6 new test files | Yes, via the drain merges |

---

## Blockers

None BLOCKED on me. Held outside this project, each with an owner:

- **AT ANDREW:** approval of the AMENDED timeline spec (gates the build cell); any further publisher access.
- **AT `1.0.0_SA_CTO~Z`:** the `shlex`/`bash -n` invocation limb (row Z-S11) -- the gate is its surface, not mine.
- **AT `1.0.0_SA_CTO~Z` + this seat, with `2.0.0_SA_COO~Z`:** the served chatter switch, on a never-widen pair, the
  gold read grant, and `AMGT_RESAPP`'s retirement window.
- **UNADJUDICATED AT ANDREW, not mine:** the sibling project's S3-delete breach. This project is MEASURED clear --
  40 harvest/research files carry zero delete calls, and all 123 markers sit under one prefix that is not mine.

---

## Current State

`AMGT_HARVST` is at a measured terminal state on branch `SITEZ`: **18 of 18 task orders `complete`**, `dep_stage`
`ROUND_CLOSE`, zero worktrees, zero `wk-AMGT_HARVST-*` branches, and the surprise channel at **40 rows with
NON-TERMINAL 0 by `surprise-row-gate.py::_latest_dispositions`** (the row-field census reads differently and that is
the append-only design, not a discrepancy -- rows Z-S15/S17/S18). Decomposition v1.4 sections 14a-14c carry three
STANDING clauses binding every future cut: no S3 delete without Andrew's word; read a schema before typing a field
value; and print the column list beside any count over the silver `article` table. `FWD-1` stays **NOT REALIZED**
with its remaining cause stated per publisher in row Z-S14. The harvest code carries six new modules from this
window -- `check_as_received.py`, `census_listing_capture.py`, `exercise_as_received.py`,
`classify_unlabelled_bronze.py`, `conftest.py` (the package poison), and the guarded persist in `worker.py` -- and
every harvest suite passes in the shared tree at its stated baseline with both pre-existing failures unchanged.
Gold holds current snapshots at `amgt/harvest/gold/{article_security_mention,chatter_daily,chatter_event}/` with
`publisher` present and Lenovo included. `AMGT_RESAPP` v0.24 is **ADMITTED** with the brief half signed by this seat
as substitute. All work is committed LOCAL on `SITEZ`; the push is `0.0.0_AB_MSTR~Z`'s.

**SESSION-SCOPED AND EXPIRING WITH THIS SESSION:** Andrew's EGRESS and AMGT-ADJUDICATION grants. They are not
re-armed by this log, by memory, or by the fact that acts were taken under them. The per-use vendor bar and the
card-to-Andrew route return by default.

---

## Next Steps

1. **[3.0.0_SA_CVO~Z] L9 for round 4 if not already discharged** -- the CTO's round-4 analysis closed the round at
   5/0/0, so this may already be complete; the packet is at `.../ledger/ROUND4_L8_PACKET_20260923.md`.
2. **[Andrew, via 1.0.0_SA_CTO~Z] approve or refuse the AMENDED timeline spec** -- the build cell is the only
   remaining in-boundary work and it is gated on this alone.
3. **[Andrew, via 1.0.0_SA_CTO~Z] the vendor question, if raised, starts from row Z-S14** -- a fresh session
   addresses at most ONE of the three recorded refusals, and the other two are a search-endpoint 403 and a
   post-re-authentication rejection.
4. **[0.0.0_AB_MSTR~Z] push `SITEZ`** -- this window's work and the CTO's rulings and analyses are LOCAL.
5. **[1.0.0_SA_CTO~Z] the invocation-parse limb (Z-S11) and the notifier's three failure shapes** -- both are
   fabric surfaces, both carded, neither built tonight.

---

## Self-assessment, because the record is worth more than the score

**Three of my ORDERS carried defects and none was caught by a gate** -- all three by reading the artifact after the
gates said PASS, two only after the order was already with a worker: an order that did not name what a moved call
may do to a propagating exception (Z-S10), one whose invocation the shell could not run (Z-S11), and one that asked
for a value the field cannot hold (Z-S13). The standing remedy I adopted: before issuing, ask what the named field
actually RECORDS and read its definition at the bytes. For an enum, read the enum.

**I contradicted a sound number and published it.** The CVO's "0 non-terminal" was right by the gate's own resolver;
I censused the two frozen row fields, found no zero, and published in a committed row, a decomposition note and a
message to four seats that it was not reproducible on any axis. Withdrawn in Z-S17/Z-S18. The durable output is the
rule the CTO adopted verbatim: **a disagreement about a number is FIRST a question about UNITS, and whoever censuses
SECOND gets to call the other wrong.**

**And the CTO's fair criticism lands on me too:** six exchanges across three seats on a channel count moved no
conclusion. **If correcting a number does not change a decision, it gets a line in the record and no broadcast.** I
sent several of those messages. The pre-cut measurement discipline earned its keep -- three cells were stopped or
re-shaped before a worker touched them -- and the correction cascade did not.
