# 2.0.0_SA_COO~D (site Z) -- /canonical-drive DSGN_AMGTV1 -- 2026-09-30 06Z

Lease FULL throughout. Cron `17,47 * * * *` (ANDREW_DIRECT_20260929_183xZ_SELF_DRIVE_AMGT_FABRIC_OPS.md).

## Round 10 -- walk I, a repair, walk J, closed

- **Walk I** (5174 @6a9ce827, containing DEV 5810586a) was VALID. It found AZN's Model tab reading "Opal's opal's
  historical-multiple reference".
  - Cause: three literal 0x08 bytes where regexes meant `\b` -- `ModelTab.tsx:295` (o-3) and `HeaderBrief.tsx:48-49` (since round
    1, so no description source ever read "from Bloomberg"). tsc and all 16 harnesses passed them. Row Z-S5.
  - 6501 JP never opened (the walker left while its first read was pending).
- **The repair:**
  - A new order file (AV-o-5) was refused by to-pipeline-gate LIMB 6 (one issuance per round; a re-cut modifies its orders).
  - AV-o-3 was re-opened as AMENDMENT 1 @c13bb7407f, with AC4 = `round10/checks/bytes.cjs` (0/3 at base, 3/3 green, ALL 16/16).
  - Worker ~37 drained it at CLOUD 4813813e75 / DEV 2bb60cc3. CTO~Z read 0 files with 0x08 over 991 portal src code files.
- **Walk J** (5174 @c1ef440d, containing 2bb60cc3) was VALID with a proven disarm. It shows long-form dates, the dossier, AZN's team
  cases with the rule line once, TSM's EV raw and labelled, and "Company description from Bloomberg". Row Z-S6 resolves Z-S5.
- **Close record and drain-end read:**
  - Written at 06:4xZ. The commit waited ~12 min: CTO~Z's ETFS_RIVALS D4->D5 move was in flight, and its three tracked D4 paths
    read deleted in the shared tree, so missions-tree-check refused every org/missions commit.
  - COO~RV's and CTO~Z's state was not touched. A retry committed the record @34427cf77c once the move landed @808f1eb302.
  - The drain-end read went to CTO~Z and the L8 packet to CVO~Z (07:00Z).

## Andrew, in session

- Asked for the timeline spine's implementation and how a day counts as "searched". Both were answered from the code (see the
  05Z log).
- The coverage-rule ask to AMGT_HARVST remains held for his word.
