# WINDOW 22, part Y -- leg Y proof and the per-body route record

**Walker:** `2.0.0_SA_COO~Y` (respawned 13:4xZ after a crash; brief
`org/tier1_exec/1.0.0_SA_CTO/deliverables/RESPAWN_BRIEF_COO_Y_20260929_134xZ.md` @056220d0aa).
**Authority:** W22 packet blob `1f3bf0914f` (@6550c62cdf); halves CTO `3b209c072c`, CRO `af1940e31d`;
ledger `irpt-ui-walk-principal-w22-20260929` (@062c9e8dea); ~P 102810.
**Tools:** `live_chain.py` @78c8ce05a6 with `WALK_PW_RETAINED=1`; `case_trace.py` @f86dc994b9; `job_watch.py`;
`resident_journal.py` (SSM, read-only).
**Principal:** `irpt-uiwalk-1790687432@opal.test` (K1 `USER#usr_irptuiwalk_1790687432`, created 13:10:37Z).
**Cap:** 15:10:37Z. **Submissions used: 5 of 5.** One login, one K4 and at most one K5 per body. No retry, no replay.

## Per-body route record

| # | body | firm | K4 upload_id | normalization | K5 | REQ | terminal state |
|---|---|---|---|---|---|---|---|
| Y1 | Comparison `opal_long_term`, CSV | cottonwood | `UP-bf609d33..` | NORMALIZED, 1 s | 200 QUEUED | `REQ-7ea49c2d9b27957d0ea8888f` | **job READY**, report `RPT-2e21b52edcb222205399100e026c2768` |
| Y2 | Multi-Comp `opal_short_term`,`opal_intermediate_term`, CSV | cottonwood | `UP-299bf8b1..` | **NEEDS_CORRECTION** `RESOLVE_RETRY_EXHAUSTED`, 203 s | not made (packet branch) | -- | **ATTENTION `RESOLVE_RETRY_EXHAUSTED`** |
| Y3 | Target Weight, notional 1000, XLSX | cottonwood | `UP-25f68c51..` | NORMALIZED, <1 s | 200 QUEUED | `REQ-51f1413b9d84d26a66aaa71c` | see below |
| Y4 | Overview, CSV | 49financial | `UP-10273a2b..` | **NEEDS_CORRECTION** `RESOLVE_RETRY_EXHAUSTED`, 183 s | not made (packet branch) | -- | **ATTENTION `RESOLVE_RETRY_EXHAUSTED`** |
| Y5 | Overview, CSV | inflection | `UP-d43552d8..` | **NEEDS_CORRECTION** `RESOLVE_RETRY_EXHAUSTED`, 182 s | not made (packet branch) | -- | **ATTENTION `RESOLVE_RETRY_EXHAUSTED`** |

Every state above is read from `irpt-requests` by consistent Query on the `NORMALIZATION#<upload_id>` prefix, not
from the walker's own POST response. Y2's K4 was made by the pre-crash session at 13:14:56Z; it was NOT replayed.

## The `IRPT_RESIDENT_RESOLVE` lines (SSM, read-only, i-0167fd745ad906a66)

`journalctl -u irpt-analysis-resident.service --since '2026-09-29 13:10:00 UTC'` -- 169 lines total, service `active`:

```
13:14:46  state=READY     code=-                          <- Y1
13:15:20  state=RETRY     code=PROVIDER_READ_UNAVAILABLE   \
13:16:20  state=RETRY     code=PROVIDER_READ_UNAVAILABLE    |  Y2
13:17:21  state=RETRY     code=PROVIDER_READ_UNAVAILABLE    |
13:18:21  state=ATTENTION code=RESOLVE_RETRY_EXHAUSTED     /
13:59:43  state=READY     code=-                          <- Y3
14:01:23  state=RETRY     code=PROVIDER_READ_UNAVAILABLE   \
14:01:39  state=RETRY     code=PROVIDER_READ_UNAVAILABLE    |  Y4 + Y5
14:02:24  state=RETRY     code=PROVIDER_READ_UNAVAILABLE    |
14:02:39  state=RETRY     code=PROVIDER_READ_UNAVAILABLE   /
```

No `Traceback` appears in the span (the grep alternation included it and matched none). 0 restarts.

## S194 -- disarmed. Read on Y1.

