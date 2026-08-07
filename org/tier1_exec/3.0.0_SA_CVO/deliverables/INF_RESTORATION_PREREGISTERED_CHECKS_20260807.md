# INF chain restoration -- PRE-REGISTERED verification criteria

**Author:** 3.0.0_SA_CVO. **Written:** 2026-08-07T16:41Z.
**Dispatch:** 1.0.0_SA_CTO 20260807T154613Z (4 axes). **Boundary:** CVO gates NOTHING; AE does not
wait on this document. Verification happens AFTER the artifact lands; a defect is a FINDING routed
same-turn to CTO + AE, never a hold.

> **WHY THIS FILE EXISTS AND WHY ITS TIMESTAMP MATTERS.** At the moment of writing,
> `canonical_performance_2026-08-06.parquet` and `_2026-08-07.parquet` **DO NOT EXIST** (head-object
> 404, verified 16:41:07Z), `canonical_nna` keys dated `2026-08-*` number **0**, and
> `pipeline-complete.json` still carries `run_date=2026-07-31`. AE fired the full chain at
> 16:17:17Z with ~63min expected (~17:20Z).
>
> CTO's axis 2 is *"a collision fix can restore a FILE without restoring the DATA."* The failure mode
> of judging that AFTER seeing values is that almost any number can be rationalised once it is in
> front of you -- and here there is a ready-made innocent explanation available (a library-version
> change at the boundary), which is exactly the kind of story that absorbs an anomaly. **Criteria
> fixed before the values exist are a TEST. The same criteria written afterward are a STORY.**
> This file is committed so that which one happened is checkable by someone other than me.

---

## 1. BASELINE (measured pre-fix, 18 consecutive published dates)

Source: `s3://opal-data-inf/gold/canonical/canonical_performance_<date>.parquet`.
Denominator stated everywhere: **6,386 keys** under `gold/canonical/` = 2,515 `canonical_performance`
+ 2,444 `holdings` + 1,426 `canonical_nna` + 1 other.

**Structure (held on all 18 days):** grain = 1 row per `(date, account_id)`; 13 columns; `date` column
single-valued and equal to the filename date; `household_id` nunique **288** (287 before 07-24);
`advisor_key` nunique **5**; exactly **1** account with negative `total_aua`.

**Identities (held on all 18 days):**

| identity | observed |
|---|---|
| `net_nna == daily_inflow - daily_outflow` | 100.0% every day |
| `growth == aua_change - net_nna` | 100.0% every day |
| `aua_change == total_aua - aua_prior` | 99.7% - 100.0% |
| today's `aua_prior` == yesterday's `total_aua` (account inner-join) | 100.0%, 796-801 matched |

**Series:**

| date | rows | sum_total_aua | sum_net_nna | rows_net_nna!=0 |
|---|---|---|---|---|
| 2026-07-24 | 795 | 201,588,353 | -12,607 | 7 |
| 2026-07-27 | 796 | 202,087,692 | 12,397 | 10 |
| 2026-07-28 | 798 | 203,315,820 | 2,565,979 | 7 |
| 2026-07-29 | 799 | 206,223,776 | -2,650 | 3 |
| 2026-07-30 | 801 | 204,775,547 | -18,047 | 4 |
| 2026-07-31 | 801 | 206,709,718 | -125,151 | 37 |
| 2026-08-01 | 802 | 206,624,794 | **0** | **0** |
| 2026-08-04 | 797 | 207,639,683 | **0** | **0** |
| 2026-08-05 | 798 | 209,431,383 | **0** | **0** |

All 15 days 07-13..07-31 carry 1-37 nonzero-NNA rows. The three after carry zero, out of ~800
accounts each. **The boundary is exactly the `canonical_nna` cliff:** newest `canonical_nna` key is
`canonical_nna_2026-07-31.parquet` (S3-written 2026-08-01T14:51:13Z).

**Write-time note:** every `canonical_performance` date sampled (07-13 .. 08-05) carries S3
LastModified `2026-08-05T14:48:37-41Z` -- one rewrite event, by the run that then died at INF_C_01 at
14:50:56Z. The three newest served dates are output of a chain that FAILED, written ~2min before it
aborted, never validated by a completion.

**Weekday/weekend size signature (structural, checkable before opening the file):** weekdays ~38KB,
weekends ~27.6KB (08-02 and 08-03 both exactly 27,609B; 08-01 38,727B; 08-04 38,009B; 08-05 38,018B).
2026-08-06 is a Wednesday and 2026-08-07 a Thursday, so a restored file arriving at weekend size is a
flag on its own.

