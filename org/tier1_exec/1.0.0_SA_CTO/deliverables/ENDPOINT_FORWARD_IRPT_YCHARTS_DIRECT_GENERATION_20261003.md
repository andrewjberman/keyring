# ENDPOINT (step 2, /endpoint --forward) -- YCharts direct-API generation, Opal-branded

**Status: L2, emitted by `1.0.0_SA_CTO` 2026-10-03 ~17:5xZ. NOT YET LANDED in a PRD**: no project is registered (L3) and no PRD
exists (L4). This file is the carrier until the block is pasted, unchanged, under the PRD's section `ENDPOINT (step 2,
/endpoint --forward)`. Andrew confirms the DONE WHEN lines (his 2026-09-03 word: "i will confirm CTO's DONE WHEN from their
/endpoint --forward").

**Brief:** `docs/briefs/irpt-ycharts-direct-generation-opal-branded-brief-20261003.md` @45f673c2ea (195 lines, `4.0.0_SA_CRO`,
2026-10-03 17:3xZ). **Order:** Andrew-direct at the `2.0.0_SA_COO~Y` terminal ~17:0xZ (relayed msg 104648), recorded verbatim in
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/RESEARCH/CRO_REQUEST_YCHARTS_DIRECT_GENERATION_20261003.md` @ee801b0505.

```
  FWD-1  Andrew asks for an Overview report on one Cottonwood portfolio and opens an Opal-branded
         version that Opal's own script made, end to end on the live YCharts account
         DONE WHEN  EXERCISED -- one live run, ending in Andrew opening the report
         ACCEPT     Andrew opens an Opal-branded Overview for a real Cottonwood portfolio, made by Opal's
                    own script from YCharts answers it asked for live, and kept with those answers in
                    Opal's own store. Every number in it can be traced to one of those answers, or is
                    marked as not available. A step that used a saved example instead of asking YCharts
                    live fails the outcome
         SOURCE     brief PART I, "The candidate thread" (lines 22-27)

  FWD-2  An analyst can read what any YCharts call in a run gave back, from Opal's own store,
         without asking YCharts again
         DONE WHEN  EXERCISED -- an analyst has looked one up
         ACCEPT     for a finished run, an analyst picks any one call and sees what it gave back, whether
                    that was identifiers, data or a document, and whether it changed since the previous
                    run. Nothing kept contains a password, a login session or a key
         SOURCE     brief O1 (lines 29-33); PART V "No secret in any artifact"

  FWD-3  For each of the three report types, an analyst can point at anything on a YCharts-made
         report and say where it came from
         DONE WHEN  EXERCISED -- an analyst has traced one element of each type
         ACCEPT     for an Overview, a Comparison and a Multi report, every number, table and chart on the
                    page is either tied to a named YCharts answer, or listed plainly as something YCharts
                    works out only inside its own report builder. Nothing on the page is left unaccounted for
         SOURCE     brief O2 (lines 35-40)

  FWD-4  An analyst can make the Comparison and Multi reports too, Opal-branded, with Opal's own
         script
         DONE WHEN  EXERCISED -- one of each made and opened
         ACCEPT     for the same portfolio and comparisons, Opal's script makes a Comparison and a Multi
                    report in Opal's branding without YCharts' report builder. Anything YCharts works out
                    only inside its builder is rebuilt from data Opal holds, or left out with a note saying
                    so. It is never imitated
         SOURCE     brief O3 (lines 42-46); PART III item 5

  FWD-5  The Opal-made report and the answers behind it are found in Opal's own store, private to the
         client's firm
         DONE WHEN  EXERCISED -- an analyst has found one by its request
         ACCEPT     given a request, an analyst finds its report and every YCharts answer behind it in the
                    client firm's private area of Opal's store. Nobody at another firm can reach them, and
                    nothing the analyst needs exists only on YCharts
         SOURCE     brief O4 (lines 48-51); PART V "Client holdings stay inside their firm"

  FWD-6  A report run is something Andrew waits for at his desk, and every run shows where its time
         went
         DONE WHEN  EXERCISED -- Andrew has waited for one, and its timing record has been read
         ACCEPT     Andrew asks for a report and has it in the same sitting, without coming back to it
                    later. The run's record shows how long each stage took, with the time YCharts spent
                    working kept apart from the time Opal spent waiting
         SOURCE     brief O5 (lines 53-56); Andrew: "It has no need to take 15-20 minutes"

  FWD-7  For the same inputs, an analyst sees which figures on the YCharts report and the Opal report
         agree, and why any differ
         DONE WHEN  EXERCISED -- once for each of the three report types
         ACCEPT     for one report of each type, an analyst lists every figure that matches and every one
                    that differs, each difference with its reason: different dates, a different way of
                    calculating, or something only YCharts works out. It is a one-time check of the new
                    script, not a comparison that keeps running
         SOURCE     brief O6 (lines 58-61)
```

