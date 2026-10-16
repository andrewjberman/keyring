# YCharts pacing, and where the process still asks YCharts first (4.0.0_SA_CRO~DELL2, 2026-10-16 ~15:3xZ)

**Asked by:** Andrew, `ANDREW_DIRECT_20261016_152xZ_YFINANCE_FIRST_YCHARTS_SECOND_EVERYWHERE_AND_YCHARTS_PACING.md` (same folder).
**For:** `1.0.0_SA_CTO~DELL2` (the ruling), `2.0.0_SA_COO~G2` (the engine). Read-only: code at HEAD and AQ2's committed journals.
Every line is MEASURED (a cited line) unless marked INFERRED.

## 1. The pacing in the code

- **The only spacing on a YCharts call is 2.0 s per account**, enforced by the provider lease:
  `infra/aws/lambda/investor-reporting/ycharts/session/operation_lease.py:42` (`SPACING = 2.0`), set on each send at `:165`.
  The upload door's lookup uses the same lease without a session (`SessionlessTransport`, `:298-317`), one operation at a
  time per account.
- **The research runner already treats the limit as a count per window, not a rate**: at most 6 requests per lease window,
  then a wait (`ycharts/research/runner.py:201-207`, `:547`). Its note: "The vendor's WAF challenged the 7th call of a run
  spaced ~1.5 s apart" (`:209-211`).
- **The measured challenge window is 122 to 373 s, and 390 s clears it.** See `ycharts/generate/resident_worker.py:860-877`
  and probe `WAF-PROBE-20261005T1254Z-W330`. The new retry schedule of 150, 300 and 450 s (`:864`) is sized to that window.

## 2. What today's runs show

From `org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_fwd1_r3/A_SET3_JOURNAL_R3.txt`:

- SET 3 ran its lookups one at a time, about 90 s apart. Four ended READY at 14:22:23Z, 14:23:55Z, 14:25:35Z and 14:27:28Z.
  The fifth was challenged at 14:28:55Z. Its retries at 14:29:56Z and 14:30:56Z, 60 s apart, were challenged too, and it was
  exhausted at 14:31:56Z.
- The 11 to 60 s gaps named in SET 2's reading are the `IRPT_RESIDENT_KIMI kind=check` calls (24.2, 16.9, 11.2 and 17.7 s in
  SET 3). Those are the AI check, not YCharts spacing.
- SET 2 had the symbols in the opposite order, and its fifth lookup was challenged as well (AQ2's reading in the same file).

**Reading.** Requests per second is not what trips the challenge. Calls 1.5 s apart (the earlier run) and calls about 90 s
apart (today) are both challenged after about 4 to 6 calls. INFERRED: the vendor's firewall counts calls over a window of
several minutes, so the working budget is about 4 to 6 lookups per roughly 6 minutes from this host. Wider spacing barely
raises it.

INFERRED, not tested: the lookup is cookieless and comes from an AWS address (52.90.35.83, `WAFLOOK_READ.txt`). A
bot-detection challenge would also explain a cutoff after a few calls. One read tells the two apart: after a 390 s rest, send
six lookups for six known symbols about 90 s apart, then six more 5 s apart. If the cutoff falls at the same count both
times, it is a count per window. If it does not, it is something else.

**Consequence.** Under the current order, every holding costs one YCharts lookup. A 20-holding upload would need about four
windows, roughly 25 minutes, before the back-off is even used. Asking yfinance first removes the YCharts lookup for every
holding Yahoo knows. YCharts is then asked only about what Yahoo misses, which is usually fewer than the budget.

## 3. Where YCharts still comes first (Andrew: "yfinance first and ycharts second as a general rule for any part of this process")

| Step | Today | Code |
|---|---|---|
| Upload door, holding check | YCharts lookup first; yfinance only on a YCharts NOT_FOUND | `intake/security_resolution.py:79-83`, `:321`; namespace `YCHARTS_SECURITY_ID` (`:203`) |
| Report pricing | The chain is built Yahoo first (`ycharts/research/price_source.py:15`, `CHAIN = ("estate", "yfinance", "ycharts")`), but it is OFF in the resident build | `reports/build_resident_package.py:119`, `"opal_pricing": {"enabled": False, ...}` |
| Report generation | Builds the portfolio in YCharts by YCharts security id (`ycharts/generate/*`). INFERRED: this is why the door resolves YCharts ids first | not traced to the line |

## Addendum 1 (2026-10-16 ~18:4xZ): the paced read came back 12 of 12 clean

`org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_r34g/PACED_READ.txt` (bb06dae32c): after a 390 s rest, six known
symbols were looked up 90 s apart, then, after the same rest, six more 5 s apart. All 12 answered 200, with no cutoff in either
phase. This disproves "4 to 6 LOOKUPS per window" as section 2 wrote it.

It is still consistent with a cutoff counted in CALLS. An unknown symbol costs two `securities_info` calls: the lookup
(`intake/resolution_broker.py:102`, one call per batch) and the suggestion verify (`intake/upload_suggestions.py:69`). So the
challenged fifth lookups of SETs 2 and 3 were likely about the 8th or 9th call. INFERRED: the journals do not log verify calls.
The earlier run was challenged on its 7th call (`runner.py:209-211`). A cutoff of about 7 calls per window fits all three
reads. `~G2` reads the trigger as unknown symbols instead (msg 9753). The unknown-symbol paced read settles it, provided it logs
every call, verify calls included (this seat's msg 9758).

**The decision for the CTO.** Is "yfinance first" (1) a door-only reorder, keeping a YCharts id lookup only for holdings
YCharts must carry? Or (2) Opal pricing switched on, so a holding Yahoo prices never needs a YCharts id? Option (1) alone
leaves the report needing YCharts ids. Option (2) is the general rule as Andrew stated it. The DONE WHEN of FWD-7 already
says "no YCharts call end to end" (`IRPT_ANLREQ_PRD.md:188`).
