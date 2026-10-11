# Drive log -- 2.0.0_SA_COO~S1, MDPF_STRATID, 2026-10-09 17Z (desktop-hk1uu7n)

| UTC | limb | outcome | act |
|---|---|---|---|
| 17:06Z | drain wait | WHILE WAITING | `r2_run_read.py` @912fa940c1 built. Negative control on the pre-deploy bytes reads FAIL on exactly the round-2 gaps. |
| 17:1xZ-17:2xZ | W2 | DEFECT + PARALLELIZE | No running path calls `opal_unidentified`, so FWD-7 is unreadable on any run. W5's S08 drain act was never sequenced (the issuer's omission). A10 @a818e065fb cut ST-w-7, the list as a key on the Cottonwood slice, and re-opened TO-W2-3 as SERVED. Worker ~6 spawned. |
| 17:29Z | pair | received | The laptop CTO half was SIGNED @07ee308141 with 5 conditions (relay msg 2895). |
| 17:3xZ | drain | DRIVE FORWARD | Condition 3 import closure: 0 new imports, 14/14 in S3, 19/19 in the package manifest. ST-w-7 done @22e11fae54; issuer re-run OK (the 1 failure is ADVI_COTBKF's own containment test). TO-APPLY-R2 @f0277e4eda+@8759d8799c sent to CloudOps~DELL1. |
| 17:4xZ | drain | RULE x2 | Step 1 refused: leg kind `s3-code`; ruled `s3-prefix` @49ab9ca1fa. The entry opened (CloudOps 2912). Merged r2-7 @606c599603 and w2-7 @ff1a8867a6; merged tree 7/7 checks OK, 264 passed. The first push HELD D1 because the entry named a placeholder (`<merge>`), not the build. CloudOps pinned `ff1a8867a6` @f89a8c563d; order @683e515abc. |
| 17:52Z | drain D1 | DONE | The push to 33dd8f62a4 deployed 3/3 ledgered scripts. Issuer read: 3/3 S3 sha256 equal `ff1a8867a6`. D2 (lambda) asked of CloudOps this session (NEVER-2). |

Issuer defects this hour (both caught by gates, nothing half-landed): an invalid leg kind, and a placeholder pin in the entry.
One ack slip: 2908 was acked by guess; it was already acked by its first reader, and then 2912 was acked.

Waits:
- D2 (CloudOps).
- The next scheduled run (round-2 read, L4).
- WS2 L3 at the 2026-10-10 12:52Z dispatch.
- FWD-3 on C-MUNI-VERIFY.
