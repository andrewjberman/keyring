# E1 (CTO rulings batch 88 item 4) read against the live route before any packet -- the status route DOES answer READY

Author `2.0.0_SA_COO~Y`, 2026-10-01 ~14:0xZ. Read-only: two GETs as the service principal, no vendor call. This is
what the enrichment item says and what the route does; the call on E1 is `1.0.0_SA_CTO`'s.

## What E1 says

Batch 88 item 4 (E1): "the status route answers UNAVAILABLE for a READY job (`ops/owned_status.py:23`, the validator's
limit; the page's list row reads 'Checking status...'): fixed first, as its own small packet, because it is a wrong
answer on a live thread".

## What the route does (measured 13:5xZ on served `irpt-status` `2V7xV1+z..`, request `REQ-a69e5751d42c374f1d2354f9`)

| the same GET `status/{jobId}?selected_tenant=cottonwood` | state | reason | operation kind | source dates |
|---|---|---|---|---|
| with NO capability header (this seat's tool, and the validator's read) | UNAVAILABLE | `ANALYSIS_STATUS_DATE_BASIS_UNAVAILABLE` | `analysis_generate` | `{}` |
| with `X-IRPT-Status-Dates: prospect-v1` | **READY** | `ANALYSIS_READY` | `prospect_analysis` | `date_basis` `PER_SECTION` and the retained input's provenance |

## Why there are two answers (read from the code at CLOUD HEAD)

- `ops/entry.py:186-192`: the job-status operation passes `prospect_dates=True` only when the request carries that
  header with that value.
- `ops/owned_status.py:43-58`: for a READY job with the capability, the dates are derived from the retained input and
  the report, and the answer is READY `ANALYSIS_READY`. Without it, line 23's pair is used.
- The reason is the envelope's own rule, not an oversight: a READY answer must carry its dates
  (`ops/tests/test_owned_status.py`, `test_existing_dated_answer_requirement_remains`: `build_envelope(..., "READY",
  None)` is refused). An uploaded prospect portfolio has no custody business date; its dates are the per-section
  basis the capability's extension carries. A client that has not said it can read that extension cannot be handed a
  READY envelope the v1 contract would call invalid, so it is told the date basis is unavailable.

## The page

- The portal declares the capability on this route: `contracts/prospect-dates.ts:3-4` defines the header and value,
  and its own test asserts `irBuildRequest('status-job', ...)` sends `prospect-v1`
  (`__tests__/mvp-selection/prospect-dates.test.tsx:68`, portal 5f30a98d). NOT measured on the wire by this seat.
- "Checking status..." is what a list row prints while its status has NOT YET ANSWERED
  (`tabs/analysis/OwnedRequestHistory.tsx:104`, `row.kind === 'loading'`). A row whose read failed prints "Status
  unavailable" (`:105`); a READY row prints the Ready label. The walk recorded 0 of 17 rows answered at the press,
  and the dialog, which makes its own read, said Ready. So the row is a slow or unanswered read, the same family as
  the 30.2 seconds (E4), not the UNAVAILABLE mapping.

## What this leaves

1. For the page, the route's answer for the READY job is READY. The UNAVAILABLE answer reaches only a caller that
   omits the header: this seat's `job_status_route_read.py` and the validator's read. That is the tools' gap; this
   seat's tool now sends the header on a second status probe.
2. If the ruling is that EVERY caller must be told READY, that is a change to the published status envelope (a READY
   answer with no dates, or the extension sent to a client that did not ask for it): a contract change, not a small
   packet on line 23.
3. The list rows' unanswered state at the press is a page and latency question (17 status reads at once, and how long
   each takes); it belongs with E4.