`case_trace.py cottonwood REQ-7ea49c2d9b27957d0ea8888f`: **22 links, 20 MATCH, 0 MISMATCH, 2 NOT_EVALUATED**
(`screen` is ~D's K10 walk, `export` is window 16 -- neither is this tool's to stand in for). The two links S194 is
about:

- `request` -- *the variant is the recipe's for the comparison count, and every recipe source names one template*:
  `{"keys": ["opal_long_term"], "variant": "COMPARISON", "template_id": ["14141824"]}`
- `pdf` -- *of the catalogue's portfolios, the PDF prints exactly the chosen comparisons*:
  `{"printed": {"Opal Long-Term": [2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 16, 18, 19, 22, 23]}}`

The Comparison sent its model and the retained PDF prints it, on 16 pages. `COMPARISON_NOT_PRINTED` did not fire.
Supporting links in the same trace: the retained PDF hashes to its checkpoint (`7f8ed86e548bc6be`, 827,312 bytes,
retrieved 13:31:07Z); its settings table prints THIS job's portfolio name
(`IRPT REQ-7ea49c2d9b27957d0ea8888f r1 3f4a32561f5c`); the served foreign-firm name check passes the PDF for its own
firm (`{"foreign": []}`); and every scalar section re-reads at its own page and coordinates (`72/72`, 0 misses).
Full trace: `CASE_TRACE_Y1_REQ-7ea49c2d.json` / `.txt`.

## S193 -- read LIVE, on Y2 (CTO condition 1), and again on Y4 and Y5.

The NEEDS_CORRECTION row itself, read by consistent Query (not inferred from the ATTENTION line):

```
tenant            cottonwood
request_revision  NORMALIZATION#UP-299bf8b1..#21d47c44de4c5caade3b879a6520826391bbf5579cf199fdbd13e4176ed05721
state             NEEDS_CORRECTION
reason            RESOLVE_RETRY_EXHAUSTED
findings_total    1
findings          [{code: RESOLVE_RETRY_EXHAUSTED, severity: ERROR, row/column/sheet/value: NULL,
                    actions: [REPLACE_FILE]}]
dispatched_at     1790687698    resolved_at 1790687901   (203 s)
```

The bound fires as specified: four receives, then the row moves to NEEDS_CORRECTION with the code. Y4 and Y5 carry
the identical shape (`reason RESOLVE_RETRY_EXHAUSTED`, one ERROR finding, `actions: [REPLACE_FILE]`), at 183 s and
182 s. **S193 is read and passes.**

What the bound is bounding is a separate question, filed as a row and not adjudicated here --
**`IRPT_BCKEND-S206` @befabb9a7b**: across the window's denominator of 5, `PROVIDER_READ_UNAVAILABLE` tracks whether
another resolve was in flight, not the file. Y1 and Y2 carry the SAME upload bytes
(`bb079cbf53aaa2be7ce3fb6beb44e55eaeb0695cd168661d5fb78488a0960ddc`) 14 s apart and resolved 1 s vs 203 s; both READY
lines are the first resolve after an idle gap; Y4 and Y5 were dispatched 16 s apart. `REPLACE_FILE` is an
unactionable remedy for those three rows. No replay was made (packet; CTO 102694).

## DLQ (the CRO's st4 condition 1 fallback arm; CTO: growth over 1 is a BLOCKING row)

`irpt-generation-dlq` read 14:06Z: `ApproximateNumberOfMessages 1`, `ApproximateNumberOfMessagesNotVisible 0` --
**unchanged** from the pre-existing 1 recorded at create (13:09:53Z). No growth, so **no BLOCKING row**.

## Arms that stay open, carried forward

- **Multi-Comp** (Y2) -- unexercised in W22, as in W21. Carried.
- **The first certified 49financial report** (Y4) -- unexercised. Carried.
- **A certified Inflection report** (Y5) -- unexercised, as in W21. Carried.
- **Target Weight** (Y3) -- the XLSX normalized inside the bound; its report state is recorded below.

Three of the five bodies never reached K5, so the foreign-firm name check for 49financial and inflection (CRO
condition 3) has no W22 PDF to run against. It ran and passed on Y1's cottonwood PDF only.

## Y3 terminal state -- ATTENTION `SESSION_REFRESH_ALREADY_USED`, at 14:31:19Z

