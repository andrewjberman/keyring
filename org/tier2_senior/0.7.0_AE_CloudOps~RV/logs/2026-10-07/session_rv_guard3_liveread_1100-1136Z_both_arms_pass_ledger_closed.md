# The first live read is PASS on both arms, and the same log proved row Z-S12 in production — 0.7.0_AE_CloudOps~RV

**archetype:** VALIDATE

**Date:** 2026-10-07
**Task Order:** `OPAL_BBGTML.TO-GUARD-3.checker-series-compare-and-tripwire-recency`
**Status:** COMPLETE — both reports delivered, NEVER-2 entry CLOSED, nothing owed by this seat.

---

## Objective

Grade V1, the order's first live read: today's 07:00 ET vehicle tripwire result and 07:30 ET checker
result, both on current data. Close the NEVER-2 entry or revert the merge within the hour.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `.tools/deploy_ledger.py` | `close-leg --leg-id V1 --proof ...` then `close --slug ...` | PASS | The contract tool refuses `close` while any leg is unproven, so the close is a mechanism rather than a claim. It also removed the `.open_deploys` sentinel itself and named both paths to commit — the sentinel/record pair is the gate's only input, so it must land in one commit. |
| `.tools/deploy_ledger.py` | `check` | PASS | Independent confirmation the slug is no longer listed OPEN. Verifying the close with the same tool that performed it, via a different verb. |
| comp-* census tools | — | SKIPPED | Non-application stated: nothing was searched this segment. Every artifact was a named log path or a scheduled-task field. |
| AE minimums (`comp-pipescript deployed`, `postdeps`, `comp-iam gaps`, `comp-blast`) | — | SKIPPED | Same non-application as the prior two segments: no gold run, no `iam.tf`, no infra, no S3 code prefix. |

**What worked:** `deploy_ledger.py`'s refusal-to-close-on-unproven-legs is the reason the NEVER-2 law
is a mechanism here and not discipline.

**What failed:** nothing in the tools. One of my own sends was refused by the Rule-31 broker cap at
175 words — correctly; the detail belonged in the deliverable, which is what the rule says. Recut to
the path plus the essentials and it delivered.

**Gap found:** none.

---

## Work Completed

### 1. Both arms, each on two instruments

| arm | log evidence | second instrument |
|---|---|---|
| 07:00 ET vehicle (11:00Z) | `bbg_tplus1_20261007_070002.log`: `PRECONDITION: PASS -- DAPI UP`; `custom CIX series graded: 13 of 84 tickers ... as-of 2026-10-06`; `all 13 custom CIX series reach the as-of 2026-10-06`; `RESULT: PASS`; `PULL EXIT CODE: 0` | `LastTaskResult 0` (was 267014) |
| 07:30 ET checker (11:30Z) | `freshness_check.log`, the only line stamped today: `PASS: data_as_of=2026-10-06 expected_frontier=2026-10-07 trading_days_behind=1 ...; per-series: ... series graded=10. every graded series ends ON data_as_of.` | `LastTaskResult 0` (was 2) |

**The precondition line was load-bearing, not decoration.** Report 1 committed in advance to grading
the tripwire arm **NOT RUN** if today repeated the 2026-10-06 DAPI-down run (row `Z-S11`,
`LastTaskResult 267014`, pull never attempted) — because in that state the tripwire never executes
and a silent log would look like a clean one. DAPI was up, so the arm is genuinely RUN.

### 2. A negative control on the summons path

A PASS must summon nobody — but silence only means something if the carrier writes when it should.
Checked on both: `freshness_ESCALATION.txt`'s last line is still **yesterday's**
`2026-10-06T11:30:02 STALE`, and zero `freshness_checker` inbox files are dated `20261007` in either
recipient directory. Yesterday's entry in the same file is what makes today's silence informative.

**Exits 4 and 5 did not fire live, and that is the correct outcome rather than a coverage gap.** The
data is healthy; a live 4 or 5 today would have meant a real defect. Exercising them in production
would require planting bad data, which is why AC1 proves them on archived object versions instead.

### 3. The same log measured row `OPAL_BBGTML-Z-S12` in production

The vehicle log carries **two** tripwire blocks: the pull leg runs the **tplus1** copy, and the send
leg (`publish_to_portal.py:64`) runs the **tzero** copy. The tzero block has the 5-model presence line
and **no `custom CIX series graded` line at all**.

> **The send gate ran today with zero per-series CIX coverage.** Row `Z-S12` predicted this from
> reading the code; this is the same fact measured on a production run, and it is what TO-GUARD-4
> closes on branch `rv-bbgtml-guard4`. It also independently matches GUARD-4 proof arm C5.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| CLOSED, not REVERTED | The order's own rule: revert only on a FAIL against CURRENT data. There was no FAIL on either arm, on either instrument. |
| Graded the arm on the PRECONDITION line before the verdict line | A tripwire that never executed produces no failure, which reads identically to a tripwire that passed. The precondition is what separates them, and it was committed to in report 1 before the outcome was known. |
| Did not treat the unexercised exits 4/5 as incomplete coverage | They are the defect paths; healthy data must not trigger them. Claiming them "untested" would invite someone to plant bad data into production to see them fire. |
| Recut the refused send rather than forcing it | `send_override` exists for a human operator's request. Nothing here warranted it; the cap was right and the detail belonged in the file. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/critical_paths/change_management/20261007T0949Z_bbgtml-guard3-...md` | V1 closed, entry CLOSED | Yes — `d75142de44` |
| `org/critical_paths/.open_deploys/bbgtml-guard3-...json` | sentinel removed by the close | Yes — `d75142de44` (deletion) |
| `.../deliverables/TO_GUARD_3_REPORT_2_FIRST_LIVE_READ_20261007.md` | report 2 of 2 | Yes — `a00f5c1b83` |

**Push state, MEASURED:** **LOCAL @`a00f5c1b83`** — `git ls-remote origin CLOUD` read `1485e4e1ce`
at 11:35Z.

---

## Blockers

**None.** Nothing is owed by this seat on TO-GUARD-3 or TO-GUARD-4.

---

## Current State

TO-GUARD-3 is closed end to end: both edits live in the shared working tree, each now exercised by
its own scheduled task on real data (checker `cfebeaf6af` exit 0 at 11:30Z; tripwire `b0551c6a59`
pull exit 0 at 11:00Z), both reports delivered to `2.0.0_SA_COO~Z`, NEVER-2 entry CLOSED at
`d75142de44` with nothing stranded, inside its 5.0h window. TO-GUARD-4 sits built and proved on
branch `rv-bbgtml-guard4` in worktree `C:/tmp/rv-guard4`, NOT MERGED, waiting on Andrew's word. The
hand-run send path is therefore still uncovered and is held only by ADDENDUM 7's reading discipline.

---

## Next Steps

1. **[`2.0.0_SA_COO~Z`] Flip `<status>` on TO-GUARD-3 and TO-GUARD-4, and disposition
   `OPAL_BBGTML-Z-S12`** — its last unmeasured claim is now measured twice, by GUARD-4 arm C5 and by
   a production run (section 3).
2. **[Andrew, via `1.0.0_SA_CTO~Z`] The word that lets the tzero port merge** — until then nobody
   hand-runs `publish_to_portal.py` without running the tplus1 tripwire on the same files first.
3. **[`0.0.0_AB_MSTR~Z`] The push** — CLOUD is diverged; everything from both orders is LOCAL.
4. **[this seat] Nothing.** Available for the next order.
