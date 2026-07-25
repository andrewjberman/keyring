<!-- 1.0.0_SA_CTO~Z · 2026-07-25 · design read for round-2 docket item 5, BEFORE any build -->

# Round-2 item 5 — `address_space` vocabulary: design read

**Status: DESIGN READ, no build.** Per doctrine §III-d.12 (*review the design, not only the build* —
measured this session as the cheaper loop by an order of magnitude). Produced by grounding, not by
reasoning from the L2 verify's summary. **Nothing here is dispatched yet; the recommendation at the
bottom is what a build order would say, and it wants an adversarial read first.**

## Measured state

**DECLARED** (`boundary_report.py` `KNOWN_ADDRESS_SPACES`, 8): `yaml_key_path` · `json_key_path` ·
`dag_node_id` · `dag_edge_type` · `cf_behavior_ordinal` · `tf_resource_address` · `code_branch_id` ·
`s3_prefix`

**LIVE-EMITTED** (5 distinct, across the 5 conformant reports): `code_call_site` (comp-cache) ·
`dag_node_type` + `dag_edge_type` (comp-blast) · `lambda_env_key` (env sensor) ·
`kuzu_schema_element` (comp-kuzu)

**INTERSECTION: 1** (`dag_edge_type`). So: **7 declared-and-never-emitted, 4 live-and-undeclared.**

## Finding 1 — this is the both-directions filter drift, in the type's OWN vocabulary

Sensor-3 measured exactly this shape in `comp-blast` and it became a census finding: *5 filter literals,
2 of which can never match, inflating apparent coverage — a filter that looks broader than it is.* **The
boundary-report type's own address-space vocabulary has the same defect, worse: 7 of 8 declared terms
are never emitted by any live sensor.** A reader counting eight terms believes eight shapes are
recognized; one is. **The instrument that detects this class in other tools carries it.**

*Caveat, stated because it bounds the finding:* the 7 are not necessarily dead — several name real
shapes for sensors that do not exist yet (`cf_behavior_ordinal`, `tf_resource_address`, `s3_prefix`),
and `yaml_key_path` names comp-residue's shape, which never became a conformant emitter. **"Declared for
a future or non-emitting sensor" is legitimate; "declared and forgotten" is not, and the two are
currently indistinguishable from the outside.**

## Finding 2 — THE SHARP ONE: the incentive is backwards

Two declared terms are **near-misses** for live ones:

| declared | live | are they the same? |
|---|---|---|
| `dag_node_id` | `dag_node_type` | **No** — a node's *identity* (`lambda:opal-foo`) vs its *kind* (`LAMBDA`) |
| `code_branch_id` | `code_call_site` | **No** — an if/else branch vs a call site |

**Consequence: a sensor author who reaches for the near-miss declared term gets SILENCE; one who emits
the accurate undeclared term gets BR008.** Being *precisely wrong* is rewarded and being *accurately
novel* is flagged. That is the open-set discipline working correctly at the mechanism level and
backwards at the incentive level — and it is invisible in the reports, because a wrong-but-declared
space produces a clean report about the wrong address space.

**This is the round-2 item, more than the poverty is.** Vocabulary poverty is loud and self-correcting
(BR008 fires, someone notices). Near-miss capture is silent and self-reinforcing.

## Recommendation (for adversarial read, not yet dispatched)

1. **Adopt the 4 live-and-undeclared terms** — they are measured, not proposed: `code_call_site`,
   `dag_node_type`, `lambda_env_key`, `kuzu_schema_element`.
2. **Do NOT prune the 7 unemitted terms.** Instead, **mark each as `ANTICIPATED` vs `RETIRED`** so
   "declared for a sensor not yet built" is distinguishable from "declared and forgotten" — the
   distinction that currently does not exist. This is the `DECLARED`-vs-`UNKNOWN` separation L1b proved
   load-bearing, applied one level down.
3. **Disambiguate the two near-miss pairs in-place** — each declared term states what it is *not*
   (`dag_node_id`: *"a node's identity; for its KIND use dag_node_type"*). Cheap, and it puts the
   correction where the mistake is made.
4. **Report the intersection.** `boundary_report` should be able to answer *"how many declared spaces
   has any sensor ever emitted?"* — the same coverage-denominator discipline the estate applied to
   everything else today, applied to the vocabulary itself. **1-of-8 is the number that would have
   surfaced this months earlier.**

**Explicitly NOT recommended: closing the set.** It is intentionally open (the frozen-enumeration
defect), and nothing here changes that.
