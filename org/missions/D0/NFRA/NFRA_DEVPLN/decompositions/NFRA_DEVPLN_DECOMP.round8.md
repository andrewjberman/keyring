# NFRA_DEVPLN decomposition -- round 8, ENRICHMENT: Andrew approved the five dell2 rows (A14) and the law edit; two cells (issuer 2.0.0_SA_COO~DV; cut 2026-10-14 ~12:0xZ)

**Status: ISSUED in one issuance.** The issuance commit carries the `fanout:` line. The decomposition is FROZEN at the cut.

**Input.** `org/missions/D0/NFRA/NFRA_DEVPLN/ledger/ROUND_ANALYSIS.round7.md` section 3 (item 2: "After Andrew rules the dell2 rows: A14, FWD-1's client-facing close (SERVED, with the L8 packet)"; item 1, the S5 widening, is served: `NFRA_CTLPLN-S9123` merged @2d35ab062c) and 1.0.0_SA_CTO msg 109110 and 109118, which carry Andrew's word of ~11:4xZ, record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_114xZ_EIGHT_OPEN_CALLS_ANSWERED.md` (rows 1-3 approve the five dell2 features; row 6 approves the CLAUDE.md Portal edit, committed @fcdfc34843 LOCAL). No round-8 analysis file exists; the CTO's two messages are the input and say so.
**Cut on.** PRD v0.3 @14a0501ee5; `python .tools/prd-signoff.py status NFRA_DEVPLN`: ADMITTED. Lease FULL.

## Measured at the base (issuer, ~12:0xZ)

1. `approval-status` reads `state=APPROVED valid=yes by=andrew` for all five: `3635` (`cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal`, head `030737656431`), `8500` (`anlreq-90-held-submit`, `794b7df495d2`), `7b45` (`anlreq-88-advisory-fee`, `9ef6a359b807`), `fde0` (`anlreq-87-model-order`, `62d455f57525`), `7773` (`partner-firm-stack`, `1c71bfd8e1a5`, 21 commits). All class `client-facing`.
2. On origin: `8500`, `7b45`, `fde0` heads are ancestors of `origin/DEV` (`ab8ecc56`), through three unapproved direct merges; `3635` and `7773` are not on DEV. None of the five is on `origin/PROD` (`7db035e4`). `portal-merge-forward.sh <branch> --repo portal` without `--push` reads `result=MERGED` for `3635` (merge `d17e7414ed`) and for `7773` (merge `991cc9867b`), each with `pushed=no`.
3. `bash .tools/portal-release-build.sh --check PROD --repo portal --prod-ref 63c4f9e3...` reads `features=4 first_parent_commits=4 unapproved=0 ref=refs/remotes/origin/PROD`.
4. The payload limb at HEAD (`.tools/portal-hooks/dev_push_payload_gate.py`) admits a plain test-only commit (route B) and any push by a seat holding a live FAST lease. `python .tools/tests/test_dev_push_payload_gate.py` reads `cases=19/19 ok=True`. `.claude/skills/closer-drive/SKILL.md` step 5 still reads "push DEV yourself ... admits a DEV push only from a live FAST lease's seat" (count of `merge-forward` in the file: 0).

## Cells and issuer acts

| item | cell / act | what | risk | served by |
|---|---|---|---|---|
| E1 | act A14a | the integrator pushes the merge-forward of `3635` and `7773` to DEV (`portal-merge-forward.sh <branch> --push`, one at a time). The three ANLREQ features are already on DEV and need none | -- | `0.0.0_AB_MSTR`, ask, one message |
| E2 | `DP-y-1` | the DT's chosen-set promote naming exactly the five approved features, receipt names the five rows and `PROMOTE-CLIENT-FACING count=5`; both trunks measured after | SERVED | `0.4.0_DT_ClientPlatform` (waits on A14a by a git command in its first step) |
| E3 | `DP-j-1` | the pre-push limb's two direct-push exemptions go: a live FAST lease no longer admits a push by itself, and a plain test-only commit no longer passes (route B becomes a test-only MERGE through `portal-merge-forward.sh` with trailer `Approved-By: test-only @-`); `/closer-drive` step 5 lands through the merge-forward | LOCAL | `0.9.0_WK_NFRA_DEVPLN~1` (worker-light) |

## Rule 24 (four postulates)

**Domain:** the items of the round-7 list plus the law edit's follow-on (msg 109110). **Subtraction:** round-7 item 1 -> merged (S9123); item 2 -> E1 + E2; the law edit's cell -> E3. No item is unowned.
**Same grain:** E1 is an act, E2 and E3 are one order each. **Intent coherence:** E1+E2 ship the approved features; E3 closes the last direct DEV routes. **State coherence:** E3 changes the push gate only; a plain commit with no merge-forward trailer is refused for every seat, and an approved merge (route A) and a PROD-into-DEV back-merge (route C) stay admitted, so E1's push still passes the hook.

## Dependency chains and fan-out

Chains: (E1 -> E2) and (E3). The edge E1 -> E2 is a precondition E2's first step checks with a git command and STOPS on. E3 writes the gate, its test and one skill file; E2 writes the DT's ledger and receipt. Disjoint. M = 2 chains; N = 2 workers; cap 8.

## Battery (L5)

`comp-iam`: not applicable (git pushes to portal branches; no IAM change). `comp-adversary`: RUN, BLIND to the filesystem around the cited paths. Findings inlined: (a) E3 must keep the test-only merge-forward working, since `portal-merge-forward.sh` writes `Approved-By: test-only @-`, which route A cannot verify, so the cell gives that trailer its own check; (b) E2's PROD tip after the promote carries five first-parent release merges, and the three ANLREQ features keep their unapproved direct merges on DEV (as for the first two features: PROD holds its own merge of each).
