# Resolution contract

Read this reference during S4 and whenever a new layer binds to a certified layer zero.

## Predicate

For one binding `b` at one declared grain and one HEAD vintage:

```
RESOLVES(b) :=
  live_authority_target_count(b) == 1
  AND pointer_resolves_at_head(b)
  AND target_carries_claimed_content(b)
  AND binding_grain(b) == authority_grain(b)
  AND mechanical_seam_passes(b)
  AND declarative_seam_passes(b)
  AND semantic_seam_passes(b)
  AND (NOT is_code_binding(b)
       OR (code_cites_authority(b) AND NOT code_redeclares_vocabulary(b)))
```

`resolved` is derived from these operands. A human does not set it independently.
Unknown or unassessed operands produce an unknown result, never false precision.

## Seam axes

- MECHANICAL: the pointer resolves at HEAD and reaches the intended live target.
- DECLARATIVE: the binding's recorded name, grain, authority, and claim match the target.
- SEMANTIC: the target actually carries the meaning the consumer relies on.

All three pass or the seam is not resolved. A correct pointer to content with the wrong
meaning is not a partial success.

## Code binding rule

Code cites the authority through a pointer, generated view, import, or resolver. It never
copies the authority's member list into a second maintained declaration. Generated output
must carry provenance and be reproducible from the cited authority.

## Contract row

Each row records:

- source and target layer;
- source surface and authority pointer;
- declared and authority grain;
- claimed content;
- HEAD vintage;
- cardinality, pointer, content, and code checks;
- three seam-axis results;
- failure direction and detector;
- evidence citations and candidate owner;
- re-run trigger.

## Binding forms and failure directions

Each row declares one primary form:

| Form | Typical loud failure | Typical clean failure | Required detectors |
|---|---|---|---|
| `RESOLVES_VIA_POINTER` | target address is missing or unparsable | address resolves to a live but wrong or stale-content target | HEAD dereference plus target-content and cardinality checks |
| `VIEW_TIME_COMPILED` | compiler or source read errors | compiler succeeds over a stale, short, or self-sourced denominator | source-vintage, independent denominator, positive control, and output-content checks |
| `CITED_ENUM` | import or resolver cannot load the authority | code copied the member list and drifts while continuing to run | citation trace plus code re-declaration census |

The table is a default hazard model, not a verdict. The contract row declares whether
loud and clean failure are possible for that binding, the exact condition for each, and
the detecting check beside it.

## Failure direction

Resolution controls fail closed. Unresolved, ambiguous, dangling, wrong-grain,
content-mismatched, or re-declared bindings cannot support a resolved claim. This method
reports and routes the defect; it does not repair the owner surface.
