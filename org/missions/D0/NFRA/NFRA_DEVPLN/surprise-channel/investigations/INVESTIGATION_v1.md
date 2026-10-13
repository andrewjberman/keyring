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
