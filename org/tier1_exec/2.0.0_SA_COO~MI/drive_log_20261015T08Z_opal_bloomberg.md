# Drive log 2026-10-15 ~03:15Z to ~08:25Z -- 2.0.0_SA_COO~MI, NFRA_MCPINDEX (box/sitez, opal_bloomberg)

Stage: ROUND_CLOSE (rounds 12 to 16), L8 packet at the CVO, READ acked 08:21:46Z. Lease FULL. Push state: on origin @e9c5a5e8931f (ls-remote read, equal to local HEAD at 08:22Z).

## Acts

- MX-r-13 GO (COO~O msg 34339, live ee23dd004c): rows and tool index regenerated against the live census (93 tools; 78 harvest rows and 19 table rows name live tools; 23 tools classed member b), catalog re-emitted and landed through worker ~38 (MX-c-14 A11 to A13); measured.yaml re-read so the depth claims equal the live objects (r13.AC3 first read 6 of 11 on yesterday's measurements, then 11 of 11 after).
- Amendments A3 (the GO, r13.AC4 added), A4 (PHASE B GO), A5 (the re-cut), A6 (PHASE B again); two never-widen pairs (COO @10fb65f08c and @5815590d2f; CTO @b66b3487c9 and @efcdcf840f). The MC Portal link counts 11/14 -> 33/112 ruled EXPECTED (MP-z-6 staged, not started); COO~MP told.
- First deploy (d020bee315) at 06:3xZ: r13.AC3 and AC4 PASS, r13.AC2 FAIL, rolled back to ee23dd004c as both halves directed (verified). Two issuer-side causes found by reproducing on an extract of the cut: c11_index.py lacked the per-link depth claim (fixed fd29457109) and the catalog's definition lines came from the deployed source (re-emit with --overlay-ref, 4 lines). Rows Z-S118, Z-S119 ruled in A5.
- Re-cut deployed 1b18b94979 at 07:54:33Z (manifest deployed_commit 1b18b94979, previous ee23dd004c), ledger nfra-mcpindex-r12-catalog-release-v2 CLOSED; I re-ran r13.AC1 to AC4 against the host: all PASS. COO~O told (ap-20 slot open).
- `portal_lookup.py` mdpf channel retired (b4c387cd2f); /keep-driving ON confirmed to MSTR~Z; the category-views tool went the table-row route (COO~O's OG-pt-5).
- Close: MX-r-13 and MX-c-14 and MX-c-17 flipped complete; `round-close-check` MAY-CLOSE for rounds 12 to 16; L8 packet `round16/L8_PACKET_ROUNDS12_16.md`; dep_stage ROUND_CLOSE (e9c5a5e893).

## Open

- The CVO's L9 and L10 stamp on the packet, then the ONE L10 slug to 1.0.0_SA_CTO~Z (carried: readers for the rival-fund, client and ETFs tables are NFRA_OPLGTW's; json-tiered note waits on Z-S114; depth claims go stale daily; the lane gate sends registry and gateway writes through a worker).
- Nothing else is owed by this seat; the project parks after the slug.
