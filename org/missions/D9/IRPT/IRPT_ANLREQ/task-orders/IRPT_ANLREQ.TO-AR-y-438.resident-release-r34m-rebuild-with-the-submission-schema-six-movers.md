# TO IRPT_ANLREQ.TO-AR-y-438.resident-release-r34m-rebuild-with-the-submission-schema-six-movers -- BUILD ONLY: rebuild the r34m resident tarball with ONE more member, the submission schema AnalysisSubmissionRequest.schema.json at the pin's blob (the running resident's copy forbids the field commentary_requested that every filing carries), so exactly six members move against the running r34l; nothing is uploaded, installed, applied or run on a host

<to_id>IRPT_ANLREQ.TO-AR-y-438.resident-release-r34m-rebuild-with-the-submission-schema-six-movers</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~317</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ97</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a build in a stage folder outside the repository; the only repository writes are the worker's deliverables) | **Decomp cell:** `AR-y-438` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (any filing reaches the resident), O5 | **depends_on:** AR-y-430 (r34m, merged 7f498fe48ec; its tarball d9be3cea... is superseded and never uploaded); IB2 read A_COMPOSITION_REFUSAL.txt (the resident journal: COMPOSITION-REFUSED step=2 class=ValidationError, twice); the issuer's measurement (below); CTO msgs 11190 and 11192

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~317`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-317` (branch `wk-IRPT_ANLREQ-317`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~317 <0.9.0_WK_IRPT_ANLREQ~317@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W317-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/IRPT_ANLREQ.TO-AR-y-406.resident-release-r34l-build-only-two-movers.proof_of_spec.json` (read it first; `git show HEAD:<path>` if absent), with `to_id` exactly the order's id, a `controls.mutant` that FIRES (named in the cell) and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "<ids>"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (commit alone) only on VALID.

### THE CELL (`AR-y-438`, inlined)

*Context and the measured cause.* Run 5B's request was refused by the resident twice with `SubmissionRefused("CLOSED_COMPOSITION_REQUIRED")` at step 2 (SCHEMA) of `CompositionAdmission.validate`. The issuer validated the request composition the run left (a synthetic object, staged read-only for you at `C:/dev/irpt-inputs-r35f/composition_run5b.json`) against the schema set INSIDE the running r34l tarball (`C:/dev/irpt-release-r35d/irpt-resident-0485393f3a-r34l.tar.gz`, members `docs/contracts/investor-reporting/v1/*.schema.json`): exactly one error, `additionalProperties` at `browser` (`commentary_requested` unexpected). The running copy of `docs/contracts/investor-reporting/v1/AnalysisSubmissionRequest.schema.json` is the base-pin blob `a7370fcd237...`, whose `additionalProperties` is false and which lacks `commentary_requested` (added at trunk by IB-pr-455 on 2026-10-11); trunk's blob is `92cc5673589...` (the same at the r34m pin `7f1eab530cde4661e9a559bf45439ebdbf73dab2`). The portal and every run send `commentary_requested`, so no filing can pass the resident until its copy moves. The r34m tarball you built under AR-y-430 (`C:/dev/irpt-release-r35e/irpt-resident-0485393f3a-r34m.tar.gz`, sha256 `d9be3cea9fde...`) carries the OLD schema member too, so it is superseded; it was never uploaded.

*The builder.* `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/build_resident_package.py` takes a member at another commit through `--override REPO_PATH=<commit-ish>` (lines 294-302: the member must already exist at `--pin`; for a path outside `infra/aws/lambda/investor-reporting` the packaged name equals the repo path; the blob is read from `<commit-ish>:REPO_PATH`). `--member` is NOT usable here (it refuses an already-packaged name). Read lines 294-302 and the part of the driver that prints and records the bindings' provenance: an override may add a provenance key (for example `overrides`); the driver's bindings check allows exactly the keys of this change and nothing else (print what the provenance gained).

*What to do.*
1. Make the folder `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~317/r58/`. Copy the four files of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~315/r57/` (`r34m_build.py`, `make_scripts_r34m.py`, `check_r34m_record.py`, `check_r34m_xref.py`) into it, unchanged except for: (a) the `R57` path constant becomes your `r58/` folder (name it `R58`); (b) `BUILD_ARGS` gains `"--override", "docs/contracts/investor-reporting/v1/AnalysisSubmissionRequest.schema.json=7f1eab530cde4661e9a559bf45439ebdbf73dab2"`; (c) `EXPECT_CHANGED` gains `"docs/contracts/investor-reporting/v1/AnalysisSubmissionRequest.schema.json"` (six members, sorted compare as before); (d) the bindings check allows the one provenance key the override adds (and only it); (e) the record id and file read `RESIDENT_R34M_BUILD2` and the schema version `irpt-resident-r34m-build-v2`, and `check_r34m_record.py` expects `changed=6` and prints `R34M-RECORD-OK changed=6 added=0 removed=0`; (f) the tool-copies key lists the four files. Any other edit is a BLOCKING row naming it. Record the sha256 of each of the four copies.
2. The stage folder is `C:/dev/irpt-release-r35f` and must not exist before the build; never use or delete `r35a` to `r35e` (r35d is the OLD root, r35e the superseded build). Before the real run print the actual member difference the way the driver computes it, and STOP if it differs from the six members (the five of AR-y-430 plus the schema): a seventh mover, a missing mover or an added member is a BLOCKING surprise row naming it.
3. Run `python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~317/r58/r34m_build.py --pin 7f1eab530cde4661e9a559bf45439ebdbf73dab2 --out C:/dev/irpt-release-r35f --record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~317/r58/RESIDENT_R34M_BUILD2.json` from your worktree (several minutes: up to 600 s per command). It prints `R34M-BUILD-OK <members> ...` or `R34M-BUILD-BAD <why>`.
4. Write `check_schema_admits.py` in your deliverables folder `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~317/` (stdlib plus `jsonschema` and `referencing`, which the repository already uses; ruff clean; offline). It takes a tarball path and a composition json path, builds a jsonschema registry from the tarball's members `docs/contracts/investor-reporting/v1/*.schema.json` (direct children only), validates the composition against `RequestComposition.schema.json` and prints `SCHEMA-ADMITS errors=0` when valid, else `SCHEMA-REFUSES errors=<n> <validator>@<json path>` of the first error (closed words only, no value) and a non-zero exit. DIFFERENCE CONTROL (required): run it on the OLD root `C:/dev/irpt-release-r35d/irpt-resident-0485393f3a-r34l.tar.gz` with `C:/dev/irpt-inputs-r35f/composition_run5b.json` (it MUST print `SCHEMA-REFUSES errors=1 additionalProperties@browser`) and on your new tarball (`SCHEMA-ADMITS errors=0`); record both lines.
5. Print, from the record, the tarball sha256 and member count, the two-build identity line, the delta against r34l (changed, added, removed), the import smoke line, the gate dry-run return codes and the sha256 of each of the four host scripts. Commit your files and the record (the stage folder stays outside the repository). Then write the proof instance (shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~315/IRPT_ANLREQ.TO-AR-y-430.resident-release-r34m-build-only-three-o5-movers.proof_of_spec.json`, your own AR-y-430 instance; `to_id` exactly `IRPT_ANLREQ.TO-AR-y-438.resident-release-r34m-rebuild-with-the-submission-schema-six-movers`, a real `controls.mutant` such as the record copied with one member name changed, the checker must refuse, and `controls.determinism` build_a equals build_b), run `python .tools/proof-of-spec-check.py <instance> "AR438-y-AC1,AR438-y-AC2,AR438-y-AC3"` and flip `<status>` to `complete` (commit alone) only on VALID.

---

## ACCEPTANCE

<criterion id="AR438-y-AC1" cell_refs="AR-y-438"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~317/r58/check_r34m_record.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~317/r58/RESIDENT_R34M_BUILD2.json</invocation><expect>R34M-RECORD-OK changed=6 added=0 removed=0</expect></criterion>
<criterion id="AR438-y-AC2" cell_refs="AR-y-438"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~317/r58/check_r34m_record.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~317/r58/RESIDENT_R34M_BUILD2.json --identity</invocation><expect>R34M-IDENTITY-OK builds_identical=yes smoke_fail=0</expect></criterion>
<criterion id="AR438-y-AC3" cell_refs="AR-y-438"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~317/check_schema_admits.py C:/dev/irpt-release-r35f/irpt-resident-0485393f3a-r34m.tar.gz C:/dev/irpt-inputs-r35f/composition_run5b.json</invocation><expect>^SCHEMA-ADMITS errors=0$</expect></criterion>



<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~317/IRPT_ANLREQ.TO-AR-y-438.resident-release-r34m-rebuild-with-the-submission-schema-six-movers.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-438.resident-release-r34m-rebuild-with-the-submission-schema-six-movers`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR438-y-AC1,AR438-y-AC2,AR438-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-438</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~317/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-438.resident-release-r34m-rebuild-with-the-submission-schema-six-movers.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a build in a stage folder outside the repository and tool copies in the worker deliverables; nothing is uploaded, installed, applied or run on a host.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the builder (lines 294-302) and the measured cause against this cell; the lens: --member used where --override is needed (refused by the builder), a seventh mover, the bindings gaining a provenance key the check does not name, the schema check that cannot refuse (the difference control on the OLD root must print SCHEMA-REFUSES), the stage folder created inside the repository, r35d deleted. NOT seen (blind): the live host and the release key; denominator: three criteria.
</preflight>
