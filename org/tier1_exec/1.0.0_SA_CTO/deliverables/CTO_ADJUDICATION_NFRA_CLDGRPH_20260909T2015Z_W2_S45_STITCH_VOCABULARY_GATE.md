# CTO ADJUDICATION -- NFRA_CLDGRPH, 2026-09-09 ~20:15Z: THE ARCH-GATE ON FIVE STITCH NODE TYPES (W2-S45 / W2-S48)

**Mode:** `/open-calls --adjudicate NFRA_CLDGRPH` (Andrew-direct 2026-09-03 ~05:2xZ). **Ruler:** `1.0.0_SA_CTO`, the arch-gate every
prior addition to `derive_runner.NODE_TYPE_LAYER` carried (`:2055-2110`: GO 223537Z, GO 20260708T030652Z, GO 20260708T202059Z, GO
20260708T170254Z, correction 002339Z), with `3.0.0_SA_CVO`'s re-sign. **Pitched by:** `2.0.0_SA_COO~A` (94685, drive tick 25) on
`0.9.0_WK_NFRA_CLDGRPH~2`'s rows W2-S45 (BLOCKING/ARMED to the CTO) and W2-S48, reported OPEN at `9c98dd1e63` with the F-4 fold BUILT
(15 of 15 fixture arms) and the image act deliberately NOT taken. **Andrew's standing word at this terminal (~12:5xZ):** adjudicate
and push forward on NFRA_CLDGRPH. **Broadcast the same turn** to `2.0.0_SA_COO~A`, `2.0.0_SA_COO`, `3.0.0_SA_CVO`, `0.0.0_AB_MSTR`.

## THE FINDING, as relayed (the worker's counts; this seat read the map and both extractors at HEAD)

The live cloud stitch artifact (29,131 nodes, 63 node types) carries FIVE node types absent from the frozen map: GOLD_SCRIPT 1,380,
S3_DATA_KEY 294, REACT_QUERY_KEY 94, PORTAL_COMPONENT 22, PORTAL_BUNDLE 1. `relabel_layers_by_node_type` raises `NodeTypeLayerGap`
(the COND-2 durability cert) on any observed type absent from the map and FAILS THE NIGHTLY CLOSED -- as designed. A guarded
partial fold drops 1,791 of 29,131 nodes and leaves 2,170 edges unresolvable, including 216 of 216 DERIVES_FROM and 955 of 955
STORED_IN: 100% of the two boundary edge types the PRD calls the JOIN.

**What the map and the extractors say (read at HEAD `c14a7b4366`-era tree):** the stitch producer emits comp-trace's vocabulary
through `extract_portal_stitch.NODE_TYPE_MAP` (COMPONENT -> PORTAL_COMPONENT, S3_ARTIFACT -> S3_DATA_KEY, GOLD_SCRIPT -> GOLD_SCRIPT,
+ PORTAL_BUNDLE synthetic root, + REACT_QUERY_KEY from cache_cli) and stamps its own `CLASS_LAYER` (portal for the three portal
types, **pipeline for S3_DATA_KEY**). The projection's frozen map already carries the SAME OBJECT CLASSES under its own names:
`Component` (199), `ReactQueryKey` (57), `PipelineScript` (133) + `PipelineFunction` (GRAPHUNI P1), and `S3Key` -> aws (the
002339Z correction: *"a storage object under the aws S3_BUCKET -> aws"*). `extract_gold_compute.py:91`: *"GOLD_SCRIPT = gold
fn/script with a firm"* -- ONE type spanning function grain and script grain. The 2026-06-26 drop comment: the GOLD_SCRIPT /
S3_DATA_KEY placeholder was *"conceptually muddy (S3=aws, scripts=code)"*, to be re-introduced *"only when the data pipeline is
actually graphed, gated by the fail-loud completeness cert"* -- which is now, on 1,380 nodes, with the cert firing as designed.

## Rule 24 applied (the four postulates the map must keep)

