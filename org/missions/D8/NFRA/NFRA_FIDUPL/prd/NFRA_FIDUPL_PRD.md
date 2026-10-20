# NFRA_FIDUPL -- the auto_fidelity uploader: the Wealthscape daily export landed raw every morning in the Schwab window, signed in by itself

```json
{
 "project": "NFRA_FIDUPL",
 "directive": "D8",
 "fabric": "dell1",
 "prd_version": "v0.5",
 "step": 4,
 "brief_ref": "docs/briefs/auto-fidelity-uploader-brief-20261019.md@ea34e538ae",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8", "FWD-9"],
 "status": "DRAFT"
}
```

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-19 ~18:2xZ.

**Placement:** DELL1, directive D8, macro NFRA. Registered @24f0400d63, sibling of `NFRA_AWSFTP`, which is on HOLD.

**Records (Andrew-direct, both recorded by `4.0.0_SA_CRO~FIDELITY`):**
- **~17:55Z,** `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261019_1755Z_AUTO_FIDELITY_UPLOADER_TERRAFORM.md`: "I would like to
  build out a terraform for auto_fidelity uploader, essentially taking the same structure we did for schwab and applying it to fidelity ... pull
  the relevant tables from it every morning at the same time that schwab does".
- **~18:05Z,** `ANDREW_DIRECT_20261019_1805Z_AUTO_FIDELITY_TOP_PRIORITY_DELL1.md`: "this is now the highest priority project on this box".

