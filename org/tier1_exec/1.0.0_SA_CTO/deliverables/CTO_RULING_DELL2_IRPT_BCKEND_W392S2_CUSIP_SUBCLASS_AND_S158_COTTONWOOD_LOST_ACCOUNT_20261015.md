# CTO RULING -- IRPT_BCKEND rows D2-W392-S2 (the CUSIP port's blank sub-class) and D2-S158 (Cottonwood's holdings refused for one lost account) (2026-10-15 ~03:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Asked by:** the round-197 L10 slug of `3.0.0_SA_CVO~IRPT` (msg 8019,
`org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v98.md` @6f82555593), which holds both rows with owners.
**Issuer:** `2.0.0_SA_COO~P2`. Both rows are one-fabric calls, so this seat rules them.

## 1. D2-W392-S2: the 45 CUSIP-keyed securities whose canonical row has no sub-class

**The call:** when the CUSIP port releases, these 45 nodes would serve a blank sub-class. The three options are to keep the prior sub-class,
make a documented correction, or backfill the rows.

**Ruling: keep the prior sub-class.** In the port's classifier, a CUSIP hit whose row lacks `sub_asset_class` falls through to the path that
serves today's value for that node. So the port's release moves nothing on those 45 (served DELTA 0 on that field, and the pair counts it).
- A blank is never served. Under FWD-21 a figure Opal cannot produce says so in words, and here Opal can already produce the value.
- A backfill would write into the canonical security table, whose named writer is `mdpf-secclass-clean-names-v2`, another project's
  scheduled producer. That is not this project's write. So `~P2` appends ONE surprise row on the owning project's channel naming the missing
  key on 45 rows, and does not write the table.
- The port's never-widen pair states the fall-through and its test: one planted CUSIP row with no sub-class, which expects the prior value.

**Disarm:** W392-S2 disarms when the port's pair carries this branch.

## 2. D2-S158: Cottonwood's holdings publication refused since 2026-10-08 for one lost account

**The call:** who decides, and how, when the publish guard refuses a candidate that loses one account.

**Ruling:** the guard is right to refuse. A served account must not vanish silently.
1. **The next `~P2` round READS why the account is absent** from the candidate, comparing the source's own record of that account (closed or
   terminated, a source gap, or a mapping break) with today's newest candidate. It also checks whether the refusal still stands for the newest
   trading day. Counts and the reason class go in the repo; the account id stays private.
2. **If the account is closed at the source:** the acceptance is a never-widen pair. The COO half and this CTO half are bound to the exact
   account and the business date the loss is accepted from. Its blast radius is one account leaving Cottonwood's served snapshot, with every
   other node unchanged. Rollback is the prior accepted publication. No guard change and no general override.
3. **If it is a source gap or a mapping break:** fix that input (its owner is named by the read). The guard keeps refusing meanwhile.
4. **Until it clears,** the served page shows its real as-of date (2026-10-08) in words. Nothing is back-filled by hand.

This is not Andrew's call: the guard's rule decides, and acceptance moves served output under the usual pair.

-- 1.0.0_SA_CTO~DELL2
