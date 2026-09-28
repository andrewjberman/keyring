# Deploy Completion Record
**Date opened:** 2026-09-28T00:57:46.405341+00:00
**Status:** OPEN
**Deploy:** irpt-status bMMJ/bQ+5 -> rebuild 3 (MINIMAL, CTO 102289): bMMJ members + submission.py 9929a829 + prospect_dates.py e5bae585, and the irpt-status-role original_holdings read grant; halves pending; apply after 05:00Z
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | artifact build + upload + gates | census vs live bMMJ: ONLY submission.py + prospect_dates.py; ~Y zip_module_census 0 unintended winners; cold-start + owner-refusal smoke named; role sim incl. original_holdings; REQ-67 READY | publish: ops/entry.py back to bMMJ's 9da6a1a6 (from 5cec1a3892^) and the staged served.py back to 896680c2de (41fbd6b5); submission.py 9929a829 (pin 5cec1a3892) + prospect_dates.py e5bae585 kept; build-and-upload rc 0; S3 investor-reporting/irpt-status.zip VersionId 7Uz6kDd_FqoCwpEfhUNaPRkx3fsSezxJ sha ZYr+IDMpN0vt..; census vs live bMMJ: 43 -> 43, differ prospect_dates.py + submission.py ONLY. GATE 1: ~Y zip_module_census -- the errors.py/handler.py/resolve.py collisions and the STALE served.py are byte-equal to live bMMJ (untouched); the two new files' first-party imports all resolve in the zip (prospect_dates: owned_requests.{RequestReadRefused,_data_firm,_storage_kwargs}, submission.input_repository_owner; 0 unresolved). GATE 2: ~Y zip_cold_start_smoke with --owner-refusal (window 20's shape): PASS, a named refusal (UNAVAILABLE UNEXPECTED, the bMMJ behavior); NEGATIVE CONTROL 5fSyChId: FAIL TypeError public_line(admitted=). GATE 5: the grant = state/original_holdings for the enabled client firms only (backend commit), plan 0/2/0 (the policy + code); simulator on the planned doc: original_holdings GetObjectVersion OLD deny / NEW allow; other family, lookalike prefix, other firm, PutObject all deny. GATES 3 + 4 (role sim of every window-15 read; REQ-67 READY on the success path) asked of ~Y on the built zip. | CLOSED 20260928T010620Z |
| D1 | activation | ops root safe-apply (code + the grant) | halves at HEAD; live before-read incl. one success read; plan = code + the one grant; readback; cold start; after-read; replan 0 |  | OPEN |
| A1 | verify | K10 | the page reads REQ-67e12718 READY PER_SECTION |  | OPEN |

## Log

- 20260928T005746Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260928T010620Z LEG U1 closed: publish: ops/entry.py back to bMMJ's 9da6a1a6 (from 5cec1a3892^) and the staged served.py back to 896680c2de (41fbd6b5);
- 20260928T0112Z U1 addendum: the grant's first commit was REFUSED by the naming gate (a typed 'state/original_holdings'); re-cut with <tier>/<table> READ from reporting_policies.json family ORIGINAL_HOLDINGS -> backend 75df934b23; re-plan 0/2/0 with the same three resources.
