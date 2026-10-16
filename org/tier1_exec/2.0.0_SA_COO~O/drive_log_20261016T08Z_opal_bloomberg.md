# Drive log -- 2.0.0_SA_COO~O, NFRA_OPLGTW round 37 (EXECUTING), 2026-10-16 06:30Z to 08:00Z (site Z)

Continues `drive_log_20261016T06Z_opal_bloomberg.md`. Finish-by Fri 2026-10-16 ~22:00Z. Commits LOCAL on `box/sitez` unless box-sync pushed them.

## Done this stretch

| act | result |
|---|---|
| `OG-ap-26` (the classification grant moves to the internal reader role) | three halves signed, applied by `~ZS` `d2e1fd6cef`, ledger CLOSED; my re-run of `ap26.AC2` PASS; proof instance and status complete |
| `OG-ap-23` re-issued ask on A3/A4 (release `56c0f8ce1d`) | COO half signed `1f8cc4d17b`; CTO half REFUSED (the tar line never put the staged `app/refs` copies in the archive); CVO half REFUSED (the five `client_*` tools were in `NATIVE_TOOLS`, against ratified PRD v3.1 Ruling 2; row Z-S162) |
| Amendments of `OG-ap-23` | A5 (tar line + member census), A6 (served `client_admission` negative arm), A7 (`data_entitlement.py` taken WHOLE: the live base lacks OG-bd-3's `decide()` branch; supersedes `OG-ap-17` on landing) |
| `OG-ad-1` (the five client tools are DATA_GRANT and TIER_ADMITTED, master_admin only) | cut `a577362790`; A1 `6220baa7bb` (pins of the old NATIVE membership in two entitlement test files follow the truth); merged `23587956e9`; AC1 and AC2 PASS |
| Full gateway suite on the merged trunk `23587956e9` | 1014 passed, 61 failed, the SAME 61 failing ids as clean trunk `474b9770d5` (0 new, 0 fixed) |
| MI's table-to-tool link file (31 links) | CONFIRMED against the adapters, 0 corrections (call graph; SmartX by its `T_*` constants) |
| `~Z`'s single re-cut GO | `trunk_sha` `23587956e9`, `mcportal_sha` `090b9cdc85`; release record now names `release_sha` `3d5c9c8bf1dea0854c9b59d58b83fdf9dcb480e4` |

## Rulings and notes

- **My error, stated plainly:** my hookups placed the five client tools in `NATIVE_TOOLS` by the default pattern, and I signed the COO half of `OG-ap-23` without reading PRD v3.1 Ruling 2. The CVO's refusal caught it. The class of a data tool is chosen at its hookup; a build order for a data tool names its admission class on the face (to carry into the next cut).
- **MI's split suggestion** (ship the 22 tools without the five client ones): declined. The CTO's PRD v3.14 ruled all 27 ship, client tools master_admin only; the tool names do not change, only who may call them.
- **Muse cell** folded into this project by Andrew (verbatim in the draft); scope narrowed ~07:0xZ to the M365 mail and Teams tools (read and send) plus `whoami`; after the 22:00Z finish; draft `DRAFT_NOT_ISSUED_TO-OG-mu-1_muse_narrowed_client.md` committed.
- The CTO's `ruling_ref` backfill and the gate check cells stay drafted and held until `OG-ap-23` has released.

## Open

`OG-ap-23`: `~Z`'s re-issued ask on the new release, then my re-sign, the CTO and CVO halves, the Phase B GO. Then: the `ruling_ref` cells, the muse cell, the gf-1 artifact pins (row Z-W111-S15), the pending-order reconciliation (`OG-ap-17` superseded by `OG-ap-23`; `OG-mg-1`, `OG-cp-1`, `OG-cp-2`), Z-S160, and the round-close check (the five ungraded judgment criteria are the CVO's).

## Traps met

- A worker's AC that passes in its sparse tree can fail in the main tree and the reverse (the gate's live-read client; a suite order effect): re-run in the main tree before ruling.
- A change of an admission class moves pins in suites outside the cell's grant (a registered-name union and three guard tests): name them in the order or the cell stops at AC2.
- Pre-reading a worker's diff against the LIVE base (not trunk) found a second file-level dependency (OG-bd-3) that a by-hunk take would have left out.

## Compiler Tools

`comp-surprise`, `round-close-check.py --round 37` (earlier, REFUSED, 2 proof-bad), `comp-iam stats`, the call-graph read of the adapters (a small python AST script in the session scratchpad; no comp-tool answers table-to-tool). Gap: no tool shows which pins a set-membership change moves across the test suites.
