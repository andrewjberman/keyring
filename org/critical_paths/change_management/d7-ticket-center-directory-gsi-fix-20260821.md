# DEPLOY-COMPLETION LEDGER — ticket-center claim-enrichment directory fix (email-index GSI)

**Opened:** 2026-08-21T20:34Z by `0.5.0_AE_OpalETL~Z` (deploy-START; NEVER#6)
**Status:** **CLOSED 2026-08-21T20:52Z** — applied (0 added / 2 changed / 0 destroyed), 0-diff
confirmed, IAM verified on the live primitive with both controls, deployed bytes == build input,
and **the EXERCISED rung passed: the claim resolved a real directory name.** All 9 legs closed;
nothing stranded.

**GO:** Andrew-direct ~2032Z at this terminal, VERBATIM: *"recs approved"* — closing `/open-calls`
CALL 1 (REC (a): apply now, run it here per Rule 26, spend the authorised test ticket in the same
act). The call was carried to him by `1.0.0_SA_CTO~Z` at 1953Z after that seat ruled BUILD-NOT-APPLY.

**SCOPE, stated narrowly — anything outside this is not covered by his word:**
the ticket-center directory fix ONLY — the `email-index` GSI code change in `lambda_function.py`
**and** the one `dynamodb:Query` grant on that index ARN. Nothing else.

**Applying seat / device:** `0.5.0_AE_OpalETL~Z` on **site Z**, per **Rule 26** (the apply runs on
the device that owns the work; no ferry).

## Why this deploy exists

`_directory_snapshot` resolved a claimer by **constructing** `PK = "USER#" + email`. Measured over
the whole live table, token-walked: **48 PROFILE rows — 31 email-form, 17 opaque `USER#usr_<hex>` —
and those 17 include 15 of the 20 opal-capital principals.** Every real Opal human who claims a
ticket missed, rendering as `"An Opal advisor"`. Deployed lookup for `andrew@opalinvest.com`
returned **NO ITEM**.

## State pinned at deploy-start

```
HEAD                     481dde1dbf   2026-08-21T20:29:52Z
handler last touched     a8274406d4   the GSI fix commit
working tree             CLEAN for infra/aws/lambda/ticket_center/ and infra/aws/terraform/ticket-center/
source lambda_function.py  62,729 B   sha256 54fa63d59537d71badee62ad35fe3342c75393dc1a6cc79fbe22e3c8424d34a3
fix tokens present       USERS_EMAIL_INDEX=3  email-index=2  IndexName=3  ENRICHMENT-AMBIGUOUS=1
non-ascii bytes          0
PRIOR deployed artifact  sha256(b64) fA1rsLL6Y+TZaiPAwEzs8WnqxJjuorrB1j3YqkFm0js=  @ 8c1f26d84b
```

## Acceptance bar — stated IN ADVANCE by `1.0.0_SA_CTO~Z` (msg 4760, 2029Z)

> **THE TEST TICKET MUST DEMONSTRATE THE ENRICHMENT RESOLVES A REAL NAME.** Not that the apply
> succeeded. Not that the GSI query returns rows in isolation. The claim path, end to end, producing
> an actual human name where it previously produced "An Opal advisor".

**DESIRED and APPLIED are necessary and NOT the acceptance.** Three seats closed DESIRED+APPLIED on
W-A and the feature was broken for every real principal anyway. **One ticket, one claim, one name —
do not pad the exercise.**

## Legs

| # | Leg | Status |
|---|---|---|
| 1 | build + upload `ticket-center/opal-ticket-api.zip` with `content-sha256` metadata | **CLOSED** — 21,915 B, `/38KUtP9qHaUJMJi55+bSk7X6qBgtfkbH+iOK9ajVSA=`, zip round-trip asserted identical to source |
| 2 | `head-object` verify the upload (never trust a `cp` exit alone) | **CLOSED** — ContentLength 21,915 + metadata match exactly |
| 3 | apply through `.tools/safe-apply.sh` (never bare; `SAFE_APPLY_TERRAFORM` knob) | **CLOSED** — `Apply complete! 0 added, 2 changed, 0 destroyed` |
| 4 | 0-diff re-plan | **CLOSED** — `-detailed-exitcode` rc=**0** (no changes), not eyeballed |
| 5 | IAM verified on the LIVE primitive, one `--resource-arns` per call, separate positive control | **CLOSED** — see matrix below |
| 6 | deployed package bytes verified against the build input (source map), NOT by filename | **CLOSED** — member sha `54fa63d5…` == source, `CodeSha256` matches |
| 7 | **EXERCISED: one test ticket, claimed, RESOLVES A REAL HUMAN NAME** | **CLOSED — PASS** |
| 8 | source map updated | **CLOSED** — 4/4 lines, mojibake preserved 51→51, re-parses VALID |
| 9 | ledger closed in-session | **CLOSED** |

## Leg 5 — IAM, three SEPARATE invocations (Rule 22a's false-deny modes)

```
TARGET    Query   .../opal-users-v2/index/email-index          -> allowed
POSITIVE  GetItem .../opal-users-v2                            -> allowed   (so a deny is real)
NEGATIVE  Query   .../opal-users-v2/index/zzz-no-such-index-9999 -> implicitDeny
```
The negative control is a **sibling index on the same table**, so it proves two things at once: the
instrument can say no, and **the grant is pinned to `email-index` rather than table-wide.**

## Leg 7 — THE ACCEPTANCE, and why it could have failed

`1.0.0_SA_CTO~Z`'s bar (msg 4760): *the claim path, end to end, producing an actual human name.*

⛔ **THE TRAP I NEARLY WALKED INTO.** `lambda_function.py:329` seeds the snapshot from the ACTOR:
`snap = {"name": actor.get("name") or "", ...}`. **Passing the claimer's real name in the authorizer
context would have made `claimed_by.name` correct EVEN IF THE GSI QUERY NEVER RAN** — a test that
cannot fail, which is exactly the family this whole defect belongs to. So the claim carried a
**sentinel** name that the directory had to destroy.

```
ticket            TCK-20260821-0d2a2024
requester         andrew@opalinvest.com   (actor; requester_email NOT supplied -> self-directed)
claimer           michael@opalinvest.com  PK USER#usr_7aa8bf335ca5 -- OPAQUE, the defect shape
authorizer name   "ZZZ-AUTHORIZER-SEED-MUST-BE-OVERWRITTEN"   <- the sentinel

claimed_by.name    = "Michael (Dev Harness)"     SENTINEL DESTROYED -> came from the directory
claimed_by.user_id = "USER#usr_7aa8bf335ca5"     THE OPAQUE PK
```

**`user_id` is the decisive evidence, not the name.** The old code constructed
`USER#michael@opalinvest.com`; it could not have produced `USER#usr_7aa8bf335ca5` by any path. The
opaque PK on the row is positive proof the GSI leg executed.

Log tokens: `WE_CLIENT_SENT kind=pickup … from=tickets@opalinvest.dev` (one email, to the requester,
NEVER#23-compliant sender) · `WE_DL_UNCONFIGURED` on create (the deliberate blank-map refusal, no
fallback address) · **zero** `ENRICHMENT-*` degradations, **zero** `WE_CLIENT_NAME_DEGRADED`.

**BOUND, stated rather than glossed:** invocation was a direct `lambda:Invoke` with a synthesized
authorizer context, so **the API Gateway custom authorizer itself was NOT exercised.** Everything
downstream of it was — routing, `authorize`, SoD, the GSI query, the DynamoDB write, and the SES
send. The authorizer was not what was under test.

## Rollback

Same-window: re-upload the prior artifact (recoverable exactly —
`git show 8c1f26d84b:infra/aws/lambda/ticket_center/lambda_function.py`, prior deployed package
sha256(b64) `fA1rsLL6Y+TZaiPAwEzs8WnqxJjuorrB1j3YqkFm0js=`) and re-apply; then remove the IAM
statement. **The IAM grant is additive and reverts cleanly.** No data migration in this deploy — the
fix changes how a row is FOUND, never what is written.

⚠ **The one test ticket DOES write a production row.** That write is authorised (Andrew ~1935Z,
CALL 6) and is not rolled back by the code rollback; it is a real internal self-addressed ticket.

## SURPRISE ITEM — filed against my own fix. class BLOCKING x standing ARMED. NOT remediated.

**`_directory_snapshot`'s DOCSTRING HEADER (`lambda_function.py:310-322`) STILL ASSERTS THE FALSE
RULE THAT CAUSED THIS DEFECT.** I corrected the mechanism in inline comments below it and left the
header standing:

> *"KEY SHAPE IS MEASURED, NOT ASSUMED (2026-08-20, live describe-table + a bounded 3-item sample):
> … PK = "USER#<email>" …"* — **false: 31 of 48.**
> *"PK is a deterministic function of email, so user_id carries no information the email does not
> already carry; whether the field earns its place is a schema call"* — **also now false.**

⛔ **THE SECOND SENTENCE IS THE ARMED ONE, AND IT IS A DELETION WARRANT.** It tells a future
engineer that `user_id` is redundant with `email` — and **tonight's exercise just measured the
opposite**: `user_id` came back `USER#usr_7aa8bf335ca5`, which is **not derivable from
`michael@opalinvest.com` by any function.** A least-privilege or schema-slimming pass reading that
docstring would drop a field that now carries real information. Same class CLAUDE.md names for
comp-iam: *never read an instrument's silence as a deletion warrant* — here the instrument is a
docstring, and it is not silent, it is confidently wrong.

**WHY IT IS NOT FIXED IN THIS DEPLOY, stated rather than quietly deferred:** editing the file now
would make deployed bytes != tree and break the leg-6 invariant I just verified, and a second apply
would widen ONE approval into two. Andrew approved the directory fix and the grant; I am not
converting that into a standing licence to re-apply.
**Disarm owner: `1.0.0_SA_CTO~Z`** — a comment-only micro-deploy tonight, or ride the next touch of
this file. **DISARMED != REMEDIATED: nothing is disarmed yet.** The hazard is live in the deployed
docstring as of this close.

*Root symmetry worth naming: the original defect was a false certainty in this same docstring. The
fix corrected the code and left the false certainty in place — an inch above the correction.*
