# Post-crash residue + worktree assessment -- NFRA_OPALAI, NFRA_MCPORTAL, cto_o_tflocal (1.0.0_SA_CTO~O)

**Order:** `org/tier0_exec/0.0.0_AB_MSTR~Z/deliverables/ANDREW_DIRECT_20260929_1755Z_POST_CRASH_RESIDUE_CLEANUP_AND_WORKTREE_ASSESSMENT.md`.
**Why this seat:** NFRA_OPALAI's COO (2.0.0_SA_COO~AI) and NFRA_MCPORTAL's COO (2.0.0_SA_COO~MP) were idle at the crash
and were not respawned. NFRA_OPLGTW (2.0.0_SA_COO~O) and NFRA_MCPINDEX (2.0.0_SA_COO~MI) filed their own assessments;
3.0.0_SA_CVO~O concurred with both (msg 26642, `POST_CRASH_RESIDUE_AND_WORKTREE_ASSESSMENT_CVO_O_20260929.md` @efa01d4120).
**Measured:** 2026-09-29 18:0x-18:4xZ, site Z. Inventory cross-read: 1.0.0_SA_CTO~Z `POSTCRASH_WORKTREE_INVENTORY_20260929_1400ET.json` @626d53db16.

## 1. Residue -- one real loose end, and it predates the crash

The crash left no residue in these two projects. The loose end found is older: two drain merges dropped their workers'
files. Row `NFRA_OPALAI-Z-S45` has the evidence.

| drain | order | files dropped | still missing at CLOUD HEAD |
|---|---|---|---|
| d45ab2cf53 (09-28 23:45 ET, 2.0.0_SA_COO~AI) | OA-e-3 asker switch-on | 9 of 9 | 8 (EC2_MANIFEST.json legitimately moved on to 093fc247c6) |
| 33076ebc84 (09-28 18:56 ET, 2.0.0_SA_COO~AI) | OA-f-3 provision description | 3 of 3 | 2 (the TO flip was restored later) |

- Denominator: 167 first-parent CLOUD merges since 2026-09-26; 5 carry such drops; the other 3 (2.0.0_SA_COO~D x2,
  2.0.0_SA_COO~MI x1) are already restored or superseded.
- The shared tree holds all 10 missing files at the exact branch-parent blobs (10 of 10). Tests on the CLOUD tree with
  them in place: 14 passed.
- A direct commit by this seat was REFUSED by the lane gate (`infra/aws/**` = CLOUD_OPS_OR_ETL;
  `deliverables/<serial>/**` = that serial only). The write is a DRAIN: a branch off CLOUD that cherry-picks the
  workers' original commits (author kept), merged with `.tools/safe-merge.sh`. Owner: 2.0.0_SA_COO~AI, spawn asked of
  0.0.0_AB_MSTR~Z.
- Re-drain source commits (exclude `infra/aws/ec2/EC2_MANIFEST.json`):
  OA-e-3 = the non-merge commits in `$(git merge-base d45ab2cf53^1 d45ab2cf53^2)..d45ab2cf53^2`, i.e. c06a3a4379,
  685fabc691, a01c3bd4d1 and the worker's proof/record commits;
  OA-f-3 = fd4103a5fe (proof + session_log).
  Acceptance: for each of the 10 paths, `git rev-parse CLOUD:<path>` == `git rev-parse <branch-parent>:<path>`.

## 2. Worktrees -- 10 checkouts, 1 KEEP, 9 DISPOSE (amended), every branch KEPT

Columns measured per worktree: patch-unique commits vs CLOUD (`git cherry`), tracked and untracked dirt.

| worktree | branch | unique | dirt | disposition |
|---|---|---|---|---|
| C:/tmp/oa-10 | wk-NFRA_OPALAI-10 | 0 | audit.jsonl (test by-product), portal gitlink, .scratch/ | DISPOSE checkout; branch KEPT (re-drain source) |
| C:/tmp/oa-15 | wk-NFRA_OPALAI-15 | 0 | opal_ai + portal gitlinks, .scratch/, .scratch_msg1/2 | DISPOSE checkout after the scratch is archived |
| C:/tmp/oa-10-rb2 | rb-nfra-opalai-r2-asker-binding-base-v2 | 1 (release lineage) | mcportal gitlink | DISPOSE checkout; branch KEPT |
| C:/tmp/oa-10-rel | rel-nfra-opalai-r2-asker-binding-gateway | 8 (release lineage) | mcportal/ untracked | DISPOSE checkout; branch KEPT |
| C:/tmp/oa-10-rel2 | rel-nfra-opalai-r2-asker-binding-gateway-v2 | 2 (release lineage) | mcportal gitlink | DISPOSE checkout; branch KEPT |
| C:/tmp/oa-10-sw-rb2 | rb-nfra-opalai-r2-asker-switch-on-base-v2 | 1 (release lineage) | mcportal gitlink | DISPOSE checkout; branch KEPT |
| C:/tmp/oa-10-sw-rel | rel-nfra-opalai-r2-asker-switch-on-gateway | 11 (release lineage) | none | DISPOSE checkout; branch KEPT |
| C:/tmp/oa-10-sw-rel2 | rel-nfra-opalai-r2-asker-switch-on-gateway-v2 | 2 (release lineage) | mcportal gitlink | DISPOSE checkout; branch KEPT |
| C:/tmp/mp3-1 | wk-NFRA_MCPORTAL-1 | 0 | portal gitlink, .scratch/, two lambda .build/ dirs | **KEEP until NFRA_OPLGTW OG-n-1 closes** (amended 19:3xZ, see below) |
| C:/Users/Opal Bloomberg/Desktop/cto_o_tflocal | cto-o-tflocal | 0 | .tools/naming-gate.py, byte-identical to CLOUD (landed 7610be987f) | DISPOSE checkout |

- Release-lineage "unique" commits are gateway releases built on the LIVE base by design, never merged to CLOUD. The
  branches stay while 093fc247c6 is the live gateway (3.0.0_SA_CVO~O's condition on both COO tables, msg 26642).
- Every DISPOSE removes a checkout only; nothing unique lives in any of them. The disposal is a recursive directory
  delete, so it runs on Andrew's word, as MSTR~Z's 71-checkout pass did. `.scratch/` is archived first, to
  `.runtime/crash-investigation-20260929/wt-scratch-archive/`.
- **AMENDMENT 2026-09-29 19:3xZ (2.0.0_SA_COO~O msg 26674):** mp3-1 moves to KEEP. It holds the only copy of
  `infra/aws/lambda/layers/mcportal-grant-writer-deps/.build/mcportal-grant-writer-deps.zip` (5,016,850 B, built
  09-28 23:57 ET by MP-a-2), which NFRA_OPLGTW OG-n-1 must copy from the tree that built it and may never rebuild
  (TO-OG-n-1 section 1 item 2). This seat measured it: the zip is present in 1 of 49 linked worktrees, mp3-1. The
  table is now 1 KEEP / 9 DISPOSE, and the removal set put to Andrew is 32.
- KEEP otherwise: none. NFRA_OPALAI's next work (the re-drain) cuts a fresh branch off CLOUD, and NFRA_MCPORTAL's two open
  orders wait on Andrew's acts (G-2ND sign-in, G-CLOSE run), with no checkout in use.
