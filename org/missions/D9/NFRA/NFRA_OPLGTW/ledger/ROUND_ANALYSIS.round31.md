# NFRA_OPLGTW -- ROUNDS 30-31 ANALYSIS (L10)

**Author:** `1.0.0_SA_CTO~O`, 2026-10-08 ~19:2xZ. The pen passed from `1.0.0_SA_CTO~Z` at the round-31 analysis (msg 31931).
**Slug:** `3.0.0_SA_CVO~Z` msg 31960, `surprise-channel/adjudications/ADJUDICATION_v22.Z.md` @6582de6869, read whole.
**Terminal notice:** `2.0.0_SA_COO~O` msg 31949.

## 1. What the two rounds did

- Live stays r28 `aa75078e1b`. Nothing was released.
- Round 30: OG-dr-1 complete on `wk-NFRA_OPLGTW-30-35` @47dd5053b2, NOT drained (ruling msg 31464).
- Round 31: OG-md-1 (C7 domain admission, PRD v1.9) complete and drained @a2c6b9cc65; md1.AC1 7 of 7, md1.AC2 23 of 23 on
  the issuer's re-grade. The domain file ships empty.
- Two `.env`-count floor tests in `tests/test_schwab_host_inputs.py` read 52 and 19 against 51 and 18; they move with the
  release (issuer's note).
- Rows: Z-S67 ARMED. Z-W35-S1 (ARMED) was stranded on the undrained branch; this seat landed the channel file alone on
  CLOUD @690eb2c255 (26 lines added, 0 removed, the row unchanged; audited row-gate override) so it is dispositioned here.

## 2. Inputs since round 29 that this analysis carries

- **Andrew's four gateway Schwab answers** (2026-10-08 ~17:4xZ, record
  `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261008_174xZ_GATEWAY_SCHWAB_FOUR_CALLS_ANSWERED.md` @116d52009d),
  on `4.0.0_SA_CRO~Z`'s assessment @139c8d018e. Carried into the PRD as the v2.0 addendum (R53).
- **Andrew's yes to the one-session move for `opal-gateway-bbg`** (2026-10-08 ~17:4xZ, record
  `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261008_174xZ_OPEN_CALLS_BOTH_YES_PULL_PUSH_AND_GATEWAY_MOVE.md`
  item 2): the prepared move is applied, then he signs in once in the Bloomberg seat's window. That is Z-S67's remedy.
- **Row NFRA_OPALAI-Z-S62** (this seat, @a81c2dcfd8): `opal_asker_query` refused `write_class_denied` to master_admin on
  the LIVE gateway (one probe with bogus ids; the gate answers before the handler).

## 3. Rulings

| # | row / input | ruling | why |
|---|---|---|---|
| R50 | Z-W35-S1 (ARMED): the refresh handler answers 503 at its 30 s budget while the rotation still commits | **The budget governs the START of the rotation, not its answer.** Once the conditional transaction that consumes generation N is sent, the handler awaits its result and answers it, even past 30 s. Before it is sent, a deadline answers 503 and generation N is untouched. One build cell, round 32, in `app/server.py` / `app/oauth_as.py`, two tests: a transaction slowed past 30 s returns the new pair and the family is NOT revoked; a deadline hit before the transaction returns 503 and the stored generation is unchanged. C1's sentence changes with it (v2.0, item 6). The same rule applies to authorization-code redemption (`server.py:681`, the same `_within_budget` shape over a single-use consume). Read by this seat: `server.py:367-382` runs the whole exchange inside `asyncio.wait_for` and answers 503 on timeout while the pool thread continues. | Answering 503 after the rotation commits hands the client a token the server has already retired; its correct retry is then treated as reuse and revokes the family. No restart is needed. This is a defect whatever caused 21:49. |
| R51 | OG-dr-1 | **Closed, not drained.** The branch stays for reference; its order stays `complete` with this pointer. | Z-W35-S1's own journal read: the 21:49 stop was already a graceful SIGTERM that drained in about 1 s. The drain bound adds nothing a normal stop lacked. |
| R52 | R48 (no grace for a previous generation) | **Stands.** The 21:49Z audit-lake read the row names (status and latency per refresh, no identifiers) is NOT required now: R50 closes the server-side route, and Andrew's one-session move closes the client-side one. | Each remedy is decided without it. |
| R53 | Andrew's four answers | Written into the PRD as **v2.0** (ENDPOINT and CONTRACTS change; both halves re-open). | His word; the shapes and acceptance are this seat's. |
| R54 | NFRA_OPALAI-Z-S62 (ARMED) | **`opal_asker_query` joins `SAFE_TOOLS`** (it reads a Teams message and a catalog answer; it writes nothing). The cell also prints the census of every tool `tools.py` registers that is in none of `SAFE_TOOLS`, `DESTRUCTIVE_OPS`, `TOOL_WRITE_CLASS`, with its denominator; any other member found is a row, not a silent add. One test calls the tool through `_run` as a scoped identity and is NOT `write_class_denied`. | The live gate refuses every tier. Alyssa's close run calls it. |
| R55 | release r29 | **One release carries:** OG-md-1, R54, R50. Release form as r28's, plus: the domain table's entries listed beside their parties (v1.9); the two floor tests updated in the release's own diff; the re-authentication named per R49. **Not before** the `opal-gateway-bbg` one-session move is applied and Andrew has signed in, and not inside the 12 hours before a 07:00 America/New_York send (R49 stands until Z-S67 reads DISARMED). | R49's terms, and Z-S67's remedy is now decided. |

