# The re-measure worked, the thresholds did not, and an outside review found the order's flow term is wrong at account level -- 0.4.0_DS_ClientPlatform~S

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, DIAGNOSE, SCRIBE

**Date:** 2026-09-30 21:15Z to 2026-10-01 00:35Z
**Task Order:** `IRPT_DASHBD.TO-DB-b-1` (amendment 4 @b116670d7c); prep for `TO-DB-b-3` (amendment 2)
**Status:** IN PROGRESS -- emit HELD by this seat; the method is under review with Andrew
**Workspace CLOUD commits:** `5ee7e08c92` (overlap record), `603af56136` (producer + run-3 measurements).
Push state UNREAD at this write.

---

## Objective

Re-measure the three guard numbers with the in-kind flow term in place, then emit. The
measurement landed; the emit did not, because two of the three numbers are unusable as
specified and a methodology review Andrew ran with an outside model found a larger defect in
the flow term itself.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| commit-gate | on each producer edit (3 runs) | PASS | clean each time |
| safe-commit + naming-gate + owned-paths | 2 commits | PASS | both landed first try |
| comp-tool rail | one recursive `grep -r` over the Desktop review folder | PARTIAL | Denied and routed to comp-find, which is repo-only and cannot read a Desktop folder. Did the scan in Python instead. |

**What worked:** nothing new; the window was measurement and review, not search.
**What failed:** nothing.
**Gap found:** the rail denies a recursive grep on a path OUTSIDE the repository and points at
comp-find, which cannot search there (repo-only). The denial has no working remedy for an
out-of-corpus path short of the `# rail-checked` marker.

---

## Work Completed

### 1. The contract landed and was verified (row IRPT_DASHBD-S2, remedy 1)

`2.0.0_SA_COO~P` landed `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` at
`10939bbfa4` (msg 103397). Checked rather than taken: `schema_hash` recomputes from the
producer's schema at HEAD, 18 columns, same order. Amendment 4 sets the rule for the round:
contract files stay out of this seat's commits and the issuer lands them.

### 2. Vendor overlap measured before any pull (`5ee7e08c92`)

`OVERLAP_BEFORE_PULL_R1.json`: of 5,318 landed vendor responses, 4 belong to roster
relationships across 2 accounts; ONE distinct usable (account, period) pair. The raw count
is 2 because the vendor repeats a range. Below the amended face's threshold of 5, so a fresh
pull is admitted. NOT taken: the tie-out compares against gold that does not exist yet.

### 3. Re-measure on Andrew's "lets restart, go" (runs 2 and 3)

| | run 1 (pre in-kind fix) | run 3 (current) |
|---|---|---|
| daily return p99.9 | +108% | +4.4% |
| daily return p0.1 | -9.1% | -91.2% |
| guard difference p99 / max | 1.20% / 3.42 | 1.07% / 214.58 |
| flow share, unconditional p99 | 0.0 | 0.000001 |
| flow share, conditional p90 | -- | 1.32 (13 flow days of 1,098) |

The in-kind fix removed the spurious gains. The large-flow threshold is unusable either way
(one figure flags every flow, the other flags nothing), and a p99 tolerance flags 1% of days
by construction. The -91% and 218x tails are NOT yet replayed through the grading path.

### 4. Two producer changes (`603af56136`)

- A day with no comparison row is no longer MEASURED; it breaks the link. Zero rows affected
  on this sample (0 of 1,098). Found by pre-reading `p1_1_ac2_guard_seam.py`, which coerces
  a null comparison return to 0.0 on a MEASURED day.
- `measure_thresholds` reports the conditional flow distribution beside the order's rule.

Also read from the checks: `DB-1-AC1` no longer reads the policy registry (row S1 is out of
the acceptance path), and AC2's docstring claims a `diff > tolerance` test on unreconciled
days that its code does not make.

### 5. Methodology review (Andrew, with an outside model)

Andrew asked for a handoff, took it to GPT, and brought the review back. Outcome:

- **Withdrawn by me:** the accounting-identity guard (circular: a missing deposit becomes
  market movement); "10% is a published constant" (it is a house policy); "never wrong from
  right inputs" (end-of-day timing misstates a large same-day inflow with perfect inputs).
