# ANDREW-DIRECT — CTO oversight of 4.0.0 + 3.0.0 for ground-up SSOT on mdpf + advi (bd/inf/cot)

**Channel:** Andrew-direct at the 1.0.0_SA_CTO terminal, 2026-08-11 ~0535Z (mid-turn message).
**Recorded by:** 1.0.0_SA_CTO, same turn. **Broadcast:** COO + MSTR + the three addressed working
seats (4.0.0_SA_CRO, 4.0.0_SA_CRO~A, 3.0.0_SA_CVO), same turn.

## VERBATIM (the phrasing IS the ruling)

> "I want you to oversee the 4.0.0_SA_CRO Base and ~A agents as well as CVO to essentially get all
> the information you need on the mdpf and advi pipelines (bd-pipeline, inf-pipeline, cot-pipeline)
> so we can figure out what needs to happen to get this all consolidated, colocated, morning
> trigger pattern, everything all wrapped up nice with a bow. I want a pattern that always is
> effectively this: ingestion into the relevant opal-data-assets/{vendor}/{firm}/bronze or however
> we have it set up, then theres an event trigger that processes that raw data into silver
> parquets. then there is a gold staging layer or full gold in
> opal-data-assets/portal/gold/{mdpf or advi}/{scope aka global or firm} with the relevant code,
> tables, and all other dependencies colocated. Then this data gets pulled over by some publisher
> to the relevant firm bucket in opal-data-portal-v2, specifically
> opal-data-portal-v2/platinum/{mdpf or advi}/{scope aka global or firm}. Something like that. I
> want to use the same patterns and clean up the rest, so that we can have this established
> forever and never have all these complex, ad hoc, haphazard routes. There is a lot of work here,
> because it covers reconaiisance, design, implementation, migrating, repointing, reallocating and
> spinning up and tearing down resource, repointing portal, there is A LOT to do here, and that is
> why i want you to really get as much information as possible from the 4.0.0 and 3.0.0 agents and
> really adversarially establish SSOT from the ground up."

## SCOPE READ (addressed seat only; no wider gate manufactured)

- **Addressed:** 1.0.0_SA_CTO. The oversight of CRO base + CRO~A + CVO for this program is
  Andrew-authorized, at this seat.
- **What it adds to the standing program** (handoff @1a518b303f + spec @3272f3c4b0..@1d3875cc45):
  1. The **event-trigger bronze→silver leg** is now explicit in the pattern (raw landing FIRES
     silver processing), alongside the **morning trigger pattern** end-to-end.
  2. The recon phase is scoped to **mdpf + advi across ALL THREE firm pipelines (bd/inf/cot)** —
     not mdpf-first-advi-later.
  3. The SSOT is to be established **ADVERSARIALLY, from the ground up** — CVO cross-examines,
     never rubber-stamps; records are not trusted (6 of 10 were false on the last measured run).
  4. "Something like that" — the grammar's fine detail remains CTO's to draft and his to ratify;
     the DIRECTION is ruled.
- **NOT changed:** the must-calculate exception-set question (still open at Andrew); the CVO cert
  gate on the mdpf cutover's live-chain acts; migrate-before-kill; no-shadow-channels; the
  moratorium (a trigger is a route, not a monitor).
