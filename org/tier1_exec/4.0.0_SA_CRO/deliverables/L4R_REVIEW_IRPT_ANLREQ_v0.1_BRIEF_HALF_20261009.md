# L4-R REVIEW -- IRPT_ANLREQ v0.1, brief half: REFUSE (two items not carried, one mismatched, coverage by pointer)

**Reviewer:** 4.0.0_SA_CRO~DELL2, 2026-10-09
**PRD:** `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` @5dd6c2422b (half_hash ddc626f124b6)
**Brief:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_223xZ_ANALYSIS_REQUEST_END_TO_END_ONE_PROJECT_CLOSER_TRACE.md`
@2b21a349d1
**Delivery:** CTO~DELL2 msg 2406.

## Denominator

The brief at the pin carries **14 items**:
- 8 under "The journey he names" (:34-45): analysis type; comparables; Excel attached; typo check and swap; ticket in
  the open page; report generated; commentary from the report; package attached.
- 6 under "What he directs" (:48-56): one workflow with the form primary; the Analysis tab after; measure the COO
  workstreams; trace closer-style; compress into ONE project; the stopping defect.

The PRD's BRIEF COVERAGE (:126-135) has **6 rows**, keyed to the CRO trace's hops rather than to the brief's items.
Every row is a pointer ("FWD-2, S1"), not the item's content. The heading denominator does not match: 14 vs 6.

## Item by item

| # | Brief item (line) | Carried? | Where, or the gap |
|---|---|---|---|
| 1 | type of analysis (:35) | YES | FWD-2 :38 |
| 2 | Opal-model checkboxes + other-ETF input (:36) | YES | FWD-2 :38 |
| 3 | holdings Excel attached (:37) | YES | FWD-1 :29-30 |
| 4 | typo check AND swap, frontend AND backend (:38) | **MISMATCHED** | see R2 |
| 5 | ticket in the open Ticket Center page (:39) | YES | FWD-1 :33 |
| 6 | backend generates the full report (:41) | YES | FWD-1 :30 |
| 7 | commentary from the report's key surfaces (:42) | YES | FWD-3 :44 |
| 8 | package attached: report + branded PDF with commentary + original Excel (:43-44) | YES | FWD-1 :30-31 |
| 9 | ONE workflow, form primary (:48) | YES | FWD-1 |
| 10 | Analysis tab after, manual path (:49) | YES | FWD-6 :61-65 |
| 11 | measure each COO workstream (:50-51) | YES | section 1 (:68-80) cites the trace @9076346655 |
| 12 | closer-style trace, then the frontend (:52-53) | YES | section 1; backlog order (:99-105) |
| 13 | **COMPRESS into ONE project** (:54-55) | **NOT CARRIED** | see R1 |
| 14 | the defect: stopping on another agent's or box's deliverable (:56) | **PARTIAL** | FWD-4 and C-ONE-JOURNEY carry the rule, but the design keeps the dependency (R1) |

## Corrections (by pinned line)

**R1 -- item 13: the compression is not in the PRD.**
- The brief directs that the IRPT_BCKEND and IRPT_YCDGEN parts, NFRA_TRNSPT's commentary part, TCKT_VNEXT and the
  frontend be compressed "into ONE project, so one driver can run it end to end" (:54-55).
- At @5dd6c2422b, the SURFACE MANIFEST (:116-124) leaves the three central surfaces with other projects' lanes:
  - S3, the upload door, with IRPT_BCKEND ~Y2;
  - S4, the engine layout and render, with IRPT_YCDGEN ~G2;
  - S5, the commentary Lambda and H1, with NFRA_TRNSPT ~T2 and IRPT_BCKEND ~P2.
- Section 2 (:97) parks hops 4 and 6 on "another project's open cell". That is the cross-project wait the brief names
  as the defect (:56). This PRD adds a fourth project around the same three.
- **Needed:** a contract (for example C-ABSORB) that names, per surface S3-S5, the cells and write paths that MOVE into
  this project, and the projects that keep the remainder (IRPT_BCKEND keeps ~P2's platform; NFRA_TRNSPT keeps
  FWD-1..9). The un-park condition of hops 4 and 6 then becomes this project's own cell, not another project's.
- If a surface deliberately stays outside, the PRD says why, and names its date and owner as a pre-arranged input,
  not a wait.

**R2 -- item 4: "swap" is read as a model swap, and the backend half is unowned.**
- In the brief, "typo check and swap ... (frontend design and backend process both)" (:38) is the security resolution
  in the form. FWD-2's ACCEPT (:40) reads it as "a person who wants a model swapped".
- The backend swap is today `KIMI_WEB_SEARCH_UNVERIFIED`
  (`infra/aws/lambda/investor-reporting/intake/resolution_kimi.py:159-165`), moved by CTO msg 120 to IRPT_YCDGEN
  FWD-16 (candidates from etf-classifications). The manifest names only S1 (frontend) for FWD-2.
- **Needed:**
  - FWD-2 states the security swap: an unknown or unpriceable holding replaced by a confirmed candidate before filing.
  - A surface row names the backend swap's owner inside this project (R1).
  - A model swap, if Andrew also meant one, is a second line, not a substitute.

**R3 -- BRIEF COVERAGE carries pointers (:126-135).**
- Rewrite it as one row per brief item (the 14 above), each carrying its content into the consuming cell:
  - the fields (analysis type values, model list source `ycharts/generate/comparison_catalogue.py`, ETF input);
  - the paths;
  - the guards (C-FIRM, C-PACKAGE pointers-only, C-KIMI abstract fields);
  - the proof gap (for example hop 9: no signed-link open yet).

**Note, no correction asked:** FWD-3's DRAFT gate (:43-47) is not in the brief. It is sourced to NFRA_TRNSPT C-KIMI, which
the PRD cites, and it does not narrow FWD-1's package. Recorded so the CVO's ratified-text half sees it was read.

## Verdict

**REFUSE** the brief half at half_hash ddc626f124b6. R1 is the substantive item. R2 and R3 are corrections that a v0.2
can carry in the same bump. The re-review re-opens only this half.
