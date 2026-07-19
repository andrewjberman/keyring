# CVO Adjudication -- opal-data-cot b-io fork-shadow variance candidate

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE
**Directive:** CTO routed (via base 004040Z) the NFRA_ONTOLOGY variance candidate to CVO; ~C filed the
grounded trace 20260719T005251Z (NFRA_ONTOLOGY_VARIANCE_COT_BIO_TRACE.md @f24cb223e).

## Current State

**VERDICT: GRAPH COVERAGE GAP -- NOT debt, NOT a firm-facet.** Delivered to ~C @010038Z, CC CTO @010056Z.
Confirms ~C's disposition, independently grounded, with one mechanism SHARPENING.

**Independent grounding (Rule 22, my own instruments):**
- RAW S3 estate (aws s3 ls, live): opal-data-cot = full medallion bronze/silver/gold/platinum/code; 380
  silver, 3,225 gold objects, 85 .py scripts. cot reads/writes its own S3 -> b-io is REAL. => (1) real-debt
  REFUTED, (2) firm-facet REFUTED (no legitimate "cot lacks b-io").
- GRAPH state: cot S3Key = 1 on BOTH the raw graph_nodes axis (marker->StaticTable-on-S3) AND comp-kuzu
  projected. 1 vs 3,600+ real objects => (3) graph coverage gap CONFIRMED.

**SHARPENING (my correction to the ~C/base "projection" label):** it is a DERIVE / materialization gap, NOT a
projection-drop. Raw graph_nodes cot S3Key = 1 == comp-kuzu's 1 -- the projection is FAITHFUL; the defect is
UPSTREAM in the S3Key materialization. Per-bucket materialization (raw graph_nodes, 232 total S3Keys):
bd=153, inf=74, mdpf=4, **cot=1**. The lone cot S3Key is a single config file
(opal-data-cot/blackdiamond/cot/session-trigger-mode.json), not the gold/silver medallion I/O -- so cot's
pipeline->bucket b-io edges have no S3Key targets. **Fixing the kuzu projection would do nothing; the fix is
the DERIVE's cot S3-scan (comp_aws_cli / globgrph cloud-graph derive).** This is the SAME projected-vs-raw
axis discipline as the AC4 v2 work, applied to NODES (materialization) rather than EDGES (projection-drop).

**Rule 13 respected:** disposition explains cot's b-io absence as a graph defect ORTHOGONAL to firm
separation (not a "cot mirrors bd" expectation). My read of cot's estate is a read-VERIFY (demanded post the
lifted sovereign block; no mirror/sync).

**Do NOT populate allowed_facets "cot lacks b-io"** (confirms ~C sec-5): encoding a graph defect as a legit
firm-difference = the manufactured-authority trap. Post derive-fix, cot resolves to Twin.

**Unknown-unknown flagged to the fix owner:** WHY does the derive materialize bd=153/inf=74 but cot=1? Likely
a firm-scoped derive config that excludes cot's pipeline-scripts from the S3-scan (bd/cot IAM+gate-separated).
If so, fix = derive-CONFIG gap; MUST materialize cot's OWN estate without mirroring bd (Rule 13). Same-root
check recommended on the other 4 fork-shadows.

**HOLD accepted (base 010041Z):** the other 4 of 5/46 fork-shadows sit on the same under-materialized graph;
HOLDING their adjudication until DS~B lands the graph-fix -> ~C re-runs -> survivors are the real candidates.
~C pings on re-run. Verdicts advisory + denominatored meanwhile (no live harm).

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `aws s3 ls` (opal-data-cot) | independent raw estate: is the medallion pipeline real? | 380 silver / 3,225 gold / 85 scripts -> b-io real (refutes debt+facet). |
| `python pyiceberg StaticTable` (graph_nodes) | raw graph_nodes cot S3Key count + per-bucket keying | cot=1, bd=153, inf=74, mdpf=4; keying bucket-prefixed (no filter miss) -> DERIVE gap, not projection. |
| `comp-kuzu` | projected cot S3Key count (compare to raw) | 1 == raw 1 -> projection faithful, defect upstream. |

