# The pre-343 receipt reads again within scope -- 0.7.0_AE_CloudOps~I

**archetype:** DEPLOY

**Date:** 2026-10-07
**Task Order:** IRPT_BCKEND.TO-IB-pr-350 @3e85fbf2b0 (risk WORLD, issuer `2.0.0_SA_COO~P2` on dell2)
**Status:** COMPLETE -- both passes

---

## Objective

Pay off the availability cost IB-pr-349 deliberately imposed. After that release a receipt naming no
account is refused on read, so every export frozen before IB-pr-343 was unreadable. Back-fill
`facts.covered_account_ids` into those receipts (PRD v0.30 item 35) so they read again for a principal
whose scope covers them -- and for no one else.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open` / `close-leg` x3 / `close` | PASS | NEVER-2 entry opened before the write, closed on measured proof, sentinel removed |
| p69_cells.py (issuer check) | `python .../checks/r69/p69_cells.py . IB69-1-AC1` | PASS | Clean unmodified PASS -- this check reads one file and makes no AWS call, so it does NOT hit the bare-`bash` trap that row S384 filed against the r68 check |
| backfill_covered_account_ids.py | `--dry-run` x2, then `--apply` | PASS | The tool is the deliverable of a sibling cell (IB-pr-344); it behaved exactly as its docstring promises, including preserving object metadata |
| bundle.py `covered_account_ids_of` | imported from the checkout, never copied | PASS | The freeze's own derivation function. Importing it is what makes the added-condition check meaningful rather than a re-implementation |
| aws s3api (head/get/list-objects-v2) | object versions, encryption, prefix listing | PASS | `s3api` rather than `s3 ls` deliberately: `s3 ls` renders LOCAL time and this record needed UTC |
| .tools/jq.exe | census and receipt field reads | PASS | Resolved by explicit path, fail-closed loud, per Rule 16 |

**What worked:** importing the freeze's own `covered_account_ids_of` instead of re-deriving the account
set. The CTO's added condition is only a real control if both sides are computed the way production
computes them; a hand-rolled extraction would have tested my parser, not the system.

**What failed:** nothing this session.

**Gap found:** none new. The one tool gap this seat filed today (no comp-tool has an IAM GROUP mode)
is in the IB-pr-349 log and row S383; it did not bear on this order.

---

## Deployment Sequence

### Pass 1 (read-only)

| Step | Action | Result |
|------|--------|--------|
| 1 | Check IB-pr-349 closed and not rolled back | `CLOSED -- nothing stranded -- closed 20261007T150015Z`, 4 legs proven, sentinel absent, `rolled_back` false |
| 2a | Read `IRPT_EVIDENCE_BUCKET` from the LIVE function config | `opal-data-ycharts` (read, not typed) |
| 2b | Identity | `arn:aws:iam::313476888478:user/Andrew_Berman` |
| 2c | `--dry-run --census-out ...` | `listed 1; read 1 = filled 1 + unfillable 0; would_write 1; wrote 0; denied 0` |
| 3 | Write the sign-off packet | `NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-350.md` |
| 4 | Commit and STOP | @`761268b116`; packet blob `2e073c2d3e16246136183efb30a3c62e3152b5b2` |

### Pass 2 (the write), on the issuer's GO

| Step | Action | Result |
|------|--------|--------|
| 0 | Read BOTH halves at the published HEAD | COO @`295835f61f`, CTO @`c48b2d2442`, ref `84bc3c379c`; both cite the packet blob, both bind ONE key |
| 0b | CTO half's ADDED CONDITION | bundle set == pending set: both 1, 0 only-in-bundle, 0 only-in-pending -- MET |
| 1 | Open ledger, commit sentinel | @`7fd6e84075`, rollback source named |
| 2 | Apply-time dry-run re-check | signed tuple `1/1/1/0/0/1/0`, denied 0 -- identical to the packet |
| 3 | `--apply` on the one signed key | `wrote 1; denied buckets 0, objects 0` |
| 4 | Re-read the written receipt fresh from S3 | `facts.covered_account_ids` an array of 1; all other fields byte-identical |
| 5 | Read through the DEPLOYED bytes, no token minted | in-scope ADMITTED; out-of-scope and empty-scope REFUSED on the COUNTS branch; 1 admitted-read line |
| 6 | Close the ledger | 3 legs proven, sentinel removed |
| 7 | Write the after-reads file | `IB69-1_backfill_after_reads.json` |
| 8 | `IB69-1-AC1` | **PASS** -- `OK: 1 listed, 1 written and re-read, 0 unfillable, 0 denied`; two planted mutants fired |

### The object, before and after

| read | value |
|---|---|
| key | `opal-data-ycharts` `firms/49financial/generations/EXP-e29b5415a06f90f943481c41a1a4821b/receipt.json` |
| pre-write version (ROLLBACK SOURCE) | `3BN57Lb6hJ7._Nn0hGZ4Yj7NEFYOV_Qa`, 870 B |
| post-write version | `Jg0xDC0pFmB8UBfEv0sl1eOQ_OrcSAqs`, 925 B |
| encryption | `aws:kms` before and after -- metadata preserved |
| unchanged fields | `export_ref.bundle_sha256`, `artifact.sha256`, `page_count` 11, `validation_status` PASSED, `job_state` READY |
| rollback liveness | the pre-write version was re-read AFTER the act and is still retrievable |

---

## Work Completed

### 1. Why dell2 could not do this, measured rather than inherited
IB-pr-344's dry run on dell2 listed this same single receipt and could not read it -- row `W145-S5`,
`kms:Decrypt` denied. The object is SSE-KMS under key `7f4d3042-10d8-49a7-b55e-3c963cea8111`. This
identity decrypted it and the census reads `denied 0`. That is the entire reason the order routes to a
laptop applier, and it is now a measurement rather than a premise I accepted.

### 2. The added condition, and the thing that would have broken it
The CTO half added: at apply, the bundle and `pending.json` must name the same account set, or write
nothing -- "a back-fill must never name an account the export did not hold, because that would widen
exactly the read the fix closed." I evaluated it BEFORE opening the ledger, because a failure means no
act at all and therefore no entry to open.

The prefix listing was the useful surprise. Under
`firms/49financial/generations/EXP-e29b5415.../` there are exactly TWO objects, `pending.json` and
`receipt.json` -- **no `bundle.json` and no `report.pdf`**. The tool's rule is "the bundle sits beside
the artifact (`artifact.storage_key`, `report.pdf` -> `bundle.json`)", and that artifact lives under a
different prefix entirely:
`firms/49financial/generations/exr_5f3c0b757a054bffbe31b431/attempts/1/exports/.../report.pdf`.
`pending.json` names the bundle outright in `bundle_key`. Had I assumed "beside the receipt" I would
have read a missing object and concluded the condition could not be satisfied -- a false STOP on a
WORLD-risk order.

With the bundle located: set equality holds, both size 1, derived with the freeze's own
`covered_account_ids_of` from `bundle.py` sha256 `09ff638dc839` -- exactly the `bundle.py` member
IB-pr-349 released, so the derivation function and the deployed consumer are the same vintage.
`report_kind` is `performance`, not retained, so the exemption that lets a retained bundle's rows name
no account does not apply here. Bundle integrity agrees three ways: the file's own sha256 equals the
receipt's `export_ref.bundle_sha256` and `pending.json`'s `bundle_sha256`.

### 3. The after-read that actually discriminates
A back-filled receipt being admitted proves little on its own -- an always-admit bug would also pass.
What matters is WHICH refusal the out-of-scope arm gets. Through the deployed bytes:

| arm | result |
|---|---|
| in-scope Opal principal | ADMITTED, `ok=True named=1 outside=0` |
| out-of-scope principal | REFUSED, `1 of 1 account(s) outside the viewer's current scope` |
| empty-scope principal | REFUSED, same counts branch |

