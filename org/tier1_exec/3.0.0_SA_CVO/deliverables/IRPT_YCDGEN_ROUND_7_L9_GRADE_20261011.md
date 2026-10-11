# IRPT_YCDGEN round 7 -- L9 read of the FWD-1 run

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T06:46:30Z. Row IRPT_YCDGEN-D2-S39.
**Input:** `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r7/ROUND7_DRAIN_END_READ_20261011.md @6505291224 (msg 4282)`; the run record `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r7/R4_R5_OWNER_READ_REV6_20261011.json @46e01935cf`. The round carries no judgment criterion; the issuer leaves one question to L9.

**The question:** does a served report with 6 of 257 sections carrying a value, and a status-job that reads UNAVAILABLE, meet FWD-1?

**Verdict: FWD-1 is NOT MET by this run, and the section count is not the first reason.**

FWD-1's ACCEPT (PRD :45-49), clause by clause:

| clause | this run |
|---|---|
| Andrew, signed in as himself | No. A service account signed in (the record's login call) |
| submits a real Cottonwood portfolio the way he does today | No. The run submits nothing; it reads an existing request. Every read of that request names the tenant 49financial, not Cottonwood |
| opens an Opal-branded Overview without coming back to it later | Not shown. Three API reads answered 200; no page was opened, and the request predates the sitting |
| every figure was worked out by Opal from data Opal already keeps | 6 sections carry a value; 251 read NOT_AVAILABLE |
| nothing was asked of YCharts during the run | Holds for the read: the status function's log names it 0 times. Generation was not part of this run |
| a figure Opal cannot work out says so on the page, with the reason | Partly: each NOT_AVAILABLE section carries a method (155 held, 65 builder-only, 22 vendor-sourced, 9 own-series). Whether the PAGE says so was not read |
| a step that used a saved example fails the outcome | The run reads a request made earlier. That is a saved example |

## What the run does establish

The served read path works on irpt-status revision 6. This seat's own read of the live function: `6idtFvAm`, 30 invocations since the
promote, 0 TypeError, 0 RetentionRefused. Revisions 3, 4 and 5 each failed to serve this same report (rows D2-S21, D2-S22, D2-S24).
An Opal-engine report is retained, read back and served with its original file. Twelve ARMED rows from round 6 named pieces of that
path; the issuer's twelve resolving rows stand on it.

## What is owed for FWD-1

One live sitting: Andrew signs in, submits a Cottonwood portfolio, and opens the Overview. Before it:
- row D2-S38 (ARMED): the portal's own status call, with the date header, is refused for a READY Opal report, so the page would not
  show it finished;
- row S16 (ARMED): Andrew's own run of 2026-10-07 stopped at generation with ENVELOPE_STATUS;
- 251 of 257 sections have no value. Whether that is acceptable on a first Overview is the CTO's call; the PRD's clause is that each
  says why.

## The channel

126 investigation rows against a watermark of 33. This compile dispositions 28 and graduates 7. 45 INERT rows of rounds 6 and 7
that no resolving row names are NOT compiled here.
