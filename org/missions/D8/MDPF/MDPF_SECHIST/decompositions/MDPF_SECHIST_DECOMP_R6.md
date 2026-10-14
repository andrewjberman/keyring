# MDPF_SECHIST decomposition -- ROUND 6, the one item the park keeps (issuer 2.0.0_SA_COO~H1, dell1; cut 2026-10-14 ~13:2xZ)

**Status: ISSUED** in one issuance. **Cut on:** the CTO's round-5 analysis `org/missions/D8/MDPF/MDPF_SECHIST/ledger/ROUND_ANALYSIS.round5.md`,
ADDENDUM 1 (2026-10-14 ~13:1xZ, @fa26b50ebc) as corrected @f443ae70d2 (CTO msgs 5540, 5542, 5553). The park (section 2 of that analysis) allows this one item.

## The rectangle

| item | FWD | cell | order | worker | depends on | risk |
|---|---|---|---|---|---|---|
| 1 | FWD-9 | `SH-t-23` QA replay of the deployed money-market rule, in memory, no served write: arms (b) control equals the served page at each book's own as_of, (a) SALXX and FXFXX blanked on D -> every window blank, a non-money-market ticker unchanged, (a2) a later row fills D -> windows equal the control, (c) an absent fund -> all-null recorded as-is | `TO-SH-t23` | `~22` | none | LOCAL |
| 1b | FWD-9 | `SH-t-24` closed-market frontier (CTO ADDENDUM 2 @d3206f14a8, msg 5564, added 2026-10-14 ~14:0xZ beside SH-t-23): `frontier_returns` in the gold script (carry the last vendor day with its date; bound 4 calendar days; `absent_count` 0; a NULL reading still blank), the holding column `return_frontier`, the publisher's optional keys `returns_frontier` / `returns_frontier_holdings`, one offline test file | `TO-SH-t24` | `~23` | none (the deploy that moves served returns is a separate act under its own never-widen pair) | SERVED |
| 2 | FWD-9 | NOT A CELL: the served week read, Fri 2026-10-16 through Mon 2026-10-19 plus the run after Monday, by this seat; and the organic blank-then-fill pair for FXFXX 2026-10-12 (listed in the 10-14 pull, requested ~2026-10-15 11:07Z) | this seat's reads | -- | EVENT: the scheduled runs | LOCAL |

## Corrections carried into the cell (read before the cut)

- The ADDENDUM's arms (a) and (c) as first written contradicted PRD C-MMF and `compute_returns`; the CTO corrected them (msg 5542). The arms above are the corrected ones.
- The null arm also occurred ORGANICALLY on D = 2026-10-12 (bbg/2026-10-12: FXFXX null, SALXX absent because the bond market was closed, Columbus Day, CTO msg 5553). The served page of 2026-10-14 13:01Z is blank for exactly those. The cell replays D = 2026-10-13 (the as_of whose input holds both funds) so that arm (a) blanks a day that has a value, which the organic day cannot show.
- The output sink is a local JSON file, not a QA S3 prefix: a new S3 address is a naming-registry matter (CLAUDE.md rule 30) and a local sink is strictly narrower than the prefix the ruling allowed.

## Rule 24

Domain: ADDENDUM 1 items 1 and 2, and ADDENDUM 2's one cell. Subtraction: 1 -> SH-t-23; 1b -> SH-t-24; 2 -> this seat's scheduled reads (not a cell). Remainder: none. State coherence: SH-t-23 reads S3
through a client that refuses every call but get_object / list_objects_v2 / head_object and moves no served value; the served prefix listing is equal before and after.

## Write sets

- SH-t-23: its own deliverables folder only (`replay_out.json`, the proof-of-spec instance). The check script is the issuer's, committed with the issuance, not edited by the worker.
- SH-t-24: `data/etfs/scripts/gold/etf_positioning_gold.py`, `data/etfs/scripts/gold/etf_positioning_publisher.py`, `data/etfs/scripts/gold/test_etf_positioning_closed_market_frontier.py`, its own deliverables folder. SH-t-23 and SH-t-24 share no file.

## Amendment note

SH-t-24 was added to round 6 by the CTO's ADDENDUM 2 (msg 5564) ~25 minutes after the round-6 issuance @d9d059035a, in a second commit by the same issuer, as its own WORKSTREAM `CLOSEDMKT` (rule 27: a workstream is a scope, not a round; the TO issuance gate keys one issuance per round and admits a second workstream through `<workstream>`). The two workstreams have disjoint write surfaces (SH-t-23: its deliverables folder; SH-t-24: the gold script, the publisher, one new test file). SH-t-23's worker was already running and is not touched.
