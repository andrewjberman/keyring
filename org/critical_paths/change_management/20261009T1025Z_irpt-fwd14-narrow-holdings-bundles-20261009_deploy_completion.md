# Deploy Completion Record
**Date opened:** 2026-10-09T10:25:13.432884+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-pr-404: IB-pr-402 FWD-14 three NARROW per-firm holdings bundles. PIN STATED (ccbe8b8be1): pin 6f7ca4840e, packet blob 4f134ade55, base commit 9efbec3c2f, narrow member sha256 dfa017b824c1aba5c1107e53ef4811edaba93b2b7903c140208e41ab8866262a. THE THREE KEYS: s3://opal-data-49financial/irpt/49financial/code/gold/investor-reporting-holdings.tar.gz; s3://opal-data-inflection/irpt/inflection/code/gold/investor-reporting-holdings.tar.gz; s3://opal-data-cottonwood/irpt/cottonwood/code/gold/investor-reporting-holdings.tar.gz. THE THREE BUILT SHA256: 49financial 3f2e738f83aa415a2b56cf506d54368f9d2f86f7ded8f19202fc373ef6a28901 (md5 01387cef54b9e15e10023f05029e357d, 468666 B); inflection 7036a650703a04b18bcf251717c1310fc5553c817eb9d7ce34ec34ed678c9718 (md5 5daec38f0fbd604c65a770ce08029c67, 468435 B); cottonwood 3f2e738f83aa415a2b56cf506d54368f9d2f86f7ded8f19202fc373ef6a28901 (md5 01387cef54b9e15e10023f05029e357d, 468666 B). THE PULLING FAMILY: irpt-holdings-refresh-lambda, 3 firms, one SSM command each; the producer fired by irpt-holdings-snapshot, cron(15 10 ? * MON-FRI *) America/New_York = 14:15Z today. ROLLBACK VERSIONS (Branch B, copy-object): 49financial 3Q_W49U7kMa_xO30Q6LQE7QLsFu7ARur; inflection SuRm8tIYq9AKTbRD91SxTJp2Fh80CqCo; cottonwood NZIQjid2En9Wbe8kM8ibfsIjxjDWKEoT. The ordered key investor-reporting.tar.gz is NOT touched. COO half @a9d5043ef9, CTO half @c4df78131d conditions 1-7; AMENDMENT 1 runs this ahead of IB-pr-397.
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | precheck and the digest gate, before the ledger opened and before any upload | per firm VersionId equals the rollback version and ETag the live ETag; the narrow member reads sha256 dfa017b8 LF-only from the commit that added it; the packer CONTROL reproduces each firm live bytes exactly; and each out.tar.gz sha256, md5 and bytes equal the packet table |  | OPEN |
| L2 | s3-prefix | opal-data-49financial irpt/49financial/code/gold/investor-reporting-holdings.tar.gz | head-object ETag equals the built md5, both metadata values echoed, and get-object of the new version hashes to the built sha256; new version id recorded |  | OPEN |
| L3 | s3-prefix | opal-data-inflection irpt/inflection/code/gold/investor-reporting-holdings.tar.gz | head-object ETag equals the built md5, both metadata values echoed, and get-object of the new version hashes to the built sha256; new version id recorded |  | OPEN |
| L4 | s3-prefix | opal-data-cottonwood irpt/cottonwood/code/gold/investor-reporting-holdings.tar.gz | head-object ETag equals the built md5, both metadata values echoed, and get-object of the new version hashes to the built sha256; new version id recorded |  | OPEN |
| L5 | verify | the replay re-run on the UPLOADED bytes, before the 14:15Z fire | every real_<firm>_live_vs_built arm identical, the worse arm REFUSES with the index unmoved, and the restored arm PUBLISHES; a miss is a STOP and Branch B |  | OPEN |
| L6 | verify | the first scheduled fire after landing, and the criteria | per firm the output line and refusal record read from the producer output and never from the SSM status; IB105-1-AC1, AC2 and AC3 PASS |  | OPEN |

## Log

- 20261009T102513Z OPENED by 0.7.0_AE_CloudOps~IB2 with 6 leg(s)
