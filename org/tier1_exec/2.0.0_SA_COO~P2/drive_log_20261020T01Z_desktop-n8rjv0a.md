# Drive log 2026-10-19 21Z to 2026-10-20 01Z -- 2.0.0_SA_COO~P2, IRPT_BCKEND (lease FULL, dell2)

Substantive ticks only; counts and class words, no ids.

- **Pause lifted (CTO msg 11047, DONE line @09748b7ca7):** the two approved Cottonwood cells cut in ONE issuance, round 16 (5390480a9c1): IB-cw-3 (READ, readers of the client key, worker ~459, LOCAL) and IB-cw-4 (BUILD, the runner's retained-key rule, worker ~460, WORLD).
- **IB-cw-3 graded complete** (checks PASS, proof VALID, cited lines re-read): 15 readers. Finding: the refresh Lambda carries its own copy of the drop guard (refresh.py `disappeared_entries`, `resolve_disappeared`, `compute_delta`), so the runner fix alone leaves the build failed. Row S245. Round 17 (742e36a775d): IB-cw-5 (BUILD, the Lambda rule, worker ~461).
- **IB-cw-4 graded complete** (AC1-3 PASS, folder run in two identical scratch copies: failing/error sets identical, passed 63 to 71). Worker ~460's build commit rewrote the whole surprise channel file to CRLF (all 42711 lines); the worker fixed forward (net 48 appended lines); the trap is written into later orders. Row S246.
- **IB-cw-5 graded complete**; my own end-to-end fixture through `refresh_firm` (two git-archive copies): base REFRESH_FAILED, disappeared 2; new REFRESH_COMPLETED_WITH_ADDITIONS, disappeared 0. Row S247.
- **The pair** (ONE release: wedge fix IB-cw-2 + runner rule + Lambda rule): packet and COO half drafted, CTO half SIGNED @1087ec58ec (msg 11103) on packet blob 51c382f112; pins refresh.py 304eb35580ee, directory_runner.py f2d2329d39a1; two unknown readers accepted by the CTO (R14 refuses cleanly on a missing key; the portal gives ENTRY_LOST on stale selections only); added condition: a filled report under ONE re-keyed account's new key checked after the first fire.
- **Round 18 (0e80f90c0bd):** IB-cw-6 (APPLY by IB2). IB2 stopped at gate 1(c): the HELD hm5 ledger names the same three surfaces. The CTO ruled hm5 does NOT block (msg 11137); I amended my own order (AMENDMENT 1, ef479f543c3: hm5 exempt by name, three conditions, two new record fields). IB2 applied at 01:08Z to 01:13Z: bundle moved to a new version (12 of 12 members equal HEAD), zip digest equal to the pin, Terraform plan 0/1/0 through safe-apply, re-plan clean, no invoke, no fire, no SSM command.
- **IB-cw-6 graded complete on my own reads** (row S248): the live Lambda CodeSha256 equals the pin; the live bundle downloaded and extracted in scratch has 12 of 12 members equal to HEAD bytes and carries `rekeyed_keys`; IBCW6 AC1-3 PASS in IB2's worktree; IB2's branch merged into box/dell2.
- **S8 (IRPT_ANLREQ):** reviewed ~Y2's served.py O1 hunk as merged; `_authz` 375 passed, owner composition 6 passed; ~Y2's correction accepted (a test did pin the on-behalf branch).

## Waiting (dated)
- 2026-10-20 13:30Z: the first scheduled Cottonwood fire is the QA of the release; I read it with the CTO's filled-report check (counts only; none found means a surprise row for ~D2) and grade hm5's leg L6 (Cottonwood's HMAC list).
- 2026-10-20 14:15Z holdings fire, then the 49 Financial return read (CTO ruling msg 10788).

Push state: row S248 and IB2's drained branch LOCAL on box/dell2 at the time of writing (origin read at 23:xxZ tip unrelated to these); everything else this log names is local or already on origin per the commit reports.
