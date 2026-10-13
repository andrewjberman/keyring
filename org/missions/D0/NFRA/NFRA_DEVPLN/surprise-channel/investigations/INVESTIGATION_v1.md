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
