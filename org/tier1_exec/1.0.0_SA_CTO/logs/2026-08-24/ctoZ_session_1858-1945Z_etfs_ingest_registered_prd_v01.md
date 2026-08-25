# 1.0.0_SA_CTO~Z -- session 18:58-19:45Z: launch on MSTR~Z's NO-BQL kickoff; ETFS_INGEST registered + stage-2 PRD v0.1; three source-grade findings that reshape the build

**archetype:** ARCHITECT
**secondary_archetypes:** SCRIBE, VALIDATE
**Seat:** site Z lane of 1.0.0_SA_CTO (PID 42992, broker :7800, Monitor `bmkwl1jnu` armed 19:00Z and confirmed running by `TaskOutput`; first `[INBOX]` event delivered the kickoff itself -- end-to-end proof of the arm).
**Commit:** `e2ba01dd27` -- **landed LOCAL on SITEZ, rides MSTR~Z's integration window** (`merge-base --is-ancestor` vs `origin/SITEZ` = NO at logging time).

## 1. Startup (org/XXX.md), measured not assumed

`/watcher`: NOT REGISTERED -> registered; no orphan for this serial (`ps` showed only MSTR~Z + BG streams, both under live wrappers); Monitor armed with the `/cygdrive/c` prefix (measured `test -d`); zero crons (`CronList` empty, per the launch order). A.1 serial file written; A.3 `PATH: 98 of 102 comp-tools resolve bare` + `comp-which` EXERCISED (banner produced); D hook present; E context set; B.1 `to-check --all --assignee 1.0.0_SA_CTO~Z` = 0 TOs (base CTO holds 6, none mine). `check-inbox` is not on PATH here -- `bash org/mcp/check-inbox.sh` works (noted, not chased). Audit-archive invoker ran: 14 INTEGRITY/COVERAGE lines, all pre-existing site-Z-vs-laptop log-file findings (RV-0057 F-001 class), none mine.

## 2. Andrew-direct words received this session (all via MSTR~Z, all already recorded + broadcast by them; quoted verbatim in the PRD s.0 and the project JSON)

Five words: NO BQL + hand off to CTO~Z + register + PRD + read-back loop (@78841bfa02) · bronze for both channels in `opal-data-assets`, canonical pattern from the start (@93d126c4aa) · D4 SITEZ until done · the full chain ground-up in pattern (bronze -> unified silver parquet -> unified gold parquet in `opal-data-etfs/gold/` -> platinum JSON in `opal-data-portal-v2`) · all relevant ETFs = DIVZ IDVZ PFDE PFOE (msgs 4830, 4831). Received-agent obligation (record + broadcast) was MSTR~Z's and is discharged by their commits/messages; I ACKed 4828/4829/4830/4831 on the READ clock.

## 3. What landed -- `e2ba01dd27`

`docs/architecture/ETFS_INGEST_PRD.md` (stage-2 purpose-level, 13 sections) · `org/projects/ETFS_INGEST.json` (`dep_stage: PRD`) · `REGISTRY.md` Active row · `ETFS_POSITIONING.json` cross-link (related + phase prefix). Validated: `registry-check` 0 malformed and the row renders; `prd-check` lists ETFS_INGEST with 6 PRD pointers; both JSONs load.

**Registration decision, stated:** NEW project code (his word *"register the project"*, twice) rather than "ETFS_POSITIONING round 2"; the PRD ports unchanged if he prefers the latter (call C5). Round 1's DONE consumes this project's DONE (the two promote conditions).

## 4. The three findings that change the build (each with its control; PRD s.3)

1. **The producer of `opal-data-etfs/silver/holdings` -- MSTR~Z's open question -- is the `etfs-netassets-daily` Lambda** (`lambda_function.py:117/:135/:159`, live env `ETFS_BUCKET=opal-data-etfs`, `cron(0 22 * * ? *)`), and its 17-column `HOLDINGS_COLUMNS` IS the "consistent output shape" both issuers already normalize into (filepoint `:624-633`, TrueShares `:464-473`). Three live consumers (L1 universe derivation, constituents leg 2, TO-1 gold).
2. **The deployed Lambda is older than its tree while the env flag is applied.** Package (`Code.Location` download, LastModified 2026-08-20T01:18:32Z, sha `tHeVS53p...`, 1083 lines): `fetch_trueshares_holdings` x1 (def `:420`), `TS_HOLDINGS_ENABLED` x1 (assignment `:381`). HEAD @4e5800fde0 (1126 lines): the call site `:550-559`. Positive control `fetch_filepoint` = 3 in BOTH copies (def + docstring mention + call). Live `get-function-configuration`: `TS_HOLDINGS_ENABLED=1`. **Rule 22a's specimen: every rung passes (plan, config, green scheduled run) on a code path the running bytes do not contain.** Each 22:00Z fire since 08-20 has silently forgone a day of DIVZ/IDVZ holdings. This is a class-OBSERVATION / standing-INERT channel item whose disarm IS the first build cell (a TF-only deploy, AE-class).
3. **The TrueShares sheet link IS in the bronze bytes we store.** `trueshares/{DIVZ,IDVZ}/bronze/netassets/20260823/*.html`: the Lambda's own `_TS_SHEET_RE` returns exactly 1 id per fund, on RAW and on `html.unescape`d text, byte-identical to the brief's URLs (`1csUjnC2fHqZQORGBccRy_ew0dgv-jpC_LOKdbjPwI9U` / `1H8LXhhQBSbQLK37-y5TPTvJsaeKfE2HVmVcRVpQHKh8`); mutant corpus (`docs.NOTGOOGLE.com`) = 0; positive control `>NAV<` = 3 / 5; negative token = 0. Anchor text in DIVZ: `<div class="button-wrapper"><a href="https://docs.google.com/spreadsheets/export?id=1csUjnC2fHqZQORGBccRy_ew0dgv-jpC_LOKdbjPwI9U&amp;exportFormat=csv`. **The brief's "injected client-side / do not grep the saved HTML" caution describes a different retrieval (an external curl, headers/URL not recorded) -- both observations can be true; the design binds to the Lambda's own fetch, which carries it.** Carried back to MSTR~Z WITH the anchor text (a correction carries the text, not a citation).

