# NEVER-WIDEN SIGN-OFF PACKET -- export deploy (B): the Performance adapter's render ports + the S143 Orion fix, then `export_render=on`

**For:** `1.0.0_SA_CTO` (CTO 101098: every served move needs the CTO's never-widen half). **Prepared by:**
`2.0.0_SA_COO~P`, 2026-09-26 ~13:4xZ. **Nothing is applied by this packet. STOP until the CTO half is at HEAD naming this
file's blob.**

**What is served today (read 13:4xZ):**

| function | CodeSha256 | IRPT_EXPORT_RENDER | IRPT_EVIDENCE_BUCKET |
|---|---|---|---|
| `irpt-performance-adapter` | `jbojclF39H..` | n/a | unset (every render read refuses) |
| `irpt-export-render` | `ryEMGlRu..` | `off` | set, the export bucket |

Export today: submit freezes, persists and grants, answers QUEUED, and dispatches NOTHING. So no user has ever
received a rendered PDF, and nothing that works today is at risk.

## THE THREE KEYS

### D1 -- irpt-performance-adapter code

- **Source:** the publish branch `55c42208a9` row: the whole row at backend `b905df2c60`, plus `grant.py`, plus the
  three Orion modules at `a7e9f51c77`.
- **What moves** vs the live `jbojcl..` build (row `4872b28043` census: 7 of 68 members; S143: 3 more):
  - `served` / `enforce` / `entry`: render ports, installed only when `IRPT_EVIDENCE_BUCKET` is set; the render
    principal answers only for the subject a grant names;
  - `runtime` + `routetable`: the census path fix;
  - `errors`: the sink;
  - `maintained_sources`: the seam;
  - `orion_selected` / `orion_account_mapping` / `orion_live`: the household scope. An account sharing its household
    is refused OBJECT_NOT_COVERED, and a failed call names its HTTP status.
- **Proof so far:**
  - performance 189, _authz 160, reports 87 pass;
  - `flat_import_check --map-root`: ok and guarded;
  - the S143 body proven live 05:07Z (ledger `irpt-orion-household-scope-proof-20260926`).
- **Rollback:** re-point the function to S3 object version of `jbojcl..` by a TF apply of the previous version, the
  pattern of every prior adapter deploy.

### D2 -- performance root: `render_grant.tf` + env `IRPT_EVIDENCE_BUCKET`

- **Plan rehearsed 00:3xZ:** 1 add (`irpt-performance-render-grant-read-policy`) / 1 change (env +
  `IRPT_EVIDENCE_BUCKET`, the same bucket the export writes grants to; the 8 other env elements unchanged) / 0 destroy.
  The code change adds `source_code_hash` / `s3_object_version` once D1 is uploaded.
- **The grant, nothing else:**
  - GetObject on `firms/*/generations/exr_*/render_grant.json`;
  - ListBucket bounded to that shape;
  - kms:Decrypt via S3 for those objects only.
- **Rollback:** delete the policy and unset the env var. The function then refuses every render read again, which is
  today's behaviour.

### D3 -- export root: `export_render = on`

- **Rule:** CTO ruling (a), msg 101013, already applied as deploy (A), ledger `irpt-export-b2b3-a-20260925`: the IAM,
  the SSM document v5 and the host scripts are LIVE.
- **What turns on:** each submit mints ONE render token, puts it at `/irpt/render-token/<ATT-id>` (SecureString), and
  dispatches the render host with the NAME. The host reads it into memory, renders the print route, and deletes the
  name. B3's finalize-on-read then validates the PDF and writes the receipt.
- **Rollback:** `export_render = off`, one env value, which is the plan's only change in that root.

## BLAST RADIUS, BOTH BRANCHES

- **What newly exists:**
  - one read-only IAM policy on the adapter role (grant objects only);
  - one env value on each of two functions;
  - the adapter code above;
  - per export attempt, one SecureString name for <= 15 min, deleted on every terminal path plus the 15-min sweep.
- **Branch R (renders succeed):**
  - A Performance export produces a PDF of a report its requester already reads.
  - The render token is scoped to exactly the grant's pinned accounts, selection, report and job (C-S219 43/43).
- **Branch F (renders fail):**
  - The export stays NOT_READY, then DEPENDENCY_UNAVAILABLE after 15 min: today's outcome with a named reason.
  - The token name is deleted on the failure path.
  - Nothing is served that was not before.
- **Performance reads for humans are UNCHANGED in both branches.**
  - The render ports answer only a render-delegate principal (`_authz/enforce.py` `_resolve_render_delegate`).
  - A human token takes the same path it takes today (C-S219: "a human token unaffected at V3, full V2 and
    served.Entry").
- **Inflection Performance** changes in both branches: a plan-armed request for an account alone in its Orion
  household now computes. Every other INF account refuses OBJECT_NOT_COVERED, where today every INF account fails
  DEPENDENCY_UNAVAILABLE. No INF plan is armed by this act, so no Orion call can happen until a separate re-arm.

## THE NEGATIVE ARM (the CTO's, carried from 101013)

- Another attempt's token NAME is refused by the host role.
- A read after delete is refused `ParameterNotFound`.
- A human request with no render token to the performance route answers exactly as before, the same arm before and
  after.

## SEQUENCE

1. Open ledger `irpt-export-deploy-b-20260926` and commit its OPEN sentinel.
2. **D1:**
   - `build-and-upload.sh investor-reporting irpt-performance-adapter` from the publish branch.
   - Restore any tracked `performance/*.py` the builder deletes from the publish working tree (the parked builder
     defect).
   - Record the artifact.
3. **D2:** plan the performance root, which must be exactly 1 add / 1 change / 0 destroy: code + env + policy. Then
   safe-apply, read back `CodeSha256 == artifact` and the env, and replan to No changes.
4. **Before-arm check:**
   - a human performance request for a 49F single account answers as before (200 PARTIAL);
   - `flat_import_check` passes on the served zip.
5. **D3:** plan the export root, which must be exactly 0 / 1 / 0 (env `IRPT_EXPORT_RENDER` off -> on). Then
   safe-apply, read back, and replan to No changes.
6. **The negative arm** as above. Then the first real render is the next user export: one of the two retained 49F
   reports (`REPORT#RPT-0bafbc77..` / `RPT-ef0b7c27..`), submitted by an Opal login in the next principal window.
7. Close and commit the ledger.

## WHAT THIS PACKET DOES NOT COVER

- Any INF re-arm.
- Any principal.
- Any change to the auth plane, the edge, or the render keys.
- The status and narrative functions' render ports: they are not needed for a Performance export, since the print query
  leaves the narrative off.

## WHAT THE HALF SIGNS AGAINST

This file's committed blob, D1-D3 as named, and each key's rollback.
