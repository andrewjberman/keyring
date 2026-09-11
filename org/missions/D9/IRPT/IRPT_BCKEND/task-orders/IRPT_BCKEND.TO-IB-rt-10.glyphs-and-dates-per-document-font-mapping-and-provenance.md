# TO IRPT_BCKEND.TO-IB-rt-10 -- GLYPHS AND DATES: text recovered through each document's actual font mapping or marked unresolved, the fi-ligature codes 45 and 46 and a negative unmapped glyph tested, and undated sections carrying document provenance rather than a neighbour's date

<to_id>IRPT_BCKEND.TO-IB-rt-10</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~4</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending -- RE-SEATED by 2.0.0_SA_COO~B at 2026-09-11 ~17:3xZ from slot ~3 to slot ~4 (a head with no incoming edge; slot ~4 freed by IB-rt-8's second COMPLETE at f20bebd15d; slot ~3 stays on IB-rt-9 then IB-rt-11). Handed now.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 2 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.13 @e6ba5d9878 (ADMITTED, both L4-R halves SIGNED) | **Round-1 analysis:** `../ledger/ROUND_ANALYSIS.round1.md` @0d57ceb2f9, ruling 6 (extraction) | **Slug rows this cell closes:** W3-S10, W3-S11 | **Decomp cell:** `IB-rt-10` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.2, s.1 + s.2) | **outcome_ref:** FWD-4 (contrib), FWD-3 (contrib) | **PRD candidate:** B10

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~4` (the same subagent as round 1, continued with its context intact). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~4;`.
- **Worktree:** `/c/tmp/wk-irpt-2-3` on branch `wk-irpt_bckend-2-3`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-2-3/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~4 <0.9.0_WK_IRPT_BCKEND~4@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/` (granted by the tree convention; no `<paths>` entry needed). Round-2 batteries are named `battery_<cell>.py` with the cell id lower-cased and hyphens as underscores.
- **Queue:** third in slot ~3, after IB-rt-9.

---

## THE CELL

**The PRD row, verbatim at @e6ba5d9878 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B10 section extraction + certification against paired PDFs
- **serves:** FWD-4 (contrib), FWD-3 (contrib, parity)
- **brief sections consumed:** O4 certification paragraph; IV.4 records paragraph; IV.1 S8
- **contracts (P=produces, C=consumes):** P `AnalysisReport.typed sections with units/dates/source coordinates`
- **paths: reuse:** --
- **paths: new home:** `infra/aws/lambda/investor-reporting/` (extractor)
- **fixtures / evidence:** **(v0.11, CRO R2)** AVAILABLE: the three SYNTHETIC vendor PDFs and their receipts from the variants packet (Overview 23 pp / Comparison 31 pp / Multi-Comp 35 pp, `pdf_validation.json`, `verification.json`, hashes; SPY/AGG on synthetic portfolio 2332257) -- real vendor output on synthetic holdings, sufficient to BUILD and exercise the extractor and its certification harness with a difference control; STILL MISSING: the paired SECTION certification against those PDFs (units, dates, page/coordinates) is B10's own work, not delivered by generator success, and REPRESENTATIVE REAL-CLIENT / real-input specimens (the proof gap named on FWD-4 and FWD-8)
- **acceptance clause draft:** text/table extraction certified with units, dates, page/coordinates; charts need reliable underlying data or an identified source-chart representation; no number inferred from a visual guess; section extraction is never marked complete on the generator's 201 or on a PDF's existence

**The CTO's ruling this cell executes (ROUND_ANALYSIS.round1.md @0d57ceb2f9, verbatim):** Per-document font mapping or explicit unresolved for the fi-ligature codes 45/46 (W3-S10); undated sections represented with document provenance, never inferred from a neighbour (W3-S11).

**What L5 adds (decomposition v0.2 s.2, s.6, s.9):**

- `ycharts/extract/`: the extractor reads each document's OWN font/ToUnicode mapping (the PDF's font resources) and recovers a cid through THAT document's map; a cid the document does not map is `UNRESOLVED_GLYPH` on the token, never a global replacement; the three retained vendor PDFs (codes 45 and 46 both observed, one document differing) plus a synthetic document with an unmapped cid are the fixtures; certification refuses a value whose text carries an unresolved glyph (round 1's rule, kept).
- Dates (W3-S11): `AnalysisReport` sections carry `date_claim` -- one of `SECTION` (the section states its date), `REPORT` (the report-level date applied with provenance `report_header:<page>`), `NONE` (undated, held out of dated arms) -- proposed to the contract as an OPTIONAL enum so `additionalProperties:false` holds (the contract edit is IB-s-18's surface: this cell adds the optional property to `_contracts/AnalysisReport.schema.json` and the v1 artifact in the same commit, with the CONTRACTS-table citation, and files a row naming the CTO's L10 read on it); dated and undated holdouts proven on the vendor PDFs (Comparison 34 of 81 rows undated, Multi 51 of 108 -- reproduced), never a neighbour's date.

---

## WHAT ROUND 1 DELIVERED THAT THIS CELL BUILDS ON (not rebuilt)

the extractor and certifier with cid refusal and undated holdouts (IB-s-10); the three retained vendor PDFs in S3 with hashes; the synthetic three-variant PDF and its difference control.

---

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~17:3xZ, at the hand-off):** this order is executed by slot ~4 (`0.9.0_WK_IRPT_BCKEND~4`, the subagent that built and deployed the export worker); every serial in this face reads ~4 accordingly and the deliverables home is `deliverables/0.9.0_WK_IRPT_BCKEND~4/`. The decomposition's seating table (v0.2 s.5) is descriptive; the fanout is unchanged at five chains. Two facts from IB-rt-8's judgment bear on glyphs: the four round-1 PDFs embedded SegoeUI/TimesNewRoman against a package declaring Lato (0 of 3 declared fonts embedded, 4 of 4 artifacts), and the live render fetched its typefaces from `fonts.googleapis.com` (2 foreign of 12 requests) -- the font mapping this cell writes is per document and provenanced, never a fetch.

## DELIVERABLE

`infra/aws/lambda/investor-reporting/ycharts/extract/{fonts.py,extract.py,certify.py}` + tests + the unmapped-glyph fixture; the optional `date_claim` property on `AnalysisReport` (schema + v1 artifact); the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_rt_10.py` and `.result.md`.

---

## BOUNDS

- **No global glyph replacement table.** A cid resolves through the document's own map or reads unresolved.
- **No number from a visual guess; no date from a neighbour.**
- **No deploy in this cell** (the extractor rides the generate package's next build; the schema change is committed, its consumer effect graded at IB-rtb-1).

### Bounds every order carries (decomposition v0.2 s.8, verbatim)

1. **NO LIVE VENDOR CALL.** Endpoint, verbatim: *"NO LIVE VENDOR CALL is authorized by this document -- availability is not authorization; a live YCharts, Black Diamond or Orion call needs Andrew's explicit per-use word."* The same bound covers the mailbox read and a YCharts login or session capture. A cell that carries a live arm proves its MECHANISM against recorded fixtures through a transport stub with a difference control; the live arm is an express qualification read by the CTO at L10 on Andrew's per-use word, never something this order does.
2. **NO MONITOR, ALARM, SNS OR SES SEND.** Nothing in this project notifies anyone. A scheduler this project creates is the product's own trigger and is applied `DISABLED` where its first fire would be a vendor call.
3. **CROSS-FIRM, both shapes.** Per-firm prefixes + IAM conditions in the shared bucket; the FIRM's own bucket for directory and holdings data; the `FirmDestinationPolicy`; the firm fixed from the sender's domain at ingestion and immutable after; Global GRANTED to an Opal principal, never to a firm one; no new all-firm financial aggregate.
4. **Deploys (NEVER-2, NEVER-9).** `.tools/safe-apply.sh` only, from a root whose state key is this cell's; a change-management entry opened at the start (`python .tools/deploy_ledger.py open ...`) and its OPEN sentinel `org/critical_paths/.open_deploys/<slug>.json` COMMITTED IMMEDIATELY (row W3-S4's rule) before the act; the entry closed at completion and COMMITTED BEFORE the reads that grade the act; served bytes verified as `CodeSha256` against the built zip, never by filename; `aws lambda update-function-code` never; `.tools/terraform.exe` is provisioned in your worktree by the issuer -- use it by that path, never a PATH substitute (a substitute re-pins remote state); every provider cache was purged estate-wide, so `init` each root you plan with the vendored binary.
5. **Andrew's four fixed constraints are not build choices:** the BDAPI-with-Kimi runner STYLE with NO OTP branch; the firm from the sender's domain at ingestion gated to enumerated destinations; the multitenant `api/scoped/` layout; terminated clients STAY VISIBLE under entitlement. And the endpoint's: units are part of a number's meaning; unsupported positions are never silently removed; no PUT of global YCharts preferences; no vendor call in render or preview; missing history is an answer, not an empty state; the narrative states contemporaneity and never causes; model targets never masquerade as observed holdings; THE YCHARTS MECHANISM IS FIXED (v0.9: K3 capture on the dedicated host -> fenced publication -> browserless Lambda REST replay).
6. **No credential in any artifact, log, fixture or commit.** Secrets are read by NAME at runtime; a recorded fixture is scrubbed before it is committed; signed URL parameters are never logged; a `describe-secret` prints version state, never a value.
7. **No served output is touched.** The 28 existing CloudFront behaviors, the 14 pre-existing scoped routes, this project's 11 live routes and every existing bucket, table and Lambda are read, never edited, except where THIS order's cell says it CHANGES or ADDS a resource.
8. **The spec is FROZEN mid-round.** A premise that does not hold, a path that is not where this face says, a result the invocation does not produce, a capability you lack: ONE row at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W<your slot>-S<k>` (a DS lane mints `IRPT_BCKEND-D-S<k>`), per `org/surprise_channel/schemas/investigation_item.schema.json`, inside the fenced json array, appended never edited, k continuing your slot's round-1 numbering; then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.
9. **Every invocation terminates.** You run each named invocation under `timeout`; rc 124 IS the recorded output, retried once at most.
10. **Every `.py` edit passes `.tools/commit-gate.sh`.** Python 3.12 (`Python312` first on PATH; bare `python` may resolve to 3.14 without PyYAML). ASCII only in production code, logs and AWS names (`OK:`/`WARN:`/`ERROR:`/`SKIP:`/`BLOCKED:`).
11. **Scratch** is `<your worktree>/.scratch/` only.
12. **NO SELF-WRAPPING HARNESS AS EVIDENCE (round-1 lesson, rows W1-S10, S24).** An arm's subject is the REAL artifact -- the real route file, the real dispatcher, the deployed function, the served object -- never a copy the battery wraps, patches or re-registers itself. A census reads the real population and prints its denominator; a `0 of 0` is printed as VACUOUS, never as a pass. Every manifest of hashes a cell writes is re-derived by its battery every run (row W3-S9).
13. **TYPED, ISSUED IDENTIFIERS AT EVERY BOUNDARY (round-1 lesson, rows W2-S9/S11, W1-S7, W3-S12).** Firm, client, relationship, account, report, export and job ids cross a function boundary as ISSUED opaque ids of a declared type; a display name, an e-mail address, a raw upstream key or a request-controlled firm token is refused at the boundary, and a refusal never echoes the refused value.

---

## ACCEPTANCE

<criterion id="RT10-AC1" cell_refs="IB-rt-10"><invocation>timeout 600 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_rt_10.py</invocation><expect>IBRT10-GLYPHS-DATES-PROVENANCED</expect></criterion>
**`RT10-AC1` -- PASSES BY OUTPUT -- per-document mapping, both codes and the negative, provenance on every date.**
**(a) PER-DOCUMENT.** For each of the 3 vendor PDFs the `fi` ligature is recovered through that document's map (the code used printed per document: 45 / 45 / 46 as measured); `(cid:` occurrences in certified text: 0 of the round-1 89 pages.
**(b) THE NEGATIVE.** The synthetic document's unmapped cid reads `UNRESOLVED_GLYPH` and certification refuses a value carrying it (printed).
**(c) DATE CLAIMS.** Every section item carries `date_claim`; counts per claim per document printed (Comparison undated 34 of 81, Multi 51 of 108 reproduced); 0 items dated from a neighbour (a mutant that copies a neighbour's date FAILS the arm).
**(d) SCHEMA-VALID.** The sections artifacts validate against the amended schema and the v1 artifact; the two files byte-equal on the added property.

<criterion id="RT10-AC2" cell_refs="IB-rt-10" judgment="true"/>
**`RT10-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: which glyphs beyond `fi` the three documents map differently; whether `REPORT` as a date claim could mislead a reader of a section that is genuinely stale; and which arm breaks first on a real client PDF. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>RT10-AC1, RT10-AC2</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rt-10.glyphs-and-dates-per-document-font-mapping-and-provenance.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/ycharts/extract/
infra/aws/lambda/investor-reporting/_contracts/
docs/contracts/investor-reporting/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.2, cell `IB-rt-10` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-rt-10</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger. BLIND SPOT, stated: the round-1 cut-time run (5 of 5 carriers, 0 gates naming this project) is inherited, not re-run here.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied by this cell; no policy, role or trust document is written. BLIND SPOT: the reads this cell makes run under the launching seat's credentials, stated not measured.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `docs/contracts/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL or its documentation lane at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: RT10-AC1, RT10-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IRPT_BCKEND.TO-IB-rt-10.glyphs-and-dates-per-document-font-mapping-and-provenance.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IRPT_BCKEND.TO-IB-rt-10.glyphs-and-dates-per-document-font-mapping-and-provenance.proof_of_spec.json RT10-AC1,RT10-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it. The PENDING-THIS-COMMIT sentinel is one-shot: pin artifact rows to the commit that carries them.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
