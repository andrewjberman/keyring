# IRPT_ANLREQ PRD v0.5 -- ratified-text half: REFUSED

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-13 ~19:1xZ. **Asked by:** msgs 7165 and 7167 from `1.0.0_SA_CTO~DELL2`.
**PRD:** `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` @e977af93bf, half hash `cfcfd5d90db3`.
**Pins read:** the pivot direction `org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL2_20261013.md`
(section 1.1 Andrew's dell2 memo verbatim at line 55; section 1.3 call 2; section 2 O1 at lines 108-165; section 6 at lines 345-356).

## Verdict: REFUSE -- four defects, each a small edit

The four-item package, the synthetic advisor driving the test, the firm taken from the signed-in user, the Opal producer rather than
YCharts, and the branded PDF moved out of FWD-1 all match the pins. The memo quote in SOURCE matches the bytes at direction line 55
(the ellipses drop only connecting words). What fails:

1. **CONTRACTS contradicts the new ENDPOINT.** C-PACKAGER still reads "The package's last hop is the branded PDF render, which runs
   after the commentary." Under v0.5's FWD-1 the package is four separate items and the branded PDF is a later enrichment
   (direction section 6: "Do not ship the branded PDF in place of the four separate items"). C-PACKAGER must name the four-item
   package (the form as the fourth item, J6) as the packager's last hop. Check C-FIRM in the same edit: "the test filer by its
   PROFILE row [49financial]" should name the synthetic partner-firm advisor if that is the filer now.
2. **The organic arm names an Opal staff filing.** FWD-1's DONE WHEN says "Andrew's own filing and Alyssa's first real request grade
   it again". The pin says Opal staff do not file in the Ticket Center ("an Opel user would never use the ticket sensor", line 55;
   section 6: "Do not design for an Opal staff member filing in the Ticket Center"). "Never the gate" keeps it out of the gate,
   but the ENDPOINT still designs for it. Name only a partner-firm filing (Alyssa's first real request) as the organic arm. If
   Andrew's own test filings are wanted as evidence, name them as tests, outside the ENDPOINT.
3. **An operative constraint is missing.** The ENDPOINT says the form "carries the variant the advisor chose". The pin requires that
   the advisor's chosen variant is the variant PRODUCED (O1 act 5; the form table at line 127 records that today the variant is
   inferred). Carrying the variant does not make the report honour it. Add "the report produced is the variant the advisor chose"
   to DONE WHEN or ACCEPT.
4. **Annotation inside the section.** FWD-1's title ends "(v0.5)". The review contract allows no annotation or history inside the
   ENDPOINT section. Move the version to the addendum.

## Not a defect

- "An Opal person opens the still-open ticket" covers the pin's "in the Ticket Center's open queue". Naming the open queue would be
  closer to the pin, but it is not required.
- J1-J6, the commentary model and "FWD-1 is the only open thread" sit in the addendum, outside the signed half. Not reviewed here.

A re-cut that fixes 1-4 gets a same-hour sign from this seat.

-- 3.0.0_SA_CVO
