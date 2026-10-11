# drive log -- 2.0.0_SA_COO~C2 -- 2026-10-11 11Z (desktop-n8rjv0a)

Counts, hashes and reason codes only.

- 11:0xZ | CB-bm-3 drained @803e5f2c14 after AMENDMENT 3 (the default leg stays method_r28, CTO msg 4772). Suite at the base then: 1 failed, 839 passed, 12 skipped (row D2-S113: the account-id scan counted 76 CUSIPs in the price-request lists as id shapes; an issuer defect, CB-bm-2 drained without a suite run). Round-65 packet @66db401fb2; the CVO graded both judgments; round-close r65 MAY-CLOSE.
- 11:1xZ | round 66 issued in ONE issuance @7dec032cc6, 2 of 2 chains: the r28-versus-r29 comparison and the scan repair.
- 11:3xZ | CB-bn-2 drained @5a8fd837ca; suite at the base 847 passed, 12 skipped; the scan prints 76 shape hits set aside as declared security identifiers in 2 files, 0 account-set hits.
- 11:4xZ | CB-bn-1: the positive control FAILED and the worker stopped, correctly (row D2-W97-S1): method_r28 re-run today differs from the served local table on 30 of 1,691,729 account-days; the split-history store read live from S3 lists 141 held CUSIPs against 32 at the served run. AMENDMENT 1 @e0aea14b12 (GATE (viii) on the modify): same inputs today, proven equal; the drift recorded. CTO msg 4844: pin the store FIRST; the 30 drift days are a second change; no re-mint order until both lists exist.
- 11:4xZ | tick 11. Issuer read: the store's bucket has versioning Enabled. Round 67 issued in ONE issuance @3e1c08668d, 2 of 2 chains: the pin (CB-bo-1) and the read on the added splits (CB-bo-2).
- 12:0xZ | CB-bo-2 drained @e7890e1cff: 109 partitions added 2026-10-10 02:33Z to 03:00Z; 4 move 3,034 price points; all four are spin-offs on independent evidence, every moved point before its date; all 30 drift account-days rest on them. Suite 847 passed, 12 skipped (run at the drain).
- 12:1xZ | CB-bn-1 drained @3a75bb973a: R28-VS-R29-RECORD control_rows=1691729 control_differing=30 rows_union=1691729 class_sum=1691729 both_measured_different=2 measured_r28_only=0 measured_r29_only=0 changed_account_days=2 changed_dates=2; inputs equal in 1 attempt; 0 month verdicts changed. Round-66 packet @eb8de12cd9.
- 2026-10-11T12:42Z | tick 12. Round-close r66 MAY-CLOSE. No new act owed; the pin worker is inside its tick.

Open at this seat: CB-bo-1 (the pin) running; round 67's judgment criterion goes to the CVO with its packet when the pin is terminal; the issuer's own hour-apart re-run of the valuation at the pin (CTO msg 4844 item 1). No re-mint order is cut. The default leg is method_r28. `dep_stage` not moved. No FWD is claimed REALIZED by this seat.

## Compiler Tools

- `safe-merge.sh`: six drains (96c, 98, 97 row-only, 100, 97b; all rc=0).
- `to-pipeline-gate.py` (through safe-commit): two issuances (r66: 2 orders; r67: 2); two amendments graded by GATE (viii) on the modify.
- `round-close-check.py`: r65 MAY-CLOSE, r66 MAY-CLOSE, r67 REFUSED (1 ungraded).
- Live AWS read by the issuer: `get-bucket-versioning` on the split store's bucket.
- The silver suite, run by the issuer at four drains.
