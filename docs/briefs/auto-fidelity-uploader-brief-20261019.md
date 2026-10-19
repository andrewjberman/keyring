# BRIEF -- auto_fidelity uploader: the Wealthscape daily export, landed every morning like Auto-Schwab

**Author:** `4.0.0_SA_CRO~FIDELITY` (dell1) | **Date:** 2026-10-19 | **Mode:** NEW
**Order:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261019_1755Z_AUTO_FIDELITY_UPLOADER_TERRAFORM.md`
(verbatim). Andrew asked for Terraform for an `auto_fidelity` uploader that takes the Schwab structure and applies it to
Fidelity, pulling the relevant tables every morning at the same time as Schwab.
**Research behind it:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261019_FIDELITY_WEALTHSCAPE_HAR_ENDPOINT_MAP.md`
(the body plus addenda 1 and 2). Three HAR captures and the exported files were read on dell1. None of them is in the
repo.

---

## PART I -- THE OUTCOME TERRITORY

**Candidate thread (FWD-1):** an Opal analyst opens the Fidelity Alongside book for the prior business day and finds
the six custom-export tables already landed that morning. Nobody signed in to Wealthscape to fetch them. Scope: one
domain (ALONGSIDE, LLC), one export profile (v1.0.1 custom CSV), the default T-1 window.

### O1 -- The Fidelity book arrives before the workday without a person touching Wealthscape
An analyst who needs Fidelity accounts, positions, balances, prices, securities or transactions for the prior business
day finds them already in the bronze tree when they start. No one signed in, entered a code or clicked Download File.

### O2 -- The Fidelity pull runs in the same morning window as the Schwab pull
A person reading the morning ingestion sees Fidelity and Schwab land in the same window. Andrew's stated reason is
consistency of timing for that ingestion. Today Schwab's three master pulls fire at 05:45, 06:15 and 06:45 ET
(`infra/aws/terraform/canonical-schwab-ec2/monolith-daily-schedule.tf`).

### O3 -- The sign-in completes on its own, including the text-message code
An operator does not have to be awake at pull time. The box signs in to Wealthscape with the firm's credentials and
reads the one-time code itself. Fidelity sends the code by text from its sending line to the Quo digital line named in
the order, and the box reads it through the Quo API.

### O4 -- An operator can tell, every morning, whether Fidelity landed and why not if it did not
Someone checking the run reads one record for the morning. It says which files were listed, downloaded, skipped or
failed, which business date they carry, and which step failed if any did. It distinguishes the failures that need
different hands:
- sign-in refused;
- code never arrived;
- the export not generated yet;
- download refused.

This mirrors the Schwab run manifests (`schwab/{m}/_ops/daily_pull/`, `meta/pulls/`). It is a record the run writes
about itself, not a new alarm.

