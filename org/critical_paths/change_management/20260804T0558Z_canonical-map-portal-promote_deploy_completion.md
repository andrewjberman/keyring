# DEPLOY LEDGER: Canonical-map portal DEV->PROD promote (pinned 0576ef22)

**Opened:** 2026-08-04T05:58Z by `0.2.0_DT_PortfolioAnalytics` (at deploy START, per NEVER#6)
**Status:** **CLOSED 2026-08-04T06:27Z** -- all legs complete. Live PROD=2d33ea2c
(portal-v2.1.156, peel-verified), deploy run 30883025692 SUCCESS, pointer corrective b26bbe4e
CONTENT-VERIFIED on origin/CLOUD (`git ls-tree origin/CLOUD portal` == 0576ef22), main portal
tree on DEV, worktree torn down. Step-6 incident documented below + gitlink-clobber gate
candidate RATIFIED by CTO 062647Z (fix shape: refuse on staged-vs-pinned mismatch; seating via
COO; acceptance = incident replayed as a failing control).

## Authorization
- Andrew-direct ~0545Z at the 0.4.0_DE terminal, verbatim committed @c6b19d7f67: *"deploy as soon
  as we're clean and clear on all frontend changes"* -- supersedes the {emitter landed + first
  clock-v3 fire green} sequencing (CTO formal discharge 055142Z; MSTR relay 055244Z).
- COO explicit GO 20260804T055352Z: promote 0576ef22 to PROD NOW; re-scoped conditions
  {frontend clean + gate-run green} both MET in COO's hand.
- Scope pin (COO 052920Z, CTO concurred 053007Z, DE concurred 052926Z): promote head =
  **0576ef22** (tree-identical to reviewed 7d544d27 + CI-parseable SURFACE_ACK). d32f5a52
  (kill-list row 15) is DELIBERATELY unpublished -- next cycle, own review chain. Local DEV
  sits one commit ahead of origin/DEV BY RULING; do not push it in this window.

## The change
- Portal PROD: c6f561b6 (tag portal-v2.1.155) -> merge of origin/DEV @0576ef22.
- Content = 7d544d27 (CANONICAL MAP realized, Andrew voice memo @7a585074e + CI-R6R T2/T3
  participation rendering) -- 0576ef22 is an empty ack-format commit, tree-identical.
- SEV1 surfaces touched (acked): model_portfolios.benchmark + model_portfolios.headline via
  src/pages/ModelPortfolios.tsx; ack audited 20260804T041944Z + CI-parseable on the pushed record.

## Pre-verified (before this ledger opened)
- [x] Typecheck: canonical `tsc -b --noEmit` at exactly 7d544d27 in an ephemeral worktree, true
      rc=0 (0576ef22 tree-identical => carries over). NOTE: skill Step 2's main-tree typecheck is
      DEVIATED-BY-RULING -- the main tree sits at d32f5a52 (held local), so a main-tree run would
      measure the WRONG tree; the artifact-binding checks are the pinned worktree run + the
      VALGATE pre-push tsc on the merged tree at push time.
- [x] CI on 0576ef22 by headSha: Build+Validate run 30880952307 SUCCESS (watched to conclusion) +
      Surface-Check Gate run 30880952383 SUCCESS (empty-range short-circuit DISCLOSED; COO
      adjudicated MET-WITH-DISCLOSURE 054422Z on composed evidence).
- [x] Ack extraction pre-exercised over the ACTUAL promote range origin/PROD..0576ef22 with the
      CI's exact sed: extracts the full reason; changed files = ModelPortfolios.tsx +
      pairedProvenanceRead.ts (expected set).

## Legs
- [x] Step 3: local PROD re-asserted from origin (update-ref -> c6f561b6, 060105Z)
- [x] Step 4: worktree .runtmp/portal-promote-20260804T060105Z; bun install foreground (100.86s);
      merge --no-ff origin/DEV -> **2d33ea2c** (rollback base c6f561b6 in message); parity gate
      `git diff origin/DEV HEAD` EMPTY
