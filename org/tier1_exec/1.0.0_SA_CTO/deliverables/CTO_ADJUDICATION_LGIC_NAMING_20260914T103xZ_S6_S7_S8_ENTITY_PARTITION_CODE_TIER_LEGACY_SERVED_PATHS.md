# CTO ADJUDICATION -- `LGIC_NAMING` -- three schema rows ruled: the entity partition (S6), the code tier (S7), and legacy served paths kept byte-for-byte (S8)

**Seat:** `1.0.0_SA_CTO` · **Stamp:** 2026-09-14 ~10:3xZ

**Class:** an L4 revision of a project past L2. Andrew confirmed `LGIC_NAMING`'s DONE WHEN lines, so under his 09-03
word this seat rules and the loop keeps cycling.

**Authority:** Andrew-direct 2026-09-03 ~05:2xZ, VERBATIM:

> *"the CTO can run /open-calls on the subject and then CTO adjudicates on the recs and it picks up from there via a
> new (or adjusted) PRD and then runs through the loop from that point."*

## Why now, and why this seat

Three ARMED rows on `LGIC_NAMING`'s channel each name `1.0.0_SA_CTO` as disarm owner, as the author of the PRD and
its data file `org/standards/NAMING_SCHEMA.json`:
- `LGIC_NAMING-S6` @`683b310b49` (this seat);
- `LGIC_NAMING-S7` @`acc5f3782b` (this seat);
- `LGIC_NAMING-S8` @`5d672d3e3a` (`3.0.0_SA_CVO`).

**Each row blocks a D8 PRD's writes:**
- `ADVI_FIRMBKTS` v1.2 holds its entity-keyed served files (S6), its code family (S7), and any rename of a legacy served name (S8).
- `MDPF_CANON` v2.3 holds its code packaging, M6 (S7).

**No round is live.** `LGIC_NAMING` sits at DECOMP. L5 v1 was drained @`40d2b55c62`, and L6 has not been issued: blocking
item (5) holds the lane IDLE on Andrew's call. So a revision now reaches the round before any worker builds the
schema. That is cheaper than an addendum after it.

**What is not touched:**
- The five ruled segments and their order. Andrew ~03:2xZ card 1: *"the five segments and their order are the ruling"*.
- ENDPOINT and CONTRACTS, which are byte-unchanged. The revision edits S1 (the brief half) and the data file only.

## OPEN CALLS -- `LGIC_NAMING` -- 3 calls, adjudicated

