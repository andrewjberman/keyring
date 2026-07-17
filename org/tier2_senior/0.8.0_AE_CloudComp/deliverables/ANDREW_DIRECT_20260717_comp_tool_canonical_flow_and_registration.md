# ANDREW-DIRECT INSTRUCTION -- recorded verbatim per XXX.md same-turn law

**Channel:** Andrew, direct at the 0.8.0_AE_CloudComp~B session terminal (mid-turn, during the
NFRA_DECOMTOOL.TO-1 landing -- delivered right as I was investigating whether AE can commit to
`org/modules/graph`, i.e. the registration/owned-paths surface for comp tools).
**Time:** 2026-07-17 ~2256Z
**Recorded by:** 0.8.0_AE_CloudComp~B (receiving agent; SURFACING, NOT adjudicating scope)
**Broadcast:** MCP to 2.0.0_SA_COO + 1.0.0_SA_CTO + 0.0.0_AB_MSTR, same turn

## VERBATIM

> Oh that is a good point, Yeah we need to make sure that all the comp tools are properly tracked, i
> believe there are 62+ and we are constantly adding more. Once you are done with your tasks here I
> want you to make a canonical flow for comp tool creation/revision/and registration. Then I want you
> to scan all the comp-tools and establish if there are any that are not properly registered and make
> sure they get registered through that canonical flow. Then i want you to write a spec on the flow
> and process and get that over to MSTR because it needs to be canonized and persisted in some key,
> colocated location to the tools, probably should be referenced in the prompt.md for 0.8.0_AE that
> they ownpath alongside CTO/CVO for committing tools according to that process, should formalize that
> whole thing, probably ANY_EXEC_OR_AE for ease of ops

## Receiving agent's read (NON-BINDING -- surface, do not adjudicate)

Sequenced AFTER the current NFRA_DECOMTOOL.TO-1 landing (Andrew: "once you are done with your tasks
here"). Five components:

1. **CANONICAL FLOW** for comp-tool creation / revision / registration -- a documented, repeatable
   process. The current comp-debris-ext + comp-iam-usage landing is effectively its FIRST EXEMPLAR
   (I am walking the registration invariant by hand right now; that walk is the raw material).
2. **REGISTRATION AUDIT** -- scan all ~62 comp-tools, establish which are NOT properly registered
   (the registration invariant = tools_index + coverage-map home + `routable:` + comp-which routing,
   NFRA_COMPCLOSE / NFRA_TOOLCHECK), and register every gap THROUGH the canonical flow.
3. **SPEC** -- write the flow/process spec and get it to MSTR, because it must be canonized +
   persisted in a key location COLOCATED with the tools (candidate home: `org/modules/graph/`
   alongside `comp-tools.yaml` / `graph-call-manifest.yaml` / `comp-coverage-map.yaml`).
4. **PROMPT.MD REFERENCE** -- reference the process in 0.8.0_AE's `prompt.md`.
5. **OWNED-PATHS FORMALIZATION** -- 0.8.0_AE gains ownpath for committing tools ALONGSIDE CTO/CVO,
   "probably ANY_EXEC_OR_AE for ease of ops." Formalize the whole thing.

## Note for the record (scope-surface, NOT a ruling)

This directive establishes the INTENDED end-state: **0.8.0_AE owns comp-tool commits
(ANY_EXEC_OR_AE), alongside CTO/CVO.** It bears directly on the IMMEDIATE DECOMTOOL landing, whose
commit path I was mid-investigation on: `org/modules/**` is presently `ANY_EXEC` (excludes AE), so
the current landing's commit still routes per EXISTING owned-paths (a grantor-landed carve-out, or
CTO/COO lands) until the formalized AE ownpath exists. This directive is the mandate to build that
general rule -- it does not retroactively grant the current commit. CTO owns the owned-paths grant;
MSTR owns canonization of the spec. I surface; they adjudicate.

## Sequencing I am adopting (pending any COO/CTO override)
- **NOW:** continue + finish NFRA_DECOMTOOL.TO-1 (comp-debris-ext + comp-iam-usage), doing the
  registration BY the emerging canonical flow so the landing doubles as the exemplar.
- **THEN (new work stream, this directive):** canonical flow doc -> registration audit + gap-fill
  -> spec to MSTR -> prompt.md reference -> owned-paths formalization (CTO/MSTR gated).
- Taxonomy pivot rule still stands above both (CTO enforce-flip / W2-W3 reactivation takes precedence).
