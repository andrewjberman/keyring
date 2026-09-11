# TO IRPT_BCKEND.TO-IB-s-10 -- SECTION EXTRACTION AND CERTIFICATION: typed sections with units, dates and page coordinates, certified against the paired PDF -- on a synthetic specimen with a difference control, because no real PDF exists

<to_id>IRPT_BCKEND.TO-IB-s-10</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~3</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-10</issued_date>
<status>staged -- assigned to slot ~3; becomes pending when the COO hands it over after IB-s-9 is terminal and merged.</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.4 @62301f71e0 | **Decomp cell:** `IB-s-10` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.1.1, s.1 + s.2) | **outcome_ref:** FWD-4 (contrib), FWD-3 (contrib, parity) | **PRD candidate:** B10

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~3`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~3;`.
- **Worktree:** `/c/tmp/wk-irpt-1-3` on branch `wk-irpt_bckend-1-3`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-1-3/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~3 <0.9.0_WK_IRPT_BCKEND~3@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/` (granted by the tree convention; no `<paths>` entry needed).
- **Queue:** fifth and last in slot ~3, after IB-s-9. IB-s-14 (slot ~4) and IB-s-15 (slot ~2) wait on this cell's merge.

---

## THE CELL

**The PRD row, verbatim at @62301f71e0 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B10 section extraction + certification against paired PDFs
- **serves:** FWD-4 (contrib), FWD-3 (contrib, parity)
- **brief sections consumed:** O4 certification paragraph; IV.4 records paragraph; IV.1 S8
- **contracts (P=produces, C=consumes):** P `AnalysisReport.typed sections with units/dates/source coordinates`
- **paths: reuse:** --
- **paths: new home:** `infra/aws/lambda/investor-reporting/` (extractor)
- **fixtures / evidence:** ACTUAL three-variant PDFs (STILL MISSING -- proof gap, named on FWD-4 and FWD-8)
- **acceptance clause draft:** text/table extraction certified with units, dates, page/coordinates; charts need reliable underlying data or an identified source-chart representation; no number inferred from a visual guess

**What L5 adds (decomposition v0.1.1 s.2, s.6, s.9):**

- **No real YCharts PDF exists (row `IRPT_BCKEND-S5`).** Build `infra/aws/lambda/investor-reporting/ycharts/extract/` -- text/table extraction into `AnalysisReport.sections` typed with units, dates and page/coordinates; certification that every extracted number ties to the PDF text at its coordinates; charts require reliable underlying data or an identified source-chart representation, and no number is inferred from a visual guess -- and PROVE it on a SYNTHETIC three-variant PDF generated from `docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json` (the field census) with the DIFFERENCE control: a copy with one changed number FAILS certification. The real-PDF arm rides the specimens' arrival and is the CTO's L10 read on FWD-4 and FWD-8; it is not a criterion here.
- The `sections/report.json` artifact lands beside the vendor PDF under the generation's attempt prefix; the released revision and the protected PDF reference are recorded on the `AnalysisReport` row.

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~01:4xZ, at the IB-s-3 drain, before this order was handed -- the disarm of rows `IRPT_BCKEND-W2-S9` and `IRPT_BCKEND-W2-S10`, whose disarm_owner is the issuer; recorded as channel row `IRPT_BCKEND-S9`):**
- **EVERY HANDLER THIS CELL SHIPS IS WRAPPED BY `_authz.guard()`** (`infra/aws/lambda/investor-reporting/_authz/enforce.py`, merged at 3cca035c66): resolve, reauthorize before serving, keys through `_keys`, one refusal envelope. A handler reachable through a route without `guard()` is a defect this cell's own battery prints: `_authz.unguarded_routes()` over the routes this cell registers reads `0 of N`, N printed. Where this cell ships no handler, the same census runs over `routes.json` at the replay.
- **THE FIRM ID HAS TWO SPELLINGS AND ONLY `_authz.FirmBinding` RECONCILES THEM (row W2-S9).** `X-Firm-Id` and `_keys.cache_key` carry the REGISTRY id (`49financial`); `DirectoryEntry.ids.firm_id` and the `_scope` cross-firm filter carry the OPAQUE id (`fir_...`, `directory_runner.opaque_id`). A handler that passes the header value into the directory join returns an EMPTY population that reads exactly like a revocation, and no per-module test can see it. Every firm-scoped read this cell makes binds through `FirmBinding`, proven against the directory artifact's own `firm_id_opaque`; a binding that does not reconcile is a REFUSAL (`FIRM_BINDING`), never an empty set. No hash is recomputed and `opaque_id` is not duplicated into a Lambda.
- **A `_keys` REFUSAL NAMES THE REFUSED VALUE (row W2-S10).** `KeyComponentRefused` carries the component with `%r` at twelve message sites; `str(exc)` in a response, a log line, an audit row, a battery print or a surprise row DISCLOSES exactly the value that was refused for being a client name or an e-mail address. Nothing this cell writes surfaces a `_keys` exception's text: the wrapper's refusal reason (parameter NAMES, found through the public `cache_key`) is the only refusal that leaves a handler, and at least one test asserts over the WHOLE envelope (body + reason + audit trail), never the census alone. `_keys` itself is not edited by this cell (not in its `<paths>`; the sanitised exception is the issuer's round-2 item on IB-s-17's surface).
- **THE DIRECTORY AND PERFORMANCE HANDLERS ALREADY MERGED (IB-s-1, IB-s-11) PREDATE THE WRAPPER** -- a decomposition sequencing defect of the issuer, carried to L10; this cell does not edit them, and IB-sb-3's replay is where their unguarded state is measured.

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~05:0xZ, at the L4 hand-off release, before this order was handed -- PRD v0.13 @e6ba5d9878 carries both L4-R sign-offs (1.0.0_SA_CTO 95827); the v0.11 CRO R2 correction to this row is folded in as an AVAILABLE INPUT, the rectangle unchanged; recorded as channel row `IRPT_BCKEND-S16`):**
- **THREE REAL VENDOR PDFs ON SYNTHETIC HOLDINGS ARE AVAILABLE.** The CRO's variants proof (`docs/research/investor_reporting_ycharts_variants_20260911/`, PRD v0.10/v0.11) generated Overview 23 pp / Comparison 31 pp / Multi-Comp 35 pp on synthetic portfolio 2332257 (SPY $60,000 + AGG $40,000) and RETAINED them (`cleanup.json`: "encrypted S3 source/request/PDF artifacts" retained) at `s3://opal-data-ycharts/research/20260911/variants/synthetic-firm/synthetic-advisor/requests/irpt-variants-20260911-{overview,comparison,multicomp}/report.pdf`, KMS-encrypted (key `86324aae-...`), with SHA-256 per variant in the packet's `pdf_validation.json` (overview `abab2ffe...`, comparison `f01cbd48...`, multicomp `0a67ecf7...`) and the receipts in `lambda_{overview,comparison,multicomp}_*.json`. Reading them is an Opal-owned S3 read -- NOT a vendor call; bound 1 is untouched. The PRD's own words at v0.13: "real vendor output on synthetic holdings, sufficient to BUILD and exercise the extractor and its certification harness with a difference control"; "section extraction is never marked complete on the generator's 201 or on a PDF's existence"; REPRESENTATIVE REAL-CLIENT specimens remain the proof gap named on FWD-4 and FWD-8.
- **HOW THIS CELL USES THEM:** fetch the three objects by key, verify each SHA-256 against `pdf_validation.json` BEFORE use (3 of 3 printed; a mismatch is a STOP and a row), and treat them as INPUT SPECIMENS beside the synthetic ones the face already names -- every existing arm still runs on the synthetic fixtures, and the new arm below runs on the vendor PDFs. Label them in every artifact path and metadata as `vendor_synthetic_holdings: true` (never `synthetic: true`, which the face reserves for the census-generated PDFs, and never as a client specimen). If the read is refused by KMS or IAM under this serial, that is ONE row and the new arm reads BLOCKED-BY-<row>; the synthetic arms stand on their own and the token is not withheld by that refusal alone.