**What worked:** the raw graph_nodes vs comp-kuzu comparison cleanly separated derive-gap from projection-drop
-- the distinction that routes the fix correctly. **Gap found:** the graph derive under-materializes cot's S3
estate ~3,600x (a real graph-quality defect the variance mechanism correctly surfaced).

## Addendum -- CTO affirmation + denominator + yaml-confirm (012226Z)

CTO AFFIRMED the disposition and owned that my both-axes check REFUTED his projection-drop hypothesis while
confirming the disposition (his AC4-v1 analogy gave the right REQUIREMENT "check the raw axis" but the wrong
MECHANISM-guess; the check discriminated -- Rule 22 on the requirement-vs-mechanism split). Two fix constraints
recorded: (1) Rule 13 ABSOLUTE -- the derive fix materializes cot's OWN estate scan-scope, never mirrors bd;
(2) derive/infra change -> CTO arch-gate before land.

**Denominator delivered (CTO's "which of the 5 share the root"):** the variance FIRM dimension is [bd, cot, inf]
only (3 firms, confirmed in the yaml). S3Key materialization bd=153 / inf=74 (adequate, the b-io modal) vs
cot=1 (under-materialized). So among firms the derive root is cot-SPECIFIC; bd/inf are well-materialized, so the
other 4 fork-shadows are NOT firm-b-io (they live in other dimensions/motifs) -- mapping them to the root needs
~C's post-fix re-run breakdown (HELD). Broader derive-health signal carried to the derive owner: mdpf=4
(non-firm bucket, real pipeline) is a SUSPECTED second instance, not yet raw-confirmed.

**yaml CONFIRMED (verified not asserted):** org/modules/graph/variance_dimensions.yaml -> allowed_facets: []
(L21), advisory: true (L34), firms [bd,cot,inf], NO cot facet. Item-1 (yaml -> MSTR -> exec-land) proceeds
clean.

## Addendum 2 -- root-cause GROUNDING refines 0.7.0's hypothesis (015435Z)

0.7.0 root-caused cot's under-materialization to the graphuni producer's firm-loop (extract_pipeline.py
build_firm_gold_dag being "3-firm + stale, excludes cot"); base folded it into my same-root denominator
(cot+mdpf share it, one loop-fix clears both). I source-checked before it's built on (Rule 22) and found it
IMPRECISE:
- CONFIRMED: FIRM_BUCKET = {bd,inf,cot} INCLUDES cot (:1185); build_firm_gold_dag has a WORKING current cot
  branch (:1195, reads data/cot/scripts/gold = 42 scripts, newest 07-15, NOT stale). So cot's root is NOT a
  missing registry entry or stale data.
- CONFIRMED: mdpf is NOT a firm (not in FIRM_BUCKET); it has its OWN build_mdpf_dag (:1331), a separate path.
- INFERRED (0.7.0's lane to source-confirm at the producer caller): cot is registry-present + build-supported
  yet materializes 1 S3Key -> the gap is the CALLER not invoking build_firm_gold_dag(firm="cot").

Fix-scoping correction handed to 0.7.0 (fix owner) + base: cot = fix the caller's firm iteration (cot already
supported, Rule-13-clean); mdpf = invoke build_mdpf_dag (separate). NOT "add cot+mdpf to a 3-firm registry."
Explicit confirmed-vs-inferred boundary kept -- I refine the hypothesis, I do NOT assert an un-sighted caller
mechanism (avoids the mirror of the projection-drop wrong-guess). I re-sign the fix on the RAW graph_nodes axis
when it lands.

## Addendum 3 -- root CONFIRMED at the output; fix seats with ~D/~A; my re-sign criteria set (020731Z)

0.7.0 source-sighted the caller at the PRODUCED ARTIFACT (stronger than code): s3://opal-313476888478-globgrph/
producers/graphuni/storage_s3keys.json (producer graphuni-storage, generated 2026-06-30, STALE) -> S3Key
coverage bd=113 / inf=55 / mdpf=1 / cot=0. So the storage producer iterates {bd,inf}, NEVER cot. DEFINITIVE at
the output. Honest boundary: the producer EMITTER code is uncommitted (a ~D/~A Phase-A tool; NFRA_GRAPHUNI has
only emit_b_stitchers.py + the output JSONs), so the literal firm-iteration line is not code-sighted -- confirmed
at the output, not the code. Nuance: the live graph_nodes cot=1 I measured is a DIFFERENT source (the config-file
node), not this producer (cot=0 in it).

FIX SEATING (confirmed): primary = ~D/~A's uncommitted P1-A storage emitter (add cot iteration via
build_firm_gold_dag(firm='cot') + build_mdpf_dag for mdpf) -> CTO arch-gate. AE compiler-engine
(build_firm_gold_dag(cot)) already works -> likely no change. 0.7.0 drives the s3_layout residual measurement.

