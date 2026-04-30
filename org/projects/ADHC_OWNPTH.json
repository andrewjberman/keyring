{
  "project_code": "ADHC_OWNPTH",
  "macro_code": "ADHC",
  "name": "Owned-Paths Pre-Commit Hook (Git-Sweep Prevention)",
  "description": "Structural prevention of cross-lane git-sweep incidents via a pre-commit hook that reads a workspace-wide path->permitted-agent YAML and blocks commits whose --author falls outside the permitted set for any touched path. Addresses 4 observed sweep incidents (7ae0ef6b / c6285ae8 / 2b3bfcd4 / 2026-04-24 AE 0.7 triplet abfed84d/71be8a7e/e11151d5) where existing cultural guardrails (--only pathspec, selective staging, worktree separation, memory feedback) were all in force and still failed. Andrew directive 2026-04-22: 'this keeps happening — propose owned-paths pre-commit hook, not more rules.' Andrew decision 2026-04-24: Option B (PRD + phased ship): register as project, Phase 1 YAML+hook fail-open warn with 1-week observation window, Phase 2 flip fail-closed. Draft base exists at org/tier1_exec/1.1.0_SA_CTO/drafts/owned_paths_comp_learns_half.yaml (232 lines covering COMP_LEARNS lane).",
  "prds": [
    {"path": "docs/architecture/ADHC_OWNPTH.md", "label": "Owned-Paths Hook PRD v1", "date": "2026-04-24"}
  ],
  "status": "active",
  "phase": "**PHASE 2 LIVE 2026-04-30 — fail-closed.** TO 1 COMPLETE (`bbf990dc` CTO). TO 2 COMPLETE (`9ade031f`+`37a721b0` DS). TO 3 COMPLETE (`74b0f77f`+`f4a8da98` AE 0.7). TO 4 TRUNCATED 2026-04-30 (Andrew direct override — observe week truncated by ~24h; sufficient evidence: TO 8 closed 4th post-wrapper sweep, zero sweeps in ~36h since). **TO 5 COMPLETE 2026-04-30** (1.0.0_SA_CTO `{{TO5_COMMIT}}`: rollout_phase 1→2 + .tools/git-hooks/owned-paths-check.sh MODE default warn→block + 8 new lane definitions (POD*_OR_EXEC, SHARED_*_OR_EXEC, ANY_EXEC_OR_AE) + 11 new path overrides (task_orders/*.md exceptions) + 5 widened existing rules (REGISTRY.md/projects.json/git-hooks/owned-paths.yaml/portal-pointer); canary 2-test PASS at 12:45Z UTC). TO 6 COMPLETE 2026-04-27 (`15276118`+`3a0a9b19` — commit-discipline package). TO 7 COMPLETE 2026-04-27 21:27Z (`1998340f` AE 0.7 — safe-commit.sh wrapper, 14/14 canary PASS). TO 8 COMPLETE 2026-04-29 (`aa004108b` AE 0.7 — record-terraform-deploy.sh migration to safe-commit.sh, closes 4th-sweep-incident door). TO 9 STAGED-LOW (AE 0.7 — tilde-form alias fix; not blocking). 8 of 9 TOs COMPLETE; TO 9 carries forward.",
  "blocking": "None — fail-closed enforcement live. 48h follow-up scan due 2026-05-02: audit `org/git-author-override-audit.log` for BLOCK events, triage real violations vs YAML gaps, surface gaps as YAML diffs immediately (do NOT auto-revert without Andrew directive). TO 9 (tilde-form alias fix) standing-low.",
  "created": "2026-04-24",
  "pods": ["0.4", "0.7"],
  "pipeline": "repo-tooling",
  "thread_counter": 0,
  "threads": []
}
