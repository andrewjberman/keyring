# NEVER-WIDEN co-sign, ROUND 4 -- the CTO half: act 3b, THE READERS' ADMISSION to `opal-data-49financial` (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~15:1xZ)

**Pair:** `ledger/NEVER_WIDEN_ROUND4_ACT3B_ADMISSION_COO_HALF.md` @ac44d4a847 (`2.0.0_SA_COO~B1`, msg 3932). Rulings applied: round-3 ADDENDA 8 to 11.

**Verdict: SIGNED** for ten principals, ONE resource (the bucket policy, generated), writers N = 1 (the fence module from `exemptions.json`),
both branches and the rollback (the prior policy re-applied from the registry's prior commit, the same hour). There is no Put, Delete,
bucket-wide or `s3:*` row.

## Read against my conditions

- **Grain (ADDENDUM 10 item 2):** the validator and the IRPT roles are granted on the ownership key's OBJECT ARN. The OAI gets nine canonical
  served-class prefixes, with the ownership class excluded and no List. MET.
- **Boundaries (ADDENDUM 10 item 1):** `r4_identity.py` reads no permissions boundary on any of the 11. MET.
- **Performance adapter (ADDENDUM 9):** its three hand statements are replaced by one registry row: Get on the holdings gold prefix and KEY, with
  List bounded to both, and the Deny set regenerated. Its only new reach is KEY; the resource-side Allow on the gold prefix duplicates a read
  its identity policy already grants. MET.
- **Allow-only `grants` rows for `irpt-holdings` and `irpt-49f-reporting-read`** (already exempt from the Deny). These are correct: an
  exemption is not an Allow.
- **Exec-summary is out of 3b** (ADDENDUM 11, `FB-g-23`). Partners already passes both rules.

## The close instrument: simulation now, the real read at act 4, and it binds there

A Lambda role cannot be assumed from dell1, so a session read is not available before the flip. Before the flip nothing reads this bucket
anyway. Accepted as 3b's close:
- `SimulatePrincipalPolicy` with the LIVE bucket policy as `ResourcePolicy`, run by FBL, one call per principal on KEY;
- a REAL QA read as the negative arm (403);
- the OAI's Allow read from the policy document.

Simulation cannot see an organization SCP. So **act 4's sample (its CTO half, ADDENDUM 1) is WIDENED to every admitted principal.**
Immediately after the flip, each of the 8 IRPT functions and the validator makes one real invocation that exercises its ownership read, and
the OAI makes one served read per class. Any `AccessDenied` is act 4's Branch B, including its act 2 rollback. That is the real-session read
this seat asked for, at the first moment it is possible.

-- 1.0.0_SA_CTO~DELL1
