# NFRA_CTLPLN -- ROUND-29 ANALYSIS (1.0.0_SA_CTO, 2026-10-16 ~16:1xZ)

**On:**
- the issuer's `ROUND29_INPUTS_FOR_ROUND_ANALYSIS.md` and `L8_PACKET_ROUND29.md` @1f141a032b (msg 109701);
- the CVO's `ADJUDICATION_v33.md` @27da2ba104 (msg 109720).

**PRD:** v0.31 (ADMITTED).

## 1. FWD coverage (CVO v33)

| grade | count | FWDs |
|---|---|---|
| REALIZED | 13 | 1, 3, 5, 8, 15, 16, 17, 18, 19, 23, 24, 25, 28 |
| ADVANCED | 11 | 2, 4, 6, 7, 10, 11, 12, 14, 21, 22, 27 |
| PARKED | 1 | 9 |
| MOVED | 3 | 13, 20, 26 |

- New this round: FWD-8, and FWD-25.
- **FWD-8:** two boxes each ran a full round in parallel, and box-sync read 74 merges with 0 conflicts. The crossbox call file
  now has one writer per box.
- **FWD-25:** all eight seat kinds were started and asked what they are. The 60 forbidden-act probes all PASS.

## 2. Rulings

1. **Source-map stage 2: ONE atomic cell, with no separate step-0 commit.** The issuer's item 1 (a). C-S102 is disarmed by this
   cell.
   - **What the cell does:**
     - re-runs the consumer census AT ITS CUT and requires `other=0 ok=True`. C-S102: a dell2 reader,
       `IRPT_DASHBD .../r149/p170_filled_reader.py:32`, landed after the round-29 census, and any reader the re-run names joins
       the atomic set;
     - generates the 240 function files from the map at its merge base and checks them in the cell (240 of 240 equal, count 240);
     - switches every atomic-set member in the proposal's section (d);
     - makes the four silent readers fail loud;
     - retires `battery_ib_rtf_1.py`;
     - deletes the map.
     All of this is ONE commit, so a half-split tree is never merged and no deploy freeze is needed.
   - **The drain** re-checks that the map is byte-unchanged since the cell's base. A Lambda deploy merged mid-cell means the
     cell regenerates before it merges.
   - **The check:** `terraform plan` on the three `locals.tf` roots reads 0 resource diffs. Never an apply.
   - **The census script writes its tracked markdown when it runs** (C-S102 world_is). The cell gives it a read-only mode, or
     writes to the cell's deliverables folder, so that a census read no longer dirties the tree.
2. **`_last_deploy_recorded` is DROPPED** (item 1 (b)). The deploy ledger under `org/critical_paths/change_management/` is the
   record of deploys. The writers of W140-S5 change in the same cell.
3. **`.owned-paths.yaml`** (item 1 (c)). The atomic cell's `<paths>` names it for exactly two lines:
   - the map's grant line becomes the `function-map/` folder, or the grant lapses;
   - `record-terraform-deploy.sh` belongs to `0.7.0_AE_CloudOps` alone (round-28 ruling 2).

   **BLIND** (a reader outside the repository) is accepted. The first real Lambda deploy after the merge is the live proof, and
   the issuer reads it.
4. **Sweep-before-merge: YES, into the L6 order template** (item 3). Any change to a shared checker or gate runs over every real
   project's records before it merges, and the order prints the counts before and after.
   - COST: one run per such cell.
   - NON-APPLICATION: a checker that no other project's records feed.
5. **W143-S1: the CVO's ruling C-S103 stands** (item 4). A NOT MET grade does not refuse a ROUND close; it feeds this analysis.
   The ROUND-CLOSE line prints `not_met=<n>` beside `graded=`, as one small cell.
6. **FWD-11: the choice was made in round 27 ruling 1, restated in round 28 ruling 5, and C-S105 still reads "waits on the CTO's
   choice".**
   - The CVO grades FWD-11 THIS round on the record of the laptop's overnight reboot of 2026-10-16. That reboot happened with
     round 24 in flight, recorded in the header paragraph of `L8_PACKET_ROUND24.md` @52567a1a41.
   - The grade is read against the DONE WHEN ("one box restarted mid-round, and the round finished").
   - No act by any seat is owed before that read. Only a grade of NOT MET leads to a deliberate reboot, and that waits on
     Andrew's word that his 10-14 hold is spent.
7. **Item 6 (smaller):**
   - W139-S4's stale comment rides the next cell that touches `mstr-ledger-check.sh`.
   - The Dell-deny rows' wording, "what the policy FILE holds", is accepted.
   - `placement-check.py`'s denominator line is done.
   - Arm (f) of `test_round29_crossbox_split.py` compares `crossbox/1` files only (C-S104), as one line in the small cell.
8. **CVO reads, unchanged:** FWD-4, FWD-12, FWD-22.

## 3. ENRICHMENT LIST for round 30 (one issuance)

1. Source-map stage 2: the one atomic cell (rulings 1-3), with the census re-run at the cut and a read-only census.
2. The follow-on readers that may come after the cut: proposal section (d), the "can follow" list.
3. The L6 order template gains the sweep-before-merge clause (ruling 4).
4. The small cell: `not_met=<n>` on the ROUND-CLOSE line, and the crossbox test arm (f) (rulings 5 and 7).
5. CVO: FWD-11 (ruling 6), FWD-4, FWD-12, FWD-22.
6. **Held for a later round** (unchanged): FWD-10 and FWD-21(a). Each needs its box CTO's word and a quiet window.
7. **Acts only Andrew can do:**
   - FWD-2: a real new machine;
   - FWD-6: a client-facing PROD push held until his word;
   - FWD-14 (`b87f`): the remote-desktop sessions from the laptop;
   - FWD-27: logins from rc and muse, and from off the tailnet.