### O5 -- Each file is filed under the business date it actually holds
An analyst asking for business date D gets the files whose content says D. The custom export reuses the same file
names every day (`prices.txt`, `transact.txt`, ...), so the date has to come from the content (the first field reads
`20261016` for Friday's data pulled Monday). A weekend run that re-serves Friday's data does not create a false Saturday.

### O6 -- The Fidelity raw files are shaped so the Schwab data engineering can be reused downstream
A data engineer extending silver and gold to Fidelity starts from five raw families with known columns, the same
families Schwab's silver carries: accounts, positions, balances, transactions, securities and prices. They do not
reverse-engineer a screen scrape. Landing stays raw, as Schwab's does. Converting to silver is a downstream outcome
(Part II).

### O7 -- The history before the schedule started can be filled in
An analyst can see Fidelity transactions from before 2026-10-19, the day the schedule began. They can also see
positions and balances for earlier dates where Fidelity can supply them. The scheduled export only produces files from
its start date forward, and Export Status keeps a 120-day calendar of files that were actually generated.

### O8 -- The whole thing is stood up and torn down from Terraform, like the Schwab box
An engineer reads one Terraform root that names the schedule, the box, the credentials' homes and the grants for the
Fidelity uploader. It sits beside `infra/aws/terraform/canonical-schwab-ec2/`, and nothing about the uploader lives
only in a console click.

---

## PART II -- WHERE THE BOUNDARY SITS

| This project OWNS | This project RELIES ON, and does not change |
|---|---|
| The Fidelity retrieval: sign-in, OTP via Quo, list, download, land raw, run record | The Wealthscape scheduled export profile (v1.0.1) Andrew configured in Fidelity's UI |
| Its Terraform root, schedule, IAM, secret homes, box or box role | The Auto-Schwab box, its SDD session and its lockfile (`infra/aws/ec2/canonical-schwab-si2/`); if the box is shared, the Schwab pull must not be disturbed |
| The Fidelity bronze landing and its manifests | Quo (the digital phone provider) and Opal's existing API access to it |
| The backfill of pre-schedule history (O7) | The LGIC naming canon (`lib/opal_naming.py`, `infra/logic/registry/`) |

**Named siblings, not owned here:**
- **The official custodian feeds:** Fidelity Integration Xchange outbound transmission and Schwab server-to-server
  delivery (`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261019_CUSTODIAN_DIRECT_FEEDS_AND_FIDELITY_SAN.md`).
  This project is the interim path ahead of them, in Andrew's words. When the feed lands it should land in the same
  bronze tree, and this uploader retires.
- **Silver and gold for Fidelity.** A converter beside `opal-assets-silver-schwab` (registry keyed by source and feed,
  `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/silver_registry.py`) is the next project's work, not this
  one's. O6 only requires that the landing does not foreclose it.
- **The existing second-hand Fidelity paths.** Inflection's Fidelity accounts reach Opal via Orion, and "Fidelity IWS"
  rows via Black Diamond (`infra/logic/registry/catalog_fork_keys.json`). They are untouched, and reconciling them
  against this direct feed is a later question.

---

## PART III -- THE QUALITATIVE BAR

- A person who used to sign in to Wealthscape to get these files no longer does, on an ordinary morning.
- Someone comparing the Fidelity and Schwab morning landings reads them as one routine, not two different habits.
- On a morning that fails, the run record names the failed step clearly enough that the next person knows whether to
  look at Fidelity, at Quo, at the export schedule or at the box. They don't have to re-derive it from logs.
- A data engineer reading the landed files recognises the same families they already convert for Schwab.

No figures are set here. Run time, freshness frontier and volume are measured at L2-L4.

---

## PART IV -- THE SUBSTRATE: is this in a canonical pattern?

Findings, each with what was measured, on 2026-10-19:

1. **The pattern exists and is written down as reusable.** `data/assets/docs/SCHWAB_BOX_ARCHETYPE.md:4` says future
   partner-service REST-pull boxes follow it. Its rule at `:27` says to use this archetype when the feed needs a
   standing session that a persistent client must maintain, and to prefer a Lambda when the auth is a stateless
   request. Its rules at `:81-88`:
   - fail loudly on every "nothing to do" path;
   - check the trading calendar first;
   - run as the user who owns the credential;
   - lock the session box-wide;
   - land raw files only;
   - no "spike" names.

   The Schwab Terraform is `infra/aws/terraform/canonical-schwab-ec2/`: `main.tf`, `iam.tf`, `monolith-iam.tf`,
   `monolith-daily-schedule.tf`, `secrets.tf` and `kms.tf`. The chain runs EventBridge cron, then SSM, then a Windows
   scheduled task as Administrator, then the puller fetched from S3 `code/`.
2. **The Fidelity retrieval is two calls, as Schwab's is.** POST
   `/ssc/importexport/wc/channel/status/v1/status.json` with `{"iEtype":"E","dateString":...}` lists the day's
   generated files. GET `/ssc/importexport/wc/channel/export/v1/downloadExport.do?fileName&fileType&profileId&requestId`
   fetches one. The source is the research doc, addendum 2. Schwab uses `FetchDetails/SpecificFileDetails.aspx` plus
   `Download/SpecificFile.aspx` (`sdd-daily-pull.ps1:324`, `:449`).
3. **The auth is NOT Schwab-shaped, and this is the main design divergence.** Schwab rides a refresh token that has
   lasted about 10 months, re-read from the Windows vault. Fidelity's session has a 4-hour inactivity limit and an
   about 10-hour hard limit (`checkTimeoutTime.json`), so **every morning is a fresh sign-in**:
   1. password, at `ecaap.advisorchannel.com/user/factor/password/authentication`;
   2. an OTP factor chosen from `OTPSMS`, `OTPVOICE` and `OTPREP`;
   3. the SMS code submitted to `/user/factor/otp/sms/authentication`;
   4. `platform-authorization/api/v2/authorize`.

   No remember-device step appeared. On the archetype's own rule at `:27` this is the standing-session case, so the box
   pattern holds rather than a Lambda.
4. **Fidelity runs active bot and device defences that Schwab's SDD endpoint did not show.** The captures show:
   - Akamai Bot Manager (`_abck`, `bm_sz`, sensor POSTs);
   - Fidelity `cfa.fidelity.com` fingerprinting;
   - ThreatMetrix (`online-metrix.net`), which probes local ports including 3389 (RDP), 5900 (VNC) and 5939
     (TeamViewer).

   A Windows EC2 box administered over RDP is exactly what that probe looks for. Whether the sign-in is driven by a
   real browser or by raw HTTP is a design question for L4. The measured fact is that raw replay meets these defences.
5. **The naming builder refuses Fidelity today.** `lib/opal_naming.py address("fidelity", ...)` raises
   `source 'fidelity' is not a systems.json key`, and `infra/logic/registry/scopes.json` has no Alongside scope.
   Schwab's masters are MASTER-class scopes, tenancy FIRM, firm `49financial`. Schwab bronze resolves to
   `s3://opal-data-assets/schwab/08242234/bronze/...`. Under rule 30 these are missing registry rows to add, never
   hand-typed paths.
6. **The tenancy question is real.** The export's domain reads **ALONGSIDE, LLC**. Its book is 4,959 open accounts and
   $1,563.1M as of 16-Oct-2026. The Alongside umbrella spans several partner firms (Andrew, 2026-10-19: Inflection,
   Cottonwood, 49 Financial "are all part of" it). One file set therefore carries more than one firm's accounts. The
   cross-firm rule (CLAUDE.md, NEVER: another firm's data in a pipeline tree) and the FIRM tenancy model decide where
   that file lands and whether it is split. That is an L4 ruling, not a landing detail.
7. **The custom export is the better feed than the standard one.** v1.0.1 is CSV with every column, scheduled all 7
   days, and produces six files:

   | File | Columns |
   |---|---|
   | `account.txt` | 141 |
   | `position.txt` | 62 |
   | `balance.txt` | 43 |
   | `prices.txt` | 44 |
   | `security.txt` | 45 |
   | `transact.txt` | 66 |

   It includes balances, which the fixed-width Standard Format A set lacks. The standard `.ipn` positions reconciled to
   the book tile within 0.4% ($1,569.6M against $1,563.1M). Neither format carries open or realized tax lots, which
   Schwab's ULN/ULT/RLD do.
8. **Quo access and an OTP relay pattern already exist.** Secrets Manager holds `quo/api-key`, created on 2026-09-10.
   Its description reads "Quo (quo.com) API key -- used to read incoming SMS/text verification codes for Google 2FA
   during automated Sign-in-with-Google flows. Andrew-direct 2026-09-10". It is registered in
   `infra/logic/registry/resources.json:2771` under system `portal`. The estate also already runs OTP relays for
   automated custodian/vendor logins:
   - `infra/aws/lambda/inf-otp-relay/lambda_function.py`: the Orion inf-exporter. The OTP is written to S3 and an EC2
     Playwright job polls and consumes it, single use, then deletes it.
   - Secrets `blackdiamond/{49f,cot}/otp-relay` and `.../otp-gateway-token`: the Black Diamond auto-login box,
     described as the "inf/otp-relay pattern".

   **Reading the Wealthscape OTP from Quo is a new consumer of an existing credential and an existing pattern, not new
   ground.** The existing relays are fed by a person or a gateway. Reading straight from the Quo inbox would be new.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- The hour Fidelity generates the scheduled export each day falls before the Schwab window, or the "same time" outcome
  (O2) cannot be met as stated. The status row's `scheduledTimeDisp` is empty, so the hour is measured only from the
  first recurring run (the 2026-10-20 status rows). The run on 2026-10-19 fired at save time, 13:32 ET, and is not
  evidence of the schedule.
- Whether weekend runs re-serve Friday's data or produce nothing.
- A Quo API credential that can read inbound SMS on the named line, and its home under the naming canon.
- Wealthscape credentials held where the box can read them. The Schwab precedent is a per-user vault; Secrets Manager
  is the alternative. Which one is an L4 call.
- The Wealthscape Terms of Use reviewed for automated access (`TOU_RIA.html`, served in every capture, unread). This
  is Andrew's call; nothing here assumes the answer.
- Registry rows for the Fidelity source and its scope(s), per Part IV finding 5. The tenancy ruling per finding 6.
- Backfill reachability: transactions by an on-demand date-range export (the standard `.trn` covered 2026-05-26 to
  2026-10-16, so a range works). Positions and balances history through `Historical Prices and Positions Export` (an
  entitlement, not yet walked) or by rolling positions back through transactions.
- If the Schwab box is reused, the Fidelity run must not collide with the SDD lockfile or the Administrator console
  session the Schwab pull depends on.

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-10-19, 17:08Z to 17:50Z, from Andrew's captures and the export status response:

- Export profile v1.0.1 (custom CSV, every column, Mon-Sun) is saved and generated once at 17:32:04Z. Its six files
  were delivered between 17:32:07Z and 17:33:36Z. Profile v1.0.0 (Standard Format A, on demand) ran at 17:25Z.
- The book is 4,959 open accounts, $1,563.1M AUA, as of 16-Oct-2026. Domain ALONGSIDE, LLC.
- The OTP reached Andrew's line as an SMS from the Fidelity sending number named in the order. The capture shows the
  `OTPSMS` factor used.
- No Fidelity source, scope, bucket path, Terraform root or puller exists in the estate today (Part IV finding 5).

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **It does not confirm the Quo credential works for this line.** The secret exists (Part IV finding 8), but its value
  was not read and the Quo inbound-SMS read was not exercised. Whether the key's workspace includes the digital line
  named in the order was not checked. The key's existing consumer, the Google 2FA flow, is
  `org/tier1_exec/4.0.0_SA_CRO/scripts/google_oauth_handler.py` (comp-find DEF hit). That is the Quo inbound-SMS read to
  reuse; its logic was not reviewed here.
- It does not claim the recurring export hour, weekend behaviour, or the historical-positions export's shape. None was
  observed yet.
- It does not claim automated sign-in passes Fidelity's bot and device defences. Nothing automated has been tried.
- It did not read the Wealthscape Terms of Use.
- It does not decide box reuse vs a new box, browser-driven vs HTTP sign-in, or the tenancy split. Those are L4.
- The custom files' column semantics beyond `prices.txt` were not profiled. The other five custom files were not handed
  over; the column counts come from the export profile's column lists.

---

## REFS

```
  BRIEF PATH        docs/briefs/auto-fidelity-uploader-brief-20261019.md
  PROJECT           NONE-YET (CTO registers at L3)
  EXISTING PRD      NONE
  ORDER             org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261019_1755Z_AUTO_FIDELITY_UPLOADER_TERRAFORM.md
                    org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261019_1704Z_FIDELITY_WEALTHSCAPE_HAR_WALK.md
  RESEARCH          org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261019_FIDELITY_WEALTHSCAPE_HAR_ENDPOINT_MAP.md
                    org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261019_CUSTODIAN_DIRECT_FEEDS_AND_FIDELITY_SAN.md
  SIBLING PROJECTS  official custodian feeds (Integration Xchange / Schwab SFTP); Fidelity silver converter (not yet a project)
  PRIOR ART         infra/aws/terraform/canonical-schwab-ec2/ ; infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1 ;
                    data/assets/docs/SCHWAB_BOX_ARCHETYPE.md ; data/assets/docs/SCHWAB_AUTO_PULL_DESIGN.md ;
                    infra/aws/lambda/opal-assets/opal-assets-silver-schwab/ ;
                    org/tier1_exec/4.0.0_SA_CRO/scripts/google_oauth_handler.py (Quo SMS read) ;
                    infra/aws/lambda/inf-otp-relay/ (OTP relay) ;
                    org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_INFLEC.Q10.ds-fidelity-api-enrichment-assessment.md
  QUO SEARCH        secret quo/api-key (Secrets Manager, created 2026-09-10); resources.json:2771; inf-otp-relay Lambda
  MEASURED AT       2026-10-19 17:08Z-17:50Z (captures); 2026-10-19 ~18:00Z (repo + naming builder)
```
