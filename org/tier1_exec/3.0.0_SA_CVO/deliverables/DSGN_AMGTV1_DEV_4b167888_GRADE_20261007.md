# DSGN_AMGTV1 -- grades on the SERVED page, portal DEV 4b167888: FWD-20, the uncovered-name read, FWD-7 (3.0.0_SA_CVO~Z, 2026-10-07 ~14:0xZ)

**Asks:** `2.0.0_SA_COO~D` msg 30978; `1.0.0_SA_CTO~Z` msg 30982.
**Served:** `git -C portal ls-remote origin DEV` reads `4b167888` (this seat, ~13:5xZ). `b3440392`, the candidate graded
at round 49, is an ancestor of it; `git diff --stat b3440392 4b167888` is one file, `scripts/ui-contract-check.mjs`
+9/-8. So the product bytes on DEV are the candidate's.
**Read:** `round50/dev-read-4b167888/` (the grades file and the instrument log) and
`round35/walk/read-20261007T133420Z/` (27 result files, the MSFT header PNG, the tab texts of BA, VLO, AMD and MSFT),
under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/`. The walk ran the local build of that sha
against the live data front door; the issuer says it logged in 30 seconds before CI concluded.

## Verdicts

| row | grade on DEV | basis |
|---|---|---|
| FWD-20 | **REALIZED** | the render check on the served sha: 76 PASS / 0 FAIL / 1 N/A, 4 of 4 arms |
| the uncovered-name read (round 47 item 5) | **MET** | MSFT US shows its one sentence once and no tiles |
| FWD-7 | **NOT REALIZED**, 2 covered names short | 93 of 95 covered names serve an officer list; BP/ LN and NG/ LN serve none |

## FWD-20 -- REALIZED on DEV

- `instrument35.candidate.grades.json`: result PASS 76, FAIL 0, N/A 1; 0 FAIL cells on any of the six states; the
  Model state's smallest text is 11.
- `instrument35.log` ends "THE INSTRUMENT GRADES THE REDESIGN AND CAN FAIL: 4 of 4 arms", rc 0.
- **What changed in the instrument on DEV, read by this seat:** the designed-states clause now requires three kinds
  (empty, loading, error) and counts no-permission without requiring it. That is PRD v0.17's FWD-19 and FWD-20. It
  closes the four-against-three finding of round 49.
- **One limit.** The nine planted fail-and-clean pairs of round 49 ran on the instrument one commit earlier. The
  commit touches only the states clause, and the planted violation there (the error state stripped) is still a
  required kind. I read the diff and judge the pair still holds; it was not re-run on the DEV instrument.

## The uncovered-name read -- MET, with one finding

`fwd24-MSFT-US-header.png`, read at full size: under the identity card the page prints "We hold no stored company data
for this name yet." once, with no key-figure tiles (round 46: seven tiles, the sentence seven times).

**Finding on the same screen, not part of this read's bar.** The Chatter line says "No articles collected for this
name this month." The Recent news card above it shows an item dated October 2nd, 2026, with 34 more behind it. The
chatter count covers the 95 covered names, and MSFT is outside them, so the sentence is wrong for an uncovered name:
it reads as "nothing was collected" beside the collected articles. It is FWD-27's "no two figures disagree" on a
name the firm does not cover. Whether that is a page line or a served one is unread.

## FWD-7 -- NOT REALIZED, and the two things the CTO asked me to weigh

The outcome is "A PM sees who runs the company, for every covered name".

1. **Are BP/ LN and NG/ LN covered names? Yes.** `covered_security_keys()` returns 95 keys and both
   `BP/_LN_Equity` and `NG/_LN_Equity` are among them (this seat's run). My read of the deployed function at ~13:4xZ:
   `/thesis` 200 on 95 of 95, the officer list non-empty on **93**, empty on **2**. So the outcome is short by exactly
   those two until the slash-safe reader ships (AMGT_RESAPP row Z-S365, a round-78 cell, and a redeploy).
2. **Does the wording accept a Bloomberg list? Yes.** The ACCEPT reads "shows the company's officers and says where
   the list came from, even when the company's filing has no officer section". A labelled fallback is what that
   sentence describes. On the walk AMD US reads "Officers from the Bloomberg fallback list -- the filing roster did
   not resolve" and "25 OFFICER(S) FROM BLOOMBERG OFFICER LIST (NO FILING ROSTER COULD BE READ)". The source is said.
   BA US (12) and VLO US (5) read from the 10-K's Item 10.

Also read on the deployed lists, for the page: NKE US opens with the Chairman and has the CFO seventh, and BA US's
filing list is alphabetical. FWD-27 asks for the chief executive first, then the CFO. Whether the page reorders was
not walked.

**FWD-7 moves to REALIZED when the deployed route serves an officer list on 95 of 95,** or names the names that have
none with their reason, and one walk shows it.

## Board on DEV, as I read it

22 REALIZED, 3 NOT_REALIZED (FWD-7, 8, 27), 1 NOT_EVALUATED (FWD-1, Andrew's own walk on PROD), 1 RETIRED. The grades
that were "on the candidate" at rounds 48 and 49 (FWD-18, FWD-20, and FWD-27's money format) are now grades of what
DEV serves.

-- 3.0.0_SA_CVO~Z
