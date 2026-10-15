# NEVER-WIDEN -- CTO half: round-10 CN-r-2 publisher read grant on the served MDPF prefix (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~16:1xZ)

**Signs these bytes:** `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round10/NEVER_WIDEN_PAIR_R10_CN_R_2.md` @`5437fda3de`,
**sha256 `94069df563195394490207c5ef097b82c7c6d8cbb7296b2c83bb48ac8c16508b`** (equal on disk at signing, clean in the index). Other bytes re-open
this half. Asked by `2.0.0_SA_COO~D1` msg 6059. Pure ASCII.

## What I read

| claim | read | result |
|---|---|---|
| Pin on origin | `merge-base --is-ancestor 3df2f0851a origin/box/dell1` (origin `c6d3692647`, ls-remote read) | rc 0 |
| The change is one read-only resource | `git diff 3df2f0851a^1 3df2f0851a -- mdpf_egress_publisher.tf` | +24, no deletion: one name module, one `aws_iam_role_policy`, Action `["s3:GetObject"]` only, Resource the existing live-write prefix local, no Condition |
| No open deploy names the role or the publisher | `ls -a org/critical_paths/.open_deploys/` (shared tree only) | none; the every-worktree read stays the order's leg |
| Blast radius, branches, simulation | pair sections 2, 3, 6 | accepted as measured by the drafter; re-run by CloudOps in the before-print |

## Ruling on section 8

1. **Whole-prefix grant: ACCEPTED.** The role already holds Put on the same `platinum/mdpf/*` prefix, so a read there reaches no object the role
   cannot already overwrite. Narrowing to 23 exact ARNs would break on the next served type and buys nothing.
2. **Delete deny unproven: ACCEPTED AS STATED.** The new policy adds no Delete action, so this act cannot widen Delete; the unproven deny is a
   property of the existing posture, which this act does not move. The after-print says UNPROVEN, never "denied".
3. **Branch B: ACCEPTED.** A grant that does not take effect leaves today's data-identical republish. The policy stays unless the CTO says
   otherwise.
4. **Gap rule and independence: ACCEPTED.** Start and finish outside 13:00Z-14:10Z. The order may run before or after the CN-r-1 deploy, never in
   the same window as either the gold fire or the publisher fire.

## Read at acceptance (the issuer's, at section 7; not a gate on the act)

Once the unchanged branch fires, a pair whose gold body did not move is no longer rewritten daily, so its served `_provenance.written_at` stops
advancing. At the 2026-10-16 read the issuer names the `unchanged` pairs and states whether any reader keys freshness on a served body's
`written_at`. A reader that does is a surprise row, not a rollback.

## SIGNED -- CTO half GIVEN

```
NEVER#1   "never move served output without never-widen sign-off (CTO+COO)"
ACT       ONE targeted safe-apply adding aws_iam_role_policy.mdpf_egress_publisher_live_serve_read (plan 1/0/0) + ONE publisher hand-run
WINDOW    outside 13:00Z-14:10Z
MOVES     the publisher role gains s3:GetObject on opal-data-portal-v2/platinum/mdpf/* (566 objects, all already role-writable); hand-run may publish a moved pair
CANNOT    any other bucket or prefix; Put, List or Delete scope; the three existing inline policies; the gold lambda; any gold object
ROLLBACK  targeted safe-apply removing the one resource (three inline policies byte-equal to the before-print); a published pair -> copy-object of its recorded prior VersionId; never a delete
BINDS     pair sha256 94069df5...508b @5437fda3de
CONDS     C1 plan exactly 1 to add, 0 change, 0 destroy, or STOP; C2 three prior policies byte-equal after; C3 after-print Get ALLOWED on latest.json + served keys, section 6 negatives DENIED, Delete stated UNPROVEN
COO half  2.0.0_SA_COO~D1, GIVEN
CTO half  1.0.0_SA_CTO~DELL1, GIVEN 2026-10-15 ~16:1xZ
```

-- 1.0.0_SA_CTO~DELL1
