# NFRA_FIDUPL -- the auto_fidelity uploader: the Wealthscape daily export landed raw every morning in the Schwab window, signed in by itself

```json
{
 "project": "NFRA_FIDUPL",
 "directive": "D8",
 "fabric": "dell1",
 "prd_version": "v0.3",
 "step": 4,
 "brief_ref": "docs/briefs/auto-fidelity-uploader-brief-20261019.md@ea34e538ae",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8"],
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
FWD-2 and FWD-4 amended in place at v0.3). Andrew's
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
```

## CONTRACTS

| row | owner | rule | proven by |
|---|---|---|---|
| C-TOU | Andrew | **No automated Wealthscape sign-in is tried before Andrew's word on the Terms of Use for automated access** (`TOU_RIA.html`, brief Part V). Read-only design and Terraform authoring may proceed. | his recorded word, cited by the first sign-in cell |
| C-NAMES | `4.0.0_SA_CRO~FIDELITY` (registry rows); every cell (use) | **Every address and resource name is `lib/opal_naming.py` output** (rule 30). The Fidelity source key in `systems.json`, and its scope row(s), are added to `infra/logic/registry/` FIRST; `address("fidelity", ...)` refuses today (brief IV.5). A builder refusal is a missing row, never a hand-typed path. | `address()` and `name()` print every path and name in the Terraform and the puller |
| C-TENANCY | `4.0.0_SA_CRO~FIDELITY` (the scope row and gate edit); every landing cell (use) | **The ALONGSIDE file set lands raw once under a FIRM-tenancy scope `alongside`** (bucket `opal-data-alongside`, built by `name()`/`address()`), never COMPOSITE (R7: the rows are identified accounts). **The same commit adds `alongside` to `_CROSS_FIRM_FOREIGN_{BUCKETS,KEY_PREFIXES}` in both directions.** No other firm's tree reads it; any split by firm is downstream. Verdict: `GOVERNANCE_VERDICT_NFRA_FIDUPL_TENANCY_20261019.md` @bc07810172. | `address("alongside", ...)` prints the landing path; `.tools/ds-precommit-check.py` cross-firm guard refuses an `alongside` path in another firm's tree |
| C-SIGNIN | the sign-in cell | **A fresh sign-in every run** (4-hour inactivity limit and about 10-hour hard limit): password, then the `OTPSMS` factor, then the code read from Quo by API for the order's digital line, then authorize. The code is single-use and never logged. The driver (browser or raw HTTP) is ruled at L4 on CRO research. | one on-demand sign-in completed with no person typing |
| C-PULL | the pull cell | **Two calls, as Schwab's are:** the export status list (`status.json`, `iEtype=E`, the day's `dateString`), then `downloadExport.do` per file. All six v1.0.1 files: `account`, `position`, `balance`, `prices`, `security`, `transact`. | the run lists 6 and downloads 6 |
| C-RAW | the pull cell | **Raw landing only**, bytes exactly as Fidelity served them, with a sha256 per file recorded in the run record (the archetype's raw rule). No conversion in this project. | a stored file's sha equals the record's |
| C-DATE | the pull cell | **The business date comes from the file content** (the first field, for example `20261016` on Monday), never from the run date. Checked against `lib/trading_calendar.py`. A Monday export is served on demand for FWD-4 (2026-10-19's files hold 2026-10-16). A weekend re-serve of Friday is landed once under Friday or not at all, never as Saturday or Sunday. | FWD-4's on-demand pull of a Monday export |
| C-RECORD | the pull cell | **One run record per morning**, beside the Schwab manifests' shape (`_ops/daily_pull/`): files listed, downloaded, skipped or failed, the business date, and the failed step. The failure classes are distinct: sign-in refused, code never arrived, export not generated yet, download refused. It is only read, never sent (moratorium). | one good morning and one deliberately failed sign-in read |
| C-WINDOW | the schedule cell | **The schedule fires in the Schwab window** (05:45, 06:15 and 06:45 ET today, `monolith-daily-schedule.tf`), on Fidelity's own clock, never triggered by an upstream landing. Fidelity's generation hour is measured from the first recurring run (the 2026-10-20 status rows) before the cron is fixed. If Fidelity generates after the window, the record says "export not generated yet" and a later attempt in the window retries. | FWD-2's on-demand chain run and the live schedule read |
| C-ISOLATION | the box cell | **The Fidelity run never touches the Schwab SDD lockfile or the Schwab console session.** Reuse of the Schwab box, or a new box, is ruled at L4 on CRO research. Either way the Schwab run on a shared morning is byte-equal to a Schwab-only morning. | FWD-8's both-run morning |
| C-TF | the Terraform cell | **One Terraform root beside `infra/aws/terraform/canonical-schwab-ec2/`** names the schedule, the box or box role, the secret homes and the IAM grants. It is applied only by `safe-apply`, and nothing lives only in a console click. Credentials go to the vault or to Secrets Manager, ruled at L4. | a plan of the root with no `-var` reads No changes after the first apply |
| C-BACKFILL | the backfill cell | **History before 2026-10-19:** transactions by an on-demand date-range export; positions and balances through `Historical Prices and Positions Export` where entitled, otherwise named as unreachable. Every date Fidelity cannot supply is listed, not left as a silent gap. | one past window read |

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
   - **(d) C-TENANCY, ruled on `3.0.0_SA_CVO~DELL1`'s verdict @bc07810172:** a FIRM-tenancy scope `alongside`, bucket
     `opal-data-alongside`, plus the cross-firm gate edit in the same commit. The COMPOSITE REC was refused under R7: the rows are
     identified accounts whose attribution is unmeasured, not absent. Relayed to `4.0.0_SA_CRO~FIDELITY` and `2.0.0_SA_COO~P1`
     (msgs 8444, 8445).
5. **Quo, measured live by the CRO:** the read is `GET /v1/messages?phoneNumberId=<Operations line>&participants[]=<Fidelity sender>`
   inside a recency window opened at the SMS-send step. The code was readable about 1.6 s after the send. The key now carries two
   numbers, so the line is chosen by id, never by "the only number".

## OPEN AT ANDREW (acts only he can do)

- **Confirm the DONE WHEN lines** (open call on dell1).
- **His word on the Wealthscape Terms of Use for automated access (C-TOU),** before the first automated sign-in. The terms prohibit
  robots and agentic AI unless Fidelity approves (`RESEARCH_20261019_NFRA_FIDUPL_WEALTHSCAPE_TERMS_OF_USE.md` @e999b31f1f). The
  in-terms paths are Fidelity's written approval, an Integration Xchange transmission, or a person's daily download. Cell candidates 0,
  2 and 3 serve all three and proceed; only candidate 1 (the automated sign-in) waits on this act.

## CELL CANDIDATES (round 1 builds the FWD-1 thread; the issuer decomposes)

0. **Prerequisite (CRO):** the Fidelity source and scope registry rows (C-NAMES).
1. **Sign-in and OTP read** (C-SIGNIN), exercised once on demand after C-TOU. It ends with an authorized session and no person typing.
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

- **v0.3.1 (~18:5xZ):** the CVO's nit: FWD-4's dated parenthetical moved out of ENDPOINT into C-DATE; the DONE WHEN is unchanged in meaning.

- **v0.3 (~18:4xZ):** FWD-2 and FWD-4 DONE WHEN amended in place (the CVO's refusal @5c277d3352: both were waits), each now driven on
  demand; fork (d) ruled on the CVO's verdict @bc07810172 (FIRM scope `alongside`); C-TENANCY re-owned to the CRO's scope row; the Terms
  of Use finding @e999b31f1f recorded under C-TOU.

- **v0.2 (~18:3xZ):** forks (a) to (c) ruled on the CRO's cited research; (d) tenancy pitched to the CVO; the Quo read pinned by line id
  and sender.

- **v0.1 (~18:2xZ):** first draft, written while Andrew's endpoint confirmation and Terms of Use word are held, and while the CRO researches
  forks (a) to (d).
