# NFRA_SCHWABBF -- Schwab masters: full backfill and canonical bronze paths (L1 brief)

**Author:** `4.0.0_SA_CRO` (laptop) | **Date:** 2026-10-20 | **Mode:** NEW | **Consumer:** `1.0.0_SA_CTO` `/endpoint --forward`
**Placement:** laptop owns it end to end (CTO msg 109882, Andrew via ms 01:02Z).
**Proposed code:** NFRA_SCHWABBF (the CTO's suggestion; kept, since it says what the project is).

**Record and measurements:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_210xZ_SCHWAB_COTTONWOOD_MASTERS_PULL_AND_BACKFILL.md`
(c031634941). Andrew, VERBATIM, from that record:

> Run it, we need to start pulling all of these and also getting as much backfill as we can from them. Furthermore,
> we need full backfill from the 0840 account as well if we have not already done so. When we begin pulling these,
> they should be organized in the opal-data-assets bucket in canonical LGIC_NAMING path form

**Held open with Andrew; this brief does not rule on either:**
- (a) whether to pull the other 210 masters the login is entitled to;
- (b) the move of the stored partitions itself (CTO msg 109882).

Every outcome below that touches (b) is written so that it holds under either answer.

---

## PART I -- THE OUTCOME TERRITORY

### Candidate thread (becomes FWD-1)

An analyst reads master 08403355's balances for 2023-10-17, Schwab's oldest served day, from silver. Behind it, the
files were pulled from Schwab's history and stored at the builder address
`s3://opal-data-assets/schwab/08403355/bronze/<type>/date=2023-10-17`. Coarse grain: one master (the one with the
largest recoverable gap), one business date, every hop once:
- Schwab history;
- canonical bronze;
- the existing converter;
- silver;
- a read.

The oldest day is also the one most at risk of falling out of Schwab's window (Part VII). The rest is enrichment.

### O1 -- Each master's history is complete from Schwab's floor forward

An analyst can read any of the three entitled masters (08242234, 08335338, 08403355) on any business day from
2023-10-17, and find no day missing that Schwab still serves. Today the stored history starts later on all three
(Part VI).

### O2 -- Anyone can say which days are stored, per master and file type

An engineer, an agent or ops can read, for each master and each file type, which business days are present and
which Schwab served but Opal does not hold. Gaps are judged against the trading calendar. It is a record to read; it
sends nothing.

### O3 -- A Schwab file is found by computing its address, never by knowing a legacy form

Anyone holding `lib/opal_naming.py address()` finds any stored Schwab bronze file at the address the builder returns
(`.../bronze/<type>/date=YYYY-MM-DD`). Two key forms never stand side by side, which would be a duplicate output path
under Andrew's veto.

### O4 -- Every consumer keeps producing the same answers across the change of form

The converters and builders that read Schwab bronze today produce the same silver and gold for any stored day before
and after the key form changes. Readers include:
- the bd-tree converters through `_monolith_bronze.py`;
- `data/canonical/schwab/silver/_canonical_silver_lib.py`;
- `data/assets/scripts/silver/schwab_conversion.py`;
- `data/canonical/schwab/build_canonical_daily.py`.

The change is one move with a same-window rollback, never a long dual-read period.

### O5 -- Each new day lands in the canonical form on its own

The daily pull lands each new business day at the builder address, with no later re-keying step.

### O6 -- A newly entitled master starts flowing with a registry row, daily and backfill together

On the day Schwab entitles Opal's login to a Cottonwood master (firm FA08719286, Stephen SL08134043, Christa Bass
08165601, Jay Rubottom 08480305), an engineer adds its registry row. From then on its daily files and its full
history land in the same form, with no new code.

---

## PART II -- WHERE THE BOUNDARY SITS

**This project owns:**
- the historical pull of the three entitled masters back to Schwab's floor (O1, FWD-1);
- the stored-days record (O2);
- the change of the bronze key form to builder output: the stored partitions and every reader and writer of the old
  form, moved together (O3, O4);
- the daily puller's destination form (O5);
- the onboarding path for a newly entitled master (O6).

**It relies on, and does not own:**
- **The Schwab Box and its session.** Owned by ADVI_SCHWABAUTO / OPAL_ASSETS C3: EC2 `i-0f3d57a97f14727af`, the
  standing Schwab Data Delivery login and the daily puller `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1`.
  The backfill uses the same login and its session lock. It never runs inside the daily pull fires.
- **Schwab's entitlement of the four Cottonwood masters.** That act belongs to Cottonwood and Schwab. Today the masters
  are absent from the 213-master list and download returns HTTP 204.
