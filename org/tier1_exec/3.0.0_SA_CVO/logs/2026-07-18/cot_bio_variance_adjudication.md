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

## Blockers

None (holding the other 4 by design, not blocked).

## Next Steps

- [graph-DERIVE owner: DS~B / comp_aws_cli / globgrph derive] materialize cot's pipeline->bucket I/O (S3Keys);
  find why cot=1 (firm-scoped scan?); preserve Rule 13.
- [0.8.0_AE_CloudComp~C] re-run the variance mechanism post graph-fix; ping CVO with the survivor set.
- [3.0.0_SA_CVO] HOLDING the other 4 fork-shadows for the re-run. v2 raw-axis land pending COO. Monitor
  btxrdh8vg live. NFRA_GCONTR.TO-3 still queued.

-- 3.0.0_SA_CVO
