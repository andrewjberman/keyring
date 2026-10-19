# L4-R review, NFRA_MCPINDEX PRD v0.19 addendum, ratified-text half -- REFUSE, three cures (3.0.0_SA_CVO~Z, 2026-10-19 ~16:4xZ)

**Asked by** `1.0.0_SA_CTO~Z`, msg 36005, acked.

**Bytes reviewed:** `git diff 4b8dcf3b86 f59634ebe3` on the PRD, the v0.19 addendum, read whole. The PRD at HEAD equals
the pin.

## Sources read

- **Andrew-direct ~16:2xZ, record @634d368d98** (`4.0.0_SA_CRO~Z`). The addendum's quotation is his words from the second
  sentence on, exactly. The dropped first sentence ("I need you to look into the gateway page on the MCPORTAL") addresses
  the CRO and moves no outcome.
- **What `bucket_source` is:** `workflows/atom_decomposition/tool_index/members.yaml:20-22` and
  `emit_catalog_v02.py:1341-1342` and `:1508-1522`.
  - It is a `<path>:<line>` CITATION declared in the index. It is not read from the tool's code.
  - It exists only on index members that no catalog row names. It appears 64 times in `members.yaml`.
  - Its check is that the line exists and the bucket name appears within `BUCKET_SOURCE_WINDOW = 6` lines of it.
- **C-GROUP item 2 AMENDED** (PRD `:772-777`): a `client_*` tool serves many (vendor, firm) pairs, and /gateway lists a tool
  under EVERY pair in its `serves`.
  - So a multi-vendor tool shown under a Schwab sub-segment carries links to rows of other vendors by design.
  - That is the likeliest explanation of what Andrew saw, and it is unmeasured here.

## What is right

- His two asks are carried. "Works" lands on FWD-24 and "routed to the right location" lands on FWD-23 and FWD-24.
- The order is his: opal-data-assets first.
- The planted wrong link is a real negative arm.
- `misrouted` as a FAIL class is the right placement.
- One tester and no parallel comparator.

## Verdict: REFUSE

There are three cures, all text-only.

### V1 (blocking): "the right location" has no oracle for intent, and "the one the tool's code reads" is singular

ROUTED compares an index link with what the code reads. FWD-24's routing check compares the answer with the linked row.
Both are anchored on the tool's code.

- **A wrong read passes both arms.** If a Schwab tool's code reads a Black Diamond location, its link to that row reads
  ROUTED and its answer matches the row. That is the defect Andrew is asking about, and the outcome as written cannot see
  it.
- **"The one" source mis-grades multi-source tools.** Per C-GROUP, a `client_*` tool's code dispatches across vendors, so
  a singular source marks its legitimate links of other vendors MISROUTED.
- **The defect has three places it can sit, and the verdict names one.** It can be the index link, the tool's code, or
  the page's display (a multi-vendor tool listed under a sub-segment with indexes for every pair).

**Cure.**
- ROUTED is graded per (tool, linked row) pair, against the SET of sources the tool's code can read. Each dispatch branch
  is cited `<path>:<line>`.
- Add the intent check: the code's source set agrees with the tool's DECLARED scope. That scope is its `serves`, its
  integration spec and its registered description, never its name. A disagreement is MISROUTED (code), a defect cell in
  NFRA_OPLGTW.
- The routing table's defect class is one of: `link`, an NFRA_MCPINDEX row; `code`, NFRA_OPLGTW; or `display`, the
  /gateway grouping under C-GROUP, which belongs to NFRA_MCPORTAL and this PRD.
- Andrew's Black Diamond-on-Schwab case is classified in that table first, by measurement.

### V2 (blocking): FWD-24's routed PASS has no rule for a response that carries no source or as-of field

"The response's own source or as-of fields match the row" cannot be read on a tool whose answer has neither. Such a tool
reads PASS without the routing evidence, which overclaims, or FAIL with no defect, which is false. The verdict set is not
MECE over what the battery can observe (rule 24 (i)).

**Cure.** Where the response carries no source field, routing is proven by that tool's FWD-23 routing-table row, which
cites the code. The battery's record for that tool says `route: code-cited` instead of `route: response-cited`. A
response field that names a different source is `misrouted`.

### V3 (blocking): the routing proof must be re-runnable, and its code source misnamed

**The proof must be re-runnable.**
- FWD-23 has to be re-proven after each fix. A one-off research audit cannot be that proof ("no FWD is a wait: each is
  proven by an act a seat runs on demand").
- The CRO's read-only audit is good evidence, and it is the seed of the defect rows.
- The routing table itself must be EMITTED by a committed, re-runnable script. That is the emitter, or a sibling of the
  battery, and it is not a second tester.

**The code source is misnamed.**
- "Read from the code (`bucket_source` and the row's key)" names an INDEX field as the code. It exists only on members
  that no catalog row names, and it is checked by 6-line proximity, not by a read of what the code fetches.
- The text names the instrument that reads the code (a trace of the tool's read path) and treats `bucket_source` as a
  claim to be checked against it, never as the oracle.

## Not graded here

- The decomposition and round 22's cells.
- CRO~Z's explanation itself, which is a research deliverable.

-- 3.0.0_SA_CVO~Z
