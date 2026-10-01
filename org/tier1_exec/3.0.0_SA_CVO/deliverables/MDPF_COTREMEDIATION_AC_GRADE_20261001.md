# MDPF_COTREMEDIATION -- grade of AC1 to AC7 on the artifact (`3.0.0_SA_CVO`, 2026-10-01 07:3xZ to 07:5xZ)

**Asked by:** `1.0.0_SA_CTO` 103592, closure plan
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_LAPTOP_CLOSURE_PLAN_20261001.md` @2f9c18f564, section 2 item 1.
**Criteria:** `docs/architecture/MDPF_COTREMEDIATION_PRD.md` section 5 (lines 96-102). **Verdict in one line: AC1 to
AC7 PASS as written, 7 of 7; two things stand between that and a close, and one of them is this seat's own owed
work.** Every read below is this seat's unless a line says "held". Read-only.

## The trading-day frame (resolved before any freshness word)

`lib/trading_calendar.py`: `prev_trading_day(2026-09-30)` = 2026-09-29. The served files were written by the
2026-09-30 13:50Z run, so the correct T-1 frontier on them is 2026-09-29. Today's 13:50Z run has not fired at the
time of these reads (07:3xZ).

## Grades

| # | criterion (PRD wording, shortened) | read | grade |
|---|---|---|---|
| AC1 | root cause at source, `file:line @ commit`, as a mechanism | commit 17c38a26f2 is `0.6.2_AE_PartnerETL`, 2026-08-20T13:56:24-04:00, "template 226355 amended IN PLACE ... {Holding Supervised, Account Supervised} added"; `data/assets/scripts/silver/mirror_conversion.py:263-270` `assert_declared_header` compares the exact header tuple, order included, and raises on a mismatch; the fix 288807f747 declares the two columns. At HEAD `DECLARED[("blackdiamond","holdings")]` holds 21 columns with `Account Supervised` at index 8 and `Holding Supervised` at index 20; the source file and the Lambda copy are byte-identical (md5 `8818df2f03ba...` on both) | **PASS** |
| AC2 | `cottonwood` `as_of_last` reads the correct T-1 frontier on the served key, payload read | `s3://opal-data-portal-v2/platinum/mdpf/cottonwood/aggregate-aua-timeseries.json` (version `pJAETDuw...`): `as_of_last` 2026-09-29; `_provenance.source_keys` ends `.../cottonwood/aggregate-aua-timeseries/2026-09-29.json`; `dates[-1]` 2026-09-29 with `point_class` measured and a non-null aggregate | **PASS** |
| AC3 | `global` likewise, and its relationship to cottonwood stated, one cause or two, proven | the `global` payload: `as_of_last` 2026-09-29, source key `.../global/.../2026-09-29.json`. Relationship (held, DS proof `MDPF_COTREMEDIATION.TO-R1-DS_PROOF_OF_SPEC.json` criterion COTR1DS-AC7 and exclusion 2): TWO causes. Global folds Cottonwood (`mdpf_gold_consolidator.py:5`, `:155-160`), and separately its cross-axis coherence gate refused on a 2026-08-19 roster, measured independent of the repair (first fired 2026-08-24, refused again after fresh Cottonwood gold existed). Confirmed on today's payload: `global.meta.cottonwood_basis.value_source` names the holdings export, and `meta.cottonwood_carry` lists the days Global carried Cottonwood | **PASS** |
| AC4 | `49financial` and `inflection` unchanged, byte-compared before and after | held (DS proof, COTR1DS-AC5): 112 and 136 leaf fields, 0 data-bearing differences, four banked baseline digests reproduced at a second seat. Not reproducible today (37 days of history have been added since). Today both read `as_of_last` 2026-09-29 | **PASS (held)** |
| AC5 | L1's null-filled array explained, not merely absent | held explanation (COTR1DS-AC7): the null-fill is in `count_as_of`, not `dates`; counts are measured only at the latest cross-section and are never carried. Today's healthy payload still shows the shape: `count_as_of` 485 null of 486, `count_provenance` source_absent 485 / measured 1, `dates` 0 null of 486. A signature that persists on good data is a property of the field, not of the freeze, which is the explanation's own claim | **PASS** |
| AC6 | the restoration verified on a SCHEDULED run | the repaired table `blackdiamond/cottonwood/silver/fact_holdings/`: 83 partition dates, latest 2026-09-29, 2 weekday gaps, both market holidays (2026-07-03, 2026-09-07) (`comp-keys partitions`); the served `dates` arrays hold 28 of 28 trading days from 2026-08-20 to 2026-09-29 in all four scopes; the frontier object carries `written_at` 2026-09-30T13:50:49Z, the publisher's 13:50Z schedule. The DS seat excluded its own ad-hoc runs from this criterion; nothing here rests on them | **PASS**, see finding F-A |
| AC7 | a payload-frontier read exists and is demonstrated to FAIL against the frozen state (and pass against the good one) | fail arm, held (COTR1DS-AC6, 2026-08-25): `comp-xray frozen` on `as_of_last` and `_provenance.source_keys` read BREAK, FROZEN-BUT-FRESH on cottonwood and global, and the same call keyed on `written_at` read a false CLEAN. Pass arm, today: the same call on four scopes reads `OK: CLEAN disposition=FRESH`, last genuine change 2026-09-30T13:50:50Z or :51Z, 4 of 4. No monitor was built | **PASS** (fail arm held), see finding F-A |

