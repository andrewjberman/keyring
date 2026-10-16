# Drive log -- 2.0.0_SA_COO~S2 -- 2026-10-16 hours 06Z to 14Z (waiting ticks summarised; substantive findings 11Z to 14Z)

**archetype:** COORDINATE

IRPT_BCKEND, export / routes / serve path. Lease FULL. Fan-out cap 4. No order of this seat is open. The hourly logs for 06Z to 10Z are not separate files: those ticks were dated waits with nothing new on my surfaces (the 05Z log @9eedf12ee9 is the last before this one).

## Findings that changed the plan

| time | finding | where recorded |
|---|---|---|
| 11:41Z to 11:55Z | Hop 1's first scheduled fire (request 356ad20d, 11:41:48Z to 11:46:46Z) logged `FILLED_CATCHUP_LIST_FAILED`, AccessDenied on `s3:ListBucket` of the 49 Financial bucket for `irpt-49f-reporting-gold-role`; `filled_report_values` holds 0 objects (naming-builder prefix, one rail-checked list, KeyCount 0) | row `IRPT_BCKEND-D2-S219` @5d54dcdbb1; `~D2` told by message (pointer only) |
| 12:55Z | `~D2` has the fix in flight: worker 241, TO-DB-b-299, "the filled report-values prefix joins the list pattern" (@52ccabe3aa). Not yet applied per the ledger | none (their cell) |
| 13:55Z | The hop 2 reader `read_filled_report_gold` (reporting-publish/handler.py:496) is a stub that raises `NotYetAvailable`; a test asserts it. `~D2`'s TO-DB-b-298 (publisher 0.4.0) put it live in `irpt-49f-reporting-publish-lambda` (CodeSha `SX0x...`, 13:04Z, Environment null, so the pass is off) | row `D2-S222` @68f1e72ab4 |
| 14:05Z | CTO msg 9438: the stub was deliberate; `~D2` cuts ONE reader cell on that file; the switch stays OFF until its own pair, signed after the reader is deployed and hop 1's write is read | row `D2-S223` @f7354e722b (DISMISSED_WITH_REASON; my first `RESOLVED` was refused by the row gate, not in the ratified enum) |

Row ids: S217 and S218 were minted by another seat while mine was uncommitted; I re-minted before the commit (S219, then S222 and S223 after S220 and S221 were taken). Nothing was ever committed twice.

## What I owe now

- IB-pr-551 deploy legs, narrowed: hop 3 (the report route on `reporting-read`) and hop 4 (the export server, `server_pinned_body`), after hop 1's first `filled_report_values` write exists. STEP 0 re-reads the export role's filled-object grant (pre-read S212: absent). Draft ADDENDUM 1 @95e42dd209 is ready, CTO half to rule `client=*` against reading through the route. Hop 2's leg is gone until the reader is deployed and the switch pair is signed (`~D2` and the CTO).
- `class_series` OBJECTS member in `reporting/entry.py`: waits on `~D2`'s `class_object` v0.4.0 (contract 0.3.3 carries none).
- Debt row `D2-S216` (G7/G8 duplicate admission): at my next touch of either `resolve.py`.

## Ticks

All ticks from 06:55Z to 14:25Z read lease FULL, hop-1 ledger OPEN with L6 unclosed, inbox empty except the messages above, and were recorded with `unblock.py tick` as dated or owed-ledger waits (count 0). Tests re-run at HEAD this session: hop 2 publish 18 passed, hop 4 export 31 passed.

## Compiler Tools

- `comp-find` (content, `--corpus aws`), `comp-kuzu`, `comp-iam service`: answered. The rail denied raw AWS listings twice (R5 AWS-FRESH, R6 pipes); one `# rail-checked:` listing of a single named prefix was used for the gate read. `aws logs filter-log-events` on the named gold function log group read the REPORT line and the failure line.
- Gap: the surprise-row id allocator is per-document read, so two seats appending to one channel collide before commit; the gate caught nothing because both appends were uncommitted. A reserve-id verb would remove it.

-- 2.0.0_SA_COO~S2
