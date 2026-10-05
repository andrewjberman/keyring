# ETFS_RIVALS D12 Step B -- never-widen pair, CTO half (flip the IDVZ/PFOE Bloomberg gate; import their 2026 history ONCE, purely additively)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-05 ~19:4xZ. **COO half:**
`deliverables/2.0.0_SA_COO~RV/round9/NEVER_WIDEN_HALF_COO_D12_STEP_B.md` (msg 29763, 61 lines).

**Authority, Andrew-direct:**
- @33ff3bdac0: "we should not touch anything being done on the Positioning pipeline. It should be done purely additively where we do
  one ad hoc targeted backfill in the rivalfunds shape for IDVZ and PFOE, then we add the two funds to the daily incremental pull";
- @4bd948e824: "Backfill is approved for IDVZ/PFOE".

## Read at signing

- **The round-9 deploy is CLOSED** 6/6 @fcf032de53 (page `rv-publish-1005r9`, refused 0, 1,870,715 B). No rivalfunds NEVER-2 entry is
  open.
- **My standing conditions (msgs 29553 thread and 29684), MET BY MEASUREMENT** (fresh mirror, nf-1's code):
  - **(i) The import is SERVED where a live home_producer object exists.** It is named on 09-30 (live revision home_producer, then
    Bloomberg). The census covers 189 of 189 dates.
  - **(ii) Purely additive.**
    - G1: 189 of 189 dates show 0 other-fund deltas, plus 12,798 Bloomberg-sourced IDVZ/PFOE rows.
    - G5: 189 of 189 dates show the other funds VALUE-EQUAL on every pre-existing column, plus 367 trades.
    - The two newer columns (`est_price_source`, `key_resolution`) read null on carried rows and are render-neutral. Byte equality
      cannot hold once the schema gains columns; value equality on every pre-existing column is the mechanism Andrew's "purely
      additively" asks for, and it is met.
- **Positioning is untouched.** Its files are neither written nor read differently by its own producer; rivalfunds stops reading them
  for these two funds.
- **No Bloomberg request:** the import reads the 189 LOCAL Step A captures, so Z-S24 does not bind it.
- **The 3-year cap is met:** 2026-01-02..10-02.
- **The daily join** (about 69 rows a day) runs inside the cb-1 budget guard.

## Conditions

1. **The order as written; stop at the first differing read.** The flip's plan reads 0/5/0 code-only, with its "before" equal to the
   round-9 live set, read back at build time.
2. **The post-act census on the SERVED objects** against the 19:1xZ snapshot. Any other-fund delta beyond the two newer columns is a
   STOP and the rollback per the COO half's table: D12 back to "0", then a canonical replay and a trade-schedule rebuild over
   2026-01-02..10-02.
3. **Timing:** the import chain finishes before the 2026-10-06 07:00 ET (11:00Z) vehicle. If it has not finished by 10:30Z, it pauses
   at a pass boundary and resumes after the vehicle reads OK, so the vehicle's run stays clean.
4. **One NEVER-2 entry** (`etfs-rivalfunds-d12-step-b`), with a named rollback per key. The page republishes once after the census
   reads OK.

**CTO HALF: SIGNED** for D12 Step B under conditions 1-4.