---

## DELIVERABLE

`infra/aws/lambda/investor-reporting/ycharts/extract/` (`extract.py`, `certify.py`) + `tests/` + `fixtures/synthetic_pdf/` (the generator script and its three outputs); the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_s_10.py` and `.result.md`.

---

## BOUNDS

- **No number from a visual guess.** A chart without underlying data yields an identified source-chart representation, never a value.
- **The synthetic PDF is labelled synthetic in its own metadata and in every artifact path** (`fixtures/synthetic_pdf/`), so it can never be mistaken for a vendor specimen.
- **No deploy in this cell** (the extractor rides the generate Lambda's package at its next build; the Lambda is IB-s-9's).

### Bounds every order carries (decomposition v0.1.1 s.8, verbatim)

1. **NO LIVE VENDOR CALL.** Endpoint, verbatim: *"NO LIVE VENDOR CALL is authorized by this document -- availability is not authorization; a live YCharts, Black Diamond or Orion call needs Andrew's explicit per-use word."* The same bound covers the mailbox read. A cell that carries a live arm proves its MECHANISM against recorded fixtures through a transport stub with a difference control; the live arm is an express qualification read by the CTO at L10 on Andrew's per-use word, never something this order does.
2. **NO MONITOR, ALARM, SNS OR SES SEND.** Nothing in this project notifies anyone. A scheduler this project creates is the product's own trigger and is applied `DISABLED` where its first fire would be a vendor call.
3. **CROSS-FIRM, both shapes.** Per-firm prefixes + IAM conditions in the shared bucket; the FIRM's own bucket for directory and holdings data; the `FirmDestinationPolicy`; the firm fixed from the sender's domain at ingestion and immutable after; Global GRANTED to an Opal principal, never to a firm one; no new all-firm financial aggregate.
4. **Deploys (NEVER-2, NEVER-9).** `.tools/safe-apply.sh` only, from a root whose state key is this cell's; a change-management entry opened at the start (`python .tools/deploy_ledger.py open ...`) and closed at completion, the sentinel `org/critical_paths/.open_deploys/<slug>.json` COMMITTED; ORDER on any act that changes the world: open the entry, ACT, close the entry and COMMIT it BEFORE taking the reads that grade the act; served bytes verified as `CodeSha256` against the built zip, never by filename; `aws lambda update-function-code` never; `.tools/terraform.exe` is provisioned in your worktree by the issuer -- use it by that path, never a PATH substitute (a substitute re-pins remote state).
5. **Andrew's four fixed constraints are not build choices:** the BDAPI-with-Kimi runner STYLE with NO OTP branch; the firm from the sender's domain at ingestion gated to enumerated destinations; the multitenant `api/scoped/` layout; terminated clients STAY VISIBLE under entitlement. And the endpoint's: units are part of a number's meaning; unsupported positions are never silently removed; no PUT of global YCharts preferences; no vendor call in render or preview; missing history is an answer, not an empty state; the narrative states contemporaneity and never causes; model targets never masquerade as observed holdings.
6. **No credential in any artifact, log, fixture or commit.** Secrets are read by NAME at runtime; a recorded fixture is scrubbed before it is committed; signed URL parameters are never logged; a `describe-secret` prints version state, never a value.
7. **No served output is touched.** The 28 existing CloudFront behaviors, the 14 existing scoped routes and every existing bucket, table and Lambda are read, never edited, except where THIS order's cell says it ADDS a resource.
8. **The spec is FROZEN mid-round.** A premise that does not hold, a path that is not where this face says, a result the invocation does not produce, a capability you lack: ONE row at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W<your slot>-S<k>`, per `org/surprise_channel/schemas/investigation_item.schema.json`, inside the fenced json array, appended never edited; then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.
9. **Every invocation terminates.** You run each named invocation under `timeout`; rc 124 IS the recorded output, retried once at most.
10. **Every `.py` edit passes `.tools/commit-gate.sh`.** Python 3.12 (`Python312` first on PATH; bare `python` may resolve to 3.14 without PyYAML). ASCII only in production code, logs and AWS names (`OK:`/`WARN:`/`ERROR:`/`SKIP:`/`BLOCKED:`).
11. **Scratch** is `<your worktree>/.scratch/` only.

