# IRPT_YCDGEN -- YCharts direct-API generation, Opal-branded (kept answers, the element map, Opal's own script)

```json
{
 "project": "IRPT_YCDGEN",
 "directive": "D9",
 "fabric": "laptop",
 "prd_version": "v0.1",
 "step": 4,
 "brief_ref": "docs/briefs/irpt-ycharts-direct-generation-opal-branded-brief-20261003.md@45f673c2ea",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7"],
 "status": "RATIFIED"
}
```

Author: `1.0.0_SA_CTO`. D9 / IRPT / laptop. Register row `org/missions/D9/IRPT/IRPT_YCDGEN/project.json` @ec37b10ed2, with one
workstream issued by `2.0.0_SA_COO~Y`.

Brief: `docs/briefs/irpt-ycharts-direct-generation-opal-branded-brief-20261003.md` @45f673c2ea (`4.0.0_SA_CRO`, 195 lines). Andrew's
order, verbatim: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/RESEARCH/CRO_REQUEST_YCHARTS_DIRECT_GENERATION_20261003.md`
@ee801b0505. Endpoint: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_IRPT_YCHARTS_DIRECT_GENERATION_20261003.md`
@c3f2fb4bb3, CONFIRMED by Andrew ("all approved", record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261003_203xZ_ALL_APPROVED_YCHARTS_DIRECT_GEN_ENDPOINT_AND_SITEZ_SCOPE.md`).
The section below carries its outcomes unchanged.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  Andrew asks for an Overview report on one Cottonwood portfolio and opens an Opal-branded
         version that Opal's own script made, end to end on the live YCharts account
         DONE WHEN  EXERCISED -- one live run, ending in Andrew opening the report
         ACCEPT     Andrew opens an Opal-branded Overview for a real Cottonwood portfolio, made by Opal's
                    own script from YCharts answers it asked for live, and kept with those answers in
                    Opal's own store. Every number in it can be traced to one of those answers, or is
                    marked as not available. A step that used a saved example instead of asking YCharts
                    live fails the outcome
         SOURCE     brief PART I, "The candidate thread" (lines 22-27)

  FWD-2  An analyst can read what any YCharts call in a run gave back, from Opal's own store,
         without asking YCharts again
         DONE WHEN  EXERCISED -- an analyst has looked one up
         ACCEPT     for a finished run, an analyst picks any one call and sees what it gave back, whether
                    that was identifiers, data or a document, and whether it changed since the previous
                    run. Nothing kept contains a password, a login session or a key
         SOURCE     brief O1 (lines 29-33); PART V "No secret in any artifact"

  FWD-3  For each of the three report types, an analyst can point at anything on a YCharts-made
         report and say where it came from
         DONE WHEN  EXERCISED -- an analyst has traced one element of each type
         ACCEPT     for an Overview, a Comparison and a Multi report, every number, table and chart on the
                    page is either tied to a named YCharts answer, or listed plainly as something YCharts
                    works out only inside its own report builder. Nothing on the page is left unaccounted for
         SOURCE     brief O2 (lines 35-40)

  FWD-4  An analyst can make the Comparison and Multi reports too, Opal-branded, with Opal's own
         script
         DONE WHEN  EXERCISED -- one of each made and opened
         ACCEPT     for the same portfolio and comparisons, Opal's script makes a Comparison and a Multi
                    report in Opal's branding without YCharts' report builder. Anything YCharts works out
                    only inside its builder is rebuilt from data Opal holds, or left out with a note saying
                    so. It is never imitated
         SOURCE     brief O3 (lines 42-46); PART III item 5

  FWD-5  The Opal-made report and the answers behind it are found in Opal's own store, private to the
         client's firm
         DONE WHEN  EXERCISED -- an analyst has found one by its request
         ACCEPT     given a request, an analyst finds its report and every YCharts answer behind it in the
                    client firm's private area of Opal's store. Nobody at another firm can reach them, and
                    nothing the analyst needs exists only on YCharts
         SOURCE     brief O4 (lines 48-51); PART V "Client holdings stay inside their firm"

  FWD-6  A report run is something Andrew waits for at his desk, and every run shows where its time
         went
         DONE WHEN  EXERCISED -- Andrew has waited for one, and its timing record has been read
         ACCEPT     Andrew asks for a report and has it in the same sitting, without coming back to it
                    later. The run's record shows how long each stage took, with the time YCharts spent
                    working kept apart from the time Opal spent waiting
         SOURCE     brief O5 (lines 53-56); Andrew: "It has no need to take 15-20 minutes"

  FWD-7  For the same inputs, an analyst sees which figures on the YCharts report and the Opal report
         agree, and why any differ
         DONE WHEN  EXERCISED -- once for each of the three report types
         ACCEPT     for one report of each type, an analyst lists every figure that matches and every one
                    that differs, each difference with its reason: different dates, a different way of
                    calculating, or something only YCharts works out. It is a one-time check of the new
                    script, not a comparison that keeps running
         SOURCE     brief O6 (lines 58-61)
```

## PROVENANCE (outside the ratified section)

- FWD-1 is the brief's candidate thread (PART I). FWD-2 to FWD-7 are the brief's O1 to O6, one to one.
- **Andrew settled three readings.** On "the same endpoints", the CTO's reading is the YCharts endpoints that supply the
  report's DATA, stated with the DONE WHEN lines he confirmed. On egress, "COO~Y and any underlying agents have whitelisted
  egress to YCharts". On the subscription, "yes we are cleared for use". Record of the last two:
  `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/ANDREW_DIRECT_20261003_173xZ_YCHARTS_EGRESS_WHITELIST_AND_SUBSCRIPTION_CLEARED.md`
  @ce20ca6854.
- A word of his that amends an FWD becomes an addendum under the next unused id (FWD-8), or an in-place amendment. It is
  never a cell's choice.

## CONTRACTS

| Contract | Direction / owner | Binding agreement |
|---|---|---|
| C-SCOPE: research plus one thread | Andrew's order; the endpoint's boundaries | This project builds Opal's own path for calling YCharts, keeping the answers, mapping the report and generating it. It runs ON DEMAND only: no schedule, and no second producer beside the served YCharts generation (the standing veto on shadow and build-alongside pipelines). Research runs are QA runs, and their artifacts are never production evidence. Adoption of Opal generation is a later decision, and adopting it REPLACES the served path in the same window. |
| C-ENDPOINTS: "the same endpoints" | Andrew-confirmed reading 1 | The endpoints are the YCharts DATA endpoints that supply a report's figures. The `custom_pdf_reports` calls (template, upload, create, validate, generate, download; `recipe.py:1-45`) return identifiers, links and YCharts' own PDF (brief F2). They are mapped for FWD-3 as "identifiers" or "document" answers, and they are never the source of a figure in an Opal report. |
| C-VENDOR: who may call YCharts | Andrew's egress word | Only `2.0.0_SA_COO~Y` and its underlying agents (its workers, `0.9.0_WK_IRPT_YCDGEN~<n>`) make YCharts calls. The CTO, the CVO and the CRO grade from Opal's store and never call YCharts. A seat outside that scope needs his word. |
| C-SESSION: one session, one lease, one pace | IRPT_BCKEND (the served path owns the session and the lease); consumed | Every research call is made inside the served path's provider-account operation lease: the same key and the same store as `infra/aws/lambda/investor-reporting/ycharts/session/operation_lease.py`, composed through `resident_session.py`. The lease serializes research runs with `~Y`'s served runs, so the two never interleave. Its `next_allowed_at` keeps the call rate inside what the YCharts firewall tolerates (rows S233; batch 97). Sign-in stays Andrew's act. A firewall challenge or a lost session STOPS research: the run releases the lease, files a row and makes no retry storm. The served path keeps the session. This project adds no lock, no second session and no sign-in. |
| C-KEEP: every answer kept and labelled | this project | Each call of a run is kept as one object: the request (method, path, the body's keys, with every value that names a person, credential or session removed), the response bytes with any cookie, token or credential scrubbed, a shape label from the closed set `IDENTIFIERS`, `DATA`, `DOCUMENT` (rule 24: one axis, what the call gave back), the response's sha256, and `changed_since_previous` (`true`, `false` or `no_previous`, computed from the same call's previous kept sha256 for the same portfolio). A planted secret in a test response must be absent from the kept object, or the scrub fails. |
| C-STORE: addresses from the builder | CLAUDE.md rule 30; X10 | Three state tables in the client firm's bucket, keyed by the request. Builder output printed at L4 (2026-10-03 20:4xZ): `address('irpt','cottonwood','state','ycharts_responses','request=REQ-329a56182b2668d44a28c8d7', object='step=04_create.json')` -> `s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_responses/request=REQ-329a56182b2668d44a28c8d7/step=04_create.json`; `...,'ycharts_runs',...,object='run.json')` -> `s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_runs/request=REQ-329a56182b2668d44a28c8d7/run.json`; `...,'ycharts_opal_reports',...,object='overview.pdf')` -> `s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_opal_reports/request=REQ-329a56182b2668d44a28c8d7/overview.pdf`. The same calls with `49financial` or `inflection` give those firms' buckets. A request id with a slash is refused by the builder (READ at L4). The `bronze` tier is NOT used: for `cottonwood` it resolves to the shared bucket `opal-data-assets` (READ at L4), and kept answers carry client holdings. |
| C-REGISTER: the X10 policy row | this project, round 1, before the first write | No X10 family names YCharts answers today (brief F5; `infra/logic/registry/reporting_policies.json` READ at L4: PERFORMANCE_SOURCE_EVIDENCE names SmartX, Black Diamond and Orion only). Round 1 adds ONE policy row, `irpt-ycdgen-research`, with three families: `YCHARTS_RESPONSE` (state, `ycharts_responses`, json), `YCHARTS_RUN` (state, `ycharts_runs`, json) and `YCHARTS_OPAL_REPORT` (state, `ycharts_opal_reports`, pdf). Retention follows the sibling state families (`unreferenced_days` 30, `accepted_ceiling_days` 2555). The row lands before any object is written under those tables. |
| C-RUN: the run record | this project | `run.json` per request holds: the request (portfolio, template, comparisons, window), the lease's fencing token, one entry per call (step, kept object key, shape label, sha256, `changed_since_previous`), stage timings, and the trace from each report element to the answer and field it came from, or `NOT_AVAILABLE` with the reason. **Timing (FWD-6)** separates three clocks: YCharts working (request sent to last byte), Opal waiting (time held by `next_allowed_at`, the lease queue or a poll interval), and Opal building (layout and render). No time target is set in this PRD (brief PART VII). FWD-6's bar is Andrew's own sitting. |
| C-MAP: the element map | this project | For each report type (Overview 14141822, Comparison 14141824, Multi 14141847; `recipe.py:121-146`), every number, table and chart on a YCharts PDF of that type is listed with its source: a named data endpoint and field, or `BUILDER_ONLY` (YCharts computes it only inside its report builder). The map is drawn from the served path's RETAINED certified PDFs (family ORIGINAL_VENDOR_PDF), so mapping costs no generate call. A type with no retained PDF waits for `~Y`'s served run of that type under its own sequence; this project makes no extra generate call. The map file names element ids and sources only. Figure values stay in the firm's store. |
| C-BRAND: Opal's branding, not YCharts' | this project; reuse the export path's assets | The Opal report uses the approved brand asset set of the IRPT export path (`infra/aws/lambda/investor-reporting/export/bundle.py`: `render_options.brand_revision` and its approved assets). It carries no YCharts logo, layout imitation or YCharts wording beyond a plain source credit. The output is a PDF. Rendering touches no portal page, no portal deploy and no PROD export surface. |
| C-BUILDERONLY: never imitated | FWD-4; brief PART III item 5 | An element marked `BUILDER_ONLY` is either rebuilt from data Opal already holds, with its method stated in the run record, or left out with a line on the report saying it is not available. No element is approximated to look like YCharts' figure. |
| C-SECRET: no secret anywhere | law; brief PART V | No cookie, token, password, session or key appears in a kept object, a run record, a log, a commit or a message. The session is read in memory through the served path's broker and never written. Kept objects carry the scrub (C-KEEP). Grading reads the store, never the session. |
| C-FIRM: client data stays in its firm | law (CLAUDE.md section 5) | Uploaded holdings, kept answers, run records and reports live only in the client firm's bucket (C-STORE). No object of one firm is written under another firm's prefix. Git holds no client figure. The element map (C-MAP) and the side-by-side check (C-COMPARE) carry element ids, verdicts and reasons; their figure values are cited by store key. |
| C-COMPARE: one-time, per type | FWD-7; the standing veto on parity comparators | For one report of each type, the same inputs as a retained YCharts PDF. Each figure is listed as `MATCH` or `DIFFER`, and each DIFFER carries one reason from the closed set `AS_OF` (different dates), `CONVENTION` (a different way of calculating) or `BUILDER_ONLY`. It runs once per type and is recorded. Nothing schedules it, and no code path repeats it. |
| C-MORATORIUM: no alerts | law (CLAUDE.md section 5) | No alarm, SNS, SES send, freshness checker or monitor. A failed run is a row and a run record, never a notification. |
| C-DELIVERY: Andrew opens the report | FWD-1 | At run end, the runner prints the report's store key and a short-lived signed link for Andrew. The link is not stored, and its query string is never logged. No portal surface is built for this project. |

## 1. The arc

**Start.** One served YCharts generation path: seven calls, a 34-key generate body, YCharts' own PDF certified and retained. A
Multi report took 17 m 43 s, 15 m 19 s of it SUBMITTING, mostly Opal's paced waiting by inference (brief F7). Today, no kept
answer exists. No map from report elements to calls exists. Opal cannot brand a YCharts report, because the figures exist only
inside YCharts' PDF (F2).

**End.**
- Every YCharts call of a research run is kept in the client firm's private store, labelled and scrubbed.
- Every element of the three report types is traced to a data endpoint, or named as computed only inside YCharts.
- Opal's own script makes Overview, Comparison and Multi reports in Opal's branding from the data endpoints.
- Each run shows where its time went.
- A one-time check per type says which figures agree and why any differ.

## 2. THREAD -- FWD-1, one Cottonwood Overview end to end (round 1)

1. **Request.** Andrew names one Cottonwood portfolio for an Overview (template 14141822, no comparison, default window).
   The research runner records the request and acquires the operation lease (C-SESSION).
2. **Map (Overview only).** The Overview elements are traced from a retained certified Overview PDF (C-MAP). This names the
   data endpoints the thread must call. If no retained Overview exists, the map waits for `~Y`'s served Overview run.
3. **Live calls.** The runner calls those data endpoints for the portfolio, one at a time under the lease's pace. Each answer
   is kept and labelled at the builder's address (C-KEEP, C-STORE). This happens after the X10 row lands (C-REGISTER).
4. **Build.** Opal's script reads the kept answers from the store, never from a saved example, and lays out an Opal-branded
   Overview (C-BRAND, C-BUILDERONLY). It writes the PDF to `ycharts_opal_reports` and `run.json` with the element trace and
   the three clocks (C-RUN).
5. **Open.** Andrew opens the report from the printed link (C-DELIVERY) in the same sitting. An analyst picks one number and
   finds its answer in the store. A hop fed by a saved example fails the outcome.

Round 1 builds only this thread. The cells, the COO's to cut at L5:
- the X10 row, the keeper and the scrub test;
- the Overview map from a retained PDF;
- the runner inside the lease, with the run record;
- the Overview layout in Opal's branding.

Nothing outside this project blocks round 1, except a session Andrew must sign in to. That is his act, as today.

## 3. ENRICHMENT BACKLOG (ordered, one line each)

1. The Comparison map, then the Multi map, from retained certified PDFs (FWD-3).
2. Comparison and Multi layouts in Opal's branding; each `BUILDER_ONLY` element is rebuilt from held data or noted (FWD-4).
3. `changed_since_previous` exercised across two runs of the same portfolio, and an analyst look-up of one call (FWD-2).
4. The firm-private read: one report and its answers found by request; one other firm's seat refused (FWD-5).
5. The timing read: Andrew waits for one run, and an analyst reads its three clocks (FWD-6).
6. The one-time side-by-side check for each of the three types (FWD-7).
7. A second firm (49 Financial or Inflection) through the same path, only when a round-N analysis names it.

## 4. Engines (one row per engine)

| Engine | Serving shape | Role here | Deploy mechanics |
|---|---|---|---|
| the research runner and Opal generation script (NEW, `infra/aws/lambda/investor-reporting/ycharts/research/`) | an on-demand Python run in the resident session's environment, beside the served generator | calls, keeps, maps, builds, records | It reuses `session/resident_session.py`, `operation_lease.py` and the served recipe's request helpers (build ladder rung 2). It needs no new compute resource; a later round that needs one prints `name()` output in its order |
| the served YCharts generation (`ycharts/generate/`, the resident host) | IRPT_BCKEND's `~Y` Analysis workstream | the lease holder it shares; the retained PDFs it maps | IRPT_BCKEND; consumed, unchanged |
| the IRPT export path's brand assets (`export/bundle.py`) | the approved brand asset set by revision | C-BRAND | IRPT_BCKEND (`~P`); read only |
| the Opal gateway YCharts integration (`infra/aws/ec2/opal-gateway/app/integrations/ycharts/`) | four read-only data tools | prior art for data-endpoint calls (brief F3); read, not imported across the host boundary | NFRA_OPLGTW; consumed |
| the X10 register (`infra/logic/registry/reporting_policies.json`) | policy rows per family | C-REGISTER | this project adds one row; LGIC grammar |

## 5. WORKSTREAMS AND OWNERS

- **One workstream, issued by `2.0.0_SA_COO~Y`.** The egress word names that seat and its agents only (C-VENDOR). `~Y` also
  issues IRPT_BCKEND's Analysis workstream. A Tier-1 seat may hold several projects, and the lease (C-SESSION) is what keeps
  the two from colliding on the one session.
- **Write surface:** `infra/aws/lambda/investor-reporting/ycharts/research/` (new), its tests, the one X10 policy row, the three
  state tables of C-STORE, and `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/`.
- **Not written here:** `ycharts/generate/`, `ycharts/session/` and `export/`. A change any of them needs is a row routed to
  IRPT_BCKEND.
- **Owned elsewhere, named and NOT built here:**
  - the session, its sign-in and the lease (IRPT_BCKEND);
  - the retained PDFs (IRPT_BCKEND);
  - the brand assets (IRPT_BCKEND);
  - the gateway data tools (NFRA_OPLGTW).
- **L4-R:** the CVO (`3.0.0_SA_CVO`) signs the ratified-text half. The CRO wrote the brief, so the brief half is accepted by
  authorship (proportionate sign-off).

## 6. Rulings closed at L4 (no decide-first question enters L5)

1. "The same endpoints" means the data endpoints (C-ENDPOINTS). This reading was put to Andrew with the outcomes he confirmed.
2. Only `~Y` and its workers call YCharts (C-VENDOR). Graders read the store.
3. Research runs share the served path's lease, key and pace (C-SESSION). A firewall challenge stops research, never the served
   path. No retry loop outlives one lease.
4. The maps come from retained certified PDFs (C-MAP). This project makes no extra generate call. A type with no retained PDF
   waits for the served sequence.
5. Kept answers, run records and Opal reports live in the firm's bucket under the `state` tier (C-STORE). `bronze` is refused
   because it resolves to a shared bucket. The X10 row lands first (C-REGISTER).
6. Branding reuses the export path's approved brand assets, and the output is a PDF (C-BRAND). No portal page or PROD export
   surface is touched.
7. A `BUILDER_ONLY` element is rebuilt from held data with its method stated, or noted as not available. It is never imitated.
8. No time target is typed (brief PART VII). The run record measures three clocks, and FWD-6 is graded on Andrew's sitting.
9. On demand only: no schedule, no second production path, and no repeating comparison. Adoption is a later decision that
   replaces the served path in the same window.
10. Any new capability (a client-facing release, another firm by default, a schedule) is a PRD addendum under the next unused
    FWD id.

## 7. SURFACE MANIFEST (step 4 -> step 5)

`claim` names the evidence class. `measured` means read at L4 (2026-10-03 ~20:4xZ) by this seat. Paths cited from the brief
are `held`. NEW surfaces are `unmeasured`.

| id | outcome_ref | surface | claim | MEASURED-BY / evidence | lane | verb | depends_on | accept | bound |
|---|---|---|---|---|---|---|---|---|---|
| S01 | FWD-2, FWD-5 | X10 policy row `irpt-ycdgen-research` in `infra/logic/registry/reporting_policies.json` (NEW row) | measured (file; no YCharts family) | read at L4 | ~Y | wire | -- | FWD-5 | lands before any write |
| S02 | FWD-1, FWD-2 | the keeper: kept object, shape label, sha256, `changed_since_previous`, the scrub (NEW, `ycharts/research/`) | unmeasured | C-KEEP | ~Y | wire | S01 | FWD-2 | planted-secret test |
| S03 | FWD-1, FWD-6 | the runner inside the operation lease (`session/operation_lease.py`, `resident_session.py`) | measured (module headers) | read at L4 | ~Y | consume | -- | FWD-1 | same key, same store |
| S04 | FWD-1, FWD-3 | the Overview element map from a retained certified Overview PDF (ORIGINAL_VENDOR_PDF family) | unmeasured; no PDF opened (brief PART VII) | C-MAP | ~Y | measure | -- | FWD-3 | ids and sources only in git |
| S05 | FWD-1 | the YCharts data endpoints the map names, called live | unmeasured; the gateway's four tools are held (`integration.py:134-173`) | brief F3 | ~Y | wire | S03, S04 | FWD-1 | one at a time |
| S06 | FWD-1, FWD-6 | `run.json` with the element trace and the three clocks at `.../state/ycharts_runs/request=<REQ>/run.json` (builder) | unmeasured | `address()` printed at L4 | ~Y | wire | S02, S05 | FWD-6 | no secret |
| S07 | FWD-1, FWD-4 | Opal's Overview layout and PDF at `.../state/ycharts_opal_reports/request=<REQ>/overview.pdf` (builder), with the export path's brand assets (`bundle.py`) | unmeasured; `bundle.py` header held (brief F4) | C-BRAND | ~Y | wire | S06 | FWD-1 | never imitated |
| S08 | FWD-1 | the signed link printed at run end | unmeasured | C-DELIVERY | ~Y | wire | S07 | FWD-1 | not stored, not logged |
| S09 | FWD-3, FWD-4 | the Comparison and Multi maps and layouts | unmeasured | C-MAP, C-BUILDERONLY | ~Y | wire | S04, S07 | FWD-3, FWD-4 | retained PDFs only |
| S10 | FWD-5 | the firm-private read by request, and a refused foreign-firm read | unmeasured | C-FIRM | ~Y | verify | S06, S07 | FWD-5 | no cross-firm key |
| S11 | FWD-7 | the one-time side-by-side record per type (`deliverables/`) | unmeasured | C-COMPARE | ~Y | measure | S09 | FWD-7 | runs once per type |
| S12 | FWD-1..FWD-7 | NEW journey test across S01-S11, reading served artifacts in the store | unmeasured | the seven ACCEPT lines | verification | verify | S07 | all | reads the store, never YCharts |

MECE check: all 7 outcomes have at least one row. Every dependency named in section 5 either has a row (S03, S04 and S07
consume) or is named as owned elsewhere.

## 8. BRIEF COVERAGE -- content carried, not just cited

| Brief heading | Carried content | Consuming sections / surfaces |
|---|---|---|
| Order (Andrew's words) | four calls and a generation; kept and categorized answers; where each contract lands in the three types; Opal's own script on the same endpoints; bucketed on Opal's side | ENDPOINT; C-SCOPE, C-KEEP, C-MAP, C-STORE |
| PART I (thread, O1-O6) | the Cottonwood Overview thread; O1-O6 | ENDPOINT FWD-1..FWD-7; section 2 |
| PART II (boundary) | owns the research and its outputs; relies on the served path, the session, the gateway tools, the export path, X10; owns no terms, no vendor word, no client release | section 5; C-SESSION, C-BRAND, C-REGISTER; engines |
| PART III (the bar) | no number explained away; answers from Opal's store; a wait at the desk; no lost session; say so, never approximate | C-BUILDERONLY, C-RUN, C-SESSION; FWD-1, FWD-6 |
| PART IV F1-F2 | the seven-step contract; the calls return identifiers and links, never figures | C-ENDPOINTS; ruling 6.1 |
| PART IV F3-F4 | the gateway's data tools; the export path's brand revision | engines; C-BRAND; S05, S07 |
| PART IV F5 | no X10 family names YCharts answers | C-REGISTER; S01 |
| PART IV F6 | the 2026-09-11 captures and variant proof | prior art for S04 and S05; still unopened (PART VII) |
| PART IV F7 | 15 m 19 s SUBMITTING, mostly Opal's paced wait by inference; the firewall spacing | C-RUN's three clocks; C-SESSION's pace; ruling 6.8 |
| PART V | egress and terms answered; the session survives; no secret; builder addresses; firm privacy; the served path undisturbed | C-VENDOR, C-SESSION, C-SECRET, C-STORE, C-FIRM, C-SCOPE |
| PART VI | Y-3 timings; `~Y` V1 runs continue | arc; C-SESSION |
| PART VII | no PDF opened; endpoint coverage unknown; "same endpoints" interpreted; captures unopened; calculation time unmeasured; no time target | C-MAP (`BUILDER_ONLY` is a finding); ruling 6.1; ruling 6.8 |
