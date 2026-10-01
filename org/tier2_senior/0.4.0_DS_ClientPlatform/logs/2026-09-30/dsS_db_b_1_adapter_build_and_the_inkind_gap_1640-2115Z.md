# I built the adapter, then found I had written the same defect I filed three hours earlier -- 0.4.0_DS_ClientPlatform~S

**archetype:** MIXED (IMPLEMENT + DIAGNOSE)

**Date:** 2026-09-30
**Task Order:** `IRPT_DASHBD.TO-DB-b-1` (round 1, workstream B, issued `2.0.0_SA_COO~P` @51c05d1530;
amendments 1 and 3 @2fde2edae3)
**Status:** IN PROGRESS -- the measure pass is HELD on Andrew's word after the harness killed it for
low system memory
**Workspace CLOUD commits:** `63b7945fc4` (adapter + declaration), `ae1d5ffb6a` (row S2),
`85863e9b5a` (row S1 + thread-account census), `4c4989c800` (Andrew-direct record). LOCAL;
origin/CLOUD `5fe52a896a` by `git ls-remote`.

---

## Objective

Build the 49 Financial reporting adapter and emit the first Opal-shape reporting gold,
`account_return_daily`, for the round-1 sample under a written contract with the C-GUARD
cross-check applied and the three guard numbers measured from the data.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-pipescript deployed | `--pipeline advi` | PASS | Proved the source I read was the RUNNING producer before the pr-263 exercise. |
| comp-read | on the PRD, the decomposition, `pipeline_cli.py`, `chain_49f_entrypoint.py`, `c00_flow_ledger.py`, `holdings_performance.py` | PASS (6 of 6) | The workhorse of the session. The PRD read is the one that mattered: it surfaced C-METHOD, which connected my own earlier finding to the cell I was about to build. |
| comp-find | `\b<VALUE>\b` x 12 over `data`, `infra/aws/lambda`, `portal/src` | PASS | The rule-24 token census. Denominator 12,876 files printed on every run; `--band DEF` is what turned three scary hit counts into "no competing definition". |
| commit-gate | on every `.py` edit | PASS | Caught one unused import on the first build and nothing after. |
| safe-commit / naming-gate / owned-paths | 5 invocations | PASS + 1 REFUSAL | The refusal is the finding in section 6. |
| comp-state | `--self-test` | PASS 4/4 | Gate for the stage report run mid-session. |

**What worked:** `comp-read --for` replaced what would have been six full-file reads with six targeted
ones, and twice returned the exact paragraph that changed what I built (`GLD-b-3` on the closure day,
C-METHOD on the return form). `comp-find --band DEF` is the difference between "MEASURED has 1,183
hits, this is a collision" and "MEASURED has six definitions and none of them is this axis".

**What failed:** nothing this block. `comp-pipescript postdeps --firm` still has no `advi` member
(logged in the previous block, unchanged).

**Gap found:** none new.

---

## Work Completed

### 1. The thread-account census, and a tie-break an instrument nearly decided

Amendment 1 made the sample six accounts: the five roster accounts plus one long-history thread
account chosen by census. First run: 558 of 560 `dim_balance` partitions read, two lost to an S3 read
timeout -- and **every top candidate sat at exactly 558**, i.e. at the readable-day count. The
tie-break was therefore being decided by which partitions happened to time out. Re-ran with retries
and a refuse-on-unread guard; 560 of 560, same pick (`0010783709`, 560 positive-value days, `fact_trn`
on 253). Recorded in `THREAD_ACCOUNT.json` with the census and the note.

### 2. The registry limb refused, as the order anticipated (row `IRPT_DASHBD-S1`)

`infra/logic/registry/reporting_policies.json` cannot express a gold parquet table. Probed the real
validator with the candidate row built in memory: `reporting tier/table is not admitted`. The limbs
admit tier `{state, platinum}` and extension `{csv, json, pdf}`; the full nine-way matrix has no
combination that describes this table. File untouched (verified clean after the probe). `address()`
and `name()` both answer, so only the conformance-record limb stops. The row offers a reading rather
than assuming one -- every field on that record is retention and disposal, so medallion gold may be
correctly out of scope, in which case the remedy is a ruling and not a widened enum.

### 3. The adapter

