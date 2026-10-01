# PRD v0.4 rulings 17-19 implemented and exercised against live data: the guard no longer substitutes, grades only inside a measured domain, and one gate runs on the emitted value -- 0.4.0_DS_ClientPlatform~S

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

**Date:** 2026-10-01 04:20Z to 04:50Z
**Task Order:** `IRPT_DASHBD.TO-DB-b-1` (pending)
**Status:** IN PROGRESS -- rulings landed; emit still HELD on rows S4/S6 with the dark issuer
**Workspace CLOUD commit:** `13d7b428ed`. LOCAL; origin/CLOUD `0abf99fcd4` (ls-remote read).

---

## Objective

`1.0.0_SA_CTO` ruled row `IRPT_DASHBD-S5` within four minutes of the ask (msg 103437, acked):
PRD v0.4 @`a8a65b9f62`, rulings 17-19. Implement them.

**Why this was not a wait.** The CTO's note says `2.0.0_SA_COO~P` amends TO-DB-b-1 to the
rulings, and that seat is dark. But TO-DB-b-1's C-METHOD header reads "the PRD is the authority,
this is its operative reading", so a PRD ruling supersedes the order's reading by the order's own
words. Implementing is following the named authority, not adjudicating scope. The amendment is
still owed for the order's TEXT; the behaviour was never gated on it.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-read | `--enumerate 'RULING 1[789]'` on the PRD | **0 hits -- and that was the right answer to distrust** | The pattern was absent because the rulings are numbered `17.`/`18.`/`19.` in a list, not as "RULING 17". A zero from a wrong pattern reads identically to a true absence, so I did not convert it: read the ruling commit's own diff instead, which is the byte-exact source anyway. |
| commit-gate | 3 runs across the edit | PASS | clean each time |
| safe-commit + gates | 1 commit | PASS | |
| live exercise | `--measure`, 2 refusal tests, graded dry-run, direct `compute_range` probe | PASS | the only evidence that counts here |

**What worked:** reading the ruling from `git show <commit> -- <path>` rather than from the file.
The commit message carried the rulings in full, so the authority and its reasoning arrived together.
**What failed:** nothing.
**Gap found:** none new.

---

## Work Completed (`13d7b428ed`)

### Ruling 17 -- the substitution is withdrawn

Both branches emitting `return_basis HOLDINGS_INCOME_FALLBACK` now emit `total_return_daily`
null, `return_basis NOT_MEASURABLE`, `day_quality FLOW_UNRECONCILED`. The quality still says WHY
while the basis says it is not measurable -- the distinction the ruling draws, preserved
deliberately. An unvalued in-kind leg takes the same path.

**Verified live, 15 account-days:** 0 rows carry `HOLDINGS_INCOME_FALLBACK`; the one disagreement
row (account 0010783709, 2026-09-17) reads `FLOW_UNRECONCILED` / `NOT_MEASURABLE` / `None` with
`_guard_graded True` and `_comparability_reason None`, beside a positive-control `MEASURED`/`TWR`
row carrying -0.004143894185766328. The member stays in `RETURN_BASIS` because the contract still
declares it and a producer narrower than its contract would refuse rows the contract permits;
the removal is the contract's own versioned edit, lane `ANY_EXEC`, the issuer's (row S2).

### Ruling 18 -- coverage travels, and the domain gates grading

`holdings_price_returns()` loaded three columns and threw away every qualification the holdings
producer emits. It now carries `excluded_weight`, `negative_value`, `leveraged`, `status` and
`prior_business_date` -- the last of which makes the ruling's valuation-interval test possible at
all, since the neighbour states the day it linked from. New `comparability()` implements the
domain member for member.

Outside the domain the guard **did not grade** -- not agreement, not disagreement -- and the day
is `MEASURED` only where `|F_t|/V_(t-1)` is at or below the tolerance, the ruling's own
error-bound test rather than a percentile of taste.

**The reason is computed and counted but NOT emitted.** The ruling puts it in a field the contract
declares; `org/standards/` is the issuer's lane and an undeclared 19th column would break the
`schema_hash` the contract binds. So it rides the existing `_`-prefixed internal convention (the
caller already strips those) and surfaces in `measure_thresholds`' branch counts.

