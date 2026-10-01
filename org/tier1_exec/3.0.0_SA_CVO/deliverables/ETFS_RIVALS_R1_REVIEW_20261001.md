# ETFS_RIVALS round 1 -- CVO review (L8 compile, L9 dispositions)

**Seat:** 3.0.0_SA_CVO~RV, paired by Andrew with 2.0.0_SA_COO~RV (COO~RV msg 27487). 2026-10-01 ~04:3xZ.
**Packet:** `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/DRAIN_END_READ_ROUND1.md`. It names
3.0.0_SA_CVO~Z as owner of this compile (:27); this lane took it under the pairing.
**Carriers:** `surprise-channel/adjudications/ADJUDICATION_v1.Z.md` (5 rows, 21 items),
`surprise-channel/remediations/REMEDIATION_v1.Z.md` (8 items). Watermark 2026-09-30T15:35Z.
**Not a slug.** Round 2 is 8 of 9 terminal (TO-RIV-d-3 open), so the L10 slug waits for round 2's drain-end and will
carry both rounds.

## Denominator

The channel holds 61 rows (`comp-surprise --project ETFS_RIVALS --all`: 61 open, 11 ARMED, 0 compiled before this
commit). This compile covers the 29 with `surfaced_at` at or before 15:35Z, the same 29 the packet counted (8
BLOCKING/ARMED, 2 BLOCKING/INERT, 19 OBSERVATION/INERT). The other 32 are round 2's.

## What this seat measured itself (not taken from the packet)

| claim | read | result |
|---|---|---|
| the gateway still serves the routes | SSM `cbe1a6ef-1cfc-473b-a539-097ebb8e9f03`, read-only | host server.py sha256 `384c6d41...` == `git show d61fde4693` (the 01:38Z NFRA_OPLGTW deploy); /health 200, /rivalfunds 401, /rivalfunds/archive 401 |
| that ref carries the routes | `git show <ref>:.../server.py \| grep -c rivalfunds` | d61fde4693: 7; positive control 4ce7946426: 7; 4ce7946426 is NOT an ancestor of d61fde4693 (content, not lineage) |
| gold exists | `list-objects-v2` opal-data-etfs | canonical_shape 745 objects / 501 dates; trade_schedule 743 / 500; newest 2026-09-29; page 12 objects, date=2026-09-30 |
| no double run (W3-S4) | markers + one sampled date | 10 build_canonical_shape markers, one per batch; date=2026-06-03's two objects were written 2026-09-30T12:32Z (24820 B) and 2026-10-01T02:17Z (77471 B) |
| ledger closed | ledger file :3 | CLOSED 20260930T153358Z |
| refs untagged (W5-S15) | `git tag --points-at` | 288fa78c93: none; 093fc247c6: none |

## Recommendations by driver

**For CTO (1.0.0_SA_CTO~Z)**
- **P1 -- rule row S1 before round 3 cuts G4.** The PRD (:307) and its own named vocabulary (etf_positioning_gold.py:150)
  contradict each other for every equity row once GICS lands. The decomposition holds sub_asset_class UNRESOLVED
  waiting on you (:98). It is a schema act: whichever reading wins, the PRD line moves with it.
- **P1 -- place W1-S4 (identity coverage) in a named round.** Decomp :123 excludes it from round 2 without naming
  where it goes. It now shapes a second table: round-2 row W3-S9 keys G5 on the Bloomberg id because G1's security_id
  is null. An item excluded by subtraction with no destination is the channel-with-no-destination failure.
- **P1 -- W1-S5: name the status and marker for a published not-updated page.** Round-2 row W1-S15 raised the same
  silence again for the multi-fund page. Two rounds have had to guess.
- **P2 -- W5-S12: one rule for deploy-only releases.** Either the issuer commits and deploys at its own seat (the path
  this round actually took), or the two gates resolve a worker's grant against the order-carrying tree. Today the
  decomposition cuts a worker leg that cannot run, and that cost this round four STOP rows (W5-S9, S10, S12, S2).
- **P2 -- W5-S3, W5-S7, W5-S14, W5-S15: fabric tooling.** Fresh-tree gateway reproducibility, the naming gate's
  tier-word false positive, the manifest re-encode (a second project hit it too: NFRA_OPALAI-Z-W2-S4), and the untagged
  rollback bases. Owners are yours to place. None blocks ETFS_RIVALS.

**For COO (2.0.0_SA_COO~RV)**
- **P2 -- the never-widen half's zero-count gate.** W5-S5: a schedule that goes live at apply time makes a "keys read
  0 at act start" gate false for any apply-then-act order spanning a 07:00 ET fire. d-3's half measured its BEFORE
  state, which is the right shape; keep it.
- **Deferred:** nothing in round 1 bears on d-3's resume. W2-S4 (ARMED, silver ordering across key formats) and W5-S24
  (BLOCKING/ARMED, silver DeleteObject) are round-2 rows for the round-2 compile, not this one.

## Deferrals

- CTO condition 5 (the signed-in /rivalfunds read, row W5-S13) is not a defect. It is FWD-1's acceptance evidence
  (PRD FIXTURES) and stays with a human. At L10 FWD-1 cannot grade REALIZED without it.
- W3-S4 is dismissed on the live record, not proven impossible. FWD-8 (the no-duplicate rerun) is its natural exercise.

## What you should have asked but did not

Whether the gateway routes survive the NEXT seat's deploy, not just the last one. This round's worst hour (W5-S16)
was another project's release, cut on a stale base, silently deleting /rivalfunds. Tonight's 01:38Z NFRA_OPLGTW deploy
kept the routes, but only because its base happened to descend from a tree carrying them by content: 4ce7946426 is
not its ancestor. Nothing checks that a gateway release preserves every live route. The /rivalfunds routes are one
rebase away from vanishing again, with ledger CLOSED and every check green, because AC2 ran once at 15:26Z and nothing
re-reads it. Round-2 row S2 (no lock across seats' gateway deploys) is the same hazard seen from the lock side. The
route-preservation side has no row. Proposed for the slug: a gateway release's pre-deploy diff names every route it
removes, and a removal of a route served by a project not in the release is a refusal.

-- 3.0.0_SA_CVO
