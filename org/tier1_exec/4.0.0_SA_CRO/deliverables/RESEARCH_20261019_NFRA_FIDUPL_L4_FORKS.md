# RESEARCH 2026-10-19 -- NFRA_FIDUPL L4 forks: past patterns, cited

**Seat:** 4.0.0_SA_CRO~FIDELITY (dell1) | **Asked by:** 1.0.0_SA_CTO~DELL1, msg 8426 (three forks + Quo)
**Project:** NFRA_FIDUPL (`org/missions/D8/NFRA/NFRA_FIDUPL`) | **Brief:** `docs/briefs/auto-fidelity-uploader-brief-20261019.md`
**Claim marks:** each finding is marked **measured** (the artifact or live state was read) or **inferred** (from prose
or reasoning). Nothing was written to AWS. The Quo read was GET-only.

## Q0 -- Quo: is the consumer located, and can it read inbound SMS on that line? YES, measured live

- **Consumer:** `org/tier1_exec/4.0.0_SA_CRO/scripts/google_oauth_handler.py`, built for the Google 2FA flow. Its API
  notes (measured 2026-09-10, `:14-24`):
  - The raw key goes in `Authorization` with no Bearer prefix.
  - **A browser-shaped User-Agent is required.** A default urllib UA gets a Cloudflare 403 (error code 1010) before
    Quo's auth check is reached.
  - `/v1/messages` requires a `participants` filter.
- **Exercise, 2026-10-19 ~18:15Z, GET only, values not printed** (measured):
  - `GET /v1/phone-numbers` returns 200 with **two** numbers: `PNEJ5tafLm +15616213066 "Operations"` (the line Andrew
    named) and `PNme8YAybw +15619336346 "Primary"`. The handler's comment says "exactly ONE number"; that was true on
    2026-09-10 and is stale now.
  - `GET /v1/conversations` on the Operations line returns 200, 6 conversations, one with participant `+18773721150`
    (Fidelity's OTP sender).
  - `GET /v1/messages?phoneNumberId=PNEJ5tafLm&participants[]=+18773721150` returns 200 with **2 incoming messages**,
    at 17:08:13Z and 17:23:34Z on 2026-10-19. Each is 131 characters and holds exactly one 6-digit token. These are
    the codes from Andrew's two sign-ins.
- **Latency** (measured): HAR2's SMS-send POST is at 17:23:33.154Z and Quo's `createdAt` is 17:23:34.780Z, so the code
  was readable **about 1.6 s** after the request. HAR2's code-submit PUT is at 17:23:40.914Z.
- **Implies:** Fidelity's sender is known, so the read can filter on it directly. Use `/v1/messages` with
  `participants[]=+18773721150` on `phoneNumberId=PNEJ5tafLm`, inside a recency window opened at the SMS-send step. The
  Google handler cannot filter that way because it does not know its sender, so it goes conversation-first. The
  recency window carries over unchanged. Don't let a second number on the key change which line is read.

## F1 -- Sign-in mechanism: real browser or raw HTTP?

**Precedent: always a real browser driven by Playwright, never raw HTTP replay.** The browser usually only mints the
session, and a REST or HTTP puller does the data.

- **Orion inf-exporter** (measured):
  - Headless Chromium through Playwright on Linux, with anti-automation flags, a Windows Chrome UA and
    `navigator.webdriver` hidden: `infra/aws/ec2/inf-exporter/src/stepwise/orion_export.ts:428-453`.
  - Saves Playwright's cookie state to S3. Orion's remember-device cookie means the SMS code is asked for only about
    every 30-90 days (`:13-15`).
  - The code relay is a person typing into a token-gated phone form; a Lambda writes it to S3 and the box polls
    (`infra/aws/lambda/inf-otp-relay/lambda_function.py:5-22`).
  - **Live today:** runs at 09:50Z and 21:00Z daily; 2026-10-19 09:51Z reads `JWT_CAPTURED`, "No OTP challenge".
- **Black Diamond** (measured):
  - Playwright Chromium on Linux. Without the anti-detection settings SS&C returned "Access Denied"
    (`infra/aws/ec2/bd-exporter/docs/WORKING_WORKFLOW.md:12-39`).
  - The runbook handles "EC2 IP Blocked by Cloudflare" by a stop/start for a new IP
    (`infra/aws/ec2/bd-exporter/terraform/QUICK_COMMANDS.md:135-146`).
  - The 49F auto-login reads the screens with a vision model (`infra/aws/ec2/bd-49f-auto-login/bd_49f_auto_login.js:1-19`).
  - Its residential proxy was dropped on Andrew's word on 2026-06-25, and it now uses the plain AWS IP
    (`secret-ids.env:34-37`).
  - The OTP arrives by email through the gateway, with a 120 s window that separates the two firms' codes.
  - Last full login 2026-09-28. A 15-minute keepalive Lambda holds the session.
- **Data harvest** (measured): headed real Chrome with one persistent profile per publisher
  (`lib/opal_data_harvest/tab_transport.py:1-5, 98-99`). It has met DataDome and PerimeterX, with solver code in
  `lib/opal_data_harvest/verification.py:235-296`.
- **No estate precedent** against Akamai Bot Manager, ThreatMetrix or cfa, and none where SMS is demanded at **every**
  login with no remember-device escape.
- **Implies:** use a real browser, Playwright with a persistent profile or saved state, to mint the session. Then call
  the two JSON/GET endpoints (status.json, downloadExport.do) inside that session, which is the inf-exporter split.
  Orion's saved-cookie shortcut does not help here: the captures showed an SMS code on every sign-in (inferred from
  HAR2). Whether a persisted Wealthscape device cookie suppresses the code is **untested**, and is worth one exercise.

