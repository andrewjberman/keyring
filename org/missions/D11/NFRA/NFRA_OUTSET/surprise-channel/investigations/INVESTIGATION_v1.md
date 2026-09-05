# NFRA_OUTSET -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Opened by:** `0.7.0_AE_CloudOps~W` at L7, executing `TO-OS-s-6` and `TO-OS-s-7` (both name this file in their
`<paths>` grant; this seat mints the file as its first writer).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`,
identity, folder == project, the allocator coordinate). Lane `ANY`.
**Id grammar:** a seat's row is `NFRA_OUTSET-S<k>`; a worker's row is `NFRA_OUTSET-W<n>-S<k>` (`<n>` = its slot); the
CVO's adjudication rows live in `../adjudications/` as `NFRA_OUTSET-C-S<k>`. **Append-only during the round.**
Never edit an existing row.
**Denominator at this write: 4 rows (S1-S4), all minted by `0.7.0_AE_CloudOps~W`.**

```json
[
  {
    "id": "NFRA_OUTSET-S1",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~W",
    "surfaced_at": "2026-09-04T21:05:00Z",
    "one_line": "TO-OS-s-6 criterion O6-AC1 CANNOT PASS AS CUT: its <invocation> runs `python .tools/comp-iam --help`, but .tools/comp-iam is a #!/bin/bash forwarder, so python parses it as Python and exits 1 with a SyntaxError and zero matches for the <expect> string 'usage'. The estate's own instrument, `comp-iam --help`, exits 0 and prints 'usage' -- the criterion's INTENT is satisfiable, only its literal invocation is not.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/comp-iam@14f26b5eff line 1 is `#!/bin/bash`; `file .tools/comp-iam` -> 'Bourne-Again shell script, ASCII text executable'; line 4 is `WORKSPACE=\"$(cd \"$(dirname \"$0\")/..\" && pwd)\"` and line 5 forwards to `python \"$WORKSPACE/org/modules/graph/iam_cli.py\" \"$@\"`",
        "MEASURED: `timeout 120 python .tools/comp-iam --help` -> rc=1, stderr 'File \".tools\\\\comp-iam\", line 4 ... SyntaxError: invalid syntax', grep -c usage = 0 (denominator: 1 invocation, 1 expect clause)",
        "MEASURED NEGATIVE-TO-POSITIVE CONTROL: `timeout 120 comp-iam --help` -> rc=0, grep -c usage = 1, printing the full subcommand list including refresh-census and simulate",
        "org/missions/D11/NFRA/NFRA_OUTSET/task-orders/NFRA_OUTSET.TO-OS-s-6.federated-transport-caller-contract-iam.md@14f26b5eff -- the criterion element: <criterion id=\"O6-AC1\" cell_refs=\"OS-s-6\"><invocation>python .tools/comp-iam --help</invocation><expect>usage</expect></criterion>"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO",
    "spec_asserts": "TO-OS-s-6 O6-AC1: the invocation `python .tools/comp-iam --help` produces output matching `usage`, and the criterion's pass 'is decided by the MATCH and never by your opinion'.",
    "world_is": ".tools/comp-iam is a bash script. `python .tools/comp-iam --help` exits 1 on a SyntaxError and emits no 'usage'. No amount of correct execution by the assignee can make the cut invocation match its own expect clause.",
    "notes": "CUT DEFECT, and routed as one rather than worked around, per the issuer's GO ('If something in a face is wrong or missing, that is a CUT DEFECT and it is mine -- file the row and tell me; do not work around it'). CONSEQUENCE: TO-OS-s-6 is NOT flipped to complete by this seat -- the <proof_of_spec> guard admits a complete flip 'only when every MECHANICAL criterion PASSES', and O6-AC1 is the order's only mechanical criterion. O6-AC2 and O6-AC3 were executed in full and are recorded in the result document; only the flip is withheld. PROPOSED REPAIR (issuer's call, not applied here): amend the <invocation> to `comp-iam --help`, which is the instrument the estate runs and which satisfies the expect clause as written. ARMED because the order cannot terminate until the cut is amended. Disarm = the issuer's amendment, after which this seat re-runs O6-AC1 and flips."
  },
  {
    "id": "NFRA_OUTSET-S2",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~W",
    "surfaced_at": "2026-09-04T21:12:00Z",
    "one_line": "comp-find CONTENT mode returns rc=124 (timeout) with ZERO bytes on stdout and ZERO bytes on stderr -- so a timed-out search is indistinguishable from a clean zero-hit search, and it suppresses the printed denominator that CLAUDE.md Rule 21 relies on to make a zero readable. Reproduced on a positive control whose hits are certain.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED: `timeout 120 comp-find \"trino\" > out 2> err` -> rc=124, `wc -c out` = 0, `wc -c err` = 0. Ran from the workspace root at HEAD 14f26b5eff.",
        "MEASURED POSITIVE CONTROL (a token certain to exist in-corpus): `timeout 120 comp-find \"NFRA_OUTSET\" --limit 5` -> rc=124, empty. The control fails identically, so the empty result is the tool's, not the corpus's.",
        "CROSS-INSTRUMENT DISPROOF OF ABSENCE: native Grep for the same pattern 'trino' (case-insensitive) returns 40+ matching files including .tools/comp-heat, .tools/_trino_fed.py, infra/aws/globgrph/Dockerfile and org/modules/graph/graph-call-manifest.yaml -- i.e. the true hit count is large, not zero",
        "CONTRAST, same session, same box: `comp-find --hidden iam_live_census` DID return promptly with a proper header and an explicit 'A count over a path that is not there is not a zero -- it is NO MEASUREMENT' error, and `comp-read` calls returned normally throughout -- so the fault is specific to comp-find CONTENT mode, not to the comp-tool rail or the shim layer"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO",
    "spec_asserts": "CLAUDE.md Rule 21: comp-find is the rail for repo content search, and a comp-find result carries a PRINTED DENOMINATOR so that a zero can be told from an absence ('0 hit(s) across 0 file(s) IS OUT-OF-CORPUS, NOT ABSENCE').",
    "world_is": "On this box at this vintage, comp-find content mode does not return within 120s and emits nothing at all -- no header, no denominator, no error. The caller sees an empty result set with no signal that no measurement occurred. Every downstream 'no hits' conclusion drawn from comp-find content mode in this window is unsound.",
    "notes": "OFF-TASK for OS-s-6/OS-s-7 -- surfaced under CLAUDE.md s.2 (append a row, keep working) and not investigated further. Root cause NOT chased. This seat's own searches were completed with native Grep, which CLAUDE.md Rule 21 explicitly carves out of the rail ('NOT gated: ... native Grep/Glob, Read'), so no finding in either result document rests on a comp-find content result. ARMED because the failure mode is silent and its output is the shape of a true negative: a seat that runs one comp-find content query and reads the empty result as 'not present' will be wrong and will have no way to notice. Routing to the issuer for the comp-rail owner (NFRA_COMPRAIL surface) because the tool is outside this order's <paths> grant."
  },
  {
    "id": "NFRA_OUTSET-S3",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~W",
    "surfaced_at": "2026-09-04T21:30:00Z",
    "one_line": "A THIRD simulate-principal-policy false-deny mode, measured: a resource ARN at the WRONG GRAIN for the action returns implicitDeny even for a principal holding AdministratorAccess (*/*). logs:GetLogEvents against a log-STREAM-grain ARN -> implicitDeny; the same action, same principal, against the log-GROUP-grain ARN -> allowed. This is distinct from the two known modes (conditioned-grant false deny; multi-ARN batch poisoning).",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED FALSE DENY: `aws iam simulate-principal-policy --policy-source-arn arn:aws:iam::313476888478:user/Andrew_Berman --action-names logs:GetLogEvents --resource-arns 'arn:aws:logs:us-east-1:313476888478:log-group:/ecs/globgrph/trino:log-stream:*'` -> EvalDecision = implicitDeny (single resource ARN; the batch-poisoning mode is NOT in play)",
        "MEASURED TRUE ALLOW, three log-GROUP-grain forms, same principal and action: '...:log-group:/ecs/globgrph/trino' -> allowed; '...:log-group:/ecs/globgrph/trino:*' -> allowed; '*' -> allowed",
        "WHY THE DENY IS IMPOSSIBLE ON THE WORLD: user/Andrew_Berman has no inline policy and four narrow attached policies, and is a member of group AdministratorAccessOpalCapital whose sole attached policy is arn:aws:iam::aws:policy/AdministratorAccess (Action:*, Resource:*), measured via list-user-policies (empty), list-attached-user-policies, list-groups-for-user and list-attached-group-policies. A principal with */* cannot be implicitDenied.",
        "INSTRUMENT CONTROLS, both fire correctly, so the simulator is not globally broken: NEGATIVE role/advi-49f-floor-scheduler-role ecs:RunTask @ task-definition/globgrph-trino:6 -> implicitDeny; POSITIVE the same role lambda:InvokeFunction @ arn:aws:lambda:us-east-1:313476888478:function:advi-49f-gold-dispatch -> allowed"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO",
    "spec_asserts": "The estate's recorded simulate-principal-policy hazards are two: (1) implicitDeny on a CONDITIONED grant is a false deny; (2) a batched multi-ARN call poisons verdicts across resources. Respecting both -- one --resource-arns per call, and no conditioned grant in the evaluated set -- is treated as sufficient to trust an EvalDecision.",
    "world_is": "A third, independent mode exists: resource-ARN GRAIN. Supplying a log-stream-grain ARN for a log-group-grain action yields implicitDeny with no error, no warning and no indication that the resource failed to match the action's resource type. Both known mitigations were in force and neither prevents it.",
    "notes": "OFF-TASK as a general instrument finding, though it arose inside O6-AC3's own trap clause and is recorded there too. WHY IT MATTERS MORE THAN IT LOOKS: I caught this only because the principal holds */*, which makes a deny self-evidently false. Against a narrowly-scoped principal -- the normal case for an IAM audit -- this mode is INVISIBLE and reads as a correct negative, so it produces confident, wrong 'X does not hold this permission' conclusions. It fails in the UNDER-GRANTED direction, which is the direction least likely to be challenged. MITIGATION for any seat running simulate: pass the resource ARN at the grain the ACTION is authorized on (log-group for logs:GetLogEvents, task-definition for ecs:RunTask), and run a */* positive control alongside any deny you intend to act on. Routing to the issuer for the estate trap catalogue (docs/doctrine/CONTROLS_OVER_CARE.md and the comp-iam simulate wrapper's own rules) because both are outside this order's <paths> grant; this seat has recorded it in its own recall surface and in the OS-s-6 result document."
  },
  {
    "id": "NFRA_OUTSET-S4",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~W",
    "surfaced_at": "2026-09-04T22:05:00Z",
    "one_line": "SYSTEMIC CUT DEFECT across the issuance: 16 of this project's 17 task-order faces name their proof_of_spec instance by the SHORT stem (NFRA_OUTSET.TO-OS-s-N.proof_of_spec.json), but .tools/to-pipeline-gate.py globs the FULL face stem including the slug (NFRA_OUTSET.TO-OS-s-N.<slug>.proof_of_spec.json). An assignee who follows its own face literally writes a file the gate cannot see, and the complete flip is REFUSED. Measured by the gate actually refusing this seat's flip, not predicted.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED REFUSAL (the gate fired on a real commit, this is not a code read): `.tools/safe-commit.sh` -> 'ERROR: BLOCKED -- pipeline layer 2 (TO issuance gate). Commit aborted; files unstaged. [to-pipeline-gate] REFUSED -- 1 violation(s): NFRA_OUTSET.TO-OS-s-7.code-heat-parquet-cadence-and-owner.md: flips to complete on PIPELINE-REGISTERED project NFRA_OUTSET, and NO proof-of-spec instance was found beside it. Layer 1: no VALID instance, no complete flip.' The instance existed and was VALID at that moment -- only its NAME differed.",
        ".tools/to-pipeline-gate.py@14f26b5eff check_complete_flip :1261-1270 -- `stem = os.path.basename(rel).rsplit('.md',1)[0]` (the FULL face stem, slug included), `names = (stem + '.proof_of_spec.json', stem + '_PROOF_OF_SPEC.json')`, then for a TREE project `glob(<project>/deliverables/*/<name>)`. No short-stem form is searched.",
        "CENSUS OF THE ISSUANCE, denominator 17 of 17 faces under org/missions/D11/NFRA/NFRA_OUTSET/task-orders/ read at HEAD 14f26b5eff: 1 face names the gate-compatible FULL stem (TO-OS-s-1: 'NFRA_OUTSET.TO-OS-s-1.rule-t-budget-across-comp-heat.proof_of_spec.json'); the other 16 (OS-s-2 through OS-s-17) name the SHORT stem. So 16/17 are defective and OS-s-1 is the accidental control proving the correct form was available at cut time.",
        "ESTATE PRECEDENT for the full-stem form: org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~P/NFRA_CLDGRPH.TO-CG-V-2.reachability-iam-authkind-verified.proof_of_spec.json -- a landed, gate-passed instance carrying the full stem including its slug"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO",
    "spec_asserts": "Each face's <proof_of_spec> block: 'The ASSIGNEE fills a PROOF_OF_SPEC.schema.json instance at org/missions/D11/NFRA/NFRA_OUTSET/deliverables/<serial>/NFRA_OUTSET.TO-OS-s-N.proof_of_spec.json and validates it ... BEFORE the complete flip, which the assignee commits itself.'",
    "world_is": ".tools/to-pipeline-gate.py searches only for the FULL-face-stem filename. An instance written at the face's stated path is invisible to the gate, which then reports 'NO proof-of-spec instance was found beside it' -- a message that reads as 'the assignee did not write one' when the assignee wrote exactly what its face specified. The flip is refused and the commit aborted with files unstaged.",
    "notes": "RESOLVED FOR THIS SEAT'S TWO ORDERS BY OBEYING THE MECHANISM, NOT THE PROSE: both instances were written under the FULL face stem, which is inside the same granted deliverables folder, so no path outside the <paths> grant was touched. The face's stated path is recorded as wrong in both result documents and in TO-OS-s-7's status line so no reader is misled. NOT a repair of the other 15 faces -- editing them is the issuer's act, not this lane's, and this row is the route. IMPACT IF UNFIXED: every remaining NFRA_OUTSET order hits this at its own completion, one at a time, each costing a refused commit and a re-diagnosis; the gate's message points at the assignee rather than at the cut, so each seat is likely to look for its own mistake first. CHEAPEST FIX: amend the 16 faces' <proof_of_spec> paths to the full stem (OS-s-1 already shows the correct form). The gate is NOT the thing to change -- it matches the landed estate convention."
  }
]
```
