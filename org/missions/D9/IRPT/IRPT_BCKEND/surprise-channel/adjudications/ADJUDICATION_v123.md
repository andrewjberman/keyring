# IRPT_BCKEND: CVO adjudication, round 1 (workstream ~PI, class WORLD: the APPLY of the signed pair IB-pr-456, the commentary_requested release)

<sweep_watermark>2026-10-15T16:05Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T16:05Z, on msg 8439 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_1_PI_DRAIN_END_20261015.md` @aadbb13fde). One order, IB-pr-579 (risk WORLD, applied by `0.7.0_AE_CloudOps~IB2`), complete. Re-run here at HEAD: IB217-1-AC1..AC3 PASS (exit 0). `round-close-check --round 1 --workstream "~PI"`: orders=1, proofs 1 of 1 ok, verdict=MAY-CLOSE. Read-only on AWS: `get-function-configuration`, `get-function` (the code URL), and `head-object`/`get-object` of one artifact version.

**(1) The live code IS the signed candidate, by content.** `irpt-ycharts-generate` reads CodeSha256 `3+fMEJhQ8enneLH30XiiV5VYEC4kk0+hZl0SFFsyM4k=`, LastModified 2026-10-15T15:34:08Z. Over the downloaded zip (635,697 bytes) this seat recomputes base64(sha256) = `3+fMEJhQ8...`, the IB-pr-564 candidate verified in v109. Member by member against the BUILD INPUT (rule 22a), all **106 of 106 members equal** their build input: 94 via `staged_from` at each row's pin, 12 via `source_dir` at HEAD; 0 differ, 0 unmapped. The three ENDPOINT members sit at pin e7bb7e923a (sha256 18aba4f0.../abbdab49.../1052343f..., the signed hashes) and carry `commentary_requested` 3/3/1. `composition_admission.py` equals its HEAD source.

**(2) The ledger is closed, with one caveat on stale views.** `org/critical_paths/change_management/20261015T1526Z_irpt-ycg-commentary-requested-ib579-20261015_deploy_completion.md` reads `CLOSED -- nothing stranded -- closed 20261015T155445Z` (closure commit b8484afc22). Union over **31 live worktrees** (`git -C <wt> ls-tree .open_deploys`): the shared tree carries no marker for the function. **Six worktrees still carry the ib579 marker on their branch HEAD**: wk-irpt-anlreq-152, -172, -173, -174, wk-irpt-dashbd-db2-b260 and wk-IRPT_BCKEND-426. They were cut while the entry was open, and their branches predate the closure commit. One more, wt-base-a4b7, carries `irpt-ycg-catalogue-ultrashort-20261013`, whose entry is CLOSED (2026-10-14T02:39Z). All are stale views of CLOSED entries; no open entry exists for this function. A seat reading its own worktree would see an open deploy until it merges trunk (CLAUDE.md NEVER-2: measure the artifact, close SUPERSEDED).

**(3) The BEFORE record and the rollback bytes, read here.** The apply record's `before` holds the byte reads CTO msg 8364 ruled: `live_zip_commentary_requested` 0/0/0 in the three ENDPOINT members, and the accepted request item sha256 1e07ec8e.... `branch_b_version_id` is `sf9zrBdAUPuzO3qgCpk52_iVf6EFle_C` on `s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-ycharts-generate.zip`. This seat fetched that version (635,191 bytes, 2026-10-14T13:00:24Z): its base64(sha256) is `5TRFZf6Grgd9V9jWBVu2QDPRVbgfWBjsuuw8rtf8hRA=`, the pre-apply live digest, and it holds `commentary_requested` 0/0/0. The rollback bytes are named, present and exact. The current artifact version is wJDd4Tr_... (2026-10-15T15:30:10Z). Record-keeping defect (P2): `lambda-source-map.json`'s deploy fields for this function still read `deployed_code_sha256` 5TRFZf6G..., `last_deployed_at` 2026-10-14T13:06:41Z and `deploy_ledger` irpt-ycg-r29-20261014, while `artifact_sha256` reads the new 3+fMEJhQ8.... The recorder was not re-run after the apply.

**(4) What the round proves, and what it does not.** PROVEN (measured, on the deployed function): the live bytes are the signed candidate, member by member; the three ENDPOINT members admit the optional `commentary_requested` member; release 29's members are unmoved (v109); the import census answers `failed: {}`; one already-accepted request reads back unchanged (item hash); the rollback bytes exist. NOT PROVEN: that the released function ACCEPTS a submission end to end (acceptance, copying the member, the queue send). That is shown only at the pin and by the member diff, never by an exercise of the deployed function. Its claim class is **UNEXERCISED** (ABSENT, not EXERCISED-AGAINST) until the FWD-1 run on the DEV build (IRPT_ANLREQ `~Y2`, `~AQ2`). This adjudication does NOT grade that behaviour PASS. It is held on `D2-S204` (ARMED, owner `2.0.0_SA_COO~P2`).

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S31",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T16:05:00Z",
  "one_line": "Round 1 ~PI (WORLD). irpt-ycharts-generate live CodeSha256 3+fMEJhQ8 recomputed from the downloaded zip; 106 of 106 members equal their build input (94 staged at pins, 12 source_dir at HEAD); ENDPOINT members at the signed pin e7bb7e923a with commentary_requested 3/3/1. Ledger irpt-ycg-commentary-requested-ib579-20261015 CLOSED; 31 worktrees read, six carry a stale ib579 marker on pre-closure branches, none open. BEFORE record (byte reads, msg 8364) present; Branch B version sf9zrBdA fetched, hashes to the pre-apply 5TRFZf6G with 0/0/0. Proven: the bytes. NOT proven: that the deployed function accepts a submission; claim class UNEXERCISED until the DEV FWD-1 run, held on D2-S204 (ARMED, ~P2), not graded PASS. P2: the source-map deploy fields are stale (deployed_code_sha256 still 5TRFZf6G). IB217-1-AC1..AC3 PASS.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~P2",
  "adjudicates": [
   "IRPT_BCKEND-D2-S204"
  ],
  "spec_asserts": "CLAUDE.md rule 22a (deployed bytes against the build input); NEVER-2 (an open entry is measured against the artifact; read every live worktree); rule 22 annex (ABSENT != EXERCISED-AGAINST); CTO msg 8364 (the BEFORE record by byte reads).",
  "world_is": "The commentary_requested release is live as bytes and reversible to named bytes. Its behaviour on the deployed function is unexercised; the DEV FWD-1 run exercises it. Six worker worktrees show the closed ledger as open until they merge trunk.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T16:0xZ of the invocations in IB-pr-579: IB217-1-AC1..3 PASS, exit 0; round-close-check ~PI round 1 MAY-CLOSE",
    "aws lambda get-function-configuration irpt-ycharts-generate: LastModified 2026-10-15T15:34:08Z, CodeSha256 3+fMEJhQ8...; get-function zip 635,697 bytes, base64(sha256) recomputed equal",
    "scratch members.py: 106 members, 106 equal to build input (lambda-source-map.json staged_from pins / source_dir at HEAD), 0 differ, 0 unmapped",
    "s3api head-object/get-object opal-313476888478-lambda-artifacts investor-reporting/irpt-ycharts-generate.zip version sf9zrBdA... (2026-10-14T13:00:24Z, 635,191 bytes): base64(sha256) 5TRFZf6G...; commentary_requested 0/0/0",
    "org/critical_paths/change_management/20261015T1526Z_irpt-ycg-commentary-requested-ib579-20261015_deploy_completion.md: CLOSED 20261015T155445Z",
    "git worktree list --porcelain (31) + ls-tree .open_deploys: six branch HEADs carry irpt-ycg-commentary-requested-ib579-20261015.json; wt-base-a4b7 carries irpt-ycg-catalogue-ultrashort-20261013 (CLOSED)",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IB217-1_apply_record.json: before, branch_b_version_id, after, unexercised_live",
    "infra/aws/lambda/ci/lambda-source-map.json irpt-ycharts-generate: artifact_sha256 3+fM, deployed_code_sha256 5TRFZf6G, last_deployed_at 2026-10-14T13:06:41Z",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_1_PI_DRAIN_END_20261015.md @aadbb13fde (msg 8439)"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Held, not dismissed: D2-S204's hazard (the deployed function's acceptance is unexercised) disarms only on the DEV FWD-1 run, by its owner. The bytes, the ledger and the rollback are verified here."
 }
]
```
