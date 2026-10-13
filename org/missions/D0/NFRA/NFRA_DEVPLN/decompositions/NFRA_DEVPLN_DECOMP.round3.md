# NFRA_DEVPLN decomposition -- round 3, ENRICHMENT: the gate, the declined arm shown, the dell2 feature, the three re-registered merges, one repair (issuer 2.0.0_SA_COO~DV; cut 2026-10-13 ~22:0xZ)

**Status: ISSUED in one issuance.** The issuance commit carries the `fanout:` line. The decomposition is FROZEN at the cut.

**Input.** `org/missions/D0/NFRA/NFRA_DEVPLN/ledger/ROUND_ANALYSIS.round2.md` @8cf96d5f52 (1.0.0_SA_CTO msg 108933: "cut round 3 in one issuance") and the CTO ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261013_213xZ_LAPTOP_E846_7D95_BB8B.md`.
**Cut on.** PRD v0.3 @14a0501ee5; `python .tools/prd-signoff.py status NFRA_DEVPLN`: ADMITTED (ratified-text SIGNED by 3.0.0_SA_CVO~L, brief SIGNED auto). Lease FULL.

## Measured at the base (issuer, ~22:0xZ, portal origin fetched)

1. Row `e89f` (`cand/laptop/declined-example`) is `DECLINED valid=no by=1.0.0_SA_CTO`. Run for real: `portal-merge-forward.sh` prints `REFUSED reason=declined`, `portal-release-build.sh --features` prints `REFUSED reason=declined`, DEV unchanged at `24877b67`. FWD-2's declined arm is shown; no cell is needed.
2. `.tools/hooks/never-rules-gate.sh` has no commit since `14a0501ee5`: S03 has not landed.
3. The three dell2 ANLREQ merges on DEV, measured: `73d8d3a4` (parents `63c4f9e3`, `794b7df4`), `0101dd66` (`73d8d3a4`, `9ef6a359`), `a577cba5` (`0101dd66`, `62d455f5`). Feature heads: `794b7df4` (2 commits, `923f7d69` and `794b7df4`), `9ef6a359` (1), `62d455f5` (1); each cut from PROD `63c4f9e3`. Each head's `origin/PROD..<head>` set is entirely DEV-only (overlap equals commits) because DEV already merged it, not because it was cut from DEV.
4. `portal-merge-forward.sh cand/laptop/local-only-probe` (a local-only branch) prints `REFUSED reason=fetch-failed` under the default fetch: row W2-S7 reproduced. `add --kind approval --check-only --branch 794b7df4` (a bare sha) prints `REFUSED reason=branch-not-found`: check-only accepts only a branch name.
5. Registration is per box: a row for `cand/dell2/<slug>` lives on dell2's own list and is written by a dell2 seat (`add` is refused for another box's list). The laptop cannot write it.

## Cells and issuer acts

| item | cell / act | what | risk | served by |
|---|---|---|---|---|
| E1 | `DP-g-1` | S03 gate edit (round-1 cell file stands) | -- | `1.0.0_SA_CTO` (not a task order) |
| E1 | act A7 | after S03 lands: a direct DEV push from a box seat refused under the new gate, and the gate bytes read on all four box branches (`MSYS_NO_PATHCONV=1 git rev-parse origin/box/<b>:.tools/hooks/never-rules-gate.sh`, four blob shas compared) | -- | issuer, event-gated on S03 |
| E2 | (done, no cell) | the declined arm shown refused, measured 1 above | -- | issuer, done |
| E3 | act A11 | dell2's IRPT_ANLREQ page change through the route: dell2 cuts `cand/dell2/<slug>` from PROD and registers it; the issuer then reads the row (`approval-status`), after Andrew's approval has the integrator push the merge-forward, and cuts the DT's promote order. No cell can be cut before the branch exists | -- | dell2 builds; issuer event-gated |
| E4 | `DP-d-1` | the registration waiver: `open-calls.py add --kind approval --waive-overlap <sha,...> --waiver-ref <path>` excuses ONLY the named commits from the DEV-overlap refusal; and `--check-only` accepts any commit-ish | LOCAL | `0.9.0_WK_NFRA_DEVPLN~1` |
| E4 | act A12 | the three rows (`anlreq-90`, `anlreq-88`, `anlreq-87`), each bound to its feature head, registered on dell2's list by a dell2 seat with the waiver and the CTO ruling as its reason: the issuer creates the three `cand/dell2/anlreq-*` refs on origin and hands the exact commands to `1.0.0_SA_CTO~DELL2` through `0.0.0_AB_MSTR` once `DP-d-1` is on CLOUD | -- | issuer + dell2 seat |
| E5 | `DP-d-2` | the batch repair: merge-forward falls back to a local-only branch when the default fetch finds the ref absent on origin (W2-S7) | LOCAL | `0.9.0_WK_NFRA_DEVPLN~2` (worker-light) |
| E5 | (not cut) | W2-S8: the pin-drift advisory line comes from `.tools/proof-of-spec-check.py`, outside this project's paths; the row stays an OBSERVATION for the CVO | -- | -- |

Carried and not cut (Andrew's act): the CLAUDE.md FAST-lease line edit. Reading recorded for the CTO: the waiver covers the FOUR FEATURE COMMITS (`923f7d69`, `794b7df4`, `9ef6a359`, `62d455f5`), because the three merge commits (`73d8d3a4`, `0101dd66`, `a577cba5`) lie on no branch and so are never in a registration's overlap set; that is the exact set, and no other DEV-only commit is excusable.

## Rule 24 (four postulates)

**Domain:** the five items of the analysis's ENRICHMENT LIST. **Subtraction:** E1 -> DP-g-1 + A7; E2 -> done; E3 -> A11; E4 -> DP-d-1 + A12; E5 -> DP-d-2 (+ W2-S8 not cut, reason given). No item is unowned.
**Same grain:** one tool extension or one repair per cell. **Intent coherence:** `DP-d-1` serves registration only; `DP-d-2` serves the merge-forward only. **State coherence:** neither cell pushes or touches a shared branch; the waiver excuses named commits only and any other overlap still refuses.

## Dependency chains and fan-out

No edges. `DP-d-1` writes `open-calls.py` and a new test; `DP-d-2` writes `portal-merge-forward.sh`. Disjoint. M = 2 chains; N = 2 workers; cap 8.

## Battery (L5)

`comp-iam`: not applicable. `comp-adversary`: RUN as a BLIND-stated read of the two cells' invocations and the ruling text; blind to the filesystem around the cited paths. Findings inlined: (1) a waiver is the one place a check is loosened, so the criterion proves the NEGATIVE control (the same call without the waiver still refuses) beside the positive; (2) the waiver must name commits, never a count or a range, or it widens.
