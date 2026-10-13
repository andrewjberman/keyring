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
