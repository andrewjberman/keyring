# SPEC — comp-blast re-based onto the canonical Kuzu graph

**Author:** 3.0.0_SA_CVO · **Date:** 2026-08-03 · **Assignee:** `0.7.0_AE_CloudOps~A`
(Andrew-instantiated for this build; assignment Andrew-direct at the CVO terminal, verbatim:
*"sure write the spec and hand it directly to 0.7.0_AE_CloudOps~A, who I am instantiating now"*).
**Authority chain:** ANDREW_RULING_projections_default_kuzu_full_graph_20260803.md (same DIR:
ruling + fix-first addendum, both verbatim). **Verifier:** CVO owns the acceptance battery and the
CLOSE verdict; this build also CLOSES the comp-blast dial left at 8/9 phases on 2026-07-31.
**Citation vintage:** repo file:line refs @03ff36daee unless noted; kuzu measurements from the
2026-08-03T21:24:05Z build (nodes snapshot-id 5232881198863681668).

---

## 1. The ruling this implements (binding)

All comp-tool projections default to the KuzuDB full resource graph (or a declared
territory-specific full graph). Hand-drawn registries/amalgamations are legal ONLY as extremely
explicit, intentional exceptions. **comp-blast must cover ALL of AWS.** Fix and test comp-blast
FIRST; test must prove it uses kuzu.

## 2. Measured current state (all OBSERVED 2026-08-03)

- `org/modules/graph/trace_graph.py:402` `build_graph()` — comp-blast's universe is a PRIVATE
  trace graph: 8 accreted extraction passes (S3 regex mapper, API routes, EventBridge,
  Lambda->EC2 SSM, Lambda routes, hardcoded BD+INF pipeline-DAG injection @V4.020, SFN invoke
  @GRAPHUNI.SFNBRIDGE, live event-source-mappings). 2,255 nodes / 2,950 edges, ~35s cold build,
  exactly 4 S3_BUCKET nodes (bd / inf / portal-v2 / assets).
- Failure that triggered the ruling: NOT-FOUND on `opal-data-mdpf` (a real production bucket,
  live consumers verified same session) while `comp-kuzu` resolved it as a CloudNode.
- Canonical graph (`comp-kuzu`, kuzu_nessie_db): **20,480 CloudNode / 40,945 CloudEdge**, 02:00Z
  full re-derive + CloudTrail event-driven incremental, per-call provenance header. Node schema:
  `node_id (PK) / arn / node_type / name / layer / drift_class / source / snapshot_ts / props`.
  Edge schema carries `edge_type`. node_type census (top): Field 4969, MS_FILE 4672, JSXElement
  2205, JSXRender 1433, PipelineFunction 1201, MS_FOLDER 1043, TypeDecl 807, IAM_POLICY 449,
  ReactComponent 442, Module 374, Prop 359, LOG_GROUP 235, S3Key 232, Component 199, IAM_ROLE
  198, LAMBDA 193, EVENT_RULE 142, PipelineScript 133, Endpoint 125, Hook 111, DataFetch 106.
  edge_type census (top): CONTAINS 12394, OWNED_BY 5947, HAS_FIELD 4269, RENDERS 2447,
  READS_FIELD 2110, CALLS 1623, PROP_PASSES 1382, DECLARES 1344, INSTANTIATES 1298,
  REFERENCES_TYPE 1129, FLOWS_TO 961, READS 704, HAS_POLICY 581, WRITES 551, PROJECTS_TO 442.
- CVO analysis, Andrew-accepted: **no property of the trace graph justifies a private universe.**
  The ONE preservable property is invocation-time HEAD-PINNING — the trace build re-derives from
  the CURRENT WORKING TREE when source drifts (exercised live this session: 3-node SHA drift ->
  cache discarded -> rebuilt before answering). Kuzu is 2-6h behind and models committed/live
  estate, not the mid-edit tree — and "what breaks if I change X" is a mid-edit question.

## 3. Target architecture

1. **UNIVERSE = the canonical kuzu graph.** Node existence, the denominator, node typology, and
   estate-wide consumer/producer traversal all answer FROM kuzu. No node that kuzu carries may be
   NOT-FOUND in comp-blast. The AWS territory comes along entire (LAMBDA, EVENT_RULE, S3 buckets
   AND S3Key grain, DYNAMODB, IAM, LOG_GROUP, ...); other territories (GIT code plane, MS_CLOUD)
   ride free — do not filter them out.
2. **SUBJECT-SCOPED WORKING-TREE OVERLAY** (the preserved head-pin): at invocation, re-derive the
   blasted SUBJECT's local edges from the current working tree (scoped reuse of the existing
   extraction passes — seconds, not the 35s whole-tree scan) and overlay them. Overlay wins on
   the subject's own edges; kuzu wins on everything else. This keeps mid-edit answers current,
   including uncommitted state.
3. **DUAL PROVENANCE, ALWAYS PRINTED:** every comp-blast emission carries BOTH vintages — the
   kuzu snapshot line (as comp-kuzu already prints) AND the overlay's worktree state (HEAD +
   dirty-flag + subject-files hash). A single-vintage answer is a P3 conformance failure.
4. **DECLARED EXCEPTIONS ONLY:** if any hand-maintained sub-registry survives inside the
   projection (it should not need to), it is DECLARED in the output per the ruling's exception
   clause — named, vintaged, and scoped. Undeclared amalgamation = defect.
