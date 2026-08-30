# 4.0.0_SA_CRO -- session log 2026-08-30 01:54Z-02:20Z: ADVI_BDPARITY rider-4 probe-account SELECTION (COO-seated, D2-T70-1)

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE

## Session summary

Seated by `2.0.0_SA_COO` 84206 on `3.0.0_SA_CVO` verdict D2-T70-1: ADVI_BDPARITY.P1-PROBE rider-4
probe-account SELECTION ONLY (C1). The two methodology cells were FROZEN INPUT @`f11fb765ad` (+ annotations
1 @`3fc9752c58`, 2 @`30d51fcbac`); nothing in this session ruled, remarked on, or re-opened them. 83415 was
read as history per the issuer. No PERFRP-subject content handled (84206 C2). No vendor call.

Deliverable: five probe accounts with the attribute each was picked for, committed @`7cd0cc1200` and sent
to the issuer, the puller and the C3 grader (84378-84380).

## Work done

1. Startup per `org/XXX.md`: registered (PID 79044), session serial file written, A.2 invoker (the two
   OWNED findings only -- not re-filed), A.3 PATH 105/105 + exercised, pre-commit hook present,
   `.agent_context` set, `/watcher` armed Monitor task `bsbem39g9` (confirmed `running`). ZERO crons.
2. Read at source: candidates table @`da93bcacfc` and @`b29b9f849b`; P1-PROBE face + A2/A3 amendment;
   convention pre-registration @`c7bfcb2917` (rider 4, C5, A3 item 4, A5); the frozen ruling + annotations;
   TaxSMA roster JSON (5 entries, 3 active); DS~C 84281 (535/535 first-appearance sweep); CVO 84210, 84354.
3. Measured on our gold (zero egress): fee/flow/days_ok for the three roster accounts over 37/37 window
   partitions with the three table rows as positive controls (3 of 3 reproduce the table exactly);
   positions on 2026-08-28 (103,351 rows / 6,185 accounts); flow_ledger EXTERNAL rows joined to twr
   (roster "flows" are zero-value in-kind rows); population denominators re-derived (7,441 / 6,193 fee /
   1,248 non-fee / 1,510 flows / 5,931 no-flows -- identical to table s.4); xref resolution of all picks
   (6,201 rows); a measured non-fee/no-flow alternate (`0035153269`, median of 9 meeting the filter, 101
   unfiltered).
4. Wrote + committed `org/tier1_exec/4.0.0_SA_CRO/deliverables/ADVI_BDPARITY_P1_PROBE_SELECTION_20260830.md`
   @`7cd0cc1200`; sent the RAVC report (84378-84380); acked the 10 broker messages read in full
   (84206, 83415, 83419, 83560, 84210, 84263, 84281, 84295, 84336, 84354) -- 24 older drain ids left
   unacked because only their subjects were seen.

## The selection (account | bd_internal_id | picked for)

| # | account | bd | picked for | recency source |
|---|---|---|---|---|
| 1 | 0022312917 | 13477111 | C5 specimen (pre-registered A3-4; rb_share 0.8982; fee 2 / flows 0) | -- |
| 2 | 0038836097 | 18927251 | C3 multi-security + FI (80 positions) AND flows (4 EXTERNAL days) | -- |
| 3 | 0010083855 | 21089351 | C2 fee off-quarter, no flows, zero rate-bearing; C2 TEST unavailable until gross-leg re-emission | -- |
| 4 | 0027265115 | 22596361 | inception-recent, KNOWN BD inception | BD SI start 2026-03-16 (bronze); ours first-linkable 03-17; ADMISSIBLE (84354) |
| 5 | 0076459710 | 23221671 | inception-recent, most recent on our plane; in-kind external event | first present 2026-07-01, first linkable 07-09, 37 days (84281) |

Judgment calls recorded in the file s.3: C5 specimen kept as registered (signature separation over
decomposition at P1); two inception-recent members because KNOWN-anchor and RETURNED-anchor are different
tests; non-fee deliberately left to P2 with a swap rule. C4 not identifiable from our gold -- stated.

## MCP traffic

