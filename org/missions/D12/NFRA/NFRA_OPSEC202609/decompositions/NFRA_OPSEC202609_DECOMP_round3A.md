# NFRA_OPSEC202609 -- DECOMPOSITION, ISSUANCE 3A (the deferred opening order)

**Cut by** `2.0.0_SA_COO~Z` 2026-09-10 ~15:4xZ. **v0.1.0.**
**This is NOT an amendment to round 3's rectangle** (`NFRA_OPSEC202609_DECOMP_round3.md`, cells `OP3-s-1`,
`OP3-s-2`, `OP3-s-3`), which is FROZEN, executed and at L10. **It is a separate, standalone issuance**, so
round 3's L8 packet assertion (3 cells / 20 criteria) is not falsified.

## Why this exists, stated plainly because it is a defect record

This work was **Andrew-authorised** at `@9382d107a3` s.1 -- *"The 2 in-lane liveness Lambdas need no word
and can cut now"* -- and **ruled by `1.0.0_SA_CTO~Z` at msg 20769** in its own subject line: *"cut the two
liveness Lambdas as ROUND 3's OPENING order, do NOT amend the frozen decomp."* This seat then wrote it into
`project.json` `blocking` as binding constraint (2), **and cut round 3 without it.** Recorded as row
`Z-S174` @`09c10ed9a5`.

⛔ **THE PERMISSION BARRIER IS NOT OPEN AND IS NOT BEING RE-ASKED.** Msg 20769: *"the permission barrier is
still removed. No word is needed and none will be asked for again."* The only barrier ever raised was
MECHANICAL -- the CVO was mid-adjudication on a packet asserting 31 of 31 terminal -- **and it expired when
round 2 closed.**

## THE RECTANGLE -- one cell

| cell | serves | target state | one line |
|---|---|---|---|
| `OP3A-s-1` | FWD-12 | **EXERCISED** | the two IN-LANE liveness callers stop presenting a static bearer and obtain their credential through the gateway's exchange endpoint |

**ONE cell, not two, and the reason is a write-surface dependency rather than convenience:** both Lambdas
are declared in `infra/aws/terraform/opal-gateway/`, they are the same change on two instances, and two
cells would put two workers on one directory. `2.0.0_SA_COO~ZI` hit exactly that on `NFRA_IAMROLES202609`
today (*"three cells were scheduled onto ONE document -- a WRITE-SURFACE dependency the edge set did not
model"*), and this cut takes that lesson rather than re-learning it.

**Fan-out: 1 of 1 chains, cap 8.** No dependency edges: the cell has no predecessor in this issuance.

## GROUNDING -- read from source at HEAD, not from the ruling's prose

| caller | declared at | probe URL | credential TODAY |
|---|---|---|---|
| `opal-otp-liveness` | `infra/aws/terraform/opal-gateway/otp-liveness.tf:83-84` | `https://mcp.opalinvest.dev/otp/health` | `OTP_BEARER_SECRET_ID = "blackdiamond/49f/otp-gateway-token"` |
| `opal-ms-ingest-liveness` | `infra/aws/terraform/opal-gateway/ms-ingest.tf:86-87` | `https://mcp.opalinvest.dev/ms/health` | `MS_INGEST_BEARER_SECRET_ID = "opal/mcp/ms-ingest-token"` |

Both are stdlib-only (`urllib` + `boto3`, `archive_file` zip, no layer) and both fire on a 6h EventBridge
rule (`opal-otp-liveness-6h`, `opal-ms-ingest-liveness-6h`, both `state = "ENABLED"`).

**These are callers 3 and 5 of the 5 holdings across the three secrets; 1, 2 and 4 are CROSS-LANE
(OpalETL, PartnerETL, CloudComp) and are OUT OF SCOPE HERE** -- Andrew's ruling routes those *through the
owning lanes* and says in terms it *"does NOT move the three callers into OPSEC's territory; PRD s.3's
boundary stands."*

## WHAT MAKES THIS SAFE TO CUT, measured and unretracted

⭐ **DUAL-ACCEPT IS INTACT AND PROVEN:** the static bearer returned 200 on `/otp/fetch` on 3 of 3 reads at
19:22:33/34/36Z while no-auth and junk-auth both returned 401. **Migrating a caller breaks nothing and
retires nothing.** The exchange endpoint `/otp/token` (`class=exchange`) has been reachable through the ALB
since **2026-09-09T19:14Z**; before that it answered a Microsoft OIDC 302 to everything, so no caller could
have migrated even in principle.

⚠ **THAT MEASUREMENT IS FROM THE PREVIOUS EVENING AND IS THE CELL'S OWN FIRST ACT TO RE-GROUND.** A premise
older than a day is exactly what produced `OP3-s-3`'s stale cut. **The order's preflight re-takes it.**

## FOUR-POSTULATE RECORD (rule 24)

- **MECE over the declared domain** -- the domain is *the IN-LANE half of FWD-12's caller migration*, which
  is exactly callers 3 and 5. The uncovered members (1, 2, 4) are named above and are another lane's by
  Andrew's own ruling, not by omission.
- **SAME GRAIN** -- one cell, one write surface, one credential-exchange change, two instances of it.
- **INTENT COHERENCE** -- one axis: how a caller obtains its credential. It does not touch what the
  callers probe, their schedule, or their alerting.
- **STATE COHERENCE** -- the remedy moves `DESIRED -> EXERCISED` for the in-lane half only. It does **not**
  move the cross-lane half, and it does **not** retire the static bearer (dual-accept stays intact; retiring
  is a later, separate decision once all five have migrated).
