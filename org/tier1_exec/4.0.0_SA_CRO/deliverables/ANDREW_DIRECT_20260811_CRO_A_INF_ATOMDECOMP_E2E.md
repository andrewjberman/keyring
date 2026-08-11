# ANDREW-DIRECT — 4.0.0_SA_CRO~A: atom_decomp on opal-data-inf + inf-pipeline, fix end to end

**Channel:** Andrew-direct at the `4.0.0_SA_CRO~A` terminal (session message, 2026-08-11 ~0410Z)
**Recorded by:** `4.0.0_SA_CRO~A`, same turn, per the RECORD+BROADCAST law (org/XXX.md).
**Broadcast:** MCP to `1.0.0_SA_CTO` + `2.0.0_SA_COO` + `0.0.0_AB_MSTR`, same turn.

## Verbatim

> "I want you to run atom_decomp on the entire opal-data-inf and inf-pipeline with the intention of
> figuring out why its stopped and fixing it end to end. look at this as a test for atom_decomp"

## Scope as bound (his words, no widening)

- **Target:** the entire `opal-data-inf` bucket + the inf-pipeline (the Inflection firm pipeline).
- **Intent:** figure out why it is STOPPED, and FIX it end to end — diagnosis AND remedy are both
  in-scope for this seat, by his word.
- **Frame:** an explicit TEST of the atom_decomp workflow — the method's performance is itself a
  deliverable.

## Overlap surfaced, not adjudicated

The standing open subject "INF spine freeze: INF_B_00 canonical frozen since 08-01, D-chain since
07-31; routing question (CTO+DS owner chain) awaiting his word" (FABRIC_STATE open subjects) appears
to be answered BY this instruction for the doing-of-the-work; whether it closes that routing
question fabric-wide is for MSTR/CTO to read, not me. MDPF-side W1/W2 (inflection label fix +
cross-firm unlink, in tonight's atomic window) are the CONSUMER face of this pipeline — coordination
with the live window owners honored; nothing here gates them.

## Instruction 2 — mid-run addition (same terminal, ~0450Z)

> "something else i want you to kepe in mind when you do this, is that we need to refactor the inf
> pipeline, because the way we do performance attribution is fucking bullshit, performance is not a
> residual, there are clear performance endpoints at the account level in orion and we need to use
> them, i want that fixed real bad it should be raw figures straight dfrom their database. when you
> run this analysis i want you to keep a close eye on the various gold scripts and what theyre doing
> because a lot of it probably is trash, explicitly any account valuation (shouldnt be necessary
> there are clear raw holdings/assets/etc endpoints no calculation or interpolation required) and
> same with performance. we even have a whole orion eclipse endpoints api file somewhere and you
> have egress to check out any endpoint you want."

**Scope as bound:** (a) the INF pipeline needs a REFACTOR — performance from Orion's account-level
performance endpoints as RAW figures, never a residual/derivation; (b) during this analysis, AUDIT
the gold scripts — explicit attention to account-VALUATION logic (should not exist; raw
holdings/assets endpoints suffice, no calculation or interpolation) and PERFORMANCE logic (same);
(c) an Orion/Eclipse endpoints API file exists in the estate — locate and use it; (d) **vendor
egress GRANTED for this run's endpoint verification** ("you have egress to check out any endpoint
you want") — Orion/Eclipse endpoint exploration is his word, per-use satisfied.

## Instruction 3 — the 49F archetype run (same terminal, ~0535Z)

> "I also want you to do an atom_decomp run on 49 Financial Gold Analytics runner.  we need to
> figure out how to get the advisor intelligence canonized. What I wanted to accomplish was using
> the 49/Schwab 0833 account as a base to create the perfect gold analytics runner then use that as
> the archetype for inflection and cottonwood, essentially hitting whatever endpoints need to be
> hit in order to replicate that shape. that is why the 49 case is such a good one to use as a
> baseline because we have complete fact tables. from there it is easy enough to reverse engineer
> field for field what we need for the others."

**Scope as bound:** (a) a SECOND atom_decomp run, target = the 49 Financial gold analytics runner;
(b) purpose = CANONIZE Advisor Intelligence: the 49F/Schwab **08335338** account (his "0833" —
full 8-digit per the standing two-bucket law; this is the ADVI bucket, NOT 08242234/MDPF) is the
BASE from which the perfect gold analytics runner is created; (c) that runner becomes the
ARCHETYPE for inflection and cottonwood — each firm hits whatever endpoints are needed to
replicate the SHAPE; (d) the 49F case is the baseline BECAUSE its fact tables are complete —
reverse-engineer field-for-field what the others need.

## Execution notes (this seat)

- Fixes ride the sanctioned mechanisms only: Terraform via `safe-apply`, commits via `safe-commit`,
  deploys per the deployment rules; ORION + ECLIPSE vendor egress are on the LIFTED standing list if
  re-pulls are needed.
- Proof bar inherited from the estate's own standard: mechanism at source, remedy landed, the
  SCHEDULED cycle emits (ad-hoc runs are QA, never production evidence) — the honest residual on an
  unattended-cycle proof will be stated, not claimed.