5. The private trace graph RETIRES as a universe. Its extraction passes live on only as the
   overlay's scoped derivers (or are absorbed/deleted — deletions are RULED per the residue
   discipline, route to Andrew via the dial's P7 when reached).

## 4. Behaviors that MUST survive unchanged (cut baselines BEFORE touching anything)

- **Exit-code contract (disjoint):** 0 clean / 1 TOOL-FAILED only / 2 stale / 3 not-found /
  4 phantom-consumer verdict. `org/modules/graph/tests/test_blast_exit_code_contract.py` (7
  tests, mutant-verified) must pass at every commit of this build. Marker strings callers key on
  (`PHANTOM-CONSUMER:` / `CONSUMER-OK:`) unchanged; `comp_debt/grounding_lib.py` rc mapping
  (4 -> ZERO_CONSUMER, 1 -> UNKNOWN, never crash->evidence) unchanged.
- **NOT-FOUND shape:** denominator + universe boundary + near-matches + "not a 'nothing breaks'
  clear" — now with the KUZU census as the denominator. Per Andrew (same session, verbatim in
  the dial ledger): near-matches are re-labeled as **duplicate/legacy candidates**, not merely
  typo candidates.
- **Freshness contract:** default serve-iff-fresh / `--check` report-only (0 fresh | 2 stale |
  1 error) / `--force` re-derive. The predicate stays ONE expression shared with the status
  surface (cli.py freshness-contract block). `--fresh` deprecation WARN stands.

## 5. Known defects to fix IN THIS WINDOW (from the 07-31 dial, all still live @03ff36daee)

(a) cp1252 `UnicodeEncodeError` — currently made SAFE (rc=1, 20 of 2,255 nodes, cli.py:378->:364);
    fix the ROOT (ASCII-only emission per CLAUDE.md Code Quality), not the wrapper.
(b) `--direction up` inverts `--check-consumers` into a false phantom (rc=4 on a node with real
    consumers). Direction and verdict must compose correctly or the combination must refuse loudly.
(c) substring `find_node` + `matches[0]` answers about a DIFFERENT node at rc=0 — the silent
    wrong-subject class. Required: exact match answers; ambiguous substring LISTS matches and
    refuses to pick silently (distinct rc, not 0).
(d) upstream traversal does not follow FETCHES edges — 6 real component callers reported as 0.
    With the kuzu universe this likely dissolves into edge_type mapping — prove it with the
    regression, don't assume it.

## 6. Acceptance battery (CVO-owned; build against these — the battery runs before CLOSE)

1. **Universe conformance:** `comp-blast opal-data-mdpf` resolves (non-NOT-FOUND); the S3-bucket
   node census equals kuzu's (count AND names); spot-set of node_types (LAMBDA, EVENT_RULE,
   S3Key, DYNAMODB_TABLE, MS_FILE) present in the projected universe.
2. **Freshness overlay:** mutate a fixture script's write-target in the working tree (no commit);
   same-invocation blast on that subject reflects the mutation; revert; reflects the reversion.
3. **Exit-code contract:** 7/7 green, plus the mutant (revert the rc=4 mapping -> the suite must
   FAIL). A suite that cannot fail is not a gate.
4. **Negative control:** a bogus node -> rc=3 NOT-FOUND carrying the KUZU denominator; a node
   present in kuzu but absent from the old trace graph (opal-data-mdpf is the canonical instance)
   -> full blast answer.
5. **Defect regressions:** one failing-direction test per (a)/(b)/(c)/(d), banked into the suite.
6. **Boundary declaration (SYSTEM_DEFINITIONS conformance):** the tool declares address_space
   (kuzu vintage + overlay scope), traversal_residue, presentation_residue, failure_direction.
7. **Registration invariant:** `comp-manifest-check completeness` passes;
   `org/modules/graph/comp-output-contracts.yaml` updated with the new universe + dual-provenance
   contract and the change rationale.

## 7. Constraints

- Repo-side tooling only (`org/modules/graph/`): no Terraform/Lambda/EC2 leg, no deploy ledger
  (the 07-31 fix set the precedent — say so in the log so the ledger keeps meaning what it means).
- Live-AWS reads: read-only boto only, graceful no-creds no-op (pass-8 precedent). NO new alerts/
  SNS/SES/monitors (moratorium). ASCII-only output.
- Commit via `.tools/safe-commit.sh` under your author line; every .py passes commit-gate.
- Performance: cold path should IMPROVE (query vs 35s scan); if any path regresses past the
  current 35s cold build, say so with numbers rather than absorbing it silently.
- If kuzu is unreachable/stale beyond its own contract at invocation, comp-blast FAILS LOUD with
  the kuzu provenance verdict — it must NOT silently fall back to a private scan (a silent
  fallback re-creates the exact defect this spec removes).

## 8. Reporting (RAVC)

ACK on receipt. Build with evidence (commit hashes, test output, before/after probes). Report to
CVO for the battery run + CLOSE verdict — that verdict also closes the comp-blast DIAL record
(unclosed since 07-31; the DIAL record synthesis rides this close, committed this time). CC CTO
(routing owner) on completion. Andrew holds two open naming acts that DO NOT block this build:
comp-blast's formal purpose line (P1) and the `chain` reserved-term collision.

— 3.0.0_SA_CVO
