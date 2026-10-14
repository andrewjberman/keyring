# Andrew-direct 2026-10-14 ~19:1xZ (laptop, 1.0.0_SA_CTO terminal) -- Security Analysis: what each security needs, when it is pulled, how DEMQUE accounts for it, and the JSON dossier

## VERBATIM

> "Another thing I want to clarify is that we should be pulling daily all necessary items for the AMGT "Security Analysis" dashboard
> application, I want to know what the needs are for that, what the various surfaces are and what needs to get done to that end. Have
> 4.0.0_SA_CRO on this box look into it on three aspects: 1.) What exactly does each "security" included in there need to display
> (anything that populates the various tabs where do they all come from per component/tab)? 2.) What is the current schedule on those
> surfaces? 3.) How are these accounted for in MDPF_DEMQUE quota system? -- The premise behind doing this is looking for gaps in the
> above that need to be filled. I also want to make sure that we have the downloadable dossier in clean JSON format with all necessary
> citations and etc., so need to know the status on that as well. These findings will likely inform either a foldin for RESAPP or
> similar project on DELL1."

## The ask, to `4.0.0_SA_CRO` (laptop), research only: no commit outside its own deliverables, no served change

Target: a daily pull of everything the Security Analysis page needs, for every security on it. The denominator is the
security list the page serves (V1 is 93 names; the CRO prints the measured count).

1. **What each security displays, per tab and per component.** For every tab and panel on `/security-analysis` (code under
   `portal/src/pages/SecurityAnalysis/`), give:
   - each field shown;
   - the served object it reads (an address, read from the code or network, not from memory);
   - the producer that writes that object;
   - that producer's upstream source (vendor, Bloomberg queue, filings, AI fill).

   One table, one row per (tab, component, field group).
2. **The current schedule of each surface.** Per producer: the trigger as DESIRED (in code or Terraform) against APPLIED (the
   live rule, read from AWS), the last success, and the as-of date it serves today on the trading-day frontier
   (`lib/trading_calendar.py`). Name every surface that is not on a daily schedule, runs only on an upstream's success, or runs
   ad hoc.
3. **How MDPF_DEMQUE's quota system accounts for each.** Which of those pulls are demand rows in DEMQUE's queue, under which
   quota (Bloomberg budget, vendor caps), at what cadence. Which ones bypass the queue. Which needs are not in the queue at
   all.
4. **The downloadable dossier.** Its status as clean JSON:
   - does the download exist;
   - its schema;
   - whether every value carries its citation (source, as-of, and a claim field: measured, inferred, held or absent, per
     CLAUDE.md "a value must carry its claim");
   - what is missing.

   Read one real security's dossier end to end.

**Output:** one findings file under `org/tier1_exec/4.0.0_SA_CRO/deliverables/`. It covers the four parts, then a **GAPS** list.
Each gap gives: the surface, what is missing, its proposed fix, and which dell1 project should take it (AMGT_RESAPP or another
named project). The CRO then sends the file path to `1.0.0_SA_CTO`. This seat rules the fold-in and relays it to dell1
(`1.0.0_SA_CTO~DELL1`), since dell1 is wholly ADVI/MDPF plus overflow AMGT.
