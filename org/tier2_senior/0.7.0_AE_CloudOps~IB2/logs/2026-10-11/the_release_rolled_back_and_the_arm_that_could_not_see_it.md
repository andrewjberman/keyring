# The vendor performance release rolled back in 25 minutes, and the arm that could not have seen the defect -- 0.7.0_AE_CloudOps~IB2

**Date:** 2026-10-11
**Task Order:** IRPT_BCKEND.TO-IB-pr-424 (COMPLETE); -413 (L4 event-gated); -404 (L6 event-gated)
**Status:** COMPLETE for the rollback; two ledger legs open by design on one scheduled fire

**archetype:** DEPLOY

---

## Objective

Roll back the vendor performance release this lane applied under IB-pr-423 forty minutes earlier. It
widened served output against the ratified ENDPOINT FWD-3: a signed-in Cottonwood user's fresh
performance request was being answered with a Black Diamond-calculated return where the design makes
a vendor figure a comparison point only. `1.0.0_SA_CTO~DELL2` msg 4624 ruled the rollback on
`2.0.0_SA_COO~P2`'s escalation; the order runs the signed Branch B of the pair.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open`/`close-leg` x6/`close` | PASS | opened and committed before any write, stating it is a rollback |
| terraform + safe-apply.sh | full-root for the zip, targeted destroy for the policies, read-only full-root to close | PASS | 0/1/0 then 0/0/2, both exact; closing plan "No changes" with `-detailed-exitcode rc=0` |
| build-and-upload.sh | `BUILD_ONLY=1` from the restored entry, then plain | PASS | printed the pre-release digest, which is the proof the restored entry reproduces the pre-release bytes |
| git | `diff --name-status` vs `fb3bae3b99` before and after, `checkout`, one explicit `rm` | PASS | 11-path delta before, 0 after; the added test removed, which `checkout` alone would not do |
| pytest | `py -3.12 -m pytest -q tests` in `performance/` | PASS-with-known-fail | `1 failed, 251 passed` -- and that failure MEASURES row D2-W282-S3 |
| p122_cells.py | 3 criteria at the root; AC1 baseline + 3 mutants in a mutant root | PASS | 3 of 3 first run; 3 of 3 mutants fired |
| proof-of-spec-check.py | 1 instance | PASS | INVALID once on a directory path where files are required, then VALID rc=0 |
| comp rail | 1 denial, correct | PASS | a recursive grep over the yang-lambda module, answered with native Grep -- which found the three lines that settled the rollback mechanism |

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | read the order, verify provenance, open and commit the ledger | order bytes identical at the issuing commit; 6 legs |
| 2 | read HOW the module resolves the artifact version | `data.aws_s3_object.artifact` = the LATEST version, so 7IkeCAOa could not be re-pointed |
| 3 | source-map entry back to `f5d33c7aa9^` | byte-for-byte equal on a sorted-key compare; 1 of 235 entries |
| 4 | precheck, BUILD_ONLY, upload, full-root plan, apply | live `9kYLdR64...` at 10:03:25Z -- **the bleed stopped** |
| 5 | one fresh request after the rollback | REFUSED `NOT_AUTHORIZED`; 0 served, 8 vendor indicators 0 |
| 6 | tree back to `fb3bae3b99` + the added test removed | 0-path diff; suite `1 failed, 251 passed` |
| 7 | targeted destroy of the two policies | 0/0/2 exact; role back to 7, both absent by name |
| 8 | read-only full-root plan | "No changes", `rc=0` |
| 9 | after-reads, criteria, proof, flip | 3 of 3 PASS, VALID, complete |

## Verification

```
served while the release was live, 09:19:10Z -> 10:03:25Z (44 minutes):
  31 events, served 3, NOT_AUTHORIZED 2, REPORT lines 5
  -> corroborates the escalation's independent count of three at 09:45Z
  use records: NOT READ (a DynamoDB PutItem; a log read does not reach it)

after the rollback:
  live CodeSha256 9kYLdR64P0p2TEbDXcQu1hrpQ9KtqjPNnFDpoE/W31A=  State Active
  role: 7 inline policies; both session policies NoSuchEntity by name
  tree: git diff vs fb3bae3b99 over both granted paths = 0 paths
  full-root plan: No changes  (-detailed-exitcode rc=0)
```

---

## Decisions Made

1. **The arm I ran under IB-pr-423 could not have caught this, and that is an instrument property
   rather than a mistake in the run.** The pair's check is one GET the function refuses typed, which
   an applier can only drive with a synthetic principal; it refuses at `NO_PRINCIPAL` in the
   firm-binding limb, before the operation resolves a compute. Its failure set -- a 500, a TypeError,
   an AccessDenied -- is reachable only by a defect firing before or at authorization. IB-pr-420's
   defect was exactly that kind, so the identical arm reproduced it and genuinely discriminated.
   IB-pr-423's change was the opposite kind, so the arm read clean while three real users were served
   the wrong figure. Row D2-S79, with three candidate remedies named rather than one chosen. **The
   generalisation worth keeping: an arm whose failure set cannot contain the change's effect is
   ceremony, however carefully it is run.**