```
+-- CALL 1 of 3 -- LGIC_NAMING-S6 --------------------------------------+
  **Does the key's partition slot admit an ENTITY partition, so a file per
  advisor, client or account has a builder form?**
  key.partition lists only `date=YYYY-MM-DD` and "a named leaf". A book per
  advisor needs an entity id AND a file, so key() cannot produce it.
  --------------------------------------------------------------------
  **REC --** (a) admit it: a NEW family uses the hive form `{entity}={id}`;
  the file is the object under it. A LEGACY served family keeps its bare
  `{id}` segment byte-for-byte, because the frozen portal requests
  `platinum/advisors/{id}/summary.json` by path (adviKeyRepoint.ts:37
  @portal 3ade1aba). Doctrine R2 already rules an entity id correct
  inside a partition, so no law moves. (b), refusing and flattening each
  entity into a named leaf, renames every such file behind an edge map
  for no reader's benefit.
  --------------------------------------------------------------------
  RULING -- (a), because it is the form the canon already sanctions (R2),
  it keeps the five segments, and it moves no served byte.
  Vectors:
    new     key("advi","49financial","platinum","advisors","advisor_id=A123")
            = advi/49financial/platinum/advisors/advisor_id=A123
            address(..., object="book.json")
            = s3://opal-data-49financial/advi/49financial/platinum/advisors/advisor_id=A123/book.json
    legacy  key("advi","49financial","platinum","advisors","A123")
            = advi/49financial/platinum/advisors/A123, object summary.json
+---------------------------------------------------------------------+

+-- CALL 2 of 3 -- LGIC_NAMING-S7 --------------------------------------+
  **Where does code live: the schema's code tier, or the canon's root
  code/ home?**
  NAMING_SCHEMA v1.2 lists `code` in key.tier (S1 at v1.2, both halves
  SIGNED). Doctrine R1's non-application list still exempts `code/`
  prefixes, and the D8 brief spells a root `code/{source}/gold/`.
  --------------------------------------------------------------------
  **REC --** (a) the ratified code tier stands:
  `{source}/{scope}/code/{built_tier}/{file}`. The table slot carries the
  tier the code builds (bronze, silver or gold), and the file or bundle
  is a named leaf. Lambda deployment artifacts take the same form: R16
  does not reach them, but R1 still grades their key (doctrine :282-283).
  Doctrine R1's `code/` carve-out narrows to the LEGACY root homes: today's
  `code/{bronze,silver,gold}/` in bd, cot, inf and mdpf, and MDPF's frozen
  rollback objects. They stay until their pipelines move.
  Why: Andrew's source-first ruling says a key "reads the same in the
  monolith, a firm bucket and a product bucket". R16 asks for code
  "beside the gold code", and `{source}/{scope}/code/` sits beside
  `{source}/{scope}/gold/` literally. It is one grammar and one builder.
  (b), the root home, removes `code` from the tier list, needs a second
  builder, and keeps a second grammar alive in every bucket.
  --------------------------------------------------------------------
  RULING -- (a). The carve-out it narrows is canon text, which is
  LGIC_CANON's, so it goes there as row LGIC_CANON-S1 (INERT: every new
  key comes from key(), which reads the schema, not the canon's prose).
  The vectors equal the candidate both D8 PRDs already name:
    ADVI    opal-data-bd/code/gold/<runner>.py
            -> key("advi","49financial","code","gold","<runner>.py")
             = advi/49financial/code/gold/<runner>.py in opal-data-49financial
    MDPF    key("mdpf","global","code","gold","mdpf-accrual-bridge.tar.gz")
             = mdpf/global/code/gold/mdpf-accrual-bridge.tar.gz in opal-data-mdpf
            (the gold Lambda zip likewise, keeping its source-map tie)
+---------------------------------------------------------------------+

+-- CALL 3 of 3 -- LGIC_NAMING-S8 --------------------------------------+
  **Does a legacy served file keep its name byte-for-byte, or is it
  renamed to kebab-case behind a per-leaf edge mapping?**
  key.table_case says a platinum leaf is kebab-case. 12 of 15 ADVI served
  leaves are snake_case (3.0.0_SA_CVO's read), and the frozen portal
  requests them by name.
  --------------------------------------------------------------------
  **REC --** (a) admit them. Below `{source}/{scope}/platinum/`, a LEGACY
  served path keeps its bytes: the table, a bare entity-id segment, and
  the file name. Kebab-case binds NEW served names only. (b) puts new edge
  logic on every served key, each under its own never-widen sign-off, to
  change a name no reader sees.
  --------------------------------------------------------------------
  RULING -- (a). This is the rule both D8 PRDs already follow (ADVI_FIRMBKTS
  v1.2's key row, SIGNED by 3.0.0_SA_CVO @e6f372e796). It is the same
  principle as call 1's legacy arm, so one data field carries both.
+---------------------------------------------------------------------+
```

## What this changes, and where

| surface | change | half / owner |
|---|---|---|
| `org/standards/NAMING_SCHEMA.json` v1.2 -> v1.3 | `key.partition` gains the entity partition. `key.table_case` bounds kebab-case to NEW served leaves. New fields: `key.legacy_served_path` (calls 1 and 3) and `key.code` (call 2). The changelog records this ruling | the data file; `LGIC_NAMING` is its author |
| `LGIC_NAMING_PRD.md` v1.2 -> v1.3, S1 | S1 cites the three data fields; ENDPOINT and CONTRACTS are byte-unchanged | the brief half re-opens (`4.0.0_SA_CRO`); the ratified-text half carries |
| `LGIC_NAMING` tree row | phase, blocking (1) and lineage | this seat |
| `LGIC_CANON-S1` | doctrine R1's `code/` non-application narrowed to legacy root homes; INERT | LGIC_CANON's next canon edit |
| L5 decomposition v1 | re-read against v1.3 by `2.0.0_SA_COO~G` before any L6 issuance. The worked cases that grade keys (N2) and the namer exercises that read the data file are the likely touches | `2.0.0_SA_COO~G` |

**What this does not do:**
- It does not lift `ADVI_FIRMBKTS`'s or `MDPF_CANON`'s holds by itself. They lift when v1.3 is ADMITTED and `LGIC_ENFORCE`'s builders read it.
- It does not re-open any D8 PRD. Their stated candidate vectors already equal the ruled forms.
- It does not touch the portal, and it moves no served byte.
