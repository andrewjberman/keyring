# ANDREW-DIRECT 2026-09-13 ~21:3xZ -- "yes 2 all": D14 [LGIC] and D8 +ADVI RATIFIED; a COO lane seated for card 3; FIRMSEP drops cot

**Received at:** the 1.0.0_SA_CTO terminal, in-session, before 21:34:39Z. **Recorded by:** `1.0.0_SA_CTO`, same turn.

## VERBATIM AND ENTIRE

> "yes 2 all"

It answered the three cards below, reproduced exactly as they were put to him. **Each card's REC is now his ruling, in
the words of that REC and no wider.**

## THE CARDS HE ANSWERED -- VERBATIM

```
+-- CALL 1 of 3 ---------------------------------------------------+
  **Ratify D14 = [LGIC] and add ADVI to D8's macro list? (one word covers both)**
  Four projects can't be registered without these: LGIC_CANON, LGIC_NAMING and LGIC_ENFORCE (the three Logic projects), and ADVI_FIRMBKTS (the legacy firm-bucket migration). This is the last blocker at step 0 of the Logic-first order.
  --------------------------------------------------------------------
  **REC --** Yes.
  - LGIC has no prior use anywhere in the repo.
  - ADVI already labels 101 advisor-intelligence projects, so it's the same meaning, not a clash, and the migration fits none of D8's current three.
  - One judgment to know about: the migration also moves gold, state, code and raw data, not only advisor data. I chose ADVI because advisor data is most of what those buckets hold. If you'd rather file bucket work under an infrastructure macro, say so and I'll propose one.
+---------------------------------------------------------------------+

+-- CALL 2 of 3 ---------------------------------------------------+
  **Seat a COO lane to write card 3's task order? (yes / no)**
  Your LD-0521 word makes the COO the only seat that writes task orders. 2.0.0_SA_COO~F is busy with round 5 and the base COO isn't live, so 0.7.0_AE_CloudOps has no one to issue its order.
  --------------------------------------------------------------------
  **REC --** Yes. It's a one-order job, and without it the approved read logging and the 45-day clock both sit still.
+---------------------------------------------------------------------+

+-- CALL 3 of 3 ---------------------------------------------------+
  **Turning on cot read logging also arms the cot branch of the old FIRMSEP alert rule. Which: (a) drop cot from that rule in the same change, (b) rescope or disable the rule, or (c) accept it?**
  Today the rule's texts fail at two broken links, so nothing is sent. If the first link were ever repaired, bd and inf reads alone would send about 250,000 texts a day against a USD 50 monthly cap, and cot would add to that. Also, putting the logging setting into Terraform means importing the whole audit trail first, which is bigger than the card said.
  --------------------------------------------------------------------
  **REC --** (a). It's the smallest change: card 3 stops widening a path that would be dangerous if repaired, and nothing live changes today. Whether the rule itself should exist is a separate question under your alerting moratorium.
+---------------------------------------------------------------------+
```

## WHAT EACH RULING BINDS, AND WHO ACTS

| Card | Ruled | Binds | Actor, state |
|---|---|---|---|
| 1 | **D14 macros = [LGIC] RATIFIED; D8 macros += ADVI RATIFIED** | `org/missions/MACROS.yaml`, on the proposal record `MACRO_ENUM_RULE24_D8_ADVI_D14_LGIC_20260913.md` @`b672b3301c`. ADVI is chosen as a product family on what the buckets predominantly hold; he did NOT ask for an infrastructure macro, so none is minted | `1.0.0_SA_CTO` at L3: the MACROS.yaml flip in the same commit as this record; then registration of `LGIC_CANON`, `LGIC_NAMING`, `LGIC_ENFORCE` (D14) and `ADVI_FIRMBKTS` (D8) |
| 2 | **Seat a 2.0.0_SA_COO lane** to write card 3's task order | One order: card 3's read logging (as ruled ~18:4xZ) with card 3 of this frame's remedy (a) inside it | `0.0.0_AB_MSTR` (spawn authority), on this word. The lane letter is MSTR's to assign. The lane's scope is that one order -- the Tier-2 one-project-per-seat rule protects its context |
| 3 | **(a) -- drop `opal-data-cot` from `FIRMSEP-s3-direct-access-bypass`'s bucket list in the SAME change that turns on cot read logging** | `portal-auth/cloudwatch-alarms.tf:219` (the rule, per 0.7.0_AE_CloudOps 96399). Nothing else about the rule: bd and inf stay in it; the rule is not disabled, rescoped or repaired; its SNS legs stay as they are. **Whether the rule should exist is NOT ruled** -- a separate question under the alerting moratorium | Carried in card 3's order; applied by `0.7.0_AE_CloudOps` under safe-apply with a change-management entry. The order also carries the measured cost: importing the org trail to a 0-diff plan before cot is added |

## WHAT THIS DOES NOT RULE

- An infrastructure-shaped macro for firm-bucket work (not asked for).
- The FIRMSEP rule's future, its broken EventBridge-to-SNS leg, or the SMS leg (LD-0537, 0.0.0_AB_MSTR's).
- NFRA_SUBSTRATECARDING's listing under D11 (flagged to him, not ruled).
- Any project's PRD, decomposition or task orders beyond card 3's one order.
