# MDPF_STRATID -- L8 packet, round 2 (workstream 1) + workstream 2 amendment A10 -- PARTIAL (pre-run)

Compiled by `2.0.0_SA_COO~S1` 2026-10-09 ~18:1xZ. **UPDATE 2026-10-13 ~18:3xZ:** section 6 is filled (the 2026-10-12 and 2026-10-13
13:30Z fires, both clean), section 1's statuses are current, and both deploy ledgers are CLOSED. The packet is ready for the single
grading pass the pivot direction packet orders (`DIRECTION_DELL1_20261013.md` section 4, outcome O9); the file name keeps "partial"
because the runner-log half of workstream 2 is parked, not closed. It is read by `3.0.0_SA_CVO` by file.

## 1. Orders and status

| order | cell | serves | worker / applier | status | commits |
|---|---|---|---|---|---|
| `TO-ST-u1` (+A1) | ST-u-1 | FWD-2 | `0.9.0_WK_MDPF_STRATID~7` | complete | fab599bcea, e07705675e (A1), f1deec74b1 |
| `TO-ST-u2` | ST-u-2 | FWD-6 | `~7` | complete | c95ee45507 |
| `TO-W2-3` A10 | ST-w-7 | FWD-7 (and FWD-4's "listed" branch) | `0.9.0_WK_MDPF_STRATID~6` | complete | 0c72f3be00, 22e11fae54 |
| `TO-APPLY-R2` | deploy | ST-u-1, ST-u-2, ST-w-7 | `0.7.0_AE_CloudOps~DELL1` | complete 2026-10-13 (ledger CLOSED 2026-10-12; instance by the issuer, VALID; AC3 added for ST-u-2) | 6259c6efbf (CloudOps), merge ff1a8867a6, 3135df8e46 (flip) |
| `TO-APPLY-W2-b` | ST-w-6 | FWD-4 (S3 strategy list read) | `0.7.0_AE_CloudOps~DELL1` | complete 2026-10-13 (legs L1-L2 CLOSED 2026-10-09; instance by the issuer, VALID) | 3135df8e46 (flip) |

## 2. Mechanical criteria (issuer re-runs)

- **Merged tree `ff1a8867a6`** (2026-10-09 ~17:4xZ): 7 of 7 OK.
  - `st_u1_tests` `U1-OK`, `st_u1_seam` `SEAM-OK`, `st_u1_regress` `U1-REGRESS-OK`.
  - `st_u2_tests` `U2-OK`, `st_u2_seam` `SEAM-OK`.
  - `w2_7_tests` `W27-OK`, `w2_7_seam` `W27-SEAM-OK`.
  - Suites stratid + taxsma + wiring: 264 passed.
- **Seam arms on the served 2026-10-08 bytes:**
  - **A (as served):** Cottonwood divz 1,369,280.57 / overlap 1,369,280.57 is held out as `OVERLAP`, and pfde 410,420.98 is counted.
    The Global total is 2,147,378,054.74, unchanged.
  - **B (planted divz overlap 0):** Dividend SMA = 17,079,326.24 + 1,369,280.57 = 18,448,606.81, and the total rises by exactly
    +1,369,280.57. Client is unchanged and nothing raises.
  - **u2:** the divz row shows `held_out [{cottonwood, 1369280.57, OVERLAP}]` and `inside_model_figure True`; pfde shows
    `held_out []`.
  - **w2_7:** `as_of` 2026-10-08, names_scanned 18, listed 1. The planted "Opal Frontier Sleeve" (1234.56) is listed `NO_MEMBER`,
    and the control is clean.

## 3. Rows (surprise channel `INVESTIGATION_v1.md`)

- `MDPF_STRATID-D1-W7-S1`: round-1 test asserted Cottonwood undeclared. RESOLVED by A1 @e07705675e, re-point @f1deec74b1.
- `D1-W7-S2`: the sleeve fold skips the Tax leaf. ACCEPTED (A1).
- `D1-W7-S3`: `by_firm` assertion strengthened. ACCEPTED (A1).
- `D1-W7-S4`: unmeasured overlap is named in `held_out`, and the bool reads False. ACCEPTED (A1).

No BLOCKING or ARMED row is open from this round.

## 4. The deploy (never-widen pair, C-GLOBAL-PAIR)

- **Pair and halves:**
  - Pair `deliverables/2.0.0_SA_COO~S1/NEVER_WIDEN_PAIR_R2_COTTONWOOD_OUTSIDE.md` @c4fdec2ec7, COO half signed.
  - Read sound by `1.0.0_SA_CTO~DELL1` @2f20db8e0f.
  - CTO half signed by laptop `1.0.0_SA_CTO` @07ee308141, with 5 conditions.
- **Condition 3, import closure:** 0 new imports; 14 of 14 gold modules present in S3; 19 of 19 named in the package manifest.
- **Condition 4, entry:** `org/critical_paths/change_management/20261009T1743Z_mdpf-stratid-r2-global-fold_deploy_completion.md`,
  author CloudOps~DELL1. L1-L3 and tf-lambda are CLOSED; L4 is OPEN, the issuer's.
- **D1 (17:52Z push 33dd8f62a4):** the 3 keys' sha256 equal `ff1a8867a6`, read by the issuer and CloudOps.
  - `consolidator 3d78e955..`, `registry 46cd1672..`, `slice 7ab6f5ce..`.
- **D2 (18:00:35Z):** the live `mdpf-gold-lambda` package's 3 changed files equal the pin, on the issuer's own download.
  CodeSha256 `yl8hYA+u..`. Re-plan: no changes.
- **Issuer defects caught by gates, nothing half-landed:**
  - leg kind `s3-code` refused at open (ruled `s3-prefix` @49ab9ca1fa);
  - the entry named a placeholder, not the build, so the first push held D1 (pinned @f89a8c563d).

## 4a. Post-deploy defect and its forward fix (rows D1-S7 ARMED -> D1-S8 DISARMED; the issuer's defect)

- **20:14Z:** CloudOps' qa_local on the deployed lambda failed the cottonwood scope (global skipped). The ST-w-7 slice imports
  `opal_unidentified`, which was in neither home (lambda package; runner `code/scripts/{silver,assets_gold,gold}` 404 x3).
  **Cause:** the CTO-condition-3 closure was read for the consolidator and registry, not for the slice.
- **F1 and F2:**
  - **F1 (20:30:33Z):** module first-minted to runner silver; sha256 `6b9c1d7f` equals the pin. Isolated import of the runner S3
    copies: IMPORT-OK.
  - **F2 (20:36:03Z, @79e30151a6):** package line added.
- **F2 exposed the L-1 key-set failure.** `unidentified_strategies` sat on Cottonwood only, so a run would put 0 of 16, and on ANY
  package once the 12:52Z dispatch writes the key.
  - **Ruled:** pad the key to every scope (ST-w-8, A11 @f1d54b1c0b; stale round-1 assertion updated under A11.1).
  - **Merged @88e974ca10:** all checks OK, 267 passed.
- **F4 (lambda at `88e974ca10`, 21:10:34Z):** qa_local green, 16 of 16, errors `[]`, L-1 identity PASS on 4 of 4 types. The issuer's
  content read of the package: 4 of 4 files equal the pin.
- **F3 (runner consolidator, 21:36:52Z, direct safe-deploy under CTO~DELL1 msg 3224):** sha256 `2cd88dc4` equals the pin. Entry
  `mdpf-stratid-r2-keyset-f3f4-dell1-20261009` CLOSED 4 of 4.
- **No scheduled run used a broken build,** and no served artifact was written by one.
- **L4 re-pointed** at `55c3cc4642`, then `88e974ca10` (MDPF_CANON's additive consolidator change; round-2 seams re-run OK on it).

## 5. What the run must show (conditions 1, 2, 5 of the CTO half)

Read by `deliverables/2.0.0_SA_COO~S1/r2_run_read.py` @b5f8c2460b. The negative control on the pre-deploy bytes reads FAIL on exactly
the round-2 gaps.
- **FWD-2:** every Cottonwood sma member with a value is counted at Global or named withheld; none is silent.
- **FWD-6:** every Global SMA tree row states `inside_model_figure` and `held_out`. The divz row shows its held-out line, by name and
  value (condition 2).
- **FWD-7:** the Cottonwood slice carries `unidentified_strategies` (names, dollars, reasons) with names_scanned > 0.
- **Total and Client:** Global total = base + tax + sma within a cent, and Client equals 268,516,586.73 where the date is unchanged.
- **Condition 1:** a per-firm move on the prior frontier date is graded against check A's restatement baseline (@5a151aacea), not
  against this fold.
- **Condition 5:** evidence carries totals, counts, names and sha256 only, never an account id.

**Fires:**
- Workstream 2 leg L3 (silver list read) and ST-w-7 (the slice's first scheduled build): the runner dispatch,
  `mdpf-feeder-backstop-daily` 2026-10-10 12:52Z.
- Round 2 leg L4: `mdpf-scheduled-floor` 2026-10-10 13:30Z. Saturday's run date is Friday 2026-10-09 (T-1, trading calendar).

## 5a. FWD-3 (restated in PRD v0.6 @ccbb31e15e, unblock UB-20261009T183753Z-5e37)

- **The restatement.**
  - DONE WHEN = (i) a planted Muni sleeve run through the production fold and routing code on copies of the served bytes, plus
    (ii) the organic read on the scheduled run. ACCEPT is unchanged.
  - Ratified-text half re-signed by `3.0.0_SA_CVO` @9794664db4. Fold by `1.0.0_SA_CTO~DELL1` (msg 3018). Case CLOSED/resumed
    with `--wait-until 2026-10-10T13:30Z`.
- **Mechanism arm (i): MET** (CVO grade @8125d09ffe).
  - `R2_CHECKS/st_r2_muni_seam.py` @283515b4c3 prints `R2-MUNI-SEAM-OK`. It calls production code byte-equal to the deployed pin
    `ff1a8867a6`.
  - Control: no Muni dollars.
  - Add: ALT Strategies > Muni 550,823.07; total +550,823.07 exactly.
  - Hold: total unchanged; named `OVERLAP` on the tree row.
  - Cottonwood view: ALT Strategies > Muni 550,823.07.
- **Organic arm (ii): PENDING**, read on the 2026-10-10 13:30Z run. Expected "no Muni SMA dollars", per the CRO census @2bb6b38092.
  `Opal_Muni_Sleeve` stays kept out with its reason until call `203a`. That call decides the sleeve's membership, not FWD-3's
  grade.

## 6. The one real run -- READ 2026-10-12 13:30Z (workstream 1 L4); workstream 2 L3 runner half still OPEN

Full read: `deliverables/2.0.0_SA_COO~S1/R2_RUN_READ_20261012.md`. The 10-10 and 10-11 fires refused Global at the cross-axis gate
(rows D1-S9, D1-S10, UNREAD, not failed). The 2026-10-12 13:30Z fire built 16 of 16, `errors=none`, and wrote Global 2026-10-09.json.

| item | read | class |
|---|---|---|
| FWD-2 | divz held out `OVERLAP` 1,370,211.85; pfde counted 411,720.53; none silent | MEASURED |
| FWD-6 | divz row `inside_model_figure=True` with its held-out line by name and value (condition 2); every SMA row states both fields | MEASURED |
| FWD-7 | `unidentified_strategies` as_of 2026-10-09, names_scanned 18, `Opal_Muni_Sleeve` 553,337.61 `RULE_NOT_COUNTED` | MEASURED |
| Total | 2,172,724,681.31 = base + tax + sma within a cent; Global history 0 diffs on 493 common dates x 4 series | MEASURED |
| Condition 1 | CTO-ruled per-firm read (@5a151aacea) clean on 49financial, inflection, cottonwood; 49financial by_model 1.99 vs model_aua 1.98 | MEASURED |
| FWD-3 organic | Global `muni` row 0.00, `held_out=[]`; the sleeve is on the unidentified list | MEASURED, grade is the CVO's |
| Client | **NOT GRADED** on the served objects: served as_of 2026-10-09 vs the 268,516,586.73 figure's as_of 2026-10-08; no same-date pre-deploy Client exists. The fold's effect on Client IS exercised on one date, with and without the fold, by seam arm B (planted divz overlap 0: total +1,370,211.85 exactly, "Client unchanged"; `st_u1_seam` SEAM-OK re-run 2026-10-13 on the live bytes) | ABSENT on served; MEASURED on the seam |

- **Issuer defect:** `r2_run_read.py` applied the Client clause with no date guard against the packet's "where the date is unchanged";
  amended with a date guard and a NOT-GRADED line, controls in the read page. The CVO rules whether NOT-GRADED stands or a QA run of
  the pre-round-2 pin on the 2026-10-09 inputs is owed.
- **Ledger:** `mdpf-stratid-r2-global-fold` CLOSED (all 5 legs). `mdpf-stratid-w2-wiring-silver` L3 stays OPEN: Stage 6 dies at
  `lib.opal_naming` before step 6d on the runner (MDPF_TAXSMA-S5, ARMED, owner `2.0.0_SA_COO~T`; row D1-S10), so no dispatch can show the
  6d log until S5 is disarmed. The served-slice half of L3 is read and equal.
  - **Parked, owner and condition (2026-10-13, `1.0.0_SA_CTO~DELL1` msg 4774):** S5 is re-owned to `2.0.0_SA_COO~D1`, the runner
    code sync (MDPF_CANON round-5 ADDENDUM 3). L3's runner-log read un-parks when that sync makes Stage 6 reach 6d; the reader is
    this seat, the first dispatch after the sync is the read.
  - **L3 AMENDED AND CLOSED (2026-10-13 ~11:2xZ, CTO ruling msg 4779, read `2.0.0_SA_COO~D1` round6/STRATID_W2_L3_NEED_READ.md):**
    a lib sync is necessary and not sufficient, because Stage 6 also stands behind C2 AccessDenied `s3:ListBucket` and the cross-axis
    gate, and M10 retires the stage. Ledger `mdpf-stratid-w2-wiring-silver` is CLOSED on the served half (MEASURED: the served slice
    reads the S3 list, 16 keys, sma members divz and pfde equal, 0 of 493 cells differ) plus the in-memory QA read (the driver was session
    scratch, so the served half is the stronger evidence). The runner-log half is PARKED, not closed: owner `2.0.0_SA_COO~D1`,
    condition "M10's producer order runs step 6d's successor", reader this seat. Gate limb: none grades a ledger-leg amendment.
