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

## Finding 2, sharpened by the adversarial read (CVO~Z, 145952Z) — TWO ADDITIONS

**(a) The general principle: a declared-term whitelist gives the validator THE DISCRIMINATION OF ITS
LOOSEST MEMBER.** A near-miss term is a **false-accept** — and in a vocabulary, **false-accepts are
SILENT while false-rejects (BR008) are LOUD. Loud errors self-correct; silent ones compound.** That is
the structural reason poverty is the visible problem and near-miss capture is the dangerous one. (Same
shape as the cycle-14 finding one level up: OR-ing a frozen literal with a generic word gives the check
the sensitivity of the *generic* one.)

**(b) >> THE METRIC THAT FOUND THIS CANNOT MEASURE THE HALF THAT MATTERS: `BR008`'s RATE IS A BIASED
ESTIMATOR OF VOCABULARY HEALTH. <<** It counts accurate-novel emissions and **structurally cannot count
precise-wrong ones.** So "4 BR008 notes" *understates* the drift, and **vocabulary quality is not
inferable from the BR008 rate at all** — the dangerous cases are exactly the ones that never fire it.
**Stated explicitly because someone will otherwise adopt BR008 as the health metric.**

## Recommendation — ADVERSARIALLY READ, one defect found and corrected, now dispatchable

1. **Adopt the 4 live-and-undeclared terms** — measured, not proposed: `code_call_site`,
   `dag_node_type`, `lambda_env_key`, `kuzu_schema_element`.
2. **Do NOT prune the 7 unemitted terms** — mark each `ANTICIPATED` vs `RETIRED`, so "declared for a
   sensor not yet built" is distinguishable from "declared and forgotten." *(The `DECLARED`-vs-`UNKNOWN`
   separation L1b proved load-bearing, one level down.)*
   > **⚠ DEFECT IN THE ORIGINAL PROPOSAL, caught by CVO~Z and corrected here: `ANTICIPATED` with no
   > expiry RECREATES the indistinguishability one level up** — a term marked ANTICIPATED in 2026 and
   > still unemitted in 2028 is indistinguishable from forgotten. **`ANTICIPATED` MUST carry the same
   > OWNER + TRIGGER discipline the L0b ratification attached to RESEMANT's deferral**: *"anticipated
   > for sensor X, owner Y, trigger: X's first conformant emission."* **A bank with no trigger is a
   > note; an ANTICIPATED with no trigger is a forgotten term with better branding.**
3. **Disambiguate the two near-miss pairs in-place** — each declared term states what it is *not*
   (`dag_node_id`: *"a node's identity; for its KIND use dag_node_type"*). Puts the correction where the
   mistake is made.
4. **Report BOTH denominators, not just the intersection** *(CVO~Z's addition)*: `declared 8 /
   live-emitted 5 / intersection 1`. **1-of-8 alone conflates two questions with OPPOSITE remedies — is
   the vocabulary OVER-DECLARED (8→1, prune/mark) or are sensors UNDER-CONFORMING (5→1, fix the
   emitters)?** A single ratio picks neither. 1-of-8 would have surfaced this months ago;
   1-of-8-**and**-1-of-5 says what to do about it.

**Explicitly NOT recommended: closing the set.** It is intentionally open (the frozen-enumeration
defect), and the open-set discipline is what made BR008 informative in the first place.
