# NFRA_DEVPLN decomposition -- round 5, ENRICHMENT: the structural close of S03, one repair batch, and the client-facing close held for Andrew (issuer 2.0.0_SA_COO~DV; cut 2026-10-13 ~23:5xZ)

**Status: ISSUED in one issuance.** The issuance commit carries the `fanout:` line. The decomposition is FROZEN at the cut.

**Input.** `org/missions/D0/NFRA/NFRA_DEVPLN/ledger/ROUND_ANALYSIS.round4.md` @e8db882826 (1.0.0_SA_CTO msg 108988: "cut round 5") and his messages 108974 (the limb in round 5, no override) and 108992 (A13 retired).
**Re-read before the cut.** The analysis file was read at its committed bytes at ~23:45Z, after the round-3 miss (row S3): sections 2 and 3, 41 lines, no addendum.
**Cut on.** PRD v0.3 @14a0501ee5; `python .tools/prd-signoff.py status NFRA_DEVPLN`: ADMITTED. Lease FULL.

## Measured at the base (issuer, ~23:5xZ, portal origin fetched)

1. Portal DEV `24877b67`, PROD `10e7664d` (unchanged since the first chosen-set promote). `portal-dev-approval-read.py` reads DEV: 1 approved, 3 unapproved.
2. dell2's list on the cluster copy: `8500` (anlreq-90), `7b45` (anlreq-88), `fde0` (anlreq-87) OPEN; `cffa` CLOSED declined by `1.0.0_SA_CTO~DELL2` at 23:02Z (a duplicate, closed before `withdrawn` existed); `3635` OPEN and the row `approval-status` reads for `cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal`. Andrew has ruled none of them.
3. `.tools/portal-hooks/pre-push` is byte-identical to the installed `portal/.git/hooks/pre-push` (cmp). It has a per-ref VALGATE D-1 loop and a PROD typecheck; it has no DEV payload check.
4. `OPAL_GIT_READ_ROOT` appears in `.tools/open-calls.py` (a second test seam beside `OPAL_CLOUD_READ_LOCAL`); the merge-forward self-test builds fixtures with unchecked commands.

## Cells and issuer acts

| item | cell / act | what | risk | served by |
|---|---|---|---|---|
| E1 | `DP-f-1` | the pre-push payload limb, FIRST: `.tools/portal-hooks/dev_push_payload_gate.py` plus a call from `.tools/portal-hooks/pre-push` for a push to `refs/heads/DEV`; exempt routes: an approved merge, a test-only change, a PROD-into-DEV back-merge, a live FAST lease's seat; every other push fails closed, typed or scripted. Not installed by the cell | LOCAL | `0.9.0_WK_NFRA_DEVPLN~1` |
| E2 | act A14 | after Andrew rules the dell2 rows: the integrator's merge-forward of each approved feature, then the DT's chosen-set promote naming only what he approved (a DT order cut at that time, SERVED, with the L8 packet to the CVO). No cell can be cut before his word: there is nothing yet to merge-forward | -- | issuer, event-gated on Andrew |
| E3 | `DP-f-2` | the repair batch: one test seam variable (`OPAL_CLOUD_READ_LOCAL` also stands in for the git source; `OPAL_GIT_READ_ROOT` removed) and exit checks on the merge-forward self-test's fixture writes (an `fx` helper) | LOCAL | `0.9.0_WK_NFRA_DEVPLN~2` (worker-light) |
| -- | (no cell) | W1-S13, the portal gitlink drift in a worker worktree: read and recorded only (CTO) | -- | -- |
| -- | (retired) | A13, the dell2 duplicate withdraw: retired by the CTO and the issuer (cffa already closed declined; 3635 is the live row) | -- | -- |
| -- | (Andrew's, carried) | the CLAUDE.md law-edit call `laptop-20261013T223003Z-3d7e`; the limb keeps both law routes (FAST and test-only) while it waits | -- | Andrew |

## Rule 24 (four postulates)

**Domain:** the three items of the analysis's ENRICHMENT LIST plus the retired A13. **Subtraction:** E1 -> DP-f-1; E2 -> A14 (event-gated, no cell); E3 -> DP-f-2 (W1-S13 recorded only). No item is unowned.
**Same grain:** one hook limb or one repair batch per cell. **Intent coherence:** `DP-f-1` is a refusal at push time; `DP-f-2` changes test seams only. **State coherence:** the limb only READS (it changes no ref) and is not installed by the cell; each exemption is a named route with its own test and its own refusal control; a missing checker warns and does not block.

## Dependency chains and fan-out

No edges. `DP-f-1` writes `.tools/portal-hooks/` and a new test; `DP-f-2` writes `open-calls.py`, one test and `portal-merge-forward.sh`. Disjoint. M = 2 chains; N = 2 workers; cap 8.

## Battery (L5)

`comp-iam`: not applicable. `comp-adversary`: RUN as a BLIND-stated read of the two cells' invocations and the CTO's three required demonstrations; blind to the filesystem around the cited paths. Findings inlined: (1) the limb widens what DEV admits through each exemption, so each route has a pass test and a refusal control; (2) the real-portal criteria name shas that are stable (the integrator's merge `24877b67` over `a577cba5`; the declined example's commit over PROD `10e7664d`), so they cannot drift with later pushes.
