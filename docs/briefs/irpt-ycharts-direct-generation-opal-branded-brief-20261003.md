# L1 BRIEF -- YCharts direct-API generation, Opal-branded

- **Author:** `4.0.0_SA_CRO` (L1), 2026-10-03 17:3xZ. **Mode:** NEW (greenfield research; the served YCharts path it
  studies is a sibling, not this project's to change).
- **Order:** Andrew-direct at the `2.0.0_SA_COO~Y` terminal, 2026-10-03 ~17:0xZ, relayed by msg 104648. His words,
  verbatim, are recorded in the request file
  `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/RESEARCH/CRO_REQUEST_YCHARTS_DIRECT_GENERATION_20261003.md`
  @`ee801b0505`:

  > It has no need to take 15-20 minutes. this is four api calls and a generation. I honestly feel like we should be
  > able to run the api calls, persist and categorize the response shape per api call, and identify from the 3
  > generation types where and how those contracts are materialized in the actual generated export file (via parsing
  > or otherwise). then once we assess how that is constructed, we run the generation with our own custom script that
  > uses the same endpoints but opal branded. also those outputs have to be bucketed on our side of course.

- **Consumer:** `1.0.0_SA_CTO`, `/endpoint --forward` at L2.

---

## PART I -- THE OUTCOME TERRITORY

### The candidate thread (FWD-1 candidate)

Andrew asks for an **Overview** report (template 14141822, no comparison) on **one Cottonwood portfolio**, default
window. Opal's own script makes the YCharts calls, keeps every response, builds an Opal-branded report from them and
files both in Opal's bucket. Andrew opens that report while he is still at his desk, and an analyst can trace any figure
in it to the response it came from. Comparison and Multi follow in the rounds after this thread works.

### O1 -- An analyst reads any one YCharts call's response from Opal's own store, without calling YCharts again

For each call in a run, the response is kept (secrets scrubbed) and labelled with its shape. At minimum, the label says
whether the call returns identifiers, data, or a document. The analyst can tell what each call gave back and whether it
changed since the last run.

### O2 -- An analyst points at any figure, table or chart in a YCharts-generated report and names where it came from

The three generation types are covered: Overview (14141822, 0 comparisons), Comparison (14141824, 1) and Multi
(14141847, 2-5) (`infra/aws/lambda/investor-reporting/ycharts/generate/recipe.py:121-146`). For every element of each
type's PDF, the analyst can name the call and field that supplies it. Where no call returns it, the element is marked
as computed inside YCharts' own generation. That mark is a finding in its own right, not a gap to hide.

### O3 -- An analyst produces the same report, Opal-branded, with Opal's own script

For the same portfolio and comparisons, Opal's script calls the endpoints O2 named and lays out an Overview, Comparison
or Multi document in Opal's branding. YCharts' report generator is not used. Elements O2 marked as computed only inside
YCharts are either rebuilt from data Opal holds or plainly absent. They are never imitated.

### O4 -- An analyst finds the Opal-generated report, and the responses that fed it, in Opal's bucket under the client's firm

The report and its inputs sit at Opal addresses, private to the client's firm, and are found by the request that made
them. Nothing an analyst needs lives only in YCharts.

### O5 -- Andrew gets the report while he waits for it, and an analyst can see where a run's time went

A run reads as one wait, not as something Andrew checks back on later. Every run shows its time stage by stage, with
YCharts' own working time separated from Opal's waits. Andrew: "It has no need to take 15-20 minutes."

### O6 -- An analyst lays the YCharts report and the Opal report side by side and sees which figures agree

For the same inputs, the analyst sees each figure that matches and each that differs, with the reason (data as-of,
calculation convention, or an element YCharts computes and Opal does not).

---

## PART II -- WHERE THE BOUNDARY SITS

**This project owns:** the research run of the YCharts calls and its persisted, labelled responses (O1); the map from
report elements to calls (O2); Opal's generation script and its branded output (O3); the placement of both in Opal's
store (O4); the per-stage timing record (O5); and the side-by-side comparison (O6).

**It relies on, and does not change:**

- **IRPT_BCKEND, the `~Y` Analysis workstream** -- the served YCharts generation path (`recipe.py` seven steps, the K5
  job queue, retained certified PDFs). It keeps running as it is: the request file says the `~Y` V1 runs continue in
  order (CTO 104634). Whether Opal generation later replaces it is a decision after this research, not part of it.
- **The shared YCharts session** -- the gateway's server-held session (`ycharts/credentials`) and the host session now
  shared with Andrew's browser (row S233). Sign-in is Andrew's act.
- **The Opal gateway YCharts integration** (`infra/aws/ec2/opal-gateway/app/integrations/ycharts/`) -- read-only data
  tools; a reuse candidate, owned where it lives.
- **The IRPT export and render path** (`infra/aws/lambda/investor-reporting/export/`, `_render_identity/`) -- already
  carries branding as a revision; a reuse candidate for "Opal branded".
- **The X10 register** (`infra/logic/06_CONFORMANCE_LEDGER.md` row X10, `infra/logic/registry/reporting_policies.json`)
  -- the private reporting families; the register is this seat's lane.

**It does not own:** the YCharts subscription terms, Andrew's vendor word, or any client-facing release of an
Opal-branded report.

---

## PART III -- THE QUALITATIVE BAR

1. Andrew could hand the Opal-branded report to a client in place of the YCharts one without having to explain a number
   away.
2. Asked "where did this number come from?", an analyst answers from Opal's own store, without going back to YCharts.
3. A report run is something Andrew waits for at his desk, not something he comes back to later.
4. No research run costs Andrew his YCharts session.
5. Where Opal cannot reproduce a YCharts element, the report says so instead of approximating it.

---

## PART IV -- THE SUBSTRATE: what exists, measured

- **F1. The request contract is known and live.** `recipe.py:1-45` names seven steps. (1) Identity, which makes no
  request. (2) Template GET `/custom_pdf_reports/generate/<id>`. (3) Holdings upload POST. (4) Create POST, which returns
  `model_portfolio_id`. (5) Validate POST, which returns 200 `{}`. (6) Generate POST, with the full 34-key body; it
  returns `report_url`/`zip_url` and took 26.76 s live. (7) Signed download, then the PDF is validated by parse. The
  variant comes from the comparison count (`recipe.py:121-146`). Template bodies and the comparison catalogue are in
  `templates.json` beside it.
- **F2. Those calls return identifiers and links, not the report's figures.** Per F1, create returns an id, validate
  returns `{}`, and generate returns URLs. The figures exist only inside the PDF that generate produces. Consequence for
  O2/O3: mapping these calls cannot place a single figure. The figures have to come from YCharts' DATA endpoints, or be
  marked as computed inside generation. Andrew's "same endpoints" is read here as the endpoints that supply the report's
  data (see PART VII).
- **F3. Opal already reads YCharts data.** The gateway integration
  (`infra/aws/ec2/opal-gateway/app/integrations/ycharts/integration.py:1-12`, tools at `:134-173`) offers four
  read-only tools on the shared session: snapshot metrics, time series, fund series and risk-return scatter. Its own
  docstring names portfolio analytics (`model_portfolios/*`, transition analysis, attribution) as "the charted next
  toolkit", not yet built.
- **F4. Opal already renders branded documents.** The export bundle (`infra/aws/lambda/investor-reporting/export/bundle.py`
  header) treats "a branding change" as "a new revision, not a recalculation". `rebrand()` changes only
  `render_options.brand_revision` and the approved asset set.
- **F5. The private reporting store has a home for Opal-made reports, but none yet that names YCharts responses.** The
  X10 families include PERFORMANCE and ANALYSIS (platinum) and ORIGINAL_VENDOR_PDF (state). PERFORMANCE_SOURCE_EVIDENCE
  holds "original SmartX/Black Diamond/Orion response bytes plus a separately identified redacted request/response
  receipt" (ledger row X10). YCharts is not in that list.
- **F6. Live captures already exist.** `docs/research/investor_reporting_ycharts_cloud_20260911/` holds the 2026-09-11
  per-step captures (`lambda_create_*.json`, `lambda_generate_*.json`, `lambda_download_01.json`,
  `pdf_validation.json`). `docs/research/investor_reporting_ycharts_variants_20260911/` holds the three-variant proof
  and `UI_CONTRACT.md`.
- **F7. The 17 m 43 s is mostly Opal's own waiting, by inference.** Y-3 (Multi, Cottonwood) spent 15 m 19 s in
  SUBMITTING. The read-back takes one status GET per receive (`READ_BACK_POLLS = 1`, `recipe.py:660`). On a
  `calculating` answer it holds the message for 900 s (`READ_BACK_LEASE_TTL_S`, `:662`). That spacing exists because the
  YCharts WAF challenged faster polling (CTO 101792, 101917, batch 97). YCharts' own calculation time has not been
  measured.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- **Andrew's word on research calls.** His standing word covers Analysis runs one at a time with the queue empty
  (2026-09-27; 2026-10-02 ~18:1xZ). Whether it covers research calls outside the job queue is his call (open).
- **The subscription terms.** Whether YCharts-computed figures may appear in an Opal-branded document is Andrew's call
  (open). O3 and O6 depend on it; O1, O2 and O5 do not.
- **A live session that survives the run.** One session per account, shared with Andrew's browser (S233). A WAF
  challenge can cost it. The research call rate has to stay inside what the WAF tolerates.
- **No secret in any artifact.** Responses are kept with cookies, tokens and credentials scrubbed; none enters a commit.
- **Opal addresses from the builders.** Every new S3 address and resource name is `lib/opal_naming.py` output (CLAUDE.md
  rule 30). Persisted YCharts responses need an X10 family (or a register row) that names them (F5).
- **Client holdings stay inside their firm.** The cross-firm guard applies to the uploaded holdings and to every output.
- **The served path is undisturbed.** The `~Y` V1 runs share the one session; research runs do not interleave with them.

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured from the request file @`ee801b0505`, read 2026-10-03 17:2xZ:

- Y-3, job `REQ-329a56182b2668d44a28c8d7` (Multi, Cottonwood), went READY at 17:03:14Z after 17 m 43 s. Its stages:
  QUEUED 19 s, SUBMITTING 15 m 19 s, DOWNLOADING 35 s, CERTIFYING 1 m 30 s. Log:
  `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/Y3/V1A/V1A2_multicomp_ult_iwm_cottonwood_20261003.log`. Report:
  `RPT-c8c4037aaf09c01cd6d7797eb28cc7f8`, retained and certified.
- The `~Y` V1 runs continue: Y-5 next, then Y-4, one at a time and spaced (CTO 104634).

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **No PDF was opened and no section was mapped.** O2 is the research; this brief does not know which sections a
  template draws.
- **Unknown whether YCharts exposes a data endpoint for every element.** Ratings, scores and some statistics may exist
  only inside generation. O2 is built to say so where it happens.
- **"The same endpoints" is an interpretation.** Read literally, it would be the `custom_pdf_reports` endpoints, but
  those return YCharts' own PDF (F2), which cannot be re-branded. This brief reads Andrew as meaning the endpoints the
  report's data comes from. The CTO should confirm this reading at L2 or route it back to Andrew.
- **The 2026-09-11 captures were not opened** (F6). Whether they already hold any figure-bearing response is unchecked.
- **YCharts' calculation time is unmeasured**, and the 15 m is inferred, not measured, to be mostly Opal's wait (F7).
  Whether an Opal-built document is faster depends on it and on the data calls' own WAF tolerance. No time target is
  set here.
- **The subscription terms were not read.**

---

## REFS

```
  BRIEF PATH        docs/briefs/irpt-ycharts-direct-generation-opal-branded-brief-20261003.md
  PROJECT           NONE-YET (CTO registers at L3)
  EXISTING PRD      NONE
  REQUEST           org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/RESEARCH/CRO_REQUEST_YCHARTS_DIRECT_GENERATION_20261003.md @ee801b0505
  SIBLING PROJECTS  IRPT_BCKEND (~Y Analysis workstream); the Opal gateway YCharts integration; the IRPT export/render path; X10 register
  PRIOR ART         recipe.py seven steps + templates.json (F1); gateway YCharts data tools (F3); export bundle brand revision (F4);
                    X10 families (F5); 2026-09-11 captures and variant proof (F6)
  OPEN FOR ANDREW   (1) does the standing YCharts word cover research calls; (2) do the subscription terms permit Opal-branded output
  MEASURED AT       2026-10-03 17:2xZ (request file read; recipe.py, integration.py, bundle.py, X10 row read at CLOUD HEAD)
```
