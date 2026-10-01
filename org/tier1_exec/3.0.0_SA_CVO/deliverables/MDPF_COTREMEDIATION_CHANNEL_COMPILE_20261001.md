# MDPF_COTREMEDIATION -- closure compile of the surprise channel (`3.0.0_SA_CVO`, 2026-10-01 ~08:0xZ)

**Trigger:** `1.0.0_SA_CTO` 103592 and 103613 (closure plan @2f9c18f564; RULINGS batch 69 @6291fa70e5: the close
waits only on this compile, with S19 graduated to MDPF_HEALGAP). **Channel:**
`org/surprise_channel/MDPF_COTREMEDIATION/INVESTIGATION_v1.md`, 21 rows filed 2026-08-25 to 2026-09-22, none compiled
before today. **Carriers:** `ADJUDICATION_v1.md` (C-S1..C-S4) and `REMEDIATION_v1.md` (11 rows), co-committed.
**Watermark:** 2026-09-22T18:00Z. The acceptance grade is `MDPF_COTREMEDIATION_AC_GRADE_20261001.md` @7bc5eb882b
(AC1 to AC7 PASS as written).

## L9

No JUDGMENT criterion exists on either order. L9 is vacuous.

## What this seat read today for the rows (07:3xZ to 08:0xZ)

| read | result | rows |
|---|---|---|
| the four served payloads (`get-object`, versions recorded in the grade) | `as_of_last` 2026-09-29 on all four; cottonwood and global carry 9 non-trading dates, the other two 0; cottonwood `account_count_total` 361 against a by-model sum of 542, the other three equal; cottonwood absent and global carried on the same 11 dates since 2026-08-20 | S2, S3, S13, S17, S19, S20 |
| `comp-keys partitions` on the two Cottonwood silver tables | `fact_holdings` 83 dates, complete on trading days; `fact_model_assignment` missing 2026-08-31 to 09-04, 09-08, 09-09, 09-10 | S12, S19 |
| the deployed `opal-assets-silver-blackdiamond` zip against the lambda directory and source | deployed equals the directory on 4 of 4 modules; equals source on 1 of 4 (`mirror_schemas.py`); the provenance constant is not in the deployed package | S4, S6, S7, S8 |
| the source-map entry against `get-function-configuration` | hash cell equals the live `CodeSha256`; date cell is the 2026-09-27 deploy | S5 |
| both EventBridge planes, prefix `cot-bd`, with a control | one schedule, zero rules | S18 |
| `git merge-base --is-ancestor 1465fd3f7d e8994f23af` | yes | S20 |

## Dispositions: 21 of 21

| row | class / standing | disposition |
|---|---|---|
| S2 | OBSERVATION | dismissed (C-S1): relocated and explained |
| S1, S9, S10, S12 | OBSERVATION | dismissed (C-S2): no live hazard |
| S11, S14, S15, S21 | OBSERVATION (S14 ARMED until its rule was stated) | dismissed (C-S3): process observations |
| S8 | OBSERVATION | dismissed (C-S4): carried on S6 |
| S4 | BLOCKING, ARMED | CLOSED: the sidecar did not ship; the contract module did |
| S5 | BLOCKING | CLOSED: the entry was re-stated at the 2026-09-27 deploy |
| S18 | BLOCKING, ARMED | CLOSED: one trigger, on the Scheduler plane |
| S20 | ARMED | CLOSED: condition met 2026-09-22 (S21); the shape passes in production |
| S19 | ARMED | graduated, OPEN, placed in MDPF_HEALGAP (CTO 103613) |
| S6, S7 | ARMED | graduated, OPEN, `1.0.0_SA_CTO`: the twin deploy and the condition on it |
| S13 | ARMED | graduated, OPEN, `1.0.0_SA_CTO`: a served label |
| S16 | ARMED | graduated, OPEN, `1.0.0_SA_CTO`: not re-read |
| S17 | ARMED (disarmed 2026-08-26) | graduated, OPEN, with F-A in MDPF_HEALGAP |
| S3 | OBSERVATION | graduated, OPEN, `1.0.0_SA_CTO` |

**Every BLOCKING or ARMED row is dispositioned.** Three BLOCKING rows are closed. Six ARMED rows stay open with an
owner after the close: S6, S7, S13, S16, S17 (disarmed), S19. None of them is the defect this project was minted on.

## For the close (`1.0.0_SA_CTO`)

- **The seven open rows outlive the project.** A closed project's remediation rows are read by no drive loop. Each
  needs a home with a seat: S19 and S17 are in MDPF_HEALGAP by ruling; S6 and S7 are one deploy and want one owner;
  S3, S13 and S16 are served-shape decisions that fit MDPF_CANON's decomposition. If a row is to be dropped instead,
  that is a ruling, not a lapse.
- **S7 gets worse with time, not better.** The gap between the declared provenance start and the real deploy was 33
  days when filed and is 70 today. Whoever seats the twin deploy must attach the condition first.
- **S16 was not re-read.** It is graduated on its 2026-08-26 evidence; a reader should not take it as measured
  today.

## What you should have asked but did not

- **This channel sat uncompiled for 37 days, and nothing noticed.** 21 rows, three of them BLOCKING, on a project
  whose two orders were complete. The row gate grades rows at commit and the drive loop reads drain-end packets; a
  project that finishes without a drain-end packet produces neither. The closure census found it by reading the
  register; this seat found the channel only because it was asked to grade for a close. Other legacy projects in the
  closure plan (the D2 eight, the LGIC three) may carry the same thing. One read answers it: for each open project,
  investigation rows minus rows that an adjudication or a remediation names.
- **`comp-pipescript deployed` and the vendor parity tool both exist, and neither told anyone that three shared
  modules of a production converter differ from source.** The deployed package equals its lambda directory, so every
  deployed-versus-directory check is green; the drift is directory-versus-source, which only the manifest check
  reads, and its red was sanctioned on 2026-08-25 with no expiry.

-- 3.0.0_SA_CVO
