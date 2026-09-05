---
name: seams
description: Integration QA on a SEAM -- the connection between two components, from one function boundary to a full pipeline -- on three pass/fail axes: MECHANICAL (does the connection carry the flow), DECLARATIVE (does the record match the implementation), SEMANTIC (is the payload the correct content with validated quality). Grounds against the deployed/served artifact; exercise-or-evidence. Output: a seam report with per-axis verdicts and the believed-vs-true delta. `/seams <target>` or `/seams <A> -> <B>`. Any agent; CVO primary. /molecule is the node; this is the edge.
---

# /seams — Integration Deep-Dive on the Connective Tissue

A seam is a **joint**: the boundary where one thing hands off to another — a function call, an object's interface, a module import, a producer->consumer data handoff, a Lambda -> SQS -> Lambda chain, an S3 artifact written by X and read by Y, a portal component consuming an API, a full pipeline end-to-end. `/seams` does a **ground-truth deep dive on that joint** and renders a pass/fail verdict on three axes, then puts the analysis **on the record** so the fabric reaches **knowledge parity** (what we believe == what is true) and a seam can be marked genuinely QA'd — not "looks wired."

The unit of analysis is the **seam itself**, never either side alone. Two correct components can still have a broken seam between them (the bug is in the joint), and a seam can "look connected" while carrying nothing, the wrong thing, or a thing nobody remembers correctly. This skill exists to catch exactly that.

Family (each its own thing): **`/molecule`** deep-analyzes a **node** (one unit — what it is, where it sits, does it smell); **`/seams`** (this) pass/fails an **edge** (the bond between two units, on three axes); **`/verify-channel`** runs the delivery/closeout verification *process* (does it deliver fresh usable data; is the project closeable). `/molecule` and `/seams` compose directly — a molecule's chain-position map names the seams to run here; node + edges = the whole graph. All share the grounding discipline below.

---

## Core grounding discipline (binds all three axes)

These are non-negotiable; a "pass" that skips them is not a pass.

