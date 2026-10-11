# Deploy Completion Record
**Date opened:** 2026-10-11T17:53:54.016338+00:00
**Status:** OPEN
**Deploy:** TCKT_VNEXT R4-pk-3: ENV ONLY -- PACKAGE_ALLOWED_FIRMS from EMPTY to 49financial,cottonwood,inflection on opal-ticket-api, the THIRD write of IRPT_ANLREQ's packager-mint pair; the artifact must NOT move
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | both halves read at their pins, the union, STOP 1 and every BEFORE read | the corrected CTO half @7b039a456b read in full (it REPLACES @65622fbcdc) and the packet read with its blob verified as 5a202040cd, the bytes the CTO hashed; the open-deploy union at one fresh instant with the per-tree denominator printed and the fifth run's own entry named as expected-open; STOP 1 git diff --name-only e9357d6ea0 HEAD over the handler and main.tf EMPTY before my own edit, against a printed control; and the BEFORE reads -- live CodeSha256 d2w1YJ8A, the deployed lambda_function.py sha256 c40036677aae180cb362f89f2c2aecb62ef53fd0b1a285bb3bd2c813176c1026 from a package DOWNLOAD and not a filename, 9 env key names with a sha256 of EACH value and no value printed, PACKAGE_ALLOWED_FIRMS length 0, opal-tickets ItemCount, and the status fields of TCK-20261009-a1052909. A live handler that is not c4003667 is a STOP before any plan |  | OPEN |
| L1 | git | the ONE edit to main.tf, committed alone | git show --numstat proves ONE file and the value plus its comment only; the comment cites the CORRECTED CTO half @7b039a456b and says why it supersedes the @65622fbcdc the order's step 3 names, never ALL (the handler drops it); pure ASCII added to a file that already carries non-ASCII, none stripped |  | OPEN |
| L2 | activation | ONE plan and ONE safe-apply, env only | the plan is 0 to add, 1 to change, 0 to destroy on exactly one resource and exactly one env key; A source_code_hash CHANGE IN THE PLAN IS A STOP because the artifact must stay the one already live; the planfile read as JSON for the key's rendered value, as I did for pk2 where a rendered null was not the applied value; no MSYS_NO_PATHCONV on safe-apply |  | OPEN |
| L3 | verify | the five after-reads (a) to (e) | (a) CodeSha256 UNCHANGED at d2w1YJ8A and the deployed handler still c4003667 by a fresh download, which is the read that proves an env-only apply did not move code; (b) 9 env key names, the EIGHT other values hashing identically to their before-hashes, and PACKAGE_ALLOWED_FIRMS reading exactly 49financial,cottonwood,inflection -- firm ids are not client data so the value is printed; (c) an unauthenticated POST to the package door refused 401, which proves reachability and only that; (d) ItemCount unchanged and TCK-20261009-a1052909's status fields identical to step 2; (e) the replan 0-diff |  | OPEN |
| L4 | verify | RECORD, and STOP 3 | record-terraform-deploy.sh run for opal-ticket-api; if it refuses or records nothing BECAUSE THE ARTIFACT DID NOT CHANGE I say so plainly and do NOT force it, and a half-landed record is reported, never hand-edited |  | OPEN |
| L5 | verify | AC1 on the unchanged build, and what stays UNEXERCISED | clamp_precheck.py --out the order's r4_pk3 path reads READ27 27/27 with the ticket host CLAMPED on c4003667; and the statement that the door's admission and its five coded 409s read APPLIED, UNEXERCISED -- no identity is bound to the resident, I hold no token, and I do not call the door with any identity |  | OPEN |

## Log

- 20261011T175354Z OPENED by 0.7.0_AE_CloudOps~TV2 with 6 leg(s)
