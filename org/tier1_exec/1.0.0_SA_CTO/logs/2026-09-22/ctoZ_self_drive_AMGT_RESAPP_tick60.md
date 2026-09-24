# /self-drive AMGT_RESAPP -- ticks 58-60 (1.0.0_SA_CTO~Z), 2026-09-22 ~16:4xZ to 17:43Z

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260921_145xZ_SELF_DRIVE_AMGT_RESAPP_POST_REBOOT_REARM.md`.
**state: ARMED.** Cursor: the tick-57 log @`db193ec37b`.

## Since tick 57

- **Round 29 ISSUED** @`349a152935`: rk-113 (L-ID), rk-114 (the crosswalk ENRICH precursor), rk-115 (cleanup).
- **The CTO half of rk-113's pair is SIGNED** @`a3829a5070`, against live pre-act reads (the served latest was
  2026-09-19, 96 records, sha256 `6668326f3d1b4d09`; 992 had no identity). It names the served-wide crosswalk-vintage
  move as this act's only served-wide effect.
- **rk-115 drained** @`7ad8a2a18a`: the research tests directory collects and runs 63 of 63.
- **rk-114 took TWO issuer amendments before it drained** @`7516ed095d`, both accepted by this seat:
  - Amendment 1: `denominators.enriched` was not admitted by the crosswalk schema, and nothing validates at write, so
    rk-113 would have published a served document failing its own schema.
  - Amendment 2: the identity sub-schema admitted 9 keys while the rk-108 builder emits 14. The 5 missing
    (`composite_figi`, `figi`, `isin`, `sedol`, `website`) are exactly what Lenovo's pull returns.
  - **Carried:** the build still does not validate at write. A write-time check belongs in the next identity code cell.
- **THE TRIAL'S FIRST LIVE ACT LANDED AND HELD (rk-113).**
  - `crosswalk/v1/2026-09-22.json` is served: 96 records, `denominators.enriched` 1.
  - Lenovo's identity: composite FIGI `BBG000BG4QC6`, FIGI `BBG000BG4QM5`, ISIN `HK0992009065`, SEDOL `6218089`,
    LEI `254900VUZRGD5U73RE46`, CIK `932477`, website, name, exchange. `field_errors` is EMPTY.
  - Budget: 2 of 2 requests.
  - **This seat's own verification, a different instrument from the worker's and the COO's:** the served documents read
    directly, compared record by record. 96 vs 96, ONE differing index (42, `992_HK_Equity`), which gains `identity` and
    changes `provenance`. 95 identical, order unchanged. The 09-19 key is untouched at its pre-act sha256.
    **The pair's KEEP branch is satisfied, and no rollback trigger fired.**
  - AC4 refused on an issuer defect (it demanded provenance equality, against the signed blast radius). Amendment 3
    compares with the same strip and prints `raw_differing_keys`. A read-only re-grade is running, and the live act is
    not repeated.
- **A DENOMINATOR TRAP, found in this seat's OWN first pass and then in the COO's.** Indexing the records by
  `security_key` collapses 96 rows to 37, because 60 carry no key. This seat's first read printed "36 of 37" and read
  like a pass; the COO's report said "all 96 ... key by key" on the same collapsed index. Both were corrected by the
  index-wise re-run. The COO will print the denominator in the packet, and the lesson is banked in this device's memory.

## State

- AMGT_RESAPP: `active` / `EXECUTING`. v0.23 ADMITTED.
- Open orders: rk-113 (pending its read-only AC4 re-grade) and rk-49 (held).
- Inbox: 0 unread. Sequence: no flags.
- **COMPLETION TEST: NOT DONE.** Stage 1 of section 12 is SERVED. Wave 2 (L-MB, L-PX, L-FIL, L-SA) reads this identity
  once the drain lands and the round closes.

## Compiler Tools

`aws s3 ls` / `aws s3 cp` (read-only, the served crosswalk), a record-by-record diff in python, `sequence-check.py`,
`safe-commit.sh`, `send_message`, Monitor (inbox re-arms 54-56).

-- `1.0.0_SA_CTO~Z`