## F2 -- Reuse the Schwab box or a new box?

- **Every auto-login box in the estate** (measured) is a dedicated Linux t3, with no inbound ports in its security
  group, run by SSM only, started on demand and stopped after the run: inf-exporter, bd-49f and cot. The 49F box is a
  separate sibling of cot for firm separation (`infra/aws/ec2/EC2_MANIFEST.json:94, :581`).
- **The Schwab box is the exception** (measured): Windows, always on, **RDP 3389 open** to one range
  (`EC2_MANIFEST.json:541` and its live security group). It runs Windows because the SI2 desktop app's DLLs and its
  vault-held refresh token require it (`data/assets/docs/SCHWAB_BOX_ARCHETYPE.md:23, :36`). Fidelity has no such
  dependency (inferred).
- **Sharing:** the estate resolves collisions with a session lock and staggered schedules: Schwab's lockfile at
  `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1:144-148, :187`; BD's staggered logins at
  `infra/aws/terraform/bd-pipeline/bd-49f-session-chain.tf:44-60`. No ledger ruling on one box per vendor versus shared
  (651 ledger files searched, 0 hits).
- **ThreatMetrix's local probe of 3389, 5900 and 5939** (measured in HAR2) targets exactly the Schwab box's open RDP.
  A Linux box with no inbound ports, run by SSM, presents none of them (inferred).
- **Implies:** a new dedicated Linux box, SSM-only, started on demand. The schedule, lock discipline and manifests
  follow the Schwab archetype. The OS and host follow the auto-login precedent. Andrew asked for "the same structure we
  did for schwab". A reading where structure means the chain (EventBridge, SSM, puller, raw bronze, manifests) and not
  the Windows host is the CTO's to rule. Flagged, not adjudicated.

## F3 -- Credential home: per-user vault or Secrets Manager?

- **Estate default: Secrets Manager**, read through the box's IAM role, with only secret-ID pointers on the box
  (measured):
  - Orion: `orion/credentials` (`infra/aws/ec2/inf-exporter/inf-jwt-fetch.sh:44-53`). The design says never pass
    them as environment variables (`docs/architecture/ADVI_INFLEC_BRONZERUN.md:477`), but the script does at `:59-61`.
    That is drift, and Fidelity should not copy it.
  - BD: `blackdiamond/49f/credentials`, with the session written back to `blackdiamond/49f/session`
    (`secret-ids.env:10-19`).
  - Harvest: one secret per publisher (`lib/opal_data_harvest/credentials.py:17-30`).
- **The Schwab vault is a special case** (measured): it holds a refresh token that the installed SI2 app manages, not
  a typed password, and the archetype ties it to the execution identity
  (`SCHWAB_BOX_ARCHETYPE.md:23, :36, :85`). No ruling prefers the vault in general.
- **Implies:** Secrets Manager. The Wealthscape username and password go in one secret, and the Quo key is the
  existing `quo/api-key`. Both are read by the box role and scoped narrowly, with names from `lib/opal_naming.py`.
  Note that the Schwab box role's `secret:schwab/*` prefix grant is self-flagged as a hazard (`secrets.tf:11-13`), so
  don't repeat a prefix wildcard.

## F4 (added) -- the tenancy of the Fidelity scope, owed before any address resolves

- **Done** (measured): the `fidelity` VENDOR system row, `infra/logic/registry/systems.json`, commit a492c648da.
  Validation passes (56 system rows, 15 scope rows, 0 warnings).
- **Open** (measured): `address("fidelity", ...)` now refuses only because the scope has no row.
- **Why the scope row can't be written yet:** the export's domain is **ALONGSIDE, LLC** (Export Status screenshot).
  Andrew describes Alongside as the umbrella that Inflection, Cottonwood and 49 Financial "are all part of". A MASTER
  row requires exactly one `firm` (`scopes.json` `_about.row_fields`). The Schwab masters are FIRM tenancy under
  `49financial`. A file set holding several firms' accounts fits no existing row shape without one of these:
  - a new FIRM-like `alongside` scope, which is a new tenant;
  - a COMPOSITE-tenancy scope, as `global` is;
  - a split by firm at landing.

  Each touches the cross-firm rule (CLAUDE.md NEVER: another firm's data in a pipeline tree). That is the CTO's L4
  ruling, and possibly Andrew's.
- **Not measured:** how many of the 4,959 accounts belong to each partner firm. The `.naa` / `account.txt` fields
  that might carry the firm (rep code, branch, custom fields) were not profiled.

## Did not check

- Any automated attempt against Wealthscape. None was made.
- Whether a persisted Wealthscape device cookie skips the SMS step.
- The Wealthscape Terms of Use.
- The hour of the recurring scheduled export (first observable in the 2026-10-20 Export Status rows).