The out-of-scope refusals land on the COUNTS branch and NOT the names-no-account branch. That is the
positive proof the fill took: before the write, every refusal came from the no-account branch. One
`irpt_export_read_admitted` line was emitted, carrying `principal_id`, the opaque `export_id` and
`covered_account_ids_count` 1.

### 4. Certifying the check before quoting it
`IB69-1-AC1` PASS means nothing unless the check can fail. Two planted mutants, each on its own field:
`denied=1` -> `FAIL: denied 1: the applier identity could not read every receipt`; and
`rewritten_reread_ok=0` -> `FAIL: would_write 1, wrote 1, re-read ok 0 differ`. The true article passes.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Evaluated the added condition BEFORE opening the ledger | It is read-only, and failing it means writing nothing -- so opening an entry first would have created a NEVER-2 record I would immediately have to close with no act in it |
| Located the bundle from `pending.bundle_key` rather than assuming it sits beside the receipt | The generation prefix holds only two objects; the artifact and bundle live under a separate `exr_...` attempt path. Assuming would have produced a false STOP |
| Imported `covered_account_ids_of` instead of extracting account ids myself | The condition is only a control if both sides are computed the way production computes them. A hand-rolled extraction tests my parser, not the system |
| Treated the COUNTS-branch refusal as the real evidence | An admit alone is consistent with an always-admit defect; the branch the refusal lands on is what distinguishes "filled" from "changed" |
| Started pass 1 without a GO message, on measured grounds | No dispatch ever reached this inbox. But `<status>` read `pending`, not `staged`, the `depends_on` was satisfied by my own closed ledger, and pass 1 is read-only. Reported the absence plainly rather than treating it as licence or as a reason to idle |
| Cleaned two duplicate files from the worktree | Both were byte-identical to the CLOUD-committed versions (`git hash-object` vs `git rev-parse`), so nothing was lost; leaving uncommitted strays risks a later drain picking them up |
| Did not flip `<status>`; did not push | The flip is the issuer's. LD-0367/0368 puts the push with the integrator; push state is reported LOCAL and measured by `ls-remote` |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `s3://opal-data-ycharts/firms/49financial/generations/EXP-e29b5415.../receipt.json` | `facts.covered_account_ids` filled (1 account) | Yes -- version `Jg0xDC0pFmB8UBfEv0sl1eOQ_OrcSAqs` |
| `.../deliverables/0.7.0_AE_CloudOps~I/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-350.md` | pass-1 packet, blob `2e073c2d3e...` | Yes -- `761268b116` |
| `.../deliverables/0.7.0_AE_CloudOps~I/IB69-1_backfill_dry_run.json` | pass-1 census | Yes -- `761268b116` |
| `.../deliverables/0.7.0_AE_CloudOps~I/IB69-1_backfill_apply.json` | apply census | Yes -- `8eaf445c12` |
| `.../deliverables/0.7.0_AE_CloudOps~I/IB69-1_backfill_after_reads.json` | the graded after-reads | Yes -- `8eaf445c12` |
| `org/critical_paths/change_management/20261007T1825Z_irpt-backfill-ib-pr-350-pass2-20261007_...md` | ledger opened then CLOSED | Yes -- `7fd6e84075` then `8eaf445c12` |
| `org/critical_paths/.open_deploys/irpt-backfill-ib-pr-350-pass2-20261007.json` | sentinel committed, removed at close | Yes -- `7fd6e84075` then `8eaf445c12` |