| postulate | the five as a plain addition | verdict |
|---|---|---|
| (i) MECE over a declared domain | four of the five name object classes the map ALREADY types (component, query key, script, S3 key): two types per class, overlapping members, no declared split | FAILS |
| (ii) same grain | GOLD_SCRIPT mixes function grain and script grain in one type (the map separates them) | FAILS |
| (iii) intent coherence (the layer axis = which real source owns the node) | S3_DATA_KEY stamped `pipeline` by its producer; the map's axis says a storage object is `aws` (the S3Key precedent) | FAILS as stamped, holds if aws |
| (iv) state coherence | a fold that admits five names and a later unification that removes four: the remedy must name which entries it moves | names it (S31) |

The **rename shortcut** (GOLD_SCRIPT -> PipelineScript, etc.) is a grain violation, as W2-S48 measured: populations at 10x (1,380 vs
133; 294 vs 232; 22 vs 199; 94 vs 57) are not two names for one set. The **plain addition** is the opposite violation: two
vocabularies for one object class frozen into the graph -- a reader asking "how many components" gets 199 or 22 by which name they
type. Neither is the taxonomy the law allows. What the law allows is a LABELLED INTERIM with its retirement placed.

+-- CALL 1 of 1 --------------------------------------------------------------+
  **Arch-gate: do the five stitch node types enter the frozen NODE_TYPE_LAYER map,
  and in which layer -- S3_DATA_KEY under aws (the S3Key precedent) or pipeline
  (the producer's own stamp)?**
  Chain ~2 (F-4 -> F-5 -> F-6, the JOIN) is idle by dependency until ruled.
  ------------------------------------------------------------------------------
  **REC (2.0.0_SA_COO~A) --** option (a): an additive GO for five entries, layer
  by layer (GOLD_SCRIPT -> pipeline as a NEW type beside PipelineScript; the three
  portal types -> portal; S3_DATA_KEY the CTO's call between aws and pipeline).
  ------------------------------------------------------------------------------
  **RULING -- (a) AS A LABELLED INTERIM, NOT AS A FROZEN VOCABULARY. GO for five
  ADDITIVE entries tonight, each admitted node stamped `vocabulary=stitch-v1`, and
  a NEW ROW S31 that unifies the vocabulary at the producer and RETIRES four of the
  five entries. Layers: GOLD_SCRIPT -> pipeline; REACT_QUERY_KEY, PORTAL_COMPONENT,
  PORTAL_BUNDLE -> portal; S3_DATA_KEY -> aws.**
  Grounds:
  1. The JOIN is FWD-7's arc and the cert fired as designed; a partial fold that
     loses 100% of both boundary edge types is not a fold. The five enter tonight.
  2. They enter LABELLED: `vocabulary=stitch-v1` on every admitted node is the one
     field a reader can filter on, so the two vocabularies never read as one story
     and the interim is measurable (its population is the retirement's denominator).
  3. S3_DATA_KEY -> aws by the S3Key precedent (002339Z): the layer axis is which
     real source owns the node, and an S3 object key is the cloud's, whoever wrote
     it. It is OBJECT grain, not a resource type: it does not move the COND-A
     resource-type baseline (S3Key did not); the CVO's re-sign of the map is the
     act, and if the CVO's signed baseline counts S3Key, the same re-sign moves the
     count 32 -> 33 -- the CVO says which.
  4. GOLD_SCRIPT -> pipeline as its own name (not a rename): W2-S48's grain finding
     stands; the mixed grain is the reason it cannot STAY, which is S31.
  FORM: the GO stamped in the map's comment as every prior GO is (text below); the
  CVO's re-sign; 2.0.0_SA_COO~A widens F-4's grant to the NODE_TYPE_LAYER dict and
  the fold's stamp, re-hands F-4; S31 cut behind S24/S25 as the JOIN's own cleanup.
+-------------------------------------------------------------------------------+

**The GO line for the map's comment (verbatim):** `CTO arch-gate GO 20260909T2015Z (NFRA_CLDGRPH W2-S45 ruling, PRD v0.10 S31):
+5 PROVISIONAL stitch-v1 types -- GOLD_SCRIPT -> pipeline; REACT_QUERY_KEY, PORTAL_COMPONENT, PORTAL_BUNDLE -> portal; S3_DATA_KEY
-> aws (object grain, the S3Key precedent; COND-A resource-type count unmoved). Every admitted node carries vocabulary=stitch-v1.
Four of the five RETIRE under S31 (vocabulary unified at the producer); PORTAL_BUNDLE stays.`

## S31 -- THE STITCH VOCABULARY UNIFIED AT THE PRODUCER (the row as landed in PRD v0.10)

- **What:** the four provisional types become the projection's own types at the projection's grain: GOLD_SCRIPT split by grain into
  `PipelineScript` / `PipelineFunction`; S3_DATA_KEY merged into `S3Key` by key identity; PORTAL_COMPONENT into `Component` and
  REACT_QUERY_KEY into `ReactQueryKey` by identity where the ids resolve. `PORTAL_BUNDLE` stays: the one genuinely new class (a
  synthetic root keyed by version tag). The map then retires the four entries and the stamp with them; comp-debt's second leg (S25)
  reads the unified vocabulary.
- **First act, before any merge:** the IDENTITY CENSUS -- of each provisional population, how many members resolve to an existing
  canonical id, printed with its denominator (1,380 / 294 / 22 / 94 as of today). Unresolved members are carried under the canonical
  type with `origin=stitch` and a reason, never dropped: admitted = merged + created, 0 lost.
- **Lane:** `0.8.0_AE_CloudComp` (the producers `derive_stitch.py`, `extract_portal_stitch.py`, `extract_gold_compute.py`; the map's
  retirement with the CVO's re-sign). **Depends on:** S24 (the fold, tonight), S25 (comp-debt's leg reads the result).
- **Accept:** `comp-kuzu "MATCH (n:CloudNode) RETURN DISTINCT n.node_type"` shows none of the four provisional names and shows
  PORTAL_BUNDLE; 0 nodes carry `vocabulary=stitch-v1`; the identity census printed per type with denominators; node count reconciled
  before/after (admitted = merged + created, 0 lost); DERIVES_FROM and STORED_IN resolve 100% after unification (the day's counts,
  216 of 216 and 955 of 955 today); the rule-initiated nightly derive SUCCEEDED; the map re-signed by the CVO with the four entries
  gone.

## Ruling ratified into s.6 as R17
A second vocabulary for an object class the graph already types enters only as a LABELLED INTERIM (a queryable stamp on every
admitted node) with its retirement row placed; a mixed-grain type is never frozen. Rule 24's four postulates decide, and a partition
that fails one is admitted only with the failure named and owned.

**Push state:** LOCAL on commit; origin/CLOUD @`c6bcb7b12b` (this seat's ls-remote 19:51Z; re-read at send).

---

## 23:05Z -- W2-S60, THE MIRROR ONE LAYER OUT: the CVO-certified grain baseline still expects the four retired types (appended, never silently)

**Pitched by** `2.0.0_SA_COO~A` (94776, drive tick 42) on `0.9.0_WK_NFRA_CLDGRPH~2`'s row NFRA_CLDGRPH-W2-S60 (BLOCKING): the
unification at the producer (S31 / F-11) is PROVEN on a local run -- identity census 1,790 of 1,790 (GOLD_SCRIPT 1,330 of 1,380
resolved: script 166 / function 1,214; S3_DATA_KEY 145 of 294; PORTAL_COMPONENT 20 of 22; REACT_QUERY_KEY 26 of 94; 269 carried
with `origin=stitch` and a reason, 24 ambiguous-across-firms carried never coin-flipped; LOST=0); admitted 3,560 = merged 3,022 +
created 538; DERIVES_FROM 216 of 216 and STORED_IN 955 of 955 resolving; the map 65 -> 61 keys with the COND-A resource-type count
unmoved at 32; three of four census figures reproducing the CVO's C-S40 exactly -- and then `org/modules/graph/grain_baseline.json`
(CVO-certified) REFUSES it, because it still certifies GOLD_SCRIPT 1,260 / S3_DATA_KEY 272 / PORTAL_COMPONENT 27 / REACT_QUERY_KEY 85
and AC-GRAIN.2 refuses on the zero they correctly become. The worker did not push.

+-- CALL 1 of 1 --------------------------------------------------------------+
  **Recertify grain_baseline.json for the four retired provisional types?**
  ------------------------------------------------------------------------------
  **REC (2.0.0_SA_COO~A) --** recertify the four to 0 (the 2026-07-25 EXTERNAL_ENDPOINT
  precedent), each entry naming the CTO gate and the CVO's sign; the canonical types'
  new magnitudes the CVO's choice: recertify now or read at L9 as the first
  post-unification magnitudes.
  ------------------------------------------------------------------------------
  **RULING -- GO, in two parts, ONE sign.** (1) The four retired types to 0 in the file's
  own form, each naming this GO and the CVO's sign: a baseline that certifies a
  vocabulary the producer no longer emits is a check reading the old world, and it
  moves with the retirement it exists to guard. (2) The canonical types recertified IN
  THE SAME SIGN at their first post-unification magnitudes (the worker's run:
  PipelineScript 332, PipelineFunction 2,428, S3Key 588, Component 24, ReactQueryKey
  188), the CVO re-measuring each before signing -- NOT read-at-L9: a band check
  against the pre-unification magnitudes (PipelineScript 133 -> 332, 2.5x) would refuse
  the correct output on exactly part (1)'s logic, and a nightly left refusing until L9
  is the waiting Andrew's ~21:4xZ word forbids. Each entry carries its basis line.
+-------------------------------------------------------------------------------+

**GO line for the file's comment (verbatim):** `CTO gate GO 20260909T2305Z (NFRA_CLDGRPH W2-S60 ruling, PRD v0.13 S31): GOLD_SCRIPT,
S3_DATA_KEY, PORTAL_COMPONENT, REACT_QUERY_KEY recertified to 0 (retired at the producer; the EXTERNAL_ENDPOINT precedent);
PipelineScript, PipelineFunction, S3Key, Component, ReactQueryKey recertified at their first post-unification magnitudes, re-measured
by 3.0.0_SA_CVO in this sign; COND-A resource-type count unmoved at 32.`

**(This record's third section, W2-S70, is at the foot of the file: the same family one plane further out -- the vocabulary of NODE TYPES
settled first, then the vocabulary of NODE IDENTITY.)**

**Form:** F-11's grant widened to `grain_baseline.json` for exactly the nine entries; the CVO signs; the zip push (ledgered), one
ad-hoc `opal-stitch-produce` build, one ad-hoc derive on the current digest, the projection and the served reads proceed under the
manual-trigger form (PRD v0.13 S32). **Carried to the L10:** W2-S61 (the producer's input carries its own prior output -- a
substrate-card question, Rule 28 q3/q4, for the stitch producer); W2-S63 (CloudOps by its row); the STORED_IN class-literal fix
(955 boundary edges that would have read 0 in the pushed zip -- the silent-zero shape the accept's negative arm must catch).

---

## 02:1xZ -- W2-S70: WHICH IDENTITY DOES A BUCKET HAVE? (the same family one plane out: node TYPES settled, node IDENTITY did not)

**Pitched by** `2.0.0_SA_COO~A` (94868, drive tick 57) on `0.9.0_WK_NFRA_CLDGRPH~2`'s row W2-S70. **Three planes, two names, no single
value right at both ends:** (a) the producer's AWS layer keys a bucket by NAME with the ARN in its own field; (b) the fold admits the NAME
only -- measured both directions on one variable, 0 of 955 admitted when the edge named the ARN, 955 when it named the name; (c) the served
graph keys `S3_BUCKET` by ARN and gives the NAME to `S3_BUCKET_POLICY`. Last tick's one-line fix moved F11-AC3 from 0 of 955 to **764 of
955, and all 764 land on `S3_BUCKET_POLICY`**; the remaining 191 are the one firm bucket with no policy node.

+-- CALL 1 of 1 --------------------------------------------------------------+
  **Which identity does a bucket HAVE in this estate -- and where is the
  disagreement reconciled?**
  ------------------------------------------------------------------------------
  **REC (2.0.0_SA_COO~A) --** rule the SERVED graph canonical (a bucket IS its
  ARN, the name an attribute); the FOLD rewrites a name endpoint onto the arn at
  admission; cut as a round-7 cell with its own image act and sign, not a
  widening of F-11. Alternative offered: the PRODUCER emits the ARN, folding
  into the third cycle already running.
  ------------------------------------------------------------------------------
  **RULING, in four parts.**
  **(1) THE 764 ARE NOT PROGRESS -- THEY ARE A FALSE RESOLUTION, AND WORSE THAN
  THE 0.** An edge resolving onto `S3_BUCKET_POLICY` asserts that a gold script
  stores its data IN A POLICY. A null read is honest; a confidently wrong one is
  the Rule 22 trap by name -- DISCRIMINATION passing inside a wrong GRAIN, every
  instrument agreeing about the same wrong thing. **F11-AC3 FAILS on 764 of 955,
  it does not pass**, and the criterion's own defect is that it checked
  both-ends-PRESENT and never the resolved node's TYPE. The arm gains that check.
  **(2) CANONICAL IDENTITY: an AWS resource node IS its ARN in the served graph;
  the NAME is an attribute.** That is the served graph's own keying and the
  estate's dominant convention (`comp_aws_cli` keys edges by ARN;
  `kuzu_nessie_load.py:161` already records the asymmetry as a known one). Ruling
  it makes the disagreement DECIDABLE once instead of per edge family.
  **(3) BOTH PLANES MOVE, and they move together or not at all.** The FOLD
  normalizes at admission (a name endpoint on a node carrying both becomes the
  arn) because the fold IS the join and it fixes every producer feeding it, not
  just this one. AND the PRODUCER emits the canonical endpoint where it knows it,
  because an artifact carrying a non-canonical endpoint is a trap for any direct
  reader -- the COMMITTED-is-not-SERVED inversion. Producer-alone is refused: the
  fold rejects ARN endpoints today (0 of 955 measured), so it would read as a
  regression to zero.
  **(4) THE CLASS, NEVER THIS EDGE FAMILY.** Before the fix, a CENSUS: every edge
  family whose endpoint names a resource carrying BOTH an id and an arn, with its
  denominator and its current resolution rate BY RESOLVED-NODE-TYPE. The worker's
  own note is the reason to look wider, and a per-edge-family fix here is exactly
  the scoped check that cannot see what the members share (CLAUDE.md Rule 22).
  The 191 stop being a special case under (2): a bucket has an ARN whether or not
  it has a policy node.
+-------------------------------------------------------------------------------+

**FORM (the COO's, endorsed):** NOT a widening of F-11. F-11 drains with AC3 reported as MEASURED-AND-FAILING beside row W2-S70 -- honest,
and the order does not wait. The census, the fold's admission rule, the producer's endpoint and the re-taken AC3 are ROUND-7 cells with
their own image act and their own never-widen sign, which the spent sign does not cover.

**CARRIED, not chased:** the served graph keying `S3_BUCKET_POLICY` by the bucket NAME is itself a grain smell -- a policy is not a bucket
-- but it is `comp_aws_cli`'s schema, outside this project's plane; named here for whoever owns that producer.

**Push state:** LOCAL on commit; origin/CLOUD @`c6bcb7b12b` (this seat's ls-remote 01:56Z).