---

## 2. PRE-REGISTERED PREDICTION

**IF** the fix clears only the sync collision and `INF_C_01` fails again on the NNA coverage guard
(or otherwise does not emit `canonical_nna` for 08-06/08-07), **THEN** all of the following hold:

1. `canonical_performance_2026-08-06/07.parquet` **are created**.
2. ~795-805 rows, 13 columns, 288 households, 5 advisor_keys.
3. Internal identities hold at ~100%.
4. `aua_prior` continuity against 08-05 holds.
5. `total_aua` looks sane, roughly $205-215M.
6. **`net_nna == 0` for every row.**
7. **A "chain completed / files present / values sane" check PASSES.**

That combination -- 1 through 5 passing WITH 6 -- is CTO's *file restored, data not*, made concrete.

## 3. THE DISCRIMINATING TESTS (two reads, no judgement call)

| # | test | healthy | zeroed |
|---|---|---|---|
| a | does `canonical_nna_2026-08-06/07.parquet` EXIST? | present | absent |
| b | `count(rows where net_nna != 0)` in the new performance files | 1-37 | 0 |

If (a) is absent, (b) is 0 **by construction** and a green chain is cosmetic on the NNA axis.

## 3a. AMENDMENT 2026-08-07T17:14Z -- made BEFORE the artifact existed

**Both dates still 404 and `canonical_nna` dated `2026-08-*` still 0 keys at the moment of this
amendment** (probe 17:11:53Z). Recording it because amending criteria is only legitimate while the
data does not exist, and the distinction has to be checkable rather than asserted.

**What changed:** `aua_prior` continuity < 99% now **BLOCKS a RESTORED verdict**. It was written as
an advisory INSPECT note.

**Why:** I mutation-tested the verifier rather than only positive-controlling it. Feeding it a
structurally-clean file with 0.9% continuity returned **RESTORED with a note** -- so a genuinely
discontinuous artifact could have passed. CTO's dispatch names continuity explicitly as an axis-2
criterion ("sane in magnitude, sign, grain and continuity"), so advisory was the wrong strength.
A rule that cannot fail on the thing it is supposed to catch is not a rule.

**Also found by the same exercise, and worth its own line:** the FIRST verifier I wrote was broken --
it called `aws` via `subprocess.run` from native Windows Python and died `FileNotFoundError`
(CreateProcess cannot spawn the MSYS `.tools/aws` shim; CLAUDE.md's python-parent-spawning-MSYS-binary
class). It would have failed at the decisive moment. It was caught only because I smoke-tested the
instrument against a state whose answer I already knew. **The verifier is now bash-does-all-AWS,
python-reads-local-files-only.** All three verdict branches are exercised: NOT RESTORED (real,
current state), PARTIAL (mutant: perf present / nna absent / net_nna zeroed), RESTORED (mutant:
perf+nna present / 37 nonzero-NNA rows).

## 4. VERDICT RULES, fixed in advance

- **RESTORED** -- 08-06 and 08-07 present, structure per S2.2-2.5, `canonical_nna` present for both
  dates, and nonzero-NNA row counts inside the historical 1-37 band.
- **PARTIAL / COSMETIC ON THE NNA AXIS** -- performance files present and structurally clean, but
  (a) absent or (b) == 0. **This is NOT "restored."** Reported as such regardless of chain rc,
  completion sentinel, or runner self-report.
- **NOT RESTORED** -- files absent, or structure departs from S2.2-2.5.
- **UNRESOLVED** -- I cannot discriminate. Recorded as UNRESOLVED, never resolved by inference.
  Specifically: a clean completion **does not** discriminate "the 08-05 NNA coverage condition
  self-resolved" from "it did not re-fire today." Could-not-verify is a finding.

**Scope note carried forward:** 08-01, 08-04 and 08-05 are ALREADY zeroed and predate the collision
entirely. "Restore 08-06 and 08-07" is therefore insufficient as a definition of done for the NNA
axis; a three-day backfill sits behind whatever fixes the NNA leg. Naming it, not proposing it --
scope is CTO's and Andrew's.

---

## 4a. RESULT -- 2026-08-07T17:31Z. **VERDICT: PARTIAL / COSMETIC ON THE NNA AXIS** (rule S4.2)

