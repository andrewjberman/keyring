# BRIEF: a scripted, scheduled refresh of the Security Scanner universe data

**Author** `4.0.0_SA_CRO~Z` -- **Date** 2026-09-24 (measured 03:46Z-04:0xZ, device OPAL_BLOOMBERG) -- **Mode** NEW --
**Consumer** `/endpoint --forward` at L2 (`1.0.0_SA_CTO`).

**Andrew-direct at this terminal, 2026-09-24 ~03:4xZ, verbatim:** *"There is a script that reruns the 'Security
Scanner' universe data. I know we must have it somewhere; it's Yang's. ... I want to see if we can find that so we
can refresh that data in the scanner."* then *"write up the brief for the scripted refresh."*

**Mechanism constraint that binds this brief (R-21 @`b390c36444`, Andrew-direct ~03:2xZ, verbatim):** *"the pull
should be deterministic/scripted in nature like the existing pull, i do not like the idea of relying on an agent for
something a script can do way better."* Vendor egress is granted broadly on authority; the mechanism is a script
with a trigger, never an agent turn.

---

## PART I -- THE OUTCOME TERRITORY

### O1 -- THE CANDIDATE THREAD. A scanner user opens Security Scanner and sees a vintage newer than 2026-08-06 that no person uploaded

One person (the analyst who runs screens in the portal; Andrew stands in), one journey: sign in, open
`/security-scanner`, pick the S&P 500 universe with the default factor set, read the `asOf` on the header. It is a
date later than 2026-08-06, and the record shows the export that produced it was pulled and landed by a scheduled
script, with no hand upload on the DataRefresh page. Coarse grain: one universe, default screen, no re-weighting.

### O2 -- An operator can re-run the export for a named as-of and get the same artifact twice

The same person, or the seat that owns the schedule, runs the producer by hand for a stated date and gets an
export whose digest matches the scheduled run's digest for the same FactSet data. "Deterministic" is disputable
here: two runs, one date, one digest, or a stated reason why FactSet's data moved between them.

### O3 -- An operator can read which export, which script version and which run produced the served vintage

From the served manifest (the estate already appends a `screening_excel` entry to `json/latest/manifest.json`) a
person reads the export key, the run stamp, and the script's own version or digest, without opening CloudWatch.
Today the manifest names the file; it does not name the producer.

### O4 -- A failed or empty pull is a visible state on the DataRefresh page, not silence

When the pull does not land (FactSet unreachable, entitlement refused, empty screen, changed columns) the
DataRefresh status surface the portal already has for scanner uploads shows FAILED with the reason, and the served
`latest/` is left as it was. This is a status object the page reads, not an alert: the monitor and alarm moratorium
stands, and nothing new sends.

### O5 -- An operator sees a column-set change in the export before it is served

