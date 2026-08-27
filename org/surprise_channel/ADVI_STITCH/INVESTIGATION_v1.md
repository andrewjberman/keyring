# INVESTIGATION v1 -- ADVI_STITCH (Phase A, round 1)

**Owner:** `3.0.0_SA_CVO` (channel) - home MINTED 2026-08-25T21:4xZ on the first item, per the stated
trigger (the home mints on an item, never as an empty file).
**APPEND-ONLY during the round.**
**Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` - `class {OBSERVATION, BLOCKING}` x
`hazard_standing {ARMED, INERT}`; "latent hazard" = prose for (any class, ARMED).

**Laptop fabric.** Items are `ADVI_STITCH-S{n}`.

---

## S1 -- AC2's deny-target named an UNMINTED tree, so the criterion would have shipped a true, well-controlled GREEN about a path holding nothing

**OBSERVATION x ARMED. Surfaced 20:43Z by `0.7.0_AE_CloudOps~J`, DISARMED SAME-TURN at 20:46Z by
`2.0.0_SA_COO` (issuer) via a TO amendment. The seat did not halt and did not touch the file.**

`STIA1AE-AC2` probed DENY on `blackdiamond/49financial/{bronze,silver}/*`. Live enumeration:
`blackdiamond/` has **EXACTLY TWO** children, `49f/` and `cottonwood/` (denominator 2 of 2, positive
control run against the bucket root returning 13 prefixes). The real tiers holding data are
`blackdiamond/49f/{bronze,silver}/`, sampled in both.

**WHY IT WAS ARMED:** run as written, AC2 returns a TRUE, correctly-denominated DENY on a path
nobody uses, ships GREEN on the criterion the TO says "carries his ruling into IAM", and leaves
`STI-inv-1`'s actual protective property COMPLETELY UNTESTED. **A false green on a protective
control -- the worst direction for this class.** O-1's oracle could not catch it either: it expects
EMPTY, and "empty because unminted" and "empty because the whole subtree is misnamed" are
byte-identical at that oracle.

**THE ISSUER'S RULING CORRECTED THE SURFACING SEAT'S PREMISE, and that is worth recording:** the
seat inferred `49financial` was a TYPO for `49f`. It is not. `49financial/` is a **DELIBERATE MINT**
under Rule 17b (`{vendor}/{firm}/{medallion}`); `49f/` is the legacy alias and holds the SOURCES.
Both spellings are correct and mean different things. **The DS lane's `STI-b-0` root was UNCHANGED
and `0.4.0_DS_ClientPlatform~Q` was told so directly** -- which is what stopped a peer hardening the
wrong root while building.

**RESIDUAL (CVO, 21:0xZ):** the amendment was measured UNCOMMITTED -- `git show HEAD:<TO>` still
carried the defective target (1 occurrence at HEAD, positive control 1 corrected in the working
tree). A fresh clone or a `HEAD` read serves the disarmed spec. Routed to the issuer; not this
channel's to fix.

---

## S2 -- the same criterion is UNOBTAINABLE, and amending its target did not reach the second cause

**BLOCKING x ARMED. Surfaced 20:57Z by `0.7.0_AE_CloudOps~J`, routed to the ISSUER same turn by
`3.0.0_SA_CVO` (71433). Seat NOT held -- still on prep; this is a decision needed before the APPLY.**

`STI-b-4` says "LANDING IAM" and **never names a PRINCIPAL.** AC1 says "the principal", AC2 "the
same principal"; neither the TO, the cell, nor `STI-b-1` resolves the referent -- `STI-b-1`
attributes writes to "0.6.0/0.7.0", which are AGENT SERIALS, not IAM principals.

Tested against the obvious candidate (`user/Andrew_Berman`), three separate invocations, ONE
`--resource-arns` each per the TO's own discipline:

```
ARM 1  TARGET      PutObject .../49financial/bronze_legacy/probe.xlsx          -> allowed
ARM 2  POS CONTROL PutObject .../49f/silver/dim_account_xref/.../data.parquet  -> allowed
ARM 3  DISCRIM     PutObject on a bucket WE DO NOT OWN                         -> allowed
ARM 3b DISCRIM     organizations:LeaveOrganization on "*"                      -> allowed
```

**ARMS 3/3b ARE THE FINDING: that principal is unrestricted admin.** Every arm returns `allowed`
whether or not the claim is true -- AC1's green would carry ZERO information (Rule 22
DISCRIMINATION fails outright), and **AC2's required DENY is not merely unmet, it is UNOBTAINABLE:
an admin is never denied, so the criterion can never pass however the grant is written.**

**WHY THIS IS A SEPARATE ITEM FROM S1 AND NOT A CONTINUATION:** S1 moved the RESOURCE. This defect
is in the PRINCIPAL, and a deny-arm against an admin returns `allowed` on the corrected live tree
exactly as it did on the unminted one. **Same criterion, same GREEN, second cause.** The two are the
`(action, resource)` trap of Rule 22a seen from both sides, and fixing one silently leaves the other.

**REMEDY SHAPE (issuer's, not this channel's):** AC1/AC2 need a SCOPED WRITE ROLE named as the
principal -- the identity the landing job will actually assume. Until that referent exists the
criterion has no subject.

**METHOD NOTE WORTH KEEPING:** the surfacing seat ran arms 3/3b *because arms 1 and 2 agreeing made
them distrust the instrument* -- "two arms agreeing is what a dead instrument looks like." Neither
the TO nor the decomp asked for that control, and nothing else in the round would have found this.

---

```json
[
  {
    "id": "ADVI_STITCH-S1",
    "surfaced_by": "0.7.0_AE_CloudOps~J",
    "surfaced_at": "2026-08-25T20:43Z",
    "one_line": "STIA1AE-AC2's deny-target named blackdiamond/49financial/{bronze,silver}/* -- an UNMINTED tree -- so the criterion would ship a true, well-controlled GREEN while the live 49f/ tiers went untested.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws s3 ls s3://opal-data-assets/blackdiamond/ -> EXACTLY 2 children (49f/, cottonwood/), denominator 2 of 2 enumerated",
        "positive control: aws s3 ls s3://opal-data-assets/ -> 13 prefixes, not empty, so the ABSENT verdict is not a broken retrieval",
        "live keys sampled: blackdiamond/49f/silver/dim_account_xref/date=2026-07-14/data.parquet (228444 B); blackdiamond/49f/bronze/allocation_390224/2026-07-14/data.xlsx (10684756 B)",
        "TO amendment landed 2026-08-25 ~20:46Z by 2.0.0_SA_COO in ADVI_STITCH.TO-A1-AE.legacy-landing-iam.md, repointing AC2 to blackdiamond/49f/{bronze,silver}/*",
        "CVO residual measured 21:0xZ: git show HEAD:<TO> still carries the defective 49financial/bronze/* target (1 occurrence at HEAD; positive control 1 corrected in working tree) -- the disarm is UNCOMMITTED"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "The issuer's ruling CORRECTED the surfacing seat's premise: 49financial/ is a DELIBERATE Rule 17b mint holding DESTINATIONS, 49f/ is the legacy alias holding SOURCES. Both spellings correct, different meanings. The DS lane's STI-b-0 root was unchanged and 0.4.0_DS_ClientPlatform~Q was told directly, which prevented a peer hardening the wrong root mid-build. Disarmed 3 minutes after surfacing."
  },
  {
    "id": "ADVI_STITCH-S2",
    "surfaced_by": "0.7.0_AE_CloudOps~J",
    "surfaced_at": "2026-08-25T20:57Z",
    "one_line": "STI-b-4 never names a PRINCIPAL, and the candidate identity is unrestricted admin -- so STIA1AE-AC2's required DENY is UNOBTAINABLE, not merely unmet, and AC1's ALLOW carries zero information.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "simulate-principal-policy, 3 separate invocations, ONE --resource-arns each per the TO's discipline, principal arn:aws:iam::313476888478:user/Andrew_Berman",
        "ARM 1 TARGET PutObject .../49financial/bronze_legacy/probe.xlsx -> allowed",
        "ARM 2 POSITIVE CONTROL PutObject .../49f/silver/dim_account_xref/date=2026-07-14/data.parquet -> allowed",
        "ARM 3 DISCRIMINATION PutObject on a bucket outside our ownership -> allowed",
        "ARM 3b DISCRIMINATION organizations:LeaveOrganization on '*' -> allowed",
        "STI-b-1 attributes the writes to '0.6.0/0.7.0', which are AGENT SERIALS and not IAM principals, so the referent is unresolved in the decomp as well as the TO",
        "RESOLUTION: iam get-role opal-advi-stitch-landing-role -> exists, created 2026-08-25T21:31:32Z (CVO's own live read, not the apply output)",
        "RESOLUTION: iam get-role-policy opal-advi-stitch-landing-scoped -> 6 statements, 5 Allow + 1 Deny 'NeverTheLiveTiers'",
        "RESOLUTION: post-mint AC2 arms return explicitDeny on 49f/bronze/allocation_390224/2026-07-14/data.xlsx and 49f/silver/dim_account_xref/date=2026-07-14/data.parquet, vs implicitDeny on ungranted prefixes -- the spread the admin principal could not produce"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "RESOLVED-AT-SOURCE 2026-08-25T21:31:32Z by the executing seat minting opal-advi-stitch-landing-role, which is the remedy shape named at surfacing. CVO verified the role LIVE (6 statements: 5 Allow + NeverTheLiveTiers Deny) rather than from the apply output. THE DISCRIMINATION IS THE PROOF: post-mint the same instrument returns THREE distinct verdicts on one principal -- allowed (targets + positive control), explicitDeny (live + prospective arms, the Deny firing), implicitDeny (schwab, nna_atomic, cottonwood, merely ungranted). explicitDeny != implicitDeny establishes the live-tier refusal as DELIBERATE. Against the pre-mint admin identity all four arms returned allowed. That contrast is the case for minting rather than borrowing, demonstrated rather than argued. SEPARATE CAUSE FROM S1: S1 moved the RESOURCE, this was the PRINCIPAL -- the two halves of Rule 22a's (action, resource) trap, where fixing one silently leaves the other. Executing seat was never held. Method note: the seat ran the admin discrimination arms because arms 1 and 2 agreeing made them distrust the instrument -- a control neither the TO nor the decomp asked for."
  }
]
```
