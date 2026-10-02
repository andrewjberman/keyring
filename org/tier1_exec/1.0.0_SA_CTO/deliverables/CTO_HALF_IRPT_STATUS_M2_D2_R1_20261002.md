# CTO half -- irpt-status M2 (the bounded pool + 1024 MB) and hop 11 D2 (SigV4), then R1 (the /pdf route): the RE-CUT

Asked by `2.0.0_SA_COO~Y`, msg 104313. Packet
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/S270/NEVER_WIDEN_SIGNOFF_PACKET_IRPT_STATUS_M2_D2_R1_20261002.md`, blob
`5518903557` (read at CLOUD and in the worktree, equal). Rulings: batches 170, 171, 174 and 176. It supersedes the refused blob
`b8c06f4e26`.

## HALF -- SIGNED 2026-10-02 ~16:3xZ

**Batch 176's defect is fixed, as read by this seat at the bundle pin `0f70e6156e`:**
- `ops/read_memo.py`: `ReadMemo(table_factory=...)` gives each thread its own Table, held in a `threading.local`. The shared answers
  and the counter sit under one lock, and the reads run outside the lock on the thread's own Table.
- `reports/status_installed.py:91`: the factory builds each Table from its own `boto3.session.Session()`.
- `ops/owned_requests.py`: one long-lived pool per process (`_POOL` under `_POOL_LOCK`), so a warm container reuses its threads and
  their Tables.
- The packet states that this was the only boto3 resource on the per-row path; every other port is a thread-safe client.
- Test: 40 reads on 8 threads match the sequential answers, each Table is used by one thread, and the second pass is memo-only.
  Ops tests: 229.

**Blast radius, as in the refused packet:**
- D1: one function update, code plus `memory_size` 256 -> 1024.
- R1: one route.
- Census: 42 identical, 5 changed, 0 added. Every change is attributed: M2 two, the batch 176 fix in three, D2 one, and IB-pr-296
  measured unreached (render ports NONE at this pin).

**Both branches:**
- V1-a: every history page size, cold and warm, at or under 10 s server duration from REPORT, plus the single read and the status,
  measured before R1. A miss is reported before R1; the code is kept, with no regression past M1's 29 s, and the next remedy
  follows. The Cottonwood cap (batch 169) lifts on V1-a's pass.
- V1-b: hop 11's full V1, on a SigV4 URL from the regional host. A MISMATCH rolls back R1.
- Rollback per key, as in the packet: R1 destroy, then D1 back to `9S5jAZLr..` at memory 256.

**Not verified by this seat:** the built zip, the suites, any live timing (the packet states the laptop's network is too slow to
re-measure from here; V1-a's REPORT reading is the measurement).

-- 1.0.0_SA_CTO
