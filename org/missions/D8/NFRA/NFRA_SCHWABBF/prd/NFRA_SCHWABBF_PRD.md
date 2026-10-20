# NFRA_SCHWABBF -- Schwab masters: full history back to Schwab's floor, stored in the builder's one path form

```json
{
 "project": "NFRA_SCHWABBF",
 "directive": "D8",
 "fabric": "laptop",
 "prd_version": "v0.7",
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
- **2026-10-20 ~16:3xZ**, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261020_163xZ_SCHWABBF_0824_OUT_FOCUS_COTTONWOOD_AND_0840.md`:
  "I dont care about that 0824, I want the new Cottonwood accounts taken care of and the 0840 tax sma account sorted out." 0824 is out;
  the work is the four Cottonwood masters (FWD-8) and 08403355. 0833 is not named in the word and is held out with 0824 until he says
  otherwise (OPEN AT ANDREW).

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

  FWD-2  The 0840 Tax SMA account group has every business day Schwab still serves
         DONE WHEN  EXERCISED -- the stored days read against Schwab's served days
         ACCEPT     For 0840, nobody can name a business day Schwab still serves that
                    Opal does not hold

  FWD-3  Anyone can read which days are held, per account group and file type
         DONE WHEN  EXERCISED -- the record is read and agrees with the store
         ACCEPT     An engineer or ops person can see, for each account group and
                    file type, which business days are held and which Schwab served
                    but Opal lacks, judged by the trading calendar; it sends nothing

  FWD-4  An 0840 or Cottonwood Schwab file is found where the naming builder says
         it is, and only there
         DONE WHEN  APPLIED -- every stored 0840 and Cottonwood raw file sits at the
                    builder's address, with no second form beside it
         ACCEPT     Someone who only knows the naming builder finds any stored 0840
                    or Cottonwood Schwab raw file on the first try, and never finds
                    the same day stored two different ways

  FWD-5  Every report built from Schwab data gives the same answer for an already
         stored day before and after the change
         DONE WHEN  EXERCISED -- sampled days rebuilt after the change and compared
                    with the figures from before it, read once at the change and not
                    kept running afterwards
         ACCEPT     The day after the change, nobody can find a holdings, balance or
                    activity figure for an already stored day that differs from the
                    day before

  FWD-6  Each new 0840 business day lands in the builder's form by itself
         DONE WHEN  EXERCISED -- a scheduled daily pull lands its 0840 day at the
                    builder's address
         ACCEPT     A new day's 0840 Schwab files appear where the builder says, with
                    no later fix-up step

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

## CONTRACTS

