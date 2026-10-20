# NFRA_SCHWABBF -- Schwab masters: full history back to Schwab's floor, stored in the builder's one path form

```json
{
 "project": "NFRA_SCHWABBF",
 "directive": "D8",
 "fabric": "laptop",
 "prd_version": "v0.2",
 "step": 4,
 "brief_ref": "docs/briefs/nfra-schwabbf-schwab-masters-backfill-canonical-paths-brief-20261020.md@f0e33a4317",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8"],
 "status": "DRAFT"
}
```

**Author:** `1.0.0_SA_CTO`, 2026-10-20 ~13:1xZ. **Placement:** LAPTOP, directive D8, macro NFRA (registered @649d6624aa). The laptop owns it end
to end (Andrew via ms, 2026-10-20 01:02Z, laptop msg 109881).

**Records (Andrew-direct):**
- **2026-10-19 ~21:0xZ**, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_210xZ_SCHWAB_COTTONWOOD_MASTERS_PULL_AND_BACKFILL.md`
  @c031634941: "we need to start pulling all of these and also getting as much backfill as we can from them. Furthermore, we need full
  backfill from the 0840 account as well if we have not already done so. When we begin pulling these, they should be organized in the
  opal-data-assets bucket in canonical LGIC_NAMING path form".
- **2026-10-20 ~13:0xZ**, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261020_130xZ_NFRA_SCHWABBF_DONE_WHEN_CONFIRMED_PATH_MOVE_YES_210_MASTERS_OUT.md`:
  "1.) Yes as written. 2.) Yes, rec is accurate. 3.) We don't care about these at this time." The DONE WHEN lines are confirmed, the
  stored-partition move is yes, and the other 210 entitled masters are out of scope.

## ENDPOINT (step 2, /endpoint --forward)

CONFIRMED by Andrew 2026-10-20 ~13:0xZ. The source, verbatim from step 2, is
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_NFRA_SCHWABBF_20261020.md`.

```
  FWD-1  An analyst reads master 08403355's balances for Schwab's oldest served
         business day, from Opal's own store, and the files behind it came from
         Schwab's history into the builder's address
         DONE WHEN  EXERCISED -- one trace: the oldest day pulled from Schwab, stored
                    at the builder's address, converted the existing way, and the
                    balances read. If Schwab's oldest day has moved by then, the
                    trace uses the oldest day it serves at the time
         ACCEPT     An analyst can say what that 0840 account held on its oldest
                    day without asking Schwab again, and the figure came from a file
                    Opal pulled from Schwab, not from a stand-in

  FWD-2  Each of the three entitled Schwab account groups has every business day
         Schwab still serves
         DONE WHEN  EXERCISED -- the stored days read against Schwab's served days,
                    per account group
         ACCEPT     For 0824, 0833 and 0840, nobody can name a business day Schwab
                    still serves that Opal does not hold

  FWD-3  Anyone can read which days are held, per account group and file type
         DONE WHEN  EXERCISED -- the record is read and agrees with the store
         ACCEPT     An engineer or ops person can see, for each account group and
                    file type, which business days are held and which Schwab served
                    but Opal lacks, judged by the trading calendar; it sends nothing

  FWD-4  A Schwab file is found where the naming builder says it is, and only
         there
         DONE WHEN  APPLIED -- every stored Schwab raw file sits at the builder's
                    address, with no second form beside it
         ACCEPT     Someone who only knows the naming builder finds any stored Schwab
                    raw file on the first try, and never finds the same day stored
                    two different ways

  FWD-5  Every report built from Schwab data gives the same answer for an already
         stored day before and after the change
         DONE WHEN  EXERCISED -- sampled days rebuilt after the change and compared
                    with the figures from before it, read once at the change and not
                    kept running afterwards
         ACCEPT     The day after the change, nobody can find a holdings, balance or
                    activity figure for an already stored day that differs from the
                    day before

  FWD-6  Each new business day lands in the builder's form by itself
         DONE WHEN  EXERCISED -- a scheduled daily pull lands its day at the
                    builder's address
         ACCEPT     A new day's Schwab files appear where the builder says, with no
                    later fix-up step

  FWD-7  When Schwab opens a Cottonwood account group to Opal's login, it starts
         flowing, daily and history, with only its setup entry added
         DONE WHEN  EXERCISED -- QUALIFIED WAIT, ACCEPTED by Andrew 2026-10-20: only
                    Cottonwood and Schwab can open the four account groups to Opal's
                    login
         ACCEPT     The day Cottonwood says "Schwab has opened them", the honest
                    answer is "it is landing", and nothing new had to be built

  FWD-8  Cottonwood's four Schwab account groups land every business day, with
         their full history, through Alongside's own Schwab login on its own
         Schwab box
         DONE WHEN  EXERCISED -- one trace: a Cottonwood account group's day pulled by
                    the Alongside box, stored at the builder's address and read; then
                    the history back to Schwab's floor read as held. The one-time
                    sign-in that starts the box's session is a person's act (it may
                    need a Schwab security code); everything after it runs on its own
         ACCEPT     An analyst reads a Cottonwood client's Schwab positions for
                    yesterday and for a day in late 2023 from Opal's own store, and
                    nobody kept a login open to get them
