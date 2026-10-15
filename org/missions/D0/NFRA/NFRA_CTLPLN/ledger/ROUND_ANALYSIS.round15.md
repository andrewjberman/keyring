# NFRA_CTLPLN -- ROUND-15 ANALYSIS (1.0.0_SA_CTO, 2026-10-15 ~06:0xZ)

**On:**
- the issuer's drain end `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND15.md`;
- its inputs `ROUND15_INPUTS_FOR_ROUND_ANALYSIS.md` (3 of 3 complete);
- the CVO's L10 slug `surprise-channel/adjudications/ADJUDICATION_v20.md` @ee8cdc921e: MAY-CLOSE, 0 graduate, S9118 DISARMED.

**PRD:** unchanged.

## 1. What round 15 moved

- **S9118 remediated and disarmed** (CT-ae-1). The run found a real defect, `W97-S1`: the reaper's seat-boundary refusal was
  unreachable for a seat, because the held-tree guard skipped any tree holding a `claude.exe` first. The fix judges the seat
  boundary first, refuse-only (`21ad9d0ca4`). A planted tree survived a real `kill-maint -Execute`.
- **The inline holiday sets** (CT-ae-2): 6 found, 5 match. `inf-gold-freshness-guard` lacks every 2027 closure. It is routed
  to ADVI_FIRMBKTS (dell1), due before 2026-12-31 (row S9125).
- **The batch** (CT-ae-3): files-mode equality for every row kind; an ENFORCE refusal unstages every in-scope path; the
  census checkpoint is ignored.

## 2. Outcome coverage

**FWD-11** remains a qualified wait on Andrew's word (call `7841`). Nothing else moved.

## 3. Rulings

1. **This seat's error, and the fix (inputs D2).** I ordered `ctlpln-97` removed as "merged" at ~01:5xZ. Its worker had been
   cut off by the spend limit before its first commit, so the branch sat at the issuance commit, which the trunk contains. The
   removal took one uncommitted test file.
   - "Merged" is now defined: the branch carries **at least one commit of its own, and every one is in the trunk**.
   - A branch with no commit of its own is NOT merged; it is unstarted or in progress. A worktree with a dirty
     `git status --porcelain` is never removed.
   - Andrew's standing word (force-remove merged worktrees at each drain) is unchanged; this only states which worktrees it
     covers. `0.0.0_AB_MSTR` applies it from now on. One small cell puts both tests into the drain's cleanup step, so the rule
     is mechanical rather than read.
2. **Worker faces gain two lines** (inputs D2, D3):
   - "commit a work-in-progress commit as soon as a file exists";
   - "copy a proof instance's field names from `<path of an existing VALID instance>`".
3. **W97-S2 (the planted test shape):** accepted as is. The reaper keys on the process image name and the command line, so a
   `cmd.exe` copy named `claude.exe` exercises the same branch a real seat does. If the guard ever keys on a signature, the
   test is re-planted.
4. **The instrument note (CVO):** `round-close-check --round N` counts orders by `<round>`, which holds the workstream round,
   so it read no CT-ae order. One small cell: it reads the issuance round from the decomposition.
5. **The interim "dry-first" rule on `kill-maint`:** whether to lift it is `0.0.0_AB_MSTR`'s, as the CVO says. My view, not
   binding: S9118 disarmed is the condition it waited on.

## 4. ENRICHMENT LIST for round 16 (one issuance)

1. The drain-cleanup "merged" test (ruling 1): an own-commit test plus a clean status before any removal, with a negative
   control on a branch at its issuance commit.
2. `round-close-check` reads the issuance round (ruling 4).
3. One batch: `W99-S1` (the placement-refusal branch unstages all, the twin of W93-S1).

Carried with owners, no cell: S9125 (dell1), S9119 (dell2), S9103, S9120, S9122 (per CVO), Z-S3 and W12-S1 (next deploys),
W89-S3 (ADVI_FIRMBKTS).
