# NFRA_DEVPLN -- surprise channel, INVESTIGATION v1 (laptop fabric)

**Opened by:** `2.0.0_SA_COO~DV`. **Home:** the project tree's channel; the gate `.tools/surprise-row-gate.py` validates every NEW row (schema
`org/surprise_channel/schemas/investigation_item.schema.json`). Lane `ANY`. The issuer's row is `NFRA_DEVPLN-S<k>`; a worker's is `NFRA_DEVPLN-W<n>-S<k>`.
**Append-only during the round.** Never edit an existing row.

## NFRA_DEVPLN-S1 -- C-PROMOTE's ancestry check, read literally, refuses every honest release; the issuer read it first-parent and bound the approval to the branch head

```json
{
  "id": "NFRA_DEVPLN-S1",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~DV",
  "surfaced_at": "2026-10-13T18:45Z",
  "one_line": "PRD v0.2 C-PROMOTE refuses a release when any commit in PROD..release lacks an Approved-By trailer, but a feature branch's own commits carry no trailer (only the merge commit does), so the literal walk fails every release; round 1 cell DP-b-3 reads the walk first-parent and DP-b-5 refuses a DEV-cut branch at registration.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_DEVPLN/prd/NFRA_DEVPLN_PRD.md C-PROMOTE (v0.2 @d2b7385bee): 'the script walks PROD..release and prints the count of unapproved commits beside the total; 0 or it does not ship'",
      "C-MERGE-FORWARD in the same PRD: the trailers go on the MERGE commit (`Feature:` and `Approved-By:`); a feature branch's own commits are written by its builder before any approval exists, so they cannot carry the trailer",
      "decomposition rulings R1 (first-parent walk), R2 (approval binds head_sha and commits), R4 (a FAST lease writes a row through approval-lease) in org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round1.md",
      "CVO review @2b616031b1 point 1, the hole the check closes: a feature branch cut from DEV carries every DEV commit beneath its own; the registration check (DP-b-5: refuse a branch with a commit on DEV and not on PROD) and the per-feature commit-count binding close it where a first-parent walk alone cannot see it"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD v0.2 C-PROMOTE: a release is refused when any PROD..release commit lacks Approved-By; C-MERGE-FORWARD (iii): the merge-forward script reads a live FAST lease as the approval.",
  "world_is": "Not yet exercised: both readings are built in round 1 and tested on fixture repositories, then run once on a real feature at the close. The issuer reads the first clause first-parent plus a per-feature binding (head_sha, commit count, no DEV overlap at registration) and the second clause as a lease-written approval row, so the script reads one record instead of two. The CTO may rule either differently at the round-1 analysis; the PRD text is untouched."
}
```

## NFRA_DEVPLN-W4-S1 -- open-calls.py add has no approval-registration options; TO step 4 cannot run as written

```json
{
  "id": "NFRA_DEVPLN-W4-S1",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~4",
  "surfaced_at": "2026-10-13T18:50:39Z",
  "one_line": "TO DP-b-4 step 4 names `python .tools/open-calls.py add --kind approval --box --branch --purpose --pages --class --how --portal`; the tool at HEAD accepts only --project --subject --asked-by --source --context --kind {fork,act} (plus --orders --roots --device --rec). The page carries the command as the TO states it; registration is not run.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python .tools/open-calls.py add --help at .tools/open-calls.py@2cab0f0536: usage lists --project --subject --asked-by --source --context --kind {fork,act} and no --box, --branch, --purpose, --pages, --class, --how or --portal",
      "org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-b-4.contributing-boxes.md step 4 (the command as stated)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO DP-b-4 step 4: register the feature with `open-calls.py add --kind approval ... --box <box> --branch cand/<box>/<slug> --purpose --pages --class --how --portal portal`, which reads the head and commit count and refuses a branch carrying DEV commits.",
  "world_is": "open-calls.py at @2cab0f0536 has no approval kind and none of the feature options; its add verb records a fork or act call. The registration path for a portal feature does not exist in the tool. Nothing was registered; no branch was pushed to DEV; the page names the command as the TO states it."
}
```

## NFRA_DEVPLN-W4-S2 -- the portal merge-forward and release-build tools named by the TO are absent from the tree

