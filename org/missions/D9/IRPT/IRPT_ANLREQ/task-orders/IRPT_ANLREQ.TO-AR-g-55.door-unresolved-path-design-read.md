# TO-AR-g-55 -- the upload door's UNRESOLVED path: a READ of how a kept unknown ticker (TICKER_NOT_FOUND, "keep as typed") can be filed as UNRESOLVED for C-SWAP, every consumer that must accept such a row, the packages that carry the change, and the contract the portal needs; READ ONLY, one record, no source change

<to_id>IRPT_ANLREQ.TO-AR-g-55</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~174</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-55` (`decompositions/IRPT_ANLREQ_DECOMP_R8_G.md`) |
**outcome_ref:** FWD-7 (C-SWAP) and FWD-1 (the door) | **depends_on:** none.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~174`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-174` (branch `wk-IRPT_ANLREQ-174`), provisioned by the issuer. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~174 <0.9.0_WK_IRPT_ANLREQ~174@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W174-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- No live call, NO PUSH, no AWS call of any kind, NO edit of any source file. Scratch outside the product tree. Use the native Grep, Glob and Read tools; a recursive shell grep over the repo is denied by a hook.

### THE CELL (`AR-g-55`, inlined) -- a READ. The product tree is not edited.

*Context.* Andrew, 2026-10-15: "swaps are not up to the filer." The filing form offers the door's own suggestion for an unknown ticker (the
"Did you mean" hint, built by `2.0.0_SA_COO~Y2` in the portal), and the filer may keep the ticker as typed. A kept unknown symbol (BREIT, SREIT,
KPEC) must FILE and reach C-SWAP, the backend replacement rule; it cannot be refused until the filer swaps it. Today the upload door does
refuse it: in `infra/aws/lambda/investor-reporting/intake/portfolio.py` a row whose symbol check is `NOT_FOUND` emits the finding
`TICKER_NOT_FOUND` (about line 501, actions `REPLACE_FILE` and `NAME_PROXY`) and `continue`s, so the row never reaches the normalized
portfolio and the upload stays `NEEDS_CORRECTION`. The CTO ruled (PRD v0.15, msg 8417) that the door changes so a KEPT `TICKER_NOT_FOUND`
holding files as `UNRESOLVED` for C-SWAP; the change rides the ENGINE lane's one resident release. Y2's design read of the hint is
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~151/r41/FILING_HINT_DESIGN_READ.json` (read it first).

Answer these four questions from SOURCE, each with `{file, line, text}` evidence read from the worktree (print the lines you cite; a line you
did not read is not cited), all under `C:/dev/wk-irpt-anlreq-174/infra/aws/lambda/investor-reporting/` unless the path says otherwise:

1. **Q1, the finding flow.** How does a `TICKER_NOT_FOUND` finding travel today, end to end: where `security_checks` come from
   (`intake/portfolio.py` `check` states, `_kept_by_history`), how a correction (`NAME_PROXY`, `ACCEPT_SUGGESTION`, the `replace` map) is posted back
   (`intake/uploads.py`, the status envelope in `ops/status.py`, `template_corrections`), what state the upload ends in with an unresolved
   row, and where the page reads the findings. At least three cites. Say plainly what happens to the row's AMOUNT when its ticker is unresolved.
2. **Q2, keep as typed.** The smallest way to let the filer keep a `TICKER_NOT_FOUND` symbol: `client_action_proposal` (an existing action
   reused or a new action name, and the body member the page would post, in the shape the envelope already uses), and `retained_row_shape`
   (the field set of a normalized row that carries `resolution: "UNRESOLVED"`, its original symbol, its amount, and NO provider receipt; say
   which existing fields it keeps and which it must leave null). Cite where each existing field is written.
3. **Q3, the consumers.** EVERY reader of the normalized portfolio or the retained composition that must accept (or must refuse, by design) a
   row with no provider receipt: at least `intake/composition_admission.py`, `reports/request_composition.py`, `ycharts/research/runner.py`
   `read_holdings`, `ycharts/research/opal_producer.py`, `ops/status.py` and the YCharts path's reader; find the rest by a name search of
   `security_id`, `provider_receipt_sha256` and `analysis_dollars` (state the search terms). For each: `consumer`, `file`, `must_change` (bool),
   `reason`, and `evidence`. A consumer that would silently treat an unresolved row as priced is the defect to find.
