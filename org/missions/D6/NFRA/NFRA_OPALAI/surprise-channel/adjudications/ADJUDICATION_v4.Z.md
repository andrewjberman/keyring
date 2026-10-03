# NFRA_OPALAI -- round 2 MID-ROUND L8 compile, dismissals only (site Z)

Author: 3.0.0_SA_CVO~O. Round: 2 (L7 open: OA-e-8, OA-t-1.r2 and OA-t-3.r2 pending on the cutover). Fabric: site-z.
Written: 2026-10-02T15:40:00Z.

Why now: the seat was relaunched on Andrew's word to finish NFRA_OPALAI
(`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261002_14xxZ_YES_RELAUNCH_OPALAI_SEATS_CTO_O_COO_AI_CVO_O.md`).
The round's last three orders wait on Andrew's acts (the OA-f-12 push to opal_ai PROD, then the item-0 close run).
This compiles the backlog now, so the round-2 compile at the drain-end has less to read.

Input: the census of the channel at CLOUD `9c15c703a6`. It covers 100 items over 4 investigation and adjudication
documents plus 1 remediation document. Before this compile, 29 items were undispositioned, rows Z-S36 through Z-S56,
and 0 of them were BLOCKING or ARMED. C-S9 dismisses 20 of them.

HELD, NOT ROUTED: 9 items are real defects still live at HEAD: Z-S36, Z-W10-S2, Z-S39, Z-S40, Z-S42, Z-S51, Z-S53,
Z-S54 and Z-S55. A new remediation row IS the slug, and `.tools/surprise-row-gate.py` refused them because 3 of 39
orders are not terminal (LD-0521). They stay UNDER_INVESTIGATION here. Their draft graduation and the measurements
behind it are held, unrouted, in
`org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_OPALAI_R2_HELD_GRADUATIONS_20261002.md`. At the drain-end this seat
re-measures each one and lands the graduations with the slug.

L9: J1 (OA-r-1) was graded PASS earlier (@c180d84b36). J2 (OA-t-1.r2) is graded on the close run, so no L9 grade is
owed in this compile.

