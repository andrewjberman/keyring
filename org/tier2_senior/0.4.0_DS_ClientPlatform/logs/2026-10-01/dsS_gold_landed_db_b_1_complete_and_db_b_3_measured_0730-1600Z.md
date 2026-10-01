# Gold landed and DB-b-1 is terminal; DB-b-3 measured and both its headline numbers come with a recommendation against them -- 0.4.0_DS_ClientPlatform~S

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, VALIDATE, IMPLEMENT, SCRIBE

**Date:** 2026-10-01 07:30Z to 16:00Z
**Task Orders:** `IRPT_DASHBD.TO-DB-b-1` (COMPLETE), `IRPT_DASHBD.TO-DB-b-3` (measured; flip held)
**Status:** gold SERVED; five of five criteria PASS; both proof-of-spec instances VALID
**Workspace CLOUD commits:** `6be02af162`, `bb8f3bb2d1`, `4bcb2d6609`, `e8f9546020`, `93759b4d47`,
`f746013ac3`, `e9cea9fdbf`, `265f24be87` and the flip. All LOCAL; origin/CLOUD `0abf99fcd4`.

---

## Objective

Emit the round-1 reporting gold, grade DB-b-1, then run DB-b-3's tie-out against Black Diamond.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open / close-leg x5 / close, twice | PASS | DB-b-1's close OMITTED the sentinel deletion and needed a follow-up commit; DB-b-3's carried it |
| the graders' own `--self-test` | all four round-1 checks | PASS 7/7, 6/6, 11/11 | run BEFORE trusting any verdict, because the review found the OLD versions of all four passing on wrong evidence |
| proof-of-spec-check | both instances, `--governing-order` bound | VALID rc=0 twice | surprises limb ENFORCE: 9/9 then 2/2 resolving |
| commit-gate / naming / surprise-row / missions-tree | every commit | PASS | |
| comp-state | `--self-test` then drift | PASS 4/4 | run for the /exec-sum grounding |
| comp-read / comp-find | the order, the graders, the roster | PASS | |

**What worked:** running each grader's sealed self-test before believing its PASS.
**What failed -- mine, three times:** a `| tail` on a long-running background command buffers until
exit, so the output file sat at 0 bytes while the job ran fine. It cost visibility on the dry run
and twice more. Standing fix: never pipe a command whose progress I want.
**Gap found:** none new in the tooling.

---

## Work Completed

### 1. The first mint (`4bcb2d6609` open, `e8f9546020` close, `93759b4d47` sentinel)

**559 date partitions, 1,105 rows** at `irpt/49financial/gold/account_return_daily/` plus the
method row. Ledger opened BEFORE any object existed, four legs, each closed on the WORLD:

- schema hash RECOMPUTED from the landed parquet equals the contract's; ONE schema across all 559
  partitions; `guard_state` nulls 0; `HOLDINGS_INCOME_FALLBACK` 0; non-finite 0; out-of-band 0.
- C-VALUE, the check the method requires and I had not yet run: `V_t - sum(positions)` equals the
  balance cash line **to the cent on 6 of 6 accounts**. Three accounts carry exactly zero cash
  where any identity would appear to hold, so the evidence is the other three -- +25,488.64,
  -21.17 and -674.80 reproduce exactly including both signs.

**THE FIRST EMIT WAS KILLED at its background time limit** and is reported rather than quietly
retried. It died in the READ-ONLY prefetch having written nothing, and that was MEASURED: both
prefixes read 0 objects afterwards with a positive control on a populated prefix. Nothing was
half-landed, so nothing to roll back. The dry run beforehand earned its cost -- `emit_day` writes
per day, so a refusal mid-run is exactly NEVER-2's hazard.

### 2. DB-b-1 graded and flipped

AC1 **failed first, on a real gap**: the second contract did not exist. Row S2 had recorded it as
waiting on the measured thresholds, which now existed. Written from the LANDED parquet's schema so
it cannot describe a table never emitted; landed by the issuer, which recomputed the hash itself.
AC1/AC2/AC3 PASS, proof-of-spec VALID, `<status>complete</status>` verified from committed bytes.

**The flip waited on one thing and I said why:** AC1 reads the FILE, not the index, so while that
contract sat uncommitted its PASS was honest about the bytes and not evidence of a durable
artifact.

### 3. DB-b-3: the tie-out

`overlap_before_pull` = **5**, so no vendor pull and `vendor_calls` 0. **My first pass got 4 and
would have made a vendor egress.** It keyed on the REQUESTED `startDate`; the order states the
behaviour that makes that wrong -- "BD returns its own period list and ignores a start it does not
hold". Three rows on one account requested different starts and returned the identical
`-0.057098708` at `daysHeld 116`: one period under three request dates.

The single gold write landed: `tieout_tolerance_proposed` 0.037, `flow_convention` UNCHANGED at
END, no day partition touched. The column's type moved null -> double exactly as the issuer
predicted, so the contract bumped. AC1 and AC2 PASS; AC2 recomputed END on **62 of 62** gradable
days, which settles the tension I had flagged between the valuation linking and AC2's endpoint
recompute.

