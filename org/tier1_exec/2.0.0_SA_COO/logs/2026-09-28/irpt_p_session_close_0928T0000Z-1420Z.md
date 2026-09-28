# Five served moves under both sign-off halves, each proved on the served bytes -- 2.0.0_SA_COO~P

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE

**Date:** 2026-09-28 (window 00:00Z-14:20Z, including the MSTR freeze gap 03:00Z-12:50Z)
**Task Order:** IRPT_BCKEND~P closer drive (FAST lease, /closer-drive, cron 312e843c)
**Status:** IN PROGRESS. This is the reboot checkpoint (CTO 102345, Andrew-direct): start nothing new.

---

## Objective

Carry IRPT_BCKEND~P's post-freeze queue to served under both never-widen halves:
- S27, the export receipt RUNNING;
- the Comparison GRANT release (generate + resident);
- irpt-status rebuild 3.

Each move gets a live before-read and after-read on the served path. Then checkpoint for the fabric reboot.

---

## Compiler Tools

No comp-tool was run for the tables below. The work was served-artifact verification: live Lambda invokes, get_function
code downloads, SSM, and Terraform plan/apply through safe-apply. The comp-find rail blocked one raw grep over scratch
output files; I re-ran it as a pipe receiver.

| Tool | Command | Result | Note |
|------|---------|--------|------|
| safe-commit gates | surprise-row-gate on S175 | PASS after a fix | the schema refused `summary`; the field is `one_line` |
| deploy_ledger.py | close-leg / close | PASS | three ledgers advanced; the GRANT ledger closed |

**What worked:** the surprise-row gate caught a schema field name at commit time.
**What failed:** none.
**Gap found:** deploy_ledger.py has no `note` verb. Citing gates before an apply meant a hand edit of the ledger's JSON
log.

---

## Work Completed

### 1. S27, the export receipt RUNNING (ledger irpt-export-receipt-running-20260928, D1 closed @dcaac5ac3d)
- irpt-export-render moved `Ulim/gmf` -> `BORQ2shb` at 12:51:49Z.
- The before-read (12:47:24Z) equals the after-read:
  - exr_9f78 -> UNAVAILABLE DEPENDENCY_UNAVAILABLE;
  - an unknown exr_ -> NOT_FOUND.
- Cold start INIT + REPORT f22ece9b. Re-plan 0.
- A1 (the RUNNING branch, live) rides the next K8.

### 2. Comparison GRANT release (ledger irpt-generate-resident-grant-20260928, CLOSED @dcaac5ac3d)
- **D1, irpt-ycharts-generate `ykJltfTd` -> `AdE17rT6`, 13:11:54Z.** Both reads ran ~Y's offline_submit_proof on the
  bytes downloaded from the live function.
  - Before: Comparison and Multi-Comp REFUSED COMPARISON_CATALOGUE_REQUIRED.
  - After: ADMITTED (P:1728413; P:1728415 + P:1728315). Overview unchanged; an unknown key REFUSED.
  - Cold start seen; re-plan 0.
- **D2, resident `fe64236bbb-st` -> `st2`,** via SSM 62358c33, rc 0. Running root read back; 0 tracebacks.
- **Row S175:** the unknown key's public code went NOT_READY -> UNEXPECTED, because MaintainedSourceRefused is unmapped.
  The portal cannot reach it, so I held it rather than rolled back. Parked with 2.0.0_SA_COO~M.

### 3. irpt-status rebuild 3 (ledger irpt-status-dates-rebuild3-20260928, D1 closed @fd9181db1b)
- ~Y's gates 3+4 (@898fda7783) were cited in the ledger @1a0c405ed0 BEFORE the apply, per CTO 102307 and CRO 102327.
- The live before-reads were three direct invokes of the served bMMJ under irpt-status-role:
  - A, the REQ-67 status-dates read: RequestReadRefused DATE_SOURCE_OWNER_BINDING;
  - B, the same read without the header: DATE_BASIS_UNAVAILABLE;
  - C, a bad firm token: FIRM_BINDING.
- safe-apply 0/2/0 at 14:04:55Z. Readback: ZYr+IDMp, and the policy carries 3 original_holdings resources.
- After: A is READY PER_SECTION with 51 section dates; B and C are unchanged. The cold start was clean. Re-plan 0.
- A1 (K10, the page read) waits for the first post-reboot window.

### 4. Rows and routing
- S175 (above).
- S176, NEW-01 (HIGH): an invested 49F account answers YTD -100% (CRO re-walk @f330857833). Filed @4c4bfeacbb; it is
  the first item after the reboot (CTO 102357).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Hold the GRANT release despite the UNEXPECTED code on an unknown key | The refusal was named in ~Y's signed arms; the code is unreachable from the portal (the keys come from the catalogue). A rollback would remove the feature Andrew granted over a label. Row S175 plus a parked remedy. |
| Take generate before/after reads on bytes downloaded from the live function | Those are exactly the served bytes. The Lambda has no read-only composition entry point, and a live POST /analysis would write a submission. |
| Park S175's remedy with ~M instead of patching generate | One exception type carries two causes. `reason_for` forbids message-matching, so the fix is two declared subclasses in ~M's `_scope/maintained_sources.py`. |
| Defer ~Y's first live Comparison window (102340) | CTO 102345 (Andrew-direct): start nothing new before the reboot. |

---

## Blockers

- **Phase B of the reboot sequence:** MSTR's S19 purge CLOSE (102315/102333). Pushes are frozen, and the worktree
  re-sync plus READY-FOR-REBOOT wait on it. Evidence: no CLOSE message in `org/mcp/inbox/2.0.0_SA_COO/~P/read/` as of
  14:18Z.

---

## Current State (zero-context handoff)

- **Served:**

  | Function or host | Version |
  |---|---|
  | irpt-export-render | `BORQ2shb` |
  | irpt-ycharts-generate | `AdE17rT6` (rollback: S3 version Iu3nADja) |
  | resident | `/opt/irpt-resident/fe64236bbb-st2` (st kept) |
  | irpt-status | `ZYr+IDMp` + the original_holdings grant (rollback: 7xPCOM83) |
  | irpt-performance-adapter | `F0bYtOfB` |
  | irpt-directory-search | `o1TXq5PH` |

- **Open ledgers (mine):** irpt-export-receipt-running-20260928 (A1), irpt-status-dates-rebuild3-20260928 (A1),
  irpt-adapter-render-selection-20260927 (A1), irpt-adapter-render-grant-kms-20260927 (A1), and
  irpt-export-async-submit-20260927 (A1). Every A1 is a live walk proof.
- **Worktrees:**
  - backend `irpt-smoke-p-backend-20260923` @75df934b23;
  - publish `irpt-p-publish-20260923` @b4f5492e9e;
  - both carry untracked plan/apply text outputs.
- **Status file:** `org/missions/D9/IRPT/IRPT_BCKEND/STATUS~P.md` @4c4bfeacbb.
- **Push state:** LOCAL (MSTR pushes after CLOSE).

---

## Next Steps

1. Post-reboot, first: trace NEW-01 (row S176) to file:line in the Performance path (adapter F0bYtOfB and the gips
   series). Acceptance: an account with positive holdings never answers -100%.
2. The first live Comparison window (~Y 102340), with K8 (S27 A1, ~D's page pin TO-IV-e-78) and K10 (rebuild 3 A1). It
   takes its own packet and halves.
3. [2.0.0_SA_COO~M]: row S175's remedy (two MaintainedSourceRefused subclasses declaring public_reason_code).
