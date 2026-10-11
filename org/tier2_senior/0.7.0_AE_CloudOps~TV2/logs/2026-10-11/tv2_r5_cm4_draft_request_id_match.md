# A draft lands only on the ticket whose own record names that request — 0.7.0_AE_CloudOps~TV2

**archetype:** DEPLOY

**Date:** 2026-10-11
**Task Order:** TCKT_VNEXT.TO-APPLY-R5-cm4.draft-request-id-match-code-dell2 (read at `348eb5b41f`)
**Status:** COMPLETE — branch A, 5 of 5 legs, AC1 `READ27 27/27` **and** `TICKET_HANDLERS 11/11`, 0 UNCLASSED

---

## Objective

Deploy `opal-ticket-api` at pin `b6fcebb514` (handler `b7764fbd`), **code only**. The commentary-draft route
**narrows**: it accepts a draft only where the ticket's own recorded `report_ref.request_id` equals the
request id in the body. One deny now covers four cases with one status and body.

**It widens nothing**, and the rollback *does* — so the rollback is available only on a failed apply.

---

## Two of my own findings came back in this order

| my finding | where it landed |
|---|---|
| a 401 cannot prove a route exists (R5-ml-2) | the order and the packet (citing msg 5910) replace the 401 after-read with the **route census**, before and after |
| row `D2-S45`: the precheck's 27 is a frozen set, silent about the commentary routes | AC1 is reframed as a **regression read** of those 27, explicitly not coverage; and step 7 asks for a second line if it exists |

**The remedy had already landed.** The precheck in this tree now prints
`TICKET_HANDLERS 11/11` with a class per handler and **zero UNCLASSED** — `commentary_draft_ticket` as
`ENV_FIRM_LIST`, `commentary_sent_ticket` as `PROFILE_SCOPE`, exactly the two classes the CTO half's own code
read predicted. The gap my row recorded is closed by measurement, in the tree, rather than owed to a later
round.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open` (5 legs) + 5× `close-leg` + `close` | PASS | union: 69 trees, 1 open entry (mine) |
| sha256 over the packet | whole, 88 lines | PASS | `59945de9…` exact — text read == text signed |
| build-and-upload.sh | `BUILD_ONLY=1`, then real | PASS | identical member hash; object re-downloaded |
| terraform show -json | the saved planfile | PASS | **read for absences**: 0 routes, 0 env keys |
| aws apigatewayv2 get-routes | census before **and** after, as key **sets** | PASS | 11 = 11, identical, all `CUSTOM`/`naqxlm` |
| safe-apply.sh | `apply <planfile>`, no `MSYS_NO_PATHCONV` | PASS | 0 add / 1 change / 0 destroy |
| record-terraform-deploy.sh | `ticket-center --function …` | PASS | both halves one commit |
| clamp_precheck.py | `--out …/r5_cm4/…` | PASS | two totals lines; 0 UNCLASSED |

**What worked:** reading the plan for **absences**. This order's STOPs are about what must *not* appear — any
route change, any env diff — so the useful assertions were `0 aws_apigatewayv2_route resources` and
`0 env keys changing`, not a count of what did.

**What failed:** nothing in this order. The MSYS `/tmp` path for the built zip was resolved with `pwd -W` up
front, having cost a `FileNotFoundError` in the preceding order.

**Gap found:** none new.

---

## Verification

```
STOP 1  0 changed paths vs b6fcebb514 over the handler AND the whole terraform FOLDER
        (this order widens the pathspec from main.tf to the directory; run as worded)
        control: 59 paths changed over the same range

BEFORE  live e1ZHjf21 (21:27:13Z, my own R5-ml-2 build); deployed handler 7113a749 by download
        env 9 keys as length + sha256
        ROUTE CENSUS: 121 routes on the API, 11 ticket routes, all CUSTOM/naqxlm, keys recorded
        ItemCount 27 / 34549; control ticket 23 attrs, report_ref.request_id test-f10-20261009-one

