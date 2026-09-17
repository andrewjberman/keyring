# /endpoint --forward -- NFRA_MCPINDEX (the Opal MCP tool index: every data property answerable in Claude, from one catalog)

**Phase 0, greenfield.** Emitted 2026-09-17 ~18:1xZ by `1.0.0_SA_CTO` on `4.0.0_SA_CRO`'s L1 handoff (97622), which carries
Andrew's words of 2026-09-17 verbatim, including his five card answers (LGIC naming; versioned in S3; D9; Opal staff only,
beta one at a time; portal reads precomputed tables, silver queried live).

**Brief read:** `docs/briefs/opal-mcp-tool-index-brief-20260917.md` @826ac6925a, author `4.0.0_SA_CRO`, 216 lines, read whole.
Part I carries ten outcomes O1-O10; Part IV nine substrate findings; Part V nine preconditions; Part VII six non-claims.

**NOT READ, deliberately:** the register, any task order, any project JSON. Phase 0 reads the brief and nothing else.

**The tag is `DONE WHEN` -- the BAR the outcome must reach, never a current state.** `FWD-n` ids are permanent: a new outcome
takes the next unused number; a retired one leaves its number vacant. **No outcome here is a WAIT:** each names an act a seat
can take on demand, and where a precondition sits in another project, the outcome's proof is run against the part this project
owns (the index) with the other part stubbed or carded, never held.

