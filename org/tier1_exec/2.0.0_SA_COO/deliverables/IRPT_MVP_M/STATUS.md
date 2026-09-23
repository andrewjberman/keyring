# IRPT M: Holdings journey restart

Seat 2.0.0_SA_COO~M; worktree ajb_irpt_m; branch codex/irpt-m-completion.
Andrew-direct restart: HOLDINGS_RESTART_20260923.md (initial record b14966e203).
Existing closer contract v1.3 applies. Reviewer: CTO. Baseline: 1fd1c8f0fb.

## Candidate and write claims

Owned holdings_snapshot.py and test_economic_regressions.py: Cottonwood actual
ACCOUNT -> UNRESOLVED -> SECURITY tree, retaining signed/zero values and unique
AccountID/AssetID positions after strict validation. Targets remain private,
never the actual custody partition. Public schema unchanged. No edits to P's
Entry/auth/selection, shared adapters, packaging or IAM. 68 economic tests and
all 180 Gold tests pass offline; these do not establish real source admission.

Source receipts and aggregate findings: HOLDINGS_SOURCE_CHECK_20260923.json.
No raw investor rows committed. COT original workbook has 5,694 missing value
cells and no currency declaration. INF has 876/876 account totals tied to
positions to one cent; 14 flattened Eclipse memberships are incomplete. Select
one unambiguous INF account for first live proof while COT/49F adapters continue.

## Next proof and dependencies

- M: actual INF position adapter and dated Eclipse membership; custody-first
  49F 08335338 adapter with sole SmartX model overlay; Holdings summary/full tree.
- M targeted checks: source-bound currency; COT incomplete accounts; Eclipse full
  associated-account expansion. No guessed currency, residual cash or null-as-zero.
- P: exact Holdings Entry/selection/public-status package and runtime requirements;
  shared quantity/name/date/coverage adapter. Concrete request sent at 19:29Z.
- CTO: exact candidate review; concrete source-authority conflicts if encountered.
  No new task-order cycle or general research effort requested.

## Live state and limits

Three legacy serving prefixes empty; three canonical current indexes absent;
snapshot scheduler DISABLED today. Deployed Holdings is September21 and conflicts
with current public-status parsing. No accepted publication, cloud mutation,
vendor call or live browser proof this turn. M7 NOT_EVALUATED. Missing currency
and unknown source values still refuse; no current real admission is claimed.

Prior source485b69c061/current-viewer paired review and publication3539ad2ae5
are preserved. Universal reference services and analysis/export enrichment are
parked unless they block this Holdings thread. Push state LOCAL; MSTR owns shared
push. No deployment performed.
