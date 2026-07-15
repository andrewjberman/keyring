# DEPLOY-COMPLETION LEDGER: etfs-netassets-daily producer swap -> v1.3.0 (V2-1 + msn strike)

**Opened:** 2026-07-15T23:49Z by 0.5.0_AE_OpalETL
**Status:** CLOSED 2026-07-15T23:55Z -- all legs complete, every gate met on its own instrument.
Legs, as run: (1) pre-gate clean (only a foreign __pycache__ .pyc, non-source, cannot enter the
zip) -> build+upload write-VERIFIED 16,988B, both files zipped; (2) source-map sha committed
pre-apply @ a8dfef12f; (3) plan gate MET EXACTLY (0/1/0; only s3_object_version +
source_code_hash + computed last_modified) -> safe-apply, modifications complete 6s;
(4) 0-diff textual verdict cited ("no differences, so no changes are needed");
(5) THREE-WAY TIE EXACT: built == uploaded == live CodeSha256 = 4/6gMExwwY1w3No9D4AeTARMXZaVjDHf1cBYq7yL5gw=;
(6) record-deploy converged + tag etfs-netassets-v1.3.0 pushed --follow-tags.
AC3 = 2026-07-16 22:00Z scheduled fire: the landing guard's OWN verdict on a fresh partition
(also the cutover's full-letter confirmation -- one fire, two named confirmations).

## Motion
Artifact swap of etfs-netassets-daily carrying BOTH CTO-approved commits, one artifact:
3461d1c4d (V2-1: set-identity landing guard + persisted pull manifest + requests/Retry client;
landing_guard.py added to zip via source map) + e45606d46 (msn tier-3 strike, tombstoned).
Code-only; env/TF config untouched beyond source_code_hash + s3_object_version.

## Authorization
- CTO V2-1 review PASS 231419Z (guard lift md5-tied by his own read) + msn-strike fast-review
  PASS 232938Z; both commits approved for ONE build.
- Sequencing: AFTER the cutover verify fire (CTO 231419Z (c)) -- cutover ledger CLOSED 23:47Z
  (f66d2f5ae), condition met. Tag = v1.3.0 (CTO 233744Z; v1.2.0 consumed by the flip leg).
- PLAN GATE (binding): source_code_hash + s3_object_version ONLY -- ANY other diff line = STOP.
- AC3 rides tomorrow's 22:00Z scheduled fire (the new guard's own verdict, fresh partition).

## Legs
1. [ ] Pre-gate: infra/aws/lambda/ committed-clean; build-and-upload.sh etfs-netassets
       etfs-netassets-daily (deterministic zip: lambda_function.py + landing_guard.py);
       upload + source-map sha update.
2. [ ] Commit source-map sha (pre-apply, per commit-before-apply).
3. [ ] Targeted plan (module.etfs_netassets_daily) -> THE GATE -> safe-apply.
4. [ ] 0-diff re-plan (textual "No changes" cited, never a piped exit code).
5. [ ] THREE-WAY TIE: built sha == uploaded sha == live CodeSha256.
6. [ ] record-deploy + tag etfs-netassets-v1.3.0 + push --follow-tags; ledger CLOSE;
       evidence to CTO/COO.

## Rollback
Re-point the artifact at the prior version (S3 versioning holds the v1.1.x zip; s3_object_version
is the lever) -> targeted apply -> live sha tie back to 40KaO/7j. One-resource, minutes.
Tonight's cutover does NOT depend on this swap (the verify ran on v1.1.x); a STOP here strands
nothing -- close the ledger at the stop point and report.