The processor derives the scoring factors as "every column not in a fixed exclusion set", so a FactSet screen that
gains or loses a column silently changes the factor set. Before the new export is copied into the trigger prefix, a
person can read a diff of its header row against the prior export's header row and, where the sets differ, the run
stops at that point with the diff recorded. The screen definition itself (the DIVZ / IDVZ screen's column list) is
versioned beside the script so that diff has a named baseline.

### O6 -- The AMGT peers ranker and the Posture comparable read the new vintage on their next batch with no code change

`lib/research/peers/universe.py` reads the six `universe_data.json` files and prints their `asOf` as the universe
vintage on every peer set. After a refresh, the next peers batch prints the new date and the Peers tab's "universe
vintage" line shows it. The person who checks is the Peers tab reader; the test is the date on the screen.

### O7 -- An analyst can request an off-cycle refresh through the same script

Between scheduled fires, an analyst who needs a fresher screen runs one command (or asks the owning seat to) and
the same producer lands the export through the same path, with the same provenance. An ad-hoc run is a QA act; the
scheduled fire remains the production event.

### O8 -- The old hand-upload path still works and is not removed

The DataRefresh page's `*screening*.xlsx` upload keeps working as the fallback for a month when FactSet's export
cannot be scripted. A person uploading by hand sees the same processing and the same provenance shape. Retiring it
is a later decision, not this brief's.

---

## PART II -- WHERE THE BOUNDARY SITS

**This work owns:** the export PRODUCER (the script that obtains `Screening_DIVZ_IDVZ_{asOf}.xlsx` from FactSet),
its TRIGGER (a scheduled task on a host that has FactSet access), its PROVENANCE (digest, version, run stamp into
the existing manifest entry), the pre-serve HEADER DIFF (O5), the screen definition file (O5), and the ledger entry
for the first scheduled fire.

**This work relies on and does not change:**
- `opal-security-scanner-processor` (the S3-triggered Lambda that turns the export into the six universes' JSON;
  project `SSCN_PORTAL`, PRD `docs/architecture/SECURITY_SCANNER_PRD.md`, contract `docs/architecture/SSCN_DATA_CONTRACT.md`).
- `opal-data-refresh-api` (owner `0.5.0_AE_OpalETL`): the `screening_excel` routing in `handle_trigger`, the
  presigned `POST /security-scanner/upload-url`, the SSCN status record.
- The portal Security Scanner page (`portal/src/pages/SecurityScanner/`, three scoped routes) and the DataRefresh
  Upload tab.
- The AMGT consumers: `lib/research/peers/universe.py` (project `AMGT_RESAPP`, closer contract
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_COMPLETION_20260923/CONTRACT.md`), the Posture comparable, and the
  open design fork on registering the scanner member space as a third crosswalk source (R-23).
- The terminal box's schedule ownership: `0.0.3_BG_BBGTerminal` was named owner of that box's schedules at R-21.
  Whether FactSet is reachable from that box is an open question (Part VII), so the host may differ.

**Sibling projects named:** `SSCN_PORTAL`, `SSCN_DIVDEF`, `SSCN_PRICOL`, `AMGT_RESAPP`, and the terminal box's
existing `OPAL_BBGTML_daily_pull` schedule family.

---

## PART III -- THE QUALITATIVE BAR

- **Freshness a reader can dispute:** a Peers tab reader who sees "universe vintage 2026-08-06" today sees a date
  inside the last scheduled window after this lands, and can name which run put it there.
- **Determinism a reviewer can dispute:** two runs on one date, one digest, or a reason. A run whose output cannot
  be re-produced from the script and its inputs is not scripted in the sense Andrew asked for.
- **Silence a reader can dispute:** when the pull fails, the DataRefresh page says so where a person already looks
  for scanner status. "It just did not update" is the failure this bar excludes.
- **No agent in the loop a grader can dispute:** the artifact of record carries a script digest and a scheduled-task
  run, both attributable from git and the ledger. A vintage that arrived by an agent's hand does not pass.

No numbers are set here. Cadence, retention of prior vintages and the header-diff tolerance are step 4 and 5 calls.

---

## PART IV -- THE SUBSTRATE: what exists, measured

1. **The producer today is a person.** The PRD's refresh section reads "Manual upload via presigned PUT URL ... S3
   event triggers processing Lambda." Five uploads exist in `s3://opal-data-portal-v2/security_scanner/uploads/`:
   2026-02-26, 05-18, 05-19, 05-21 and 08-06 (LastModified 2026-08-07T19:00Z). The PRD calls the cadence monthly;
   the measured cadence is five uploads in seven months with a three-month gap before the last.
2. **The processing half is built, deployed and idempotent by key.** `opal-security-scanner-processor` (python3.12,
   2048 MB, 300 s, code @2026-08-07T21:38Z) derives `asOf` from the key, replaces FactSet's `42` sentinel, derives
   scoring columns dynamically, and writes `json/security_scanner/{asOf}/...` and `latest/...` for six universes plus
   `factor_metadata.json`, then appends a `screening_excel` entry to `json/latest/manifest.json`. Latest outputs are
   stamped 2026-08-07T21:59Z. Nothing in it needs to change for O1.
3. **The upload half is built.** `opal-data-refresh-api` copies a pending `*screening*.xlsx` to
   `security_scanner/uploads/{asOf}/Screening_DIVZ_IDVZ_{asOf}.xlsx`, deriving `asOf` from the filename's YYYYMMDD,
   and records an `SSCN_EXECUTION` row for status polling. A presigned PUT route exists beside it. Either entry
   point serves a scripted producer without a new route.
4. **Yang's script is a workbook updater, not an export producer.** `quick_update_weights.py` (latest copy
   2025-11-11 on Andrew's OneDrive under `Desktop/ajb_workspace/models/factor_scanner/`; reference copy in
   `docs/architecture/security-scanner-source/V0_quick_update_weights.py`; launcher `02_MODEL_REFRESH.bat`) reads a
   `data_tables/Screening_DIVZ_IDVZ_*.xlsx` already on disk and rewrites `Factor_Scanning_Model.xlsm`. It consumes
   the export. The export comes from FactSet's Universal Screening report (the processor's own comment names the
   report header rows). The repo's `models/factor_scanner` is a submodule pointer (`c59b266adf`), empty on this
   device.
5. **No FactSet client exists in the estate.** A definition-band census for `factset` over 72,149 files returns 4
   hits, all of them regexes over field prefixes in the corpus extractor or unrelated page captures; a filename census
   returns 0. There is no API client, no credential path and no scheduled FactSet task anywhere in the repo.
6. **The reference scheduled producer is on this box.** `OPAL_BBGTML_daily_pull` is a Windows scheduled task,
   daily 07:00 local, running `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd` under the interactive
   logon of the terminal user; last run 2026-09-23 07:00:01 with `LastTaskResult 50` (read, not interpreted here).
   R-21 named this family as the shape Andrew wants and `0.0.3_BG_BBGTerminal` as the owner of that box's schedules.