---

## ACCEPTANCE

<criterion id="S10-AC1" cell_refs="IB-s-10"><invocation>timeout 300 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_s_10.py</invocation><expect>IBS10-EXTRACTION-CERTIFIED</expect></criterion>
**`S10-AC1` -- PASSES BY OUTPUT -- extraction and certification on the synthetic specimens, with the difference control.**
**(a) THREE VARIANTS EXTRACTED.** Overview, Comparison, Multi synthetic PDFs -> typed sections; every number carries units, a date where the census says one exists, and a page + coordinates; `N of N` fields per variant against the census.
**(b) CERTIFIED.** Every extracted number ties to the PDF text at its coordinates; printed `N of N`.
**(c) THE DIFFERENCE CONTROL.** The same PDF with ONE number changed after extraction FAILS certification naming the field and the coordinates. Printed.
**(d) NO VISUAL GUESS.** A chart-only region yields an identified source-chart representation with NO numeric value (census of emitted values for that region = 0). Printed.
**(e) SCHEMA-VALID AND LABELLED.** The sections artifact validates against `AnalysisReport`; every synthetic artifact carries the `synthetic: true` marker (census).

**(amend) GUARDED, BOUND, AND SILENT ON THE REFUSED VALUE (issuer amendment at the IB-s-3 drain, rows W2-S9 / W2-S10).** `unguarded_routes()` over this cell's routes reads `0 of N` (N printed); every firm-scoped read binds through `FirmBinding` and a fixture with a non-reconciling binding is REFUSED with `FIRM_BINDING` rather than served empty; a fixture that keys by a client display name is refused and the whole envelope (body + reason + audit trail) contains 0 occurrences of the refused value (census printed). Where this cell ships no handler, the arm reads over `routes.json` at the replay. CLARIFIED at the IB-s-7 drain (row W3-S5, disarm by the issuer): `routes.json` is IB-s-15's deliverable at `infra/aws/terraform/investor-reporting/api/routes.json` and does not exist before that cell lands; a cell that ships no handler and runs before it does NOT report a `0 of 0` census as a pass -- it prints the census AS VACUOUS and runs the two CONTROLS IB-s-7's battery ran (a handler registered unguarded censused `1 of 1`; the same handler wrapped censused `0 of 1`), so the arm proves the censor, not an empty set. IB-s-15 and IB-sb-3 read the real file.