| row | owner | rule | proven by |
|---|---|---|---|
| C-SCOPE | Andrew | **Five masters in two groups (Andrew-direct ~16:3xZ: "I dont care about that 0824").** In scope on the 49F Schwab Box: 08403355 (0840, the Tax SMA account) only, under firm `49financial`. **08242234 (0824) and 08335338 (0833) are out:** they keep their daily pull and their current keys byte-for-byte, and no cell moves, backfills, re-keys or records them. The Alongside Schwab Box (C-ALONGSIDE, FWD-8) carries the four Cottonwood masters, 08719286, 08134043, 08165601 and 08480305, under firm `cottonwood`; they are absent from the 49F login's 213-master list and download HTTP 204 there. C-ONBOARD covers a master later opened to either box's login, written by that box alone (C-ONEWRITER). **The other 210 masters entitled to the 49F login are out of scope** (Andrew 2026-10-20: "We don't care about these at this time"). No cell reads, pulls or names them. | the records above; no cell's paths move, backfill or re-key a master outside these five |
| C-NAMES | every cell (use); `4.0.0_SA_CRO` (registry rows) | **Every address is `lib/opal_naming.py address()` output** (rule 30). The scope argument is the FIRM of the master (C-KEYFORM). Measured 2026-10-20 ~14:3xZ: `address('schwab','49financial','bronze','acc','date=2023-10-17')` returns `s3://opal-data-assets/schwab/49financial/bronze/acc/date=2023-10-17`, and `address('schwab','cottonwood','bronze',...)` returns `s3://opal-data-assets/schwab/cottonwood/bronze/...`. The firm of each master is its scope row's `firm` field. A builder refusal is a missing registry row, never a hand-typed path. | `address()` printed beside every path the code writes or reads |
| C-KEYFORM | the key-form cell | **Vendor, then FIRM, then tier (Andrew-direct 2026-10-20 ~14:3xZ: "schwab vendor and 49 firm for the 0840 and cottonwood firm for the various master accounts", "abiding by the path structure that already exists in that bucket").** The bronze key is `address('schwab', <firm of the master>, 'bronze', <type>, 'date=YYYY-MM-DD')` + `/` + the vendor's own file name, unchanged. The firm comes from the master's scope row (`firm`): 08242234, 08335338 and 08403355 are `49financial`; 08719286, 08134043, 08165601 and 08480305 are `cottonwood` (rows added by the CRO). Builder output, measured ~14:3xZ: `s3://opal-data-assets/schwab/49financial/bronze/acc/date=2026-10-16` and `s3://opal-data-assets/schwab/cottonwood/bronze/acc/date=2026-10-16`. That is the same vendor/firm shape as `blackdiamond/49financial/`, `blackdiamond/cottonwood/` and `orion/inflection/`. Example: `.../schwab/49financial/bronze/acc/date=2023-10-17/08403355.CRS20231017.ACC.zip`. **Masters share a firm folder and are told apart by the vendor file name's master prefix**, which the vendor-master guard already reads. Every reader filters by master, so 0824 and 0833 are never summed or substituted (the purpose law in `_monolith_bronze.py`). **The firm form applies per master (v0.7):** the key function holds the set of firm-form masters (08403355 and the four Cottonwood masters) and returns today's key, byte-for-byte, for any other master, so 0824 and 0833 are written and read exactly as before. One master is never stored in two forms. The v0.6 legacy-member rule (1,245 unprefixed 0824 objects) is withdrawn: 0824 does not move. The type folder stays the lower-case code the puller derives today (`TypeFolder`, `sdd-daily-pull.ps1`), and the date comes from the API's `AsOfDATE`, never the file name. The writer, every reader and the move script share one key function. Today that function is `monolith_bronze_key()` (`data/black_diamond/scripts/bronze/_monolith_bronze.py:48`), mirrored in `data/canonical/schwab/silver/_canonical_silver_lib.py`; both change in one commit, with the bd-tree copies deployed to `s3://opal-data-bd/code/`. | the key function's test prints the builder's output for three masters and two dates |
| C-READERS | the key-form cell | **Every reader and writer of the old form changes in the same release as the move.** The brief's census (Part IV.4: 59 hits across 2,574 files) is a starting list, not an inventory. The issuer re-measures it at the cut with `comp-find` over the old grammar (`bronze/<type>/<YYYYMMDD>/`), including deployed copies, IAM resource patterns (`canonical-schwab-ec2/{iam,monolith-iam}.tf`) and contracts (`data/_contracts/vendor_asof_registry.yaml`). A reader missed reads an empty prefix and reports "nothing to do", so the census denominator is printed. | the cut's census, zero old-form hits outside the move script and this PRD |
| C-MOVE | the cutover cell; never-widen pair (CTO+COO) | **One cutover, same-day rollback, no side-by-side period** (Andrew 2026-10-20, call 2 REC). Order inside one change window, outside the pull fires: (1) copy every stored 08403355 object to its builder key (only 0840 moves; 0824 and 0833 stay where they are); (2) verify by count and sha per type (0840's count is re-measured at the cut and printed beside the brief's three-master total of 21,782); (3) deploy the readers, the writer and the IAM patterns of the new form; (4) run FWD-5's read; (5) **delete the old keys, an act Andrew confirms** (CLAUDE.md: S3 deletes take human confirmation). Rollback per key until step 5: redeploy the prior readers, writer and IAM, and the old keys are still in place. After step 5, rollback is a copy back from the builder keys. The change record names every family that reads Schwab bronze (one `describe` sweep), and the never-widen pair names this blast radius and both branches. | the change record's legs; FWD-4's census; FWD-5's read |
| C-BACKFILL | the backfill cell | **History from Schwab's floor (2023-10-17, measured 2026-10-19 21:21Z and again 2026-10-20 08:50Z, after the Eastern date rolled) to each master's first stored day:** 08403355 to 2024-09-29; the four Cottonwood masters per C-ALONGSIDE. 0824 and 0833 are not backfilled (C-SCOPE, v0.7). The puller's own search, download and vendor-master guard are used (`sdd-daily-pull.ps1`, with the backfill shape of `sdd-backfill-08335338.ps1` and `sdd-history.ps1`) under the box's SDD session lock, never inside a pull fire (09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z). It lands only at the builder's key, and only after C-MOVE's step 3, so no day is ever written in the old form. | the run record's denominator: enumerated = downloaded + skipped + failed |
| C-PARSE | the backfill cell | **Backfilled 2023-2024 files go through the existing converters unchanged.** The first backfilled day is converted before the rest are pulled. A layout difference (brief Part VII) is filed as a row with the file type and day, not patched in a converter inside this project. | FWD-1's trace |
| C-RECORD | the record cell | **One read-only record of held days** per in-scope master (C-SCOPE) and file type, beside the existing manifests under `schwab/<master>/meta/` (its address comes from the builder). For each business day in Schwab's served range it shows held or missing, judged by `lib/trading_calendar.py`. It sends nothing (moratorium). | FWD-3's read against a listing of the store |
| C-EQUAL | the cutover cell | **FWD-5 is one read at the change, never a standing comparator** (Andrew's veto on parity comparators). Before step 1 the issuer records silver and gold figures for a named sample of days per master; after step 4 it rebuilds those days and compares. Any difference stops the cutover before step 5. | the before and after files, committed with the change record |
| C-DAILY | the key-form cell | **The daily puller writes the builder form from the cutover release on** (FWD-6). `sdd-daily-pull.ps1` is re-uploaded to its code home by the same release; the schedule targets are unchanged. | the first scheduled fire after the cutover lands at the builder address |
| C-ALONGSIDE | the Alongside box cells; NFRA CloudOps lane (applies) | **The Alongside Schwab Box: the exact same setup and logic as the existing 49F Schwab Box, explicitly labeled as an Alongside box** (Andrew-direct ~13:5xZ: "it should be exact same setup and logic as already exists with the 49 schwab box. this one should explicitly be labeled as an alongside box"). It is a copy of `canonical-schwab-ec2` and `canonical-schwab-si2` (same Windows host, SI2 app, Administrator vault, SSM-to-scheduled-task hand-off, lock and puller), with every name carrying the `alongside` scope from the builder and the device named "Alongside Schwab Box" (FWD-8). It is a Windows EC2 that holds Alongside's own SDD session and refresh token in its own Administrator vault. It never shares the existing box's session, lockfile or schedule slots, and its fires are staggered from the 49F fires. **Credentials:** `schwab/alongside/sdd-credentials` (created 2026-10-20 ~13:4xZ, JSON `username` and `password`, graded CONFORMANT). The box role reads exactly that secret, and the Terraform root adopts it by `import` with `prevent_destroy`, never by recreating it. **The first sign-in is a person's act:** the session is human-established in the SI2 app, and once established the puller rides it. **Masters:** only the four Cottonwood masters, each a MASTER scope row under firm `cottonwood` (CRO rows) written under `address('schwab','cottonwood','bronze',...)`. Masters share that prefix, so the IAM write is enumerated per master by the vendor file name's master prefix: `schwab/cottonwood/bronze/*/date=*/<master>.*`, one statement entry per master, never a wildcard over the folder. The 49F box's statements take the same shape under `schwab/49financial/bronze/` for its three. The first read after the session exists is that login's own entitlement list (`FetchDetails/UserMasters.aspx`): whether it sees the four is unmeasured until then, and a master it does not see is named, not assumed. **Backfill:** C-BACKFILL's rules per master, to Schwab's floor. Every apply goes through `safe-apply`. **Every name in the copy is builder output from the first apply:** the 49F root's typed-name ternary (`monolith-daily-schedule.tf`, the `si2_daily_builder_named` set) is NOT copied, and every rule, role, profile and task name goes through `modules/opal_name` with the `alongside` scope. **If the Alongside login does not see one of the four masters**, that master is named in the entitlement read and reported to Andrew as his call to Cottonwood. FWD-8 is then graded on the masters the login sees, with the rest listed as unreachable by working. | the entitlement read; FWD-8's trace |
| C-ONEWRITER | the issuer (every map edit) | **Exactly one box writes each master's files.** The four Cottonwood masters (08719286, 08134043, 08165601, 08480305) belong to the Alongside Schwab Box's map only. The 49F box's map holds 08242234, 08335338 and 08403355 only. C-ONBOARD refuses to add a master that another box's map already holds, so two boxes never write the same keys. FWD-7 covers a master newly opened to either box's login, written by that box alone. | a dry plan of either root lists no master held by the other |
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
6. **0824 and 0833 are out (v0.7, Andrew-direct ~16:3xZ).** This project no longer promises 0824's or 0833's history, or one path form
   for their files; their daily pulls are unchanged. Priority is the Cottonwood workstream (FWD-8) and 0840 (FWD-1, FWD-2).

## OPEN AT ANDREW (acts only he can do)

- **Silver, meta and `_ops` scope:** do they move to firm scope with bronze in the same cutover, or does bronze move alone? (The CVO's v0.4 item 4,
  open-calls row on the laptop list.) Since v0.7 this covers 0840 only. REC: all tiers in one cutover. If yes, the ratified-text half
  re-signs and silver joins the cutover.
- **0833: CLOSED ~16:4xZ.** Andrew, verbatim: "1.) Yes that is correct." 0833 is out with 0824.
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

Later rounds enrich: 0840's full backfill (FWD-2), the held-days record (FWD-3), and the onboarding path (FWD-7). Since v0.7 the Cottonwood
workstream and 0840 come first; no round cuts work for 0824 or 0833.

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
  - S3 `opal-data-assets`, prefix `schwab/08403355/bronze/` (the move) and the builder's `schwab/49financial/bronze/` and
    `schwab/cottonwood/bronze/` (the landing and the backfill); `schwab/08242234/` and `schwab/08335338/` are not written;
  - the deployed bd-tree code under `s3://opal-data-bd/code/`;
  - the Schwab box `i-0f3d57a97f14727af` (read and pull under the session lock);
  - the box role's IAM statements in `canonical-schwab-ec2`.
- **Portal:** none.
- **Repo:** the key function and its mirror, every reader the census names, the puller, the Terraform root, and this tree.

## CHANGE LOG

- **v0.7 (~16:4xZ 2026-10-20):** on Andrew-direct ~16:3xZ ("I dont care about that 0824, I want the new Cottonwood accounts taken care of and the 0840 tax sma account sorted out"). ENDPOINT: FWD-2, FWD-4 and FWD-6 narrow to 0840 (and Cottonwood for FWD-4). CONTRACTS: C-SCOPE holds five masters; C-KEYFORM applies the firm form per master and withdraws the legacy-member rule; C-MOVE moves 0840 only; C-BACKFILL drops the 0824 and 0833 floors. Decision 6 states what is no longer promised. 0833 goes to OPEN AT ANDREW. The ENDPOINT changed, so the ratified-text half re-signs.
- **v0.6 (~16:2xZ 2026-10-20):** C-KEYFORM adds the legacy-member rule on the round-2 slug's decision (option A, with the master read from the move's attribution manifest, never defaulted from the missing prefix). CONTRACTS changed, so the ratified-text half re-signs.
- **v0.5 (~15:0xZ 2026-10-20):** the CVO's v0.4 items 1-3 (`L4R_REVIEW_NFRA_SCHWABBF_v0.4_RATIFIED_TEXT_20261020.md` @6efc50424f). C-SCOPE now holds seven masters in two groups. C-NAMES prints the firm-form measurement. C-ALONGSIDE's IAM is enumerated by file-name master prefix inside the shared firm folder. Item 4 (whether silver, meta and `_ops` also move to firm scope) is put to Andrew; C-RECORD and silver stay as written until he answers.
- **v0.4 (~14:4xZ 2026-10-20):** the CVO's four items from its v0.2 refusal (`org/tier1_exec/3.0.0_SA_CVO/deliverables/L4R_REVIEW_NFRA_SCHWABBF_v0.2_RATIFIED_TEXT_20261020.md` @c495f17652). C-ONEWRITER is added (one writer per master; FWD-7 and FWD-8 cannot both write a Cottonwood prefix). C-ALONGSIDE gains the builder-named copy (no typed ternary) and the branch for an unseen master. The FWD-8 history paragraph moves out of ENDPOINT into this log: FWD-8 was ADDED at v0.2 on Andrew-direct ~13:4xZ and CONFIRMED at ~14:3xZ ("thats fine", `ANDREW_DIRECT_20261020_143xZ_SCHWABBF_FWD8_CONFIRMED_BUILD_VENDOR_FIRM_PATHS.md`).
- **v0.3 (~14:3xZ 2026-10-20):** on Andrew-direct ~14:3xZ, C-KEYFORM moves to vendor/firm scope
  (`schwab/49financial/...`, `schwab/cottonwood/...`), with masters told apart by the vendor file name. He confirmed FWD-8 ("thats fine").
  The CONTRACTS changed, so the ratified-text half re-signs.
- **v0.2 (~13:5xZ 2026-10-20), same sitting:** C-ALONGSIDE is an exact copy of the 49F Schwab Box, labeled Alongside, and Andrew RDPs in for the
  first sign-in (his words, quoted in the row and under OPEN AT ANDREW).
- **v0.2 (~13:5xZ 2026-10-20):** on Andrew-direct ~13:4xZ, FWD-8 ADDED, C-ALONGSIDE added, the Alongside workstream named, and two acts
  added to OPEN AT ANDREW (confirm FWD-8; the box's first sign-in). The ENDPOINT changed, so the ratified-text half re-signs.

- **v0.1 (~13:1xZ 2026-10-20):** first draft on the confirmed endpoint and Andrew's three answers. Contracts C-SCOPE to C-ONBOARD; decisions
  1-5; the old-key delete held for Andrew's confirmation.
