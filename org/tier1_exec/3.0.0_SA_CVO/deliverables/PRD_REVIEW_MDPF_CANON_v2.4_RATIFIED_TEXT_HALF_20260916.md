# PRD review -- MDPF_CANON v2.4, ratified-text half (ENDPOINT + CONTRACTS)

Reviewer: `3.0.0_SA_CVO`. Delivered by `1.0.0_SA_CTO` msg 97518 (executed record 97523).
PRD: `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md` @ `ef899e790f`, ratified-text half_hash `5c03134b9dda`.
Previous signature: v2.2 @ `ef21e34660`, half_hash `d5177552975d`.

## VERDICT: REFUSE -- the correction fixed gold and left the same defect on `state`, one clause later in the same row

## What changed (measured)

| commit | ratified-text | brief |
|---|---|---|
| ef21e34660 (v2.2, signed) | d5177552975d | 8a3ec329c64f |
| 8d12b77adb (v2.3) | d5177552975d | a0737dee5352 |
| ef899e790f (v2.4) | **5c03134b9dda** | d5b30fb957da |

The ratified-text diff is ONE line: CONTRACTS `:177`, the key-string row. The gold instance is now
"the address `address("mdpf", {scope}, "gold", {artifact}, "date=...")` returns under R7".

## What passes -- gold, checked by calling the builder, not by reading the row

`lib/opal_naming.py address("mdpf", scope, "gold", "aum_metrics", "date=2026-09-15")` in this worktree:

| scope | gold address |
|---|---|
| 49financial | `s3://opal-data-49financial/mdpf/49financial/gold/...` |
| inflection | `s3://opal-data-inflection/mdpf/inflection/gold/...` |
| cottonwood | `s3://opal-data-cottonwood/mdpf/cottonwood/gold/...` |
| global | `s3://opal-data-mdpf/mdpf/global/gold/...` |
| demo | `s3://opal-data-demo/mdpf/demo/gold/...` |

Every bucket the row names matches the builder. The row no longer types a gold bucket. Andrew's call-3
words match his record @ `50d1b9403e`.

## DEFECT 1 -- the `state` instance in the SAME row is still typed, and wrong for four of five scopes

The row still reads: *state `s3://opal-data-mdpf/mdpf/{scope}/state/...` (R21)*.

The builder over the same five scopes, tier `state`:

| scope | builder returns | row types |
|---|---|---|
| 49financial | `s3://opal-data-49financial/.../state/...` | `opal-data-mdpf` -- WRONG |
| inflection | `s3://opal-data-inflection/.../state/...` | `opal-data-mdpf` -- WRONG |
| cottonwood | `s3://opal-data-cottonwood/.../state/...` | `opal-data-mdpf` -- WRONG |
| global | `s3://opal-data-mdpf/.../state/...` | agrees |
| demo | `s3://opal-data-demo/.../state/...` | `opal-data-mdpf` -- WRONG |

The row's own citation says the same thing as the builder. R21 (`infra/logic/02_DOCTRINE.md`) puts state
*"in the bucket whose tenancy the state belongs to"*, and Rule 30 homes *"firm-attributable gold, platinum
and `state/` in the FIRM bucket"*. **So the row cites R21 for an address R21 contradicts.** This is the
defect class of 97324 exactly: a typed instance beside a builder mandate. It survived because the cure
was scoped to the word "gold".

**CURE:** state the state instance the way the gold instance now reads -- the address `address("mdpf",
{scope}, "state", ...)` returns -- never a typed bucket. Also check the row's other typed instances
against the builder in the same pass. Bronze (`opal-data-assets`) and the firm platinum slice
(`opal-data-{firm}`) agree today, but they are still typed, and an instance that agrees only today is the
next one of these.

## DEFECT 2 -- history and a seat reference inside CONTRACTS

The new clause carries *"this replaces the typed `s3://opal-data-mdpf/mdpf/{scope}/gold/...` instance that
contradicted the same sentence's builder mandate, the CVO's finding"*, and *"measured at HEAD"*.

- The first is revision history plus a seat reference -- the bar in every L4-R delivery, and the one I
  refused NFRA_OPLGTW v0.3 on an hour ago.
- "measured at HEAD" is a vintage with no commit. The measurement is also unnecessary, because the row
  defers to the builder.

Andrew's quoted words may stay; they are the source.

**CURE:** move the "replaces ... finding" clause to the header change note or the rulings record; drop
"measured at HEAD".

## Outside this half -- carriers the correction missed (not a condition of this verdict)

A census of `opal-data-mdpf` and `/state/` across the whole PRD @ `ef899e790f` finds typed gold and state
homes still in the BRIEF half and the title. Rule 22: count every carrier of the corrected property.

- `:1` title: *"gold as dated parquet in opal-data-mdpf"*
- `:359` the new-surfaces table: `s3://opal-data-mdpf/mdpf/{scope}/gold/` and `.../state/`
- `:423` the blast-radius table: the same pair

`:343` (M2) was corrected. These three were not, so the brief half now disagrees with CONTRACTS on where
firm gold lives. The brief half re-opened on its own hash (`d5b30fb957da`), so `4.0.0_SA_CRO` will read it.
This is named here so that read is not scoped to M2.

-- 3.0.0_SA_CVO

---

## ADDENDUM (after `4.0.0_SA_CRO` msg 97531) -- DEFECT 3, on the ENDPOINT this seat owns

`4.0.0_SA_CRO` named a fact and left its grading to this seat: FWD-1 `:86`/`:91`. Graded here.

FWD-1 at `ef899e790f`:
- headline -- *"every one of them is kept in the one place built for them"*
- ACCEPT -- *"every stored figure of this kind is in the same one place, full history, one addition per
  day -- where today ... the place meant for them is empty"*

**ACCEPT is the checkable bar, and it is singular.** Under call 3 plus R7, as CONTRACTS `:177` now reads, a
correct build puts gold in FOUR buckets: `opal-data-49financial`, `-inflection`, `-cottonwood` for the
firm scopes and `opal-data-mdpf` for global. A grader reading "the same one place" literally FAILS that
correct build. A grader reading it as "one place by one rule" cannot tell the correct build from a wrong
one that put every scope in `opal-data-mdpf`. **Neither reading discriminates**, so the bar is defective
on its own terms. "The place meant for them is empty" also names the product bucket's old gold plane,
which is no longer the home for firm figures.

It is the same one-fact-many-carriers class: the gold home is carried by CONTRACTS `:177` (moved), M2 `:343`
(moved), PATHS `:359`, manifest `:423`, title `:1`, coverage row `:389`, and FWD-1 `:86`/`:91` (not moved).

**CURE:** FWD-1's ACCEPT names the rule, not a count of places. For example: *"every stored figure of this
kind is where the one naming rule puts it -- that firm's own bucket for a firm's figures, the product
bucket for the cross-firm composite -- full history, one addition per day"*. The "today" clause must say
what is wrong today without calling one bucket the destination. The headline follows. This is in plain
English and changes what can fail, not what Andrew asked for: his call 3 already made the home per-firm.

On `state/`, which 97531 flags as possibly a second question to Andrew: it is not. R21 is already HIS
ruling (GAP-1, card 5, 09-13 ~01:3xZ), and its text puts state *"in the bucket whose tenancy the state
belongs to"*. The builder returns exactly that. DEFECT 1 applies an existing ruling; it does not widen
call 3.

-- 3.0.0_SA_CVO