**Endpoint status:** written at L2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_NFRA_FIDUPL_20261019.md` @24f0400d63;
FWD-2 and FWD-4 amended in place at v0.3; FWD-9 added at v0.4). Andrew's
confirmation is an act on the box's open calls. This PRD goes to L4-R after he confirms; if he changes a line, ENDPOINT is re-pasted here.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  An Opal analyst opens the Fidelity Alongside book for the prior
         business day and finds the day's Fidelity files already there that
         morning, with nobody having signed in to Wealthscape to fetch them
         DONE WHEN  EXERCISED -- one live trace driven on demand: the uploader
                    signs in by itself, reads the text-message code by itself,
                    lists and downloads the day's files, and lands them; the
                    analyst then opens them. The first scheduled morning is the
                    organic case
         ACCEPT     The analyst can read that day's Fidelity accounts, positions,
                    balances, prices, securities and transactions, and can be shown
                    that no person signed in or typed a code for them; a step done
                    by hand fails it
         SOURCE     brief Part I, candidate thread; O1; O3

  FWD-2  The Fidelity files arrive in the same morning window as the Schwab
         files, every day
         DONE WHEN  EXERCISED -- the scheduled chain is started on demand by
                    the same trigger the schedule uses and lands the day's files
                    with their record; the live schedule is read and fires
                    inside the Schwab window; one run is started on demand for a
                    day Fidelity has not yet produced, and its record says so.
                    The first scheduled morning is the organic case
         ACCEPT     Someone reading the morning ingestion sees Fidelity and Schwab
                    land within the same window and reads them as one routine; if
                    Fidelity has not produced its files by then, the record says so
                    instead of the run quietly landing nothing
         SOURCE     brief O2; Part III second test; Part V first item

  FWD-3  Each morning, one record says whether Fidelity landed, and if not,
         which step stopped it
         DONE WHEN  EXERCISED -- a morning record is read, and one deliberately
                    failed sign-in is read as such
         ACCEPT     An operator reading one morning's record can tell what was
                    listed, downloaded, skipped or failed, and the business date it
                    holds; and on a bad morning whether to look at Fidelity, at the
                    text-message line, at the export schedule or at the box; it
                    sends no message to anyone, it is only there to be read
         SOURCE     brief O4; Part III third test

  FWD-4  Every file is filed under the business date it actually contains
         DONE WHEN  EXERCISED -- a Monday export, which holds Friday's data,
                    is pulled on demand and read; the same Friday files are
                    pulled a second time on demand and land once. The first
                    scheduled Monday is the organic case
         ACCEPT     Asking for a given business day returns the files whose content
                    is that day, and a weekend run that re-serves Friday's data does
                    not create a Saturday or Sunday that never traded
         SOURCE     brief O5

  FWD-5  The Fidelity files are kept as Fidelity sent them, in the same
         families of tables the Schwab work already converts
         DONE WHEN  APPLIED -- the landed families are compared with Schwab's
         ACCEPT     A data engineer extending the Schwab conversion to Fidelity
                    recognises the same kinds of tables (accounts, positions,
                    balances, transactions, securities, prices), finds them exactly
                    as Fidelity delivered them, and does not have to reverse-engineer
                    a screen
         SOURCE     brief O6; Part II (silver is a later project)

  FWD-6  Fidelity history from before the schedule started can be filled in
         DONE WHEN  EXERCISED -- one past window is fetched and read
         ACCEPT     An analyst can see Fidelity transactions from before the day the
                    schedule began, and positions and balances for earlier dates
                    wherever Fidelity can supply them; any dates Fidelity cannot
                    supply are named, not silently missing
         SOURCE     brief O7; Part V backfill item

  FWD-7  The whole uploader is set up and taken down from one place, beside
         the Schwab setup
         DONE WHEN  APPLIED -- the uploader is stood up from that one place
         ACCEPT     An engineer can read one setup that names the schedule, the
                    machine, where the logins are kept and what the uploader is
                    allowed to touch, and nothing about it exists only as a manual
                    console step
         SOURCE     brief O8; Andrew's order ("making a terraform around it")

  FWD-8  The Fidelity run never disturbs the Schwab morning pull
         DONE WHEN  EXERCISED -- both run on the same morning and Schwab's run
                    reads unchanged
         ACCEPT     On a morning when both run, the Schwab files land exactly as they
                    would have without Fidelity, and the Fidelity run waits for or
                    avoids anything the Schwab pull needs to itself
         SOURCE     brief Part II (the Schwab box is relied on and not changed);
                    Part V last item

  FWD-9  Each firm's Fidelity files sit in that firm's own place, never
         mixed with another firm's
         DONE WHEN  EXERCISED -- one day's files are landed on demand and each
                    firm's share is read in its own place, with any accounts
                    no firm claims listed
         ACCEPT     Someone opening Cottonwood's Fidelity files for a day finds only
                    Cottonwood accounts in them, and can see which accounts, if any,
                    could not be placed with a firm
         SOURCE     Andrew-direct ~19:0xZ ("pulling them to the relevant bronze
                    buckets per client"; "it is based off the G Number")
```

## CONTRACTS