7. **The consumers are two and both read `latest/`.** The portal page through three scoped routes, and
   `lib/research/peers/universe.py` through `SCANNER_PREFIX` and the factor metadata key, which then feeds the
   peers ranker, the Posture comparable and the R-23 crosswalk fork. The scanner's `asOf` is the peers ranker's
   `universe_vintage`, printed on every peer set.
8. **Canonical-pattern fit (Rule 30, LGIC).** The input key and the output keys already exist and are consumed;
   this brief adds no new S3 address or resource name. If the PRD chooses a versioned home for the screen definition
   file (O5) or a producer-run record, that address comes from `lib/opal_naming.py address()` and a registry row, per
   Rule 30. A scheduled task on a Windows box is outside the LGIC tier homes and is governed by the deploy ledger.

---

## PART V -- WHAT MUST BE TRUE, without sequencing it

- FactSet must be reachable by a script from some host on a schedule: an API (FactSet's screening or content APIs)
  or a headless export of the saved Universal Screening report. Which one exists for Opal's entitlement is unknown
  to this seat and is the first thing the PRD must establish (Part VII).
- A credential path for that access that a script can read and an agent never types: a secret on the host or in
  the estate's secret store, never in a turn.
- A host with that access and an owner for its schedule. If it is the terminal box, `0.0.3_BG_BBGTerminal` per
  R-21; if it is another machine, an owner is Andrew's to name.
- The saved screen (DIVZ / IDVZ) and its column list captured as a file so O5 has a baseline.
- The first scheduled fire is a production schedule: a deploy-ledger entry in
  `org/critical_paths/change_management/` opened before and closed after; ad-hoc QA runs before it are permitted and
  are not production evidence.
- The never-widen pair applies if the producer is ever pointed at anything other than the existing upload prefix;
  writing to the existing prefix the processor already watches is the same act a hand upload performs today.
- Vendor authority: covered by R-21's grant on authority; the mechanism constraint is the whole of what remains.

---

## PART VI -- STATUS, NOT OUTCOME-BEARING

Measured 2026-09-24 03:46Z-03:50Z unless stated:

- Served scanner vintage: `asOf 2026-08-06` on all six universes (outputs stamped 2026-08-07T21:59Z).
- Last upload: `security_scanner/uploads/2026-08-06/Screening_DIVZ_IDVZ_20260806.xlsx`, 9,147,939 bytes.
- Processor: `opal-security-scanner-processor` CodeSha256 `9ozYU1v8V0M0qVQmFn1Bo4KUmKB6HzVFNKWLCdfkkiY=` @2026-08-07T21:38Z.
- OneDrive (Andrew): `Factor_Scanning_Model.xlsm` 2025-11-03; `quick_update_weights.py` newest 2025-11-11; exports
  present only for 2025-10-27 and 2025-10-28; `02_MODEL_REFRESH.bat` runs `scripts\python\quick_update_weights.py`.
- Opal Capital team site: no workbook, no export (two searches, 0 and 1 unrelated hit).
- AMGT peers universe vintage in every served peer set: 2026-08-06 (from the Peers trace brief, 01:46Z).
- Existing scheduled producer on this box: `OPAL_BBGTML_daily_pull`, daily 07:00 local, last 2026-09-23 07:00:01.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- It does not know whether Opal's FactSet entitlement includes any programmatic export, nor which machine holds a
  FactSet login. That is the load-bearing unknown; if neither exists, O1 collapses to a reminder for a person and the
  brief should be re-cut.
- It did not open the FactSet screen or the workbook; the column list in the exports was read only through the
  processor's exclusion set and the 2026-05-18 probe recorded in the data contract.
- It did not interpret `LastTaskResult 50` on the existing Bloomberg pull; out of scope, noted for its owner.
- It did not measure whether the six universes' membership moved between 2026-05-21 and 2026-08-06, so it makes
  no claim about how stale "seven weeks" is in practice for the peers ranker.
- It did not assess FactSet licensing terms for scripted access; that is a vendor-terms question for Andrew.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/sscn-scripted-refresh-brief-20260924.md
  PROJECT           NONE-YET (sibling of SSCN_PORTAL; consumer AMGT_RESAPP)
  EXISTING PRD      docs/architecture/SECURITY_SCANNER_PRD.md (the processing half, unchanged)
  SIBLING PROJECTS  SSCN_PORTAL, SSCN_DIVDEF, SSCN_PRICOL, AMGT_RESAPP; terminal-box schedules (0.0.3_BG_BBGTerminal)
  PRIOR ART         opal-security-scanner-processor; opal-data-refresh-api screening_excel routing + presign route;
                    DataRefresh Upload tab; V0_quick_update_weights.py (workbook updater); OPAL_BBGTML_daily_pull
                    (scheduled-producer shape); R-21 mechanism constraint
  MEASURED AT       2026-09-24 03:46Z-03:50Z (S3, Lambda, OneDrive, team site, scheduled task)
  RECORDS           R-21 @b390c36444 (egress + mechanism); PEERS_END_TO_END_GAP_BRIEF_20260923.md (vintage coupling)
```
