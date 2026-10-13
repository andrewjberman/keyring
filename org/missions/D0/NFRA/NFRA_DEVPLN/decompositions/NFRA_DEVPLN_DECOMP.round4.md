# NFRA_DEVPLN decomposition -- round 4, ENRICHMENT: the route made safe for a feature built on another box (issuer 2.0.0_SA_COO~DV; cut 2026-10-13 ~22:5xZ)

**Status: ISSUED in one issuance.** The issuance commit carries the `fanout:` line. The decomposition is FROZEN at the cut.

**Input.** `org/missions/D0/NFRA/NFRA_DEVPLN/ledger/ROUND_ANALYSIS.round3.md` @75335735b6 (1.0.0_SA_CTO msg 108959: "cut round 4"), ENRICHMENT LIST items 1-4, plus the issuer's own row `NFRA_DEVPLN-S2` (below), which the CTO's list predates.
**Cut on.** PRD v0.3 @14a0501ee5; `python .tools/prd-signoff.py status NFRA_DEVPLN`: ADMITTED. Lease FULL.

## Measured at the base (issuer, ~22:5xZ)

1. dell2 has registered its first organic client-facing feature, branch `cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal` (on portal origin @`03073765`), TWICE: rows `dell2-20261013T221352Z-cffa` (keep) and `dell2-20261013T221411Z-3635` (duplicate), both OPEN, both visible in `list --all --cloud`.
2. On the laptop, `python .tools/open-calls.py approval-status --branch cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal` prints `state=ABSENT`. `approval_read` (`.tools/open-calls.py` line ~1459) prefers any working-tree list for the box; the laptop's copy of dell2's list is readable and stale, so a real OPEN row reads as absent, not unreadable.
3. `close` on an approval row accepts only `--decision approved|declined`; the duplicate cannot be withdrawn without reading as Andrew's decline. `approval_read` picks the NEWEST row per branch, which is the duplicate `3635`.
4. `.tools/hooks/never-rules-gate.sh` has no commit since `14a0501ee5`: S03 not landed (the CTO says it is landing next).
5. `portal-merge-forward.sh cand/laptop/local-only-probe --repo portal` prints git's `multiple merge bases` warning (row W2-S10); `refs/heads/<b>` is read ahead of a stale `origin/<b>` only when the ref is absent on origin, which is the stale-safe choice (row W2-S9: no repair).

## Cells and issuer acts

| item | cell / act | what | risk | served by |
|---|---|---|---|---|
| E1 | `DP-g-1` | S03 gate edit, landing now (the round-1 cell file stands) | -- | `1.0.0_SA_CTO` |
| E1 | act A7 | after S03: a direct DEV push from a box seat refused under the new gate; the four blob shas of `never-rules-gate.sh` read on `origin/box/{laptop,dell1,dell2,sitez}` (`MSYS_NO_PATHCONV=1 git rev-parse <ref>:.tools/hooks/never-rules-gate.sh`, with a positive control) | -- | issuer, event-gated on S03 |
| E2 | act A12 | the three ANLREQ rows (waiver ref = the round-3 analysis), registered by a dell2 seat; relayed through MSTR | -- | dell2 seat |
| E3 | act A11 | dell2's feature through the route: registration check, Andrew's word, the integrator's merge-forward, the DT's chosen-set promote (a DT order at that time), the read. Its row exists now (twice); the cells below make it routable | -- | issuer, event-gated on Andrew's word |
| S2a | `DP-e-1` | a `withdrawn` close decision for approval rows: `close --decision withdrawn`; `approval-status` ignores withdrawn rows; all rows withdrawn reads `ABSENT` so every consumer refuses | LOCAL | `0.9.0_WK_NFRA_DEVPLN~1` |
| S2b | `DP-e-2` | `approval-status` reads a foreign box's list from the freshest readable source (cluster copy, `origin/box/<box>`, working tree, by `written_at`); this box's own list stays the working tree. Runs after `DP-e-1` in slot ~1 (same file) | LOCAL | `0.9.0_WK_NFRA_DEVPLN~1` |
| E4 | `DP-e-3` | W2-S10: the merge-forward's changed-file read no longer prints git's `multiple merge bases` warning | LOCAL | `0.9.0_WK_NFRA_DEVPLN~2` (worker-light) |
| E4 | (no repair) | W2-S9: the local fallback already prefers `refs/heads/<b>` exactly when origin lacks the ref, which is the stale-safe ref; `--no-fetch` keeps reading `origin/<b>` first by design | -- | -- |
| -- | (not cut) | W2-S8 goes to the CVO as an observation (CTO) | -- | -- |

Issuer reading, recorded: `DP-e-1` and `DP-e-2` are not on the CTO's round-3 list. They answer row `NFRA_DEVPLN-S2`, raised at ~22:25Z from dell2's first live registration; they are inside the issuer's own decomposition (the approval row's read and close), and without them the first client-facing feature cannot be routed from the laptop. The CTO reads them at the round-4 analysis.

## Rule 24 (four postulates)

**Domain:** the four items of the analysis's list plus row S2. **Subtraction:** E1 -> DP-g-1 + A7; E2 -> A12; E3 -> A11 (+ DP-e-1, DP-e-2 as its preconditions); E4 -> DP-e-3 (+ W2-S9 no repair, reason given). No item is unowned.
**Same grain:** one close decision, one read source or one warning per cell. **Intent coherence:** `DP-e-1` changes what a row can END as; `DP-e-2` changes where a row is READ from; neither changes who may approve. **State coherence:** a withdrawn row ends the row and moves no branch, no trunk and no other row; withdrawing is not declining.

## Dependency chains and fan-out

Edge `DP-e-1 -> DP-e-2` (both write `.tools/open-calls.py`). `DP-e-3` writes `.tools/portal-merge-forward.sh` only. M = 2 chains; N = 2 workers; cap 8.

## Battery (L5)

`comp-iam`: not applicable (`DP-e-2` reads one S3 object through the tool's own reader, which already exists; no policy changes). `comp-adversary`: RUN as a BLIND-stated read of the three cells' invocations; blind to the filesystem around the cited paths. Findings inlined: (1) a freshest-source rule must tie-break and fail closed: equal `written_at` takes the cluster copy, and every source unreadable is UNREADABLE (rc 2), never ABSENT; (2) a withdraw must not be usable by the builder to erase a DECLINED or APPROVED row, so it applies only to an OPEN row.
