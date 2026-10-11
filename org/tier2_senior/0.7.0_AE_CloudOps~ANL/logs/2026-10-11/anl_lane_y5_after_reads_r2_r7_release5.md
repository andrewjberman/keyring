# Release 5 after-reads R2 to R7 on irpt-status Iw3FADFr: R2 R3 R5 R6 R7 true, R4 ABSENT -- 0.7.0_AE_CloudOps~ANL

**Date:** 2026-10-11
**Task Order:** IRPT_ANLREQ.TO-READS-Y5
**Status:** COMPLETE (measured; the `<status>` flip is the issuer's)

**archetype:** VALIDATE

---

## Objective

Run the release 5 after-reads R2 to R7 of `irpt-status` build `Iw3FADFr...` from the laptop, which holds the `irpt-requests` decrypt.
Read-only. Follows the gate-closed log `anl_lane_y5_gate_closed_before_arms_rev6.md`.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-iam / comp-blast / comp-routes / comp-cache / comp-schedule | -- | SKIPPED | the order declares each not applicable or run by reading |
| get-function-configuration | `.tools/aws lambda get-function-configuration --function-name irpt-status` | `Iw3FADFr...` LastModified 2026-10-11T10:25:40Z | step 0, read by this seat at 10:44Z after the issuer's GO (msg 108304) |
| snap.py | `python -I .../y5_scripts/snap.py <out>` | R2 R3 R4 R5 snapshot | diffed against `Y5_before_arms_rev6_snapshot.json` |
| apply5_checks.py | `python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r3/apply5_checks.py reads --root .` | `APPLY5-READS-OK` | see Gap found |

**What worked:** the BEFORE snapshot taken while the gate was closed made R2, R3 and R5 a per-request diff: the same 50 accepted
requests, the same readable 14.
**What failed:** nothing in the reads.
**Gap found:** run exactly as the order prints it (no `--root`), `apply5_checks.py reads` prints `no .../Y5_after_reads_result.json` and
`APPLY5-READS-FAIL`: its default root is `Path(__file__).resolve().parents[8]`, which is `.../ajb_workspace/org` at this depth
(`parents[9]` is the workspace). With `--root .` it prints `APPLY5-READS-OK`. Reported to the issuer.

---

## Verification

| Read | Result |
|---|---|
| 0 gate | `CodeSha256` `Iw3FADFrSt5G97zRTSkvZ7txSlXnaNQNpgPZi+G5tw0=`, LastModified 2026-10-11T10:25:40Z, Active / Successful |
| R2 TRUE | 14 of 14 readable requests (cottonwood, YCHARTS form) now carry `retained_ref` (0 of 14 before); body without `retained_ref`, `sections` count and `request_ref` equal by digest; 0 `READY_REPORT_RECEIPT_REQUIRED` over 50 reads |
| R3 TRUE | history rows 40 before and 40 after (cottonwood 39, inflection 1), same row identities by digest; every row carries `client_id` and `client_claim` (UPLOAD 40, SELECTED 0, UNREADABLE 0); `unreadable_rows` 0 |
| R4 ABSENT | no readable OPAL_ENGINE request: 50 accepted scanned, 14 readable, 0 OPAL_ENGINE. REQ-5e4149d2863aea31cc87d660 answers FIRM_BINDING on sections and status-job, so its provider is NOT MEASURED. ABSENT is not a pass of that branch |
| R5 TRUE | section-date read with `x-irpt-status-dates: prospect-v1`: 0 of 50 requests changed against revision 6; the 14 readable are READY / PER_SECTION on both builds |
| R6 TRUE | 3a signed link answered, fetched bytes hash equal the response and the retained original (`bc9bdfb7...`), link discarded, expiry only recorded; 3b both arms refused (NOT_AUTHORIZED, FIRM_BINDING); 3c null (0 of 10 49financial compositions lack browser.input_id); 4_record true (0 schema errors); 4_route true (5 APIs, 133 routes scanned, `/original` declared 1 time) |
| R7 TRUE | 3 object versions before and 3 after, under the three artifact directories the `/original` read resolves for REQ-4b5155ac2ea9467ab771b414 in `opal-data-irpt`; DynamoDB tables were not counted |

Denominator: 1894 irpt-requests items scanned over 2 pages; 50 `analysis#REQ-<24hex>#1` records (cottonwood 39, 49financial 10,
inflection 1). The 49financial history reads answer FIRM_BINDING or NOT_FOUND on owner replay and carry no rows in R3.

---

**AMENDMENT 1 (@f4176d55a2) and the root fix (@e678c59c59), 11:0xZ.** The issuer fixed `apply5_checks.py` line 52 to `parents[9]`; the
criterion now prints `APPLY5-READS-OK` run verbatim, no `--root`. Added `reads.R2.section_unit_read` over the 14 READY reports: 988
sections, units pct 513 / number 224 / ratio 102 / chart 51 / count 46 / years 22 / score 15 / price 15 (sum 988); value types number
937, string 0, null 51 (the 51 chart sections); the percent unit is `pct`: 88 values with abs below 1 (includes any zero), 425 with abs
1 or more. Counts and unit strings only. The proof instance records the verbatim invocation and the amended order's vintage.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| R4 recorded ABSENT, not true | the order's own rule: REQ-5e4149d2 only "if readable"; none was |
| R3 rows summed over the two tenants that answered | no single readable owner spans both; scope text in the file says so |
| Did not retry any read | none was false |

---

## Files Modified

| File | Change |
|---|---|
| `org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/Y5_after_reads_result.json` | the result (new) |
| `org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/IRPT_ANLREQ.TO-READS-Y5.release5-after-reads-laptop.proof_of_spec.json` | the proof instance (new) |
| this log | new |

NO AWS resource, policy, object, table row or Lambda was created, modified or deleted.

---

## Blockers

None for the reads. Open for the issuer: R4 is ABSENT because REQ-5e4149d2 is not readable by owner replay from the laptop.

---

## Current State

Lane `0.7.0_AE_CloudOps~ANL` live, one inbox watcher armed, zero crons. Order measured; the check line reads `APPLY5-READS-OK` with `--root .`.

---

## Next Steps

1. `[2.0.0_SA_COO~Y2]` Rule on R4 ABSENT; fix the default root in `apply5_checks.py` (`parents[9]`); flip `<status>` on TO-READS-Y5.
2. `[0.0.0_AB_MSTR]` Carry the box/laptop commit to CLOUD at the next box-sync; this seat does not push.
