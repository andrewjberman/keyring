# drive log -- 2.0.0_SA_COO~C2 -- 2026-10-11 10Z (desktop-n8rjv0a)

Counts, hashes and reason codes only.

- 09:4xZ | round 64 drained 4 of 4 (packet @59f48b48ae): price coverage on 2026-05-06 (459 of 826 securities unpriced; 0 priced by the custodian's data or a store the build reads); the PRD states no income outcome for the table; the 24 flagged days in four classes, one a defect of the form; the test-only stamp switch removed. The CVO graded both judgments MET; round-close r64 MAY-CLOSE.
- 09:5xZ | row D2-S108: the method row is IRPT_DASHBD's producer output and stated income_basis cash_when_received for version 3. CTO: the fix is IRPT_DASHBD's cell. Read back by this seat at 10:46Z after that project's rewrite: income_basis null, claim absent, reason present; 0 other columns moved; mint verify 3325/3325 with sidecar and method row matching. Row D2-S112 @74144c06ec.
- 10:0xZ to 10:1xZ | four reads for the CTO on the Performance hop: year to date 9,613 of 80,390 account-days measured (659 of 769 accounts under a tenth); the walk's account by masked last-four has no 2026 row (join not established); the table ends 2026-06-22 because the source is ONE delivery as of 2026-06-23; bronze holds 5 objects, all that date; PRD line 119: a one-time backfill by design. CTO msg 4706: the hop's source is IRPT_BCKEND FWD-3 on the current feed, not this table.
- 10:2xZ | CTO ROUND-65 ANALYSIS @1e9128413f; round 65 issued in ONE issuance @c15e72c38f, 3 of 3 chains.
- 10:3xZ to 10:5xZ | CB-bm-3 (method_r29): three issuer defects -- one file granted of six needed (row D2-S111, AMENDMENT 1 @c06b93d147); the valuation script still ungranted (census then taken: 51 hits, 14 files of 407; AMENDMENT 2 @ccd8d1ce68); the code default moved ahead of the CTO's addendum (drain held; CTO msg 4772; AMENDMENT 3 @e3dd6c3e67). Each amendment graded by GATE (viii) on the modify. CTO msg 4734: r29 becomes the default by its addendum, after an r28-versus-r29 comparison; the re-mint covers exactly the changed days.
- 10:4xZ | tick 10. CB-bm-1 drained @80348d1900 (207 outlier days: 206 a credit on a leftover balance, 1 a defect of the form). CB-bm-2: the issuer's AC2 invocation was corrupted by its own template; the assignee repaired element and instance together; drained @9bb6681873 (Yahoo leg 3,102 securities, Bloomberg leg 1,306; written, NOT sent).
- 11:0xZ | CB-bm-3 drained @803e5f2c14. Suite at the base: 1 failed, 839 passed, 12 skipped (row D2-S113: the account-id scan counts 76 CUSIPs as id shapes; an issuer defect, CB-bm-2 drained without a suite run). Round-65 packet @66db401fb2 to the CVO. Round 66 issued @7dec032cc6, 2 of 2 chains: the comparison (~97) and the scan repair (~98).

Open at this seat: the two round-66 orders; round 65's two judgment criteria at the CVO; the suite red at the base on one test until CB-bn-2 drains. No re-mint order is cut. The default leg is method_r28. `dep_stage` not moved. No FWD is claimed REALIZED by this seat.

## Compiler Tools

- `safe-merge.sh`: nine drains (r64: 4; r65: 94, 95, 96b row-only, 96c), all rc=0.
- `to-pipeline-gate.py` (through safe-commit): three issuances (r64: 4 orders; r65: 3; r66: 2); three amendments graded by GATE (viii) on the modify.
- `comp-find`: one census (METHOD_R28|method_r28 over data/assets/scripts), denominator printed.
- `round-close-check.py`: r62 MAY-CLOSE, r64 MAY-CLOSE, r65 REFUSED (2 ungraded).
- Live AWS reads by the issuer: `s3api list-objects-v2` of one bronze prefix; `head-object` and `get-object` of two method-row keys, current and prior version.
- The mint adapter's `--verify-served`, twice (without and with the stamped manifest).
