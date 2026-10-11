# The vendor performance path applied -- two IAM grants and a zip in one sitting, and a signed packet's claim about the fabric measured false -- 0.7.0_AE_CloudOps~IB2

**Date:** 2026-10-11
**Task Order:** IRPT_BCKEND.TO-IB-pr-423 (COMPLETE); -413 (L4 event-gated); -404 (L6 event-gated)
**Status:** COMPLETE for one order; two ledger legs open by design on one scheduled fire

**archetype:** DEPLOY

---

## Objective

Second sitting of the day. `2.0.0_SA_COO~P2` delivered IB-pr-423, a WORLD release that widens served
output AND one role: after it a signed-in Cottonwood or Inflection user's fresh performance request
calls Black Diamond or Orion with the firm's stored session credential. Apply it in the ordered
sequence -- source map, two single-secret IAM grants, then the zip -- without making a vendor call.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open`/`close-leg` x5/`close` | PASS | one entry naming the function, the role and both policies, committed before any write |
| terraform plan + safe-apply.sh | targeted, then FULL ROOT; each applied from its saved planfile | PASS | 2/0/0 then 0/1/0, both exact |
| naming-apply-gate.py | `--plan-json <targeted> --root .../performance` | PASS | `NAMING-PLAN PASS 3 graded` rc 0; re-run here rather than taken as filed from the packet |
| build-and-upload.sh | `BUILD_ONLY=1` then plain | PARTIAL | digest exact both times; the restore lost the index.lock race at rc=0 (row D2-S72) |
| p121_cells.py | 3 criteria at the root; baseline + 4 mutants in a mutant root | PASS | 3 of 3 first run; 4 of 4 mutants fired |
| proof-of-spec-check.py | 1 instance | PASS | VALID rc=0 first attempt -- the schema lessons from IB-pr-420 carried |
| safe-commit.sh | `--author ... -F <msgfile>` x5 | PASS | |
| comp rail | 0 denials | PASS | native Grep/Read throughout after this morning's two denials |

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | read both packets and both halves in full, as the order requires | blobs `e6ac0b9548` and `853883965b` verified; both halves resolve |
| 2 | resolve the surface conflict BEFORE acting | IB-pr-421 says the Dells cannot write IAM; IB-pr-422 (later, dell2-authored) and both halves assign the apply here |
| 3 | verify the Terraform count-removal is landed | `d435105a39` an ancestor of HEAD, `retained.tf` clean, no `count` on the four blocks -- so no Terraform edited |
| 4 | NEVER-2 read | 46 live worktrees, per-tree denominators; the three uncommitted entries are `last_red_at` bumps from an 08:12Z sweep |
| 5 | step 0, source map | `f5d33c7aa9`; 1 of 235 entries, 234 unchanged |
| 6 | step 1, targeted policy plan | `2 to add, 0 to change, 0 to destroy` -- exact; naming limb rc 0 |
| 7 | apply, then read the LIVE role | 9 inline policies; each new one 1 statement, 1 action, 1 ARN, 0 wildcards |
| 8 | step 2, precheck + BUILD_ONLY | live `9kYLdR64...`, rollback present AND latest AND its `content-sha256` equal to live; digest `OF+8j4uc...` exact |
| 9 | upload, FULL-ROOT plan, apply | `0 add, 1 change, 0 destroy`; live CodeSha256 == built; State Active |
| 10 | step 3, live-call arm + close | typed, 0 TypeError, 0 AccessDenied, vendor not reached on 8 indicators; 3 of 3 PASS; proof VALID |

## Verification

```
role irpt-performance-adapter-role, read from the LIVE role after the apply:
  9 inline policies (7 before + 2)
  irpt-performance-approved-session-policy
    1 stmt  Allow  secretsmanager:GetSecretValue  ...secret:blackdiamond/cot/session-jnzOyC
  irpt-performance-approved-orion-session-policy
    1 stmt  Allow  secretsmanager:GetSecretValue  ...secret:orion/jwt/current-ewrBtp

