# The engine consumes the signed field, and the ruling that governs it turns out to be one grain too coarse — 0.4.0_DS_ClientPlatform~U

**Seat:** `0.4.0_DS_ClientPlatform~U` · **Window:** 2026-08-27T17:55Z – 18:30Z
**TO:** `ADVI_49F.c02-CFINPUT` (face in the historical `~A` folder, re-seated here by its SEATING-EXECUTED block)
**Sequenced under:** `2.0.0_SA_COO` 76133 TO 2 — no new GO; gate `c01-SIGNFIELD` SATISFIED and ACCEPTED COMPLETE (76286)
**Commit:** `cab1f8bff9` — LOCAL (ls-remote read). **Deliberately NOT deployed.**

## Objective

`c02_twr_engine` consumes the new signed in-kind field, and its class filter becomes a function
of the boundary grain rather than a constant. Row selection only — the linking method is not
impeached and is not touched.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-pipescript deployed | `c02_twr_engine --pipeline advi` | **STALE — and that is CORRECT** | Run deliberately as a *negative* confirmation: c02 is committed and NOT deployed, so STALE is the state CF-4 requires. Recorded with a caution for the eventual post-deploy verifier: `c02_twr_engine.py` is **CRLF** in the tree while `c00`/`c01` are **LF**, so a post-deploy STALE must be resolved by normalised content compare before it is believed. |
| commit-gate | 2 files | PASS | py_compile + ds-precommit + ruff py39. |
| safe-commit | `-F` msgfile, non-shell writer | PASS | msg-verify MATCH len=5133. |
| (no comp-blast) | — | not re-run | Its graph was still serving the timed-out stale snapshot measured at 16:4xZ; re-running the same degraded instrument would be repetition, not corroboration. The flow_ledger consumer set was already enumerated at source this session and CTO 76200 verified it independently. |

## Work Completed

### 1. `flows_from_ledger` reads the signed field, and refuses a ledger that cannot supply it

`signed_amount` is `0.00` on every IC row **by design**, so reading it alone is the whole of
defect 1: the transferred value reaches the return as zero flow while the securities land in
ending market value, and the transfer is rendered as *performance*. A pre-1.2 ledger is refused
loudly rather than silently reproducing the defect.

### 2. The class filter as a function of grain

`--flow-boundary {account,relationship}`; account grain neutralises `EXTERNAL`+`INTERNAL`,
relationship grain `EXTERNAL` only. Per Rule 24(iv) the emitted `twr_daily` carries
`flow_boundary` on its face and the manifest carries a full `cf_input_census` — every ledger row
the filter refused, counted **by the reason it was refused**, so "excluded" is never read as
"worth nothing".

### 3. Acceptance — the pre-registered all-ten table

**8 of 8 TESTABLE rows PASS.** `0032486794` +69,056.00% → +0.00%; `0050000151` +310.73% →
−0.00%; `0066766188` −100.00% → +0.00%; `0048403874` −100.00% → −0.38%; `0049284242` −99.84% →
−0.67%; `0016371483` −99.27% → −0.26%; `0042335575` +157.80% → +0.08%; `0012942467` +108.58% →
−0.12%.

## Decisions Made

| Decision | Rationale |
|---|---|
| **Commit but do NOT deploy** | CF-4 routes the served-semantics change P4-class through CTO. Deploying on my own gate is the silent re-statement CF-4 exists to prevent. |
| Admit `INTERNAL` only where provenance established a **different-account counterparty** | A transaction code is not a counterparty. The same logic that excludes `same-account-type-transfer` (intra-account by construction) excludes `code-rule`. Implemented as one named frozenset — reversible in one line whichever way CTO rules. |
| Escalate the provenance fork rather than decide it | The ruling is at class grain; the code must be written at provenance grain, and $214,155.29/day rides on the difference. "Never stop at a fork" — so I implemented the conservative arm, shipped nothing, and routed it with numbers. |

## The thing I got wrong, and what it changes

**I reported 9 of 10, then 8 of 8, and the second number is the honest one.** My first harness
scored `0013289888` and `0057178995` as PASS. Both sat near zero *after* the fix — but they also
sat near zero *before* it, because neither carries its registered outlier on this partition;
their outlier dates are elsewhere. Both arms rested on the same truth, so the check had nothing
to discriminate and its pass meant nothing. A testability gate now requires the PRE arm to
reproduce the registered **emitted** value before a row counts as evidence.

**And a correction to my own root-cause doc that changes what defect 1 IS.** I wrote that c02's
docstring "states the defect as the design". It does not — it states the *correct* design and
always has. I quoted line `:19` and stopped at the line break; the sentence continues onto
`:20-21` with *"+ signed in-kind values on EXTERNAL in-kind legs"*, present in **5 of 5 commits**
since `a781ae9b5d` (2026-08-11). So this is not a wrong design faithfully implemented — it is a
right design whose second clause was never written. This change *restores* the module's own spec.

## Blockers

**Three, all genuinely at other seats or gates — named rather than implied.**

1. **CF-4** — the P4 gate is `1.0.0_SA_CTO`'s. Deploy held.
2. **The provenance fork** — `1.0.0_SA_CTO`'s ruling (76323, routed with issuer context by COO 76327). CF-3's full-scope *population* changes with the answer.
3. **CF-2** — `4.0.0_SA_CRO~A`'s matched-window harness is their instrument; the one sanctioned CRO cc fires at harness-verified, not before.

## Current State

`c02-CFINPUT` is at **implemented-stage ACCEPTED** (COO 76327, stage-scoped — the TO stays open
and I have not flipped its status). Not deployed. `P14-VEHICLE`'s V14-3 gate now waits on c02
alone, so this fork is the head of the critical path.

## Addendum 18:2xZ — the fork RULED before this log was committed, so blocker 2 is closed

Written into the log rather than left to age: `1.0.0_SA_CTO` 76329 **ruled the implemented
reading STANDS** — `INTER_ACCOUNT_PROVENANCE = {pair-match, text-counterpart}`; code-rule
INTERNAL is not admitted on the code alone, cash or in-kind. The grain rationale as ruled: 74122
binds transfers whose inter-account character is **established**; route (a) is excluded because
it measurably never crosses, route (b) because *nobody knows* whether it crosses, "and a filter
must not encode a guess as a measurement."

Two consequences already in motion: **CF-3 full scope is unblocked and running** on the ruled
population; and **CF-3b** is cut on my face as a NON-GATING sub-item (COO 76335) — a cross-account
pair-scan that graduates code-rule in-kind legs through the *existing* pair-match provenance, so
zero new principle and the one-line mechanism is untouched. Expected criteria widened
`CF-1..CF-5` → `CF-1,CF-2,CF-3,CF-3b,CF-4,CF-5` by issuer amendment.

The residue is now a **reporting obligation**, not a silent exclusion: unestablished rows stay
refused-by-reason in the census, and the P1.5 re-grade report carries their per-day dollar size
**with its denominator**, so Andrew makes the serve read with the number in view.

## Next Steps

1. CF-3 full scope on the ruled population — sweep running, residual dollars captured per day.
2. CF-3b pair-scan (non-gating), sequenced at my judgment.
3. CF-2 (CRO~A's harness) → CF-4 (CTO P4 gate) → CF-5 proof instance over the widened id set.