Received 8 live (84206 spawn-direct, 84210 grader's note, 84263/84295 window OPEN/CLOSE, 84281 sweep,
84336 annotation, 84354 annotation 2, plus the 02:20Z OPEN); 4 history (83415, 83419, 83560, 08-26
items). Sent 2: RAVC ACK (84249-84251) and RAVC REPORT with 3 INERT surprise lines (84378-84380).

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| comp-which | `comp-which "how do I grep the repo"` (A.3 exercise) | PASS | forwarder ran, banner produced |
| comp-find | `comp-find -i "pre-registration" --files` | WARN | exceeded 120s, backgrounded; the file was located by native Grep instead (Rule 21 nudge-and-proceed) |
| safe-commit.sh | risk-reflex 1 file vs 1,838 danger nodes CLEAN; commit-gate checked 0 of 1 (.md falls through, not cited as validation) | PASS | @`7cd0cc1200`, msg-verify MATCH len=2132 |

What worked: the table-row positive control (3 of 3) made the roster attributes citable on DS~C's own
definitions without a shared code path. What failed: a bare column list over the window tripped on the
2026-08-18 partition (schema is 10 of 14 columns) -- read schema-tolerantly. Gap found: none in the tools;
one instrument observation on the data (below).

## Surprise channel (OBSERVATION / INERT, sent in 84378-84380)

1. `twr_daily date=2026-08-18` schema lacks `bmv/emv/cf_net/cf_gross` outright (not merely null-typed).
2. `dim_account_xref 2026-08-28` `account_is_open` NULL for `0027265115`.
3. `canonical_positions 2026-08-28` one `rate_bearing` NULL position on `0038836097`.

## Blockers

None at this seat. The pull (GATE 1, vendor egress) is Andrew's word to `0.4.0_DS_ClientPlatform~C`, not
a blocker on this face.

## Addendum 02:22Z-02:25Z (before the log commit)

- **C3 GRADED PASS** by `3.0.0_SA_CVO` 84418 (checked at the grader's seat: file EXISTS at 7cd0cc1200, 160
  lines, five picks + alternate present, client names 0/0/0 against a positive control of 4). Issuer
  `2.0.0_SA_COO` 84428 ACCEPTED the selection as delivered, no non-fee swap at P1.
- **BLOCKING/ARMED surprise (DS~C 84436), disarmed same turn by the issuer (84471):** the DEPLOYED
  `opal-assets-bd49f-reporting-pull` (CodeSha256 `0XJf+G2p...`, 2026-08-28T18:09:29Z, `DRY_RUN="0"`)
  predates the BP1-1 commit @`27af942259` by 31h -- firing would spend Andrew's ONE pull on 2 of 4 ruled
  periods with no index join. This seat sent one relay line (84478-84480): the GO's "DRY_RUN still 1"
  described the repo, not the running artifact; concur the Terraform deploy + sha read is the disarm
  (owner `0.7.0_AE_CloudOps~K`, staffed by COO). No gate implemented here.
- DS~N 84426 closed my surprise line (i) at the engine: the 10-column shape is the documented all-refused
  write (`tests/test_c02_twr_engine.py::test_all_refused_frame_omits_the_operand_columns_entirely`);
  2025-01-09 is a market closure; only 2026-08-18 remains a candidate defect (C02-g-2).

## Current State (for a reader with zero context)

- Selection FILE: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ADVI_BDPARITY_P1_PROBE_SELECTION_20260830.md`
  @`7cd0cc1200`, author `4.0.0_SA_CRO`. **PUSH STATE: on origin @`9fb8236299`** (MSTR CLOSE 84448, ls-remote
  02:21:32Z; own `git fetch` + `merge-base --is-ancestor 7cd0cc1200 FETCH_HEAD` rc=0 at 02:24Z, bogus-hash
  control fatals).
- Grading: C3 PASS (84418). Release clause C4: if Andrew answers D2-T69-R2 YES, this seat is released and
  the file stands as the record.
- The pull (BP1-2) is HELD by the issuer (84471) until the deployed puller's CodeSha256 changes and
  post-dates 27af942259; the cohort it fires on is this file's five.
- The three roster accounts' full attribute rows and the alternate are in the file s.1/s.4; the
  measurement definitions and controls in s.5.

## Next Steps

1. [`3.0.0_SA_CVO`] grade the selection on C3 (member present, recency measured, attribute printed).
2. [`0.4.0_DS_ClientPlatform~C`] BP1-2 probe table on the five, when GATE 1 (Andrew) opens; the
   swap rule in file s.4 needs no re-measurement if the issuer wants non-fee at P1.
3. [`2.0.0_SA_COO`] the non-fee-at-P1 call (s.3c) if wanted; otherwise nothing owed to this seat.
4. [`4.0.0_SA_CRO`] commit this log at the 02:20Z window CLOSE (hold observed); then event-driven via the
   inbox Monitor.
