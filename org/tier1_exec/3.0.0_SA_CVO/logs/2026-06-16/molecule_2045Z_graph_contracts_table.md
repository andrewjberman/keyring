# MOLECULE: globgrph.graph_contracts (live Iceberg table on Nessie main)   (scale: MESO)

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, EXPLORE

## Unit + expected role
The `graph_contracts` Iceberg table on globgrph Nessie `main`
(`s3://opal-313476888478-globgrph/warehouse/globgrph/graph_contracts_bccbceec-.../`), read live via pyiceberg
StaticTable on the current metadata (`00000-a2b5eb5e...`). Expected role (PRD §3): the value-layer never-widen
anchor — per-surface contract rows (canonical_writer / period_defs / forbidden_writers / ratified_by) that
comp-surface-check Q2 + the CVO value-check read to catch a BMKAUD-class semantic break.

## 1. Composition — what it actually is (vs §3 declared)
Live schema = **exactly the §3 ratified 13-column set, zero drift**: contract_id(string,required), surface,
artifact_keys(list), canonical_writer, canonical_producer, source_of_truth, period_defs(map<string,string>),
models(list), forbidden_writers(list), enforcement(struct<iam_backstop,surface_gate,value_check>),
ratified_by(list), ratified_at(string), active(boolean). The CTO amendments are present: `active BOOLEAN` exists;
NO explicit `version` column (Nessie commits are the version). **Caught + corrected my own misread:** the field-id
"gaps" (4,9,10,12,14,20) are NOT dropped columns — they are the list/map/struct nested element ids (period_defs
map id8 -> key9/value10; each list id -> +1 element id; enforcement struct -> 16/17/18). All ids 1-22 accounted.
Knowledge parity: **live == §3 doc.**

## 2. State — live snapshot characterized
- **3 rows**, all `active=True`, all ratified with REAL Nessie hashes (benchmark `6f21c75c…`; peers+aum
  `a7bc0aed…`). period_defs counts: benchmark 11, peers 9, aum 4 — all match my authored YAML byte-for-byte
  (prior verdict d12fd76).
- **1 current snapshot** (op=APPEND, total-records=3, current_snapshot_id 7372628383041021108). The Iceberg
  snapshot log shows only the current snapshot — consistent with Nessie holding version lineage in its commit
  graph (snapshot.parent=null by design, banked: [[reference_nessie_iceberg_snapshot_parent_null_by_design_no_cas_guard]]);
  per-row authoring provenance is the `ratified_at` field, NOT the Iceberg snapshot history.

## 3. Position in the chain
- **Upstream (writers):** AE `derive_runner --load-contracts <yaml>` in-VPC (prefix-aware image fe645e103),
  source = my CVO-authored `graph_contracts.yaml`. Co-located on Nessie main with `graph_nodes` + `graph_edges`
  (same branch -> contract edits time-travel with the estate graph).
- **Downstream (readers):** comp-surface-check Q2 = **LIVE consumer (advisory)** ✓; the runtime period_defs
  value-check (CVO) = **PENDING (not built)**; `pipescript --contract` (DS TO-4) = **NOT BUILT** (confirmed: not a
  known flag); NFRA_INFRPT P3 contract-integrity section = **staged**.
- **Reach:** changing a row changes what Q2 sanctions on the model_portfolios surfaces. Seams already QA'd in
  `seams_2035Z_session_work_integration.md` (load seam SOUND; aum/peers value-limb UNVERIFIED@semantic).

