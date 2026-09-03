# TO NFRA_CLDGRPH.TO-CG-C-3 -- the DERIVER REPORTS READ STATE HONESTLY: a failed S3 notification read is UNREADABLE, never zero; the S3_BUCKET-[TRIGGERS]->LAMBDA edge derived from the declared Terraform resources as a second source; a read-versus-unreadable denominator on every build -- the round-2 stamp's SPEC_ERROR route of row S20 (the base CVO's handoff of NFRA_COMPEFFICACY-S15)

<to_id>NFRA_CLDGRPH.TO-CG-C-3</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.8.0_AE_CloudComp~O</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<issued_date>2026-09-03</issued_date>
<status>pending -- GO paired at cut (2026-09-03 ~18:3xZ). ROUND 3 of NFRA_CLDGRPH, cut in the tick that read the round-2 stamp (spine L10 -> L6) against the cell the decomposition added at v0.2 for exactly this route: CG-s-14. The seat is a CODEX lane of the graph engine home's role (`org/modules/graph/comp_*.py` is `0.8.0_AE_CloudComp`'s lane), seated by the issuer this tick. The assignee commits its own status flip after a VALID proof-of-spec instance; the L8 seat reads the record.</status>

**Directive:** D0 · **Fabric:** laptop · **PRD:** `../prd/NFRA_CLDGRPH_PRD.md` v0.4 @`25c66d3358` (R5: the projection re-publishes what the deriver produces; FWD-2, FWD-4) · **Decomp cell:** `CG-s-14` (`../decompositions/NFRA_CLDGRPH_DECOMP.md` v0.2, added at changelog 0.2 on the stamp's route) · **Stamp:** `../surprise-channel/remediations/REMEDIATION_v2.md` @`0c72b64180`, row S20 -- `route: SPEC_ERROR`, `loop_target: 6`, `owner: 2.0.0_SA_COO~A`; remedy verbatim: "Represent a failed notification read as UNREADABLE rather than zero, derive declared S3-to-Lambda notification targets from Terraform as a second source, and publish read-versus-unreadable denominators on every build." · **Lane:** `org/modules/graph/**` (the graph engine home; `0.8.0_AE_CloudComp~O` PERMITTED, measured at the cut) + the deliverable at `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.8.0_AE_CloudComp~O/` · **Rule 27 seating:** `0.8.0_AE_CloudComp~O`.

---

## THE CELL -- the measured defect and the shape of the fix

Measured by `0.8.0_AE_CloudComp` under NFRA_COMPEFFICACY (row S15 @`a140eed779`), carried to this project by the base CVO (record @`b5d228fe62`) and filed here as S20 @`72c0022be8`: on the live graph, `MATCH (b:CloudNode)-[e:CloudEdge]->(l:CloudNode) WHERE b.node_type='S3_BUCKET' AND e.edge_type='TRIGGERS' AND l.node_type='LAMBDA'` returns 0 rows while the estate declares real `aws_s3_bucket_notification` resources with Lambda targets (bd-pipeline, cot-pipeline, inf-pipeline); `opal-data-bd` is an S3_BUCKET node with zero outgoing TRIGGERS edges against three declared targets; a forced refresh does not change it. Cause at source: `org/modules/graph/comp_aws_cli.py:1439-1447` (`derive_edges`) -- `get_bucket_notification_configuration` inside a bare `except: pass`, with the node-property twin at `:273-279` in the same shape. A failed read equals a genuine zero, and the ported projection now re-publishes that zero under a fresh vintage every night. The consumer that needs the edge: `comp-trigger`'s PARTIAL_OR_BLIND state (NFRA_COMPEFFICACY's FWD-2 limb reads fixture-covered until this derives honestly).

## DELIVERABLE