1. **Ground truth lives in the DEPLOYED / LIVE / SERVED artifact — never the source, the self-report, or stale memory.** Read the running Lambda package (not the repo), the served S3 object (not the producer log), the live graph (not the doc), the deployed dispatcher (not the committed one). *Committed != deployed; "ran fine" != landed; a prior finding's status != current.* (Banked the hard way: [[reference_reverify_prior_finding_fix_status_against_deploy_not_stale_open_framing]], [[reference_stale_deployed_script_class_and_noncurrent_version_recovery]], [[feedback_verify_against_served_artifact_not_partial_proxy]].)
2. **Exercise-or-evidence, never assume-fires.** A configured path is not a firing path. Either *exercise* the seam (trigger it, observe the effect) or find *evidence it fired* (a real event, an artifact's fresh LastModified, a log of the actual traversal). Config-OK != delivering. (Anchors: SSM EventBridge detail-type matched 0 events while ENABLED; a "verbatim trigger" fired exit=0 but re-materialized nothing.)
3. **Sharpest-test-binds.** Pick the check most likely to fail. If a coarse check PASSes and a sharp check FAILs, the FAIL is the verdict. A coarse-pass that misses a sharp defect launders a broken seam into "QA'd."
4. **Could-not-verify is a finding, not a pass.** If you can't reach the live state (perms, dead runner, missing artifact), report "UNVERIFIED — here is why." Never assume-pass an unreachable check.
5. **Reach for the comp-* tool, not the blind grep.** `comp-which "<question>"` maps a seam question to the canonical call; the per-axis tool tables below are the starting kit. The graph (`comp-kuzu`) answers "does this edge even exist" before you trace by hand.

---

## Step 0 — Define the seam (the unit of analysis)

Before testing, pin down exactly what joint you are examining. State it explicitly in the report:

- **Side A (producer / caller / source)** — what emits or invokes.
- **Side B (consumer / callee / sink)** — what receives or is invoked.
- **The boundary** — the call signature, the import name, the S3 key, the event pattern, the queue, the API route, the contract.
- **The scale** — MICRO (one function call / object interface / import) … MESO (one producer->consumer handoff, one Lambda chain link) … MACRO (a full pipeline end-to-end). Scale sets decomposition (see "Scaling" below).
- **The expected contract** — what is *supposed* to cross this seam (shape, semantics, cadence, owner). This is the yardstick the three axes measure against; capture it from the most authoritative source AND hold it suspect (Axis 2 tests whether the contract itself is true).

A seam you cannot name precisely you cannot QA. If the target is fuzzy ("check the pipeline"), enumerate its constituent seams first and pick.

---

## Axis 1 — MECHANICAL: does the connection physically carry the flow?

**The question:** if A fires, does the control/data *actually traverse* to B and take effect — or does it silently no-op / mis-route / never fire?

**Failure modes this axis catches** (each a real class in this fabric):
- A **name resolves to the wrong target** — `oracle = load_flows_from_transactions()` that now delegates to the windowed path -> a windowed-vs-windowed self-compare ([[reference_entrypoint_delegation_defeats_name_based_oracle_harness_tautology]]).
- A **gate keyed on the wrong value** — a Lambda@Edge origin-response gate keyed on the *pre-rewrite* `/api/scoped/*` URI when it actually sees the rewritten `/gold/*` -> silent prod no-op ([[reference_ledge_origin_response_sees_rewritten_uri_not_original]]).
- An **event pattern that matches nothing** — SSM EventBridge `detail-type`/`document-name` schema mismatch -> ENABLED rule, 0 events, chain never fires ([[reference_ssm_runcommand_eventbridge_detail_type_schema]]).
- A **no-op handler branch** — a delete event -> describe throws -> derive returns None -> nothing written -> stale row (the globgrph DELETE-propagation hole, pre-fix).
- A **var that never reaches the child** — a dispatcher var set without export -> child python uses the lib default ([[reference_bucket_ref_rederive_trace_shared_lib_defaults_not_per_script_grep]]).
- A **path/reference residual** — a split-component or backslash path the substring grep missed ([[feedback_path_rename_sweep_split_component_grep_blind_spot]]).
- **Committed-but-not-deployed** — the fix is in the repo; the running Lambda/runner has the old code.
- A **missing IAM/permission** on a new call -> the cross fails at runtime, not at deploy.

**Method:** trace the *actual* path end to end. Read the boundary code on BOTH sides (does the key A writes == the key B reads? does the call signature match? does the import name resolve to what you think?). Then **exercise-or-evidence**: trigger the seam (or find a real firing) and confirm the effect landed in the live/deployed state. For event/edge seams, prove the pattern matches a real-shaped event (`aws events test-event-pattern`), not just that the rule is enabled.

**Tooling:** `comp-pipescript io` (does the column A emits exist for B; who actually consumes) · `comp-kuzu "MATCH (a)-[:...]->(b)..."` (does the edge exist in the live graph) · `comp-blast` (what actually depends on this) · `comp-routes behaviors` (4xx / edge-rewrite masking) · `comp-iam service|gaps` (the perm to make the call) · download the **deployed** artifact and grep the actual code path.

**Verdict:** PASS = the flow demonstrably traverses A->B and takes effect (exercised or evidenced against live state). FAIL = it no-ops / mis-routes / never fires / fails at runtime — name the exact break (file:line + the live evidence).

---

## Axis 2 — DECLARATIVE: is the map true to the territory?

**The question:** does our *recorded belief* about this seam — its docstring, PRD clause, contract, registry row, TO status, the field's name, a memory, a prior finding — match what the **implementation actually is**? This is the **knowledge-parity** axis.

**Failure modes this axis catches:**
- A **stale docstring** claiming a safety gate that has been removed (the GLDINC `write_load_flows_state` docstring still saying "persists ONLY after a clean scorecard" after the entry went unconditional).
- A **name that lies about the computation** — the LD-0012 class: `capital_gains_ttm` (name says "realized TTM") computed as delta-cumulative-UNREALIZED; a field whose name implies a meaning the code doesn't deliver, cascading to every downstream reader.
- A **status stale vs deployed** — reporting "P1 open" when the fix shipped days ago ([[reference_reverify_prior_finding_fix_status_against_deploy_not_stale_open_framing]] — verified the symptom-count, asserted the fix-status from stale memory; the failure THIS axis exists to prevent).
- **Cross-record drift** — REGISTRY row vs project JSON `status` vs TO `<status>` vs PRD `Status:` disagreeing; a contract field the consumer JOIN reads differently than it was authored (the graph_contracts §3.2-text-vs-WATCH-tier drift).
- A **memory/doc naming a file/flag/function that no longer exists.**

**Method:** read the authoritative *record* (the claim) AND the *implementation* (the truth) and diff them. The truth side MUST be the deployed/live artifact per the grounding discipline — Axis 2's entire job is to catch map-territory drift, so reading the map twice proves nothing. Where the claim and the code disagree, the **code is the territory**; the record is what's wrong (or the code is, if the record encodes a ratified intent the code violates — then it's a mechanical/semantic break, route accordingly).

**Tooling:** `comp-pipescript io` (declared consumers vs actual) · `comp-transform schema-check` (component's declared props vs the data's real shape) · `comp-kuzu` `drift_class` (declared vs observed in the estate graph) · the deployed-vs-committed diff (get-function Code.Location -> grep the signature) · the alignment cross-read (REGISTRY / JSON / TO / PRD).

**Verdict:** PASS = the record and the live implementation agree (knowledge parity holds). FAIL = drift — state the **delta**: "believed X (per <record:line>), actually Y (per <deployed evidence>)." A FAIL here is a knowledge-parity defect; the fix is to **correct the stale record to match reality** (the in-scope repair for alignment metadata; substantive code drift routes to the owner). Bringing the record back to parity is the deliverable, not just noting the gap.

---

## Axis 3 — SEMANTIC: is the payload the correct content, quality-validated?

**The question:** the thing crossing the seam is present and the connection works — but is it the **right** thing, with **validated quality**? Presence and shape are necessary, never sufficient.

**Failure modes this axis catches:**
- **Right shape, wrong values** — a parity break; sum-of-leaves != parent; an incremental that doesn't reproduce the full re-derive (caught by row-for-row content equality, not row-count).
- **Stale vintage** — `data_as_of` frozen while wall-clock advances; a D-1 sentinel keyed to data-day not serving-day ([[reference_d1_pipeline_freshness_fix_rekey_sentinel_not_dateflip]]).
- **Fresh + present + valid-float but SEMANTICALLY wrong** — the BMKAUD class: a SmartX override replaced the canonical benchmark and a `1M`-definition mismatch shipped; structurally fine so no alarm fired, caught only by eye. This is the highest-value catch — structure passes, meaning is wrong.
- **Magnitude / sign sense-check failure** — a `-$54.8M capital_gains_ttm` on a ~$200M book; a "growth" metric coming out wrong-signed; a number whose magnitude doesn't fit the book/asset-class/prior-value.
- **Units / grain mismatch** — bucket-grain matching where object-grain is meant (the co-tenant false-positive class); a join at the wrong granularity.
- **Transport degradation** — a 32MB JSON served raw past the CloudFront 10MB auto-compress cap, or a gzip assumed that wasn't ([[reference_cloudfront_10mb_autocompress_cap_large_json_needs_origin_gzip]]).
- **Over/under-processing** — an over-dedup dropping rows (int-vs-str key); a silver slim that dropped a field.

**Method:** validate the *content*, not the envelope. Read the served/live payload and run the sharpest applicable check: parity/reconciliation (sum-to-parent, inflows−outflows==nna to the cent, `all_pass` flags), vintage (`data_as_of` vs the firm-wide settled date, cross-checked against siblings), magnitude/sign sense (does the number make sense for the book/scale/prior?), name-vs-semantic (does the field's name match what the code computes?), units/grain, decision-usefulness for the actual consumer. The META-CHECK heuristic (magnitude / sign / naming-vs-semantic) is the SCAN; a mechanically-functional output that fails it IS NOT a success.

**Tooling:** read the served object + parity-check it yourself · `comp-validate <script> --artifact <file>` (the producer's value config; PASS/WAIVED safe, NO_CONFIG/ZERO_CHECKS = UNVALIDATED) · the value-layer contract (`period_defs` / graph_contracts value limb) · S3-version diff for content equality across a cutover.

**Verdict:** PASS = the payload is the correct content with validated quality and is decision-useful to B. FAIL = wrong values / stale / semantically-off / wrong-grain / degraded — cite the sharp check that failed and the expected-vs-actual.

---

## The seam report (the output — "on the record")

Write a report so the seam's QA is **citable** and the knowledge-parity delta is preserved. Default location: the invoking agent's `logs/{YYYY-MM-DD}/seams_{HHMMZ}_{seam-slug}.md`. For a **critical or recurring seam**, also (or instead) write a durable entry under `org/seams/{seam-slug}.md` so verified seams accrue into a reusable knowledge base. Commit under your own author line via `.tools/safe-commit.sh`.

Structure:

```
# SEAM: <A>  ->  <B>   (scale: MICRO|MESO|MACRO)
**archetype:** VALIDATE   (or TRACE/DIAGNOSE per dominant work)

## Seam definition
- Side A / Side B / boundary / expected contract (and where the contract is recorded).

## Axis verdicts
| Axis | Verdict | Evidence | Delta (if FAIL) |
|---|---|---|---|
| MECHANICAL  | PASS/FAIL/UNVERIFIED | <live/deployed evidence, file:line> | <the break> |
| DECLARATIVE | PASS/FAIL/UNVERIFIED | <record:line vs deployed truth>     | believed X, actually Y |
| SEMANTIC    | PASS/FAIL/UNVERIFIED | <sharp content check + expected/actual> | <wrong-thing> |

## Knowledge-parity delta
What we BELIEVED about this seam vs what is TRUE. What record was corrected (commit) / routed to the owner.

## Verdict
SOUND (all 3 PASS) | BROKEN@<axis> | UNVERIFIED@<axis> (why).

## grounding: field (Rule 22 — per CAUSAL claim)
A payload/state finding (the value crossing the seam, the live evidence on any axis) is STATE — grounded vs the deployed/served artifact, no field. But any MECHANISM/causal claim — a "the seam carries the wrong thing / doesn't connect BECAUSE X" on any axis, a root-cause for a FAIL — carries `grounding: SOURCE-CONFIRMED <file:line | comp-tool+output>` or `grounding: INFERRED (live-state-only)`. An INFERRED mechanism may PROMPT a source-check but is non-actionable and may NOT use the reserved words (proof / provably / root cause / definitively); absent field on a causal claim = not-accepted. Spec: `org/tier1_exec/3.0.0_SA_CVO/GROUNDING_FIELD_EMISSION_FORMAT.md` (Rule 22 / 53919cb32).

## Residual / unknowns
What was NOT exercised (e.g., "code deployed but not proven on a live event"), what's still owed.

## Compiler Tools
<the comp-* runs per axis + results>
```

**Overall verdict rule:** a seam is **SOUND only when all three axes PASS.** Any FAIL = the seam is broken *at that axis* (name it). Any unreachable check = UNVERIFIED *at that axis* (never silently upgraded to PASS). Knowledge parity is reached when DECLARATIVE passes AND the report is on the record.

---

## Scaling — micro to macro

- **MICRO (one function / object / import):** run the 3 axes directly on the single boundary. Fast, surgical. Most "is this call wired right" asks.
- **MESO (one handoff / one chain link):** run the 3 axes on the producer->consumer pair; the boundary is the S3 key / queue / event / API route.
- **MACRO (full pipeline):** **decompose into its constituent seams** (producer -> S3 -> dispatcher -> runner -> served -> frontend, each link a seam), then run `/seams` on each. Use `comp-estate --resource <name>` / `comp-pipescript` to enumerate the links so none is a silent Unknown. **Weakest-seam-binds:** the pipeline is SOUND iff *every* constituent seam is SOUND on all three axes; the pipeline's verdict is its weakest seam. Call `/verify-channel` for the data-delivery legs (freshness) and fold its result into that seam's SEMANTIC axis.

A chain is exactly as sound as its least-sound joint — and the joints are where "everything looked fine" hides.

---

## Invocation

| Form | Meaning |
|---|---|
| `/seams <target>` | Deep-dive the seam(s) of a function / object / artifact / pipeline. If `<target>` is a single component, examine its inbound + outbound seams; if a pipeline, decompose + run each. |
| `/seams <A> -> <B>` | Examine one directed seam explicitly. |
| `/seams <target> --axis mechanical\|declarative\|semantic` | Run a single axis (e.g., a fast mechanical-only "does it even connect"). Default = all three. |

Not a cron / not a loop — invoked on demand for a deliberate integration deep-dive. Any agent may run it; CVO and verification-minded agents are the primary users. It does not fix code (verifier discipline) — it renders verdicts, corrects stale *records* to parity (the declarative repair), and routes code/runtime fixes to the owning lane with a grounded, mechanism-specific finding.

---

## One-line reminder

A seam can look connected, carry nothing, carry the wrong thing, or carry the right thing nobody remembers correctly. `/seams` proves which — mechanically, declaratively, semantically — against ground truth, and writes the answer down so the fabric knows it for real.
