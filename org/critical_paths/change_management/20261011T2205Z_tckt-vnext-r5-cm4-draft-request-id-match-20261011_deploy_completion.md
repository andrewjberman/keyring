# Deploy Completion Record
**Date opened:** 2026-10-11T22:05:32.590097+00:00
**Status:** OPEN
**Deploy:** TCKT_VNEXT R5-cm-4: opal-ticket-api CODE ONLY at b6fcebb514 (handler b7764fbd) -- the commentary-draft route NARROWS to require the ticket's own recorded request id to match the body. No route or env change; the rollback RE-WIDENS and is taken only on a failed apply
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | both halves read, the packet hashed, the union, STOP 1 and every BEFORE read | the CTO half @15b0cd9a3f read in full and the packet @675c87aa34 read whole with its sha256 verified against the 59945de9a7ee069e value the half names over 88 lines, so the text I read is the text that was signed; the open-deploy union at one fresh instant with the per-tree denominator printed and any opal-ticket-api entry but my own a STOP; STOP 1 git diff --name-only b6fcebb514 HEAD over the handler AND THE WHOLE terraform folder (not just main.tf, as this order words it) EMPTY, against a printed control; and the BEFORE reads -- live CodeSha256 e1ZHjf21 (my own R5-ml-2 apply) with the deployed handler 7113a749 by a package DOWNLOAD and anything else a STOP before any plan; 9 env key names with a sha256 of EACH value and no value printed; THE TICKET ROUTE CENSUS as the order now makes it the proof rather than a 401 -- 11 route keys listed, each CUSTOM behind the portal authorizer, which is this order adopting my own R5-ml-2 finding that a 401 cannot distinguish an absent route from a guarded one; opal-tickets ItemCount; and the control ticket's status fields with whether it carries draft_commentary or commentary_sent |  | OPEN |
| L1 | activation | build and upload at the pin, then ONE plan and ONE safe-apply, CODE ONLY | the built zip's lambda_function.py hashes b7764fbd63a6b59a79c5d95b2e22bb329fccd13d54d1c0c8da08e2041f5673ef or it is a STOP before any plan, proven by a BUILD_ONLY pass before anything is uploaded and by re-downloading the uploaded object; the plan is 0 to add, 1 to change, 0 to destroy with source_code_hash the ONLY field moving -- ANY route change or ANY env diff is a STOP with nothing applied, read from the planfile JSON rather than the rendered diff; safe-apply without MSYS_NO_PATHCONV |  | OPEN |
| L2 | verify | the after-reads, with the census carrying the existence claim | (a) CodeSha256 equal to the uploaded zip and the deployed handler re-downloaded reading b7764fbd; (b) the env UNCHANGED, 9 names and all 9 values hashing exactly as before, since this order changes no env; (c) THE TICKET ROUTE CENSUS UNCHANGED -- the same 11 keys behind the same authorizer, which is the proof the routes stand and is deliberately NOT a 401; (d) ItemCount unchanged and the control ticket byte-identical with no commentary_sent appearing; (e) the replan 0-diff |  | OPEN |
| L3 | verify | RECORD, and STOP 3 | record-terraform-deploy.sh for opal-ticket-api with its pipeline positional; the map entry's artifact_sha256 equal to the live CodeSha256 read after the commit, the stamped commit's handler hashed against the DEPLOYED file beside a positive control on the prior build, and both halves of the record in ONE commit -- a half-landed record is reported, never hand-edited |  | OPEN |
| L4 | verify | AC1 as a REGRESSION read, the second line if it exists, and what stays UNEXERCISED | clamp_precheck.py --out the order's r5_cm4 path with its totals line(s) printed AS THEY READ; READ27 27/27 is explicitly a regression read of the FROZEN 27 routes and is NOT claimed as coverage of the commentary routes -- the order and the CTO half both now say so, citing my row D2-S45; if the precheck prints a second line TICKET_HANDLERS n/m I print it too and report any UNCLASSED handler FIRST; and the statement that the route's admission, the request-id MATCH, every arm of its four-case deny and both 409s are UNEXERCISED, because nobody calls the route today -- the drafter still creates a new ticket, I mint no identity and call the route with none |  | OPEN |

## Log

- 20261011T220532Z OPENED by 0.7.0_AE_CloudOps~TV2 with 5 leg(s)
