# Deploy Completion Record
**Date opened:** 2026-08-29T02:46:12.358918+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260829T024847Z
**Deploy:** D1_CATVIEWS rebuild #3: mdpf-gold-lambda repin to 73c2dea263 (item 1 GLOBAL leg, shape B). Both touched files are PACKAGED members, so the 9dcc87dd5b build is stale by this commit -- fires BEFORE any reserved delete so Andrew's word is spent once, on a build containing every fix.
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-data-assets portal/gold/mdpf/_code/mdpf-gold-lambda.zip re-uploaded at the new pin | builder zip_sha256 equals the DOWNLOADED-BACK served object sha256, and head-object metadata content-sha256 carries the same hex | VersionId Mpv.veBsx7I42MEiMhWUkttFFfvBaqL1, 834732 bytes. DOWNLOADED BACK and re-hashed: sha256=53ff3b33534103fc46f7c910dd96a29393b68e01ff198f0fb36768211ccb7210 == builder sealed zip_sha256, round-trip identical. Prior VersionId mwfjwbJag2Enrony7iLZYxLzunCMX3WI retained as the same-window rollback handle. | CLOSED 20260829T024715Z |
| L2 | activation | terraform safe-apply repins aws_lambda_function.mdpf_gold | apply rc plus 0-diff replan | safe-apply rc=0 (HALT_ACK=1; the gate surfaced the SAME two 7d-old withdrawals as rebuild #2, re-read fresh rather than assumed unchanged -- I ran it WITHOUT HALT_ACK first precisely so a NEW message could not be waved through). Apply complete: 0 added, 1 changed, 0 destroyed. Diff = source_code_hash ce654e87 -> 53ff3b33 and s3_object_version mwfjwbJa -> Mpv.veBs. Targeted replan after: 'No changes. Your infrastructure matches the configuration.' Terraform-only per NEVER#9. | CLOSED 20260829T024847Z |
| L3 | verify | CodeSha256 CHANGED from zmVOh+naGSCZPQ8ia7lQy/lxGhZ6Wu43g/sSltyTMww= AND the 22-module audit returns 22 IDENTICAL 0 DRIFTED at the NEW pin | per-module sha256 read from the package DOWNLOADED FROM THE FUNCTION vs sha256sum of git show pin path, denominator printed, negative control run | CodeSha256 zmVOh+naGSCZPQ8ia7lQy/lxGhZ6Wu43g/sSltyTMww= -> U/87M1NBA/xG98kQ3Zaik5O2jgH/GY8Ps2doIRzLchA=, again a PREDICTION computed from the sealed zip BEFORE the apply, not a post-hoc read. Package DOWNLOADED FROM THE FUNCTION (get-function Code.Location); sha256 of the downloaded bytes == reported CodeSha256. BUILD_MANIFEST read OUT OF the downloaded zip: source_vintage.commit == 73c2dea263aa31a5b8906e2685902061d1a34d78. PER-MODULE: denominator 22, IDENTICAL 22, DRIFTED 0, ABSENT 0, each module re-hashed from the SHIPPED bytes against sha256 of git show pin path. NEGATIVE CONTROL: one appended byte on a probe module changes the hash. SCOPE (CVO 15384): a change-detector over the PACKAGE list, not a completeness bound; completeness is enforce_import_closure at build, which passed (18 packaged .py). | CLOSED 20260829T024847Z |

## Log

- 20260829T024612Z OPENED by 0.7.0_AE_CloudOps with 3 leg(s)
- 20260829T024715Z LEG L1 closed: VersionId Mpv.veBsx7I42MEiMhWUkttFFfvBaqL1, 834732 bytes. DOWNLOADED BACK and re-hashed: sha256=53ff3b33534103fc46f7c910
- 20260829T024847Z LEG L2 closed: safe-apply rc=0 (HALT_ACK=1; the gate surfaced the SAME two 7d-old withdrawals as rebuild #2, re-read fresh rather than 
- 20260829T024847Z LEG L3 closed: CodeSha256 zmVOh+naGSCZPQ8ia7lQy/lxGhZ6Wu43g/sSltyTMww= -> U/87M1NBA/xG98kQ3Zaik5O2jgH/GY8Ps2doIRzLchA=, again a PREDICT
- 20260829T024847Z CLOSED -- all 3 legs proven
