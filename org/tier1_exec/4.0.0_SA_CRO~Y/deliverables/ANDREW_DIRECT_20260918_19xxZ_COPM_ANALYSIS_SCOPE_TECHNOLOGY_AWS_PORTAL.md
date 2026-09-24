# ANDREW-DIRECT 2026-09-18 ~19:0xZ -- COPM vs. platform analysis: scope narrowed to technology (AWS Cloud + opalinvest.dev), AI in particular

**Channel:** Claude Code terminal, seat `4.0.0_SA_CRO~Y`, two consecutive user messages in the same session
that produced `ANDREW_DIRECT_20260918_1836Z_COPM_PARSE_COMPLIANCE_POLICY.md`.

## Verbatim, message 1 (the ask and the deliverable shape)

> That's fine, now what we need is a structured, chunk-by-chunk in document page order, analysis of what
> the policy says versus what the opal technology platform does in practce. i want to create a plan with
> you on how to do this based on the outcome deliverable. I believe what we should be able to generate is
> effectively a document that leads with a green/yellow/red summary breakdown of each item delineated in
> this document and where the platform stands as a whole, then it breaks them down reds first, then
> yellows, then greens, with a table of contents for the various items. Something like this. What do you
> think? What do you suggest?

## Verbatim, message 2 (the scope ruling)

> The truth of the matter is, our focus here is really on the technology side. We do not necessarily have
> information on the rest of the organization, so i'd scope this entirely around any technology,
> particularly AI, functions that are governed in the Opal AWS Cloud and displayed on the opalinvest.dev
> portal. That is a tighter, more realistic deliverable. Regarding everything else you said, yes i agree,
> let's get started with a synthesis of what you said and my scope narrowing listed here.

## Scope as read (surfaced, not adjudicated)

The PLATFORM under analysis is the Opal AWS Cloud estate plus the opalinvest.dev portal, including any
AI running there. Every obligation in the manual that binds people, paper, offices or off-platform
processes is OUT OF SCOPE by declaration. "Everything else you said, yes i agree" adopts this seat's
proposal of 2026-09-18 ~18:5xZ: obligation atoms (not chunks) as the unit; a three-bucket triage
(IMPLEMENTS / IN-SCOPE / OUT) reviewed by Andrew before any color; GREEN / YELLOW / RED each carrying a
basis (MEASURED / HELD / UNVERIFIED); a report that leads with an executive summary and a per-section
heatmap, then reds, yellows, greens, two tables of contents, and a page-order ledger appendix.

The plan is written as `C:\Users\Opal Bloomberg\Desktop\compliance_policy\ANALYSIS_PLAN.md`. The work
runs at this seat, directly with Andrew; it is not a fabric project and no register row is opened
unless Andrew says so.

## State at this record

- Step 1 DONE: `extract_requirements.py` -> `requirements.jsonl`, 1,996 atoms (190 control-box rows,
  1,799 obligation sentences incl. 157 bullets inheriting an introducer, 7 tables), page order.
- Step 2 DONE pending Andrew's review: `triage.py` -> `triage.jsonl`, `triage.md`, `triage_summary.json`:
  IMPLEMENTS 111, IN-SCOPE 489, OUT 1,396; 96 rules; 11 open questions each of which decides a rule's
  bucket. Review page: `triage_review.html` (published as a private Artifact).
- Andrew answered all 11 questions ~19:4xZ (verbatim in the terminal; summarized in ANALYSIS_PLAN.md):
  portal audience = wealth advisors, no clients; distributor hosts ETF disclosures; PM team runs baskets
  off-platform; no orders originate in the platform; portal is not the restrictions system of record; no
  valuation/liquidity data on the estate; TicketCenter is advisor-level; "the firm's server" = AWS; the
  agent fabric is engineering assistants (Andrew-only access), Microsoft 365 is the more relevant AI/mail
  plane. Two further words ~20:2xZ: "schwab client data is in opal-data-assets/schwab"; "its all
  encrypted volumes/buckets". Re-triage: IMPLEMENTS 90 / IN-SCOPE 210 / OUT 1,696, 0 open questions.
- Step 3 DONE: `facts.py` -> `facts/platform_facts.md`, 40 facts (MEASURED from source and read-only
  live AWS calls at ~20:0x-20:2xZ, HELD from Andrew, UNVERIFIED where the estate cannot show it), plus
  `facts/s3_posture_sweep.py` over all 38 buckets.
- Step 4 DONE: `findings.py` -> `findings.jsonl`: 35 items covering all 300 in-scope atoms: 12 RED,
  17 YELLOW, 6 GREEN; basis 26 MEASURED, 6 HELD, 3 UNVERIFIED.
- Step 5 DONE: `build_report.py` -> `COPM_platform_report.html` published privately at
  https://claude.ai/artifact/MAeqm7Sh9DkfJXR1MJMGf8 (triage page: https://claude.ai/artifact/XbGic4kHmALyB93P6o11pY),
  and `COPM_platform_report.md`.
- Nothing in the estate was changed; every AWS call was read-only. Step 6 (review of reds and yellows
  with Andrew) is next and is his.
