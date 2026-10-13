# ANDREW DIRECT -- vendor-agnostic serving: one Opal Shape in gold (2026-10-13 ~18:2xZ)

**Channel:** Andrew, at the dell2 terminal, in the session of `1.0.0_SA_CTO~DELL2`, answering the three smoke findings on a 49 Financial
SmartX-model account. The Holdings page shows "Held at the model's target, not position-level ... not broken down by asset class",
while its rows list the target mix by class. **Verbatim:**

> 1.) Good. 2.) Yeah we have all that information presenting in the below rows so there should be an easy enough way to present that in one simple mechanism regardless what data vendor it is sourced from. I say this because we should not have overly opinionated processes, we want to design to be as vendor-agnostic as possible, especially because we are doing the bulk of the work anyway. The vendors should merely be data providers, generally we want to own the serving process through our shapes rather than making differnet responses/structures. It is better to make an "Opal Shape" for anything that is served, that is the purpose of a "Gold" layer in the buckets. Do you understand? 3.) Good

The items he answers:
1. YTD measured from the first day of data, labelled with it.
2. The class breakdown.
3. The ticker reads CASH.

## What it binds (this seat's reading)

- **The breakdown is ONE mechanism over the served rows.** It sums the rows' own class values, whatever produced them: a position,
  a model's target mix, or any vendor. There is no vendor- or holding-kind special case. The earlier ruling "computed from the model's
  target weights" is replaced by this.
- **The principle:** everything served has one Opal Shape, and the gold layer is where vendor data becomes it. Vendors are data
  providers only. A reader never branches on which vendor fed a served object. A new vendor means a new mapping into the shape,
  never a new response structure.
- It binds new work from now on. An existing vendor-shaped serve reaches the shape through its own project's next enrichment, not as
  a rider (the R19 pattern).

-- recorded by 1.0.0_SA_CTO~DELL2
