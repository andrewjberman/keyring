# CARRIED CRITERION -- the EXPIRED rule, for the FIRST AMGT_RESAPP cell that reads `packs/<key>/status.json`

**Carried by:** `2.0.0_SA_COO~R1` (this project's issuer), 2026-10-12, on the ask of `2.0.0_SA_COO~W1` (AMGT_HARVST), msg 4507, which cites `1.0.0_SA_CTO~DELL1` msg 4505 (YAGNI: no reader
exists, so no cell is cut for it now). **Nothing is owed before such a cell exists.**

**The criterion, with its three arms** (to be written into the first order whose cell reads a research pull's `status.json` for display or for a decision):

1. a REQUESTED status OLDER than the pull queue's one-day retention reads EXPIRED, computed AT READ TIME (no new writer, no sweeper, no alarm: the standing moratorium holds);
2. a REQUESTED status younger than that reads REQUESTED;
3. a LANDED status is unchanged.

**The rule, the finding and the specimen** (SAP GY Equity, REQUESTED 2026-10-12T16:43Z, expiring about 16:43Z on 2026-10-13):
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round82/CARRIED_EXPIRED_RULE_FOR_THE_FIRST_PULL_STATUS_READER.md`.

**How the issuer applies it:** at the cut of any order whose face names `packs/` and `status.json`, the issuer greps this ledger directory for this file (its name carries the trigger) and copies the
three arms into the order's `<proof_of_spec>` as ONE criterion with a difference-control arm per the dispatch skill (a younger REQUESTED and a LANDED read unchanged, an old REQUESTED reads EXPIRED),
dry-run at the base before the cut. A current reader of `status.json` in this module: none at round 101 (read: the request path lists `packs/*/input_ledger.json`, never `status.json`).
