# NFRA_DEVPLN decomposition -- round 6, ENRICHMENT: the test-seam guard; the client-facing close and the installs wait on others (issuer 2.0.0_SA_COO~DV; cut 2026-10-14 ~02:0xZ)

**Status: ISSUED in one issuance.** The issuance commit carries the `fanout:` line. The decomposition is FROZEN at the cut.

**Input.** `org/missions/D0/NFRA/NFRA_DEVPLN/ledger/ROUND_ANALYSIS.round5.md` @6bbbc233d4 (1.0.0_SA_CTO msg 109013). The file was re-read at its committed bytes before the cut (sections 1-3, no addendum).
**Cut on.** PRD v0.3 @14a0501ee5; `python .tools/prd-signoff.py status NFRA_DEVPLN`: ADMITTED. Lease FULL.

## Measured at the base (issuer, ~02:0xZ)

1. dell2's list on the cluster copy: five OPEN approval rows for Andrew, all client-facing: `3635` (`irpt-ytd-from-first-day-and-wider-export-modal`), `8500`, `7b45`, `fde0` (the three ANLREQ features) and `7773` (`cand/dell2/partner-firm-stack`, a partner-firm filing, opened 23:19Z). Andrew has ruled none. Portal DEV `5e40e541` (2 approved, 3 unapproved), PROD `10e7664d`.
2. The test seam is unguarded. `OPAL_CLOUD_READ_LOCAL=/tmp/ocl_probe` (a directory holding a `box=dell1/open_calls.json` with `written_at` 2099 and no rows), with NO `OPAL_STATE_ROOT`, makes `approval-status --branch cand/dell1/amgt-sa-header-money-and-dash-reasons` print `NOTE: dell1 list read from cluster written_at=2099-01-01T00:00:00Z` and `state=ABSENT`, while the real row reads `APPROVED valid=yes`. A stray variable in a production environment makes fixture data authoritative; for a test-only class, ABSENT means "no approval needed". `_source_git` already refuses real refs under `OPAL_STATE_ROOT` (line ~1496); `_source_cluster` and the git stand-in honour `OPAL_CLOUD_READ_LOCAL` with no test switch beside it (lines ~1487 and ~1513).
3. The pre-push limb is merged (`367ce6ff40`) and NOT installed; the CTO directed `0.0.0_AB_MSTR` to install it on the laptop now and then on `~DELL2`, `~DELL1`, `~Z` (msg 109013).

## Cells and issuer acts

| item | cell / act | what | risk | served by |
|---|---|---|---|---|
| E1 | act A14 | after Andrew rules the five dell2 rows: the integrator's merge-forward of each approved feature, then the DT's chosen-set promote naming only those (a DT order cut then, SERVED, with the L8 packet to the CVO). No order is cut before he rules | -- | issuer, event-gated on Andrew |
| E2 | act A15 | the install read-backs from all four managers (each: `cmp` of the installed hook against the canonical source, and the unapproved-commit demonstration through the INSTALLED hook, exit 1), folded into the round's record. Not a worker cell | -- | the managers; issuer collects |
| E3 | `DP-h-1` | the seam guard (W2-S12): `OPAL_CLOUD_READ_LOCAL` is honoured only when `OPAL_STATE_ROOT` is also set (a test switch); set without it, it is ignored with a stderr NOTE and the production sources are read | LOCAL | `0.9.0_WK_NFRA_DEVPLN~1` (worker-light) |

Not cut, by ruling: W1-S15's stricter reading stands (a live FAST lease admits its own commits through the walk; a new DEV ref and a non-fast-forward are still refused first): the limb already behaves so, no change.

## Rule 24 (four postulates)

**Domain:** the three items of the analysis's list. **Subtraction:** E1 -> A14 (event-gated); E2 -> A15 (managers); E3 -> DP-h-1. No item is unowned.
**Same grain:** one guard. **Intent coherence:** the guard changes WHEN a test stand-in is honoured, never what a production read returns. **State coherence:** with the stand-in honoured only under `OPAL_STATE_ROOT`, a production tool that sets only one of the variables cannot read fixtures, and a test that sets both reads only fixtures.

## Dependency chains and fan-out

One cell; no edge. M = 1 chain; N = 1 worker; cap 8.

## Battery (L5)

`comp-iam`: not applicable (the cell adds no S3 call; the reads it guards already exist). `comp-adversary`: RUN as a BLIND-stated read of the one cell's invocations and the measurement above; blind to the filesystem around the cited paths. Finding inlined: a guard that silently ignores a variable hides a misconfigured test, so the ignore prints a NOTE and the test asserts the NOTE.
