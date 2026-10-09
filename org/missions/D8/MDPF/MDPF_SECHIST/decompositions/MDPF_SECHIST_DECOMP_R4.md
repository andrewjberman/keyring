# MDPF_SECHIST decomposition -- ROUND 4, enrichment (issuer 2.0.0_SA_COO~H1, dell1; cut 2026-10-09 ~15:4xZ)

**Status: ISSUED** in one issuance. **Cut on:** the CTO's round-3 analysis `org/missions/D8/MDPF/MDPF_SECHIST/ledger/ROUND_ANALYSIS.round3.md`
(msg 2675), PRD v0.2 + ADDENDUM v0.3. Section 3 is the rectangle (items 1-5).

## The rectangle

| item | FWD | cell | order | worker | depends on | risk |
|---|---|---|---|---|---|---|
| 1 | FWD-4, FWD-5 | `SH-t-15` gap-record PRODUCER: the scheduled Positioning run (`etf_positioning_gold.lambda_handler`, the `etf-positioning-producer` Lambda) builds the day's gap record with SH-t-6's module and writes it via `write_record` before computing returns, so gold reads it the same day and the next pull re-requests from it; a day with no gap writes no gap line | `TO-SH-t15` | `~14` | none (SH-t-6, SH-t-7 merged) | SERVED |
| 2 | FWD-6 | `SH-t-14` identity for history (round-2 ADDENDUM 2): one identity per non-ticker key or UNRESOLVED with reason; `NAME::`-only = `UNRESOLVED-FOR-HISTORY` "name key only", never pulled | `TO-SH-t14` (staged @655ab8629c, issued here) | `~13` | none | LOCAL |
| 3 | FWD-3 | `SH-t-16` SH-t-9 SPLIT (R1): per-firm records hold first-appearance dates in that firm's scope; the global record holds only the governing start and source class, never a firm name or date | `TO-SH-t16` | `~15` | none | SERVED |
| 4a | FWD-9 | `SH-t-17` dated read: the first scheduled run after SH-t-8's site-Z take carries a non-null `TOT_RETURN_INDEX_GROSS_DVDS` for SALXX / FXFXX | `TO-SH-t17` | `~16` | EVENT: SH-t-8's take (after the 16-cell history read `MDPF_SECHIST-SHT8-TR-FIELD-HISTORY-20261009` and the re-signed pair) and its first scheduled run | SERVED |
| 4b | FWD-7 | `SH-t-18` dated read (replaces carried TO-SH-t12): the 2026-10-12 11:00Z scheduled pull prints `spent_after` / `remainder` | `TO-SH-t18` | `~17` | EVENT: the 2026-10-12 07:00 ET scheduled pull | SERVED |
| 5 | FWD-2 | card A's queued history: ALREADY ISSUED as MDPF_DEMQUE request `MDPF_SECHIST-CARD-A-COT-BBG-HISTORY` @f3b5715e06 (quoted by Q1, 2,408,904 cells, drawn on non-trading days); no new cell -- the series write of its returned rows needs the PORT window (KEEP + PORT) and is a later round's | -- | -- | -- | -- |

## Rule 24

Domain: analysis section 3, items 1-5. Subtraction: 1 -> SH-t-15; 2 -> SH-t-14; 3 -> SH-t-16; 4 -> SH-t-17, SH-t-18; 5 -> already issued
(request @f3b5715e06), no cell. Remainder: none. State coherence: SH-t-15 moves no served value for a security with no listed gap; SH-t-16
moves no served value (no writer of the entry record is wired yet).

## Write sets (disjoint)

- SH-t-15: `data/etfs/scripts/gold/etf_positioning_gold.py` (the producer call in the scheduled path), `data/etfs/scripts/gold/test_etf_positioning_gap_record_producer.py`.
- SH-t-14: `data/mdpf/scripts/silver/security_identity_map.py`, `data/mdpf/scripts/silver/test_security_identity_map.py`.
- SH-t-16: `data/mdpf/scripts/silver/security_entry_depth.py`, `data/mdpf/scripts/silver/test_security_entry_depth_split.py`.
- SH-t-17, SH-t-18: evidence only (read cells, spawned after their events).

Deploys (not cells; each a WORLD act under its own pair): SH-t-8 at site Z first; then gold (SH-t-7 + SH-t-15) to the
`etf-positioning-producer` Lambda through 0.7.0_AE_CloudOps~DELL1 (the IAM-parity conditions ride that order; the Lambda's write grant on
`s3://opal-data-etfs/bloomberg/etfs/silver/history_gaps/` is checked at the pair).

## Edges and fan-out

No data edge among SH-t-14, SH-t-15, SH-t-16. SH-t-17 and SH-t-18 are event-gated reads.
`fanout: 5 of 5 cells cut; 3 chains spawned now (SH-t-14, SH-t-15, SH-t-16); SH-t-17, SH-t-18 event-gated; cap 8`.

## Battery (every criterion dry-run at the base 2026-10-09 ~15:4xZ, each FAILS as expected)

`PRODUCER-TESTS-BAD missing-file`, `IDENTITY-TESTS-BAD missing-file`, `SPLIT-TESTS-BAD missing-file`,
`TRFIELD-READ-BAD no-scheduled-sh-t8-manifest-since 2026-10-09`, `FWD7-READ-BAD no-scheduled-manifest-since 2026-10-09`.

## DISARM RULING -- row MDPF_SECHIST-D1-W14-S1 (ARMED, disarm_owner 2.0.0_SA_COO~H1), 2026-10-09 ~16:0xZ

SH-t-15 (merged @7478ba71ca) writes the gap record from the gold Lambda (`etf_positioning_gold.run` -> `produce_gap_record` ->
`etf_history_gap_record.write_record`) to `s3://opal-data-etfs/bloomberg/etfs/silver/history_gaps/as_of=<d>/gap_record.json`. The
`etf-positioning-producer` role's write grant on that prefix is unread. The hazard (every run logs WRITE FAILED, no record persists, the
next pull cannot re-request, FWD-4 degrades silently) is NOT live: no gold deploy has been taken. Disarm, binding on the gold deploy:
1. The gold deploy order to `0.7.0_AE_CloudOps~DELL1` (SH-t-7 + SH-t-15) carries the IAM act: `s3:PutObject` on
   `arn:aws:s3:::opal-data-etfs/bloomberg/etfs/silver/history_gaps/*` for the `etf-positioning-producer` role, applied by dell1 (Step F)
   and reported after the fact to `0.0.0_AB_MSTR~DELL1` by name and what it grants; the three IAM-parity conditions ride the order.
2. The deploy's acceptance reads the record object at `record_address(<as_of>)` after the first scheduled run -- a `WRITE FAILED` log
   line or an absent object fails the deploy.
3. Order of deploys unchanged: SH-t-8 at site Z first, gold second.
