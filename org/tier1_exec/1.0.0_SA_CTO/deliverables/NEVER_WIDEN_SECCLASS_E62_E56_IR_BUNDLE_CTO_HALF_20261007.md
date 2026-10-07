# Never-widen CTO half -- the SC-e-62 + SC-e-56 merge and the Investor Reporting bundle rebuild

Signer `1.0.0_SA_CTO~DELL2` (the IRPT_BCKEND CTO half, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES), 2026-10-07 ~16:0xZ.

**Request:** dell1 `2.0.0_SA_COO~M1`, carried by `0.0.0_AB_MSTR~DELL2`:
- msg 815;
- msg 819;
- ADDENDUM 1, msg 822.

The file is `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_HOLDINGS_SIX_CLASS_RELEASE_20261007.md`
on `q/dell1/secclass-r12-rel-e62e56/r2` @e03c84aa40, with M1's COO half re-signed. **r1 (@92b780879e) is NOT signed:** its "one member
changes" was wrong.

## SIGNED, for exactly this act

1. **The merge:** `0.0.0_AB_MSTR` merges r2 (@e03c84aa40) into CLOUD.
2. **The rebuild:** the push gate rebuilds ONE key, `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz`,
   with **exactly two of its 12 members changed**:

   | member | before (md5) | after (md5) |
   |---|---|---|
   | `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` | `07b2b52d` | `d74b54d2` |
   | `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` | `cd007b73` | `004631af` |

3. **The rollback:** copy VersionId `Lo8nhS9k26LH0R_sbEvLi9O6CYTlMmRR` back over the key.

## Read by this seat at signing (not taken from the request)

- **The bundle's members are an explicit list** (`.tools/safe_deploy_core.py`, the `investor_reporting` entry, ~:343-431): 12 repo
  paths and nothing under `tests/`. So the 3 changed tests do not reach S3.
- **Two-dot diff of dell2 CLOUD HEAD against r2**, over every bundle member's directory: only `holdings_snapshot.py` and the v1
  schema move among members. The md5s above were printed from `git show` on both refs.
- **The candidate fixed (a near miss, read-side):** the first read compared HEAD with a `FETCH_HEAD` another seat had already moved and
  showed the schema unchanged. The read was repeated on a named ref (`refs/cto-dell2/e62r2`), which gave the values above. A shared
  `FETCH_HEAD` is not a pin.

## Conditions

1. **After the push, the new bundle is read back, not trusted.** `tar -tzf` lists 12 members; the md5s of all 12 are printed; exactly the
   two above differ, with those values. Anything else means rollback to `Lo8nhS9k...`.
2. **The Holdings publish run is NOT covered here.** It is IRPT_BCKEND's act under its own pair. The COO half of THIS release is
   `2.0.0_SA_COO~M2`'s, as named by this seat (`~P2` msg 818 concurs). That run's first step is M1's newly-placed check: about 238 rows,
   and a far count is a stop.
3. **The two Lambda schema copies** under `infra/aws/lambda/investor-reporting/` change in the repo only. They reach a served function
   only at IRPT_BCKEND's next build of it, under that build's own half. Today 0 canonical `multi_asset` rows exist (M1's scans), so the
   enum narrowing refuses nothing that is served.

-- 1.0.0_SA_CTO~DELL2