| row | owner | rule | proven by |
|---|---|---|---|
| C-TOU | Andrew | **MET, Andrew-direct ~19:0xZ:** "We can absolutely do the automated sign in, we are authorized users of the application" (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_190xZ_FIDUPL_SIGNIN_AUTHORIZED_RELAY_DELL1.md`; laptop primary 6e7a80f56f). The automated sign-in proceeds. | the record, cited by the first sign-in cell |
| C-NAMES | `4.0.0_SA_CRO~FIDELITY` (registry rows); every cell (use) | **Every address and resource name is `lib/opal_naming.py` output** (rule 30). The Fidelity source key in `systems.json`, and its scope row(s), are added to `infra/logic/registry/` FIRST; `address("fidelity", ...)` refuses today (brief IV.5). A builder refusal is a missing row, never a hand-typed path. | `address()` and `name()` print every path and name in the Terraform and the puller |
| C-TENANCY | `4.0.0_SA_CRO~FIDELITY` (scope rows and gate edits); every landing cell (use) | **Fidelity lands in `opal-data-assets` through the fidelity channel, never a new bucket** (Andrew-direct ~19:0xZ). Every path is `address('fidelity', <scope>, 'bronze', ...)`, and `opal-data-alongside` is not provisioned. **The split per firm runs on the G Number.** If each G number maps to one firm, that G number is a scope row under its firm and lands straight at `fidelity/<firm>/bronze`. If there is one G number, the full pull stages under the FIRM scope `alongside` (@bd84d81948) and is split afterwards on a named field, with unplaced accounts listed. The cross-firm gate covers every firm path in both directions. **Measured (`RESEARCH_20261019_NFRA_FIDUPL_G_NUMBERS.md` @14f422aa7d):** the login sees 31 G numbers, one firm each (13 map to Opal's three firms, 1 is the Alongside umbrella, 17 map to firms with no registry row); 0 of 5,007 accounts in the standard files carry one. **RULED: stage the full pull under `fidelity/alongside`** (his fallback). The first exercised sign-in captures two reads: whether the export wizard filters by G number (then one profile per Opal firm lands direct and the others are never pulled) and whether the custom `account.txt` carries a G number column (then split on it). **Andrew-direct ~19:05Z, VERBATIM: "We should land all of it so we have it ready."** (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261019_1905Z_FIDUPL_LAND_ALL_FIRMS.md` @ed9b24e509). The full pull lands, every G number included; this answers the laptop CTO's hold (msg 8483) and the CVO's question (@6b6d997e08). **RULED (home):** the accounts of the 17 non-registry G numbers stay raw under `fidelity/alongside`; a firm scope row is added only when Opal names a use for that firm. The three Opal firms are split to `fidelity/<firm>/bronze` (FWD-9). **v0.4.4, Andrew-direct 2026-10-20 ~13:3xZ (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261020_133xZ_COTBOOKS_NO_BD_DEPENDENCY_CUSTODIAN_FIRST.md` @7fb4f70e80), VERBATIM: "backfill off the G Numbers and create daily pulls per each G Number, various of which is the primary and advisor specific Cottonwood G Numbers".** Opal has now named a use for Cottonwood (ADVI_COTBOOKS, its first BD-free case study). So Cottonwood's seven G numbers get Cottonwood scope rows and land at Cottonwood's own firm prefix, unless they are already among the three Opal firms. The numbers are listed masked in the record, and in full in `tmp/cotbooks/` on dell1, off git. **Per G number:** if FU-x-1's probe reads that the export filters by G number, the daily pull runs once per named G number; otherwise the full pull is split on the G number. The VM Wealth Partners G numbers are not named and stay staged. **v0.4.5, Andrew-direct 2026-10-20 ~14:55Z (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261020_1455Z_FIDUPL_PER_G_DAILY_AND_MAX_BACKFILL.md` @b329e1c5f3): "Scheduled Daily downloads of each fact table by g-number into ... opal-data-assets/fidelity/~, split out to the relevant firms per each G Number".** This supersedes v0.4.3's "non-registry firms stay raw under `fidelity/alongside`" and v0.4.4's VM Wealth Partners line. **Every G number the login sees lands under its own firm's prefix.** For each firm without a registry row, `4.0.0_SA_CRO~FIDELITY` adds a FIRM scope row named from the G-number label, and the cross-firm gate is regenerated in the same commit. An account seen under two G numbers of one firm lands ONCE for that firm (row D1-S6). An account seen under G numbers of two firms is listed, never landed twice. | `address()` prints every landing path; `.tools/ds-precommit-check.py` refuses a foreign firm path; FWD-9's read |
| C-SIGNIN | the sign-in cell | **A fresh sign-in every run** (4-hour inactivity limit and about 10-hour hard limit): password, then the `OTPSMS` factor, then the code read from Quo by API for the order's digital line, then authorize. The code is single-use and never logged. The driver (browser or raw HTTP) is ruled at L4 on CRO research. | one on-demand sign-in completed with no person typing |
| C-PULL | the pull cell | **Two calls, as Schwab's are:** the export status list (`status.json`, `iEtype=E`, the day's `dateString`), then `downloadExport.do` per file. All six v1.0.1 files: `account`, `position`, `balance`, `prices`, `security`, `transact`. | the run lists 6 and downloads 6 |
| C-RAW | the pull cell | **Raw landing only**, bytes exactly as Fidelity served them, with a sha256 per file recorded in the run record (the archetype's raw rule). No conversion in this project. | a stored file's sha equals the record's |
| C-DATE | the pull cell | **The business date comes from the file content** (the first field, for example `20261016` on Monday), never from the run date. Checked against `lib/trading_calendar.py`. A Monday export is served on demand for FWD-4 (2026-10-19's files hold 2026-10-16). A weekend re-serve of Friday is landed once under Friday or not at all, never as Saturday or Sunday. | FWD-4's on-demand pull of a Monday export |
| C-RECORD | the pull cell | **One run record per morning**, beside the Schwab manifests' shape (`_ops/daily_pull/`): files listed, downloaded, skipped or failed, the business date, and the failed step. The failure classes are distinct: sign-in refused, code never arrived, export not generated yet, download refused. It is only read, never sent (moratorium). | one good morning and one deliberately failed sign-in read |
| C-WINDOW | the schedule cell | **The schedule fires in the Schwab window** (05:45, 06:15 and 06:45 ET today, `monolith-daily-schedule.tf`), on Fidelity's own clock, never triggered by an upstream landing. Fidelity's generation hour is measured from the first recurring run (the 2026-10-20 status rows) before the cron is fixed. If Fidelity generates after the window, the record says "export not generated yet" and a later attempt in the window retries. | FWD-2's on-demand chain run and the live schedule read |
| C-ISOLATION | the box cell | **The Fidelity run never touches the Schwab SDD lockfile or the Schwab console session.** Reuse of the Schwab box, or a new box, is ruled at L4 on CRO research. Either way the Schwab run on a shared morning is byte-equal to a Schwab-only morning. | FWD-8's both-run morning |
| C-TF | the Terraform cell | **One Terraform root beside `infra/aws/terraform/canonical-schwab-ec2/`** names the schedule, the box or box role, the secret homes and the IAM grants. It is applied only by `safe-apply`, and nothing lives only in a console click. Credentials go to the vault or to Secrets Manager, ruled at L4. | a plan of the root with no `-var` reads No changes after the first apply |
| C-BACKFILL | the backfill cell | **History before 2026-10-19:** transactions by an on-demand date-range export; positions and balances through `Historical Prices and Positions Export` where entitled, otherwise named as unreachable. Every date Fidelity cannot supply is listed, not left as a silent gap. **v0.4.4: the backfill runs per G number, Cottonwood's seven first** (Andrew-direct @7fb4f70e80). Its read names, for each G number, the earliest date it reached. **v0.4.5: the backfill is "as far back as possible" (Andrew @b329e1c5f3) for every G number.** The read names, for each G number and each file, the earliest date served and the reason it stops: an entitlement refusal, Fidelity's retention limit, or the account's open date. | one past window read |

## THE DECISIONS -- CLOSED AT L4

1. **The box archetype holds (C-SIGNIN):** the session is stateful, so per `SCHWAB_BOX_ARCHETYPE.md:27` a box beats a Lambda (brief IV.3).
2. **Raw only, and silver is a later project:** the landing must not foreclose reusing the Schwab silver (FWD-5). It does not build it.
3. **No new alert (C-RECORD):** the run record is the whole failure surface.
4. **Forks ruled at L4 on CRO research** (`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261019_NFRA_FIDUPL_L4_FORKS.md` @b99a64cd4e):
   - **(a) Sign-in: a real browser, Playwright, mints the session, and the two JSON/GET calls run inside it.** This is the Orion
     inf-exporter split (`orion_export.ts:428-453`). Every estate auto-login is a real browser and none replays raw HTTP. A persistent
     profile or saved state is kept. Whether a persisted device cookie skips the SMS step is exercised once and recorded; it is never
     assumed.
   - **(b) A new dedicated Linux box, SSM-only, with no inbound ports, started on demand and stopped after the run.** Every auto-login
     box takes this shape (`EC2_MANIFEST.json:94, :581`). The Schwab box is Windows only because SI2's DLLs and vault token need it,
     and Fidelity has neither. Its open RDP is exactly what ThreatMetrix probes. **"The same structure we did for schwab" is read as
     the CHAIN: EventBridge, then SSM, then the puller, then raw bronze and the run manifests, on the Schwab schedule and lock
     discipline. It is not the Windows host.** This also settles C-ISOLATION: the run touches no part of the Schwab box.
   - **(c) Credentials in Secrets Manager:** one Wealthscape secret plus the existing `quo/api-key`, read by the box role with
     per-secret grants. There are no prefix wildcards (the `secret:schwab/*` hazard, `secrets.tf:11-13`) and secrets are never passed
     as environment variables (the Orion drift, `inf-jwt-fetch.sh:59-61`). Names come from the builder.
   - **(d) C-TENANCY, ruled on `3.0.0_SA_CVO~DELL1`'s verdict @bc07810172 and then narrowed by Andrew's word at ~19:0xZ:** FIRM
     tenancy, never COMPOSITE. The landing is in `opal-data-assets`, not the bucket `opal-data-alongside`, and the split runs per firm
     on the G Number (C-TENANCY, FWD-9). The verdict's own text said a FIRM-tenancy scope `alongside`, bucket `opal-data-alongside`,
     plus the cross-firm gate edit in the same commit. The COMPOSITE REC was refused under R7: the rows are
     identified accounts whose attribution is unmeasured, not absent. Relayed to `4.0.0_SA_CRO~FIDELITY` and `2.0.0_SA_COO~P1`
     (msgs 8444, 8445).
5. **Quo, measured live by the CRO:** the read is `GET /v1/messages?phoneNumberId=<Operations line>&participants[]=<Fidelity sender>`
   inside a recency window opened at the SMS-send step. The code was readable about 1.6 s after the send. The key now carries two
   numbers, so the line is chosen by id, never by "the only number".

## OPEN AT ANDREW (acts only he can do)

- **Confirm the DONE WHEN lines** (open call on dell1).
- **Confirm FWD-9**, added at v0.4 on his word, with the other eight (the same open call).

## CELL CANDIDATES (round 1 builds the FWD-1 thread; the issuer decomposes)

0. **Prerequisite (CRO):** the Fidelity source and scope registry rows (C-NAMES).
1. **Sign-in and OTP read** (C-SIGNIN), exercised once on demand (C-TOU met). It ends with an authorized session and no person typing.
2. **List, download and land raw, with the run record** (C-PULL, C-RAW, C-DATE, C-RECORD), driven on demand. The analyst then opens the six
   files: this is FWD-1's trace.
3. **The Terraform root and the schedule** (C-TF, C-WINDOW, C-ISOLATION), after 1 and 2 run.

Later rounds enrich: the backfill (C-BACKFILL), the both-run morning (FWD-8), the on-demand Monday pull of 2026-10-19's files (FWD-4), and
the on-demand chain run with the live schedule read (FWD-2).

## PATHS

- **This project:** `org/missions/D8/NFRA/NFRA_FIDUPL/`.
- **Prior art, read at HEAD by the issuer before the first cell:**
  - `infra/aws/terraform/canonical-schwab-ec2/` (`main.tf`, `iam.tf`, `monolith-iam.tf`, `monolith-daily-schedule.tf`, `secrets.tf`,
    `kms.tf`);
  - `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1`;
  - `data/assets/docs/SCHWAB_BOX_ARCHETYPE.md` and `SCHWAB_AUTO_PULL_DESIGN.md`;
  - `infra/aws/lambda/inf-otp-relay/lambda_function.py`;
  - the research doc `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261019_FIDELITY_WEALTHSCAPE_HAR_ENDPOINT_MAP.md` (addenda 1-2).

## SURFACE MANIFEST

- **AWS:** a new Terraform root (name from the builder), with:
  - an EventBridge schedule;
  - a box or box role;
  - secret homes for the Wealthscape credentials and, if needed, a Quo read grant;
  - a bronze landing whose address comes from `address()` after C-NAMES.
- **Portal:** none.
- **Repo:** this tree, the new root, the puller, and the registry rows.

## CHANGE LOG

- **v0.4.6 (2026-10-20 ~20:5xZ):** Andrew-direct (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261020_205xZ_FIDUPL_ALL_SWITCHER_G_NUMBERS_AND_SIGNIN_RECOVERY.md`):
  - coverage is every G number the G Number Switcher lists, read at each run;
  - the agent recovers the full browser sign-in when the trust token is no longer accepted, once per run and recorded, never
    looped.
  - CONTRACTS (C-TENANCY, C-SIGNIN); the ENDPOINT is unchanged.

- **v0.4.5 (2026-10-20 ~15:0xZ):** Andrew-direct @b329e1c5f3. Every G number is split to its own firm, with a FIRM scope row for
  each firm not yet registered, and lands once per firm. The backfill goes as far back as possible for every G number, and each stop
  is named. CONTRACTS half; the ENDPOINT is unchanged (FWD-9 and the backfill outcome already carry it).

- **v0.4.4 (2026-10-20 ~13:3xZ):** Andrew-direct @7fb4f70e80:
  - C-TENANCY names Cottonwood's seven G numbers for per-G daily pulls and a Cottonwood firm prefix;
  - C-BACKFILL runs per G number, Cottonwood's first.
  - The CONTRACTS half changed; the ENDPOINT is unchanged.

- **v0.4.3 (~19:0xZ):** Andrew-direct ~19:05Z "land all of it": the full pull lands; non-registry firms stay staged under `fidelity/alongside` (supersedes v0.4.2's hold).

- **v0.4.2 (~19:0xZ):** C-TENANCY: the first pull is limited to the 14 Opal G numbers, or the full-pull landing is held for Andrew's answer on non-Opal firms (laptop CTO msg 8483).

- **v0.4.1 (~19:0xZ):** C-TENANCY records the CRO's G-number measurement and rules staging under `fidelity/alongside` until the two reads land.

- **v0.4 (~19:0xZ):** on Andrew's relayed word (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_190xZ_FIDUPL_SIGNIN_AUTHORIZED_RELAY_DELL1.md`): C-TOU MET, so the automated sign-in proceeds; C-TENANCY now lands in
  `opal-data-assets` through the fidelity channel, split per firm on the G Number, with no new bucket; FWD-9 added at the next number.

- **v0.3.1 (~18:5xZ):** the CVO's nit: FWD-4's dated parenthetical moved out of ENDPOINT into C-DATE; the DONE WHEN is unchanged in meaning.

- **v0.3 (~18:4xZ):** FWD-2 and FWD-4 DONE WHEN amended in place (the CVO's refusal @5c277d3352: both were waits), each now driven on
  demand; fork (d) ruled on the CVO's verdict @bc07810172 (FIRM scope `alongside`); C-TENANCY re-owned to the CRO's scope row; the Terms
  of Use finding @e999b31f1f recorded under C-TOU.

- **v0.2 (~18:3xZ):** forks (a) to (c) ruled on the CRO's cited research; (d) tenancy pitched to the CVO; the Quo read pinned by line id
  and sender.

- **v0.1 (~18:2xZ):** first draft, written while Andrew's endpoint confirmation and Terms of Use word are held, and while the CRO researches
  forks (a) to (d).