## Boundaries the outcomes keep (not outcomes)

- **No second production path.** This project is research, plus the one thread. Opal's script does not run alongside the
  served YCharts generation as a second producer of the same reports (Andrew's standing veto on shadow and build-alongside
  pipelines and on standing parity comparators). FWD-7 is a one-time check. If Opal generation is later adopted, it
  REPLACES the served path in the same window; that is a decision after this research, not part of it.
- **The served path is undisturbed:** research runs never interleave with `~Y`'s Analysis runs on the one session.
- **No research run costs Andrew his YCharts session** (brief PART III item 4). Calls stay one at a time, at a pace the
  YCharts firewall tolerates. A firewall challenge stops the research, not the served path.
- **No client-facing release** of an Opal-branded report is in scope (brief PART II).
- **Every new store address and resource name comes from the naming builders** (CLAUDE.md rule 30). Kept YCharts answers
  need a register family that names them (brief F5).

## Three readings put to Andrew with the DONE WHEN lines

1. **"The same endpoints" -- the CTO's reading (the brief asks for it at L2): the YCharts endpoints that supply the
   report's DATA.** The report-generation calls return only identifiers and links, never figures (brief F2), and their
   output is YCharts' own PDF, which cannot carry Opal's branding. So "Opal-branded, same endpoints" can only be met from
   the data endpoints. FWD-3 finds out which elements those endpoints supply, and names the rest.
2. **The vendor word for research calls -- the CTO's reading: his ~17:0xZ order covers them** ("we should be able to run
   the api calls, persist and categorize the response shape per api call ... then ... run the generation with our own
   custom script that uses the same endpoints"). It is bounded as above: one at a time, never interleaved with the served
   runs, at a firewall-tolerated pace. His confirming the DONE WHEN lines confirms this reading; a narrower word narrows it.
3. **The subscription terms -- his, and not readable by any seat:** may figures YCharts supplies appear in an Opal-branded
   document? Until he answers, every Opal-branded report from this project stays internal (Andrew and analysts). That is
   already the scope, so no outcome waits on the answer; a client-facing release would.

## Provenance

```
GROUNDED ON: docs/briefs/irpt-ycharts-direct-generation-opal-branded-brief-20261003.md @45f673c2ea (read whole, 195 lines);
             the request file it cites, by its quoted words only
NOT READ:    the task-order register, any project JSON, any PRD (none exists); recipe.py, integration.py, bundle.py and the
             X10 row (the brief's citations are used as written); the 2026-09-11 captures; the YCharts subscription terms
```

-- 1.0.0_SA_CTO

## UPDATE ~17:4xZ -- readings 2 and 3 answered by Andrew at the `2.0.0_SA_COO~Y` terminal (~17:3xZ)

Verbatim: "COO~Y and any underlying agents have whitelisted egress to YCharts. Regarding subscription issues, yes we are cleared
for use." Record:
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/ANDREW_DIRECT_20261003_173xZ_YCHARTS_EGRESS_WHITELIST_AND_SUBSCRIPTION_CLEARED.md`
@ce20ca6854 (relayed msg 104655).
- **Reading 2 is settled:** YCharts egress is whitelisted for `2.0.0_SA_COO~Y` and its agents, as spoken. The pacing bounds
  above stay, because they protect the one shared session (row S233), not the egress.
- **Reading 3 is settled:** the subscription clears this use. A client-facing release of an Opal-branded report stays outside
  this project's scope (brief PART II); it is a separate decision, no longer blocked on the terms.
- **Reading 1 stands as the CTO's** (the data endpoints), confirmed here.

What remains for L2: Andrew's confirmation of the seven DONE WHEN lines.
