# RECOMPILE FROM THE CLOUD -- design for dissolving the pipeline substrate's derivation into the aws pass

**Author:** `1.0.0_SA_CTO~A` -- 2026-08-11, on Andrew's sovereign NOW (~23:1xZ 08-10, relayed by CVO
231208Z: *"Move forward with the recompile design and the Kimi subdivision now"*).
**Ruling implemented:** `@09355b6d93` -- **(b) RECOMPILE FROM THE CLOUD**: pipelines modeled as what
AWS itself sees, compiled in the SAME deterministic pass + freshness discipline as the aws
substrate; the repo-AST code graph becomes ENRICHMENT on those aws-anchored nodes.
**Binding constraint (Andrew-direct ~22:3xZ, verbatim):** *"there should be no hand drawn anything
with pipeline. I don't even really believe in there being a pipeline territory here because really
its just AWS which is already a category."*
**Migration method:** ATOM_DECOMP replacement+decommission (CVO rider input 1, adopted; Andrew's
wrap ruling -- this design's ground-truth phase runs as the Rule-14 rectangle CRO is seeding).
**Evidence base:** every measured claim below cites `E2E_FUNCTIONAL_ASSESSMENT_GRAPH_KIMI` v1.1
`@42287ad1e6` (the seed of the pipeline-substrate rectangle) or `file:line @ HEAD 959236f60d`-era
source reads made this session. Claims not so cited are marked DESIGN (a choice, not a fact).

---

## 1. What is being replaced, and why it froze (MEASURED)

The current chain is four hops, each a place to freeze, and the first is hand-drawn:

```
Pass-6 hand builders          extract_gold_compute.py       producers/graphuni/*.json     nightly derive
trace_graph.py:449-493   -->  (manual one-shot,        -->  (FROZEN 2026-06-30/07-01, --> re-ingests the
BD/INF/MDPF/assets;           ZERO TF refs, NO             41 days at assessment)        same frozen
NO cot builder                schedule)                                                  snapshot nightly
```

- **Hand-drawn roster:** the per-tree builder calls are literally hand-added, one per tree, and
  cot never got one -- 0 of 42 cot gold scripts in the graph while cot is DECLARED in the
  producer's own `_FIRM` scope (`extract_gold_compute.py:34`; assessment v1.1 cot cell). This is
  the exact class Andrew's constraint and the estate's "a predicate is not a roster" law name.
- **Unscheduled production producer:** zero Terraform references; a manual one-shot feeding a
  scheduled consumer -- the CLAUDE.md ad-hoc-rule half-(b) defect class, measured live (F1, P1).
- **Freshness illusion:** graph_nodes reads "last-write 1.0h ago" while its pipeline DATA is
  July-1 -- fresh derive, frozen input (assessment `pipeline_substrate.snapshot_vintage`).
- Coverage at assessment: bd 69/69 (as of July 1), inf 46/53, mdpf 18/21, cot 0/42; the script at
  the center of the day's MDPF repair invisible to the graph.

**The remedy is structural, not a patch:** no re-emission, no cot builder, no schedule bolted onto
the one-shot (per COO sequencing, the recompile SUPERSEDES all three -- R1a/R1b fold in here).

## 2. Target architecture (DESIGN)

**One sentence: the pipeline substrate becomes a section of the aws extraction itself -- derived
nightly, in-derive, from S3/EC2/scheduler ground truth, with the repo-AST joined on as enrichment
by a deploy-grammar predicate.**

### 2.1 The cloud-anchored derivation (in `run_full_derive`'s deterministic pass)

A new `extract_pipeline_cloud()` in `infra/aws/globgrph/`, wired INSIDE the nightly derive exactly
where the aws resources derive (NOT as a producer-JSON ingest -- the producer/snapshot layer is
what froze). Sources, all things AWS itself sees:

1. **Deployed code objects.** Enumerate `s3://<bucket>/<code-prefix>` for every (tree, layer) in
   the crossing `PIPELINE_MAP x VALID_LAYERS` + `AUX_CODE_PREFIXES` (`.tools/safe_deploy_core.py:29`
   -- the deploy gate's OWN machine-readable grammar, so the graph's universe and the deploy
   mechanism's universe are THE SAME OBJECT and cannot drift apart). Each `.py` object ->
   `PipelineScript` node, id `pipeline:<firm>:<tier>:<script>` (id grammar preserved), with
   `vintage` = S3 LastModified + ETag -- a REAL freshness fact per node, not a snapshot date.
   **cot is covered by construction**: its bucket/prefix is a PIPELINE_MAP row like every other;
   no per-tree code exists anywhere in the design.
2. **Runners + schedules.** EC2 services from `EC2_MANIFEST.json` + live instances, Lambda
   invokers, EventBridge rules/Scheduler schedules -- all ALREADY aws-substrate nodes
   (`NODE_TYPE_LAYER` aws block, `derive_runner.py:2053+`). The extractor adds the edges:
   SCHEDULE/EVENT_RULE --TRIGGERS--> runner --RUNS--> PipelineScript (deployed-object join). A
   pipeline with no inbound TRIGGERS chain is thereby VISIBLY unscheduled -- the F1 defect class
   becomes a queryable graph fact instead of a discovered surprise.
3. **Repo-AST enrichment (the predicate, never a roster).** For every deployed object, the deploy
   grammar names its repo source (`data/<tree>/scripts/<layer>/<script>.py`); the AST facts
   (functions -> `PipelineFunction`, CALLS, READS_S3/WRITES_S3 with the firm-qualified S3Key
   convention from `extract_gold_compute.py:136-162`, which this design retains) attach to the
   cloud-anchored node. The enrichment universe is a PREDICATE: `every deployed code object` JOIN
   `every file matching data/*/scripts/*/**.py`. Divergence between the two sides is EMITTED, not
   absorbed: deployed-without-source and source-without-deployment are first-class edge-less
   findings (`drift_class` on the node) -- this is `comp-pipescript deployed`'s MATCH/STALE/MISSING
   verdict becoming a nightly graph property.

### 2.2 Freshness discipline

Same as aws: derived every nightly run from live listings (S3 list + manifest reads are cheap;
the AST enrichment reads the repo the derive already clones). No intermediate snapshot artifact
exists to freeze. `producers/graphuni/` pipeline members are decommissioned in W3 (s.4).

### 2.3 What deliberately does NOT change (the invariants, from the assessment + handoff)

- **Type-level addressability:** `PipelineScript` / `PipelineFunction` / `Pipeline` node types
  survive verbatim (tier stays an attribute per the ratified amendment-1 form).
- **id grammar:** `pipeline:<firm>:<tier>:<script>[:<fn>]` unchanged -- per-tree accounting and
  every existing query keep working.
- **Side-grain denominators:** BACKEND = aws + pipeline already; recompiling the derivation moves
  ZERO nodes across the side rollup, by construction.
- **Consumer set:** `NODE_TYPE_LAYER` (`derive_runner.py:2085`), the graphuni `setdefault`
  (`:2202-2203`), `layer='pipeline'` filters -- all untouched in W1-W3. Layer-label questions are
  W4's, separately gated (s.5).

## 3. Migration -- ATOM_DECOMP replacement+decommission, four waves + one gated

Method: Rule 9 (delete nothing before replacement / parity / cutover / drain / rollback /
absence-proof), `replacement_ledger` + `migration_waves` templates. Population: the 1,337 live
pipeline nodes (assessment `nodes_by_substrate.pipeline`) plus the coverage the old chain never
had (cot 42, inf +7, mdpf +3).

- **W0 -- rectangle (ground truth).** CRO's seeded Rule-14 rectangle at
  `runs/pipeline-substrate/<stamp>/` (entities = builders/runners/trees/frozen-gap; fields =
  deployed object, schedule, two clocks, consumers, builder-status, graph population). Seed =
  assessment v1.1 + COO trigger census + AE sweeps. Design authorship cites cells; a cell that
  contradicts a s.2 assumption is a LIVE DELTA to this doc.
- **W1 -- build + prove on the real path.** `extract_pipeline_cloud()` lands behind a derive flag
  (default OFF for exactly one ad-hoc QA derive). Tests: predicate coverage (every PIPELINE_MAP
  row enumerated; a synthetic new tree row is picked up with ZERO code change -- the anti-roster
  mutant), id-grammar byte-parity on a sampled node set vs the live graph, S3Key firm-qualification
  parity, divergence emission positive controls (a planted deployed-without-source object).
  **Parity read = ONE ad-hoc QA derive, run-and-read, nothing standing** (the no-standing-
  comparator veto honored). EXPECTED DELTAS DECLARED IN ADVANCE, so parity is judged against the
  right baseline: +42 cot, +~7 inf, +~3 mdpf, per-node vintage present, plus any deployed-vs-repo
  divergence the old chain could not see. Byte-identity with the frozen graph is NOT the bar --
  the deltas are the point; UNEXPLAINED deltas are the failure.
- **W2 -- cutover, one derive, same-window rollback.** Flag ON + graphuni ingest's pipeline
  members skipped, in the SAME derive commit (single-writer seam preserved: one commit, no
  dangling cross-lane edges). Rollback = flip both back; the frozen snapshots still exist during
  W2 by design (drain, not delete).
- **W3 -- decommission + absence-proof.** Consumers first, binaries last (the comp-surface-check
  lesson): retire the Pass-6 pipeline builder CALLS from `trace_graph.py` (comp-blast first --
  the TraceGraph serves local tools too, and only the graphuni-facing members retire),
  `extract_gold_compute.py` marked retired, `producers/graphuni/` pipeline snapshot keys deleted
  from S3 (destructive: Andrew/owner confirm per autonomy rules), then the absence-proof: a derive
  with zero pipeline-producer ingest lines and full pipeline population.
- **W4 -- layer-label dissolution. SEPARATELY GATED, NOT AUTHORIZED BY THIS DOC.** See s.5.

**Group A convergence (declared consumer, not built now):** once W1 lands, the derive holds
committed->deployed facts per node nightly; the estate-report runner's Group A stratum
(INSTRUMENT_UNAVAILABLE on its host since @959236f60d, loudly) gets its named source. Wiring that
consumer is its own later act.

## 4. What this structurally retires

| Defect (measured) | How it dies |
|---|---|
| hand-drawn per-tree builders (no cot) | enumeration = deploy grammar crossing; no per-tree code exists |
| unscheduled one-shot producer | no producer; derivation runs ON the derive's schedule |
| frozen snapshot re-ingested nightly | no snapshot artifact exists |
| coverage lag (inf -7, mdpf -3) | nightly re-enumeration of live S3 |
| committed-vs-deployed invisibility | divergence is an emitted node property |

## 5. The territory concurrence -- disposed here (timing was released to this seat)

**Recommendation: CONCUR with dissolving "pipeline" as a peer territory, EXECUTED AS W4, strictly
after W1-W3 parity.** Andrew's stated view (*"really its just AWS"*) and CVO's recorded leaning
(v1.8: "pipeline is aws material, not a peer") agree on the destination; the migration risk is
entirely in the CONSUMERS (`NODE_TYPE_LAYER` 3 entries, the `:2202-2203` setdefault,
`layer='pipeline'` filters, side-rollup inputs), which is why the label flip is its own wave with
its own parity read (side denominators must not move -- BACKEND is aws+pipeline before and after,
so the rollup is invariant while every filter migrates to TYPE-based predicates first). **This
W1-derivation-first / W4-label-last sequencing IS the migration-sequencing fix v1.9
SYSTEM_DEFINITIONS is staged on** (CVO holds it; Andrew holds the land-now override): v1.9 can
land any time at-or-after W1 lands, because the vocabulary act no longer depends on the
derivation act. CRO owns the package reshape; this disposition goes to CRO + CVO with this doc.

## 6. Open calls at Andrew (surfaced, none gating W0-W1 build start)

1. **W3 snapshot deletion** -- destructive S3 delete, needs his word at that wave (not now).
2. **W4 GO** -- the label dissolution, after W1-W3 parity evidence is in front of him.
3. Nothing else: no new schedule is requested (the derive's existing schedule carries the
   recompile -- the R1a "schedule needs a word" question is dissolved, not answered).

## 7. Sizing + staffing

The W1 extractor is one in-derive module + tests, the shape and size of `ms_cloud_extract.py`'s
integration (the proven in-derive precedent, `derive_runner.py:39-42`). Buildable at this seat;
per my note to MSTR, if implementation contends with this lane's method-owner queue I will ask
for a build seat WITH size evidence, not before. CVO verifies the landing as a Rule-14
coherence-armed certification (their 232737Z standing offer), carrying the name-search sweep for
caller-side-configuration blindness (the wrong-end-of-the-arrow lesson -- directly relevant here:
TRIGGERS live on the CALLER, so W1's edge derivation searches FOR the script's name from the
scheduler side, not only FROM the script).
