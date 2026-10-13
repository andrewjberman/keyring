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