**Both headline numbers carry a recommendation against them**, which is the honest output:

- **3.70% tolerance** -- the rule executed faithfully, but what it is a percentile OF is not a
  disagreement between two calculations of the same thing. Opal's link excludes withheld days,
  BD's covers its full `daysHeld`. Clearest case: 34 of 38 days, +9.1259% against +12.7830%, with
  a $1,108,201.80 inception funding among the withheld.
- **flow_convention_preferred START** -- of 10 flow-bearing account-days across five periods,
  exactly ONE survives into the eligible population. The circularity is structural: a convention
  differs only where there is a flow, and a flow big enough to matter is what makes the producer
  withhold the day.

### 4. The efficacy and accuracy picture (measured for the /exec-sum)

| | |
|---|---|
| days serving a number | **1,071 of 1,105 (96.9%)** |
| withheld, with a stated reason | 34 (3.1%) |
| days the guard could GRADE | 708 (64.1%) |
| of those, AGREED | **700 (98.9%)** |
| served numbers with NO independent check | **371 of 1,071 (34.6%)** |

The gap is concentrated on the Tax SMA books, which are ~45% short by design against a long-only
comparison instrument. The one non-TaxSMA account is 99.8% served and fully checkable.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Dry-run the full history before the emit | `emit_day` writes per day; a mid-run refusal is the half-landed state NEVER-2 exists to prevent. |
| Report the killed emit rather than retry silently | The note required it, and the world had to be measured before claiming no damage. |
| Add `--method-row-only` | Re-emitting 559 partitions to change one field of one dim row would risk 1,105 served rows for a value none of them carries. |
| Hold both status flips until each contract was durable | The criteria read files, not the index. |
| Compute DB-b-3's numbers exactly as specified, then recommend against them | `tieout_tolerance_proposed` is by its own name a proposal; quietly substituting a better-looking rule would have hidden the finding. |
| Build the record with the GRADER's own statistics | Its p90 is nearest-rank; an interpolated p90 (0.0287 against 0.0366) would have missed its 1e-12 recompute by four orders of magnitude. |
| MASK ACCOUNT NUMBERS IN FUTURE REVIEW PACKAGES BY DEFAULT | Andrew's action overtook the question I had carried to him, and the forward-looking version is mine to decide under my own gates rather than to ask again. The existing Desktop folder is NOT retroactively masked: it already left the machine, and the review cites its paths and line numbers, so altering it would break the reviewer's own references. |

---

## Corrections I owe the record

1. **Row S11 corrects my own S10.** I wrote that START and MIDPOINT are identical on all five
   periods. They are identical on THREE -- the three with no eligible flow day -- and what ties is
   their MEDIAN, because with five periods the median lands on a non-discriminating period. I read
   the per-convention SUMMARY and stated it at PER-PERIOD grain: rule 24 (ii).
2. **The one-pager's first table row was wrong** the same way -- the 2026-04-08 period's returns
   under the 2026-03-16 label, with invented day counts. Caught by printing every cell from the
   record before committing. The JSON was right throughout, which is the argument for the record
   being the artifact and the prose a view of it.
3. **The instance asserted a control I had not run.** It claimed both graders' self-tests when I
   had run only AC1's. Running AC2's returned 6 of 6, so the claim became a measurement.
4. **DB-b-1's ledger close omitted the sentinel deletion.** AC3 passed on a tree whose git state
   still recorded an OPEN sentinel. Fixed in its own commit; DB-b-3's close carried it correctly.

---

## Blockers

- **`2.0.0_SA_COO~P`** -- land the method contract bump to 0.2.0; DB-b-3's flip waits on it.
- **`1.0.0_SA_CTO`** -- rows S9/S10: the tolerance NUMBER is its ruling per addendum ruling 11.
- **ANDREW, one call** -- FWD-8's ACCEPT clause reserves to him whether a figure is defensible when
  a third of its served days carry no independent check. Nothing is stopped; the outcome's grade is.

---

## Current State

The engine serves 1,071 defensible numbers of 1,105 account-days and labels every one with whether
a check ran. Eight defects were found and repaired today, the worst of them mine. What is NOT
established is accuracy against an external oracle: the tie-out is exercised but compares different
day sets, so it measures coverage rather than agreement. Both DB-b-1 and DB-b-3 are measured and
graded; one flip is terminal and one is held on a durable contract.

---

## Next Steps

1. **[`2.0.0_SA_COO~P`]** Land the 0.2.0 method contract; then this lane flips DB-b-3.
2. **[`1.0.0_SA_CTO`]** Rule the tolerance, and rule whether the tie-out is renamed to report
   coverage or restricted to comparable day sets.
3. **[Andrew]** The FWD-8 acceptance call above.
4. **[`0.4.0_DS_ClientPlatform~S`]** On those: re-run the tie-out on comparable periods if (2)
   says so; otherwise this lane's round-1 work is complete.
