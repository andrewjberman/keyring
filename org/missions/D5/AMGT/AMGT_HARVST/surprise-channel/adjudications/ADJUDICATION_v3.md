# AMGT_HARVST round 2: CVO adjudication, ADDENDUM 1 -- `Z-S5`, and a refinement of my own AC4 reasoning

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-23T03:0xZ at HEAD after `67a8a9a670`, LOCAL on SITEZ.
`2.0.0_SA_COO~Y` filed `Z-S5` AFTER my round-2 grade (ADJUDICATION_v2 @`cfd06a014d`), measuring its own spec
against the sharpened question rather than waiting for the grade. The row is dispositioned here, and **my own
reasoning in v2 is refined rather than defended.**

## `Z-S5` is CORRECT, and its measurement is better than my inference

It scanned all eight sections for `prop`, `props`, `component`, `contract`, `receives`, `receive`, `passed to`,
`type contract`, `interface` and `signature`: **five lines match and none is an error channel** — two about a
possibly shared charting component, one contrasting list components, one about thresholds, and §7 explicitly
leaving the shared component undecided.

**I reasoned; it measured.** My v2 grade said both cited defects are prevented. **That sentence needs splitting,
and the split is the row's:**

| | prevented by the spec? | why |
|---|---|---|
| `Z-S227`'s class (an error discarded) | **YES** | the state is enumerated and decided by the transport outcome |
| `C-S400`'s rendered HARM (absence asserted as fact) | **YES** | §5 forbids rendering `error: true` as an empty array, and §6 forbids rendering the failure as emptiness |
| `C-S400`'s MECHANISM (no channel to the renderer) | ⛔ **NO** | no clause requires any surface to RECEIVE the error |

**So a build can satisfy every word, draw the page-level failed state correctly, and still hand an inner surface a
props shape with no error field** — which is precisely how the overlay's false sentence is unreachable today.

## AC4's grade STANDS, and here is the honest reason

**The criterion asks whether the amended spec DRAWS every state including the call's own failure, such that a build
cannot reproduce the defect on this surface.** The rendered harm — the thing a viewer sees and the thing both cited
rows are ABOUT — is forbidden at the spec level, explicitly and in both directions. **A PASS on that question is
correct.**

⚠ **What I should have written, and write now: the spec closes the HARM and leaves the MECHANISM unconstrained.**
v2 carried that to the build cell's criteria. `Z-S5` places it better — **in the SPEC's coverage, and therefore in
the issuer's cut** — because a build criterion binds one cell while a spec clause binds every build against it.
**I adopt the row's placement over my own.**

## The disarm, and what nobody did

**One cheap clause in a round-3 cell: every surface the spec names RECEIVES the error through a typed channel, not
merely draws a failed state.**

⭐ **And the issuer did NOT amend the spec to close a gap it had just found in its own cut.** The round is closed at
drain-end, the spec is a graded deliverable, and editing one off-process would be worse than carrying the gap
visibly. **That restraint is the correct call and I record it as such** — a graded artifact edited outside a cell
is how a record stops meaning anything, and the temptation was at its highest here because the gap was the
issuer's own.

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S7",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T03:05Z",
    "one_line": "GRADUATED: Z-S5 -- the amended timeline spec closes C-S400's rendered HARM (assertion-from-absence forbidden both ways) but leaves its MECHANISM unconstrained: measured over all eight sections, no clause requires any rendering surface to RECEIVE the error through a typed channel, so a build can satisfy every word and still ship a props shape with no error field.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "2.0.0_SA_COO~Y's scan of all eight sections for prop/props/component/contract/receives/receive/passed to/type contract/interface/signature: 5 matching lines, none an error channel; SS7 explicitly leaves the shared charting component undecided.",
        "SS5 forbids error:true being merged into series/events/articles or rendered as a zero-length array; SS6 forbids the failure being rendered as a blank chart, empty series or zero-height line. Both are HARM prohibitions, not channel requirements.",
        "C-S400 on the sibling page: SecurityOverlayProps declares bundle and isLoading only, so a branch is not expressible until a prop is threaded -- the same mechanism this spec does not forbid."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "A build against this spec cannot reproduce the Z-S227 / C-S400 defect on this surface.",
    "world_is": "It cannot reproduce the rendered harm; it can still reproduce the unreachable-state mechanism.",
    "notes": "AC4's PASS STANDS: the criterion asks whether every state is DRAWN such that the defect cannot be reproduced, and the rendered harm -- what a viewer sees and what both cited rows are about -- is forbidden in both directions. The disarm is one clause in a round-3 cell: every surface the spec names RECEIVES the error through a typed channel. ⭐ I ADOPT THE ROW'S PLACEMENT OVER MY OWN: v2 carried this to the build cell's criteria; the row places it in the SPEC's coverage, which binds every build rather than one cell. The issuer did NOT amend a graded deliverable off-process to close its own gap, and that restraint is correct. Remediation row owed at L10.",
    "adjudicates": [
      "AMGT_HARVST-Z-S5"
    ]
  }
]
```
