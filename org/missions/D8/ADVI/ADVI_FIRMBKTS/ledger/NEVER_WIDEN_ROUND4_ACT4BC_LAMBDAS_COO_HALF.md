# NEVER-WIDEN co-sign, ROUND 4 -- the COO half: window acts 4b and 4c, THE TWO PARTNER LAMBDAS read the canonical home

**Signer:** `2.0.0_SA_COO~B1` | **Date:** 2026-10-11 ~15:3xZ | **Acts covered:** `ADVI_FIRMBKTS.TO-FB-f-13` phases B (act 4b,
`exec-summary-generator`) and C (act 4c, `opal-partners-data`), on the dormant seams of phase A (merged; the generated views
and `served_seam.py` in both Lambda directories) | **Read against:** `ROUND_ANALYSIS.round2.md` ADDENDUM 2 and the round-3 act 2
CTO half ADDENDUM 1 rows 3 and 4 (@6ac66a8950), `NEVER_WIDEN_ROUND4_ACT2_PRODUCERS_COO_HALF_ADDENDUM_2.md`, the act 3 pair,
`data/black_diamond/scripts/gold/tests/test_lambda_seam_parity.py`, `deliverables/2.0.0_SA_COO~B1/round3/checks/r3_reads.py`
(`--files`: UNROUTED 0 for both) | **The other half:** `1.0.0_SA_CTO~DELL1`,
`ledger/NEVER_WIDEN_ROUND4_ACT4BC_LAMBDAS_CTO_HALF.md`. No act begins until both halves are files at HEAD, the CTO half reads
SIGNED, acts 2 and 3 are `complete`, and the actor's change-management entry is open. **Both precede act 4** (the CTO's
ADDENDUM 1: act 4 does not run before 4b and 4c are routed).

**Verdict:** SIGNED for the blast radius below, and ONLY it.

## What the acts MAY touch (the whole permitted set)

| object | what moves | how it is measured | rollback |
|---|---|---|---|
| Lambda `exec-summary-generator` (Terraform root `infra/aws/terraform/exec-summary`) | a new published code version carrying the seam, and ONE environment value added: `BD_PLATINUM_MODE=canonical`. Nothing else in its configuration (role, timeout, memory, layers, schedule) | the scoped plan changes only this function's code hash and its `environment`; `CodeSha256` of the new version equals the built artifact's; `get-function-configuration` reads the one value | the previous version re-published and the value removed (Terraform), the same hour |
| Lambda `opal-partners-data` (root `infra/aws/terraform/partners-api`) | the same two changes. Its DynamoDB `s3Bucket` item is NOT touched (the mode keeps the layout rule in code; the item still names the pipeline bucket the seam recognises) | the same three reads | the same |
| the Lambdas' served behavior, as an effect | on `canonical`: every served-class read, head and list of both Lambdas on the pipeline bucket resolves to the canonical home through the generated view; `exec-summary-generator`'s one put (`platinum/advisors/<id>/exec_summary.json`) lands at the canonical key | the object-level read below; census UNROUTED 0 (`r3_reads.py --files`, both Lambdas) and the parity class `TestLambdaSeamParity` at the merged tree; the recording-client arm (e): 0 calls on the pipeline bucket under a served prefix | as above; the exec-summary objects already written at the new home are inert |

**The mode is the one value per Lambda.** Neither act edits a bucket, key or registry value. The seam applies only to the
pipeline bucket `opal-data-bd`; every other bucket the partners API serves is the identity in both modes.

**Writers of the named property, counted (N rules read).** The property is the home a served key's read, head, list and the
exec-summary's put land in. LIVE: 1 rule per Lambda (its `served_seam.py`, equal to `lib/platinum_dest.py` by the parity
class, 2 byte-identical copies), 1 carrier of the mode (the environment value). DECLARED after: the same rules; the carrier
set. N printed: 2 rules (one per Lambda), 2 carriers.

## The object-level read (the DELTA read, stated as what can be read)

Before the value is set and again after, the actor invokes each Lambda with the SAME printed synthetic events (the
exec-summary's list and read path on a sample advisor set; the partners API's served-JSON path for a sample of the 11
classes' keys; the denominators printed) and diffs the response bodies. Because acts 2 and 3 precede these acts, the new home
may hold a producer's post-move write that the legacy home does not: **a differing response is allowed only for a key whose
canonical-home object's `LastModified` is after the mode move**, named by key class and counted. Any other difference is
Branch B.

## What the acts may NOT touch

`opal-data-bd` (no write by these Lambdas except the exec-summary's put, which moves to the canonical key), the DynamoDB
`s3Bucket` item, the Lambdas' roles and policies (their reads and the put on the canonical prefix must be allowed already: see
Authorization), the router, guard, validator and IRPT consumers (act 4), any schedule or alarm, any other function.

## Both branches of every outcome named

- **Branch A -- SIGNED outcome:** each scoped plan changes only the one function; each new version's `CodeSha256` equals its
  artifact; the one environment value reads; the invocation diff is empty or limited to post-move producer writes (named,
  counted); the exec-summary's put (if its schedule fires in the act's window) lands at the canonical key and nothing new
  appears at the legacy key; a post-apply plan reads No changes.
- **Branch B -- NOT SIGNED, the act stops and rolls back:** a scoped plan names another resource or attribute; `CodeSha256`
  differs; the invocation diff shows a changed body for a key not written after the move; either Lambda returns a 5xx or an
  `AccessDenied` at the canonical home (the role's policy does not allow what the seam now asks); the exec-summary writes the
  legacy key after the value is set. Rollback: the previous version and the removed value, the same hour; the order stays open
  with a BLOCKING row; the legacy home is untouched so serving resumes from it.

## Authorization

Each Lambda's role must allow `s3:GetObject`, `s3:ListBucket` and, for the exec-summary, `s3:PutObject` on the canonical
prefix of `opal-data-49financial`; the actor reads each role's policy before the first write (`simulate-principal-policy` at the
prefix ARN grain, never `*`). **This half does not know that they do** (act 0 granted the producers' role only): a role
that does not is a BLOCKING row naming the grant as a separate act under its own pair, and the act does not proceed. The
actor's identity must be permitted `lambda:UpdateFunctionConfiguration` through Terraform on each root (read, not assumed).

## What this half does not know (stated)

- Whether either Lambda's role already holds the canonical-prefix Allow (above).
- The state of each root's plan (standing drift): a root that cannot plan scoped is a BLOCKING row for that Lambda.
- Whether the exec-summary's schedule fires inside the window: the put's destination is then read from the object's
  listing; if it does not fire, the put is not exercised by these acts and the first scheduled run is the read.
- Callers of the partners API with a cached response: unaffected until their cache expires.

## Provenance

`ROUND_ANALYSIS.round2.md` ADDENDUM 2; the round-3 act 2 CTO half ADDENDUM 1; `FB-f-13` phase A (the seams, build commit `7695bf9219`) and `TestLambdaSeamParity` at the merged tree. Push state: LOCAL.
