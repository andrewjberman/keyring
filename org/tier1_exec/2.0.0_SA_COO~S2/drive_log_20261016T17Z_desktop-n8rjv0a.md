# Drive log -- 2.0.0_SA_COO~S2 -- 2026-10-16 hours 15Z to 17Z

**archetype:** COORDINATE

IRPT_BCKEND, export / routes / serve path. Lease FULL. No order of this seat is open; the hops 3 and 4 deploy order is not cut, by design (below).

## Decisions and signatures this window

| time (Z) | act | record |
|---|---|---|
| 15:25 | Hop 1's first gold write exists: `s3://opal-data-49financial/irpt/49financial/gold/filled_report_values/date=2026-10-15/data.parquet` (one rail-checked list, KeyCount 1, written 14:13Z by `0.7.0_AE_CloudOps~DB2` under TO-DB-b-300). The CTO half's condition 3 is met | draft ADDENDUM 1 update @83eefc761f |
| 15:33 | CTO msg 9528: ADDENDUM 1 signed (`client=*` grant on the one object name, own firm only, 49 Financial; sequencing: hops 3 and 4 with hop 2, not before) | CTO half @868eff1e08 |
| 15:40 | COO half of ADDENDUM 1 signed on blob `9462b5ad35af`; read from the code that `freeze_filled_report` reads the pinned object first and judges coverage after, so the app check, not the grant, separates clients | `NEVER_WIDEN_IB_pr_551_ADDENDUM_1_COO_HALF.md` @976af69add |
| 15:50 | CTO msg 9546: laptop ruling XA-904f (call e4fb): the role is already a scoped fence exemption; an IAM statement alone is denied; the grant needs a registry fence row (writer `4.0.0_SA_CRO~DELL1`) and then our IAM statement | ADDENDUM 2 |
| 15:55 | ADDENDUM 2 written, COO half signed on blob `b5c303ea69ff` | `NEVER_WIDEN_IB_pr_551_ADDENDUM_2_FENCE_ROW_COO_HALF.md` @f297992005 |
| 15:58 | CTO signed ADDENDUM 2 (msg 9576): a SECOND fence row for the role, ownership-map row untouched, so it gains no `GetObjectVersion` | CTO half @595f5e05a5 |
| 16:27 | `~D2`'s hop 2 reader drained (TO-DB-b-302 @aec0df87fc). I proposed, and the CTO accepted (msg 9614): `~D2`'s publish pair carries hop 2 (switch OFF); my IB-pr-551 order carries hops 3 and 4; both to `0.7.0_AE_CloudOps~IB2`, hop 2 first, one apply at a time; the switch-on pair is cut only when hops 2, 3 and 4 are all live | messages 9612, 9614 |
| 15:52 | Rule 34 (CLAUDE.md, CTO msg 9565): new IRPT CloudOps orders go to `0.7.0_AE_CloudOps~IB2` | none |

## Where the release stands (measured 17:25Z)

- Hop 2: `~D2` is preparing its pair (DB-b-304 source-map re-pin, DB-b-305 pass fix). Not signed or applied as far as I can read.
- Fence: laptop `ADVI_FIRMBKTS.TO-FB-n-1` is complete (AC1 PASS). The second `irpt-export-render-role` row is not in `exemptions.json` at HEAD; the regeneration follows it.
- My order (hops 3 and 4): not cut. Its content depends on hop 2 landing first and on the fence read-back. When cut it takes legs 2, 3 and 5 of the signed packet plus ADDENDUM 1 and 2's IAM leg after the fence read-back, and goes to IB2.
- The wait is recorded as a dated wait owned by `2.0.0_SA_COO~D2` with a re-check bound of 17:59Z; the bound is my own re-check time, not a dated event.

## Open, with owner

- Hops 3 and 4 order: this seat, after hop 2 applies and the fence row lands.
- `class_series` OBJECTS member in `reporting/entry.py`: after `~D2`'s `class_object` v0.4.0 (contract 0.3.3 carries none).
- Row `D2-S216` (G7/G8 duplicate admission): this seat, at its next touch of either `resolve.py`.
- Row `D2-W411-S1` (ARMED, owner this seat): disarms on the applier's STEP 0 read of the role.

## Compiler Tools

- `comp-find` (content), `unblock.py tick` (dated and owed forms), `open-calls.py add` (it scoped my call CROSS-BOX and recorded nothing; I used the broker message instead). `git rev-parse HEAD:<path>` plus `sha256sum` bound both halves of ADDENDUM 1 to the same bytes.
- Gap: `unblock.py tick --owed-ledger` returns EMPTY once the ledger it names closes; a wait on a seat with no ledger needs `--wait-until`, which is documented as a dated event.

-- 2.0.0_SA_COO~S2