`data/assets/scripts/gold/irpt_reporting/account_return_daily.py` + `sources.json`. The money law
(`gross_amount`, never `net_amount`) and the IC trap (a direction read only from a cash-verified row)
carried from `c00_flow_ledger.py` rather than rediscovered. The skipped-day rule on its face from my
own row `IRPT_BCKEND-S237`. Smoke-tested live: on a zero-flow day the whole-account return and the
holdings basket return agree to ~4e-06, which is the cash share.

### 4. THE FINDING OF THE SESSION: I wrote the defect I had just filed

The first full measure pass produced numbers that could not be written down:

| signal | value | why it is not writable |
|---|---|---|
| `large_flow_share` p99 | **0.0** | a threshold of zero flags every day carrying any flow |
| guard diff max | **3.4158** | 341 percentage points between the form and the cross-check |
| `r_t` p99.9 | **+1.0817** | a +108% DAY, outside the plausibility band |

I went looking instead of writing them down. Cause: **F_t counted CASH rows only.** In-kind securities
transfers landed in `V_t` with nothing subtracting them. Measured on the six sample accounts: 41
account-days carry in-kind legs, and the largest are the ACAT transfers that OPEN four of the six --
$1,982,263.33, $2,075,948.92, $1,108,201.80, $763,458.68 -- **each on or beside its account's first
positive value.** Every client's opening book was being served as one day's gain.

That is `IRPT_BCKEND-S237`'s own shape, reached by a different route, **in the code written to prevent
it**, three hours after I filed the row. Finding a class of defect confers no immunity to it; the only
thing that caught this was refusing to write down a number I could not explain.

Fixed: in-kind legs value at quantity x same-day close (row price where positive, else the day's close
for that identifier from the positions table), directed by position side through a map deliberately
SEPARATE from the cash one with its own call site, and a leg that reaches neither price is UNVALUED
and marks its account-day `FLOW_UNRECONCILED` rather than being zero-buried.

**Verified on the known days**, which is the point:

| day | account | flow now | book | verdict |
|---|---|---|---|---|
| 2026-03-19 | 0084073310 | $763,458.68 | $762,601.30 | NOT_MEASURABLE (no prior value) |
| 2026-07-08 | 0076459710 | $1,108,201.80 | $1,111,852.97 | NOT_MEASURABLE |
| 2026-03-26 | 0035940058 | $1,982,263.33 | $1,932,279.26 | NOT_MEASURABLE |
| 2026-07-29 | 0084073310 | **$0.00** | $1,033,299.42 | MEASURED -- and CHECKED |

The fourth is the one worth naming. $0.00 against a known $2,075,948.92 looked like the bug surviving.
It is correct: two legs, one cusip (`037833100`), identical quantity and price, one SHORT and one LONG
-- a registration journal netting exactly zero. I only know that because I read the legs instead of
accepting a plausible number.

### 5. Two defects the failure exposed in passing

- **`read_partition` had no retry**, so a transient S3 timeout killed a whole run (it killed my
  diagnostic). Now retries and then RAISES with the key named: a failed read is neither an absence nor
  a zero -- the same trap as section 1, one layer down.
- **The transaction read projected all 140 columns when it needs 7**, and every read was serial: 0.88 s
  parse against 0.01 s projected, 6.2 s per trading day, about an hour across the history, paid twice
  (measure and emit). Projected and prefetched in parallel: the same 20-day probe went 2m04s -> 35s and
  returned the **identical** tolerance, which is the control that says it got faster without getting
  different.

### 6. The order granted a path it cannot confer (row `IRPT_DASHBD-S2`)

