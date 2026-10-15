# ADVI_COTBKF decomposition -- ROUND 87 (issuer 2.0.0_SA_COO~C1 on dell1; drafted 2026-10-15) -- the use_class guard and the better matching

**Status: DRAFT -> ISSUED in one issuance, when round 86 is terminal.**

**Cut on:** (a) `1.0.0_SA_CTO~DELL1` msg 6119, condition C3 of `MDPF_DEMQUE/ledger/NEVER_WIDEN_R9_INACTIVE_YAHOO_CTO_HALF.md`: the `use_class` read in
`commonwealth_price_need.py`, so that a NOT_FOR_ACTIVE Yahoo price never feeds an active account's return; (b) the same seat's msg 6124 =
`ledger/CTO_RULING_DELL1_UNPARK_ACCELERATE_20261015.md` amendment 3 (answers crossbox ORDER `XB-20261015T182453Z-e03b`, research
`deliverables/2.0.0_SA_COO~C1/RESEARCH_20261015_COTTONWOOD_MATCHING_KEYS.copy.md`): R3 custodian-number equality, R4 name-to-household with the inside-household
fingerprint and client-line propagation, and the exact-name review list. Andrew, verbatim (dell2 record `ANDREW_DIRECT_20261015_175xZ_BETTER_MATCHING_CRM_KEY_AND_COLUMN_RUN.md`
@628b6102dc): "No we need to do better at matching. ... im wondering if there could be an intermediary key fashioned from something in there." and "The name is also a very
obvious match mechanism if nobody tried that already to push stuff over the line."
PRD v0.10, no addendum. FWD-9 stands: a link is never guessed. The CRM zip stays unread (open call `dell1-20261015T184344Z-d3cc`, Andrew's).

**Rule 24.** Domain: the two CTO messages. Subtraction from their numbered items: msg 6119 -> CB-ci-1 (the read) and CB-ci-2 (the other readers, so the guard holds beyond
one script); amendment 3 item 1 -> CB-ci-3; item 2 -> CB-ci-4; item 3 -> CB-ci-5; item 4 (CRM zip, mapping file) -> Andrew's, no cell. Uncovered: none inside this project.

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-ci-1` | `commonwealth_price_need.py` reads the Yahoo index's `use_class` the way it reads `porting_verdict`: a `NOT_FOR_ACTIVE` or unreadable class is never `covered` for a holder in the active set | FWD-3 | LOCAL | none (NO_COLUMN is the tested state until the index carries the column) | `0.9.0_WK_ADVI_COTBKF~172` |
| `CB-ci-2` | a READ of every reader that can put a Yahoo-index price into an active account's value or return; file:line and counts, no code change | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~173` |
| `CB-ci-3` | R3: Commonwealth account number equals Black Diamond's custodian `Account Number`; a new standalone module, links to an outside file, yield against the 219 | FWD-8 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~174` |
| `CB-ci-4` | R4: name to a unique Black Diamond household, then the holdings fingerprint inside it within the date window; DETERMINISTIC only on a fingerprint pass, else CANDIDATE; client-line propagation through the same step; positive control on the 471 matched | FWD-8 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~175` |
| `CB-ci-5` | the exact-name 1:1 REVIEW LIST: candidate links with corroboration flags and no PII value, never an automatic link | FWD-8 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~176` |
| `CB-ci-6` | the round-85 build script made deterministic: a total sort key (row order depended on PYTHONHASHSEED, row D1-W169-S4), three runs under three seeds, the V2 residual against the pin stated (round 86's `CB-ch-1`, superseded by this cell) | FWD-3 | LOCAL | CB-ch-1 (merged @3fce5cc614) | `0.9.0_WK_ADVI_COTBKF~169` (continued) |

**Fan-out (to state at the cut):** `6 of 6 chains, cap 8`. No edge: ci-3, ci-4 and ci-5 each carry their own small name and number normaliser and write their own module; ci-1 writes
`commonwealth_price_need.py` and its test only; ci-2 writes only its deliverables folder; ci-6 writes `cotbkf_active_set_v2.py` and its test (a continuation of slot ~169). Disjoint write sets. NOTHING here writes S3 or edits `commonwealth_crosswalk.py`: wiring a new
rule into the SERVED crosswalk is a later act under a never-widen pair, not this round's.

**Yield denominators (the CTO's, fixed here):** 387 unmatched active accounts in `REVERSE_MATCH_V3.csv`, of which 168 are `NEW_CLIENT_AFTER_MIGRATION` (no predecessor exists): the reachable denominator is 219.