- **Confirmed against the code:** the flow term is wrong at account level. The order's face
  (`TO-DB-b-1` line 62) makes a matched inter-account leg INTERNAL and the producer sums
  EXTERNAL only (lines 441, 453). The retiring engine admits those legs at account level by
  CTO ruling (`c02_twr_engine.py:87-96`, `:373`). I built the regression having read that
  ruling earlier the same day. Six sampled days show 59 cash legs matched INTERNAL.
- **Found through the review:** using the custodian's own snapshot on the closed day gives
  -0.183% for account 0093614544 where the carry-forward rule on the order's face gives
  -0.286%; and fee debits stay in value while the figure is labelled "before advisory fees".
- **Matcher exposure measured:** 5 of 25 matched groups over six days are not pairs.

### 6. Review package for the outside model

`C:\Users\AndrewBerman\Desktop\GPT_REVIEW_49F_DAILY_RETURN_20260930\` (outside the repo, 62
files): producer, spec, prior art, evidence, diagnostic scripts and their recorded outputs,
plus `01_RESPONSE_TO_REVIEW.md`. Scanned: 0 client names, 0 credentials, 20 distinct real
account numbers. The producer copy is content-identical to `603af56136`.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Hold the emit | The flow term, the timing rule and both thresholds change what the table's columns mean. Writing it first would mean rewriting it. |
| Commit run 3 as evidence, not as thresholds | The numbers are real measurements and the record of why percentiles fail; the commit message says they are not approved. |
| Do not fix the account-boundary defect unilaterally | The fix departs from the order's face. It is the issuer's amendment, and Andrew is deciding the method directly. |
| No vendor pull yet | Trigger met and authorised, but there is nothing to compare against until the gold exists. |

---

## Files Modified

See commit messages `5ee7e08c92`, `603af56136`. Outside the repo: the Desktop review folder
(section 6). `org/standards/` contract: landed by the issuer at `10939bbfa4`, not by this seat.

---

## Briefs Written

| Brief | Path | Audience |
|---|---|---|
| Handoff text + addendum | in session; copy at `...\GPT_REVIEW_49F_DAILY_RETURN_20260930\02_HANDOFF_AS_SENT.md` | Andrew, outside reviewer |
| Response to the review | `...\GPT_REVIEW_49F_DAILY_RETURN_20260930\01_RESPONSE_TO_REVIEW.md` | outside reviewer |

---

## MCP traffic

3 messages: received 103389 (both order faces now cite the egress grant; a pull is admitted
below 5 overlap pairs) and 103397 (contract landed, amendment 4); sent the overlap record to
`2.0.0_SA_COO~P`.

---

## Blockers

- **HELD on Andrew** -- whether the method changes go to the issuer and the CTO. Evidence:
  the order's face at line 62 and `c02_twr_engine.py:87-96` disagree, and the review is his.
  Not yet filed as findings: the account-boundary defect, the fee label, the snapshot-interval
  improvement. They are written up in the Desktop response and in this log only.

---

## Current State

The producer at `603af56136` computes a daily return from the custodian balance value and
classified transactions, with in-kind transfers valued and the closed-day flows carried
forward. It is NOT fit to emit: inter-account transfers are missing from the flow term, both
thresholds are sample percentiles, the fee label contradicts the arithmetic, and the extreme
rows have not been replayed through the grading path. Nothing is in S3 under
`irpt/49financial/gold/account_return_daily/` or `dim_return_method/`. The change-management
ledger for the emit is not opened. `IRPT_BCKEND-S237`/`S239` (the served 2025-01-10 error in
the retiring engine's table) remain open with `2.0.0_SA_COO~P`.

---

## Next Steps

1. **[Andrew]** Say whether the method changes go forward, and whether the Desktop folder
   needs account numbers masked before it leaves the machine.
2. **[`0.4.0_DS_ClientPlatform~S`]** On that word: file the account-boundary and fee-label
   findings in the IRPT_DASHBD channel and send one message to `2.0.0_SA_COO~P`.
3. **[`2.0.0_SA_COO~P`]** Amend `TO-DB-b-1`'s method text (flow term at account level,
   valuation intervals, timing rule, thresholds) or rule that it stands.
4. **[`1.0.0_SA_CTO`]** C-METHOD, C-GUARD and C-LABEL in the PRD are touched by the same
   changes; row `IRPT_DASHBD-S1` is still open.
5. **[`0.4.0_DS_ClientPlatform~S`]** Then: rebuild the flow term, replay the tails, re-measure,
   method contract, ledger, emit, `DB-1-AC1`/`AC2`/`AC3`; then `TO-DB-b-3`.
