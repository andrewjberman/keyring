# TO IRPT_BCKEND.TO-IB-pr-447 -- READ ONLY: does the RUNNING irpt-intake-poller read firm_registry.json, and where would those firms come from under the naming canon's registry

<to_id>IRPT_BCKEND.TO-IB-pr-447</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~305</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>144</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 5611 (cell IB-s-6 is IRPT_BCKEND's) | **Decomp cell:** `IB-pr-447` (decomposition section 136) | **outcome_ref:** FWD-9

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-305/` (bash `/c/dev/wk-irpt-bckend-305`). Work only there.

**Why.** Row `IRPT_ANLREQ-D2-W53-S3` (read it in
`org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md`, and its record
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/r11/INTAKE_POLLER_MAP_ENTRY.json`) measured that 21 of the
28 live members of the function `irpt-intake-poller` have no blob in git: the function serves from bytes the tree cannot
reproduce. The remedy is a release of the poller from the tree. Before that release is designed, one question: **a release
from the tree that drops a file the running code opens is an outage.** `firm_registry.json` is declared in the function's
source-map entry (`infra/aws/lambda/ci/lambda-source-map.json`, key `irpt-intake-poller`, read its `files`, `staged_from` and
both notes) and its served content exists nowhere in git.

**HARD BOUNDS.** READ ONLY. The AWS calls allowed are exactly: `lambda get-function` and `lambda get-function-configuration`
on `irpt-intake-poller` (through `.tools/aws`), and one download of the package from the URL `get-function` returns. NO
invoke, NO update, NO S3 write, NO terraform, no other function. Put the downloaded zip and its extraction in a NEW EMPTY
folder OUTSIDE the worktree; it is data: never run, import or execute anything from it (read it with the `zipfile` module
from a script kept in a different folder, `python -I`). Do not copy the content of `firm_registry.json` into any committed
file: name its FIELDS and count its entries; write no firm's name, no account id, no address.

**Read and state:**
1. **The live package** (`live_package`): the function's `CodeSha256` and the read time; the base64 sha256 of the downloaded
   bytes and that it EQUALS `CodeSha256` (if it does not, stop and file a row); the member count; whether a member named
   `firm_registry.json` is in it (`file_in_package`); from the configuration, whether an environment variable points at it
   (`env_var_points_at_it`; name the variable, not secrets).
2. **Every read of the firm registry in LIVE members** (`registry_reads_in_live_members`): search every `.py` member of the
   live package for the file's name, for `IRPT_FIRM_REGISTRY`, and for every function that loads it (follow the loader: in
   the tree it is `load_firm_ids` and its siblings in the `_keys` module, packaged flat as `keys.py`); each hit with the
   member, the line number IN THE LIVE MEMBER, and what is read (`what_is_read`). State `searched_for`.
3. **Is it reached at run time** (`reached_at_run_time`): from the handler's entry point in the live package, is any of those
   reads on a path a scheduled poll or a request reaches (import time counts: say which)? `true`, `false` or `null`, with its
   claim (`measured` only for what the live bytes show by reading the call path; nothing is exercised) and the path in words.
4. **The fields taken** (`fields_taken_from_the_file`): each field or key the code takes from the file.
5. **Under the canon** (`under_the_canon.per_field`, one entry per field of step 4, same order): does the naming canon's
   registry hold it? Read `infra/logic/registry/` (list its files), `lib/opal_naming.py` (the loader functions and what they
   return), and `infra/logic/02_DOCTRINE.md` R1-R21 where it names firms or tenants. `canon_holds_it` true with `read_by` as
   `file:function`, or false. Also say in one sentence how the tree's OTHER investor-reporting functions get their firm list
   today (the `_keys` loader and what file it opens), since the poller's release would follow them.
6. **A release from the tree that drops the file** (`a_release_that_drops_the_file`): `OUTAGE`, `NO_EFFECT` or
   `CANNOT_BE_TOLD`, with its claim and the reason, read from steps 2-3 (what the code does when the file is absent: raises,
   falls back, or refuses; cite the live member's line).
7. `not_established`: everything you could not settle.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~305/`: `IB144-1_poller_firm_registry_read.json`
with `{live_package:{code_sha256, read_at_utc, downloaded_bytes_hash_equals_code_sha256, members, file_in_package,
registry_entry_count}, env_var_points_at_it, env_var_name, searched_for:[...], registry_reads_in_live_members:[{member, line,
what_is_read}], reached_at_run_time:{answer, claim, path_in_words}, fields_taken_from_the_file:[...],
under_the_canon:{registry_files:[...], per_field:[{field, canon_holds_it, read_by}], how_the_other_functions_get_firms},
a_release_that_drops_the_file:{effect, claim, reason}, not_established:[...], aws_writes_made:0, functions_invoked:0}`; and a
one-page `IB144-1_POLLER_FIRM_REGISTRY_READ.md` in plain sentences, each with its claim. No design of the release.

<criterion id="IB144-1-AC1" cell_refs="IB-pr-447"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r144/p144_cells.py" . IB144-1-AC1</invocation><expect>IB144-1-AC1 PASS</expect></criterion>
<criterion id="IB144-1-AC2" cell_refs="IB-pr-447"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r144/p144_cells.py" . IB144-1-AC2</invocation><expect>IB144-1-AC2 PASS</expect></criterion>
<criterion id="IB144-1-AC3" cell_refs="IB-pr-447"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r144/p144_cells.py" . IB144-1-AC3</invocation><expect>IB144-1-AC3 PASS</expect></criterion>

<expected_criteria>IB144-1-AC1, IB144-1-AC2, IB144-1-AC3</expected_criteria>

The checks grade the shape and the bounds. The answers are UNMEASURED by the issuer; "it cannot be told" passes where true.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file is edited.
- **Refusal clause:** if a criterion cannot be met as written, or an AWS read is refused, stop, file a row and report. Never
  weaken a check; do not edit `p144_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W305-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~305" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~305@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~305 <0.9.0_WK_IRPT_BCKEND~305@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~305/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-447.intake-poller-reads-firm-registry.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 136 (round 144, workstream ~P), cell `IB-pr-447`.
<owned_cells>IB-pr-447</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB144-1-AC1, IB144-1-AC2, IB144-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~305/IRPT_BCKEND.TO-IB-pr-447.intake-poller-reads-firm-registry.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the live digest and that the downloaded bytes equal it; whether the file is in the package
and the variable that points at it; each read of it in live members; whether it is reached at run time, with the claim; the
fields taken; which the canon holds and by what call; what a release that drops the file would do; what is not established;
each criterion's last line; the proof checker's result; commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read written to the worker's own deliverables folder; two describe-class reads of one function and one package download; nothing is changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; a refused read is a row.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p144_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~19:1xZ: IB144-1-AC1..3 FAIL (no file); commit-gate clean. The issuer read the source-map entry (the note states the registry file's served content has no git blob, row IRPT_BCKEND-W4-S34). The face forbids copying the registry's content and designing the release.
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only).
</preflight>
