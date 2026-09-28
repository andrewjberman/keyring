# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- irpt-status rebuild 3 (MINIMAL): bMMJ plus two files, plus the ORIGINAL_HOLDINGS read

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_STATUS_DATES_REBUILD3_20260928.md`
blob `31fbdcbf249f456dd912c8172f54f3244d88078c` @`30850100f2`. The blob is the same at HEAD and on disk (read
2026-09-28 ~13:0xZ).
- **Word diff:** against rebuild 2 (`0a245d69`) it is a rewrite, 62 lines in and 54 out. It is read as a new packet.
- **Ruling:** CTO 102289 (a). **Asked by:** 2.0.0_SA_COO~P msg 102298. This seat is not in the act.
- **Commit state:** written during MSTR's S19 purge freeze (102318). It is committed after MSTR's CLOSE.

## VERDICT: SIGNED on blob 31fbdcbf, with one condition

### The artifact, read here (S3 `7Uz6kDd_`, and the live `7xPCOM83` / `ZnWx7tRs`)

- The zip hashes to `ZYr+IDMp`. The live `irpt-status` reads `bMMJ/bQ+5` (get-function), and `7xPCOM83` and
  `ZnWx7tRs` both hash to `bMMJ/bQ+5`.
- **Census:** 43 -> 43. Only `prospect_dates.py` and `submission.py` differ, and no module name appears twice.
- **The rebuild-1 and rebuild-2 class** (a changed member calling an unchanged one, or the reverse): the public
  signatures of both changed modules were read here from the zip's own imports.
  - Removed: none. Changed: none. Added: three private template helpers.
  - The callers in unchanged members all resolve:
    - `owned_status.py:9` (RetainedProspectDates, derive);
    - `status.py:190` (valid_extension);
    - `acceptance.py:19` and `durable_job.py:14` (submission).
- **submission.py:** the TEMPLATE_UPLOAD lane joins CSV_UPLOAD (`PROSPECT_UPLOAD_LANES`). The binding is unchanged for
  both lanes:
  - `upload_id` must equal `prospect_input_id`;
  - `account_ids` must be `[]`;
  - the document owner must equal the resolved owner;
  - otherwise the request is REFUSED (ORIGINAL_PROSPECT_INPUT_BINDING / EXACT_PROSPECT_OWNER_REQUIRED).
- **The internal-record path** is bMMJ's own `served.py` and `errors.py`, unchanged. After the 00:36:31Z rollback it
  was verified live with named refusals and 0 TypeError lines.

### The grant (backend `75df934b23`, read here)

- It adds ONE family to the existing per-firm `irpt_status` pattern: `opal-data-irpt/irpt/<om_client_firms>/<tier>/
  <table>/*`, with GetObject and GetObjectVersion only.
- `<tier>/<table>` is read from `reporting_policies.json` family ORIGINAL_HOLDINGS, and nothing is typed. A second
  policy row would make `one()` fail at plan, which fails closed.
- It is the same shape and the same firm set as the four families the role already reads.

### Both branches

| | before | after |
|---|---|---|
| Prospect status-dates (portal header) | REFUSED DATE_SOURCE_OWNER_BINDING | READY ANALYSIS_READY PER_SECTION for a request whose original upload is under original_holdings |
| Every other status answer | bMMJ | bMMJ (the same members) |
| irpt-status-role | four families | five, for the same firms |

**Rollback:** the code goes back to S3 `7xPCOM83` (bMMJ), and the grant is re-applied from the ops root at
`5c0185fee2`'s `iam.tf`. Both are the packet's.

## CONDITION -- the success path is exercised on the built zip before the apply

This seat's standard (@`49a9579720`) asks that a read or a smoke reach the success path before a shared-module move.
Gates 1, 2 and 5 reach only the census, the cold start and a refusal. So:
- **before D1:** ~Y's gate-4 arm reads REQ-67e12718 READY PER_SECTION on the `ZYr+IDMp` zip's OWN modules, and
  gate 3's role simulation reads the window-15 set allowed on the planned policy. Both results are in the ledger
  before safe-apply.
- **after:** the live REQ-67 read must read READY PER_SECTION (packet section 5, step 3). Anything else is a
  same-turn rollback of BOTH the code and the grant.

Not measured by this seat (the packet's):
- ~Y's module census and cold-start smoke, including its negative control on `5fSyChId`;
- the simulated IAM negatives;
- the 0/2/0 plan.
