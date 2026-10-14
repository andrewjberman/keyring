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

## NFRA_DEVPLN-W3-S1 -- the cell says two Step 0 freeze bullets merge LIVE origin/DEV at GO time; only one bullet carries that text

```json
{
  "id": "NFRA_DEVPLN-W3-S1",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~3",
  "surfaced_at": "2026-10-13T19:05:42Z",
  "one_line": "The cell names two Step 0 freeze bullets that say the promote merges LIVE origin/DEV at GO time; only one bullet carries that text in .claude/skills/prod-deploy/SKILL.md at HEAD.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "DP-b-3 build step 6: in Step 0 change the two freeze bullets that say the promote merges LIVE origin/DEV at GO time so they say the promote ships the named list.",
  "world_is": "At 01c718ffe3 only the 'Declare the freeze window' bullet (SKILL.md lines 45-49) states the live-DEV merge. The 'If COO dispatched this promote via GO message' bullet (line 50) states no merge. The one merge bullet was changed to name the --features list; the GO-message bullet was left unchanged because it carries no merge statement.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-b-3.chosen-set-release.md worker face, BUILD step 6",
      ".claude/skills/prod-deploy/SKILL.md@01c718ffe3 lines 45-50 read at HEAD: one bullet names the live origin/DEV merge, the other does not"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## NFRA_DEVPLN-W3-S2 -- the builder refuses on setup and argument errors the pinned reason-token list does not name

```json
{
  "id": "NFRA_DEVPLN-W3-S2",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~3",
  "surfaced_at": "2026-10-13T19:05:42Z",
  "one_line": "The release builder needs refusal tokens for setup and argument errors (bad-args, no-workspace, no-repo, prod-ref-missing, worktree-failed, no-runtmp) that the cell's token list does not name.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "DP-b-3 build steps 2-3: a refusal names the branch and one reason token from not-approved, declined, approver-not-valid, stale-head, commits-differ, status-unreadable; release refusals are branch-not-found, conflict, unapproved-commits.",
  "world_is": "The builder also refuses with bad-args, no-workspace, no-repo, prod-ref-missing, worktree-failed and no-runtmp. Each prints the same RELEASE result=REFUSED line and exits 1 or 2, and none is a feature-level verdict. A same-second release-stamp collision waits one second and re-stamps; it prints no token.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/portal-release-build.sh at the worktree (this commit): refuse() and bad_args() call sites, header comment lists both token sets",
      "org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-b-3.chosen-set-release.md worker face, BUILD steps 2-3 (the pinned token list)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## NFRA_DEVPLN-W3-S3 -- the cell says change nothing in Steps 5-8 but also add the PROMOTE-LIST lines to the receipt, which is the Step 8 table

```json
{
  "id": "NFRA_DEVPLN-W3-S3",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~3",
  "surfaced_at": "2026-10-13T19:05:42Z",
  "one_line": "The cell keeps Steps 5-8 unchanged and also asks for the PROMOTE-LIST lines in the promote receipt, but the receipt is the Step 8 table, so the two instructions meet inside Step 8.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "DP-b-3 build step 6: 'Change nothing else in the file (the DT-only check, the push law, Steps 1-3, 5-8 and the abort path stay)' and 'Add to the promote receipt the PROMOTE-LIST lines.'",
  "world_is": "The promote receipt is the Step 8 artifact table. One row ('Promote list') was added to that table, which is the only Step 8 change; the rest of Step 8 and Steps 5-7 are unchanged.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".claude/skills/prod-deploy/SKILL.md@01c718ffe3 Step 8 table, read at HEAD: 'Field | Value' artifact table is the receipt",
      "git diff of .claude/skills/prod-deploy/SKILL.md at the worktree: one added table row inside Step 8, no other Step 8 line changed"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## NFRA_DEVPLN-W3-S4 -- the skill file carries non-ASCII bytes that predate this cell, against the cell's no-non-ASCII rule

```json
{
  "id": "NFRA_DEVPLN-W3-S4",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~3",
  "surfaced_at": "2026-10-13T19:05:42Z",
  "one_line": "The cell rule 'No non-ASCII in any file' does not hold for .claude/skills/prod-deploy/SKILL.md, which carried 189 non-ASCII bytes at HEAD and carries 183 after this cell's edit.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "DP-b-3 RULES FOR THIS CELL: 'No non-ASCII in any file.'",
  "world_is": "The skill file already held non-ASCII (em dashes, arrows, quotes) at 01c718ffe3. This cell added zero non-ASCII bytes (checked on the added diff lines); the pre-existing bytes sit outside the cell's changes and were not removed.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git show 01c718ffe3:.claude/skills/prod-deploy/SKILL.md counted with a byte scan: 189 bytes above 127",
      "the same byte scan of the worktree file: 183 bytes above 127; the added diff lines: 0 bytes above 127"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## NFRA_DEVPLN-W3-S5 -- the cell asks for the TO <status> flip to complete, but the TO file is not in the order's <paths> grant

```json
{
  "id": "NFRA_DEVPLN-W3-S5",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~3",
  "surfaced_at": "2026-10-13T19:20:00Z",
  "one_line": "The order says to flip its own <status> to complete, but its task-order file is not in the <paths> grant, so the flip is left for the issuer.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "DP-b-3 worker face: flip the task order <status> to complete only when every mechanical criterion passes and the instance is VALID; <paths> is the write grant (.tools/portal-release-build.sh, .claude/skills/prod-deploy/SKILL.md, the investigation file).",
  "world_is": "org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-b-3.chosen-set-release.md is not in <paths>, so the worker does not edit it. The status flip is left for the issuer 2.0.0_SA_COO~DV, the same disposition an earlier TO in this family recorded (NFRA_CTLPLN-W78-S4).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-b-3.chosen-set-release.md <paths> block: three entries, none is the TO file",
      "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~78/NFRA_CTLPLN.TO-CT-ab-4.kill-tools-seat-boundary.proof_of_spec.json declared_exclusions: the same flip left for the issuer"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## NFRA_DEVPLN-W1-S5 -- the DP-b-5 AC2 branch is a stale PROD cut with no DEV commit beneath it, so the overlap rule as written registers it and does not refuse it

```json
{
  "id": "NFRA_DEVPLN-W1-S5",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~1",
  "surfaced_at": "2026-10-13T19:27:10Z",
  "one_line": "DPb5-AC2 expects the real branch origin/wk-dsgn-irptv1-r25-61-prodcut (+34 over DEV) to be refused dev-overlap; its only commits over origin/PROD are 2 and neither is in origin/DEV, so the rule in BUILD item 1 registers it with commits=2.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-b-5.registration-facts-and-lease.md BUILD item 1 (overlap = commits in origin/PROD..<branch> also in origin/PROD..origin/DEV) and criterion DPb5-AC2 (expect result=REFUSED reason=dev-overlap)",
      "run at wk-NFRA_DEVPLN-1 (.tools/open-calls.py at this worktree, portal checkout wk-NFRA_DEVPLN-1-portal): python .tools/open-calls.py add --kind approval --check-only --project NFRA_DEVPLN --box dell1 --branch origin/wk-dsgn-irptv1-r25-61-prodcut --purpose x --pages x --class client-facing --how x --portal portal -> 'APPROVAL-REGISTER result=OK row=- head_sha=fc876722f5af6e92f8f045982e1b1d7ad73755f7 commits=2 check-only=yes', rc 0",
      "git -C portal: rev-list --count origin/PROD..origin/wk-dsgn-irptv1-r25-61-prodcut = 2 (fc876722, 418600b2, both subject 'feat(IRPT, DSGN_IRPTV1 IV-e-111): PROD cut'); git cherry origin/DEV on the branch marks both '+' (no equivalent patch in DEV); origin/DEV..branch = 34; merge-base(branch, origin/PROD) = 37aa1247 (an older PROD commit, not the PROD tip 15c97549); origin/PROD is not an ancestor of origin/DEV (rc 1), and origin/DEV..origin/PROD = 33"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "DPb5-AC2 says the branch is '+34 over DEV' and that its registration is refused for the DEV overlap; BUILD item 1 defines overlap as the commits of origin/PROD..<branch> that are also in origin/PROD..origin/DEV.",
  "world_is": "The branch was cut from an older PROD commit (37aa1247), so its own history over PROD is 2 commits that DEV does not hold; the 34 commits over DEV are PROD history that DEV lacks (DEV does not contain PROD), not DEV commits beneath the feature. Under the defined overlap the count is 0 and the tool registers it (result=OK, commits=2). Refusing it would need a different rule (for example, counting DEV..<branch>), and that rule would refuse every PROD cut because DEV does not contain PROD. The tool was built to BUILD item 1 and AC2 was run as written: it prints result=OK, not result=REFUSED. The CTO or issuer rules whether AC2 names another branch or the overlap definition changes. Nothing was written: the run was --check-only and the live list hash was unchanged."
}
```

## NFRA_DEVPLN-W1-S6 -- BUILD item 1 makes --portal required on add --kind approval, and the DP-b-1 approval test calls add without it, so that test now fails at its first add

```json
{
  "id": "NFRA_DEVPLN-W1-S6",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~1",
  "surfaced_at": "2026-10-13T19:27:10Z",
  "one_line": "The DP-b-5 order makes --portal required for add --kind approval (refused rc 3, reason=portal-required); the DP-b-1 approval test adds rows with no --portal and expects rc 0, so .tools/tests/test_open_calls_approval.py now fails (traceback at case 3, row_for None).",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~DV",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-b-5.registration-facts-and-lease.md BUILD item 1: '--portal ... (required for this kind; without it: APPROVAL-REGISTER result=REFUSED reason=portal-required, rc 3)'",
      "the worker's inherited state (this order's preamble): '.tools/tests/test_open_calls_approval.py passes 13/13; ... build on them without breaking that test'",
      "run at wk-NFRA_DEVPLN-1: python .tools/tests/test_open_calls_approval.py -> Traceback ... line 125 in main: cid = row_for(env, 'cand/laptop/t-cto')['id'] -> TypeError: 'NoneType' object is not subscriptable; DP-b-1 test helper add_approval (lines 82-85) passes no --portal"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BUILD item 1 requires --portal on every add --kind approval; the inherited note requires the DP-b-1 approval test to stay green.",
  "world_is": "Both cannot hold as written. The DP-b-5 change is built to BUILD item 1, so the DP-b-1 test's add calls are refused: case 1 reads no row, and case 3 raises at line 125 and the run stops there. The test file is outside this order's paths (.tools/open-calls.py, .tools/tests/test_open_calls_register.py), so it was not edited. Until the issuer amends the DP-b-1 test (pass a temporary --portal) or the requirement, the approval test is red on this branch. Nothing is written by the refused adds, so the live lists are not affected. The disarm is the issuer's: amend the DP-b-1 test or rule the requirement."
}
```

## NFRA_DEVPLN-W1-S7 -- approval-lease takes a --project the order's flag list does not name

```json
{
  "id": "NFRA_DEVPLN-W1-S7",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~1",
  "surfaced_at": "2026-10-13T19:27:10Z",
  "one_line": "BUILD item 3 lists approval-lease flags without --project, but the row needs a project for its scope and add requires --project; built: --project defaults to NFRA_DEVPLN.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "task order DP-b-5 BUILD item 3: 'approval-lease --branch <b> --box ... --purpose ... --pages ... --class ... --how ... --portal <path> --lease-file <path>' (no --project)",
      ".tools/open-calls.py at this worktree: cmd_add requires --project; approval rows carry project and scope (ROW_REQUIRED includes scope)",
      ".tools/open-calls.py approval-lease subparser: --project default NFRA_DEVPLN; --portal and --lease-file are not argparse-required, so their refusals print reason=portal-required and reason=lease-not-live with rc 3"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "approval-lease takes the listed flags and writes a CLOSED approval row for this seat's live FAST lease.",
  "world_is": "The built command accepts the listed flags and an optional --project (default NFRA_DEVPLN, the project that owns the approval kind), and --asked-by defaults to OPAL_AGENT_SERIAL. A call that omits --project gets NFRA_DEVPLN, not a refusal. The CTO may rule the default or require the flag."
}
```

## NFRA_DEVPLN-W1-S8 -- the older open-calls suite is red at base: its fork add omits --context, which the tool has required since the 2026-10-09 context rule

```json
{
  "id": "NFRA_DEVPLN-W1-S8",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~1",
  "surfaced_at": "2026-10-13T19:27:10Z",
  "one_line": "python .tools/tests/test_open_calls.py reads cases=0/2 at HEAD e2c9f07062: its base_add carries no --context, so add refuses rc 2 and the list it reads is never written.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "run at wk-NFRA_DEVPLN-1: python .tools/tests/test_open_calls.py -> FileNotFoundError at line 103 (rows()), 'OPEN-CALLS-TEST cases=0/2 ok=False'",
      ".tools/tests/test_open_calls.py base_add (line 116): add --project NFRA_CTLPLN --asked-by ... --source ... with no --context",
      "run at wk-NFRA_DEVPLN-1: python .tools/open-calls.py add --project NFRA_CTLPLN --asked-by 1.0.0_SA_CTO --source docs/none.md --subject 'own-box call' --orders <path> -> 'ERROR: --context is required for a fork call', rc 2"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The suite's first case expects a fork add without --context to write this box's list and read OWN-BOX.",
  "world_is": "The fork add refuses without --context on HEAD (the check is in cmd_add, unchanged by DP-b-5), so the suite's case 1 never writes its list and the suite exits red. The failure predates DP-b-5. The suite is outside this order's paths, so it was not edited."
}
```

## NFRA_DEVPLN-W1-S9 -- DPb5-AC2 (amended) names origin/DEV as a DEV-cut tip, but the live portal holds no commit over origin/PROD in origin/DEV, so the run prints reason=empty, not dev-overlap

```json
{
  "id": "NFRA_DEVPLN-W1-S9",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~1",
  "surfaced_at": "2026-10-13T19:39:12Z",
  "one_line": "AC2 as amended (origin/DEV, expect REFUSED reason=dev-overlap) prints APPROVAL-REGISTER result=REFUSED reason=empty commits=0 at the real portal: origin/DEV has 0 commits over origin/PROD, so no overlap can be counted.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-b-5.registration-facts-and-lease.md at c357598ced: DPb5-AC2 invocation with --branch origin/DEV and expect 'APPROVAL-REGISTER result=REFUSED reason=dev-overlap'; the amendment text says origin/DEV is a DEV-cut tip 'about 201 commits over PROD, all of them DEV-only'",
      "run at /c/Users/AndrewBerman/Desktop/ajb_wk/devpln-1 (portal checkout /c/Users/AndrewBerman/Desktop/ajb_wk/devpln-1/portal) at 2026-10-13T19:39Z: timeout 120 python .tools/open-calls.py add --kind approval --check-only --project NFRA_DEVPLN --box dell1 --branch origin/DEV --purpose x --pages x --class client-facing --how x --portal portal -> 'APPROVAL-REGISTER result=REFUSED reason=empty commits=0', rc 3",
      "read-only git -C portal at the same run: rev-parse refs/remotes/origin/PROD = 63c4f9e35f259ad76071b1099aeb9dddb150409f; refs/remotes/origin/DEV = 4d6010234ed2eb1d0a1c1782b4bf782b7e019993; rev-list --count origin/PROD..origin/DEV = 0; rev-list --count origin/DEV..origin/PROD = 34; merge-base --is-ancestor origin/PROD origin/DEV = no"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "DPb5-AC2 (as amended) says origin/DEV is a DEV-cut tip of about 201 commits over PROD, all DEV-only, and that the registration is refused reason=dev-overlap; BUILD item 1 refuses commits=0 as reason=empty, and counts overlap only within origin/PROD..<branch>.",
  "world_is": "origin/DEV is 34 commits BEHIND origin/PROD and holds no commit that origin/PROD lacks, so origin/PROD..origin/DEV is empty and the overlap set is empty. The branch origin/DEV has 0 commits over origin/PROD, so the tool refuses it at the earlier empty check (rc 3, nothing written), as BUILD item 1 defines. No branch can be refused reason=dev-overlap against this portal as it stands, because the overlap set it counts against is empty. The ~201 figure does not match the live refs. The tool follows BUILD item 1; the issuer or CTO rules the expected line or the branch. Nothing was written: the run was --check-only."
}
```

## NFRA_DEVPLN-W1-S10 -- the DP-b-1 approval test cannot be green after DP-b-5: its case 1 asserts head_sha and commits are null after an add, which DP-b-5 now writes computed; the amendment fixed only the --portal refusal

```json
{
  "id": "NFRA_DEVPLN-W1-S10",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~1",
  "surfaced_at": "2026-10-13T19:39:12Z",
  "one_line": "With --portal supplied to every approval add (item 4), .tools/tests/test_open_calls_approval.py still fails case 1 (cases=12/13 ok=False): it asserts head_sha and commits are None after add, and DP-b-5 writes them computed (commits=1, head = branch tip).",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~DV",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-b-5.registration-facts-and-lease.md at c357598ced: item 4 'the test keeps all 13 of its cases and stays green'; DPb5-AC3 expect ok=True; worker rule: do not change what that test asserts",
      ".tools/tests/test_open_calls_approval.py line 146 (case 1 of the DP-b-1 test, unchanged): r['approval']['head_sha'] is None and r['approval']['commits'] is None",
      "run at /c/Users/AndrewBerman/Desktop/ajb_wk/devpln-1: timeout 120 python .tools/tests/test_open_calls_approval.py -> first line 'FAIL  add makes an OPEN approval row (head_sha and commits null, pages split)', last line 'OPEN-CALLS-APPROVAL-TEST cases=12/13 ok=False', rc 1",
      "probe of that same case 1 add against the fixture portal (scratch script, removed): rc 0, 'APPROVAL-REGISTER result=OK row=... head_sha=be0a27ff0085efb9708b304cc3b4f1eb2cdc2a7d commits=1'; the stored row carries head_sha be0a27ff0085efb9708b304cc3b4f1eb2cdc2a7d and commits 1"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Item 4 of DP-b-5 (amended): the DP-b-1 test keeps its 13 cases, every approval add passes --portal to a temporary fixture, and the test stays green (DPb5-AC3 expects ok=True). BUILD item 1: add writes head_sha and commits computed.",
  "world_is": "Both cannot hold as written. The fixture change makes the adds succeed, and the successful add writes the computed head and commits, so case 1's null assertion is false. Making AC3 green would need that assertion changed, which the order forbids, so the assertion is left as written and the test stays red (12/13). The fixture change is in place in .tools/tests/test_open_calls_approval.py. The disarm is the issuer's: rule whether case 1 is the DP-b-1 placeholder (now computed) and amend its expectation, or keep it. Nothing was written to the live lists; the test runs on OPAL_STATE_ROOT."
}
```

## NFRA_DEVPLN-W1-S11 -- DP-c-1 names ruff on "the tool and its test", but its paths grant only the tool; the test is the tool's own --selftest

```json
{
  "id": "NFRA_DEVPLN-W1-S11",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~1",
  "surfaced_at": "2026-10-13T20:59:41Z",
  "one_line": "DP-c-1 asks for ruff clean on the tool and its test, but its <paths> name only .tools/portal-dev-approval-read.py and no separate test file is named or exists; the test is the tool's own --selftest, and ruff ran on the tool alone",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-c-1.dev-approval-read.md 5b69a3c295 RULES FOR THIS CELL ('Ruff clean on the tool and its test') and <paths> (.tools/portal-dev-approval-read.py, the investigation file, the order)",
      ".tools/portal-dev-approval-read.py 5b69a3c295-UNCOMMITTED: selftest() is the test, run as python .tools/portal-dev-approval-read.py --selftest -> DEV-APPROVAL-SELFTEST cases=7/7 ok=True; ruff check .tools/portal-dev-approval-read.py -> All checks passed!"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "DP-c-1 RULES FOR THIS CELL: ruff clean on the tool and its test; the paths block grants the tool file only.",
  "world_is": "No separate test file exists or is granted for this cell. The worker put the test inside the tool as --selftest (7 cases, exit 0) and ran ruff on the tool file only; a standalone test file would have needed a path outside the grant."
}
```

## NFRA_DEVPLN-W2-S5 -- the open-calls test was red because its fixture call lacked --context and --rec, not because the tool was wrong; repaired in the test

```json
{
  "id": "NFRA_DEVPLN-W2-S5",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~2",
  "surfaced_at": "2026-10-13T21:06:48Z",
  "one_line": "The order says the open-calls test prints cases=2/2 and that its red cause may be a fork add without --context; the test has 19 cases, and its fixture add lacked both --context and --rec, which the tool requires for a fork. The test was repaired by supplying both; the tool was not changed.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO DP-r-1 DPr1-AC1 expects OPEN-CALLS-TEST cases=2/2 ok=True, and BUILD item 1 says repair the test, not the tool, when the test is right.",
  "world_is": "At 5b69a3c295 the run prints cases=0/2 ok=False because case 1 raised FileNotFoundError: add was refused rc 2, so no state file was written. cmd_add requires --context (40-600 characters) and a fork requires --rec; the test base_add supplied neither. After the repair the run prints cases=19/19 ok=True. The denominator 2 in the order was the count of entries that existed when the test aborted.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-r-1.repair-batch.md BUILD item 1 and DPr1-AC1 (cases=2/2 expected)",
      ".tools/tests/test_open_calls.py@5b69a3c295 base_add (line 108 at HEAD) carried no --context and no --rec; python .tools/tests/test_open_calls.py at base printed cases=0/2 ok=False with the FileNotFoundError",
      ".tools/open-calls.py@5b69a3c295 cmd_add (line 1013) and check_call_text (lines 783-792) refuse a call without --context and a fork without --rec"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## NFRA_DEVPLN-W2-S6 -- approval-lease --project breaks four lease cases of test_open_calls_register.py, a file outside this order's paths

```json
{
  "id": "NFRA_DEVPLN-W2-S6",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~2",
  "surfaced_at": "2026-10-13T21:06:48Z",
  "one_line": "Making approval-lease require --project (DPr1-AC3) turns four lease cases of test_open_calls_register.py red: its register_lease helper calls approval-lease without --project. That file is not in this order's paths, so the one-argument fix cannot be made here, and the order's keep-green instruction cannot be met inside the grant.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "TO DP-r-1 BUILD item 3: --project becomes required; keep test_open_calls_approval.py and test_open_calls_register.py green.",
  "world_is": "At this worktree test_open_calls_register.py prints OPEN-CALLS-REGISTER-TEST cases=6/10 ok=False. The four failing cases (a live lease writes an APPROVED row; expired, other-seat and HOLD leases; a missing lease file; a live lease on a DEV-cut branch) each exit rc 2 at argparse before their own check. Test_open_calls_approval.py stays 13/13 ok=True. No caller in the tree omits --project except that helper, so the hazard is a loud refusal, not silent harm. The fix is --project NFRA_DEVPLN in register_lease, a path the order does not grant.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/tests/test_open_calls_register.py@5b69a3c295 line 136 register_lease builds approval-lease args with no --project",
      ".tools/open-calls.py@5b69a3c295 approval-lease --project is required=True after this order's edit (line 1797); argparse prints 'the following arguments are required: --project' with rc 2",
      "git grep approval-lease at 5b69a3c295: the only caller that omits --project is the register test helper"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## NFRA_DEVPLN-W2-S7 -- the default fetch refuses a branch that exists only locally with fetch-failed; the local fallback runs only under --no-fetch

```json
{
  "id": "NFRA_DEVPLN-W2-S7",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~2",
  "surfaced_at": "2026-10-13T21:06:48Z",
  "one_line": "The order does not say whether a branch missing from origin is a failed fetch. Built as one: the default run fetches the branch and refuses fetch-failed when origin has no such ref, so the local-only fallback in step 1 is reachable only with --no-fetch.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO DP-r-1 BUILD item 2(a): before it decides it fetches origin for DEV and for the branch; a failed fetch is REFUSED fetch-failed; item 2(c): --no-fetch on an unknown branch still prints branch-not-found.",
  "world_is": "A temporary repository with a local branch localonly and no origin ref: the default run prints result=REFUSED reason=fetch-failed (git: couldn't find remote ref refs/heads/localonly); with --no-fetch the same branch passes step 1 and reaches the approval reader. The temporary repository was not the real portal.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/portal-merge-forward.sh@wk-NFRA_DEVPLN-2 (uncommitted at this row) fetch block after git check-ref-format: git fetch origin '+refs/heads/<branch>:refs/remotes/origin/<branch>' refuses fetch-failed",
      "temporary repository under mktemp -d with origin.git and a local branch localonly: default run REFUSED fetch-failed; --no-fetch run reaches status-unreadable (the reader stand-in printed nothing)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## NFRA_DEVPLN-W2-S8 -- proof-of-spec-check's POST-COMMIT pin-drift line names 066fd5d7e2 as the commit that changed the register test row's file, and git says it did not

```json
{
  "id": "NFRA_DEVPLN-W2-S8",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~2",
  "surfaced_at": "2026-10-13T21:18:04Z",
  "one_line": "On the proof instance for DP-r-1, the checker's artifact-resolution/pin-drift line reports 1 row whose pinned version had a line removed or changed by 066fd5d7e2 (the proof-instance commit). The row is .tools/tests/test_open_calls_register.py pinned at 6b9bc6662b, the one-line repair. Git shows 066fd5d7e2 adds only the instance file (118 insertions) and touches no tool or test file.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "proof-of-spec-check artifact-resolution: a pinned row's graded content is read at its pin, and POST-COMMIT drift is announced when the pinned version was changed by the instance commit (AMGT_CORPUS-Z-S70 class).",
  "world_is": "The checker returned VALID rc=0 with 5/5 rows and 0 violations; its drift announcement attributes a change to a commit that does not touch the cited file. git log -- .tools/tests/test_open_calls_register.py lists 6b9bc6662b then 7bff1eab9b, and 066fd5d7e2 is an ancestor of 6b9bc6662b, so the attribution is not the instance commit's diff. The announcement is advisory (ANNOUNCED, not asserted) and did not change the verdict.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "proof-of-spec-check run on org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.9.0_WK_NFRA_DEVPLN~2/NFRA_DEVPLN.TO-DP-r-1.repair-batch.proof_of_spec.json: artifact-resolution/pin-drift names .tools/tests/test_open_calls_register.py@6b9bc6662b, 1 line changed by 066fd5d7e2",
      "git show --stat 066fd5d7e2: 1 file changed, 118 insertions, the instance JSON only",
      "git log --oneline -3 -- .tools/tests/test_open_calls_register.py at HEAD: 6b9bc6662b, 7bff1eab9b"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## NFRA_DEVPLN-W1-S12 -- the cited ruling names three merges, not the four waived commits; the waiver ref is checked for existence only

```json
{
  "id": "NFRA_DEVPLN-W1-S12",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~1",
  "surfaced_at": "2026-10-13T22:01:38Z",
  "one_line": "The CTO ruling cited as --waiver-ref names three merges (62d455f5 through a577cba5) and not the four commits the waiver names; the tool checks only that the ref file exists",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261013_213xZ_LAPTOP_E846_7D95_BB8B.md@f3cc33dddc lines 29-34: the three IRPT_ANLREQ merges 62d455f5 through a577cba5; WAIVED for exactly these three named merge shas; No other DEV-only commit is admitted this way. Only 62d455f5 is named literally; 923f7d69, 794b7df4 and 9ef6a359 do not appear in the file (grep, worktree)",
      "DP-d-1 order, AC2: the waiver names 923f7d69,794b7df4 and cites this ruling; the check-only run returned APPROVAL-REGISTER result=OK row=- head_sha=794b7df495d2baa3d2f887f148f4389e729ca07d commits=2 check-only=yes waived=2 rc 0",
      ".tools/open-calls.py@worktree waiver_ref_rel(): the --waiver-ref check is os.path.isfile only; the ruling's text is not read, so a ref that names none of the waived shas is accepted"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "DP-d-1 cell: the CTO ruled the DEV-overlap refusal WAIVED for exactly four named commits, 923f7d69, 794b7df4 (feature head), 9ef6a359 and 62d455f5, and the waiver is referenced by a ruling file.",
  "world_is": "The cited ruling CTO_RULING_20261013_213xZ_LAPTOP_E846_7D95_BB8B.md names three IRPT_ANLREQ merges, 62d455f5 through a577cba5, and says the waiver is for exactly those three named merge shas. Only 62d455f5 appears literally in it; the four-commit set is the issuer's reading recorded in the decomposition, not the ruling's text. The waiver tool accepts any existing ref file, so AC2 registers the 794b7df4 waiver on a ruling that does not name two of its shas. Nothing was registered by this cell (check-only only)."
}
```

## NFRA_DEVPLN-W2-S9 -- the local-only fallback reads refs/heads/<branch> even when a stale refs/remotes/origin/<branch> remains, where --no-fetch would read that remote-tracking ref

```json
{
  "id": "NFRA_DEVPLN-W2-S9",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~2",
  "surfaced_at": "2026-10-13T22:01:01Z",
  "one_line": "TO DP-d-2 says an absent-on-origin branch continues exactly as --no-fetch would, but --no-fetch reads refs/remotes/origin/<branch> first when it exists. Built the local fallback to skip that ref, so the NOTE 'using the local branch' is true; a remote-tracking ref left by a branch deleted on origin is not merged.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO DP-d-2 BUILD item 1: absent on origin -> do NOT fetch it, do NOT refuse; continue with the local branch exactly as --no-fetch would, and print the NOTE line.",
  "world_is": "Step 1 of .tools/portal-merge-forward.sh prefers refs/remotes/origin/<branch> over refs/heads/<branch> whenever the former exists. In the absent-on-origin path the built code sets local_only=1 and skips that preference, so refs/heads/<branch> is read. The two readings differ only when a stale remote-tracking ref survives a branch deleted on origin; no such case is measured in the portal repo (the probe branch has no origin ref) and none is exercised by the selftest.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/portal-merge-forward.sh@wk-NFRA_DEVPLN-2 (uncommitted at this row) step 1: local_only flag set in the ls-remote exit-2 branch and tested before the origin/<branch> preference",
      "git -C portal rev-parse --verify -q refs/remotes/origin/cand/laptop/local-only-probe: exit 1 (no stale remote-tracking ref for the probe branch)",
      "selftest case 13a: local-only branch under the default fetch, MERGED with the NOTE line on stderr"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## NFRA_DEVPLN-W2-S10 -- the AC2 seam run prints a git multiple-merge-bases warning from the three-dot diff, and the step-2 product-file test reads one of the two bases

```json
{
  "id": "NFRA_DEVPLN-W2-S10",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~2",
  "surfaced_at": "2026-10-13T22:01:01Z",
  "one_line": "Running the AC2 seam against the real portal prints 'warning: refs/remotes/origin/DEV...refs/heads/cand/laptop/local-only-probe: multiple merge bases'. The ABSENT path's git diff --name-only DEV...BRANCH uses one of the two merge bases, so its product-file list is not the full three-dot set.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO DP-d-2 AC2: the seam against the real portal repo and the local-only branch is refused no-approval-row, and nothing is merged, pushed or left behind.",
  "world_is": "The AC2 call returned result=REFUSED reason=no-approval-row (rc=1) with the warning on stderr. git merge-base --all on the DEV tip and the probe branch returns 2 bases (63c4f9e35f, 07f065e69f). The verdict is the required one; whether a different base would change the product-file list for this branch is not measured.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "bash .tools/portal-merge-forward.sh cand/laptop/local-only-probe --repo portal (rc=1): stderr line 'warning: refs/remotes/origin/DEV...refs/heads/cand/laptop/local-only-probe: multiple merge bases, using 63c4f9e35f...'",
      "git -C portal merge-base --all refs/remotes/origin/DEV refs/heads/cand/laptop/local-only-probe: 2 lines (63c4f9e35f..., 07f065e69f...)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## NFRA_DEVPLN-S2 -- the route needs a withdraw decision and a cluster-first read for another box's rows

```json
{
  "id": "NFRA_DEVPLN-S2",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~DV",
  "surfaced_at": "2026-10-13T22:25Z",
  "one_line": "dell2's first organic client-facing approval (cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal) exposes two route gaps: an approval row has no lawful close except approved or declined (a duplicate cannot be withdrawn), and approval-status reads a foreign box's list from a stale working-tree copy instead of the cluster copy.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "relay from 0.0.0_AB_MSTR (bus 4ac17c50, CTO~DELL2 msg 7302): dell2 registered the same branch twice, dell2-20261013T221352Z-cffa (keep) and dell2-20261013T221411Z-3635 (duplicate); close takes only --decision approved|declined, so closing the duplicate declined could read as Andrew declining the feature",
      "python .tools/open-calls.py list --all --cloud at ~22:25Z: both rows listed OPEN from the cluster copy",
      "python .tools/open-calls.py approval-status --branch cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal on the laptop: state=ABSENT (the laptop's working-tree copy of dell2's list predates the rows; approval_read at .tools/open-calls.py:1459 prefers any working-tree file over the cluster copy and over origin/box/dell2)",
      "approval_read picks the NEWEST row per branch by opened_at: the duplicate 3635 (22:14:11Z) would be the row the merge-forward reads, so approving only cffa would still refuse as not-approved"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD v0.3 C-APPROVAL: one row per feature, the row is the record the merge-forward and the promote read; FWD-2: the list is the open-calls list he already reads, from whichever box he is at.",
  "world_is": "Two defects in the route for a feature on a box other than the one running the merge-forward. (1) A duplicate row is read as the feature's row and cannot be withdrawn: the route needs a close decision of withdrawn that the status reader ignores (all rows withdrawn reads ABSENT, so the consumers refuse). (2) A foreign box's list is read from a possibly stale local copy; a stale readable copy reads as ABSENT, which for a test-only change would let the merge-forward proceed. The reader should take a foreign box's list from the cluster copy first and fall back to git. Interim: leave both rows OPEN and have Andrew close BOTH with the same decision. Proposed as the first two cells of round 4, ahead of the CTO's analysis."
}
```

## NFRA_DEVPLN-W1-S13 -- the worktree's portal gitlink is recorded at 4d601023 but its nested checkout sits at 24877b67, so git status shows portal modified before any edit

```json
{
  "id": "NFRA_DEVPLN-W1-S13",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~1",
  "surfaced_at": "2026-10-13T22:54:33Z",
  "one_line": "At the start of DP-e-1 the worktree HEAD records portal at 4d6010234e, but the nested portal checkout (branch wk-NFRA_DEVPLN-1-portal) is at 24877b67b7 and git diff reports portal as modified; the portal is read only for this order, so it was left as found and not committed",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git ls-tree HEAD portal (worktree /c/Users/AndrewBerman/Desktop/ajb_wk/devpln-1, HEAD 7dbc992996): 160000 commit 4d6010234ed2eb1d0a1c1782b4bf782b7e019993 portal",
      "git -C portal rev-parse HEAD: 24877b67b7a175bcfe73c779f69c0bf7c3c639c8 (branch wk-NFRA_DEVPLN-1-portal; git -C portal log: 24877b67 Merge cand/laptop/contributing-boxes into DEV)",
      "git -C portal merge-base --is-ancestor 4d6010234ed2eb1d0a1c1782b4bf782b7e019993 24877b67b7a175bcfe73c779f69c0bf7c3c639c8: ancestor (the checkout is ahead of the recorded pin); git -C portal status --short: 0 lines (the nested checkout is clean)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The worker face says the portal checkout is READ ONLY for this worker and the worktree carries the order's paths only; a portal change is made on a cand branch cut from the last PROD release.",
  "world_is": "The worktree's recorded gitlink for portal is 4d6010234e, one commit behind-or-equal to a nested checkout at 24877b67b7 that is ahead of it on the wk-NFRA_DEVPLN-1-portal branch, so the parent index reports portal as modified with no edit by this worker. The cell touches no portal file, so DP-e-1 is unaffected; the gitlink mismatch is not repaired by this worker."
}
```

## NFRA_DEVPLN-S3 -- the pre-push payload limb (CTO addendum) missed round 4; the gate refused a same-round add

```json
{
  "id": "NFRA_DEVPLN-S3",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~DV",
  "surfaced_at": "2026-10-13T23:05Z",
  "one_line": "The CTO's round-3 analysis ADDENDUM item (a DEV payload limb in the portal repo's pre-push hook) is missing from the round-4 issuance 7dbc992996; the issuer cut without re-reading the analysis after it grew, and the pipeline gate refused adding the order to the same round (one issuance per round).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "ledger/ROUND_ANALYSIS.round3.md ADDENDUM ~22:3xZ: 'The structural close is a payload check in the portal repo's git pre-push limb ... That is a round-4 cell for this project.' The issuer read the file at ~22:25Z (3 sections) and cut at ~22:55Z (issuance 7dbc992996: DP-e-1, DP-e-2, DP-e-3).",
      "attempted amendment commit adding NFRA_DEVPLN.TO-DP-e-4: .tools/to-pipeline-gate.py REFUSED it: 'workstream ENRICHMENT round 4 of NFRA_DEVPLN already has an issuance at HEAD ... ONE ISSUER PER ROUND is keyed to the ROUND, never the serial (Rule 27)'. No override was taken. The draft order is saved at org/tier1_exec/2.0.0_SA_COO~DV/deliverables/drafts/ROUND5_DRAFT_dev-push-payload-limb.md",
      "the CTO named .tools/git-hooks/pre-push-safe-deploy.sh as the portal repo's pre-push limb; that file is the workspace repo's HALTGT hook (it delegates to safe-deploy.sh and never runs on a portal push). The portal repo's installed hook portal/.git/hooks/pre-push is byte-identical to .tools/portal-hooks/pre-push (cmp), which already carries the per-ref VALGATE loop"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CTO round-3 analysis addendum: the pre-push payload limb is a round-4 cell for NFRA_DEVPLN, in .tools/git-hooks/pre-push-safe-deploy.sh.",
  "world_is": "The limb is not in round 4. The correct file is .tools/portal-hooks/pre-push (plus a separate checker script). It becomes the first cell of round 5 unless the CTO rules an audited pipeline override into round 4 on his own word; the issuer takes neither route on its own."
}
```

## NFRA_DEVPLN-W2-S11 -- the merge-forward self-test fixture writes have no exit check, so a failed write silently produces a degenerate graph

```json
{
  "id": "NFRA_DEVPLN-W2-S11",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~2",
  "surfaced_at": "2026-10-13T22:58:47Z",
  "one_line": "pmf_selftest builds its fixtures with no set -e and no exit check on the git and printf steps. A failed write inside the fixture does not stop the self-test; it yields an empty commit and a graph that is not the one the case names.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO DP-e-3 BUILD: the self-test adds case 16, a criss-cross history (two merge bases) built in a mktemp repository, asserting no multiple-merge-bases warning and an ABSENT product-file refusal.",
  "world_is": "In the first draft of case 16 the y-side write ran before its src/__tests__ directory existed. The printf failed with 'No such file or directory', the commit reported 'nothing to commit', and git merge-base --all returned ONE base, so the criss-cross was not built. The draft's own run printed cases=28/29 ok=False; only the new precondition (16a) caught the degenerate graph. Without such a precondition a fixture failure would read as a green case on the wrong graph. The fix in case 16 is a mkdir before the write. The fixture steps of cases 1-15 carry the same unchecked failure mode and were not changed (out of this order's paths and cell).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "wk-NFRA_DEVPLN-2 .tools/portal-merge-forward.sh at dc9b9ed25a (HEAD before this order's commit): pmf_selftest runs its fixture git and printf commands with no set -e and no exit check",
      "probe at .scratch/criss-probe (the same graph built by hand, before the fix): 'No such file or directory' for src/__tests__/y.test.ts, 'nothing to commit, working tree clean', and git merge-base --all cc-x cc-y printed one base (766371a7)",
      "selftest run before the fix: 'SELFTEST FAIL 16a precondition: the criss-cross branch has exactly two merge bases' and 'MERGE-FORWARD-SELFTEST cases=28/29 ok=False'; after the mkdir fix: cases=29/29 ok=True"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## NFRA_DEVPLN-W1-S14 -- the DP-e-2 build step 6 needs a git-source test seam the order does not name; the cell adds OPAL_GIT_READ_ROOT (tests only) beside OPAL_CLOUD_READ_LOCAL

```json
{
  "id": "NFRA_DEVPLN-W1-S14",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~1",
  "surfaced_at": "2026-10-13T23:13:04Z",
  "one_line": "The order names one test-only variable (OPAL_CLOUD_READ_LOCAL) for the cluster stand-in, but its git-newer-than-cluster case cannot run without a controlled origin/box/<box> ref; the cell adds a second test-only variable OPAL_GIT_READ_ROOT, read only when set, and the test builds its own temporary repository",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "approval_read git source before this cell (.tools/open-calls.py at 4d40d2552f): subprocess.run([\"git\", \"-C\", ROOT, \"show\", \"origin/box/<box>:org/devices/state/<box>/open_calls.json\"]); ROOT is the real checkout, so a test reads the real refs",
      "git -C <worktree> rev-parse origin/box/dell2 is the real remote ref; a test that needs git newer than a stale cluster copy must either write a real ref or read the real dell2 history, and neither is a temporary state",
      ".tools/tests/test_open_calls_cloudread.py case 2 (git newer than a stale cluster copy) runs with OPAL_GIT_READ_ROOT pointing at a temporary repository; 7/7 cases pass, and the real refs are untouched"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "DP-e-2 build step 4 adds ONE test-only variable, OPAL_CLOUD_READ_LOCAL, and build step 6 requires a foreign box whose git copy is newer than a stale cluster copy to read git, on a temporary state root.",
  "world_is": "The git source has no test seam of its own, so the git-newer case cannot be exercised without a second variable; OPAL_GIT_READ_ROOT is that seam (the repository whose origin/box refs are read, default ROOT, unset in production). The order's one-variable count is exceeded by this one; the production read path and the grammar of the approval-status line are unchanged."
}
```

## NFRA_DEVPLN-W1-S15 -- The order gives a live FAST lease admission for the whole push (BUILD 4) and refusals for a delete, a new ref and a non-

```json
{
  "id": "NFRA_DEVPLN-W1-S15",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~1",
  "surfaced_at": "2026-10-13T23:55:45Z",
  "one_line": "The order gives a live FAST lease admission for the whole push (BUILD 4) and refusals for a delete, a new ref and a non-fast-forward (BUILD 2) without an order between them; the cell runs the structural refusals first, so a lease admits only the commit walk",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/portal-hooks/dev_push_payload_gate.py decide() at the worktree (working copy at bb0100a77b, uncommitted at write time): ref skip, then delete, new-ref and not-fast-forward refusals, then the FAST lease check, then the commit walk",
      "the order's BUILD 2 names the three refusals and BUILD 4 says 'the whole push is ADMITTED reason=fast-lease' with no ordering between them",
      "tests: .tools/tests/test_dev_push_payload_gate.py cases 'delete refused', 'new ref refused', 'non-fast-forward refused' run with no lease, and the lease cases run with a commit payload; 19/19 pass"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BUILD 4: a live FAST lease held by OPAL_AGENT_SERIAL makes the whole push ADMITTED reason=fast-lease; BUILD 2: a delete, a new branch or a non-fast-forward push is REFUSED. The order names no precedence between the two.",
  "world_is": "A lease seat that pushes a delete or a non-fast-forward of DEV is still refused, because the structural refusals run before the lease check. The lease therefore exempts only the commit payload walk. The order's 'whole push' wording would admit a delete or a history rewrite; the built order does not. Reported for the lane owner's ruling, not changed here."
}
```

## NFRA_DEVPLN-W2-S12 -- the one-variable seam needs a test-only guard keyed on OPAL_STATE_ROOT, or the no-source case reads the real origin/box refs

```json
{
  "id": "NFRA_DEVPLN-W2-S12",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~2",
  "surfaced_at": "2026-10-14T01:00:28Z",
  "one_line": "With OPAL_GIT_READ_ROOT removed, a test with OPAL_CLOUD_READ_LOCAL unset would still read the git source from the real checkout ROOT. The cell skips the git source when OPAL_STATE_ROOT is set and OPAL_CLOUD_READ_LOCAL is not, so test case 4 (no readable source) stays hermetic. The order names no such guard.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "DP-f-2 build step 1: remove OPAL_GIT_READ_ROOT entirely; OPAL_CLOUD_READ_LOCAL stands in for the git source when set; production reads (variable unset) are unchanged; the tests use no real git ref and no S3.",
  "world_is": "With OPAL_CLOUD_READ_LOCAL unset, _source_git runs git show against ROOT's real origin/box/<box> refs, so test case 4 (cluster=False, no working-tree copy) would read the real list for a foreign box and fail its UNREADABLE assertion. The cell adds a guard in _source_git: when OPAL_STATE_ROOT is set and OPAL_CLOUD_READ_LOCAL is unset, the git source is skipped with a reason. The guard is reached only under a test switch; production, with both variables unset, is unchanged. Four other first-party tools also name OPAL_STATE_ROOT (open-calls-scan.py, seat-list.py, xadj.py, open-calls.py); I did not read the first three, so whether any sets it in production is UNVERIFIED.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "wk-NFRA_DEVPLN-2 .tools/open-calls.py _source_git (uncommitted at 6d46d2db81 plus this cell's edit): 'if os.environ.get(\"OPAL_STATE_ROOT\", \"\").strip(): raise _Skip(\"git copy not read under the test switch (OPAL_STATE_ROOT)\")' placed after the OPAL_CLOUD_READ_LOCAL branch",
      "comp-find --files 'OPAL_STATE_ROOT' .tools: DENOMINATOR 30 hit(s) across 535 file(s) scanned in scope [corpus=all]; BANDS SURFACED=16 TEST=14",
      "python .tools/tests/test_open_calls_cloudread.py: cases=8/8 ok=True; test_open_calls.py 19/19, _approval 13/13, _register 10/10, _waiver 11/11, _withdraw 7/7, each ok=True"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## NFRA_DEVPLN-W1-S16 -- with OPAL_STATE_ROOT unset the production git source runs a real git show, so the zz9 no-stand-in case cannot keep the real origin/box refs unread

```json
{
  "id": "NFRA_DEVPLN-W1-S16",
  "project": "NFRA_DEVPLN",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_DEVPLN~1",
  "surfaced_at": "2026-10-14T01:27:47Z",
  "one_line": "The order says tests read no real origin/box ref, yet its case (a) runs with OPAL_STATE_ROOT unset, which is exactly the production path that runs git show against ROOT's real origin/box refs",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "worktree .tools/open-calls.py _source_git (wk-NFRA_DEVPLN-1, uncommitted at 596f3a96ad plus this cell's edit): with _seam_dir() returning empty (no OPAL_STATE_ROOT), the function falls through to subprocess git -C ROOT show origin/box/<box>:org/devices/state/<box>/open_calls.json",
      "worktree .tools/tests/test_open_calls_cloudread.py case 9 (stand-in set, OPAL_STATE_ROOT unset, box zz9): status() passes state=False, so the production git source runs for box zz9; the ref is absent, so git show fails and the source is skipped",
      "python .tools/tests/test_open_calls_cloudread.py: cases=10/10 ok=True; test_open_calls_approval 13/13, _register 10/10, _waiver 11/11, _withdraw 7/7 ok=True"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Tests make no S3 call and read no real origin/box ref. Case (a): the stand-in is set, OPAL_STATE_ROOT is unset, box zz9 exists nowhere in the repo, expect UNREADABLE rc 2 with the fixture row not used.",
  "world_is": "Case (a) cannot run without the production git source, because the seam is ignored when OPAL_STATE_ROOT is unset. The production source then issues git show against the real origin/box/zz9 ref. The ref does not exist, so nothing is read and the case passes, but the test does touch the real repo's ref namespace. A box that did have a real origin/box ref would be read. The tests-read-no-real-ref rule holds only because zz9 is absent. Reported for the lane owner's ruling; the production path is unchanged and no test switch was added to the git source for this case."
}
```