MY RE-SIGN CRITERIA (set + agreed, TWO axes because two sources): (1) PRODUCER axis -- regenerated
storage_s3keys.json iterates cot (>0) + mdpf; (2) LIVE graph axis -- live graph_nodes cot S3Key count RISES to
cot's materialized set (raw graph_nodes, the served truth, not the stale JSON / producer self-report), firm-clean
(no bd bleed). RE-RUN REQUIREMENT: the JSON is stale -> this is NOT code-only; sequence is ~D/~A code -> producer
RE-RUN -> AB-MAT re-materialize -> live. I re-sign strictly on the live end-state + the s3_layout residual.

## Addendum 4 -- s3_layout residual retracted + INDEPENDENTLY CONFIRMED clean (022106Z)

0.7.0 retracted its own s3_layout residual flag (self-caught wrong-dir: it checked the gold ROOT, not gold/lib).
I confirmed the retraction independently (a second, contradictory claim -> verify, don't accept):
data/cot/scripts/gold/lib/s3_layout.py EXISTS (63 key-constants, 31 importers); extract_pipeline._parse_s3_layout
(:161-162) targets exactly lib/s3_layout.py via AST. So cot materializes via the s3_layout path (full key set),
NOT the degraded fallback. **RE-SIGN CRITERIA UPDATED:** the SECONDARY (s3_layout residual) axis is now EXPECTED
CLEAN (was: flagged risk) -- but still MEASURED post-fix (a retracted risk is a lowered prior, not a skipped
check). Fix confirmed SINGLE-CAUSE: cot has registry + working build branch + current scripts + s3_layout; the
SOLE gap is the producer not iterating cot.

## Addendum 5 -- cot fix DECOUPLED from the bd sovereign-hold ruling (grounded, 025749Z)

COO surfaced (0.7.0 finding, CTO-routed) that 4 extract_pipeline.py chokepoints (_parse_s3_layout /
_extract_script_io / _parse_dispatch / parse_gold_direct_invoke) hard-hold bd (only 1 of 5 got the 07-14
block-lift). _parse_s3_layout is ON my cot re-sign path -- so I grounded whether the bd-hold collides with the
cot fix. IT DOES NOT: the chokepoints gate on _held_path_hit vs SOVEREIGN_HELD_MARKERS =
(data/black_diamond/, data/canonical/schwab/silver/, schwab/silver/, opal-data-bd, opal-data-schwab); cot's
paths test NOT held (data/cot/scripts/gold/lib/s3_layout.py -> None). So the sovereign hold is path-scoped to
black_diamond/schwab; the cot fix + the CTO bd-hold ruling are INDEPENDENT threads. **Re-sign implication: my
cot path through _parse_s3_layout is clean regardless of the bd-hold ruling -- no need to re-check it at
re-sign time.** (Separate puzzle flagged to CTO/~B for their ruling: bd shows 113/153 S3Keys materialized
despite the hold -> stale, or a non-held bd path -- theirs to resolve, not mine.)

## Blockers

None (holding the other 4 by design, not blocked).

## Next Steps

- [graph-DERIVE owner: DS~B / comp_aws_cli / globgrph derive] materialize cot's pipeline->bucket I/O (S3Keys);
  find why cot=1 (firm-scoped scan?); preserve Rule 13.
- [0.8.0_AE_CloudComp~C] re-run the variance mechanism post graph-fix; ping CVO with the survivor set.
- [3.0.0_SA_CVO] HOLDING the other 4 fork-shadows for the re-run. v2 raw-axis land pending COO. Monitor
  btxrdh8vg live. NFRA_GCONTR.TO-3 still queued.

-- 3.0.0_SA_CVO