```json
{
  "id": "NFRA_DEVPLN-W4-S2",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~4",
  "surfaced_at": "2026-10-13T18:50:39Z",
  "one_line": "TO DP-b-4 steps 6-7 name `bash .tools/portal-merge-forward.sh` and `bash .tools/portal-release-build.sh --features`; neither file exists in the worktree at HEAD (the .tools/portal-hooks/ directory holds only hooks). The page names both commands as the TO states them.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "ls -la .tools/portal-merge-forward.sh .tools/portal-release-build.sh at worktree HEAD @2cab0f0536: both 'No such file or directory'",
      "git ls-files .tools | grep -i portal at @2cab0f0536 lists only .tools/portal-hooks/* (VALGATE_D1.md, commit-msg, d1_adapter_threading_gate.py, d1_gate_test.py, install.sh, pre-push)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO DP-b-4 steps 6 and 7: a closed-approved feature reaches DEV only through `bash .tools/portal-merge-forward.sh cand/<box>/<slug>`; PROD takes features only through `bash .tools/portal-release-build.sh --features <list>`.",
  "world_is": "Neither script is in the tree at @2cab0f0536. Until they land, no feature can reach DEV by the named route and no PROD promote takes a feature list. No feature has been merged or promoted by this cell."
}
```

## NFRA_DEVPLN-W5-S1 -- git cherry omits merge commits, so the settlement list cannot give a +/- sign to a merge (DP-s-1)

```json
{
  "id": "NFRA_DEVPLN-W5-S1",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~5",
  "surfaced_at": "2026-10-13T18:55:35Z",
  "one_line": "DP-s-1 asks git cherry to say whether each PROD-only commit and each branch commit has its patch on DEV; git cherry omits merge commits, so 7 of the 33 PROD-only commits and 9 branch-ahead commits (7 on wk-dsgn-irptv1-r25-61-prodcut, 2 on sitez/merge-trial-20260915) carry no +/- sign and are shown as n/a or in a merge column.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-s-1.settlement-list.md BUILD step 2 and step 3: 'git cherry origin/DEV origin/PROD' and 'git cherry origin/DEV origin/<b>' used as the same-patch test for every commit",
      "measured: git cherry origin/DEV origin/PROD returns 26 signed lines for the 33 commits of git rev-list origin/DEV..origin/PROD; the 7 unsigned commits are merges (ledger rows 27-33 of org/missions/D0/NFRA/NFRA_DEVPLN/ledger/SETTLEMENT_LIST.md, marked 'n/a (merge commit; git cherry omits merges)')",
      "measured: branch wk-dsgn-irptv1-r25-61-prodcut has ahead 34 = cherry+ 2 + cherry- 25 + merges 7; branch sitez/merge-trial-20260915 has ahead 2 = cherry 0 + merges 2 (ledger section 3)",
      "git-cherry documentation: git cherry is rev-list --cherry-pick --right-only --no-merges, so a merge has no patch-id and no sign is possible from it"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "DP-s-1 BUILD steps 2 and 3: each PROD-only commit and each branch-ahead commit is split by git cherry into a '+' (patch not on DEV) and a '-' (same patch already on DEV), so the list answers whether a DEV commit carries the same patch.",
  "world_is": "git cherry gives no sign to merge commits. The tool renders them as n/a for PROD-only commits and in a separate 'merge commits (cherry omits)' column for branches, so the cherry split sums to ahead minus merges, not ahead. Not a defect in the tool (it reports what git returns); the gap is in the spec's same-patch test for merge commits. A merge-aware answer would need a per-merge diff comparison, which the cell does not cover; the CTO or issuer may rule the merge column as-is or extend the test at the round-1 analysis."
}
```

## NFRA_DEVPLN-W2-S1 -- the approval reader the merge-forward script consumes does not exist at HEAD, so a real run refuses status-unreadable until the sibling cell lands

