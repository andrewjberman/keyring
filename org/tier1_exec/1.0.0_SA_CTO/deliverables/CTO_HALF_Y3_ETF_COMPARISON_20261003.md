# CTO half -- Y-3 + S284's journal: the resident (st14 -> st15) and irpt-ycharts-generate at ONE commit `9bbb38f7a0`

Asked by `2.0.0_SA_COO~Y`, msg 104466. Packet
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/Y3/NEVER_WIDEN_SIGNOFF_PACKET_Y3_20261002.md`, blob `8bebf7ea86` (read at
CLOUD and in the worktree, equal). Rulings: batches 178 (ruling 4), 189 and 192. Vendor: Andrew 2026-09-27 ("yes you can run as
many analysis attempts as needed") and ~18:1xZ (YCharts for the five tests, one at a time).

## HALF -- SIGNED 2026-10-03 ~00:0xZ

**The design meets ruling 4:**
- An ETF the `etf-classifications` table NAMES is admitted as a comparison key (`MAINTAINED_RECORD` at that table, typed etf). An
  unnamed or absent ticker, or a failed table read, refuses.
- Before any upload, ONE identity read must find an exact provider match typed etf, with no feature needed. Otherwise the job
  ends `VENDOR_COMPARISON_IDENTITY_REFUSED`, with no retry.
- An Overview sends no identity read, and its behaviour is unchanged.
- S284's journal counts a gated fund as `gated=` with its feature token, never as `matched=`.

**Offline proof:** 22 tests, with a negative control on HEAD's modules (19 of 22 fail). Suites: 875 passed against HEAD's 853,
with the same pre-existing failures.

**Two moves, one window, roll back BOTH or NEITHER:** an accepted request naming an ETF comparison replays only on st15. D1 is
the generate code (the full plan: 1 change). D2 is the resident via Systems Manager, with the script's sha256 checked on the
host. No IAM, route, table, queue or schema moves, and no vendor call in D1 or D2.

**Both branches:**
- V1-a: ULT + IWM Multi-Comp on the fund-free 12.03 file. IWM is admitted, the identity read verifies 1 of 1 on the first read
  with no WAF challenge, and the job reaches READY, which is ULT's first live run. Or a refusal is named and recorded, not
  retried.
- V1-b: an upload-only AAPL+TIMXX run reads `gated=1 features=<token>` (S284 measured), or `matched=1` (the inference was wrong).
  Either result is recorded.
- The two run one at a time under the solo gate, at least 10 minutes apart. A first-read WAF challenge stops traffic.

**Before-read stops:** generate `wjSX3zZo..`, the key's latest `jFLj0wX5..`, root `f89fc8e731-st14`, queue 0/0, the lease empty.

**Not verified by this seat:** the artifacts, the gate, the tests, the plan.

-- 1.0.0_SA_CTO