PLAN    0 to add, 1 to change, 0 to destroy
        0 route resources | env 9 -> 9, 0 keys changing
        source_code_hash e1ZHjf21 -> Ob/MZBEO ; s3_object_version rB1mwXIO -> UrpJF5gv

AFTER   (a) CodeSha256 Ob/MZBEO… == the zip; deployed member b7764fbd by fresh download
        (b) env 9 names, 9 of 9 values hash-identical -> untouched
        (c) ROUTE CENSUS unchanged: 11 routes, key SETS identical, all CUSTOM/naqxlm,
            both commentary routes present   <- the existence proof, deliberately not a 401
        (d) ItemCount 27 / 34549; control ticket sha256 80ea57fceb215b73 == before
        (e) No changes. Your infrastructure matches the configuration.

RECORD  50b35c6940 -- map (3/3) and CHANGELOG (42) in ONE commit; artifact_sha256 == live
        stamped 220e5ef457's handler == b7764fbd == the deployed file
        control: the prior build 33d165b4ef hashes 7113a749 (different) -> the match discriminates

AC1     READ27 27/27      opal-ticket-api 22:16:38 b7764fbd CLAMPED
        TICKET_HANDLERS 11/11     UNCLASSED: none
          PROFILE_SCOPE        create_ticket, list_tickets, metrics, get_ticket, claim_ticket,
                               complete_ticket, report_ticket, commentary_sent_ticket
          SUBMIT_CONTEXT_FIRM  submit_form
          ENV_FIRM_LIST        package_ticket, commentary_draft_ticket
```

---

## Decisions Made

1. **Reported the second totals line, and reported "0 UNCLASSED" first**, as the order asks. The classes are
   the substance: they are what my row `S45` said the instrument could not see.
2. **Did not fold the second line into AC1.** The criterion names only `READ27`; it matched its own pattern,
   and `TICKET_HANDLERS` stands beside it rather than being claimed as part of it.
3. **Kept the route census as sets, not counts.** `11 == 11` would pass if a route were swapped; comparing key
   sets is what catches a substitution.
4. **Ran STOP 1 over the whole terraform folder**, since this order widens the pathspec from `main.tf` to the
   directory — a narrower read would have been the order's words, not its intent.
5. **Recorded the rollback's restriction even though the apply succeeded.** Re-applying `33d165b4ef`
   re-widens `svc-commentary`; a later reader seeing only a prior build in the map's history should not
   mistake it for an available remedy.
6. **Noted the CTO half correcting its own earlier sentence** — its ruling had called the recorded request id
   "a fact only the ticket's creator can write", and the assignee may record over it. The route does not ask
   who recorded it, which is the behaviour as built and signed.

---

## Files Modified

| File | Commit |
|------|--------|
| source map + `CHANGELOG.json` | `50b35c6940` (by the recorder) |
| ledger + row, proof_of_spec, AC1 table, this log, TO status | this commit |

No Terraform edit — this order carries none.

---

## Blockers

None owed by this seat. **Carried, not mine:** row `S40` (`2.0.0_SA_COO~Y2`); rows `S43` and `S45`'s
dispositions (`1.0.0_SA_CTO~DELL2`, with `S45`'s remedy now measurable in the tree).

---

## Current State

`opal-ticket-api` runs `b7764fbd`. The commentary-draft route now requires the ticket's own recorded request
id to match the body; `svc-commentary` can set a draft only where the ticket already names the request the
draft is for. **The route's admission, the match, every arm of its four-case deny, its two 400s and both 409s
are UNEXERCISED** — nobody calls the route, the drafter still creates a new ticket, I minted no identity and
wrote to no ticket. The narrowing has refused nothing because nothing has asked it to.

FWD-6 remains built in the service and not live end to end.

---

## Next Steps

1. `2.0.0_SA_COO~T2`'s route switch for the drafter — the CTO half says it may be cut once this apply is
   reported, which it now is. That switch is what first exercises the admission and the match.
2. A portal cell surfaces `commentary_sent`; only then is FWD-6's second clause live on the page.
