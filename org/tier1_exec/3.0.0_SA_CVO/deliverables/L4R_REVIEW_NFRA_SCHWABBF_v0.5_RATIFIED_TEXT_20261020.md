# L4-R review -- NFRA_SCHWABBF PRD v0.5 @99555e0048, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (laptop), 2026-10-20 ~15:0xZ. Delivered by 1.0.0_SA_CTO msg 109908 (acked). Half hash `439d6b591efd`.
**Graded:** the diff ab4d21cec6 -> 99555e0048. ENDPOINT is byte-identical to v0.4 (FWD-1 to FWD-8, all confirmed by Andrew); CONTRACTS
change in C-SCOPE, C-NAMES and C-ALONGSIDE; one change-log entry.

## Verdict: SIGN

## The v0.4 items, read at 99555e0048

| v0.4 item | v0.5 | result |
|---|---|---|
| 1. C-SCOPE excluded FWD-8's masters | seven masters in two groups: 0824, 0833 and 0840 on the 49F box under `49financial`; the four Cottonwood masters on the Alongside box under `cottonwood`; C-ONBOARD for a master later opened to either login, written by that box alone | cleared; agrees with C-ONEWRITER and FWD-8 |
| 2. C-NAMES printed master scope | "The scope argument is the FIRM of the master"; measured `address('schwab','49financial',...)` and `cottonwood` | cleared; this seat ran the builder for both firms at v0.3 and got the printed paths |
| 3. C-ALONGSIDE IAM by master prefix | `schwab/cottonwood/bronze/*/date=*/<master>.*`, one statement entry per master, never a folder wildcard; the 49F box takes the same shape | cleared; masters stay enumerated |
| 4. silver, meta and `_ops` scope | put to Andrew; C-RECORD (`schwab/<master>/meta/`, :113) and silver stay as written until he answers | the rows now agree by declaration: bronze moves to firm scope, the rest is declared unchanged pending his word. That is the "or" branch of the v0.4 review |

A census of `schwab/<...>/` paths in the file finds one master-scope path, C-RECORD's `meta/` (:113), which item 4 declares.

## Carried, not grounds

1. **Item 4 has no carrier.** The change log says "put to Andrew", but OPEN AT ANDREW does not list it and `open-calls` holds no open
   NFRA_SCHWABBF row. Andrew's question needs a row, or it is a wish, not an ask. If he answers "move them too", C-RECORD, C-MOVE's object
   count, C-EQUAL and C-READERS change, and this half re-signs.
2. **The cutover moves bronze alone until then.** Until Andrew answers, the bucket will hold `schwab/<firm>/bronze/` beside
   `schwab/<master>/{silver,meta,_ops}/`. If he later moves silver, that is a second cutover with its own never-widen pair, not a rider
   on this one.
3. FWD-8's reach depends on the Alongside login's entitlement list, unread until the session exists; C-ALONGSIDE names the branch.

-- 3.0.0_SA_CVO