---

  FWD-1  A staff member who does not know which system holds a fact asks Claude and is
         pointed to the right tool, with the data's freshness and scope, on the first try
         DONE WHEN  EXERCISED -- a set of real questions, asked cold by someone who did not
                    build the index, routes correctly
         ACCEPT     a discover family is loaded in every session and answers from ONE catalog
                    (never a second): which property and dataset holds the fact, its freshness,
                    its firm scope, its caveats, and the next tool to call; a question about a
                    property that is not catalogued says so and names nothing
         PROOF      a named question set run in a live session by a non-author, with the count
                    routed correctly over the count asked, and every wrong route listed
         SOURCE     brief O1; Part III bullet 1; Part IV.1-2

  FWD-2  For any figure the portal displays, Claude returns the portal's own number with the
         same as-of date
         DONE WHEN  EXERCISED -- a side-by-side read on live data, per surface
         ACCEPT     the tools read the SAME precomputed tables the portal points at; for each
                    surface in scope (model AUM and account distribution, ETF positioning,
                    market and macro, advisor intelligence) the figure and the as-of date match
                    the portal exactly; a disagreement is this project's defect, never a caveat
         PROOF      one comparison per surface, each naming the portal page, the tool call and
                    both values; zero disagreements, denominators printed
         SOURCE     brief O2; Part III bullet 2; his answer 5; Part IV.5

  FWD-3  A staff member asks about positions, balances and transactions at either Schwab
         master and gets an answer from silver, without opening the custodian's site
         DONE WHEN  EXERCISED -- a granted person asks and reads the answer
         ACCEPT     one master and one date per answer, never summed across masters; the
                    answer states its date and completeness; transactions are reachable, not
                    only the three `dim_*` tables
         PROOF      a live session transcript for each question class, with the row counts
                    reproduced from the same silver objects by a second instrument
         SOURCE     brief O3; Part IV.3; Part V.5 names NFRA_OPLGTW's enablement as the
                    precondition -- this project proves its own half against the built tools,
                    and the enablement is that project's act

  FWD-4  The same question classes work for Black Diamond, Orion, Eclipse and SmartX
         DONE WHEN  EXERCISED -- per property, on that property's real silver tables
         ACCEPT     each property was ANALYSED first (its common questions written down) and
                    its purpose-built tools cut from that analysis; each answer states date,
                    scope and completeness; a property with no analysis ships no tool
         PROOF      per property: the analysis record, the tool list it produced, and a live
                    answer per tool class with its denominators
         SOURCE     brief O4; Part III bullet 3; Part V.2

  FWD-5  A staff member asks about the ETFs -- holdings, net assets, daily NAV -- per fund
         DONE WHEN  EXERCISED -- per fund, against the served tables
         ACCEPT     the same ladder as FWD-4, per fund (TrueShares, Pathfinder); NAV and net
                    assets carry their date; a fund with no data for a date says so
         PROOF      one live answer per fund per question class, compared with the served
                    artifact
         SOURCE     brief O5

  FWD-6  A question that fits no purpose-built tool still gets a safe answer, and the index
         never sends Claude to that path for a common question
         DONE WHEN  EXERCISED -- both halves: the fallback answers, and the routing prefers
                    the purpose-built tool
         ACCEPT     a TYPED query (filters, group-bys, aggregates as a structured object,
                    never raw SQL) over any catalogued dataset, with hard caps and a response
                    stating date, completeness and whether it was cut short; for the routing
                    half, a named set of common questions reaches its purpose-built tool
                    without being told to
         PROOF      the typed-query transcript including a refused unsafe shape and a
                    cut-short response; the routing count over the same question set as FWD-1
         SOURCE     brief O6; Part III bullets 4-5; Part IV.3

  FWD-7  A staff member asks for one client or household and sees them across custodian and
         platform
         DONE WHEN  EXERCISED -- one real client answered across at least two systems
         ACCEPT     the match is made by a stated rule, and every unmatched record is REPORTED
                    rather than dropped; an answer never merges two people; the rule's
                    precision and recall are printed on a named sample
         PROOF      one client's cross-system answer with the match rule, the sample's
                    precision and recall, and the unmatched list
         SOURCE     brief O7; Part IV.8 (entity resolution is parked) and Part V.6 -- this
                    project cuts the matching rule it needs or cards the gap; it does not wait
                    on a parked project

  FWD-8  A staff member asks for long history or live market data and gets it on demand
         DONE WHEN  EXERCISED -- one long-history answer and one market-data answer
         ACCEPT     the long-history path returns a bounded answer over a span the Gateway's
                    in-process engine cannot hold, and says which substrate served it; the
                    vendor reads (YCharts; Bloomberg where its own standing word allows)
                    appear in the SAME index rather than as a separate world; no new vendor
                    egress beyond Andrew's standing per-use word
         PROOF      one answer per half with its substrate named and its cost/time recorded
         SOURCE     brief O8; Part IV.7 (no Glue or Athena today); Part V.7

  FWD-9  Andrew admits staff to the beta one person at a time, and each person sees only the
         tools and data he granted
         DONE WHEN  EXERCISED -- one admission and one removal, both observed
         ACCEPT     a person not admitted sees NO data tools; an admitted person sees exactly
                    their granted set, and a phrasing that asks for another firm's or master's
                    data is refused; removal takes effect without a redeploy
         PROOF      two sessions (admitted, not admitted) with the tool lists each sees, one
                    refusal transcript, and the roster change with its timestamp
         SOURCE     brief O9; his answer 4; Part V.9

 FWD-10  Adding the next property or tool is one catalog entry plus a tool, and the index
         describes it with nobody writing the description twice
         DONE WHEN  EXERCISED -- the NEXT property after the first three is added this way and
                    the addition is timed
         ACCEPT     the catalog entry (business meaning, example questions, grain, freshness
                    field, firm-scope rule, never-sum rules, producer, tools) is what Claude
                    reads; a tool with no catalog entry or no safety classification DOES NOT
                    SHIP -- proven by a planted unclassified tool being refused; the catalog is
                    versioned in S3 at a builder-named address and has ONE writer
         PROOF      the added property's diff (catalog entry + tool, nothing else), the refusal
                    of the planted unclassified tool, and the elapsed time
         SOURCE     brief O10; his answers 1-2; Part IV.9 (the live `read_teams_attachment`
                    defect is this failure already in production); Part V.4

---

## What this endpoint does NOT carry

1. **Enabling the Schwab tools in deployment** is `NFRA_OPLGTW`'s act (brief Part II). FWD-3 proves the index half.
2. **The admin screen that grants access** belongs to the mcportal brief; FWD-9's proof uses the operator command until it exists.
3. **New precomputed tables** -- none are asked for; the portal's exist and silver is queried live (his answer 5).
4. **Partner or client access** -- zero, under his standing 2026-08-20 ruling.
5. **Tax SMA tools** -- excluded until D9's tax work lands.

## The one call this seat owes at L4

`NAMING_SCHEMA.json` v1.10 does not grade MCP tool names (brief Part IV.4). The brief reads Andrew's answer as
`{system}_{function}[_{qualifier}]`, system from `infra/logic/registry/systems.json`, scope always an explicit argument
validated against `scopes.json`, and the cross-property discover tools under a reserved `opal` system. **Whether that becomes a
GRADED part of the schema is this seat's schema-bump call at L4**, ratified through LGIC_NAMING's schema, never as a rider on
LGIC_ENFORCE. The PRD states the rule either way; grading it is the bump.

## Next

Andrew's DONE WHEN confirmation on FWD-1..FWD-10 (the spine makes that his), then L4 (the PRD) at this seat.
