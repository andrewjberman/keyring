# /endpoint --forward -- one canonical per-security table for every holdings surface

**Phase 0, greenfield.** Emitted 2026-09-29 ~19:1xZ by `1.0.0_SA_CTO`, at L2 of the project the CTO placed as part (c)
(`CTO_PLACEMENT_20260929_182xZ_ONE_CANONICAL_SECURITY_TABLE.md` @c3c3f414dc).

**Inputs read, whole:**
- `docs/briefs/canonical-security-table-brief-20260929.md` @be6ef31a65 (blob 1e0a2b99f4), 231 lines, author `4.0.0_SA_CRO`.
- The same brief's working-tree addendum, O7 and O8 (from Andrew's UI walk 2 of 2026-09-29). It was uncommitted when
  read at 19:05Z. Source: "CRO 102981, brief addendum pending". Its commit is to be cited at L4.
- Andrew's words, `org/tier1_exec/2.0.0_SA_COO~D/deliverables/ANDREW_DIRECT_20260929_175xZ_ONE_CANONICAL_SECURITY_TABLE_FOR_ALL_HOLDINGS.md`
  @099316efdd.

**NOT READ, deliberately:** the task-order register, any project JSON, the live tables, and the deployed Lambda bytes.
No project exists yet, and every live value cited in the brief is ~D's trace, not this seat's read.

**The tag is `DONE WHEN`:** the bar an outcome must reach, never its current state. `FWD-n` ids are permanent. A new
outcome takes the next unused number, a retired one leaves its number vacant, and no number is ever reused. **No
outcome is a wait.** Each names an act a seat can take on demand. The one act reserved to Andrew, the deletion in
FWD-5, is qualified there.

**Where this lands:** the section `ENDPOINT (step 2, /endpoint --forward)` of the project's PRD at L4. The project code
and directive are set at L3, which has not run. **NOT YET LANDED in a PRD.** Andrew confirms the DONE WHEN lines below.

---

