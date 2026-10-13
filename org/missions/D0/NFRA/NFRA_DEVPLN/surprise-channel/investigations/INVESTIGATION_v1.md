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