Run terminated 17:21:39Z, `exit_code 1`. Criteria above were committed @803c398573 (+ amendment
@3a790b1b91) while both dates read 404 -- so the rule was fixed before the values existed.

**AE's fix WORKED, and this belongs first.** `chain_full_20260807_161721.log:10-20` -- sync clean,
all eight multi-homed basenames `collision OK (identical xN)`, no FATAL. The chain ran its full
~64 minutes for the first time since 08-05 and reached `INF_C_01` for the first time in two days.

**The AUA axis is genuinely restored, not cosmetically:**

| | rows | cols | adv | sum_total_aua | nna identity | aua_prior continuity |
|---|---|---|---|---|---|---|
| 2026-08-06 | 798 | 13 | 5 | 209,445,467 | 100.0% | 100.0% |
| 2026-08-07 | 799 | 13 | 5 | 208,325,960 | 100.0% | 100.0% |

**The NNA axis is not:** `canonical_nna_2026-08-06/07.parquet` **ABSENT**; rows with
`net_nna != 0` = **0 of 798** and **0 of 799** (historical band 1-37);
`pipeline-complete.json` still `run_date=2026-07-31`.

**Mechanism SOURCE-CONFIRMED** (`chain_full_20260807_161721.log`, 36,170 lines, file coordinates):
`:36039` the guard error, `:36054` `nna_coverage_guard.NNACoverageRegression`, `:36066`
`CHAIN chain:full FAILED at INF_C_01 (exit=1)`, `:36067` aborted `2026-08-07T17:21:38Z`.
**Identical 5 accounts, identical $514,487.47, identical partitions to 08-05.** So the 08-05
condition did **not** self-resolve -- it was masked two days by the collision and re-fired on first
contact.

**Prediction scored 6/7.** Confirmed: files created; rows in band; 13 cols; 5 advisor_keys;
identities ~100%; continuity holds; `total_aua` in band; and clause 6, the load-bearing one --
`net_nna == 0` for every row. **Missed:** households read **290**, the rule said exactly 288.
**That is MY band being too tight, not a data defect** -- the series drifts 287 -> 288 -> 290,
consistent with organic household growth. Recorded as a rule error rather than quietly widened.
**Clause 7 corrected in the estate's favour:** I predicted a naive "chain completed / files present
/ values sane" check would pass. Half right -- the rc and completion sentinel DID fail honestly
(`exit=1`, sentinel not advanced). What would have passed is an **artifact-level** check: files
present, structurally perfect, continuity 100%. I was too pessimistic about the chain-level signal.

**CONSEQUENCE THAT GREW:** the served zeroed-NNA range is now **FIVE** dates, not three -- 08-01,
08-04, 08-05, **and now 08-06 and 08-07**, written by this run before it aborted. Every future run
past the sync step adds another, because the producer emits `0` rather than null for a date with no
`canonical_nna`. **The backfill scope grows until the NNA leg is fixed.**

⛔ **BACKFILL MUST NOT FIRE ON THIS BRANCH.** Release condition is the `INF_C_01` coverage-guard
excusal on the 5 accounts / $514,487.47 -- Andrew's call, put to him before this verdict.

## 5. GROUNDING / LIMITS

- `INF_C_01` failure is **SOURCE-CONFIRMED**: `nna_coverage_guard.py:320` raising
  `NNACoverageRegression`, from `INF_C_01.canonical_nna.py:918` (`main()` :956); log
  `chain_full_20260805_134750.log:35996` (file coordinates; file is 36,127 lines). 5 accounts,
  $514,487.47.
- **INFERRED, not source-confirmed:** WHY a missing `canonical_nna` yields `0` rather than null. The
  date-boundary coincidence is exact; the join has not been read. Do not upgrade this without opening
  the producer.
- **NOT ESTABLISHED:** downstream consumers of `canonical_performance` (no claim made about what is
  portal-served off it, or who sees the zeros); any relation between the 5 guard accounts and the
  zeroed NNA; whether the 08-05 condition still holds today.
- Trading frame **inherited from CTO, not re-derived**: `expected_last_trading_day = 2026-08-07`;
  last canonical present at diagnosis 2026-08-05; two trading days owed; not a weekend artifact.

**No alert, alarm, SNS, SES, freshness checker or monitor is proposed or built by this work**
(standing moratorium, Andrew-direct 2026-07-28). The instruments here are: reading the log, and
reading the parquet.

-- 3.0.0_SA_CVO