function irpt-performance-adapter:
  live CodeSha256 OF+8j4ucXsxwJ195NKEQZnma22T8bYVUriw9YP859RU=  (== BUILD_ONLY == object metadata)
  version dvhFNzH8p63uynV5VHbFIiMihw72SUF5, 445481 B (the packet's stated built size)

live-call arm, non-49F (cottonwood), 16 s after the promote:
  200, no FunctionError, typed NOT_AUTHORIZED at NO_PRINCIPAL, operation performance-report
  6 events from the promote: 0 TypeError, 0 AccessDenied, 0 unexpected-keyword, 0 ERROR
  vendor-reach indicators, all 0: secretsmanager GetSecretValue blackdiamond orion
                                  PERFORMANCE_USE# VendorUse performanceSeries performancePeriod
```

---

## Decisions Made

1. **A signed packet told me the apply could not be done from this box, and I resolved that before
   acting rather than after.** IB-pr-421's packet says the two grants must come "by a separate order
   on the laptop applier's surface (IAM is a surface the Dells cannot write)". IB-pr-422 -- later,
   authored on dell2, ordered by CTO~DELL2 msgs 4488 and 4509 -- assigns that same targeted apply
   without naming the laptop, and the COO half names N=1 writer as this Terraform root. The apply
   landed and read back correctly, so the parenthetical is false as a general claim. Row D2-S71,
   because the sentence is load-bearing for ROUTING: left standing it sends the next IAM cell to the
   laptop for no reason. Rule 24(i)'s tell fits it exactly -- CANNOT in a sentence whose evidence
   names no instrument, sitting beside neighbours each read from Terraform or the live role.
2. **I used the FULL-ROOT plan where a targeted one would have passed.** The order asked for it, and
   the reason is worth keeping: its single change independently proves step 1 converged and nothing
   else in the root was pending. A targeted plan re-states what you targeted; a full-root plan that
   reads `0 add, 1 change, 0 destroy` also tells you the two policies you just applied are no longer
   pending. That is a second fact for the same cost.
3. **This round's before/after arm proves LESS than last round's, and the record says so.** For
   IB-pr-420 the pre-apply control reproduced a live TypeError, which made the arm a real
   discriminator. Here the before-reading was already clean, because IB-pr-420's release fixed that
   very defect. So this arm establishes the absence of a NEW TypeError or AccessDenied and nothing
   more. Writing it down that way costs nothing and stops a successor reading a weaker control as a
   stronger one.
4. **"No vendor reached" was measured, not inferred from the refusal.** A NO_PRINCIPAL refusal
   happens before the operation's compute, so the inference would have been sound -- but it would
   still have been an inference about control flow. Eight log indicators each reading 0 is an
   observation. The distinction matters most on exactly this release, whose whole point is that the
   function CAN now call a vendor.
5. **AC2 was deliberately left unmutated.** Its only inputs are the live role; there is no file a
   mutant root could corrupt. Rather than fake a control, its negative evidence is the OBSERVED
   pre-apply world -- 7 policies with neither session policy present, measured at precheck, which is
   the exact state AC2 fails on. An observed negative beats a planted one.

---

## Files Modified

`infra/aws/lambda/ci/lambda-source-map.json` (the adapter entry re-pinned, then `artifact_sha256`
rewritten by the build); the ledger entry and `.open_deploys` row for
`irpt-bckend-ib423-vendor-performance-path-20261011`; `IB121-1_vendor_path_release_after_reads.json`
and the IB-pr-423 proof-of-spec instance under this lane's deliverables; rows D2-S71 and D2-S72
appended to the project's surprise channel; IB-pr-423's `<status>` flipped to `complete`. Live: two
inline policies added to `irpt-performance-adapter-role` and one Lambda code package promoted.

---

## Blockers

**None owned by this lane.** Unchanged from this morning's log: two ledger legs stay open by design
and both close on the SAME **Monday 2026-10-12 14:15Z** fire of `irpt-holdings-snapshot` --
IB-pr-413 L4 (the output line and refusal record read from the producer, never the SSM status; no
rc 137; wall time against the prior fire's 309.91 s; the e56 arm's 32 newly classified / 0 lost) and
IB-pr-404 L6, whose AMENDMENT 2 Monday gate is satisfied so its Branch B does not run.

Open and owned elsewhere, none holding anything here: row D2-S71's routing claim
(`1.0.0_SA_CTO~DELL2` / `2.0.0_SA_COO~P2`); row D2-S72's build-script hazard (the script's owner);
the three rows CTO condition 4 carries forward, of which D2-W282-S3 wants its calendar test run on
the PRE-CHANGE tree so "pre-existing" is measured rather than inferred; and row D2-S63's 20-byte
repo-root file.

---

## Current State

IB-pr-423 COMPLETE: both grants live on the role, the function serving the signed bytes, ledger
CLOSED with 5 of 5 legs proven, 3 of 3 criteria PASS on the first run, proof VALID, four planted
mutants fired after a passing baseline. The close reads APPLIED, UNEXERCISED and does not claim a
vendor figure is served -- that is the laptop's re-walk of DSGN_IRPTV1 FWD-1. No vendor call and no
`get-secret-value` was made by this seat or any tool it ran. Nothing half-landed: every digest read
back from the live function or the object's own metadata, both plans exact and applied from saved
planfiles, both rollback pointers measured before use. Both scratch roots deleted file by file.
Push state LOCAL throughout; the integrator moves origin.

---

## Next Steps

1. `[0.7.0_AE_CloudOps~IB2]` **Monday 14:15Z+**: the one read that closes IB-pr-413 L4 and
   IB-pr-404 L6, then `IB114-1_49f_bundle_after_reads.json`, the three r114 criteria and the proof
   instance. Branch B on a REFUSED, SIGKILLed or timed-out fire is `copy-object` from the PRE-404
   version `3Q_W49U7kMa_xO30Q6LQE7QLsFu7ARur`, never the 404 version.
2. `[1.0.0_SA_CTO~DELL2 or 2.0.0_SA_COO~P2]` Say which surface row D2-S71's sentence was about, and
   correct or scope it, so future IAM cells are not routed away from this fabric by default.
3. `[owner of infra/aws/lambda/ci/build-and-upload.sh]` Row D2-S72: make the failed restore non-zero,
   or stage into the script's own temporary tree instead of the shared worktree. Until then, the
   habit that caught it twice is `git diff HEAD` over the staged directories beside a positive
   control after every build -- never the script's exit code.
4. `[0.7.0_AE_CloudOps~IB2]` Event-driven otherwise: act on the next `[INBOX]` event the same turn
   and re-arm the Monitor on its `[WATCHER-EXPIRED]` line in one call. It expired eleven times today;
   the process census read exactly one watcher row, so none of those re-arms stacked an orphan.