## 1. The outcomes

  FWD-1  An advisor opens a Black Diamond client's holdings and sees each security's class and
         sub-class exactly as Opal's one shared list holds it, on the live Black Diamond outputs
         DONE WHEN  EXERCISED -- one live run of the Black Diamond chain for the latest day, traced
                    from the shared list to the page the advisor reads
         ACCEPT     for a real Black Diamond client, gold funds such as GLD and PHYS read as
                    commodities and VXX reads as a hedge, the same as Positioning shows them; the
                    trace shows every class on that page came from the one shared list, and the old
                    Black Diamond copy of the list was never consulted at any step
         SOURCE     brief O1 (l.33-41), "The candidate thread"

  FWD-2  Anyone who asks "what class is this security in Opal's holdings?" gets one answer,
         whichever screen or report they look at
         DONE WHEN  EXERCISED -- a set of securities checked across every holdings screen and report
         ACCEPT     a chosen handful of securities (at least one fund, one gold fund, VXX, and one that
                    is on no list) shows the same class and sub-class on Investor Reporting, Positioning,
                    each firm's reports, the 49F data, the partner feed, the market overview and the
                    attribution view; a security with no entry is shown as unclassified by name, never
                    quietly put into some class
         SOURCE     brief O2 (l.43-48)

  FWD-3  A person corrects or adds a security in one place, and every screen shows the change
         after its next ordinary run
         DONE WHEN  EXERCISED -- one real correction or addition made on demand, and read on every
                    screen after its next run
         ACCEPT     one security is added or corrected in the one place; nobody edits a second file or
                    list; after each screen's next run the new class shows everywhere FWD-2 names, and
                    nowhere still shows the old one
         SOURCE     brief O3 (l.50-54)

  FWD-4  Anyone can prove there is no second definition of a security's class left anywhere in
         Opal's code
         DONE WHEN  EXERCISED -- the repeatable check run on demand and read at each round's close
         ACCEPT     a check anyone can rerun lists every place in the code that assigns a class to a
                    security outside the one shared list, and says how many places it looked at; at the
                    end it lists none, and when an old copy is deliberately put back as a test, the
                    check finds it
         SOURCE     brief O4 (l.56-60); Part IV.4 (the existing one-definition pattern)

  FWD-5  The old Black Diamond copy of the list is gone, and it can be shown that nothing needed it
         DONE WHEN  EXERCISED -- the copy deleted on Andrew's confirmation, after the check reads
                    that nothing uses it. That confirmation is Andrew's act for a destructive,
                    unrecoverable step, and it is asked for the moment the check reads zero.
         ACCEPT     before the deletion, the FWD-4 check and the list of who is allowed to read the old
                    copy both show no remaining user; every figure that moved when its last users were
                    switched was listed before and read after; the old values are kept on record, so a
                    disputed figure can still be traced
         SOURCE     brief O5 (l.62-66); Part V (l.179-181)

  FWD-6  Where a screen must classify from a different authority, that is written down, and a reader
         can tell which rule a security follows
         DONE WHEN  EXERCISED -- a reader looks up securities on the screens that follow another
                    authority and can say, for each, which rule applied and who owns it
         ACCEPT     each declared exception names its owner and its reason; a reader of Positioning's
                    ETF view or the Schwab firm data can tell a class that came from the shared list
                    from one that came from the declared exception; the old quiet rules such as "treat
                    hedges as alternatives" or "VXX is equity" are gone, not declared
         SOURCE     brief O6 (l.68-73); section 2 below (the CTO's decision)

  FWD-7  A security that newly appears in any firm's daily holdings gets its entry in the shared
         list on a regular schedule, before anyone has to notice it
         DONE WHEN  EXERCISED -- the scheduled classification fired on demand against a day that holds
                    a security with no entry. The ordinary scheduled run that follows is the check that
                    it keeps working, and a one-off catch-up run is test evidence only.
         ACCEPT     on a day holding a security that no list covers, the scheduled step adds its class
                    and sub-class without a person starting it by hand; no screen shows that security as
                    "Other" or unclassified for longer than the schedule's own gap; where the step asks
                    an outside model for the classification, that use has Andrew's word, never a default
         SOURCE     brief addendum O7 (CRO 102981, brief addendum pending); Andrew, walk 2 of 2026-09-29
                    ("structure a continuous pipeline as new securities become apparent")

  FWD-8  The shared list says whether each security is a fund or an individual stock, and a holdings
         table uses that to place individual stocks after the funds
         DONE WHEN  EXERCISED -- one real client's holdings, with both funds and individual stocks, read
                    on the page
         ACCEPT     each entry in the shared list says fund or individual stock; for a client holding both,
                    the holdings table shows the funds by their classes first and the individual stocks
                    after them, and nothing but the shared list decides which is which
         SOURCE     brief addendum O8 (CRO 102981, brief addendum pending); Andrew, walk 2 of 2026-09-29
                    ("individual securities should be marked as such ... a field in that DynamoDB table")

## 2. Decision the brief left to the CTO: the Bloomberg and Schwab authorities (brief Part II l.97-98, Part VII l.210-211)

**Neither joins the canonical table as an authority for class or sub-class. Both are DECLARED DEPARTURES under FWD-6,
each with an owner and a reason.**
- Positioning's ETF view keeps Bloomberg GICS, owned by the Bloomberg-side projects (ETFS_CANON / ETFS_POSITIONING).
- The Schwab firm composition keeps Schwab as its security master, owned by its pipeline.
- Either may be read as an INPUT to FWD-7's scheduled classification, including FWD-8's fund-or-stock marker; the
  canonical row stays the one answer.

**Reason:** they answer different questions: Bloomberg GICS answers sector, and Schwab answers custodial identity. A
second writer of Opal's own asset-class taxonomy is exactly the multi-writer drift this project removes (brief Part IV.2:
three values of VXX across three writers).

## 3. Placement notes carried to L3/L4 (not outcomes)

- **Boundary:** cells (a)+(b) (IRPT_BCKEND ~M) and the portal display order (DSGN_IRPTV1 ~D) are not this project's. They
  are named as relied-on work, per brief Part II.
- **FWD-8's shape:** FWD-8 adds a field to the table. The brief's Part II assigns a table-shape change to POSN_ASTTAX's
  successor, while the addendum O8 says "the FIELD is this project's". This endpoint takes the addendum's reading, the
  later and Andrew-sourced one. L3 names the field's owner explicitly, so the two texts do not both stand.
- **Rule 30:** no new resource name or address is typed here. If FWD-7's scheduled path needs a new function, schedule
  or role, the PRD takes its names from `lib/opal_naming.py` builder output.
- Every copy's replacement is a served move under never-widen halves, with a before/after read per surface (brief Part
  IV.6). This is carried as law, not as an outcome.