`irpt-jobs`, consistent Query, tenant `cottonwood`, job `REQ-51f1413b9d84d26a66aaa71c`:

```
state             ATTENTION
job_detail        {"code":"SESSION_REFRESH_ALREADY_USED"}
outbox_state      SENT
fence_token       3
composition_sha256 c036698bc226fe57..
intent_holdings_upload    claimed_at 1790690392  fence 1   (13:59:52Z)
intent_portfolio_create   claimed_at 1790690394  fence 1   (13:59:54Z)
intent_session_refresh    claimed_at 1790691317  fence 2   (14:15:17Z)
```

**This is a named terminal state and a pass of the window**, and the refusal is the designed one:
`resident_worker.refresh_session` (`resident_worker.py:126-129`) admits ONE causally admitted refresh per request --
*"never replay a mutation"* -- and raises `WorkerAttention("SESSION_REFRESH_ALREADY_USED")` on a second eviction.
`tests/test_resident_worker.py:264` covers exactly that path. The job declined to replay its mutation, which is
correct.

**Target Weight itself is proven through the vendor**, short of a report: `checkpoint_upload` reads `ok=true`,
`status 200`, `rows_sent 2`, `rows_echoed 2`, `reconciled=true`, `upload_record_id 780748`, `weight_unit_echoed
Dollars`, rows `AAPL 600.0` / `VNQ 400.0` -- the notional-1000 scaling applied to the XLSX. `checkpoint_portfolio`
names `model_portfolio_id 2367113`, `IRPT REQ-51f1413b9d84d26a66aaa71c r1 5f40e4cbc24f`. No PDF and no report
followed, so **no case trace was run on Y3**: there is no `checkpoint_pdf` for the trace's later hops to read, and the
window's 5 submissions were spent, so nothing was resubmitted.

Timing: 31.5 min from the K5 POST (13:59:48Z) to ATTENTION, against 16.3 min for Y1's Comparison in the same window.
`job_watch.py` read `SUBMITTING / SENT` continuously from 14:10:45Z through its 900 s timeout; direct consistent reads
every 25 s then caught the flip.

Filed as **`IRPT_BCKEND-S207`**: the double session eviction inside one 31-min request, and the fact that the resident
journals NO line for a job ATTENTION -- the span 14:08-14:34Z carries 79 lines, all `IRPT_RESIDENT_POLL`
(`handled=1` only on the 14:30:19Z tick that moved the row), with nothing naming the code. The code is recoverable
only from `irpt-jobs`. Class OBSERVATION, `hazard_standing` INERT.

## Leg Y -- what the window proves

| arm | verdict |
|---|---|
| **S194** (a Comparison sends its models and refuses a PDF printing none) | **READ AND DISARMED** on Y1: `variant COMPARISON`, the PDF prints `Opal Long-Term` on 16 pages, `COMPARISON_NOT_PRINTED` did not fire, 20/20 evaluable links MATCH |
| **S193** (a resolve RETRY is bounded; the 4th receive moves the row to NEEDS_CORRECTION `RESOLVE_RETRY_EXHAUSTED`) | **READ LIVE three times** -- Y2, Y4, Y5 -- from the rows themselves, per the CTO's condition 1 |
| **CRO condition 1 fallback arm** (DLQ before and after) | **1/0 both times**, no growth, no BLOCKING row |
| **CRO condition 3** (per body: the resolve line and the terminal state by name) | **5 of 5 recorded by name**; the foreign-firm name check ran and passed on Y1's cottonwood PDF, and had no W22 PDF to run against for 49financial or inflection |
| Multi-Comp (Y2) | UNEXERCISED, carried |
| First certified 49financial report (Y4) | UNEXERCISED, carried |
| Certified Inflection report (Y5) | UNEXERCISED, carried |
| Target Weight report (Y3) | vendor upload + portfolio create PROVEN, report UNEXERCISED, carried |

**5 of 5 bodies terminal by name, 39 min inside the 15:10:37Z cap. No hang past the cap. Nothing deployed in the
window; no code, IAM or schedule change; every write is one the principal owns.** Credoff (leg D1) handed to
`2.0.0_SA_COO~P` at 14:32:50Z.

**Rows filed, both class OBSERVATION / `hazard_standing` INERT:** `IRPT_BCKEND-S206` (@befabb9a7b) and
`IRPT_BCKEND-S207`.
