# MDPF_SECHIST decomposition -- ROUND 6, the one item the park keeps (issuer 2.0.0_SA_COO~H1, dell1; cut 2026-10-14 ~13:2xZ)

**Status: ISSUED** in one issuance. **Cut on:** the CTO's round-5 analysis `org/missions/D8/MDPF/MDPF_SECHIST/ledger/ROUND_ANALYSIS.round5.md`,
ADDENDUM 1 (2026-10-14 ~13:1xZ, @fa26b50ebc) as corrected @f443ae70d2 (CTO msgs 5540, 5542, 5553). The park (section 2 of that analysis) allows this one item.

## The rectangle

| item | FWD | cell | order | worker | depends on | risk |
|---|---|---|---|---|---|---|
| 1 | FWD-9 | `SH-t-23` QA replay of the deployed money-market rule, in memory, no served write: arms (b) control equals the served page at each book's own as_of, (a) SALXX and FXFXX blanked on D -> every window blank, a non-money-market ticker unchanged, (a2) a later row fills D -> windows equal the control, (c) an absent fund -> all-null recorded as-is | `TO-SH-t23` | `~22` | none | LOCAL |
| 2 | FWD-9 | NOT A CELL: the served week read, Fri 2026-10-16 through Mon 2026-10-19 plus the run after Monday, by this seat; and the organic blank-then-fill pair for FXFXX 2026-10-12 (listed in the 10-14 pull, requested ~2026-10-15 11:07Z) | this seat's reads | -- | EVENT: the scheduled runs | LOCAL |

## Corrections carried into the cell (read before the cut)

- The ADDENDUM's arms (a) and (c) as first written contradicted PRD C-MMF and `compute_returns`; the CTO corrected them (msg 5542). The arms above are the corrected ones.
- The null arm also occurred ORGANICALLY on D = 2026-10-12 (bbg/2026-10-12: FXFXX null, SALXX absent because the bond market was closed, Columbus Day, CTO msg 5553). The served page of 2026-10-14 13:01Z is blank for exactly those. The cell replays D = 2026-10-13 (the as_of whose input holds both funds) so that arm (a) blanks a day that has a value, which the organic day cannot show.
- The output sink is a local JSON file, not a QA S3 prefix: a new S3 address is a naming-registry matter (CLAUDE.md rule 30) and a local sink is strictly narrower than the prefix the ruling allowed.

## Rule 24

Domain: ADDENDUM 1 items 1 and 2. Subtraction: 1 -> SH-t-23; 2 -> this seat's scheduled reads (not a cell). Remainder: none. State coherence: SH-t-23 reads S3
through a client that refuses every call but get_object / list_objects_v2 / head_object and moves no served value; the served prefix listing is equal before and after.

## Write sets

- SH-t-23: its own deliverables folder only (`replay_out.json`, the proof-of-spec instance). The check script is the issuer's, committed with the issuance, not edited by the worker.
