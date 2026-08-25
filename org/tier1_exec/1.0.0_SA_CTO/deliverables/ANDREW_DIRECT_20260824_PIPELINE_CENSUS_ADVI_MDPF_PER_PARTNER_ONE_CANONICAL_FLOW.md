# ANDREW-DIRECT 2026-08-24 ~19:2xZ (base CTO terminal) -- a SEPARATE PROJECT: identify the pipelines, data flows, code locations and data locations for ADVI per partner AND for MDPF per partner; quantitatively assess + verify each; once ground truth is established, propose a REMEDIATION per pipeline toward ONE canonical structure and flow -- all paths in pattern, unified. Trigger concern: Cottonwood MDPF scripts "allegedly" in opal-data-mdpf while every other tree colocates scripts in opal-data-assets

**Recorded by:** `1.0.0_SA_CTO` (addressed seat) - **archetype:** SCRIBE / COORDINATE
**Context:** "one final pass" of the PRD round -- scripting / data ops. Quoted exactly as typed.

## VERBATIM

> "Finally, there should likely be one final pass worked out here that covers scripting/data ops. Something that concerns
> me about Cottonwood is that for mdpf, they have scripts "allegedly" located in opal-data-mdpf whereas all the others have
> scripts colocated in the relevant opal-data-assets bucket location. I want to make sure that there is a separate project
> registered the purpose of which is to identify the pipelines, data flows, code locations, data locations, etc for the
> advisor intelligence (advi) pipeline per partner, as well as for the model portfolios (mdpf) pipeline per partner. The
> purpose of this project will be to quantitatively assess and verify these various pipelines and once ground truth is
> established for each, propose a "remediation" for each the purpose of which is one canonical structure and flow so that
> all paths are in pattern and unified on that basis."

## WHAT IT BINDS (surfaced, unwidened)

1. **A SEPARATE PROJECT, registered** (his word "make sure that there is a separate project registered"). Purpose, in his
   two halves: **(a) IDENTIFY** -- the pipelines, data flows, code locations, data locations "etc" for the **ADVI pipeline
   per partner** (49 Financial, Inflection, Cottonwood) and the **MDPF pipeline per partner**; **(b) quantitatively ASSESS
   and VERIFY** each -- ground truth per pipeline, measured (Rule 22a: deployed bytes vs built-from, applied vs desired;
   `comp-pipescript deployed` per tree; the estate's own census tools).
2. **THEN a REMEDIATION per pipeline**, proposed (not executed by this project) -- toward **ONE canonical structure and
   flow** so that all paths are in pattern (Rule 17b: `{vendor}/{firm}/{medallion}` under `opal-data-assets`; platinum
   serving under `opal-data-portal-v2`; the S3-code standard for scripts) and unified on that basis.
3. **The trigger fact to measure first:** Cottonwood MDPF scripts "allegedly" located in `opal-data-mdpf` while the other
   trees colocate scripts in the relevant `opal-data-assets` location -- a code-home divergence (Rule 22a's two-homes
   class; the `safe-deploy` PIPELINE_MAP is the desired-state instrument, the live bucket listing the applied one).
4. **Scope discipline:** census + verification + PROPOSAL. Every remediation is its own decomp/TO on his word;
   NEVER#3 (served output never moves without never-widen sign-off) and NEVER#2 (no cross-firm references) bind every
   proposal; "in pattern" is judged against the ratified canonical form (Rule 17b + the 08-11 gold/platinum amendment),
   not against the majority of what exists.
5. **Relation to prior work (rung 2, to be cited not rebuilt):** `comp-estate` threads (advi-bd / advi-inf / advi-cot /
   smartx / canonical-schwab), `comp-pipescript deployed` (all-trees, firm-separated), NFRA_DEPLOYCENSUS (deployed-vs-
   built-from census), MDPF_CANPLAT / MDPF_CANRTE (the canonical spine + dispatch authority), MDPF_PROVCANON (one
   contract across four scopes + both producer trees), OPAL_ADVIPOINTERS (the five-phase ADVI framework), the 08-05
   estate measurement in CLAUDE.md 17b (top-level `gold/ json/ portal/ code/` outside the grammar).

## CONSEQUENCES (this seat)
- Registration (stage 1) now; a stage-2 purpose-level PRD with the census matrix (pipeline x partner x {code home,
  data home, trigger/schedule, served keys, deploy vehicle}) as its ground-truth run; stage 3 = COO decomp of the
  measurement cells; the remediation proposals land as a second stage-2 act per pipeline on his word.
- Broadcast: MSTR + COO/CVO/DS/AE (queued). Same turn. Not a 49F-restricted subject in itself; CRO not needed.