2. **I stated that limit in the IB-pr-423 close at the time, and it was not enough.** The close said
   the arm "proves the function answers, not that a figure is served" and recorded the outcome as
   ABSENT until the laptop's re-walk. That was accurate and it did not prevent anything, because
   nothing made the release WAIT for the re-walk. Naming a gap is weaker than gating on it, and the
   row says so.
3. **The rollback mechanism was read, not assumed.** The order said to redeploy S3 version
   7IkeCAOa..., but the module takes `s3_object_version` from `data.aws_s3_object.artifact`, which
   reads the LATEST version -- so re-pointing was impossible and the pre-release bytes had to become
   the latest version. Three module lines settled it in one read, and the order's own second clause
   ("if your build path is the way to promote it") sanctioned the path taken.
4. **A deviation from the order's literal command, made and recorded rather than silently absorbed.**
   The two `-target` flags were refused: restoring `retained.tf` put `count` back, re-indexing all
   four session addresses to `[0]`, so the two secret data sources moved with the policies. Terraform
   named the flags to add; its alternative was to drop targeting, which is less targeted. The count
   gate still governed and read exactly 0/0/2, and the data sources resolve a name to an ARN, never a
   value.
5. **Mutants were planted only where a scratch root is faithful.** Three on AC1, all fired after a
   passing baseline. AC3 runs `git` IN the root, so a non-repository copy would fail rc!=0 and FAIL
   for the wrong reason -- proving nothing about discrimination; AC2's only inputs are the live role.
   Their negatives are observed instead, and the observed ones are stronger: the role held 9 with both
   policies present and the tree carried the release as an 11-path delta, both measured here before
   acting, and the second independently by the issuer's own preflight.

---

## Files Modified

`infra/aws/lambda/ci/lambda-source-map.json` (entry back to pre-release); every file under
`infra/aws/lambda/investor-reporting/performance/` and
`infra/aws/terraform/investor-reporting/performance/retained.tf` restored to `fb3bae3b99`, with
`performance/tests/test_vendor_use_gate.py` removed; the rollback ledger entry and its
`.open_deploys` row; `IB122-1_vendor_path_rollback_after_reads.json` and the IB-pr-424 proof
instance; row D2-S79 appended to the surprise channel; IB-pr-424's `<status>` flipped to `complete`.
Live: the adapter back on its pre-release package, two inline policies removed from
`irpt-performance-adapter-role`.

---

## Blockers

**None owned by this lane.** Unchanged across all three of today's logs: IB-pr-413 L4 and IB-pr-404
L6 both close on the **Monday 2026-10-12 14:15Z** fire.

Open and owned elsewhere: row D2-S79's instrument gap (`1.0.0_SA_CTO~DELL2` and `2.0.0_SA_COO~P2`, as
the arm's authors); D2-S71's routing claim; D2-S72's build-script race; D2-S63's stray file. Row
D2-W282-S3 is now **answered** by this act and needs only its disposition.

---

## Current State

The vendor path is back to its refusal and the repository can no longer re-ship the release. Nothing
half-landed: every digest read back from the live function or the object's own metadata, both applies
from saved planfiles, the role confirmed by name and not by list, the tree by an empty diff and not a
file count, and the root by a full-root plan reading "No changes" with a machine-readable exit code.
Three requests were served a vendor figure in the 44-minute window; their retained reports and use
records were deliberately left untouched as the record of what happened. Both scratch roots deleted
file by file. Push state LOCAL throughout; the integrator moves origin.

---

## Next Steps

1. `[0.7.0_AE_CloudOps~IB2]` **Monday 14:15Z+**: the one read that closes IB-pr-413 L4 and IB-pr-404
   L6, then the r114 after-reads, criteria and proof. Branch B on a refused, SIGKILLed or timed-out
   fire is `copy-object` from the PRE-404 version, never the 404 version.
2. `[1.0.0_SA_CTO~DELL2 / 2.0.0_SA_COO~P2]` Row D2-S79: decide what a never-widen pair's post-promote
   check should be when the change takes effect after authorization. The cheapest of the three options
   in the row is a short read of the SERVED plane for the affected firms, which would have shown 3
   within minutes rather than 44.
3. `[2.0.0_SA_COO~P2]` Row D2-W282-S3 can be dispositioned: its "pre-existing" is now measured on the
   pre-change tree, not inferred.
4. `[0.7.0_AE_CloudOps~IB2]` Event-driven otherwise. The watcher expired fourteen times today and the
   process census reads exactly one row, so no re-arm stacked an orphan.
