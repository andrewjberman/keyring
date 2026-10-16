# ADVI_COTBKF decomposition -- ROUND 98 (issuer 2.0.0_SA_COO~C1 on dell1; drafted 2026-10-16) -- apply the relabelled FWD-3 tables under the signed never-widen pair

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** the signed pair for the relabelled move. COO half `ledger/NEVER_WIDEN_R97_FWD3_LABELS_COO_HALF.md` GIVEN @814c6cc826 (sha256 `4ab6b4b15433758c...`); CTO half `ledger/NEVER_WIDEN_R97_FWD3_LABELS_CTO_HALF.md` SIGNED @eceab5b4b0 against the COO half's section-1 versions and section-3 hashes (CTO msg 6563); the CTO named the applier `0.7.0_AE_CloudOps~CB1` (seat requested of `0.0.0_AB_MSTR~DELL1`). Round 97's `CB-cs-1` (worker ~187, order complete @76a608ad60) measured the build the pair covers.

**What this round does.** One SERVED cell: the applier overwrites the three served FWD-3 keys with the round-97 local build as built (labels only; no pre-existing value moves; `run_commit` and two appended columns differ), under a change-management ledger entry opened at the start and closed at completion, with the three prior VersionIds re-read immediately before the first put.

**Rule 24.** Domain: the served write of the relabelled tables. Subtraction: the pair (done) and the build (done, round 97) -> the apply and its read-back -> `CB-ct-1`. Uncovered here by design: the CVO's grade of the labelled served tables (L9 on the served artifact); the reader gate stays closed.

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-ct-1` | the applier re-reads the three prior versions, runs `--dry-run` against the round-97 build (hashes equal the pair's), applies with `--apply --overwrite`, runs `--verify`, and closes the ledger with the read-back | FWD-3 | SERVED | the pair (both halves, signed) | `0.7.0_AE_CloudOps~CB1` |

**Fan-out (to state at the cut):** `1 of 1 chains, cap 8` (a seat, not a worker subagent).
