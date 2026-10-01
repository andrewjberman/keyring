# Reboot brief -- 2.0.0_SA_COO~Y -- 2026-10-01

Order: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_161xZ_DEVICE_SLOW_REBOOT_BRIEFS_AND_RESPAWN.md`
@223a35bb6b. Written ~16:3xZ. All commits LOCAL; origin/CLOUD `0abf99fcd4` (ls-remote read 16:32Z).

## 1. Identity

- Serial `2.0.0_SA_COO~Y`, base folder `org/tier1_exec/2.0.0_SA_COO~Y/`; lane deliverables
  `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/`. Project IRPT_BCKEND (D9), workstream ~Y (Analysis / YCharts).
- FAST lease `IRPT_BCKEND~Y` until 2026-10-01T19:52:30Z (`python .tools/drive-mode.py read IRPT_BCKEND~Y`). Loop:
  `/canonical-drive IRPT_BCKEND` every 10 min (LIVE_ARMS RELAUNCH row). Status file:
  `org/missions/D9/IRPT/IRPT_BCKEND/STATUS~Y.md` (@d65b5ed483, as of 15:5xZ; this brief is newer).

## 2. Where the work stands

- IRPT_BCKEND ~Y: the Analysis thread is LIVE (CTO rulings batch 88, 13:13Z). The round enriches in the CTO's order E1
  (withdrawn), E2 (withdrawn, batch 97), E3 (done), E4 (`2.0.0_SA_COO~D`'s), E5, E6.
- E3: Multi-Comp `REQ-a1d9abc0bc037ea3d9e4a7ed` READY 15:36Z, outcome
  `IRPT_MVP_Y/E3_MULTICOMP/OUTCOME_E3_MULTICOMP_20261001.md` @be3dfa1d47; the CVO graded PASS (103899); walked 16:29Z;
  NOT live until E7 (batch 98). The Overview stays live.
- Served resident: root `/opt/irpt-resident/481166a8f2-st9` since 14:59:17Z on EC2 `i-0167fd745ad906a66`; rollback root
  `9ac9b56d3c-st8` kept on the host. It does not depend on this laptop.
- On CLOUD, not served (the next resident build's members): item 15 `392149291372` (merge `fba4b93df2`): the
  calculating release back to the receive's 900 s (batch 97 item 4) and the journal line
  `IRPT_RESIDENT_WAF_READ header=<token>` (batch 97 item 5); item 16 `7122afefc1` (merge `e6ae03865b`): row S253, the
  job row's append-only `vendor_requests` ledger. Tests at the branch tip: generate 333 passed, 30 skipped; session
  111 passed, 1 skipped; offline suite rc 0.
- Next act: the st10 never-widen packet for items 15 and 16 (same release pattern as `IRPT_MVP_Y/ST9/`), then E6.

## 3. Open acts that must survive the reboot

- Ledger entries this seat holds open in `org/critical_paths/.open_deploys/`: NONE. Every one of today's is closed
  (last two: `irpt-resident-st9-20261001` @e5a8cab669, `irpt-e3-multicomp-20261001` @be3dfa1d47). The worktree's
  HEAD tree holds none either (read by `git ls-tree`).
- Worktree `C:/Users/AndrewBerman/Desktop/coo-y-r30`, branch `coo-y-r30`, head `7122afefc1`, 0 uncommitted files,
  merged into CLOUD. Do not remove worktree `wk-nfra-oplgtw-og-v-4-p1` (not this seat's).
- Queues `irpt-generation` and `irpt-generation-dlq` 0/0 after the last job; no job is in flight.
- Clocks: none scheduled for this lane. The stored YCharts session is the 08:21:20Z version, read LIVE at 15:15Z.

## 4. Owed

- This seat owes: nothing asked and unanswered. TO-IB-yr-271 (asked by 103899) is closed in this brief's commit as
  SUPERSEDED with an issuer amendment.
- Owed to this seat: nothing. `2.0.0_SA_COO~D` walked `REQ-a1d9abc0bc037ea3d9e4a7ed` at 16:29Z (103910): Ready,
  100 of 100 sections, neither comparison named; the CTO ruled the arm not live until E7 (103913).
- Signed halves outstanding: none. The st10 packet is not yet written.

## 5. Relaunch

- RESPAWN: yes. The lease runs to 19:52Z, two built items wait on one release, and E7 is ordered.
- First three acts: (1) read this brief, `STATUS~Y.md` and the inbox (`check-inbox 2.0.0_SA_COO~Y`), ack every
  message; (2) re-arm the inbox watcher and the 10-minute drive; (3) **E7 first** (CTO rulings batch 98 items 1-3
  @29a6581479, msg 103913): the Multi-Comp arm is NOT live until a served route names the chosen comparisons --
  serve their names from the request's frozen keys and the catalogue's labels, never read back from the PDF; then
  `2.0.0_SA_COO~D` shows them and re-walks, and the CTO calls the arm live. E7 runs ahead of E5 and E6. The st10
  packet for items 15 and 16 follows (build, gate against the running st9 tar, upload to new keys, packet + ledger,
  COO half, ask the CTO half).
- `--say` hint: "Read org/tier1_exec/2.0.0_SA_COO~Y/deliverables/REBOOT_BRIEF_20261001_2.0.0_SA_COO_Y.md, then
  org/missions/D9/IRPT/IRPT_BCKEND/STATUS~Y.md, then your inbox."

## 6. Not done and not known

- E6 (batch 93 item 8): the status list's 15.7 s and a status read's 2.3 to 13.6 s, timed by hop before any
  change. Not started.
- Row S230 (the resident's own sign-in fails `AUTH_FAILED`): read its reason token at the next natural failure; no
  session is displaced on purpose.
- Why the vendor challenges the request after a job's first receive: not read. Item 15's journal line names the
  header's action at the next challenge; that read comes before any shorter release is proposed.
- Item 16's ledger has run only offline; its first live read is the first job on st10.
