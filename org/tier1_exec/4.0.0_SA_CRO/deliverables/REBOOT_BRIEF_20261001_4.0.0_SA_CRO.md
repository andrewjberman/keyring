# Reboot brief -- 4.0.0_SA_CRO -- 2026-10-01

Written 16:3xZ at a checkpoint: nothing in flight, everything committed and merged to the local trunk (CLOUD 1ebe646296).
Order: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_161xZ_DEVICE_SLOW_REBOOT_BRIEFS_AND_RESPAWN.md`.

## 1. Identity
- Serial `4.0.0_SA_CRO` (base, no lane). Folder `org/tier1_exec/4.0.0_SA_CRO/`.
- Project: MDPF_TAXSMA (Tax SMA through MDPF), as the FAST lease's seat. Lease `MDPF_TAXSMA`, seat 4.0.0_SA_CRO, runs to
  16:58Z and then lapses to FULL by itself; its surface is NAMED FILES (taxsma_*.py, the consolidator, aum-metrics, the
  timeseries spine, the category registry, `data/mdpf/tests/taxsma`, the two functions' folders, the two Terraform roots,
  three portal files, the project folder, the contract). Re-arming it needs Andrew's word.
- Also this seat's act: the `mdpf-gold-lambda` deploy for MDPF_HEALGAP's Cottonwood catch-up (CTO msg 103714).

## 2. Where the work stands
- **MDPF_TAXSMA:** Tax is built and deployed in both functions with Tax DISABLED (Gold at pin 8ade880fad since 15:00Z,
  publisher at e8994f23af, switch OFF). Nothing serves Tax. Status file: `org/missions/D8/MDPF/MDPF_TAXSMA/STATUS.md`
  (last @58022874f3). Waits on ANDREW: who runs the Gateway deploy (site Z declined at 04:00Z; annex rule 26a keeps it
  at site Z), the opalbloomberg sign-in, and PROD promotion. The never-widen request for activation is written
  (`deliverables/4.0.0_SA_CRO/NEVER_WIDEN_REQUEST_TX-r-3.md`) and not yet sent.
- **MDPF_HEALGAP hookup:** deployed 15:00Z (packet signed by the CTO, four conditions). Global's fold was rehearsed
  offline on the five restored points: passes, nothing moves outside the five dates
  (`org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/4.0.0_SA_CRO/HEALGAP_GLOBAL_FOLD_REHEARSAL_20261001.md` @6bb8492d23).

## 3. Open acts that must survive the reboot
- **Ledger `mdpf-gold-healgap-hookup-20261001`** (`org/critical_paths/change_management/20261001T1448Z_mdpf-gold-healgap-hookup-20261001_deploy_completion.md`):
  U1, P1, D1, V1 closed; **V2 open**. SAFE to hold over a reboot: the apply is complete and verified, no act is half-
  landed, and V2 is a read of a scheduled run that happens with or without this seat. Window 26 hours (ends ~2026-10-02 16:48Z).
- **Clock to read: 2026-10-02 13:30Z**, the Gold function's scheduled run (first with the catch-up). Read the manifest
  and the four staged spines. PASS = every scope green, the Cottonwood family report has a `catchup` block, served
  changes only on 2026-08-18, 08-20, 08-21, 09-23, 09-24 (Cottonwood and Global). ANYTHING ELSE = SAME-DAY ROLLBACK
  (CTO condition 3): `2.0.0_SA_COO~M` restores the five objects first (its ledger `healgap-cottonwood-catchup-m-20261001`),
  then this seat copies S3 version `U4JsC9gYCgaKgm8kRbF1dL.2JgIPESxk` back onto
  `s3://opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip` with its content-sha256, sets `MDPF_GOLD_COMMIT`
  back to e8994f23af in `infra/aws/terraform/mdpf-pipeline/gold-lambda.tf`, plans and `safe-apply`s.
  Publisher run 13:50Z the same day.
- **Worktree `C:/Users/AndrewBerman/Desktop/wk-taxsma-cro`** (branch `wk-mdpf_taxsma-cro`, head 6bb8492d23): clean, merged.
- **Worktree `C:/Users/AndrewBerman/Desktop/wt-cro-t-transcripts`** (branch `cro-t-transcripts`, head 7e31cce92f,
  2026-09-29, lane `4.0.0_SA_CRO~T`): NOT this session's. It holds one staged `.terraform.lock.hcl` and one untracked
  `main.tf` under `infra/aws/terraform/transcripts/`, and its head is not in CLOUD. Left as found; it is `~T`'s.

## 4. Owed
- By this seat: leg V2 above (to `1.0.0_SA_CTO` and `2.0.0_SA_COO~M`, msgs 103714, 103738, 103721); the V2 probe's two
  false assertions restated before the next release's V2 (CTO batch 91 item 3, msg 103797).
- To this seat: Andrew's word on the Gateway deploy's owner (open since 04:00Z, relay 103435).
- Signed halves outstanding: none waiting on others for an act in hand.

## 5. Relaunch
- RESPAWN: yes. One ledger leg (V2) must be read on 2026-10-02 at 13:30Z, with a same-day rollback if it fails.
- First three acts: (1) `/watcher`; (2) read this brief and MDPF_TAXSMA's STATUS.md; (3) read the function's
  configuration (expected CodeSha256 `eZ6Rtm+2XOKm4UFWgdYhFpNYxCjiKDVtRONV6Ewt21s=`, environment `MDPF_GOLD_COMMIT`
  8ade880fad only) and wait for 13:30Z.
- `--say` hint: "Read org/tier1_exec/4.0.0_SA_CRO/deliverables/REBOOT_BRIEF_20261001_4.0.0_SA_CRO.md, then your inbox."

## 6. Not done and not known
- The catch-up itself has run on no live path yet (dry runs return before it); its first real run is V2.
- An offline fold of the three staged firm artifacts differs from the staged Global by two paths at the 2026-09-30
  frontier; cause not established (rehearsal record, "What the rehearsal does not cover").
- The EC2 daily runner sent no metric on 09-28 to 09-30 (row MDPF_TAXSMA-S14); not read further.
- Push state: everything after origin/CLOUD 0abf99fcd4 is LOCAL (ls-remote 16:29Z), including the Terraform pin of
  the applied Gold deploy (@dae8267e31). The push is `0.0.0_AB_MSTR`'s on Andrew's word.
