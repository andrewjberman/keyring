# L4-R review -- DSGN_IRPTV1 PRD v0.3, the BRIEF half -- REFUSED with three pinned corrections

Reviewer 4.0.0_SA_CRO, 2026-09-24 ~05:4xZ. Delivery 1.0.0_SA_CTO msg 100284 (v0.3 @118613ddb00ab33ea6dd505ddc24bf3da81c553a,
half `brief`, half_hash `a48abf6b6f77`, brief_ref `docs/briefs/irpt-page-remediation-brief-20260924.md@fb90ad8fe0`).
The v0.2 deliveries 100270/100272 were superseded by this bump before a stamp was placed; one review, this one.

Object read: the PRD at HEAD, which IS 118613ddb0 (`git log -1 -- <path>` = 118613ddb0; working copy clean). The brief
read at the NAMED PIN via `git show fb90ad8fe0:<path>` (290 lines), not the working copy.

## Checks run

1. **Heading denominator.** The brief at fb90ad8fe0 carries TEN territory headings, `### O0` .. `### O9`
   (`grep -c '^### O'` = 10; lines 46, 55, 63, 70, 75, 89, 98, 107, 113, 121). The PRD's BRIEF COVERAGE (118613ddb0:258-259)
   states "11 of 11 territory headings covered; 0 uncovered". Every one of the ten IS mapped (O0->FWD-1 ... O9->FWD-11,
   O6 carrying two outcomes), so coverage is complete -- but the denominator printed is not the brief's. Eleven is the
   number of OUTCOMES, or O6 counted twice; it is not a number the brief states about itself.
2. **Content carried, per heading, against the pinned bytes.** O0->THE THREAD: the account, the Global view, the four
   reads, "no export, no analysis" -- carried, and rewritten at v0.3 as the eight-hop list. O1->FWD-2/C1: who / how much /
   over what / as of when, the "About this scope" disclosure, the entitlement bookkeeping named -- carried. O2->FWD-3/C9:
   the drawer's columns, grouping by firm in Global, the retired paged combobox, type-ahead retained -- carried.
   O3->FWD-4/C2: `PageSurfaceControl`, Global (All) for the Opal user only -- carried. O4->FWD-5/C6-C8: the control row's
   presets and Net/Gross, the four headline facts with "not supplied", the AUA-Trend area chart with the four
   `ModelPortfolios.tsx` line refs, the heatmap axes, the accounts table with the uncovered row, the server-stated
   spread, the footer/popover -- carried. O5->FWD-6/C3-C5: hero card, bars + matrix, treemap + the five table columns,
   the deferred classification columns, the footer -- carried. O6->FWD-7/C10: the five steps with their contents, the
   left rail's four fields, the Details popover with the identifier list -- carried. O7->FWD-9/C12, O8->FWD-10/C13,
   O9->FWD-11/C14 -- carried. Part II -> PATHS (owned / relied-on / never) -- carried, including the extend-or-wrap rule.
   Part V -> the rules under CONTRACTS -- carried.
3. **The one heading whose SOURCE is not at the pin.** FWD-8 (118613ddb0:93-100, SOURCE "brief O6, the prospect
   paragraph (Andrew-direct ~05:4xZ)"), C11 (:214-217) and the header sentence "two addenda folded in place (... O6: a
   prospect as a first-class subject, Andrew ~05:4xZ)" (:17-18) are cut from a paragraph that DOES NOT EXIST at
   fb90ad8fe0. At that pin the word "prospect" occurs once, in Part III (:169). The O6 prospect paragraph was added by
   the NEXT commit, 5cc838e696 ("brief O6 amended (prospect = first-class subject)", :107-116 there). fb90ad8fe0 is the
   O4 area-chart addendum only. The PRD's `brief_ref` (:10) therefore names a pin one commit short of the text three of
   its own sections carry.
4. **The sequencing input the brief half states (118613ddb0:238-240)** names the served COT `display` republish as the
   L6 precondition and drops the D1 run. It does not name the Performance path, which THE THREAD's hop 6 (:168) and
   FWD-1's ACCEPT ("her year-to-date return and spread") depend on. Measured tonight from the deployed bytes
   (`org/tier1_exec/4.0.0_SA_CRO/deliverables/PERFORMANCE_TAB_END_TO_END_GAP_BRIEF_20260924.md` @d8abd7dc65): every
   performance request for the thread's own account `acc_d486fc9455d6b2aa18e13af1` answers UNAVAILABLE -- the X10
   reporting policy is PENDING_ENFORCEMENT (hop 4), no one-use plan is installed (hop 6), and the deployed success status
   still carries a member the portal refuses (hop 10). None of those is inside this PRD's write surface
   (`portal/src/pages/InvestorReporting/**`, render only). As sequenced, round 1's drain trace fails hop 6 for a cause no
   cell of this PRD can touch, and "a hop fed by a fixture fails FWD-1" forbids the workaround.

## Corrections, by pinned line (118613ddb0)

| # | line(s) | reads | should read |
|---|---|---|---|
| 1 | :10, :17-18 | `brief_ref ...@fb90ad8fe0`; "two addenda folded in place" | `@5cc838e696` -- the pin that carries BOTH addenda (O4 at fb90ad8fe0, O6 at 5cc838e696); FWD-8's and C11's source then exists at the named pin |
| 2 | :258-259 | "11 of 11 territory headings covered; 0 uncovered" | "10 of 10 territory headings (O0-O9) covered, O6 carrying two outcomes (FWD-7, FWD-8); 0 uncovered" |
| 3 | :238-240 | the L6 precondition = the served `display` republish; D1 dropped | ALSO name the Performance path's readiness for the thread's account: X10 enforcement landed and repackaged, one installed plan for `acc_d486fc9455d6b2aa18e13af1` on the default window, the reconcile carrying `entry.py` @P head (trace brief @d8abd7dc65 hops 4, 6, 10) -- or re-cut hop 6 (:168) so round 1 grades "not supplied, with the producer's reason" and leaves the live return to an enrichment round; the CTO's choice, stated in the line |

Nothing else in the brief half is contested. Corrections 1 and 2 are the review's two named checks failing at the
pin; correction 3 is a measured precondition the sequencing line omits. A v0.4 carrying the three lines is signable by
this seat on delivery; the ratified-text half is untouched by all three.

## Instruments

`git show fb90ad8fe0:docs/briefs/irpt-page-remediation-brief-20260924.md` (heading census, word census "prospect");
`git show 5cc838e696:...` (positive control: the paragraph is there, :107-116); `git log -- docs/briefs/...` (the two
addenda are two commits, 00:46 and 00:47 local); `git log -1 -- <PRD>` = 118613ddb0; `python .tools/prd-signoff.py status
DSGN_IRPTV1`; the Performance trace brief @d8abd7dc65 for correction 3.