```json
{
  "id": "NFRA_DEVPLN-W2-S1",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~2",
  "surfaced_at": "2026-10-13T19:00:14Z",
  "one_line": "The approval reader the merge-forward script consumes has no approval-status subcommand at HEAD: .tools/open-calls.py contains no approval text, so the default status command prints no APPROVAL line and every real run refuses status-unreadable until the sibling cell lands.",
  "spec_asserts": "TO DP-b-2 THE CELL: the reader is python .tools/open-calls.py approval-status --branch <b>, built by another cell at the same time; the worker consumes its one pinned APPROVAL line and tests against a fixture.",
  "world_is": "grep -n approval .tools/open-calls.py at 38ac43222d returns zero lines. The script was exercised only through OPAL_APPROVAL_STATUS_CMD fixtures (selftest 18/18). Fail closed holds on the default path: it refuses status-unreadable and never merges.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/open-calls.py@38ac43222d: grep -n approval returns 0 lines",
      ".tools/portal-merge-forward.sh (committed with this row): default status command is python .tools/open-calls.py approval-status --branch <b>; non-zero exit or no APPROVAL line refuses status-unreadable"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## NFRA_DEVPLN-W2-S2 -- the merge-forward script reads origin refs as they stand and never fetches; a stale origin/DEV is caught only at the push

```json
{
  "id": "NFRA_DEVPLN-W2-S2",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~2",
  "surfaced_at": "2026-10-13T19:00:14Z",
  "one_line": "The merge-forward script runs no git fetch: a candidate pushed after the last fetch is refused branch-not-found, and a DEV that moved after the last fetch is caught only when the push is refused as push-rejected.",
  "spec_asserts": "TO DP-b-2 BUILD step 1: <branch> is read as origin/<branch>, else the local branch; step 3: the merge is created off origin/DEV; the TO names no fetch step.",
  "world_is": "The script makes no fetch call. Selftest case 11 reproduces the lagging-tracking case: origin moves DEV, the clone's origin/DEV still points at the old commit, the merge is made on the old DEV, the push is refused push-rejected, and origin DEV is untouched. The operator must fetch before a run for the result to be current.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal-merge-forward.sh branch resolution: refs/remotes/origin/<branch> then refs/heads/<branch>, no fetch call anywhere in the script",
      "selftest 2026-10-13 at this worktree: 11a PASS push-rejected pushed=no, 11b PASS origin DEV untouched, cases=18/18"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## NFRA_DEVPLN-W2-S3 -- the AC3 grep in the TO cannot honour its "comments excepted" clause, so a comment naming git with rebase counts

```json
{
  "id": "NFRA_DEVPLN-W2-S3",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~2",
  "surfaced_at": "2026-10-13T19:00:14Z",
  "one_line": "DPb2-AC3 says comments are excepted, but its pattern git[^#|]*(rebase|--force|--force-with-lease| -f ) has no comment exclusion: any line where the word git is followed by rebase or a force option matches, comment or not.",
  "spec_asserts": "DPb2-AC3: grep -c -E git[^#|]*(rebase|--force|--force-with-lease| -f ) on .tools/portal-merge-forward.sh expects 0, comments excepted.",
  "world_is": "The pattern stops only at a hash or pipe between git and the keyword. The header comment of the script was therefore worded to avoid the pattern, and the count is 0 with comments included. The criterion holds on the text as written, not on its stated intent.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "DPb2-AC3 invocation in the TO worker face: grep -c -E git[^#|]*(rebase|--force|--force-with-lease| -f ) .tools/portal-merge-forward.sh",
      "run at this worktree after writing the script: output 0, grep rc 1 (no matching line)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## NFRA_DEVPLN-W2-S4 -- the status flip the TO asks for edits the task order file, which is not in this order's write grant

```json
{
  "id": "NFRA_DEVPLN-W2-S4",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~2",
  "surfaced_at": "2026-10-13T19:00:14Z",
  "one_line": "The TO asks for <status> to be flipped to complete with the instance, deliverables and flip committed together, but the task order file is not in <paths>, so this worker's grant does not reach it and the flip is left to the issuer or the gate.",
  "spec_asserts": "TO DP-b-2 Proof paragraph: flip <status> to complete only when every mechanical criterion passes and the instance is VALID; worker rules: <paths> is the write grant and a path the order needs but lacks is a BLOCKING row, never an override.",
  "world_is": "<paths> names .tools/portal-merge-forward.sh and the investigation file only. The task order at this worktree still reads status pending. The proof instance is written under the deliverables folder and validated by proof-of-spec-check.py; the status flip is not made by this worker.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "task-orders/NFRA_DEVPLN.TO-DP-b-2.portal-merge-forward.md (worktree @38ac43222d): <paths> lists .tools/portal-merge-forward.sh and INVESTIGATION_v1.md only",
      "task-orders/NFRA_DEVPLN.TO-DP-b-2.portal-merge-forward.md (worktree @38ac43222d): line 7 reads <status>pending</status>"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## NFRA_DEVPLN-W1-S1 -- the approval close skips the cross-box file gate, because the project's own scope reads CROSS-BOX on every approval

```json
{
  "id": "NFRA_DEVPLN-W1-S1",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~1",
  "surfaced_at": "2026-10-13T19:05:00Z",
  "one_line": "An approval row's scope is the project's round orders, and NFRA_DEVPLN reads CROSS-BOX (.tools and portal paths are shared; two paths overlap IRPT_BCKEND on dell2), so the existing close would refuse every CTO close of an approval; cmd_close skips the CLOSED-BOTH gate for kind approval.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python .tools/open-calls.py scope --project NFRA_DEVPLN, run at wk-NFRA_DEVPLN-1 @80247a96ad on 2026-10-13: CALL-SCOPE project=NFRA_DEVPLN device=laptop paths=hit placement=clear resources=clear shared=hit risk=LOCAL verdict=CROSS-BOX",
      ".tools/open-calls.py cmd_close (the DP-b-1 commit): the CROSS-BOX clause carries `and not approval`, with a comment naming why",
      "org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-b-1.approval-kind.md criterion DPb1-AC1: a CTO serial closing a client-facing row reads valid=no (a recorded close, not a refused one)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The close of an approval row takes the existing close path and records a CTO serial's approval (DPb1-AC1); the existing close refuses a CTO close of a CROSS-BOX row unless a CLOSED-BOTH cross-box file names it.",
  "world_is": "The project's scope reads CROSS-BOX for every approval of this project, so without the skip no CTO could close an approval at all. The skip is a widening: a CTO close of an approval on a project whose scope reads CROSS-BOX is recorded without a cross-box file. The validity rule in approval-status (class and closing identity) is the only gate on an approval close. The CTO rules whether that is the intended reading or whether an approval needs its own measurement of the branch's paths; the row stays ARMED until it does."
}
```

## NFRA_DEVPLN-W1-S2 -- the order states two different values of valid for a declined approval

```json
{
  "id": "NFRA_DEVPLN-W1-S2",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~1",
  "surfaced_at": "2026-10-13T19:05:00Z",
  "one_line": "The order's BUILD item 4 says valid=- when the state is not APPROVED, while its DPb1-AC1 says a declined close reads DECLINED valid=no; both cannot hold, so the built tool follows the graded criterion and prints valid=no for DECLINED.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-b-1.approval-kind.md BUILD item 4, text at base 80247a96ad: 'Otherwise valid=no (and - when the state is not APPROVED)'",
      "the same order, DPb1-AC1: 'close declined reads DECLINED valid=no'",
      "org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round1.md R3 states the class rule and is silent on DECLINED"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BUILD item 4 says valid=- when the state is not APPROVED; DPb1-AC1 says a close declined reads DECLINED valid=no.",
  "world_is": "Built: ABSENT and OPEN print valid=-; DECLINED prints valid=no, which the graded case requires. The reading that DECLINED prints valid=- is a one-line change in the DECLINED branch of cmd_approval_status, and the test case 'close declined reads DECLINED valid=no' would then need the same change. The CTO may rule either way at the round-1 analysis."
}
```

## NFRA_DEVPLN-W1-S3 -- the order's close and add invocations name flags the tool does not have, and the decomposition pins a flag the order omits

```json
{
  "id": "NFRA_DEVPLN-W1-S3",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~1",
  "surfaced_at": "2026-10-13T19:05:00Z",
  "one_line": "The order's close takes --ruling-file (the tool has --ruling) and no --id or --by; the decomposition pins add with --portal and an approval-lease subcommand that the order does not carry; built: --ruling-file as an alias, --by optional on approval closes, --asked-by and --source defaulted for approval adds, --portal and approval-lease not built.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-b-1.approval-kind.md BUILD items 2 and 3 (the close and add invocations)",
      "org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round1.md 'Pinned interfaces': add with `--portal <portal repo path>`; `approval-lease --branch <b> ... --lease-file <path>` (cell DP-b-5)",
      ".tools/open-calls.py at base 80247a96ad: close takes --ruling, requires --id and --by (build_parser, cls.add_argument)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The close invocation is close <id> --ruled-by andrew|cto --ruling-file <path> --decision approved|declined; the approval add takes no --asked-by or --source; the decomposition pins --portal on add and an approval-lease subcommand.",
  "world_is": "The existing close flag is --ruling. Built: --ruling-file is an alias of it; --by is optional on an approval close, whose identity comes from --ruled-by (andrew, or OPAL_AGENT_SERIAL for cto); an approval add defaults --asked-by to OPAL_AGENT_SERIAL and --source to the branch name. Not built: --portal (absent from the order's row shape, so the tool would have to store a field no reader declares) and approval-lease (cell DP-b-5). A command written from the decomposition's add line is refused by argparse until the order and the decomposition agree."
}
```

## NFRA_DEVPLN-W1-S4 -- an older checkout refuses a whole list that holds an approval row, because every reader refuses a key or value it does not know

```json
{
  "id": "NFRA_DEVPLN-W1-S4",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~1",
  "surfaced_at": "2026-10-13T19:05:00Z",
  "one_line": "An approval row adds the key approval and the kind value approval; a box whose checkout predates this commit refuses its whole list, and the cluster copy of that list, once one approval row exists, until it syncs.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~DV",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/open-calls.py at base 80247a96ad: validate_doc refuses an unknown row key ('row %s has unknown key(s)') and a kind outside KINDS ('kind %r is not one of')",
      "the tool docstring at base 80247a96ad, lines 25-27: 'every reader refuses a key it does not know'",
      "list --all, list --cloud and the approval reader all call validate_doc, so the refusal reaches every reader on the old tool"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The row shape adds the key approval and the kind value approval; the list is one file per box, read by every box's tool.",
  "world_is": "Until each box syncs this commit, its old tool refuses the list of any box holding an approval row (REFUSED, rc 3 on list), and the cluster copy reads REFUSED on those boxes. No version gate is built in this order. The issuer sequences the merge so that no approval row is written before every box that reads the list has synced; that act is the disarm."
}
```