---

## Blockers

**None owed by this seat.** Three commits -- `761268b116`, `7fd6e84075`, `8eaf445c12` -- are LOCAL;
origin/CLOUD read `a30d12d8fd` by `ls-remote` at report time. Landing is the integrator's act under
LD-0367 and was asked of `0.0.0_AB_MSTR` at msg 106518. That is a handoff, not a blocker on the work:
the S3 write is live and verified independently of any git state.

---

## Current State

The one export receipt written before IB-pr-343 now carries `facts.covered_account_ids` with its single
account, at version `Jg0xDC0pFmB8UBfEv0sl1eOQ_OrcSAqs` in `opal-data-ycharts`, SSE-KMS preserved and
every other field byte-identical to the pre-write object. Read through the deployed
`irpt-export-render` bytes (`entry.py` sha256 `fc241d806ecc`), it is ADMITTED for a principal whose
scope covers that account and REFUSED on the counts branch for one that does not -- so IB-pr-343's
fail-closed guarantee is intact while the export is readable again by the right reader. The NEVER-2
ledger `20261007T1825Z_irpt-backfill-ib-pr-350-pass2-20261007` is CLOSED with three legs proven and no
sentinel; the pre-write version `3BN57Lb6hJ7._Nn0hGZ4Yj7NEFYOV_Qa` remains retrievable, so rollback is
live and would move toward safety rather than reopening anything. `IB69-1-AC1` reads PASS with two
planted mutants fired. Together with IB-pr-349 this closes the pair: the hole is shut and the
availability cost it imposed is paid off.

---

## Next Steps

1. **[`0.0.0_AB_MSTR`] Land `761268b116`, `7fd6e84075`, `8eaf445c12`** -- the packet, the ledger and the
   graded after-reads. The issuer re-grades from the trunk and cannot see them until they land.
2. **[`2.0.0_SA_COO~P2`] Flip `<status>` on TO-IB-pr-350** and on TO-IB-pr-349. Both are the issuer's.
3. **[`2.0.0_SA_COO~P2`] Fix the r68 check's bash resolution** -- row S384, one line: import
   `.tools/git_bash_resolver` and call `bash_argv(aws, ...)`. The r69 check needs nothing; it makes no
   AWS call.
4. **[`1.0.0_SA_CTO`] Rule on a read-Deny for the 21 unfenced buckets** -- row S383 plus
   `0.7.0_AE_CloudOps~E`'s denominator (24 buckets, 3 fenced) and dell2's 24/24 reach. The grant is
   signed; the residual is least-privilege.
5. **[any seat fielding an IRPT question] Scale is unproven.** Exactly ONE pre-343 receipt existed, so
   nothing here says the back-fill works at volume. A firm with no objects reads 0 and that is not
   coverage.
