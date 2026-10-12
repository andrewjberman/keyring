# TO IRPT_BCKEND.TO-IB-pr-462 -- READ ONLY: four deploy ledger entries left OPEN on site Z, each open leg MEASURED against its artifact; nothing re-executed

<to_id>IRPT_BCKEND.TO-IB-pr-462</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~317</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>158</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6192 (on `0.0.0_AB_MSTR~DELL2` msg 6190, a relay from site Z) | **Decomp cell:** `IB-pr-462` (decomposition section 150) | **outcome_ref:** FWD-1

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-317/` (bash `/c/dev/wk-irpt-bckend-317`). Work only there.

**THE LAW THIS CELL APPLIES (CLAUDE.md, NEVER-2):** an entry a device left OPEN proves only that THAT device saw no
completion. Before acting on any open entry, MEASURE THE ARTIFACT, with a positive control. World-done closes it SUPERSEDED,
never re-execute.

**HARD BOUNDS.** READ ONLY. NOTHING is re-executed, re-applied, rolled back, planned-and-applied, invoked or signed in under
these entries: they are 16 to 18 days old and the functions have been released several times since. No terraform apply, no
`safe-apply`, no Lambda invoke, no SSM command, no sign-in as a person or a service, no S3 write, no edit of any sentinel or
ledger file. AWS reads allowed, through `.tools/aws`: `lambda get-function-configuration` (query the fields you need by
`--query`; NEVER print or record an environment variable's VALUE: record only whether a key is present and, where a leg needs
it, a derived fact such as "the plan's expiry is in the past"), `iam get-role-policy`, `iam simulate-principal-policy`,
`apigateway`/`apigatewayv2` `get-*` of one named resource, `scheduler get-schedule`, `s3api head-object`, and a DynamoDB
`get-item` / `query` for ONE named key where a leg names a claim row (record presence or absence, never the item). Record no
account id, no plan value, no secret, no firm's client data.

**The four entries** are tracked on site Z's branch, not on this box. Run `git fetch origin box/sitez` then read each with
`MSYS_NO_PATHCONV=1 git show origin/box/sitez:org/critical_paths/.open_deploys/<slug>.json` (record `read_from_commit` =
`git rev-parse origin/box/sitez`; never `2>/dev/null` a `git show`; a positive control: the same command on a path you know
exists). Read each entry's `entry_path` ledger file the same way. Also say whether any of the four sentinels exists on this
box's branch (`present_on_this_box`).

| slug | author | legs | the ONE open leg |
|---|---|---|---|
| `irpt-p-live-scope-20260923` | 2.0.0_SA_COO~P | 6 | `HTTP` (verify): "legitimate authorized HTTP and Andrew smoke" of the CloudFront authenticated scope browse on portal-v2.1.185; status HELD-SOVEREIGN-GATED |
| `irpt-performance-49f-engine-20260924` | 2.0.0_SA_COO~P | 2 | `S1` (verify): a signed-in 49F one-account YTD request answers a retained OPAL_ENGINE report; then the per-account cross-check |
| `irpt-performance-inf-one-use-20260925` | 2.0.0_SA_COO~P | 5 | `S1` (verify): "the one Orion use claimed by a signed-in request and its report retained, OR the plan expires unspent" |
| `irpt-holdings-principals-dispatch-m-20260925` | 2.0.0_SA_COO~M | 4 | `N1` (verify): the negative arm EXERCISED AS THE PRINCIPALS (one firm's principal refused on another firm's bucket, both directions); status HELD, gated on a host window |

Confirm that table from the sentinels themselves (`legs_total`, `legs_open`, `author`, `status_in_sentinel`); if a sentinel
disagrees with it, the sentinel wins and you say so in a row.

**For each open leg** (`entries.<slug>.measured.<leg>`): `was_to_produce` (the leg's own `proof_required`, in words);
`measures` (a list; each `what`, `command_class` such as get-function-configuration or simulate-principal-policy or git, and
`reading`: a digest, a state, a decision, a count, present/absent); `positive_control` (`what`, `reading`: the same instrument
on something known to exist or to be allowed, so an empty or denied reading is not mistaken for an absence); then ONE verdict:
- `SUPERSEDED_WORLD_DONE`: the thing the leg was to prove is shown by a measure (cite it in `measure_cited`). Example: the
  third entry's leg is satisfied by its OWN second branch if the plan expired unspent: the plan's expiry is in the past
  (read from the sentinel's closed leg A3, which states it) AND no claim row for it exists (one keyed read, presence only)
  AND the function's environment today (key presence only) no longer carries that plan or carries a later one.
- `SUPERSEDED_OVERTAKEN`: the artifact the leg was to verify no longer exists as the served thing, so the verification can no
  longer be made of it: e.g. the function's live CodeSha256 today differs from the digest the entry deployed, and the map or a
  later closed ledger entry records the releases that replaced it (cite them: `git log` on the map's entry, or the later
  entries under `org/critical_paths/change_management/`); for the portal leg, the PROD tag served today is later than
  `portal-v2.1.185` (read the tag from the portal repository's refs at `C:/dev/ajb_workspace/portal`, read only, `git -C ...
  tag --points-at` / `describe`; record the commit and tag, and say it is another checkout). Overtaken is NOT the same as
  done: say plainly that the original verification was never recorded and can no longer be made of that build.
- `NOT_DONE`: the leg's proof was never made and the thing it guards is still as it was: `half_landed` (what is applied and
  what is unproven) and `since`. For the fourth entry: the grants and the function landed (legs closed); the negative arm was
  never EXERCISED as the principals. Measure what CAN be read now: do the three firm roles and their policies still exist as
  the entry planned (`iam get-role-policy`, presence and the statement ids only), and `iam simulate-principal-policy` for
  each firm role against another firm's bucket (both directions the leg names) with a positive control on its own bucket.
  A SIMULATION IS NOT AN EXERCISE: if the simulation reads denied, that is a measure of the policy, and the leg stays
  `NOT_DONE` unless a record on the trunk shows the arm was exercised live since (search
  `org/critical_paths/change_management/` and the IRPT projects' channels for the role names and "N1"; cite what you find).
  If the buckets or roles the entry names have since been replaced (another project moved firm buckets), say so with the
  evidence: then the leg is `SUPERSEDED_OVERTAKEN` for the old shape and the NEW shape's negative arm is a row.
Each verdict carries a `claim` (`measured`, `inferred`, `held`, `absent`) and a `reason`.

Also record `how_the_close_is_to_be_written`: the sentinels are not on this box, so no close is written here; say which
command closes an entry as superseded (read `.tools/` for the deploy ledger tool and its `close` / `supersede` verbs; cite the
file and the verb) and that it is run where the sentinel is tracked, by the seat the issuer names, on this record.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~317/`: `IB158-1_open_ledger_legs_measured.json`
with `{read_from_ref: "origin/box/sitez", read_from_commit, present_on_this_box, open_legs_measured: 4, entries:{<slug>:{author,
status_in_sentinel, legs_total, legs_open:[...], measured:{<leg>:{...}}}}, how_the_close_is_to_be_written, not_established:[...],
re_executed:0, re_applied:0, rolled_back:0, functions_invoked:0, sign_ins_made:0, sentinels_edited:0, aws_writes_made:0}`; and a
one-page `IB158-1_OPEN_LEDGER_LEGS_MEASURED.md`: one paragraph per entry, the verdict first.