**(v0.11) THE VENDOR PDFs, EXTRACTED AND CERTIFIED (issuer amendment, PRD v0.11 CRO R2).** The three retained vendor PDFs fetched from the research prefix with SHA-256 equal to `pdf_validation.json` (`3 of 3`); each extracted into typed sections with units, dates and page + coordinates (`N of N` per variant against the census, and the fields the census does NOT name listed as UNCENSUSED, never invented); every number certified to the PDF text at its coordinates; the DIFFERENCE CONTROL run on ONE of them (one number changed after extraction FAILS certification naming field and coordinates); chart-only regions yield a source-chart representation with 0 numeric values (census); `sections/report.json` for each labelled `vendor_synthetic_holdings: true`. Printed per variant.

<criterion id="S10-AC2" cell_refs="IB-s-10" judgment="true"/>
**`S10-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: what a real vendor PDF could carry that the census-generated synthetic cannot (fonts, ligatures, rotated tables, footnote markers), and which certification arm would break first; and whether the extractor's page-coordinate grain is fine enough to catch a transposed digit. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>S10-AC1, S10-AC2</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-10.section-extraction-certified-against-a-paired-pdf.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/ycharts/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.1.1, cell `IB-s-10` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-s-10</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger; it builds a library and runs a local battery. BLIND SPOT, stated: the cut-time run (5 of 5 carriers, 0 gates naming this project) is inherited from the issuance, not re-run here.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied by this cell; no policy, role or trust document is written. BLIND SPOT: the reads this cell makes run under the launching seat's credentials, which is stated, not measured.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable (a fresh cut has no prior artifact for it to read).
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: S10-AC1, S10-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-s-10.section-extraction-certified-against-a-paired-pdf.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-s-10.section-extraction-certified-against-a-paired-pdf.proof_of_spec.json S10-AC1,S10-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
