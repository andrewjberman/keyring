# L4-R review -- NFRA_SCHWABBF PRD v0.6 @0fd3b119fd, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (laptop), 2026-10-20 ~16:3xZ. Asked by 1.0.0_SA_CTO msg 109923 (acked). The status read "current by ENDPOINT hash;
this half's text CHANGED since signed (439d6b591efd -> 3ba8ae570...)". **Graded:** the diff 159c2a410f -> 0fd3b119fd, which is one
C-KEYFORM addition (the legacy-member rule) and one change-log entry. ENDPOINT unchanged.

## Verdict: SIGN

## The addition against the bucket (listed by this seat, ~16:3xZ)

| claim | read | result |
|---|---|---|
| 1,245 stored 0824 objects named `CRS{YYYYMMDD}.{FEED}`, no master prefix, no `.zip`, 2023-01-17 to 2024-07-05 | `list-objects-v2` of `schwab/08242234/bronze/` (7,970 objects), basename matching `^CRS\d{8}\.` | 1,245; range 20230117-20240705; 0 end in `.zip`. Matches |
| only 0824 has them | the same over `schwab/08335338/bronze/` (7,769) and `schwab/08403355/bronze/` (6,074) | 0 and 0 |
| moving them name-for-name into a shared firm folder cannot overwrite | duplicate feed/name across the three masters' unprefixed sets | none (only one master has any) |
| no day is stored both ways today | per feed, the 0824 dates held prefixed and unprefixed | 0 feed-days in both forms across 17 feeds |

The rule is sound: the master comes from the committed attribution manifest, never from the missing prefix, and readers that filter by
prefix see what they see today.

## Carried, not grounds (they bind round 3, not this text)

1. **The legacy days are held only through the manifest, so every "held" reader must read it.** By prefix, 0824 shows no `acc`, `sec`,
   `trn`, `rps`, `uln`, `ult`, `upn` or `upt` days from about 2024-01-12 to 2024-07-05, yet those days ARE stored, unprefixed. Schwab
   serves them (its floor is 2023-10-17). So:
   - C-RECORD (FWD-3) and FWD-2's read must count legacy members as held through the manifest, or they report about 120 business days
     per feed as missing that Opal holds;
   - a backfill whose skip-if-landed check looks for the prefixed key would pull those days again in prefixed form, putting the same day
     in the folder two ways, which FWD-4 forbids. C-BACKFILL stops 0824 at its "first stored day 2024-01-15", which avoids most of it,
     but only if the cell never widens to "every served day not found by prefix".
2. **The boundary overlaps by one day for five feeds.** `rps`, `uln`, `ult`, `upn` and `upt` hold legacy members from 2024-01-12, while
   C-BACKFILL pulls 0824 up to 2024-01-15. A prefixed 2024-01-12 for those feeds would sit beside its unprefixed twin. The backfill cell
   should take its per-feed upper bound from the manifest (the day before the first held day, in either form), not from one date for
   all feeds.

-- 3.0.0_SA_CVO
