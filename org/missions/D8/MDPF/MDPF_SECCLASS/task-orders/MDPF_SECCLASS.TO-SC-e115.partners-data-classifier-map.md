# TO MDPF_SECCLASS.TO-SC-e115.partners-data-classifier-map -- round 29 SC-e-115: locate and read the partners-data classifier and its consumers (a read; the repoint is cut after it)

<to_id>MDPF_SECCLASS.TO-SC-e115</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~104</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-18</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>29</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-115` (`decompositions/MDPF_SECCLASS_DECOMP_R29.md`) |
**outcome_ref:** the partners-data repoint (CTO round-28 item 4) | **depends_on:** none | **source:** CTO round-28 analysis section 3 item 4; round-28 pre-read R27_CHECKS/ROUND28_PREREAD_PARTNERS_DATA_REPOINT_20261016.md

---

## WORKER FACE

### THE CELL

`SC-e-115`. The portal's `opal-partners-data` Lambda (us-east-1) classifies holdings with a module `etf_classifier` that reads the OLD classification table `bd-securities` (11,007 rows, four classes). The canonical table `etf-classifications` (11,375 rows) carries six classes (`equity`, `fixed_income`, `alternatives`, `structured`, `commodities`, `cash`). The CTO has ruled that this Lambda's classifier is repointed to the canonical table in round 29, under its own signed pair; that pair has to price, per client-facing reader, the 527 `structured`, 164 `commodities` and 381 `cash` key changes and the 1,555 dropped old-list-only keys. Before any build can be cut, someone must find the code and read how it treats the classes. You are that someone. You change nothing.

**What is already known (start from it):**
- The Lambda is live: `aws lambda get-function-configuration --function-name opal-partners-data --region us-east-1` returns a `CodeSha256` (it began `c9FXD84szSBD...` at the cut). The repo does NOT hold it under `infra/aws/lambda/` (that folder has `partner-etl-ops-sqs-consumer` and others, not this one); the portal repo (`portal/`, a separate nested repository) and `lambda/`-style folders elsewhere under the workspace are candidates. `comp-find --files <name>` locates a file by name; do not run a blind recursive grep.
- The round-27 pre-read (`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R27_CHECKS/ROUND28_PREREAD_PARTNERS_DATA_REPOINT_20261016.md`) holds counts you may cite but must not trust blindly, and says: the reader's output contract has three classes plus empty (`equity | fixed_income | alternatives | ''`, `hedge` mapped to `alternatives`); the consumer of `etf_classifier` in `lambda_function.py` (the holdings classify call near line 1054) was NOT read for how it treats the classes.
- The news layer-3 curation also reads the old list; it is a separate item and is NOT your cell.

**What you do:** (1) Locate the Lambda's source (repo path or a deployed artifact) and the file that defines `etf_classifier`. (2) Read the classify call sites in the Lambda and quote each (path, line, the line's text). (3) State, from the code, what the consumer does with each of the six canonical classes and with an empty result (for example: maps to a client-facing bucket, drops, breaks, passes through). (4) Write `PARTNERS_MAP.json` at the path in `<paths>`.

`PARTNERS_MAP.json` has exactly these keys (the script lists them in its header; read `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R29_CHECKS/check_r29_reads.py`, do not edit it):
- `lambda`: `{"name": "opal-partners-data", "region": "us-east-1", "code_sha256": <the live CodeSha256, which the checker re-reads>}`.
- `repo_paths`: a non-empty list of repo-relative paths (forward slashes) that exist at HEAD and hold the Lambda's source; if the source is only in a deployed artifact, say so in `class_handling` and list the repo paths that are closest (the checker requires at least one existing path).
- `classifier_path`: the repo-relative path of the file defining `etf_classifier`.
- `call_sites`: a non-empty list of `{"path", "line", "text"}`; the checker requires `text` to be a substring of that line of that file.
- `class_handling`: at least 60 characters: how the consumer treats each of the six classes and an empty result.
- `contract`: `{"returns": [<the class strings the module can return today>]}`.

### ACCEPTANCE

<criterion id="SC29-e115-AC1" cell_refs="SC-e-115"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R29_CHECKS/check_r29_reads.py partners</invocation><expect>R29-partners ok=True</expect></criterion>
`SC29-e115-AC1` -- the live Lambda hash matches, every named path exists, and every quoted call site is found on its line.

<expected_criteria>SC29-e115-AC1</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-18 ~02:0xZ): AC1 FAILS as expected (`R29-partners ok=False problems=['no file at ...PARTNERS_MAP.json']`). The script's `selftest` runs a green arm and negative arms for every mode and prints `R29-SELFTEST ok=True`; its live readers were checked against known numbers (the served 2026-10-02 delta +407,720.32; the live CodeSha256 of opal-partners-data).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **AWS READS ONLY** (S3 `list-object-versions`, `head-object`, `get-object`, `list-objects-v2`; CloudWatch Logs `filter-log-events`, `describe-log-groups`, `describe-log-streams`; Lambda `get-function`, `get-function-configuration`; SSM `get-command-invocation`, `list-command-invocations`; through `.tools/aws` or boto3). No write, delete, copy, put, tag, invoke, start, stop or deploy of any kind. Nothing is changed.
- **No package install and no download** into the repo. pandas, pyarrow and boto3 are installed.
- **Never edit** anything outside the `<paths>` block; the script under `R29_CHECKS/` is READ-ONLY to you. Never push.
- **Append to the surprise channel in BYTE MODE** (`open(path, 'ab')`), one new row only if you file one: never read and rewrite that file (it mixes CRLF and LF blocks and a round trip changes the old bytes).
- **Refusal clause.** If you cannot do what the cell asks, do not guess and do not edit a check. Write what you read (with each listing's positive control) in your report, file a surprise row (id `MDPF_SECCLASS-D1-W104-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) naming what you could not account for, and stop; leave AC1 failing.
- Run every invocation under `timeout 120`; bound each of your own reads by key or prefix, never sweep a whole bucket.

<paths>
org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~104/PARTNERS_MAP.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R29.md</decomp_doc> (round 29), cell `SC-e-115`.
<owned_cells>SC-e-115</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC29-e115-AC1. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~104/MDPF_SECCLASS.TO-SC-e115.partners-data-classifier-map.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC29-e115-AC1`.
</proof_of_spec>

**REPORT:** what you found and where (paths, version ids, times), the criterion's output verbatim, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE nothing is scheduled; nothing ships.
comp-iam: DECLARED-NOT-APPLICABLE only the reads the seat's role already makes.
comp-adversary: RUN -- a file that quotes text the check does not find in the source; a number typed rather than recomputed (the check recomputes it from S3, the repo or the live Lambda); a path that does not exist; a reason under its length floor.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-28 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_28_20261018.md`, msg 7829); DECOMP_R29.