## 4. Behavior — exercised, not inferred
Ran `comp-surface-check contract-selfcheck` (Phase-3 synthetic BMKAUD replay) -> **the table IS live-consumed**:
- source = "live snapshot (latest)"; Q1 detects `+smartx-model-monthly-pull`; **Q2 -> UNSANCTIONED** (it reads
  benchmark's live `forbidden_writers` to know smartx is forbidden) -> the BMKAUD-catch fires end-to-end against
  the live table; ratified-in-window -> SANCTIONED. **ALL PASS, rc=0.**
- **Advisory mode confirmed:** "SEV1 touch would BLOCK in blocking mode (ramp not yet flipped) -- warning only";
  `rc-invariance off=0 on=0` (advisory layer doesn't change exit codes — correct for the §9 ramp).
- **False-clean discipline live + working:** the selfcheck LOUDLY flags `model_portfolios.headline (SEV1) is
  UNCONTRACTED (LOUD: unreviewed)` — the missing headline row is VISIBLE, not silently clean. Exactly the
  "uncontracted SEV1 reads LOUD" acceptance criterion, observed firing.

## 5. Semantic quality + smell pass
The 3 rows are correct content (byte-verified). **Decision-useful read:** the table is correctly populated AND
actively consumed by ONE live reader (Q2, advisory) where it demonstrably works (BMKAUD-catch fires; headline
LOUD-uncontracted). Full enforcement is phased/pending: policy limb is live-but-ADVISORY (no block yet, §9 ramp);
the value limb has NO runtime reader (the CVO value-check is unbuilt); 2 other consumers (pipescript --contract,
P3) not built. Not a defect — the phased rollout — but the honest state: **the table is doing its job for its one
live consumer; 3 of 4 readers are still owed.**

## Smell findings
| Smell | Rating | Evidence | Why it caught my eye |
|---|---|---|---|
| 3-of-4 consumers pending | **WATCH** | only Q2 (advisory) reads it live; value-check/pipescript-contract/P3 unbuilt | a contract table is only as useful as its readers; today it's mostly "governance metadata at rest" + one advisory reader. By design (phased), tracked. |
| aum forbidden_writers tripwire Q2-invisible | **WATCH** | aum.forbidden_writers=[smartx-exporter-role], but EC2 producers have 0 WRITES edges -> tripwire can't fire pre-06-17-derive-fix | the false-clean class; honestly caveated in the row's enforcement.iam_backstop; moots if EC2 decommissions (0.5.0_AE) |
| Iceberg snapshot log = current-only | **NOTE** | 1 snapshot, parent=null (Nessie design) | a dev-box auditor expecting Iceberg time-travel of graph_contracts gets current-state-only; lineage = ratified_at + Nessie commits |
| authoring-YAML benchmark ratified_at stale vs live | **NOTE** | YAML=PENDING-ANDREW-SIGNOFF; live=6f21c75c | known dev-box source-vs-live drift on one field; protected by the already-present guard; do not "fix" the YAML (would risk a re-load) |
| field-id "gaps" | **NOTE (corrected, not a smell)** | ids 4/9/10/12/14/20 = list/map/struct element ids, all accounted | recorded so a future reader doesn't misread nesting as dropped columns (I made + corrected that inference) |
| headline LOUD-uncontracted | **NOTE (positive)** | selfcheck flags SEV1 headline UNCONTRACTED | the false-clean discipline is live + working — the system surfaces the missing row, doesn't false-clean it |

## Assessment
The `graph_contracts` table is **healthy, schema-clean (exactly §3), byte-correct, and actively consumed by
comp-surface-check Q2** — the benchmark BMKAUD-catch fires end-to-end against the live table and uncontracted SEV1
(headline) reads LOUD. No defects. Its decision-usefulness is **partially realized by design**: policy limb
live-but-advisory, value limb + two other readers pending. Every open item (value-check assertion, headline row,
aum EC2-tripwire enforcement) is known/owned/phased — none silent. The table does its job for its one live
consumer and is correctly staged for the pending ones. No DIG-rated smell; the two WATCHes are tracked phased work,
not defects.

## Knowledge-parity delta + residual
- Believed == true on composition (schema), state (rows), and behavior (Q2 consumes it). Corrected one transient
  self-misread (field-id gaps) before it reached the record.
- Residual (NOT exercised, owed): the runtime value-check assertion (closes the value limb / the aum+peers
  SEMANTIC axis from /seams); the headline SEV1 row (Andrew sign-off); aum-tripwire Q2-enforcement (06-17 fix or
  EC2 decommission). All carried in the rows + TO-3 remaining scope.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| pyiceberg StaticTable (live read) | D1/D2/D5 — schema + snapshots + full rows | 13-col §3 schema, 1 snapshot/3 records, rows byte-correct |
| comp-surface-check contract-selfcheck | D4 — exercise Q2 against live table | ALL PASS; Q2 reads live snapshot, UNSANCTIONED fires, headline LOUD-uncontracted, advisory rc-invariant |
| pipescript --contract (probe) | D3 — consumer existence | NOT BUILT (DS TO-4 pending) |

— 3.0.0_SA_CVO