`<paths>` grants two files under `org/standards/` and the preflight states "lane: the `<paths>` block
IS the grant". That directory is lane `ANY_EXEC`; the hook grades the COMMITTING AGENT, not the order.
Control: the identical commit without that one path landed at `63b7945fc4`, every gate green. The
audited author override exists and was NOT used -- the refusal is an ownership boundary, not a
mis-stamped author, and spending an override to cross it is what the audit log exists to catch.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Refuse to write the first thresholds down | Three signals were degenerate or absurd. A measured number I cannot explain is not a measurement. |
| Fix in-kind rather than widen the band | The band was not the problem; F_t was. Widening would have served the defect under a laxer guard. |
| Quarantine the pre-fix thresholds rather than delete | They are the evidence the first pass was unusable. Renamed so the live filename is ABSENT and the producer fails closed -- exercised: "REFUSED: an emit needs --thresholds-in". |
| Do not use the audited override on `org/standards/` | An ownership boundary, not an author-stamp problem. |
| Do not restart the memory-killed pass | The harness's kill notice says to report and wait. Held on Andrew's word. |
| Record Andrew's egress grant verbatim and NOT spend it | "whatever calls you need" is conditioned on need. The tie-out still runs on landed responses first; the issuer has since bounded the trigger at under 5 account-period pairs. |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` | new, 900+ lines | Yes -- `63b7945fc4` |
| `data/assets/scripts/gold/irpt_reporting/sources.json` | new declaration | Yes -- `63b7945fc4` |
| `.../deliverables/0.4.0_DS_ClientPlatform~S/THREAD_ACCOUNT.json` | census record | Yes -- `85863e9b5a` |
| `.../MEASURED_THRESHOLDS_R1.SUPERSEDED_PRE_INKIND_FIX.json` | quarantined | Yes -- `63b7945fc4` |
| `.../IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` | rows S1, S2 | Yes -- `85863e9b5a`, `ae1d5ffb6a` |
| `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` | written, 18 cols, hash `b5fa8e4e48bf...` | **No -- lane refusal, row S2** |
| `org/tier2_senior/.../ANDREW_DIRECT_20260930_1855Z_*.md` | Andrew-direct record | Yes -- `4c4989c800` |

**No S3 object written this session.**

**CORRECTION TO THE RECORD:** `63b7945fc4`'s subject reads "... + the `account_return_daily` contract"
and the contract is NOT in that commit. The message was written before the lane refusal was known and
the commit was retried with a narrower pathspec. A commit message cannot be edited; row
`IRPT_DASHBD-S2` and this line are the pointers.

---

## Briefs Written

| Brief | Path | Audience |
|---|---|---|
| Rows S1, S2 | `.../IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` | `2.0.0_SA_COO~P`, `1.0.0_SA_CTO` |
| Andrew-direct record | `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ANDREW_DIRECT_20260930_1855Z_EGRESS_FOR_WHATEVER_CALLS_YOU_NEED.md` | `1.0.0_SA_CTO`, `2.0.0_SA_COO~P` |

---

## Blockers

- **HELD on Andrew** -- the full measure pass. The harness killed it for critically low system memory
  (3.9 GB free of 31.7 GB at the check) and its notice instructs the seat to report and not restart
  unasked. Not a fault of the command; it died in the prefetch with no partial results.
- **Owed by an exec** -- the two contract files under `org/standards/` (row `IRPT_DASHBD-S2`). Not
  blocking the emit, which is gated on the thresholds.

---

## Current State

The adapter is built, committed at `63b7945fc4` and correct on every case verified by hand, including
the in-kind term that the first measure pass proved was missing. The contract is written and hash-locked
to the producer but cannot land under this seat's author line. The pre-fix thresholds are quarantined and
the producer fails closed without live ones, so no emit can accidentally rest on the defective
distribution. Nothing is in S3 and no number is served. What remains for DB-b-1 is the re-measure, the
method contract that consumes it, the change-management ledger, the emit for six accounts, and the three
acceptance criteria.

---

## Next Steps

1. **[Andrew]** One word to restart the measure pass -- ~16 min, read-heavy rather than memory-heavy.
2. **[`0.4.0_DS_ClientPlatform~S`]** Method contract from the measured numbers, ledger open, emit, then
   `DB-1-AC1`/`AC2`/`AC3`.
3. **[`2.0.0_SA_COO~P`]** Land the two `org/standards/` contract files, or rule one of row S2's other two
   remedies.
4. **[`1.0.0_SA_CTO`]** Row `IRPT_DASHBD-S1` -- whether medallion gold belongs in the X10 reporting
   register at all. `DB-1-AC1`'s policy-file half cannot grade until it is ruled.
5. **[`2.0.0_SA_COO~P`]** Rows `IRPT_BCKEND-S237`/`S239` remain open on the served 2025-01-10 returns;
   nothing in this cell turns on them.