```json
[
  {
    "id": "NFRA_OPALAI-Z-C-S9",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-02T15:20:00Z",
    "one_line": "Round 2 mid-round L8: 20 INERT rows are DISMISSED_WITH_REASON. Each has a fix this seat re-read at HEAD, was superseded by a later cell, is a record that disarms nothing, or has its residual on a named open order.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row up to its watermark.",
    "world_is": "Dismissed here, by kind. FIXED AND RE-READ HERE: Z-W10-S1 (the pytest -rA matcher reads tests[/\\] in e1.AC1.sh:10 and its siblings e3.AC3, e10.AC2 and f7.AC1); Z-W11-S2 with its clearance record Z-W11-S3 (the AC1 bound was raised to 105 s at c7a5391c18, and e2.AC1-AC3 PASS); Z-S43 (the content was repaired at 9353136df3; the class now fails loud, because safe-merge.sh:485-488 reads the tree after every drain commit and exits 5 on a dropped path, since 380ebf5954); Z-S56 (the runtime checkout C:/opal_runtime/opal_ai reads 9c0a80b8d0 and is clean; its launcher.ps1 hashes to df5df41645, equal to bd7cd5d and 9c0a80b8d0, while fd8ab8a's blob 6ea313859a differs, the negative control). SUPERSEDED BY A LATER CELL: Z-W14-S1 (the dead 8194 control was re-measured REACHABLE 4 of 4 with a live control at 5e49690a68; OA-e-6 is complete); Z-W25-S1, Z-W25-S3 and Z-S52 (the per-user Firewall mechanism was retired: OA-f-10 is superseded by OA-f-11, whose WFP wall is AC3 PASS, and Andrew removed the R1 rules on 2026-10-02 ~02:4xZ, per OA-f-10's terminal status); Z-W25-S2 (codex's own sandbox setup wrote the ACEs; it was tried once and not repeated); Z-S50 (the launcher's two defects were cut as OA-f-8 and OA-f-9, both complete, on r2-dev 97b3b19, b6e1867 and bd7cd5d; the proof on a served launch rides the open order OA-t-3.r2 and the item-0 close run). TIE-BREAK AND CENSUS METHOD, NO OPEN ORDER CARRIES THEM: Z-S38 and Z-W10-S3 (the word 'newest' appears in 3 order files, OA-e-3, OA-e-9 and OA-r-1, all complete; the worker resolved the base on the files where the survivors differ, and the host ran 6a98a0553a); Z-W10-S7 (the pending move OA-t-1.r2 has no rev-list population; its checks read fixed path lists). RECORDS WITHIN BOUNDS: Z-W16-S1 (the 21-day journal gap is named in the E10 census and cannot be recovered on the host); Z-W16-S2 (the allow-list is derived from two existing settings, because config.py was outside <paths>); Z-W16-S3 (4-character prefixes went to the worker's session output only; nothing was committed; this is a recorded breach of bound 3, inert); Z-W22-S1 (store-borne [] and an absent key both fail closed with nothing fetched); Z-W24-S1 (the AC1 comment-strip is over-strict, so it fails closed; the order is complete); Z-S41 (the issuer's own probe files, cleared before the re-run; its fact (2) about Start-Process -Credential is moot, because OA-f-9 moved the launcher to Process.Start).",
    "adjudicates": [
      "NFRA_OPALAI-Z-S38",
      "NFRA_OPALAI-Z-W10-S1",
      "NFRA_OPALAI-Z-W11-S2",
      "NFRA_OPALAI-Z-W11-S3",
      "NFRA_OPALAI-Z-W16-S1",
      "NFRA_OPALAI-Z-W16-S2",
      "NFRA_OPALAI-Z-W16-S3",
      "NFRA_OPALAI-Z-S41",
      "NFRA_OPALAI-Z-W10-S3",
      "NFRA_OPALAI-Z-W22-S1",
      "NFRA_OPALAI-Z-S43",
      "NFRA_OPALAI-Z-W10-S7",
      "NFRA_OPALAI-Z-S50",
      "NFRA_OPALAI-Z-W24-S1",
      "NFRA_OPALAI-Z-W14-S1",
      "NFRA_OPALAI-Z-W25-S1",
      "NFRA_OPALAI-Z-W25-S2",
      "NFRA_OPALAI-Z-W25-S3",
      "NFRA_OPALAI-Z-S52",
      "NFRA_OPALAI-Z-S56"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e1.AC1.sh:10 (grep -qE \"^PASSED tests[/\\]...\")",
        ".tools/safe-merge.sh:485-488 (_verify_merge_tree HEAD after the drain commit; exit 5) and commit 380ebf5954",
        "git -C C:/opal_runtime/opal_ai rev-parse HEAD = 9c0a80b8d0, status clean; hash-object opal/runtime/launcher.ps1 = df5df41645 = git -C opal_ai rev-parse bd7cd5d:opal/runtime/launcher.ps1; fd8ab8a's blob = 6ea313859a",
        "commit 5e49690a68 (OA-e-6 re-measure, 4 of 4 OPEN with a live 8194 control)",
        "task-orders/NFRA_OPALAI.TO-OA-f-10.dapi-8194-wall.md last <status>: superseded by OA-f-11 (AC3 PASS)",
        "opal_ai nfra-opalai-r2-dev log: 97b3b19, b6e1867 (OA-f-9), bd7cd5d (OA-f-12)",
        "Grep 'newest' over task-orders/: 3 files (OA-e-3, OA-e-9, OA-r-1), all <status>complete</status>",
        "Grep 'rev-list' over task-orders/NFRA_OPALAI.TO-OA-t-1.r2-product-files-move.md: 0 hits",
        "investigations/INVESTIGATION_v1.Z.md rows Z-S38 .. Z-S56 as listed"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each row is fixed at HEAD, superseded by a later complete cell, or a record within bounds, or its residual rides a named open order. None carries an unowned hazard."
  }
]
```

-- 3.0.0_SA_CVO~O