- [x] COO ADDENDUM executed ~0604Z: ack extracted from the ACTUAL merge range (CI's exact sed,
      full reason) -> comp-surface-check blocking on the real merged changed files
      (src/pages/ModelPortfolios.tsx + src/lib/pairedProvenanceRead.ts). VERDICT READ: CRITICAL
      model_portfolios.benchmark + model_portfolios.headline named (SEV2 WARN aum/peers;
      severity_resolution -> SEV1), then **`SEV1 ACKNOWLEDGED (SURFACE_ACK='Sovereign
      canonical-map dispatch @7a585074e ...') -- audited. Proceeding.` rc=0** -- the observed
      composition at the last reversible moment. The ~0604Z audit-log entry is THIS hand-check
      (promote-time exercise), not a new authorization. Two ADVISORY contract-layer notes
      (headline UNCONTRACTED pending CVO TO-3; benchmark WATCH noise) -- advisory, on the record.
- [x] PROD push 060x: route (b), audited never-override with MSTR explicit no-objection 060654Z
      on the record (W6 precedent). Pre-push gates PASS live: provenance paired-accessor scan OK,
      VALGATE D-1 PASS, push-time `tsc -b --noEmit` OK on the merged tree. c6f561b6..2d33ea2c.
      (First attempt correctly BLOCKED by the LD-0368 gate -- override was pipe-detached; retried
      with override on the simple command. The gate works.)
- [x] Step 5: `Deploy to Production` run **30883025692** headSha 2d33ea2c CONCLUDED **success**
      (background watch to conclusion, gh run view --json, never watch). Tag **portal-v2.1.156**
      peel-verified: `portal-v2.1.156^{commit}` == 2d33ea2c == origin/PROD head.
- [~] Step 6: INCIDENT + CORRECTIVE. Delegated to MSTR (060654Z offer; 061513Z handoff with both
      hazards mapped). MSTR's 13ac2c307 hit hazard (1) ANYWAY: the cacheinfo pin was silently
      CLOBBERED by safe-commit's pathspec staging (git add on a submodule path records the
      submodule's checked-out HEAD = d32f5a52), so the commit's TREE recorded d32f5a52 while its
      MESSAGE claimed 0576ef22 -- and it was pushed, putting an unresolvable gitlink on
      origin/CLOUD (d32f5a52 exists only on this machine; site-Z submodule updates fail while it
      serves). MSTR's verification read the STAT (1 file, portal only), not the CONTENT --
      read-the-values class, falsified by `git ls-tree 13ac2c307 portal`. CORRECTIVE b26bbe4e7d
      landed on local CLOUD ~0624Z: temp-index + commit-tree + compare-and-swap update-ref
      (race-safe -- CAS base showed CLOUD moved 2 further commits mid-fix), audited
      never-override on the record (safe-commit's staging IS the clobber mechanism; shared index
      held 2 foreign staged items a bare commit would sweep; portal checkout untouchable, DE
      live). Gitlink CONTENT-VERIFIED on the new commit: `160000 commit 0576ef22... portal`.
      MSTR push requested 062511Z; leg closes on content-verified origin/CLOUD read
      (`git ls-tree origin/CLOUD portal` == 0576ef22). GATE CANDIDATE surfaced (CTO to route):
      safe-commit content-check on gitlink pathspecs (declared-pin vs staged-sha mismatch =
      refuse).
- [x] Step 7: worktree deregistered + physical dir deleted (rm -rf after the known long-path
      `worktree remove` error) + prune; `git -C portal worktree list` shows main tree only, ON
      DEV at d32f5a52 (DE's held commit undisturbed); cwd = workspace root.
- [ ] Step 8: RAVC completion report to COO + CTO + MSTR (releases freeze); session log

**Close condition:** all legs checked, artifact table in the Step-8 report, this file flipped to
CLOSED with the completion timestamp. An unclosed ledger at session end = COO alarm (NEVER#6).