4. **Q4, the change set.** `packages`: the deployed artifacts that carry the changed files (the `irpt-ycharts-generate` Lambda zip, the `irpt-status`
   zip, the resident tarball; read `lambda-source-map.json` and the resident package builder `reports/build_resident_package.py` for the member
   lists), each with `name`, `members` and `owner_seat` (the seat or project that owns it today; the intake files are `2.0.0_SA_COO~Y2`'s
   workstream). `change_set`: each file and what changes. `tests`: the tests that pin today's behaviour. `contract_for_y2`: the exact request and
   response shape the portal needs, as plain text. Then the **recommendation**: `smallest_safe_change`, and a `risk_note` that names what the change
   could widen (a path by which an unpriced row reaches a report as if priced, or a refusal that stops being a refusal).

### Deliverable and ACCEPTANCE

Write `C:/dev/wk-irpt-anlreq-174/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~174/r8/DOOR_UNRESOLVED_READ.json` with these keys:

- `base` (the sha your branch started from), `cell` (`"AR-g-55"`), `not_read` (a list of strings: what you did not read and why).
- `q1`: `{"finding_flow": str, "evidence": [cite, ... (at least 3)]}`.
- `q2`: `{"client_action_proposal": str, "retained_row_shape": str, "evidence": [cite, ...]}`.
- `q3`: `{"consumers": [{"consumer": str, "file": str, "must_change": bool, "reason": str, "evidence": [cite, ...]}, ... (at least 3)]}`.
- `q4`: `{"packages": [{"name": str, "members": [str, ...], "owner_seat": str}, ...], "change_set": [{"file": str, "change": str}, ...], "tests": [cite, ...], "contract_for_y2": str}`.
- `recommendation`: `{"smallest_safe_change": str, "risk_note": str, "evidence": [cite, ...]}`.
- A `cite` is `{"file": "<path under the repo root, forward slashes>", "line": <int>, "text": "<a substring of that line>"}`.

<criterion id="AR55-g-AC1" cell_refs="AR-g-55"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g_read_checks.py shape55 org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~174/r8/DOOR_UNRESOLVED_READ.json</invocation><expect>^SHAPE-OK </expect></criterion>

<criterion id="AR55-g-AC2" cell_refs="AR-g-55"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g_read_checks.py cite org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~174/r8/DOOR_UNRESOLVED_READ.json</invocation><expect>^CITES-OK </expect></criterion>

<criterion id="AR55-g-AC3J" cell_refs="AR-g-55" judgment="true"/>
`AR55-g-AC3J` (judgment, graded at L9, never by you): the answers follow from the cited lines, a "not found" is said plainly with what was searched, every consumer that could treat an unresolved row as priced is named, and the recommendation is the smallest change the evidence supports.

<expected_criteria>AR55-g-AC1 AR55-g-AC2 AR55-g-AC3J</expected_criteria>

- AC1 loads the record and prints `SHAPE-OK` only when every key and evidence list above is present; otherwise `SHAPE-BAD <why>`. At base it FAILs (no record).
- AC2 re-opens every cite in the record (the denominator is printed) and prints `CITES-OK <n> of <n>` only when each cited line exists and the cited text is a substring of it. At base it FAILs (no record).

## BOUNDS

- **Grant:** exactly the `<paths>` below. You edit NO source file; the product tree is READ ONLY.
- If a cited file does not exist at the path named, find the file that now holds the function (a name search), cite that, and say so in the record.
- Rows: APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~174/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-55.door-unresolved-path-design-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R8_G.md</decomp_doc> round 8, workstream ~G, cell `AR-g-55`.
<owned_cells>AR-g-55</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR55-g-AC1, AR55-g-AC2, AR55-g-AC3J. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~174/IRPT_ANLREQ.TO-AR-g-55.door-unresolved-path-design-read.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-55`.
- The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: commit the record first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate AFTER its commit with `python .tools/proof-of-spec-check.py <instance> "AR55-g-AC1,AR55-g-AC2,AR55-g-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~136/IRPT_ANLREQ.TO-AR-y-328.resident-release-bindings-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** each criterion's output lines; the recommendation in one sentence; commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of source and one record; nothing is changed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the cell against the answer shape. Traps: an unresolved row that reaches a report as if it were priced (a hole in the other direction); a consumer assumed to tolerate a row with no provider receipt because it never failed on one; a refusal that stops being a refusal; a change that widens what an uploader can file without a trace. NOT seen (blind): the live packages and the deployed bytes; denominator: 4 questions, each answered with cited lines.
</preflight>

- Cut on PRD v0.15 item 3 (CTO msg 8417): the door change rides the ENGINE lane's one resident release. Risk LOCAL: the cell reads source and writes one record. Base: `AR55-g-AC1` and `AC2` FAIL as expected (no record). The checker's green arm, mutant arm and absent-record arm were run by the issuer before the cut.
- Its output decides the build cell of the door change, the package list of the resident release, and the contract `2.0.0_SA_COO~Y2` builds the portal against; nothing is changed by this cell.
