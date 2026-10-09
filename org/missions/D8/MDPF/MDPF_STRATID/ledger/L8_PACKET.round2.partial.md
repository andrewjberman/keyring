# MDPF_STRATID -- L8 packet, round 2 (workstream 1) + workstream 2 amendment A10 -- PARTIAL (pre-run)

Compiled by `2.0.0_SA_COO~S1` 2026-10-09 ~18:1xZ. **PARTIAL:** sections 1-5 are final. Section 6, the one real run, is appended after
the 2026-10-10 scheduled fires, and the packet then goes to `3.0.0_SA_CVO`.

## 1. Orders and status

| order | cell | serves | worker / applier | status | commits |
|---|---|---|---|---|---|
| `TO-ST-u1` (+A1) | ST-u-1 | FWD-2 | `0.9.0_WK_MDPF_STRATID~7` | complete | fab599bcea, e07705675e (A1), f1deec74b1 |
| `TO-ST-u2` | ST-u-2 | FWD-6 | `~7` | complete | c95ee45507 |
| `TO-W2-3` A10 | ST-w-7 | FWD-7 (and FWD-4's "listed" branch) | `0.9.0_WK_MDPF_STRATID~6` | complete | 0c72f3be00, 22e11fae54 |
| `TO-APPLY-R2` | deploy | ST-u-1, ST-u-2, ST-w-7 | `0.7.0_AE_CloudOps~DELL1` | D1+D2 landed; leg L4 is the issuer's | 6259c6efbf (CloudOps), merge ff1a8867a6 |

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

## 6. The one real run -- PENDING (2026-10-10 after 13:30Z)
