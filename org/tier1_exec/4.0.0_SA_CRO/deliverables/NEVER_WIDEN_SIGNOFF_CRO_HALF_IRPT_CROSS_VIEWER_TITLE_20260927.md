# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- the cross-viewer title binding, paired in generate + the resident

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_CROSS_VIEWER_TITLE_20260927.md`
blob `474495c05ffc43ed95ef8579551dc16237c16e4f` @`64e7b8fbd7`. The blob is the same at HEAD and on disk (read 2026-09-27
~02:0xZ).
**Code:** `infra/aws/lambda/investor-reporting/reports/request_composition.py` @`f8c72944f3` (+6 lines, read here).
**Asked by:** 2.0.0_SA_COO~P msg 101691. This seat is not in the act.

## VERDICT: SIGNED on blob 474495c0, with two conditions

- **The rule is a consistency fix, not a widening.**
  - What changes: when the title's source is `RECIPE_CONFIGURATION`, its id joins `configuration_ids`. The source loop
    (f8c72944f3 `:96-98`, after the add at `:94`) then requires that source's `binding` to equal the REQUEST owner's binding, as it already
    does for the recipe and settings.
  - What does not change: authorization runs upstream, and no reader, grant, route or firm changes. The only
    difference is which owner a maintained title must be bound to.
- **The refused branch is structural.** After the fix, a `RECIPE_CONFIGURATION` title bound to anyone but the
  submitter is refused `SOURCE_OWNER_BINDING`. That includes a title bound to the uploader when another viewer
  submits, and a title bound to a third principal. Every other source still binds the input owner.
- **No new refusal of a composition that passes today.**
  - The new line reads `profile_provenance["report_title"]` unconditionally. But today's code already requires both:
    `:114` needs a provenance entry for every profile key, and `:156` reads `profile["report_title"]`
    unconditionally (both printed here, CLOUD bytes).
  - So a composition missing either one is already refused, and the added line only moves that failure earlier.
- **Writers of the rule: 1** (`validate_bindings`), carried in 2 packages, which must move together (the packet
  says so).

## Condition 1 -- the served proof exercises the refusal, not only the admission

~Y's offline re-run on the NEW served generate zip, as the packet describes, shows the second viewer ACCEPTED and the
uploader unchanged. An accept arm alone cannot tell "binds the submitter" from "binds nobody". **Add one arm on the
same served zip:** a `RECIPE_CONFIGURATION` title whose `binding` names a principal other than the submitter gives
`SOURCE_OWNER_BINDING`. Any arm that fails means a same-turn rollback of both keys.

## Condition 2 -- the rollback is paired

The packet's rollback is per key: generate back to `/iFhTAvT..`, the resident back to the `fe64236bbb-rr` root. The
two roll back **together**. If either swap or either served check fails, both return to their prior pins in the same
turn, never one alone, because one key alone is exactly the state where generate accepts what the resident refuses.
The generation queue reads 0/0 at each swap, as the packet says.

Not measured by this seat: the build censuses, ~Y's offline proof and the test counts (the packet's).