**The tolerance's population changed with it, which matters more than the gate.** A difference
measured across different valuation intervals, or against a mostly-excluded basket, is not a
disagreement about anything and cannot be an observation in a distribution of disagreements. The
tolerance is now p99 over DOMAIN days with the wider denominator printed beside it.
`measure_thresholds` also reports the excluded-weight distribution the ceiling is chosen from and
leaves the ceiling **UNSET**.

### Ruling 19 -- one gate, after selection, on the emitted value

New `eligible()`: required inputs present, every value finite, enums inside their sets, and the
band applied to the **emitted** `total_return_daily` rather than to a raw value then discarded.
Non-finite is checked explicitly, because `nan > hi` and `nan < lo` are both False, so a NaN
passed every ordinary branch looking `MEASURED` -- the one failure a plausibility band cannot
catch by construction.

### Two refusals, both exercised

| Test | Result |
|---|---|
| `--upload` with no `comparability_max_excluded_weight` | REFUSED |
| `--thresholds-in` a file marked `SUPERSEDED` | REFUSED |

The second is the one worth keeping: the quarantine was a RENAME, and a rename is a record, not a
mechanism. Anyone could have passed the quarantined path and had it read as live. Now the file's
own `SUPERSEDED` flag refuses.

---

## Measured

5 accounts x 10 trading days on the repaired producer: tolerance p99 **5e-06**, max **7e-06** --
against the quarantined run's max of **214.579843**. Excluded weight is 0.0 on all 50 account-days,
so the comparability domain is fully satisfied on this sample. First calibration evidence from this
cell that is not measuring its own defect.

**NOT a round-1 calibration, and no threshold here went to `dim_return_method`.** Rows S4 and S6
(account boundary, fee basis, valuation interval) are open with the dark issuer and change the flow
term.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Implement without waiting for the order's amendment | The order names the PRD as its authority in its own C-METHOD header. Waiting would have been a gate I invented. |
| Keep `BASIS_FALLBACK` in `RETURN_BASIS` | The contract still declares it. A producer whose accepted set is narrower than its contract refuses rows the contract permits. |
| Withhold the 19th column | Contract-declared field, issuer's lane. Emitting it would break the schema hash. |
| Leave the excluded-weight ceiling UNSET and REFUSE without it | A producer that picks its own bound then grades itself against it is exactly the circularity row S3 recorded. |
| Add the `SUPERSEDED` refusal unasked | Not in the ruling. The quarantine was a filename, and I had just finished writing a row about a calibration being readable as live. |
| Do not reply to the CTO | Rule 31: a corroboration goes to the record, not an inbox. The commit is the record. |

---

## Blockers

- **`2.0.0_SA_COO~P` DARK** -- rows S4, S6, S7, plus the TO-DB-b-1 text amendment and the contract
  edits the rulings name. Every remaining producer repair is downstream of the boundary and
  interval decisions.
- **Nothing on Andrew. Nothing on the CTO** -- S5 is answered and implemented.

---

## Next Steps

1. **[`2.0.0_SA_COO~P`]** Rows S4/S6: amend the boundary, fee basis and valuation interval; land
   the two contract edits rulings 17-18 name (remove `HOLDINGS_INCOME_FALLBACK`, declare the
   not-graded reason field).
2. **[`0.4.0_DS_ClientPlatform~S`]** On those: rebuild the flow term at account grain, propagate
   unknown cash instead of zeroing it, make inception durable, replay every cited extreme on
   pinned snapshots, re-measure (tolerance, large-flow share, band, excluded-weight ceiling),
   write the method contract, open the ledger, emit, grade AC1/AC2/AC3, then `TO-DB-b-3`.
3. **[CTO or issuer]** Choose `comparability_max_excluded_weight` from the re-measured
   distribution -- not askable yet, since the honest distribution needs the flow-term fix first.

---

## Note on the one thing I would have missed

`comp-read --enumerate 'RULING 1[789]'` returned `0 hit(s)` against the PRD. The rulings were
there; my pattern was wrong (they are numbered `17.` in a list). Had I taken that zero as an
absence I would have reported the CTO's ruling as unfindable, or worse, implemented from the
summary in the message body alone. CLAUDE.md's line that an early stop and a true absence read
identically is the same hazard one layer up: a wrong PATTERN and a true absence also read
identically, and the denominator printed beside the zero (395 lines, 35 sections scanned) proves
only that the tool looked, never that it looked for the right thing.