1. **THE READ STATE** in `derive_edges` and the node-property twin: a failed `get_bucket_notification_configuration` (an exception, an AccessDenied, a timeout) is recorded as UNREADABLE for that bucket -- never an empty configuration -- and the build's summary prints the denominator `buckets read / buckets unreadable` with the unreadable names; the same for any sibling read in the two blocks that swallows into zero (census them; the bare `except: pass` count before and after, with the file:line list).
2. **THE SECOND SOURCE**: the S3_BUCKET-[TRIGGERS]->LAMBDA edge derived ALSO from the declared `aws_s3_bucket_notification` resources in the estate's Terraform (`infra/aws/terraform/**`), tagged with its provenance (`live` / `declared` / both), so a live read that fails leaves the declared edge standing and the two sources' disagreement is visible on the edge, never silently reconciled.
3. **THE ENGINE, NOT A COPY**: the fix lands in the deriver the derive runner and the incremental updater run (the same `comp_aws_cli.py`); no second deriver, no shadow output; the derive runner's next real run publishes the honest edge through the existing path (marker -> Pipe -> worker). No Terraform, no resource, no deploy of the deriver's runtime by this cell -- if the deriver runs from an image that must be rebuilt for the fix to reach the cloud, say so on the row and the issuer routes it; the fix is exercised locally against the live account in any case.
4. **EXERCISED:** (a) the live derive of the three declared targets returns NON-ZERO TRIGGERS edges (the three quoted with their provenance); (b) the denominator printed on a real build (read / unreadable, names); (c) THE CONTROL THAT CAN FAIL: a planted denied read (a bucket name the caller cannot read, or a stubbed refusal in a test seam that never touches AWS) reports UNREADABLE with the denominator moving by one, and the edge count for that bucket is not zero-by-silence; the pre-fix code on the same plant reports zero (the before/after contrast).
5. **THE DELIVERABLE FILE** `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.8.0_AE_CloudComp~O/CG-s-14.deriver-read-state.result.md`: one fenced JSON block (the census of swallowed reads before/after with file:line, the three edges with provenance, the denominator line, the plant's before/after) plus prose, and a HANDOFF line for NFRA_COMPEFFICACY's `comp-trigger` limb (which the base CVO named as the consumer).

## ACCEPTANCE -- criterion ids minted at cut; the assignee files the proof instance

<criterion id="C3-AC1" cell_refs="CG-s-14"/> `C3-AC1` -- THE READ STATE: no failed notification read collapses to zero in `derive_edges` or the node-property twin; the census of bare-except swallows before and after with `file:line @ commit`; the denominator line on the build.
<criterion id="C3-AC2" cell_refs="CG-s-14"/> `C3-AC2` -- THE SECOND SOURCE: TRIGGERS edges derived from the declared `aws_s3_bucket_notification` resources with provenance on the edge; a live/declared disagreement visible, never reconciled silently; `file:line @ commit`.
<criterion id="C3-AC3" cell_refs="CG-s-14"/> `C3-AC3` -- EXERCISED on the live account: the three declared targets derive NON-ZERO (quoted with provenance) and the denominator prints on a real build; the pre-fix zero shown as the before.
<criterion id="C3-AC4" cell_refs="CG-s-14"/> `C3-AC4` -- THE CAN-FAIL ARM: a planted denied read reports UNREADABLE, the denominator moves by one, no zero-by-silence; the plant never touches a real bucket's configuration.
<criterion id="C3-AC5" cell_refs="CG-s-14"/> `C3-AC5` -- ONE ENGINE: no second deriver or output path; the runtime question (does the fix reach the cloud deriver without an image rebuild) answered on the record, routed as a row if it needs an act outside this cell; `.tools/commit-gate.sh` clean on every .py touched.
<criterion id="C3-AC6" cell_refs="CG-s-14"/> `C3-AC6` -- PUSH STATE MEASURED at report (never a push); the proof instance VALID (`.tools/proof-of-spec-check.py` rc 0) with every `surprises` entry resolving to a row (S20 at its commit plus any new row) BEFORE the complete flip, which this seat commits itself; the handoff line for `comp-trigger`.

<expected_criteria>C3-AC1, C3-AC2, C3-AC3, C3-AC4, C3-AC5, C3-AC6</expected_criteria>

## SURFACES

`org/modules/graph/comp_aws_cli.py` (`:273-279`, `:1439-1447` at HEAD; re-locate by content) · the derive runner (`infra/aws/globgrph/derive_runner.py`) and the incremental updater as the deriver's callers (READ only) · `infra/aws/terraform/**` `aws_s3_bucket_notification` resources (the second source; READ only) · `comp-find --corpus aws` (the live graph, its own `built:` vintage) · rows S20 @`72c0022be8`, NFRA_COMPEFFICACY-S15 @`a140eed779`, the handoff @`b5d228fe62`, the stamp @`0c72b64180`.

## BOUNDS

- **The graph engine home only** (`org/modules/graph/**`); no change under `infra/aws/globgrph/**` or any Terraform; no resource, no deploy, no apply.
- **Read-only against AWS** except the derive's own reads; the plant never writes or changes a bucket's configuration; no marker write.
- **No second deriver, no shadow output path** (CLAUDE.md s.5); the honest edge reaches the projection through the existing path on the next real stamp.
- **No alarm, SNS, checker or monitor.** **A spec-vs-world divergence is a ROW** at `../surprise-channel/investigations/INVESTIGATION_v1.md` (append-only; id minted at commit; correct the header denominator); a BLOCKING row also to the issuer same turn; never message a CVO seat. **No `git push`, under this or any order.** Commit via `.tools/safe-commit.sh --author "0.8.0_AE_CloudComp~O <0.8.0_AE_CloudComp~O@opal.agent>" -F <msgfile>`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> @70918d5d2b (v0.2, changelog 0.2), cell CG-s-14 (added on the stamp's route of S20).
<owned_cells>CG-s-14</owned_cells>
Read-dependencies, NOT claimed: CG-s-2 (the worker that re-publishes the derived graph), CG-x-2 (the daytime limb this edge feeds).
</decomp_ref>

<preflight>
comp-schedule: RUN -- GATES ARMED 21 across 5 carriers (C1 sentinel denominator 21 -> 5, C2 deploy-ledger 4 -> 4, C3 moratoria 12 -> 12, C4 scope-guard 20 SEMI-DECIDABLE -> 0, C5 project-blocking 337 NOT-DECIDABLE -> 0); 138 prose blocking fields NEEDS-READ; 0 armed gates name NFRA_CLDGRPH, globgrph, kuzu, opal-gateway or projection (read 2026-09-03 18:11:28Z, this tick).
comp-iam: RUN -- DECLARED-NOT-APPLICABLE with the reason on its own line: this cell creates or changes no principal, policy or resource (the graph engine home only; the derive runs under the caller's existing identity); the DESIRED plane read at cut (18:12Z) is unchanged at 14 / 292 / 0 / 2 gaps and stays so.
comp-adversary: RUN -- rc 0 at read-vintage @68d7f16a6c (2026-09-03T18:32:00Z, --no-packet: stage 4 disabled by the caller, disclosed); pins found 5 commits, 5 repo paths, 1 file:line cite, 7 tool mentions; cited commits 5 attempted / 5 verified / 0 UNVERIFIABLE; cited paths 5 attempted / 3 stable / 2 flagged (both GONE at read-vintage = the deliverable file and the proof instance this TO CREATES); uncited siblings 231 with the cap (25) declared; complement sources 4 run / 0 deferred / 5 declared-excluded (v1 contract). The decomposition vintage @70918d5d2b landed after this compose; the face cites it by hash.
lane: RUN -- owned-paths-validate --check-agent 0.8.0_AE_CloudComp~O on org/modules/graph/comp_aws_cli.py and the deliverables folder: 2 of 2 PERMITTED, 0 violations (read 2026-09-03 18:22Z); the seat 0.8.0_AE_CloudComp~O launched via ajb2 at 18:30:12Z (lane O never used on 0.8.0_AE_CloudComp, spawn-audit census).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `C3-AC1`..`C3-AC6`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.8.0_AE_CloudComp~O/NFRA_CLDGRPH.TO-CG-C-3.deriver-read-state.proof_of_spec.json`
and validates it with `.tools/proof-of-spec-check.py` BEFORE the complete flip, which the assignee commits itself. C3-AC4's plant is the
arm that must be able to FAIL.
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `comp-read org/modules/graph/comp_aws_cli.py --for "every read of a bucket's notification configuration and every bare except around an AWS read in derive_edges and the node-property derivation"`; `comp-read org/modules/graph/comp_aws_cli.py --enumerate 'except:\s*$|except Exception|pass$'` for the swallow census with its denominator; `comp-find --corpus aws 'TRIGGERS'` for the live edge count (the DB's own vintage). AFTER: `.tools/commit-gate.sh` on every .py touched; `.tools/proof-of-spec-check.py`; `git ls-remote` + `is-ancestor` for C3-AC6.
</compiler_tools_mandate>

**DELIVERABLE REPORT:** to `2.0.0_SA_COO~A` with per-criterion evidence, the census numbers, the three edges with provenance, the plant's before/after, and push state as MEASURED. GO = this TO + the dispatch message.
