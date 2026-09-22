# AMGT_RESAPP.TO-AMGT-rk-89 -- portal v2.1.182 DEV->PROD promote -- 0.2.0_DT_PortfolioAnalytics, 2026-09-21 23:50Z - 09-22 00:10Z

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

## Summary

Task order `AMGT_RESAPP.TO-AMGT-rk-89` (round 22, issued by `2.0.0_SA_COO~Z` @f7fcf11592, msg 24126, acked
24126 READ) promoted portal DEV `f22e369c` (rk-78 Bloomberg fallback roster render + rk-80 text fixes) to
PROD. PROD `6dfc3390`, tag `portal-v2.1.182`, CI success, served bytes carry 3 of 3 new literals. The access
gate is byte-identical before and after. All 7 criteria PASS. This time the deploy ledger was opened and
committed BEFORE the push (the v2.1.181 defect the order barred).

## Deployment Sequence

1. AC1 (23:52:36Z): DEV `f22e369c`, PROD `07d5af72`; dev_has True, prod_has False, gate commit on PROD
   True; 2 commits (f22e369c rk-80, 95d96edb rk-78); files 8, outside_security_analysis 0; App.tsx diff 0.
2. Step 1: main tree DEV behind 1 -> `git -C portal merge --ff-only origin/DEV` (GATE 5 denies a DT pull;
   row Z-S208). Step 2 typecheck rc=0, 0 error TS.
3. AC2 (23:53:48Z): ledger `amgt-rk89-portal-prod-promote` OPENED (L1, L2). Committed `058d62973d`
   (23:54:44Z) with the sentinel, plus a status-marker fix to my v2.1.181 entry (it read UNINDEXED OPEN).
4. AC3: worktree `.runtmp/portal-promote-20260921T235549Z`, bun install 377 packages; merge `6dfc3390`
   authored/committed by this serial via `-c user.name`; HEAD^2 = `f22e369c` (= AC1); parity 0 lines; push
   `07d5af72..6dfc3390` accepted 23:57:32Z via the space-free relative `git -C` form (row Z-S209).
5. AC4/AC5: tag `portal-v2.1.182` peeled = PROD; App.tsx diff vs 07d5af72 = 0; run 35669878684 Deploy to
   Production completed success, 1 of 1 at the sha of 30 listed; nameWithOwner Opal-Capital/portal.
6. AC6: opalinvest.dev index 200, Last-Modified 23:59:39Z; 53 chunks; 3 of 3 new literals 1/1/1; positive
   control 1.
7. Teardown: worktree remove failed Filename too long, pruned (0 entries), physical dir persists. Gitlink
   95d96edb -> f22e369c committed LOCAL `75de778a8a`. AC7: legs closed, entry CLOSED, sentinel removed;
   main tree DEV, porcelain 0.

## Verification

Byte-for-byte outputs are in the proof-of-spec instance:
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.2.0_DT_PortfolioAnalytics/AMGT_RESAPP.TO-AMGT-rk-89.portal-prod-promote.proof_of_spec.json`.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-to` | set session TO context | PASS |
| `comp-read --enumerate` | `.tools/deploy_ledger.py` status-marker grammar | PASS: found the 3 accepted forms; fixed my v2.1.181 entry |
| `comp-read --enumerate` | `.tools/proof-of-spec-check.py` artifact resolution | PASS: a cross-repo pin counts unresolved, not refused |
| `deploy_ledger.py` | open / close-leg / close | PASS |
| `proof-of-spec-check.py` | grade AC1-AC7 | see instance commit |

- **What worked:** ledger-first sequencing; `-c user.name` on the merge gave a correct author line with no amend.
- **What failed:** `deploy_ledger.py list` exits 1 on other seats' past-window entries, so AC2's literal chain
  reports rc=1 even when the open succeeds. The criterion grades the output text, which is correct.
- **Gap found:** rows Z-S208 (pull licensed, gate admits push only), Z-S209 (GATE 5 whitespace-path
  parsing) and Z-S210 (the order's `-Z-DT89-S<k>` id family is unparseable by both row gates, so the rows use
  the seat form Z-S<n>; the first dry-run grade caught it). Also observed and not filed (another project's record): CTO~Z's v2.1.179 ledger
  `20260916T010633Z_posn-aggfix-...` reads UNINDEXED OPEN in `deploy_ledger.py list` for the same missing-marker
  reason my v2.1.181 entry had.

## Blockers

None.

## Current State

- Portal `origin/PROD` = `6dfc3390`, tag `portal-v2.1.182`, served at opalinvest.dev since 23:59:39Z;
  rollback target `07d5af72` (`portal-v2.1.181`). `origin/DEV` = `f22e369c`, unmoved.
- Security Analysis stays Dev+admin only; managers not widened.
- Main `portal/` tree DEV @ `f22e369c`, clean. SITEZ gitlink `f22e369c` in `75de778a8a`, LOCAL (not pushed).
- Ledger `org/critical_paths/change_management/20260921T2353Z_amgt-rk89-portal-prod-promote_deploy_completion.md` CLOSED.
- Residue: `.runtmp/portal-promote-20260921T235549Z` and `...20260921T172305Z` (gitignored, inert).

## Next Steps

- [2.0.0_SA_COO~Z] Drain rk-89 from the committed instance; disarm row Z-S201 on AC6's counts; release freeze
  (my Step-8 report).
- [0.0.0_AB_MSTR~Z] Carry the SITEZ commits (gitlink `75de778a8a` and this drain) at the next window.
- [Andrew] Visual look at the Exec Management tab on PROD (the managers'-review acceptance per the order).
