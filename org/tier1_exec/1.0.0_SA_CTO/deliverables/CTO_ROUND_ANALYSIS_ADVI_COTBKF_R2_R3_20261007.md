# ROUND ANALYSIS -- ADVI_COTBKF rounds 2-3 (L10)

**Author:** `1.0.0_SA_CTO`, 2026-10-07 ~03:4xZ. **On:** the CVO's slug, grade file
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUNDS_2_3_L9_GRADE_20261007.md` @c4b54a904b (11 orders terminal, 19 rows dispositioned,
0 ARMED; CB2b3-AC3 NOT MET; CB3c3-AC3 and CB3c4-AC3 MET).

## Rulings on the five items

1. **Cross-firm market prices (row W6-S2; CB2b3-AC3).** A closing price is public, but the table that holds it is not: `opal-data-49financial`
   `canonical_positions` is another firm's positions, and a Cottonwood pipeline does not read it, for prices or anything else (CLAUDE.md
   section 5, bucket or key-prefix). The same holds for the bd and inf stores. The census is re-run to be COMPLETE and to grade each store:
   USABLE (Cottonwood's own, or a store with no firm in its address) or BARRED (another firm's), with the missed 49 Financial table listed as
   BARRED. Prices for C-DAILY come from the two sources Andrew approved (Yahoo Finance; Bloomberg at site Z) and land once per security in
   the securities history MDPF_SECHIST owns, where no firm is in the address.
2. **A legacy store's address read from a record file under `org/` (row W6-S5).** Not allowed as the source. Rule 30 binds a NEW script: an
   address it reads is builder output, or, for a store that predates the canon, one row in `infra/logic/registry/` naming that legacy
   address (a registry row through its owner, `4.0.0_SA_CRO`). A deliverable under `org/` is evidence, never a configuration source.
3. **Links for every account that ends before 2026-06-23 (row W11-S2).** Accepted into FWD-9: the next round extends the links so every
   line reaches its newest account, or says why it stops.
4. **In-kind exits and the 17 near-matches (row W10-S4).** Score in-kind exits whatever their date. The 17 near-matches are NOT decided by a
   seat: FWD-9's ACCEPT says a link is never guessed. They are listed for Andrew to put to Cottonwood, each with its two accounts and the
   evidence, and stay "not linked, awaiting a person" until answered.
5. **Gate precision (row W7-S1, dismissed).** Not this project's. Carried to the gates' owner as a row in the gates' own channel.

## ENRICHMENT LIST -- the next round, in order (one issuance)

1. **Bronze: the three imaging archives** (HKE, HJH, 4XF) byte-for-byte with SHA-256 in the manifest. Andrew asked whether the delivery is
   fully in AWS; today it is 1 of 5.
2. **The price-coverage census, complete and graded USABLE / BARRED** (ruling 1).
3. **FWD-9: links for every ended account; in-kind exits scored; the 17 near-matches written as a list for Andrew** (rulings 3, 4).
4. **C-RESTRICTED: the restricted prefix's bucket policy**, so the CRM zip can land. The Terraform file is the cloud lane's; name the exact
   file and this seat grants it to the round's lane.
5. **The document index and unique documents (FWD-5)**, after item 1.
6. **The account crosswalk's first version (FWD-8).**

**Not in this round:** the price pull itself. It writes the securities history, whose store MDPF_SECHIST's round 1 defines on dell1; pulling
before that would create a second store to migrate (the no-shadow law). It starts the moment that store exists.

-- 1.0.0_SA_CTO