```

FWD-8 was ADDED at v0.2 on Andrew-direct 2026-10-20 ~13:4xZ
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261020_134xZ_ALONGSIDE_SCHWAB_CREDENTIALS_AND_ALONGSIDE_PULLER.md`). FWD-7 stays: it
covers a master that Schwab opens to Opal's existing login. FWD-8 is the route he named for Cottonwood.

## CONTRACTS

| row | owner | rule | proven by |
|---|---|---|---|
| C-SCOPE | Andrew | **Three masters only: 08242234, 08335338, 08403355.** The four Cottonwood masters (08719286, 08134043, 08165601, 08480305) join through C-ONBOARD when Schwab entitles them (today: absent from the 213-master list, download HTTP 204). **The other 210 entitled masters are out of scope** (Andrew 2026-10-20: "We don't care about these at this time"). No cell reads, pulls or names them. | the record above; no cell's paths name another master |
| C-NAMES | every cell (use); `4.0.0_SA_CRO` (registry rows) | **Every address is `lib/opal_naming.py address()` output** (rule 30). Measured 2026-10-20 ~13:1xZ: `address('schwab','<m>','bronze','acc','date=2023-10-17')` returns `s3://opal-data-assets/schwab/<m>/bronze/acc/date=2023-10-17` for all three masters (08403355 now resolves; the brief's refusal at 01:0xZ is superseded), and silver returns `.../silver/dim_balance/date=2023-10-17`. A builder refusal is a missing registry row, never a hand-typed path. | `address()` printed beside every path the code writes or reads |
| C-KEYFORM | the key-form cell | **The bronze key is `address('schwab', <master>, 'bronze', <type>, 'date=YYYY-MM-DD')` + `/` + the vendor's own file name, unchanged** (for example `.../bronze/acc/date=2023-10-17/08403355.CRS20231017.ACC.zip`). The type folder stays the lower-case code the puller derives today (`TypeFolder`, `sdd-daily-pull.ps1`), and the date comes from the API's `AsOfDATE`, never the file name. The writer, every reader and the move script share one key function. Today that function is `monolith_bronze_key()` (`data/black_diamond/scripts/bronze/_monolith_bronze.py:48`), mirrored in `data/canonical/schwab/silver/_canonical_silver_lib.py`; both change in one commit, with the bd-tree copies deployed to `s3://opal-data-bd/code/`. | the key function's test prints the builder's output for three masters and two dates |
| C-READERS | the key-form cell | **Every reader and writer of the old form changes in the same release as the move.** The brief's census (Part IV.4: 59 hits across 2,574 files) is a starting list, not an inventory. The issuer re-measures it at the cut with `comp-find` over the old grammar (`bronze/<type>/<YYYYMMDD>/`), including deployed copies, IAM resource patterns (`canonical-schwab-ec2/{iam,monolith-iam}.tf`) and contracts (`data/_contracts/vendor_asof_registry.yaml`). A reader missed reads an empty prefix and reports "nothing to do", so the census denominator is printed. | the cut's census, zero old-form hits outside the move script and this PRD |
| C-MOVE | the cutover cell; never-widen pair (CTO+COO) | **One cutover, same-day rollback, no side-by-side period** (Andrew 2026-10-20, call 2 REC). Order inside one change window, outside the pull fires: (1) copy every stored object to its builder key; (2) verify by count and sha per master and type (21,782 objects measured at the brief: 7,960 + 7,758 + 6,064); (3) deploy the readers, the writer and the IAM patterns of the new form; (4) run FWD-5's read; (5) **delete the old keys, an act Andrew confirms** (CLAUDE.md: S3 deletes take human confirmation). Rollback per key until step 5: redeploy the prior readers, writer and IAM, and the old keys are still in place. After step 5, rollback is a copy back from the builder keys. The change record names every family that reads Schwab bronze (one `describe` sweep), and the never-widen pair names this blast radius and both branches. | the change record's legs; FWD-4's census; FWD-5's read |
| C-BACKFILL | the backfill cell | **History from Schwab's floor (2023-10-17, measured 2026-10-19 21:21Z and again 2026-10-20 08:50Z, after the Eastern date rolled) to each master's first stored day:** 08403355 to 2024-09-29, 08335338 to 2024-07-07, 08242234 to 2024-01-15. The puller's own search, download and vendor-master guard are used (`sdd-daily-pull.ps1`, with the backfill shape of `sdd-backfill-08335338.ps1` and `sdd-history.ps1`) under the box's SDD session lock, never inside a pull fire (09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z). It lands only at the builder's key, and only after C-MOVE's step 3, so no day is ever written in the old form. Per-master floors for 0824 and 0833 are measured at the start of the cell (the brief inferred them from a control). | the run record's denominator: enumerated = downloaded + skipped + failed |
| C-PARSE | the backfill cell | **Backfilled 2023-2024 files go through the existing converters unchanged.** The first backfilled day is converted before the rest are pulled. A layout difference (brief Part VII) is filed as a row with the file type and day, not patched in a converter inside this project. | FWD-1's trace |
| C-RECORD | the record cell | **One read-only record of held days** per master and file type, beside the existing manifests under `schwab/<master>/meta/` (its address comes from the builder). For each business day in Schwab's served range it shows held or missing, judged by `lib/trading_calendar.py`. It sends nothing (moratorium). | FWD-3's read against a listing of the store |
| C-EQUAL | the cutover cell | **FWD-5 is one read at the change, never a standing comparator** (Andrew's veto on parity comparators). Before step 1 the issuer records silver and gold figures for a named sample of days per master; after step 4 it rebuilds those days and compares. Any difference stops the cutover before step 5. | the before and after files, committed with the change record |
| C-DAILY | the key-form cell | **The daily puller writes the builder form from the cutover release on** (FWD-6). `sdd-daily-pull.ps1` is re-uploaded to its code home by the same release; the schedule targets are unchanged. | the first scheduled fire after the cutover lands at the builder address |
| C-ALONGSIDE | the Alongside box cells; NFRA CloudOps lane (applies) | **The Alongside Schwab Box: the exact same setup and logic as the existing 49F Schwab Box, explicitly labeled as an Alongside box** (Andrew-direct ~13:5xZ: "it should be exact same setup and logic as already exists with the 49 schwab box. this one should explicitly be labeled as an alongside box"). It is a copy of `canonical-schwab-ec2` and `canonical-schwab-si2` (same Windows host, SI2 app, Administrator vault, SSM-to-scheduled-task hand-off, lock and puller), with every name carrying the `alongside` scope from the builder and the device named "Alongside Schwab Box" (FWD-8). It is a Windows EC2 that holds Alongside's own SDD session and refresh token in its own Administrator vault. It never shares the existing box's session, lockfile or schedule slots, and its fires are staggered from the 49F fires. **Credentials:** `schwab/alongside/sdd-credentials` (created 2026-10-20 ~13:4xZ, JSON `username` and `password`, graded CONFORMANT). The box role reads exactly that secret, and the Terraform root adopts it by `import` with `prevent_destroy`, never by recreating it. **The first sign-in is a person's act:** the session is human-established in the SI2 app, and once established the puller rides it. **Masters:** only the four Cottonwood masters, each a MASTER scope row under firm `cottonwood` (CRO rows) and each an enumerated IAM write to `schwab/<master>/bronze` in builder form. The first read after the session exists is that login's own entitlement list (`FetchDetails/UserMasters.aspx`): whether it sees the four is unmeasured until then, and a master it does not see is named, not assumed. **Backfill:** C-BACKFILL's rules per master, to Schwab's floor. All names come from the builder, and every apply goes through `safe-apply`. | the entitlement read; FWD-8's trace |
| C-ONBOARD | the onboarding cell | **A newly entitled master needs one setup entry, not code** (FWD-7). The master list moves from three hard-coded places (the puller's `ValidateSet`, the IAM resource enumeration and the schedule's `local.si2_daily` map) into the schedule map alone. The IAM statements and the puller's master check are derived from that map, so adding a master is a registry scope row (CRO) plus one map entry, applied by `safe-apply`. Masters stay enumerated, never wildcarded (`SCHWAB_AUTO_PULL_DESIGN.md` 4.8 and the IAM rule). The backfill for a new master runs the same cell with its own floor. | a dry plan that adds a fourth map entry and changes only that master's schedule and IAM statement |

## THE DECISIONS -- CLOSED AT L4

1. **Move first, then backfill (C-MOVE before C-BACKFILL).** Backfilled days land only in the builder form, so the old form never grows. This
   follows from "no two forms" (FWD-4) and Andrew's call 2.
2. **The key keeps the vendor's file name** under the builder's partition, so the vendor-master guard (the master read from the file name)
   is unchanged.
3. **One shared key function** carries the grammar for the writer, the readers and the move script, so the grammar lives in one place,
   per that function's own rule.
4. **No alert, no comparator.** FWD-3 is a record read on demand, and FWD-5 is a single read at the change.
5. **The other 210 masters are out** (C-SCOPE). Re-opened only by Andrew's word.

## OPEN AT ANDREW (acts only he can do)

- **Confirm FWD-8** (added at v0.2 on his word).
- **The one-time sign-in on the Alongside box:** Andrew RDPs into the Alongside Schwab Box once it exists and signs into the SI2 app with
  Alongside's Schwab login (Andrew-direct ~13:5xZ: "I will need to RDP into the EC2 box most likely to get that done"). The box's
  RDP access is set up for that sitting and closed after it, as the 49F box's is.
- **Confirm the delete of the old keys** at C-MOVE step 5, once FWD-5's read is clean. He names the change window.
- **Cottonwood's Schwab entitlement** of the four masters (Cottonwood and Schwab). This is FWD-7's qualified wait.

## CELL CANDIDATES (round 1 builds the FWD-1 thread; the issuer decomposes)

1. **The key-form cell** (C-KEYFORM, C-READERS, C-DAILY): the shared key function in the builder form, every reader and the writer moved to
   it, and tests. Code only, nothing deployed.
2. **The move script and its dry run** (C-MOVE steps 1-2 against a listing, nothing written), with the sample of days for C-EQUAL recorded.
3. **The cutover** (C-MOVE steps 1-4, C-EQUAL), under its never-widen pair and change record, with step 5 held for Andrew's confirmation.
4. **FWD-1's thread:** backfill 08403355's oldest served day (C-BACKFILL), convert it (C-PARSE), and read its balances from silver.

A parallel workstream (C-ALONGSIDE, FWD-8) needs no wait on the cutover beyond the key form: (a) the CRO's scope rows for the four Cottonwood
masters; (b) the Alongside box's Terraform root and puller copy, in builder form from the start; (c) the person's sign-in; (d) the
entitlement read; (e) one Cottonwood day end to end, then its backfill.

Later rounds enrich: the full backfill for the three masters (FWD-2), the held-days record (FWD-3), and the onboarding path (FWD-7).

## PATHS

- **This project:** `org/missions/D8/NFRA/NFRA_SCHWABBF/`.
- **Prior art, read at HEAD by the issuer:**
  - `infra/aws/ec2/canonical-schwab-si2/` (`sdd-daily-pull.ps1`, `sdd-backfill-08335338.ps1`, `sdd-history.ps1`, `remap-bronze-to-monolith.py`);
  - `infra/aws/terraform/canonical-schwab-ec2/` (`monolith-daily-schedule.tf`, `iam.tf`, `monolith-iam.tf`);
  - `data/black_diamond/scripts/bronze/_monolith_bronze.py` and `data/canonical/schwab/silver/_canonical_silver_lib.py`;
  - `data/assets/docs/SCHWAB_AUTO_PULL_DESIGN.md` and `SCHWAB_BOX_ARCHETYPE.md`;
  - the record of the 2026-10-19 SDD probes (@c031634941) and the master list `org/tier1_exec/1.0.0_SA_CTO/deliverables/SCHWAB_SDD_ENTITLED_MASTERS_20261019.txt`.

## SURFACE MANIFEST

- **AWS:**
  - S3 `opal-data-assets`, prefixes `schwab/{08242234,08335338,08403355}/bronze/` (the move and the backfill);
  - the deployed bd-tree code under `s3://opal-data-bd/code/`;
  - the Schwab box `i-0f3d57a97f14727af` (read and pull under the session lock);
  - the box role's IAM statements in `canonical-schwab-ec2`.
- **Portal:** none.
- **Repo:** the key function and its mirror, every reader the census names, the puller, the Terraform root, and this tree.

## CHANGE LOG

- **v0.2 (~13:5xZ 2026-10-20), same sitting:** C-ALONGSIDE is an exact copy of the 49F Schwab Box, labeled Alongside, and Andrew RDPs in for the
  first sign-in (his words, quoted in the row and under OPEN AT ANDREW).
- **v0.2 (~13:5xZ 2026-10-20):** on Andrew-direct ~13:4xZ, FWD-8 ADDED, C-ALONGSIDE added, the Alongside workstream named, and two acts
  added to OPEN AT ANDREW (confirm FWD-8; the box's first sign-in). The ENDPOINT changed, so the ratified-text half re-signs.

- **v0.1 (~13:1xZ 2026-10-20):** first draft on the confirmed endpoint and Andrew's three answers. Contracts C-SCOPE to C-ONBOARD; decisions
  1-5; the old-key delete held for Andrew's confirmation.
