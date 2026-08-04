# RCG Cycle-3 Adjudication Protocol — the 411 set

**Author:** 4.0.0_SA_CRO, 2026-08-04 ~0710Z
**Status:** DRAFT — executes only after 1.0.0_SA_CTO~B review ack (their 062006Z asks are
folded in as conditions 1 and 2). Andrew override retained throughout (R-0020).
**Ruling basis:** CTOB-RCG-001 (batch mechanics), R-0010 (epistemic flags), R-0013
(concretely-resolvable evidence), R-0019 (the binding cohort verdicts + the open
lambda-TF-cross-check question this protocol discharges), D-0007 (the set predicate).

## 1. The set — a predicate, never a roster

Adjudication set = tracked files at LABELS.jsonl last-row-wins where
`confidence == SPLIT` (any path) UNION `path startswith infra/aws/lambda/ AND
confidence in {LEAN, SPLIT}`. **Re-derived at execution time; every run prints its
denominators.** (The count-vs-memory law: the number below is today's OBSERVED baseline,
not the set definition.)

OBSERVED 2026-08-04 ~0708Z: 411 = 3 SPLIT-anywhere + 408 lambda. All 408 lambda files
currently carry KEEP at low confidence — the delegation round's default pending exactly
this cross-check. 88 function-trees. Registry recon (substring-grade, superseded by s.2's
exact join): 80 trees referenced by the deploy registry (388 files), 8 trees absent
(20 files): cloudfront_market_generator, m365-ms-ingest-liveness, mdpf-manifest,
precompute_market_metrics, schwab-bronze-freshness, security-sweep-daily, smartx_query,
trending_image_generator.

## 2. Evidence per lambda function-tree — three independent signals, exact joins

Per tree `infra/aws/lambda/<fn>/`, gather (all OBSERVED, cited in the label row):

- **(a) Deploy registry:** an entry in `infra/aws/lambda/ci/lambda-source-map.json`
  whose source_dir resolves to the tree (EXACT field join, not substring — the s.1 recon
  is not this check).
- **(b) Terraform:** a TF resource/module whose source references the tree (comp-aws
  edges + the owning `.tf` file:line). DESIRED plane only — declares intent, not
  existence (Rule 22a).
- **(c) Live:** `aws lambda get-function` for the function the registry/TF names —
  APPLIED truth. (Operational aws, not nudged; one call per tree, read-only.)

Verdict table (per tree, mapped to file labels):

| (a) registry | (b) TF | (c) live | Verdict |
|---|---|---|---|
| yes | yes | yes | LIVE — KEEP (or MIGRATE where the layer-refactor spec will claim it) |
| no | no | no | ORPHAN — ARCHIVE-eligible, subject to s.3 + s.4 |
| any disagreement | | | DIVERGENT — NOT a label call; a drift FINDING routed to CTO~B (a registry/TF/live mismatch is Rule-4 CI-drift territory, and adjudicating it as a label would bury it) |

## 3. Condition 1 (CTO~B 062006Z): ratified cohort verdicts are BINDING

R-0019 ratified: `layers/` + `v2_portal/` = KEEP; `portal/` + `market_query` +
`test_seeking_alpha_unauth` = MIGRATE. Any set member inside those cohorts inherits the
ratified verdict, RE-DERIVED at adjudication time (the C6 rationale at coarser grain).
If live evidence CONTRADICTS a ratified verdict, the item ESCALATES to Andrew with the
evidence — an andrew_ratification is never silently overridden (that failure mode
produced the 4,103-label contradiction this subtree is famous for).

## 4. Condition 2 (CTO~B 062006Z): the build-recipe pass — hunt the ka_testing shape

Before ANY tree receives an ARCHIVE-eligible verdict: enumerate its recipe files
(Dockerfile, docker-compose*, Makefile, deploy*.sh, build*.sh, requirements*.txt,
template.y*ml, in-tree *.tf) and check every SURVIVING file that references the tree or
its recipes (the deleted-recipe / kept-app inversion too). C7 sees only `__init__.py`;
this pass covers the general gutted-tree class deliberately. A hit converts the verdict
to REFERENCE_KEEP or MIGRATE-with-citation-repair, exactly as the held-4 resolution did.

## 5. Model blindness — protecting E-0004

Adjudication NEVER consults v3 (or v2) `p_archive`. Both prediction sets are frozen
(vintage 20260803T223617Z_d16f20d5 + the preserved v2 copy); E-0004 scores both against
these adjudication outcomes — labels that do not exist until this protocol runs, same
denominator, truly prospective. Consulting the model during adjudication would make the
eval circular; the blindness IS the control. E-0004 also populates the planted-controls
and calibration fields for the first time (a control that cannot fail is not a control):
>=10 planted items (5 known-KEEP, 5 known-ARCHIVE from already-ratified cohorts) ride
the adjudication queue unmarked, and the adjudicator's hit-rate on them is reported.

## 6. Output form

Each adjudication appends a LABELS.jsonl row: `{path, label, binary,
source: "cycle3_adjudication"` (NEW source value — CTO~B ack requested; weighting for
cycle-4 retrain proposed at 3.0, same as delegation), `ruling: "CTOB-RCG-001"`,
`evidence: "<registry entry | tf file:line | live-check result | recipe-pass result>"`,
`confidence, date}`. Confidence HIGH only on >=3 agreeing independent signal families
(PRD s.9 convergence rule; (a)/(b) are one family when both merely absent — two
absence-shaped signals count as one). The 3 non-lambda SPLIT files (2 docs
REFERENCE_KEEP, 1 MIGRATE) are adjudicated individually under the same evidence bar.

## 7. Execution and sequencing

1. CTO~B review ack of this protocol (including the two flagged asks: the new source
   value; the DIVERGENT-routes-to-you rule).
2. Mechanical evidence sweep (registry join + TF join + live checks + recipe pass),
   emitted as a per-tree evidence table — OBSERVED, no labels yet.
3. Adjudication rows appended in cohort-coherent tranches, blind per s.5.
4. Any ARCHIVE outcomes queue for standard ratified batches (cap 500, sweep gate,
   attribution — unchanged mechanics). MIGRATE and CONTESTED never batch-delete.
5. E-0004 dual-eval closes the loop; cycle-4 retrain folds the rows.

Estimated yield, stated to be falsified: the 8 orphan-recon trees (20 files) are the
plausible ARCHIVE mass; the 380+ registry-referenced files most likely settle
KEEP-at-HIGH or transfer to the MIGRATE/layer-refactor spec. If the evidence sweep
returns materially otherwise, the surprise itself routes to CTO~B before tranche 1.