<criterion id="IB158-1-AC1" cell_refs="IB-pr-462"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r158/p158_cells.py" . IB158-1-AC1</invocation><expect>IB158-1-AC1 PASS</expect></criterion>
<criterion id="IB158-1-AC2" cell_refs="IB-pr-462"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r158/p158_cells.py" . IB158-1-AC2</invocation><expect>IB158-1-AC2 PASS</expect></criterion>
<criterion id="IB158-1-AC3" cell_refs="IB-pr-462"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r158/p158_cells.py" . IB158-1-AC3</invocation><expect>IB158-1-AC3 PASS</expect></criterion>

<expected_criteria>IB158-1-AC1, IB158-1-AC2, IB158-1-AC3</expected_criteria>

The checks grade the denominators, the shape of each measure with its control, the closed set of verdicts and the seven zeros.
Which verdict each leg takes is UNMEASURED by the issuer; `NOT_DONE` is a full answer.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else.
- **Refusal clause:** an AWS read refused (record it as a measure with the refusal, never retry another way), a sentinel that
  cannot be read, or a criterion that cannot be met as written: file a row and report. Never weaken a check; do not edit
  `p158_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W317-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~317" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~317@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~317 <0.9.0_WK_IRPT_BCKEND~317@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~317/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-462.four-open-ledger-entries-measured.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 150 (round 158, workstream ~P), cell `IB-pr-462`.
<owned_cells>IB-pr-462</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB158-1-AC1, IB158-1-AC2, IB158-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~317/IRPT_BCKEND.TO-IB-pr-462.four-open-ledger-entries-measured.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the commit the sentinels were read at and whether any is on this box; per entry, the open
leg, each measure with its reading, the positive control, the verdict with its claim and reason, and for NOT_DONE what is
half-landed and since when; how a close is written and where; what is not established; each criterion's last line; the proof
checker's result; commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read written to the worker's own deliverables folder; nothing is re-executed, applied, rolled back, invoked or edited; no sentinel is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; get-role-policy and simulate-principal-policy are reads.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; route bindings are read where a leg names them.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; one may be read.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p158_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~00:2xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. The issuer fetched origin/box/sitez (@d68d9a5eda) and printed all four sentinels (with a size control on the first): each has exactly one open leg, all four of kind verify; the leg counts and names in the face's table are from that print. None of the four is on this box (0 of 4 by name in org/critical_paths/.open_deploys/). The face separates OVERTAKEN from DONE and forbids reading a simulation as an exercise (rule 22: ABSENT is not EXERCISED-AGAINST).
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only).
</preflight>
