# NFRA_CTLPLN -- ROUND-17 ANALYSIS (1.0.0_SA_CTO, 2026-10-15 ~09:4xZ)

**On:**
- the issuer's drain end `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND17.md` @24e899265f (2 of 2 complete, MAY-CLOSE);
- the CVO's L10 slug `surprise-channel/adjudications/ADJUDICATION_v22.md` @b591dedbc5, with its watermark fix @aaf0da8375. All
  criteria were re-run there; W100-S1 is DISARMED.

**PRD:** unchanged.

## 1. What round 17 moved

- **Preserve-then-remove is real** (CT-ag-1). A real `worktree_gc --go --only` on the real repository preserved a dirty
  merged worktree to `1e32e8229a`, the planted file reads back from it, and both verbs agree. W100-S1 and W100-S2 are closed.
  This is the last piece of the ctlpln-97 lesson.
- **The sparse worker checkout is real** (CT-ag-2). A real cell ran green at 0.02 of a full checkout's size. The laptop disk
  pressure that pushed C: down to 6G twice is now answered at the source.

## 2. Rulings

1. **W103-S1:** the sparse set always includes what `safe-commit.sh` needs: `org/modules/graph/`, `org/devices/`,
   `infra/logic/registry/` and `.tools/`. Proof: `safe-commit.sh` runs green inside a worktree cut by `wk-provision.sh`. The
   packet names this as not measured.
2. **S9126:** `worktree_gc.py` normalizes `--only` to a resolved path before its in-use match. It fails safe today (SKIP IN
   USE), so it is a small fix.
3. **The preserve step and links:** a junction or symlink in a worktree is preserved as the link, not followed. This could not
   be tested here (WinError 1314), so it is stated in the code comment and the test is skipped with that reason.
4. **The plain `--go` (without `--only`) on the real repository is NOT run as a test.** It is the drain's ordinary use and runs
   at the next drain under the new rules.

## 3. ENRICHMENT LIST for round 18 (one issuance)

1. One batch:
   - the W103-S1 sparse set, plus `safe-commit` green inside a `wk-provision.sh` worktree;
   - the S9126 path normalization;
   - the link note.
2. Carried, with owners as before: S9125 (dell1), S9119, S9103, S9120, S9122, Z-S3, W12-S1, W89-S3.

**Standing note:** NFRA_CTLPLN's rounds are now small hygiene batches. FWD-11 waits on Andrew (call `7841`) and FWD-9 is
parked. Once round 18 drains, the project's remaining outcomes need either his restart hour or a lease that does not exist
yet. Before round 19, this seat reads whether the project should close what it has or park, and puts that to Andrew if so.
