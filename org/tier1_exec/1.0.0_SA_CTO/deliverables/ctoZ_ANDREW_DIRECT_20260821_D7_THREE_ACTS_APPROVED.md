# ANDREW-DIRECT 2026-08-21 ~1346Z -- THE THREE HELD D7 ACTS ARE APPROVED

**Recorded by:** 1.0.0_SA_CTO~Z (the seat that carded them)
**Surface:** /open-calls at the CTO~Z terminal, 3 cards, 2026-08-21 13:45Z
**Broadcast:** same turn, per the record+broadcast law (org/XXX.md)

## HIS WORD, VERBATIM

> **"approved on all three, proceed"**

That answers, in card order:

1. **CALL 1 -- run the ticket-center apply on this box.** APPROVED.
2. **CALL 2 -- write the W-F import edge (the escalation wiring).** APPROVED.
3. **CALL 3 -- wire the gateway to send Teams messages as HTML.** APPROVED.

## SCOPE -- READ THIS BEFORE ACTING

**His word covers the three acts AS CARDED, at the cost AS STATED.** It is not a
general apply authorization for D7 and it is not a licence to widen any of the
three. An approval covers what the approver was shown -- the same standard that
held F-3 back from "proceed with D E F" in the first place.

**WHAT HE WAS SHOWN, per card:**

- **CALL 1** -- the apply CARRIES W-A's QUEUE (81c502cff2 + 4d5a92f4d7 +
  78cd2b0695), not a single change; deploy ledger opened at start and closed
  in-session per NEVER#6.
- **CALL 2** -- sequenced AFTER Call 1, because the 2pm sweep has nothing to
  escalate until tickets flow through an applied Lambda.
- **CALL 3** -- cost is a `systemctl restart` through `safe-ec2-deploy.sh`, NOT
  an instance bounce and NO IP move; it drops in-flight MCP calls at
  `GATEWAY_WORKERS=1` and re-derives the `.env` from four Secrets Manager
  secrets on the way up.

## PLACEMENT -- RULE 26 RESOLVES CLEANLY, MEASURED

All four build commits are ancestors of HEAD on this box and all four were
authored by `0.5.0_AE_OpalETL~Z`, a site-Z seat:

| commit | act | author | ancestor of HEAD |
|---|---|---|---|
| `81c502cff2` | W-A lifecycle analytics | 0.5.0_AE_OpalETL~Z | YES |
| `4d5a92f4d7` | W-E SES first line | 0.5.0_AE_OpalETL~Z | YES |
| `78cd2b0695` | TO-A W-E re-cut | 0.5.0_AE_OpalETL~Z | YES |
| `7b7b0004a9` | D-HTML renderer | 0.5.0_AE_OpalETL~Z | YES |

**So the builder and the box already agree.** Rule 26's test -- the seat that
BUILT a change APPLIES it, on its own box, under the normal wrappers -- names
`0.5.0_AE_OpalETL~Z` for all three acts with no ferry and no placement question.

**MECHANISM VERIFIED LIVE ON THIS BOX 2026-08-21 ~1346Z:** `safe-apply.sh`
PRESENT, `safe-deploy.sh` PRESENT, `infra/aws/ec2/safe-ec2-deploy.sh` PRESENT,
`infra/aws/ec2/verify-ec2.sh` PRESENT, deploy-completion ledger dir PRESENT.
Terraform resolves on PATH at **v1.15.8**; **`.tools/terraform.exe` DOES NOT
EXIST here** -- exactly as Rule 26 records. Resolve the binary, do not assume
the baked path.

## THE ONE HAZARD THIS CREATES, AND IT IS A DOUBLE-APPLY

`org/tier2_senior/0.7.0_AE_CloudOps/task_orders/D7_TICKETING.WA-APPLY.laptop-apply-leg-ticket-center-lifecycle-v2.md`
is **`staged` with its ACTIVATION CONDITION ALREADY MET (~0110Z) and the GO
deliberately deferred to the next working block.** That is a live laptop-side
apply leg for the SAME Terraform.

**If it fires after this one lands, two boxes apply the same state.** Rule 26
supersedes its placement, so it should not fire -- but a superseded TO that
nobody was told about is exactly the shape that fires anyway. Surfaced same turn
to `2.0.0_SA_COO~Z` (issuing seat) and `0.0.0_AB_MSTR~Z`.

**This is a NOTIFICATION, NOT A GATE** -- I am not holding the CloudOps seat and
not editing another lane's TO. The placement moved by Andrew's word and by law;
the seats that own it decide what their record should say.

## F-2 -- DECIDED AT THIS LANE, NOT CARDED

Routed to `0.5.0_AE_OpalETL~Z` as a defect fix rather than put to Andrew: it is
a latent-defect repair routing into an EXISTING `REFUSED` outcome, not a new
capability, and holding a one-line fix for sovereign word is gate-manufacture
rather than caution.

**`2.0.0_SA_COO~Z` sharpened the severity and it survives the sharpening:**
unreachable via the product surface (`created_at` is server-generated), but
**reachable via any operator or migration write.** That makes the fix more
warranted, not less -- and it is still latent, never fired, and reversible.

## STANDING CONSTRAINTS THAT DID NOT MOVE

- **NEVER#6** -- a begun deploy FINISHES in-session or rolls back loud. Ledger
  opened at deploy-start, closed at completion.
- **The notification moratorium stands.** Nothing here authorises an alarm,
  monitor, freshness checker, SNS topic or SES bounce/complaint clone.
- **Zero crons.** No loop is armed by any of this.
- **Rule 22a** -- a green plan and a green config read do not establish that
  code RUNS. Verify on the layer the claim is about.

-- 1.0.0_SA_CTO~Z, 2026-08-21
