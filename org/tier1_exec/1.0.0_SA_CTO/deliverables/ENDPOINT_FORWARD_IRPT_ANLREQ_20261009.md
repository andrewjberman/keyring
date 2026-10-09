# ENDPOINT (step 2, /endpoint --forward) -- IRPT_ANLREQ: one Analysis Request, end to end, from the form to the package on the ticket

Author `1.0.0_SA_CTO~DELL2`, 2026-10-09 ~03:4xZ. Placement: dell2. Interim driver `2.0.0_SA_COO~Y2` (CVO verdict msg 1889), under
`/closer`.

**Andrew's words:**
- the request, 2026-10-08 ~22:3xZ, @2b21a349d1: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_223xZ_ANALYSIS_REQUEST_END_TO_END_ONE_PROJECT_CLOSER_TRACE.md`;
- the build word and the DONE-WHEN, given as this seat's discretion, 2026-10-09 ~03:4xZ @35fabf20c8:
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_034xZ_SELF_DRIVE_30M_EVERY_DELL2_PROJECT_AND_DISCRETION_ON_THREE_ACTS.md`.

**Brief (the trace):** `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANALYSIS_REQUEST_END_TO_END_GAP_BRIEF_20261008.md` @9076346655, nine hops.

**What it compresses:**
- TCKT_VNEXT's Analysis Request scope (form, ticket, trigger, attach route, ticket page; FWD-6, FWD-9, C-PACKAGE);
- IRPT_BCKEND `~Y2`'s Analysis lane (upload door, check and swap, generation);
- IRPT_YCDGEN (the Opal engine and brand);
- NFRA_TRNSPT FWD-10 and FWD-11 (the commentary thread).

Their other outcomes stay in their own projects.

**FWD-1 is the ONE journey** (rule 27). Every later FWD enriches it. The ids are permanent; this is the first emission.

```
  FWD-1  One Analysis Request goes from the Ticket Center form to a finished package on the same open ticket, with no person in between
         DONE WHEN  EXERCISED -- on DEV, a seat files ONE request through the form (analysis type, Opal-model checkboxes, other ETFs, holdings Excel) for a
                    49financial client with an eligible advisor; with nobody touching it, the ticket ends up carrying the report, the branded Opal PDF with
                    the investment commentary, and the original Excel, each opened from the ticket page; Alyssa's own first real request grades it again
                    (the organic arm)
         ACCEPT     an Opal person opens the still-open ticket and finds the report, the branded PDF with the commentary and the advisor's original Excel,
                    without asking anyone and without anyone having forwarded a file
         SOURCE     Andrew 2026-10-08 ~22:3xZ; CRO trace hops 1-9

  FWD-2  The form fits the request and catches a bad request before it files
         DONE WHEN  EXERCISED -- the form offers the analysis types and the Opal models as checkboxes plus a field for other ETFs; a mistyped ETF is caught
                    and a correction offered, and a swap is accepted, before the ticket is created
         ACCEPT     a person who types an ETF wrong is told before filing and can pick the right one; a person who wants a model swapped can say so in the form
         SOURCE     Andrew ("typo check and swap ability completely ironed out"); CRO trace hops 1-2

  FWD-3  The investment commentary is written from the report itself, and stays a draft until a person sends it
         DONE WHEN  EXERCISED -- the commentary for FWD-1's request is drafted from that report's key surfaces (abstract fields only, no client identity)
                    and shown on the ticket as a DRAFT
         ACCEPT     the commentary talks about this report's portfolio and comparison, not a generic text; it says DRAFT; nothing is sent to an advisor
                    without a person
         SOURCE     Andrew ("running over key surfaces in that report to feed the investment commentary summary"); NFRA_TRNSPT FWD-10, C-KIMI

  FWD-4  A broken hop never silently stops the request
         DONE WHEN  EXERCISED -- a request is driven through each failure on purpose (the generator down, the commentary refused, the attach refused), and
                    each time the ticket says which step failed and what happens next
         ACCEPT     an Opal person looking at a stuck request can tell from the ticket alone where it stopped and why; no request sits silently unfinished
         SOURCE     Andrew ("agents ... get held up on some random block ... and then they just stop working"); CRO no-stop rule

  FWD-5  Another firm never sees the request, the package or the commentary
         DONE WHEN  EXERCISED -- a sign-in at another firm tries the ticket and each package file and is refused every time, repeatable on demand
         ACCEPT     someone signed in for a different firm is refused the ticket and every file in its package; a statement that it is refused does not count
         SOURCE     TCKT_VNEXT FWD-2; C-PACKAGE firm check; "ALL never admits"

  FWD-6  The Analysis tab is the manual path for the unusual case
         DONE WHEN  EXERCISED -- one request the automatic path cannot finish (a swap the form cannot express) is completed by a person from the Analysis
                    tab, and the package lands on the same ticket
         ACCEPT     an Opal person finishes an unusual request by hand from the Analysis tab, and the ticket ends up the same as an automatic one
         SOURCE     Andrew ("frontend work on the actual Analysis tab will be completed after the fact ... only for unusual cases")
```

## Not here (stays with the source projects)

TCKT_VNEXT's non-analysis ticket types; NFRA_TRNSPT FWD-1 to FWD-9 (transcripts, company read, mail); IRPT_BCKEND's Performance and
Performance client statement lane (`~P2`); IRPT_DASHBD.

-- 1.0.0_SA_CTO~DELL2
