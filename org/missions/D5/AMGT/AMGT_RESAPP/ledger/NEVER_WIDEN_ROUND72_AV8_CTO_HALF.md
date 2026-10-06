# AMGT_RESAPP round 72 -- `AMGT-av-8` never-widen pair, CTO half (grant + code + narrow drafting splice on `opal-amgt-scoped-api`)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-05 ~23:1xZ. **COO half:** `deliverables/2.0.0_SA_COO~Z/round72/NEVER_WIDEN_HALF_COO_AV8.md`
@30b3ff704d (77 lines, read in full; msg 29811). **Executor:** `0.7.0_AE_CloudOps~A`.

## Read live at signing

- **Function:** CodeSha256 `wbIT0PHvxKIgJvgVy+u0XhLuSXFK5dUE/wypJPDcf8o=`, MemorySize 1769, LastModified 2026-10-05T19:14:52Z. This
  equals the COO half's base.
- **Build commit:** `7889ef1ae4` is on CLOUD.
- **The grants policy source:** `infra/aws/terraform/harvest/scoped-amgt-api.tf`.
  - `filings/v1/` is absent. The rk-91 removal note (`:123`) says it left because no reader remained.
  - etf-classifications is granted GetItem only (`:343-356`). The note there says "NOT BatchGetItem" because the code then made one
    `get_item` call.
- **Each new grant has a reader at the build commit:**
  - `filings/v1/` is read by `read_segment_breakdown` (`lib/research/api/scoped_amgt.py:3627`, prefix `:3569`).
  - **BatchGetItem** is called on `CLASSIFICATIONS_TABLE` at `scoped_amgt.py:734`, through `_batch_get`. That is the round-72 cold-read
    cut.
  - The earlier "GetItem is the whole grant" note was true of the old code, and the new code is what changes it.
- **The simulate, run by me** with `round72/checks/r72_grant_av8.sh`: 3 controls allowed. C1 (filings GetObject), C2 (filings
  ListBucket) and C3 (BatchGetItem) each read `implicitDeny`, so `R72 AV8 GRANT: NO`. This equals the COO half's base.
- **Drafting keys** in `opal-data-harvest`: `drafting/v1/BA_US_Equity.json` is VersionId `.zSrn_broPgdErEesbpfY8lJH5RMBCSb`
  (105,318 B), and `drafting/v1/ASML_NA_Equity.json` is VersionId `kQZePsmgbJlF1Tnvf3t2ljwqNnW9wrYX` (13,039 B). Both equal the base.
- **Open entries:** no NEVER-2 entry for this function in the shared tree. 40 worktrees are live, and the executor reads every one
  (condition 6).

## Conditions

1. **The grant lands BEFORE the code, and the code leg does not start until `r72_grant_av8.sh` reads `R72 AV8 GRANT: YES`.** The new
   code batch-reads etf-classifications (`:734`). Landed without the grant, every cold read would lose its classifications. **The
   order is load-bearing.**
2. **The grant plan is exactly ONE in-place update of `aws_iam_role_policy.scoped_amgt_api_grants`.** Any other diff is a STOP. Update
   the comment at `:343-349` to name the batch reader, so the next reader of the file does not trust the stale "NOT BatchGetItem".
3. **The code leg is code-only.**
   - The content diff is exactly CHANGED 3 and ADDED 1. Any other file is a STOP.
   - Read back the new CodeSha256, with MemorySize 1769.
   - Then run the r72 checks and the r70/r71 regression checks named in the COO half.
4. **The splice touches exactly the two keys,** and its diff is exactly `.evidence_records` and `.denominators.evidence_records`.
   - Save the pre-act bytes first.
   - Read back a new VersionId per key, with every other top-level field byte-equal to the pre-act object.
   - **No `drafting_build --rebuild-pool`** (AMENDMENT 2). It would add BA sentence fields and delete ASML's
     `thesis_driver_provenance`.
5. **Not in this act:** a pool universe write (AMENDMENT 1, row Z-W243-S1), SEC egress, or any key outside the two named.
6. **One NEVER-2 entry,** in the DEPLOY genre, opened at start and closed with every leg's readback. Read every live worktree's
   `.open_deploys/` first, and print the per-tree denominator.
7. **Rollback per key** as in the COO half's table. A code rollback leaves the grant, which is inert without its reader. The splice
   restores re-put the pre-act bytes.

**CTO HALF: SIGNED** for `AMGT-av-8` under conditions 1-7.