Also measured: two silvers / two producers / one bronze (readers of the `opal-data-assets` ETF silver trees: 22 hits / 27,945 files, 4 SURFACED, all converter/schema -- no in-repo consumer found); `opal-data-etfs/gold/` = 0 objects; identifier hazards (BBGID in PFDE's CUSIP column; IDVZ 44/44 bare US ADR tickers with CUSIP 44/44; SALXX in both issuers; Bloomberg count +1/+2).

## 5. Tensions surfaced (PRD s.6) and calls (s.7) -- none resolved silently

Gold home vs Rule 17b as amended 08-11 (his later word binds; a 17b AMENDMENT is routed to base CTO rather than a silent exception, because the 08-11 ruling was also his) · ETFS_CANON's live platinum artifact STAYS (NEVER#3; out of scope) · universe closed at four (the two site-Z scripts restating the list in code = an in-pattern cell, MSTR~Z's own finding) · no bronze for the Bloomberg API legs · unified-at-silver vs Rule 17 no-slimming (superset row) · **WHICH VEHICLE fetches TrueShares** -- base CTO's A4 (~15:5xZ) read his ~15:2xZ word as "vehicle moves to the site-Z script, Lambda call site retired"; his ~19:1xZ word endorsed the assets-bucket bronze pattern that only the Lambda produces. Rec: the Lambda (rung 2; no second standing path; both words satisfied). **Flagged for his confirmation via the read-back -- my reading of the breadth of two of his words, not an adjudication.** · the +1/+2 owner (issuer = truth for the list; Bloomberg count = a manifest `count_delta`).

## 6. Requests routed

- **MSTR~Z:** read-back (his instruction); D4 register edit (member-set add `ETFS_INGEST`; placement `SITEZ -- until the project is done`) to base MSTR; the three corrections with text; CVO~Z routing of the surprise items (s.12) once CVO~Z is seated.
- **Base CTO (via MSTR~Z bridge):** the Rule 17b amendment candidate (tension 1) -- proposing, not implementing.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| comp-find | `-i "silver/holdings"` (357/27,945) · `"holding_ticker"` (35) · assets-bucket raw (96; 19 SURFACED) · (i)-silver readers (22; 4 SURFACED) · `etfs-netassets-daily` (594) · TF env/schedule in `infra/aws/terraform/etfs-netassets` (11) · portal `sub_asset_class\|GICS` (23 / 9 files) · portal `GICS\|sub-categor` (43 / 412) | PASS -- every census with its denominator; one BRE-pipe miss self-caught (`\|` -> bare `\|`) and re-run |
| comp-which | exercised at A.3 | banner produced (forwarder RAN) |
| registry-check / prd-check | post-registration | 0 malformed; ETFS_INGEST renders in both |
| comp-aws | `comp-aws etfs-netassets-daily` | WRONG CALL FORM (takes subcommands); schedule read via comp-find on the TF instead -- gap noted, not chased |
| raw aws (rail-checked, 5 markers) | `get-function-configuration`, package download, `s3 ls`/`cp` on three buckets | PASS -- Rule 22a CODE/APPLIED layer reads no comp-tool covers |
| safe-commit | `-F` msgfile authored with the Write tool (F-010) | PASS @e2ba01dd27; risk-reflex HOLD on REGISTRY.md cites LD-0326:56 (a row MOVE); this was an INSERT -- read, proceeded |

## Blockers

**None at this seat.** At Andrew via MSTR~Z's read-back: C2 gold home · C3 "sub-categories" vocabulary · C4 TrueShares vehicle · C5 registration form. At MSTR (base): the D4 row edit. Surfaced not chased: `check-inbox` not on PATH at this seat; `comp-aws` call-form gap for "what schedules Lambda X".

## Current State -- handoff for a fresh seat

- **ETFS_INGEST** `dep_stage: PRD` @e2ba01dd27 (LOCAL). Awaiting MSTR~Z read-back -> Andrew's spawn word -> COO~Z stage 3. First decomp cell the PRD argues for: the TF-only deploy of @4e5800fde0 (AE-class, on the owning device) -- it fills the DIVZ/IDVZ shells with zero new code.
- **In flight, untouched:** L1 daily pull (L1-2 1/3; A2 on the observed close, ceiling 09-04); constituents script first SCHEDULED fire 08-25 07:00 local; TO-5 committed-not-applied; TO-4 Half 2 wired-not-deployed; ETFS_POSITIONING promote STAGED-HELD.
- **Live seats on site Z:** MSTR~Z, BG (holding), CTO~Z. Zero crons.

## Next Steps

- **[0.0.0_AB_MSTR~Z]** read the PRD back against the five words; route the D4 row edit; bridge C2-C5 to Andrew; route the three corrections + surprise items.
- **[Andrew]** C2-C5; the spawn word for COO~Z + executing ~Z seats.
- **[2.0.0_SA_COO~Z on spawn]** stage 3 decomp over PRD s.4 territory; cohort + certifier classes declared at open (CVO~Z).
- **[1.0.0_SA_CTO~Z]** remain up; amend the PRD on the read-back; route the Rule 17b amendment candidate to base CTO on his C2 word.