**Z-S67** stays ARMED with `disarm_owner` `2.0.0_SA_COO~O`; it disarms on the first gateway deploy after the move whose
release form reads 0 revoked families for the concierge. **Z-W35-S1** stays ARMED until R50 is live.

## 4. ENRICHMENT LIST -- round 32 (one issuance by `2.0.0_SA_COO~O`, on PRD v2.0)

1. R54: `opal_asker_query` into `SAFE_TOOLS`, the census, the test through `_run`.
2. R50: the refresh rotation answers once sent; its two tests.
3. **G5, read only:** one `-Mode enumerate` run of `sdd-daily-pull.ps1` for master `08403355` on the Schwab box (Andrew's yes),
   outside the 30-minute window of either daily pull (box-wide session lock), with a positive control: the same window
   enumerated for `08335338`. The order adds `08403355` to the `-Master` set on its own branch only to make the call; nothing
   lands in S3, nothing is scheduled. The record: files per type and the vendor filename grammar for both masters, side by side.
4. **G1-G3 measurement, read only (parquet footers, no row content):** the exact column list of `fact_acc`, `fact_uln`,
   `fact_ult`, `fact_rld`, `fact_rly`, `fact_rty` and `fact_trn` for both masters at the newest partition, and the oldest and
   newest qualified completion marker per master. These lists are what v2.0's contract additions are written from.
5. **G2 closure census:** for each master, the dates in the last 13 months that have a silver partition and NO qualified
   completion marker. 08335338 holds 27 markers, 2026-08-31 to 2026-10-07 (read today), so 13 months of history needs the
   producer's metadata backfill (C3); this item sizes it and changes nothing.
6. Release r29 (R55), after items 1 and 2 drain, on the release form.

Items 3-5 decide v2.0's build round; the build of G1-G4 is round 33's, cut from this list's records.

## 4a. AMENDMENT before issuance (2026-10-08 ~21:3xZ): FWD-12 and FWD-13 are built IN round 32

Cause: Andrew-direct ~21:2xZ, "asap" on Alyssa's 13-month access and on the Tax SMA master tested, added to the daily pull and
served on the gateway (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_212xZ_ALYSSA_13M_AND_TAX_SMA_MASTER_ASAP.md`).
Round 32 was not yet issued; this section replaces section 4's last sentence for those two outcomes only.

- **7. FWD-13 build, chained on item 3.** When item 3's record shows `08403355` returns files in the same shape as `08335338`
  (the same file types, the same vendor filename grammar, a clean silver conversion of one day), the same round adds `08403355`
  to the daily pull's `-Master` set and to the gateway catalog as a separate master. Andrew's 17:4xZ answer 1 already rules the
  add on that condition; no further word is needed. The add is a scheduled-producer change: a NEVER-2 ledger entry and the
  never-widen sign-off (CTO+COO, blast radius = the new master's keys only) before it lands. If item 3 returns no files, item 7
  stops and the outcome reports that.
- **8. FWD-12 build, chained on item 5.** Item 5 sizes the completion-marker gap; item 8 then backfills the producer's
  completion metadata (C3) for every date in the 13 months that has a silver partition, for both existing masters (and
  `08403355` once item 7 lands), and sets the grant reach to 13 months. A date with no proven-complete source stays
  unavailable, never guessed.
- **Unchanged:** items 1, 2, 4 and 6. Alyssa's sitting still waits on release r29, which waits on Andrew's `opal-gateway-bbg`
  sign-in (section 5). G1, G3 and G4 (identity columns, lots) stay round 33's: "asap" named only the 13 months and the master.
- Fan-out is the COO's, derived from the two chains (3 -> 7, 5 -> 8) beside items 1, 2 and 4.

## 5. ACTS ONLY ANDREW CAN DO (cited)

- The `opal-gateway-bbg` sign-in after the move (his Microsoft login; record @ item 2 above). Release r29 waits on it.

-- 1.0.0_SA_CTO~O
