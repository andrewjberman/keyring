# NEVER-WIDEN SIGN-OFF -- CTO HALF -- `IRPT_BCKEND` `IB-rtc-7`: the 49 Financial source principal

**Signer:** `1.0.0_SA_CTO`. **Date:** 2026-09-18 ~06:4xZ. **Law:** CLAUDE.md NEVER#1 (CTO + COO halves).
**Counterpart:** COO half `org/tier1_exec/2.0.0_SA_COO~B/deliverables/NEVER_WIDEN_SIGNOFF_COO_HALF_IRPT_BCKEND_IB-rtc-7_49F_PRINCIPAL.md` @`437789944a`.
**Subject packet:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtc-6.md`
@`119fda050a`, blob **`bb92a81c697c6d3fb8b01cb65fedfb9cb0563e38`**.

⭐ **THE PIN IS VERIFIED BY THIS SEAT, not copied from the hand-off:** `git hash-object` on the packet returns
`bb92a81c697c6d3fb8b01cb65fedfb9cb0563e38`, identical to the claim. **This half signs THOSE BYTES.** If the packet
changes, this half is void and is re-signed against the new blob.

**SCOPE: this half covers K1-K5 and NOTHING ELSE.** Five keys named in the packet, five keys named here.

---

## What this half independently verified rather than accepted

Three claims the packet makes are load-bearing for the grant working AND for it not widening. **Each was re-run here
on this seat's own instrument**, because a sign-off that re-reads the producer's reasoning is repetition, not a second
half.

| claim | instrument | result |
|---|---|---|
| the role name is **builder output**, not typed (Rule 30) | `lib/opal_naming.py` `name("irpt","49financial","directory-read","role")` | returns **`irpt-49f-directory-read-role`** -- **exact match** |
| the LIVE fence on `opal-data-49financial` **admits** it | `role/irpt-49f-directory-read-role` vs `ArnNotLike role/*-49f-*` | **MATCHES the admit pattern** -- the grant can work |
| it collides with **none** of the four old Deny prefixes | vs `role/cot-*`, `role/inf-*`, `role/mdpf-*`, `role/opal-assets-mdpf-*` | **0 of 4** -- no accidental denial |

⛔ **Rule 30's refusal is mine to make and there is nothing to refuse: the name is the builder's output, so this half
does not certify a typed string.**

---

## K1 -- `aws_iam_role.irpt_49f_directory_read` (`irpt-49f-directory-read-role`) -- CREATE

**MAY TOUCH:** creation of one IAM role in account `313476888478` whose trust holds exactly ONE statement naming
exactly ONE principal, `arn:aws:iam::313476888478:role/mdpf-daily-runner-ec2-role`.

⛔ **BLAST RADIUS, STATED AT ITS HONEST WIDTH AND NOT AT ITS NARROWEST:** the trust is as narrow as a principal ARN
permits, **but that principal is a SHARED HOST ROLE.** So **every process running as `mdpf-daily-runner-ec2-role`
becomes able to assume this role** -- the whole mdpf daily chain on `i-02448edb624a7a7cf`, the accrual bridge's SSM
runs, and the IRPT dispatch's builds. **That is the true radius and this half signs it with that width, not with
"one principal".** No user, no service and no other role can assume it.

**ROLLBACK:** revert the declaring commit's `principal_49f.tf`, then
`.tools/safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/directory apply`. Plans **2 to destroy** (role +
inline policy), nothing else. **There is no prior state for K1, so destroying it restores the world exactly.**

**BOTH BRANCHES:** if the apply creates the role, the radius above is live. **If it does not create it** (plan drift,
a refused apply), `K4`/`K5` are inert by construction -- `directory_runner.Firm49F` without the env variable uses the
host session and is refused by the fence with a WARN, which is today's behaviour. **Neither branch leaves a
half-grant.**

## K2 -- `aws_iam_role_policy.irpt_49f_directory_read` -- CREATE

**MAY TOUCH:** `s3:GetObject` on **5** enumerated dimension prefixes in `opal-data-49financial`, and **1**
`s3:ListBucket` on that bucket **conditioned** to those same five prefixes.

**MAY NOT TOUCH, and this is the half's substance:** **0 write actions anywhere**; **0 statements on any other
bucket**; ListBucket is prefix-conditioned rather than bucket-wide -- ⭐ **which is what allows N4 to
DISCRIMINATE.** A bucket-wide list would have made the negative control unable to fail. KMS: none required
(bucket is SSE-S3 `AES256`).

**BLASTS RADIUS:** whoever assumes K1 may list and read those five tables. **The host role itself gains nothing on
this bucket** -- the fence denies it and it holds no S3 grant there.

**ROLLBACK:** deleted with K1's destroy. Same command, same plan.

## K3 -- `aws_iam_role_policy.mdpf_runner` (`mdpf-runner-scoped`) -- +1 STATEMENT, 32 -> 33

**MAY TOUCH:** one `sts:AssumeRole` statement whose Resource is exactly K1's ARN.

**BLAST RADIUS: no new DATA access by itself.** It names K1; the grant K1+K2 describe is the whole of it. The
before-document is captured verbatim (`IB-rtc-6_host_policy_before.json`, sha256 `b1d8027fe940...`), and the
remaining 32 statements are unchanged in the plan. Size after: ~6,850 of the 10,240 aggregate inline limit.

**ROLLBACK:** revert the statement, re-apply **targeted** (below). The policy returns to the captured `before`
document **byte for byte**, which is checkable against that sha256 rather than asserted.

## K4 -- `irpt-directory-refresh` Lambda environment -- +1 KEY

**MAY TOUCH:** one env key, `IRPT_DIRECTORY_SOURCE_ROLE_MAP`, mapping `49financial` to K1's ARN. The other **4** keys
are unchanged.

**BLAST RADIUS:** `refresh.py` exports the ARN into the **49 Financial build's shell only**, keeping only a
role-ARN-shaped value. **Inflection and Cottonwood builds are unchanged.**
⚠ **The ARN is BUILT at plan time rather than read back from K1** -- the packet's reason is sound (a read-back prints
the whole environment as "known after apply" and HIDES this key). **The cost is that the ARN's correctness rests on
the builder, which is exactly why this half re-ran the builder above.**

**ROLLBACK:** revert the `schedule.tf` line, apply the directory root; the environment returns to 4 keys.

## K5 -- `refresh.py` + `directory_runner.py` (code; no IAM)

**MAY TOUCH:** the hand-off of the ARN, and `Firm49F`'s five dimension reads moving to a lazily assumed session
(`irpt-directory-source-read`). The BD xref stays on the host session.

**BLAST RADIUS:** none without K4. ⭐ **Neutral by construction: absent the env variable it behaves exactly as today.**
It reaches the host only through a rebuilt Lambda artifact and a DS-lane bundle mint -- **so K5 cannot land
accidentally as a side effect of a Terraform apply.**

**ROLLBACK:** revert the two edits; the next rebuild and mint restore prior behaviour.

---

## The named outcome, its writer count, and the branch that falsifies it

**NAMED OUTCOME:** *the new principal does not become a writer of the 49 Financial directory destination, and the
writer count stays **12**.*

⛔ **WRITERS OF THE NAMED PROPERTY, PRINTED AS THE LAW REQUIRES: 12 of 262** simulated principals on
`s3:PutObject` at `opal-data-bd/investor-reporting/directory/...` -- 8 `bd-*` roles, `mdpf-daily-runner-ec2-role`
(its existing destination write), and users `Andrew_Berman`, `Andrew_Berman_Console`, `Opal_Terminal`. **0 UNKNOWN**
across the census. The resource plane allows no write at all (2 statements, both CloudFront `GetObject`; 0 Deny).
The new principal simulates `implicitDeny` on that key.

**THIS HALF COVERS BOTH BRANCHES:** if the post-apply re-census reads **12**, the outcome holds. ⛔ **If it reads
13 -- or 12 with a DIFFERENT membership -- `IB-rtc-7` STOPS and rolls back K1+K2+K3 by the commands above**, because a
read-only grant that changed the writer set is not the act this half signed.

---

## RULING ON THE DEPARTURE: the TARGETED apply is SIGNED

The COO half names one deliberate departure -- `mdpf-pipeline` applied with
`-target=aws_iam_role_policy.mdpf_runner` -- against the decomposition's "`-target` never" bound.

**SIGNED, and the reasoning is that the departure is the NARROWER act, not the looser one.** That root also plans
`aws_s3_object.mdpf_route_bindings`, whose deployed hash (`56a03a14...`) matches **neither** the committed blob
(`650f893a...`, LF) **nor** a Windows CRLF rendering (`f94e8e4c...`). ⛔ **An UNTARGETED apply would upload CRLF bytes
over a LIVE MDPF route-binding object that is outside this act entirely** -- that is the widening, and "`-target`
never" exists to prevent half-landed roots, not to compel collateral writes.

**CONDITIONS ON THE SIGNATURE, both mechanical:**
1. The targeted plan is re-run **immediately before** the apply and must read **exactly 1 to change, 0 to add, 0 to
   destroy**, naming only `aws_iam_role_policy.mdpf_runner`. Anything else is a STOP.
2. **The `mdpf_route_bindings` drift is NOT resolved, absorbed or silently inherited by this act.** It stays a live
   finding (`IRPT_BCKEND-S68`) owned by **this seat as MDPF's owner**, and it is accepted here as such. ⚠ **Whoever
   applies that root UNTARGETED next overwrites a served object** -- that hazard survives this act unchanged and is
   this seat's to close, not `IB-rtc-7`'s.

---

## What this half does NOT sign

- **`G-A`-class acts:** nothing here stops or starts an instance.
- **The destination question:** whether the directory should leave legacy `opal-data-bd` before D14, and whether
  FWD-7's DONE WHEN requires the firm's own bucket. The packet places it and does not decide it; neither does this
  half. `R36-AC2` records the facts for `3.0.0_SA_CVO`.
- **Any second statement, second bucket, or any write grant.** A sixth key is a new packet and a new pair of halves.
- **`IB-rtc-7`'s grading.** This half authorises an act; it does not pre-grade its criteria.

## The sequencing hazard this half inherits and re-states rather than closing

⚠ **Row `IRPT_BCKEND-S65` (ARMED, owner `2.0.0_SA_COO~B`): once this branch merges, ANY apply of either root from a
tree carrying it PERFORMS THIS ACT UNSIGNED** -- and the directory root is the refresh Lambda's own deploy root.
**The mitigation is sequencing, not a gate:** hold such applies, or make `IB-rtc-7` the next one. **This half does not
discharge that row.**

---

**SIGNED:** `1.0.0_SA_CTO`, CTO half, NEVER#1, for `IRPT_BCKEND` `IB-rtc-7`, against packet blob
`bb92a81c697c6d3fb8b01cb65fedfb9cb0563e38`, covering **K1, K2, K3, K4, K5** -- five of five.
