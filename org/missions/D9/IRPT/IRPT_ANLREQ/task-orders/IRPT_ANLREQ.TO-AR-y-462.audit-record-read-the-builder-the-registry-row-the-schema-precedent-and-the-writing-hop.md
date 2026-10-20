# TO IRPT_ANLREQ.TO-AR-y-462.audit-record-read-the-builder-the-registry-row-the-schema-precedent-and-the-writing-hop -- READ ONLY: for contract C-AUDIT-RECORD (PRD v0.25), find how a new S3 family gets its builder-made address, where a registry row is added, which JSON Schema precedent a consumer rejects against, and which hop of the producer knows the four linkages; no code is edited

<to_id>IRPT_ANLREQ.TO-AR-y-462.audit-record-read-the-builder-the-registry-row-the-schema-precedent-and-the-writing-hop</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~327</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ121</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a read of source; one record file) | **Decomp cell:** `AR-y-462` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** the audit record of PRD v0.25 (contract C-AUDIT-RECORD, CTO ruling R3) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~327`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-327` (branch `wk-IRPT_ANLREQ-327`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~327 <0.9.0_WK_IRPT_ANLREQ~327@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W327-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields.
- **No AWS call, no network, no code edit, no push, no deploy.** Read with the Read and Grep tools; for a repo-wide name search use Grep with a `glob`, never a recursive shell grep. The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first), with `to_id` exactly the order's id; run `python .tools/proof-of-spec-check.py <instance> "AR462-y-AC1,AR462-y-AC2,AR462-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID.

### THE CELL (`AR-y-462`, inlined)

*Context.* PRD v0.25 (`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md`, the row beginning `C-AUDIT-RECORD:`) says: one audit JSON per analysis request, a NEW `analysis-report` family beside `ycharts_runs` (run.json unchanged; LGIC R19), in each firm's bucket at a builder-made address, with a published JSON Schema that a consumer rejects a malformed record against; four linkages (the ticket, the form as filed, the filer, the package and commentary pointers); retention 2,555 days from filing. Every new S3 address is `lib/opal_naming.py` `address()` output and every resource name is `name()` output (CLAUDE.md rule 30; `infra/logic/02_DOCTRINE.md` R1-R21; registry rows under `infra/logic/registry/`).

*The read.* Write `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~327/AUDIT_RECORD_READ.md` with exactly these four sections, each heading starting `## S1 `, `## S2 `, `## S3 `, `## S4 `, every claim carrying a `path:line` cite read in this worktree:
- **S1 the builder and the family:** how `address()` is called for an existing family that sits beside this one (`ycharts_runs` and its neighbours): the call, its arguments, the registry row that backs it (file and row), and exactly which registry file gets a new row for an `analysis-report` family and what fields that row needs; whether a builder refusal on an unknown family is mechanical (name the check).
- **S2 the tenancy and retention:** how each firm's bucket and prefix is resolved for a family (per-firm buckets or a shared bucket with a key-prefix), where a lifecycle or retention rule for a family would be declared (the Terraform or registry place, not an edit), and what the existing precedents use for retention days.
- **S3 the schema precedent:** an existing published JSON Schema in this repo that a consumer rejects a malformed record against (name the schema file, the consumer that validates it, and the validator library), and whether that library is importable in the investor-reporting resident's environment (read its requirements or imports; say what you could not read).
- **S4 the writing hop:** which function of the producer or the ticket-attach path first holds all four linkages (ticket id, the form as filed, the filer, the package and commentary pointers) and which later hop is the last that still can write one record per request; the two or three candidate hops with the reason each fits or fails, and the one question you could not answer from source.
End the file with one line `NOT-READ: <what you did not or could not read, or none>`.

---

## ACCEPTANCE

<criterion id="AR462-y-AC1" cell_refs="AR-y-462"><invocation>grep -c -E '^## S[1-4] ' org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~327/AUDIT_RECORD_READ.md</invocation><expect>^4$</expect></criterion>
<criterion id="AR462-y-AC2" cell_refs="AR-y-462"><invocation>grep -c -o -E '[A-Za-z0-9_./-]+\.(py|json|tf|md):[0-9]+' org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~327/AUDIT_RECORD_READ.md</invocation><expect>^([89]|[1-9][0-9]+)$</expect></criterion>
<criterion id="AR462-y-AC3" cell_refs="AR-y-462"><invocation>grep -c -E '^NOT-READ: .+' org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~327/AUDIT_RECORD_READ.md</invocation><expect>^1$</expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~327/IRPT_ANLREQ.TO-AR-y-462.audit-record-read-the-builder-the-registry-row-the-schema-precedent-and-the-writing-hop.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-462.audit-record-read-the-builder-the-registry-row-the-schema-precedent-and-the-writing-hop`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR462-y-AC1,AR462-y-AC2,AR462-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-462</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~327/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-462.audit-record-read-the-builder-the-registry-row-the-schema-precedent-and-the-writing-hop.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of source and one record file in the worker deliverables; no code edit, no AWS call, no deploy.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the PRD v0.25 ADDENDUM and the C-AUDIT-RECORD row against this cell; the lens: a cite to a line that does not carry the claim (every cite must be re-read at the line), a family invented because the row names it, a registry file that does not back the builder, a validator that exists in the repo but not in the resident. NOT seen (blind): the deployed bytes and the live buckets; denominator: four sections.
</preflight>