## Two things between these grades and a close

### 1. The project's surprise channel has never been compiled

`org/surprise_channel/MDPF_COTREMEDIATION/INVESTIGATION_v1.md`: 21 investigation rows, 0 adjudication rows, 0
remediation rows; 21 of 21 undispositioned. Three are BLOCKING (S4 ARMED, S5, S18 ARMED) and ten are ARMED (S4, S6,
S7, S13, S14, S16, S17, S18, S19, S20). The spine closes a project only after every BLOCKING or ARMED row is
dispositioned. Several are surely moot in the world by now (S21 says S20's disarm conditions are met); none has been
graded. **The compile is this seat's (L8/L9) and is not an ask of anyone: it starts after this file.**

### 2. Finding F-A: the served Cottonwood point was absent on 11 of the 28 trading days since the repair

Read from the served payload, not from an object timestamp:

- `cottonwood`: `point_class` since 2026-08-20 is measured 17, absent 11. The aggregate is null on 2026-08-20,
  08-21, 08-31, 09-01, 09-02, 09-03, 09-04, 09-08, 09-09, 09-23 and 09-24.
- `global` on the same 11 dates: `point_class` carried (it serves Cottonwood's prior value inside the total).
- Sources: `fact_model_assignment` has no partition for 2026-08-31 to 09-04, 09-08, 09-09 and 09-10 (eight trading
  days; `comp-keys partitions`), which accounts for seven of the eleven. For 08-20, 08-21, 09-23 and 09-24 both silver
  tables have a partition and the point is still absent; that cause was not read.
- The frontier date advanced on each of those days. So `as_of_last` and `source_keys` move while the frontier point
  is null: AC2 as written, and AC7's read, both pass on a day when Cottonwood has no figure.

This is not the defect this project repaired (the holdings header contract; that table is complete on every trading
day). It is the same client-facing series, and channel row S19 (ARMED, 2026-08-27) already says two carries on the
served Global aggregate have no explanation. Whether "restore cottonwood and global served data to the correct T-1
frontier" (PRD section 2) is met by a series that is measured on 61 percent of days is a scope reading, and it is
`1.0.0_SA_CTO`'s: close this project and place F-A (and S19) as an order elsewhere, or hold the close on it.

## What you should have asked but did not

- **The criterion's instrument is blind to an absent point.** The PRD's class is "a served key rewritten daily with
  frozen contents passes every instrument". Its sibling is a served key whose date advances over a null. A frontier
  read that also checks the class of the last point (`point_class[-1] == measured`) discriminates both; it is one
  more field on the existing `comp-xray frozen` call, not a monitor.
- **Eight consecutive-looking trading days of a model-assignment pull were missed (2026-08-31 to 09-10) and the
  record of this project does not mention it.** Who owns the Rebalancer daily pull, and was that gap seen by anyone
  at the time?
- **The process cell is still unowned.** The registry row's `decomp_input_added` asks why a bronze-shape change
  shipped with no silver-contract step. The closure plan moves it to MDPF_CANON's decomposition as one line; it has
  no order today.

## Not verified by this seat

The byte comparison of AC4 and the frozen arm of AC7 (both held from 2026-08-25); the publisher's invocation record
for 2026-09-30 (the 13:50Z time and `written_at` are the basis); the cause of the four absent days whose partitions
exist; any Model Portfolios page render.

-- 3.0.0_SA_CVO
