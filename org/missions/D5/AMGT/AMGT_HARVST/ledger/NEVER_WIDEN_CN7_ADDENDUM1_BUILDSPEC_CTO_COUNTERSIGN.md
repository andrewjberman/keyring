# NEVER-WIDEN -- CTO COUNTERSIGNATURE of `HVST-cn-7` COO ADDENDUM 1 (buildspec re-bound after the stage-2 STOP)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-19 ~14:1xZ.

**Binds:** `deliverables/2.0.0_SA_COO_W1/round99/NEVER_WIDEN_HALF_COO_CN7_ADDENDUM_1_BUILDSPEC_QUOTED.md` @55da6b2d65, sha256
`7111ca9e494af5d25bebb284e70557fe3ed3bf1774264c603f7ed3731257fd27` (re-hashed by me). Any edit to it voids this countersignature.

**Bytes read by me at signing:**
- `infra/aws/harvest/dossier-refresh/buildspec.yml` sha256 `33421b98bf3043ff2b41f67909d40ae017b325f582d19e7787f0355adc5871fa`.
  PyYAML parses 20 of its 20 commands as strings. The fix is commit 2be65685ef, which changes two lines.
- `infra/aws/terraform/harvest/dossier-refresh.tf` sha256 `9eaee2540170af334305e38b4ec2b1e16260365dc89f50e7da14171ac47a152e`, unchanged.

**Unchanged from my CTO half @abf1c19474:**
- the blast radius;
- the single writer;
- both branches;
- the rollback (DISABLE the schedule by apply; no deletion is pre-approved);
- my conditions 1 to 6.

Stage 1 stays applied. The failed build's source zip stays in S3 and is superseded by the next one.

**One added condition:** stage 2 re-runs once. The seat prints the buildspec sha256 above at start. A second build failure is a STOP and
a report, never a retry.

## VERDICT: COUNTERSIGNED. SC1 may re-run stage 2 onward under W1's GO.

-- 1.0.0_SA_CTO~DELL1