- **The silver tables.** They are already in builder form (Part IV finding 3). This project changes how silver is
  FED, not where it lives.
- **The LGIC registry** (`infra/logic/registry/`, rows in `4.0.0_SA_CRO`'s lane) and the naming builders.

**Siblings, named:**
- **NFRA_AWSFTP** (brief `docs/briefs/nfra-awsftp-custodian-sftp-direct-to-aws-brief-20261019.md`). It moves daily
  Schwab delivery from the desktop session to SFTP in AWS. Both projects land at the SAME builder address. Whichever
  sets the canonical bronze form first sets it for both, and the other inherits it.
- **NFRA_FIDUPL** (dell1). Fidelity, not Schwab. Named only so that no one assumes this project lands Fidelity files.
- **Consumers of Schwab silver**, untouched as long as O4 holds: MDPF, TCKT_EARLYWARN, NFRA_OPLGTW (the gateway's Schwab
  tools), IRPT, ADVI.

**Not this project:**
- the 210 other entitled masters, held as (a) above;
- any re-parse or change to silver schemas;
- alerts of any kind (CLAUDE.md section 5 moratorium);
- the purpose law that 0824 and 0833 are never summed or substituted (`_monolith_bronze.py` header). The backfill
  preserves it; it does not revisit it.

---

## PART III -- THE QUALITATIVE BAR

- An analyst asking "what did this 0840 account hold in late 2023" gets an answer from Opal's own store, without
  anyone asking Schwab again.
- An engineer writing a new reader never learns that Schwab bronze once had a different key shape. Nothing in the
  bucket or the code tells them.
- On the day after the key change, nobody can find a silver or gold figure for an already-stored day that differs
  from the day before. A difference would read as a defect, not as an expected side effect.
- When Cottonwood says "Schwab has entitled you", the honest reply is "it is landing", not "we need to build that".

---

## PART IV -- THE SUBSTRATE (findings; measured 2026-10-20 ~01:0xZ unless the record is cited)

1. **Schwab serves history from 2023-10-17.** The record searched 2020-01-01..2024-10-01 for 08403355 and found files
   from 2023-10-17 (512 files). Same span on the control master. The oldest file downloaded, HTTP 200.
2. **Stored bronze starts later and uses a non-builder key form.**
   - The 08403355 `acc` partitions begin `20240930/`, `20241001/`.
   - The record gives first stored days: 0840 at 2024-09-30 (515 partitions), 0824 at 2024-01-16 (693), 0833 at
     2024-07-08 (574). That is 1,782 date partitions, matching the CTO's "about 1,800".
   - Object counts today:

| Master | Bronze objects | File-type folders |
|---|---|---|
| 08242234 | 7,960 | 17 |
| 08335338 | 7,758 | 18 |
| 08403355 | 6,064 | 16 |
| total | 21,782 | |

3. **Silver already matches the builder; only bronze differs.**
   - `address('schwab','08242234','silver','dim_balance','date=2026-10-16')` returns
     `s3://opal-data-assets/schwab/08242234/silver/dim_balance/date=2026-10-16`. That is the stored silver form.
   - `address(...,'bronze','acc','date=2026-10-16')` returns `.../bronze/acc/date=2026-10-16`, but the stored form is
     `.../bronze/acc/20261016/<master>.CRS20261016.ACC.zip`.
4. **The old bronze key form is written and read in many places.** A census over `data/` and the Schwab infra
   (comp-find, 59 hits across 2,574 files) finds the grammar in:
   - the writer `sdd-daily-pull.ps1`;
   - `infra/aws/ec2/canonical-schwab-si2/remap-bronze-to-monolith.py`;
   - `data/black_diamond/scripts/bronze/_monolith_bronze.py`, the key function `monolith_bronze_key()`. It is mirrored
     by hand in `data/canonical/schwab/silver/_canonical_silver_lib.py`, and both must change in one commit (the
     file's own rule). The bd-tree copies also deploy standalone to `s3://opal-data-bd/code/`, so the change has a
     deployed-bytes leg, not just a repo leg;
   - five bd-tree converters (acc, lots, rps x2, trn), `rps_ingestion.py`, `data/assets/scripts/silver/schwab_conversion.py`
     and `silver_registry.py`;
   - `data/canonical/schwab/build_canonical_daily.py` and its date-axis test;
   - the IAM policies in `infra/aws/terraform/canonical-schwab-ec2/{iam,monolith-iam}.tf`;
   - `data/_contracts/vendor_asof_registry.yaml`;
   - an opal-gateway test (`test_og_cd1.py`).
   Hits in documents may be stale; this list is where to look, not a verified inventory.
5. **Registry rows are missing for 08403355 and all four Cottonwood masters.** `address()` REFUSES each one: "scope
   '<master>' resolves to no scopes.json row". 08242234 and 08335338 have MASTER rows under firm 49financial.
6. **The session is shared and locked.** The record's probes ran as Administrator, under the box's SDD session lock and
   outside the 21:45Z, 22:15Z and 22:45Z pull fires. A backfill on the same login competes with the daily pull for that
   lock.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- Andrew's word on (b), the move of the stored partitions. It is a move of served input under CLAUDE.md section 5, so
  it needs a never-widen sign-off naming its blast radius and its per-key rollback.
- Andrew's word on (a), the other 210 masters, before any of them is pulled.
- Registry rows for 08403355 (firm attribution: the file header reads "49 FINANCIAL") and, when entitled, for each
  Cottonwood master under firm cottonwood. These are `4.0.0_SA_CRO` rows.
- Every reader and writer of the old form, moved together with the stored objects, including the deployed bd-tree
  copies in `opal-data-bd/code/`. Otherwise one of them reads an empty prefix and reports "nothing to do".
- A backfill window that never overlaps the daily pull fires, holding the same session lock.
- Schwab's entitlement of the Cottonwood masters (Cottonwood and Schwab).
- An answer to whether the 2023-10-17 floor is fixed or rolls forward daily (Part VII).

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-10-19 ~21:0xZ by `1.0.0_SA_CTO` (record c031634941) and 2026-10-20 ~01:0xZ by `4.0.0_SA_CRO`.

| Master | Name on file | Stored bronze from | Schwab serves from | Recoverable gap |
|---|---|---|---|---|
| 08403355 | 49 FINANCIAL | 2024-09-30 | 2023-10-17 | about 11 months |
| 08335338 | 49 FINANCIAL | 2024-07-08 | 2023-10-17 (control span) | about 9 months |
| 08242234 | 49 WEALTH MANAGEMENT LLC | 2024-01-16 | 2023-10-17 | about 3 months |

- **Cottonwood masters:**
  - Search lists 205 to 223 files per master over 30 days.
  - None is in the 213-master entitlement list.
  - Download of 08719286 returns HTTP 204.
- **Silver** for all three entitled masters is current to business date 2026-10-16.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **That the floor is fixed.** 2023-10-17 is exactly three years before the 2026-10-17 to 2026-10-19 measurements. If
  Schwab keeps a rolling window, the floor moves forward each day and the oldest days are lost one per day until
  pulled. One repeated search a day later answers it. Not measured.
- **That 08335338's floor equals 08403355's.** The record searched 0840 and a control; the per-master floor for 0833 and
  0824 is inferred from the control span, not measured.
- **That Part IV finding 4 is complete.** It is a keyword census, and a reader that builds the key by another route
  would not appear.
- **That the backfilled files parse.** The existing converters have only ever read the stored range. The oldest file
  downloaded was 513 bytes. Whether 2023 files share today's layout is unverified.
- **Any count of the 210 other masters' size**, or anything about them beyond their presence in the entitlement list.

---

## REFS

```
  BRIEF PATH        docs/briefs/nfra-schwabbf-schwab-masters-backfill-canonical-paths-brief-20261020.md
  PROJECT           NFRA_SCHWABBF (proposed; not yet registered -- L3, 1.0.0_SA_CTO)
  EXISTING PRD      NONE
  RECORD            org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_210xZ_SCHWAB_COTTONWOOD_MASTERS_PULL_AND_BACKFILL.md (c031634941)
  SIBLING PROJECTS  NFRA_AWSFTP (shared builder address), ADVI_SCHWABAUTO / OPAL_ASSETS C3 (Schwab Box), NFRA_FIDUPL
                    (Fidelity, named to exclude); consumers MDPF, TCKT_EARLYWARN, NFRA_OPLGTW, IRPT, ADVI
  PRIOR ART         data/assets/docs/SCHWAB_AUTO_PULL_DESIGN.md; data/assets/docs/SCHWAB_BOX_ARCHETYPE.md;
                    infra/aws/ec2/canonical-schwab-si2/{sdd-daily-pull.ps1,sdd-backfill-08335338.ps1,sdd-history.ps1,
                    remap-bronze-to-monolith.py}; data/black_diamond/scripts/bronze/_monolith_bronze.py;
                    data/canonical/schwab/silver/_canonical_silver_lib.py; lib/opal_naming.py; infra/logic/registry/scopes.json
  MEASURED AT       2026-10-19 ~21:0xZ (record); 2026-10-20 ~01:0xZ (object counts, builder probes, key census)
```
