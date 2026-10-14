# NFRA_DEVPLN decomposition -- round 7, ENRICHMENT: one small repair (S4 and W1-S16); the client-facing close waits on Andrew (issuer 2.0.0_SA_COO~DV; cut 2026-10-14 ~02:0xZ)

**Status: ISSUED in one issuance.** The issuance commit carries the `fanout:` line. The decomposition is FROZEN at the cut.

**Input.** `org/missions/D0/NFRA/NFRA_DEVPLN/ledger/ROUND_ANALYSIS.round6.md` (1.0.0_SA_CTO msg 109029), read at its committed bytes before the cut: sections 1-3, no addendum. Section 3: "If he has not ruled when round 7 is cut, the round is the repair alone. The project then waits on his approvals, a dated wait recorded with `unblock.py tick --owed-call` on the five rows, not an empty tick."
**Cut on.** PRD v0.3 @14a0501ee5; `python .tools/prd-signoff.py status NFRA_DEVPLN`: ADMITTED. Lease FULL.

## Measured at the base (issuer, ~02:0xZ)

1. Andrew has ruled none of the five dell2 rows (`3635`, `8500`, `7b45`, `fde0`, `7773`): all OPEN on the cluster copy. So the round is the repair alone.
2. `bash .tools/portal-release-build.sh --check PROD --repo portal --prod-ref 63c4f9e3...` prints `RELEASE-CHECK features=1 first_parent_commits=1 unapproved=0` and `head=10e7664d...`: it read the STALE local branch `refs/heads/PROD` (`10e7664d`) and not `origin/PROD` (`7d5cb34d`), which holds 2 first-parent commits since the settlement. The output names no ref. Code: `main_check`, `.tools/portal-release-build.sh` line ~146-152 tries `refs/heads/$CHECK_REL` first, then `refs/remotes/origin/$CHECK_REL`.
3. `bash .tools/portal-release-build.sh --selftest` reads `cases=10/10 ok=True`. `.tools/tests/test_open_calls_cloudread.py` reads `cases=10/10 ok=True` and its case 9 (the stand-in set with `OPAL_STATE_ROOT` unset) runs the production git source, a real `git show origin/box/zz9` in the real repository; the file has no `GIT_DIR` isolation (count 0).

## Cells and issuer acts

| item | cell / act | what | risk | served by |
|---|---|---|---|---|
| E1 | act A14 | after Andrew rules the five dell2 rows: the integrator's merge-forward, then the DT's chosen-set promote naming only what he approves (SERVED, with the L8 packet). No order is cut before he rules. The wait is recorded with `unblock.py tick --owed-call` on each row | -- | issuer, event-gated on Andrew |
| E2 | `DP-i-1` | the repair: (S4) `portal-release-build.sh --check <name>` prefers `refs/remotes/origin/<name>` for a trunk name (`DEV`, `PROD`) and prints the resolved ref and sha on its result lines; (W1-S16) test case 9 stops making a real ref lookup | LOCAL | `0.9.0_WK_NFRA_DEVPLN~1` (worker-light) |

## Rule 24 (four postulates)

**Domain:** the two items of the analysis's list. **Subtraction:** E1 -> A14 (event-gated); E2 -> DP-i-1. No item is unowned.
**Same grain:** one repair batch of two small, related fixes. **Intent coherence:** both stop a check from reading a ref it should not (a stale local trunk; the real repository inside a test). **State coherence:** `--check` only reads; a name that is not a trunk keeps its current resolution order (local release branch first), so the normal flow (a `release/<stamp>` branch built locally) is unchanged.

## Dependency chains and fan-out

One cell; no edge. M = 1 chain; N = 1 worker; cap 8.

## Battery (L5)

`comp-iam`: not applicable. `comp-adversary`: RUN as a BLIND-stated read of the cell's invocations; blind to the filesystem around the cited paths. Finding inlined: the printed `ref=` must be the ref actually read (not the requested name), or the new field could itself mislead.
