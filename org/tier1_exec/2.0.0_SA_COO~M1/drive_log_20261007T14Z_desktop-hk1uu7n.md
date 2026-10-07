# /canonical-drive -- 2.0.0_SA_COO~M1 on dell1 -- 2026-10-07 14Z

Scope: MDPF_SECCLASS (DIRECTED, 10m). Lease FULL each tick.

| tick (UTC) | limb | outcome |
|---|---|---|
| ~14:0xZ | L7 | (1) e58 trace drained 61664c4891 (first failing hop `page`, blob f624ffb58a); CTO (a), no closer (msg 287); e59 amendment 1 @bfab501547 to the portal page hop, slot ~46 (portal, link); e60 re-seated on ~41 |
| ~14:1xZ | L7 | e21 issuer flip gate-refused (layer 1; the override does not lift it), reverted; CTO msg 301: ~S lands it. e60 held as `secclass-r10-held-d04` @24a219520b |
| ~14:1xZ-14:2xZ | L7 -> L8 | (1) e59 drained 4a5b15ee4f with the issuer hookup c0ec00e6 (types.ts + panel; tsc rc=0, 6/6); DRAIN_END_R10 @d9ce041409 READ by 3.0.0_SA_CVO; held-32 merge word given (e42 live, ETag 4092c5b8) |
| ~14:4xZ | L10 -> L6 | (1) round-10 analysis @a856d1525f + PRD v0.15: CLOUD synced cecc5f9013, DECOMP_R11 + ONE issuance 5b7c05382d (fanout 2 of 2): e65 C-CASH-TOKEN (held-34 line), e66 silver union |
| ~14:5xZ | L7 | e65 name-leg scope put to the CTO; narrowed to a 7-phrase whole-name allowlist (msg 346, PRD v0.16); amendment 1 @e2fd242c4a; re-seat drained as `secclass-r11-held-34` @4ac906c5c7 |

Decisions closed this hour:
- The BD thread's one break is the portal page, fixed on candidate `cand-dell1-secclass-e59-r10` (laptop review PASS, 106294). DEV is on Andrew's word.
- A flat order's complete flip belongs to its assignee (CTO 301), never the issuer.
- C-CASH-TOKEN: the ticker leg is `^(BD|F)?CASH(IN|OUT)?$`; the name leg matches only the seven whole-name phrases.
- Round 11 is two cells; every other section-3 item is an issuer act; SC-e-45 and SC-e-46 stay deferred.

Owed:
- the e53 `multi_asset` census (running) to the CTO;
- the E_18 read (BD 23:00Z);
- the e42 L2 read (2026-10-08T12:45Z);
- the CASH_NAME_PHRASES contract field on the round branch.
