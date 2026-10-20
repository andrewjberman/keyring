# NFRA_OPLGTW -- ROUND-46 ANALYSIS (L10 answer; the round-47 enrichment list)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-20 ~08:3xZ.
**Answers:** `2.0.0_SA_COO~O`'s slug, msg 36178, `deliverables/2.0.0_SA_COO~O/L10_SLUG_ROUND46_DRAFT.md` @345c76a903. Item list:
`deliverables/2.0.0_SA_COO~O/r46/ROUND47_ITEMS_OWED_DRAFT.md`.
**Issuer:** `2.0.0_SA_COO~O`.

## 1. As read

- **11 orders complete, OG-rs-1 SUPERSEDED (MSTR~Z restarted the service), MAY-CLOSE.**
- **Live is `13917ef993` on t4g.large.** Ledger `nfra-oplgtw-gateway-resize-t4g-large` CLOSED at 07:05:52Z.
  - Downtime: 44 s for the resize plus about 16 s for the restart.
  - Limits are 5600M/6400M; 103 tools; 27 of 27 PASS.
- **Alyssa's Schwab grant** covers three masters at their current accounts (OG-mg-2, then OG-ms-2). Andrew's grant is HELD
  under OG-mg-2 option (b).
- **OG-ev-13 HOLDS**, which closes the audit lake leg (Z-S402).
- **The 10-19 17:30Z hang cause is NOT established.** The two large replies completed one at a time on the new host, with
  memory moving about 1 MB. Z-S420 stays ARMED.
- **The GO took 14 minutes to reach `~NFRA1` (06:03Z sent, 06:17Z read)**, inside an essential window. That is a watcher and
  delivery gap for MSTR~Z, not this project's.

## 2. Ruling -- a round-N analysis, no addendum

The ENDPOINT is unchanged. Every item below serves an existing FWD, a carried row, or one of Andrew's recorded words.

### The round-47 list (ONE issuance, cap 8 by your chains), in this rank

1. **D1 (Z-S409):** `fence_kind` rows for orion, eclipse and commonwealth. Proof: one live call per vendor reads PASS. It is
   first because Inflection and Commonwealth have never answered.
2. **The size caps: P4-P7 (Z-S413) plus the three oversize tools of Z-S424.**
   - The 50 KB cap is measured on the bytes actually sent.
   - Trimming never nulls a whole field.
   - The MDPF envelope and `opal_discover` are projected.
   - This is an availability fix as well as a reader fix: until it lands, Z-S420 has no mechanism-level disarm.
3. **The memory guard for concurrent load (Z-S425),** with `target_memory_mib` set to the real 8 GiB in the same release.
   - A run of parallel callers is bounded by the service, never by the courtesy of the callers.
   - Proof: a driven run of N parallel large calls holds /health 200.
   - Z-S420 disarms on items 2 and 3 together.
4. **The Z-S407 mask** (CVO condition C1; you are the disarm owner).
5. **D2 (Z-S410, ARMED: Cottonwood's false zero)** and **D3 (Z-S411)**.
6. **The master-wide Schwab scope resolved at read time, with no stored list** (Andrew-direct ~17:2xZ 10-19, "there shouldnt be a
   persisted list").
   - Then Andrew's own grant moves to it. That retires OG-mg-2's held half and the `email_deny` follow-on together.
   - The `email_deny` handling is ruled in that cell's ask, not ahead of it.
7. **The breakdown handler's `index_pairs` (P1, the handler half)**, so that `2.0.0_SA_COO~MP` can cut the page filter. It
   carries the `mcportal_commit` pin.
8. **Y2 (Z-S422) and Y1/R1/T1 (Z-S423), plus H2 (`news_for_security`)**, as one cell of small fixes.

**Grants after the code, each with its own never-widen** (Andrew-direct ~17:5xZ, @50bd4a33b4):
- Menachem's Schwab grant, in the master-wide shape once item 6 lands, otherwise in the current shape;
- `client_*` for Alyssa and Menachem, after D1-D3 read PASS.

**Also in the issuance, small:**
- the EC2 manifest `machine_type` backfilled to `t4g.large`;
- the `*/silver/*` ListBucket narrowing (item 2 of your list);
- the `admin_people_access` pair, on `2.0.0_SA_COO~MP`'s written yes;
- a row disposing Z-S402 with the OG-ev-13 verdict.

**Not cut:**
- The `audit.py` comment rides the next release that touches `audit.py` (round-45 ruling).
- Andrew's owner-session read of the route is his to do when he chooses, and gates nothing.

**Release discipline:**
- Items 1-5, 7 and 8 batch into ONE or TWO releases, each under its own never-widen ask, inside an off-hours window like the
  OG-rz-2 window.
- No more than two concurrent battery calls on the gateway until item 3 is live.
