# TO-AR-g-111 -- irpt-status returns the closed failure code and its words: the words table in status.py, and the reader in owned_status.py (C-HOP-FAILURE)

<to_id>IRPT_ANLREQ.TO-AR-g-111</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~253</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>30</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-111` (`decompositions/IRPT_ANLREQ_DECOMP_R30_G.md`) |
**outcome_ref:** FWD-4 (PRD v0.21 contract C-HOP-FAILURE, clauses 1 and 2) | **depends_on:** `AR-g-109` (`HOP_FAILURE_CODES` and `get_state`'s `hop_failure`, merged `bc0e7e96c4`). Order: CTO msgs 8907, 8971; `2.0.0_SA_COO~V2` msg 8974 (reads the merged shape).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~253`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-253` (branch `wk-IRPT_ANLREQ-253`), provisioned by the issuer with `infra/`, `docs/`, `data/`, `lib/`, `org/standards` and the project folder on disk. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~253 <0.9.0_WK_IRPT_ANLREQ~253@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either. (A provisioner error about a portal sub-worktree does not concern you.)
- A row id has the form `IRPT_ANLREQ-D2-W253-S<k>` (take the next free `<k>`; check the channel file for `W253` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree.
- Run each test file ON ITS OWN (`python -m pytest -q <one file>`). The checker is run WITHOUT `-I`.

### Read first (under `C:/dev/wk-irpt-anlreq-253/infra/aws/lambda/investor-reporting/`)

- `ops/status.py` (`CORRECTION_WORDS` and the class after it) and `ops/owned_status.py` (the whole file) and `ops/tests/test_owned_status.py` plus its fixtures in `ops/tests/test_owned_report.py` (`world`, `report_world`: `r.job` is the job row in DynamoDB item form).
- `ycharts/generate/durable_job.py` (`HOP_FAILURE_CODES`, and `get_state`, which now returns a plain `hop_failure` = `{hop, code, at}` when the row holds one).

### THE CELL (`AR-g-111`, inlined)

PRD C-HOP-FAILURE: the ticket page READS a failed hop through the status route. `irpt-status` returns a closed failure code beside the state and one table of words that names the step and what happens next. No new envelope field and no schema change: the code travels as the existing `public_reason_code` (`^[A-Z0-9_]+$`), the words as the description of one safe `NONE` action (both already in the contract). The page (another seat's) reads: code = `public_reason_code`, words = the `NONE` action's `description`, step = named in the words.

**`ops/status.py`, exactly this, inserted after the `CORRECTION_WORDS` dict and before `class EnvelopeRefused` (copy the block as written):**

```python
# IRPT_ANLREQ C-HOP-FAILURE (PRD v0.21): the closed failure codes a request's job row can carry (`hop_failure.code`, written by the three
# silent hops) and the one table of words that names the step and what happens next. A literal table: nothing a caller or the row supplied is
# ever interpolated. The code travels as the envelope's public_reason_code; the words as the description of one safe NONE action.
FAILURE_STEP_WORDS = {
    "READY_SIGNAL": ("The analysis was generated, but the message that tells the commentary step it is ready could not be sent. "
                     "Opal Staff have been left a record and will follow up; you do not need to submit the request again."),
    "COMMENTARY": ("The analysis was generated, but the commentary draft step did not finish. "
                   "Opal Staff have been left a record and will follow up; you do not need to submit the request again."),
    "PACKAGER": ("The analysis and commentary were produced, but the final package could not be attached to this ticket. "
                 "Opal Staff have been left a record and will follow up; you do not need to submit the request again."),
    "GENERATE": ("The analysis could not be generated. Opal Staff have been left a record and will follow up; "
                 "you do not need to submit the request again."),
}
FAILURE_WORDS = {
    "READY_SIGNAL_SEND_FAILED": FAILURE_STEP_WORDS["READY_SIGNAL"],
    "COMMENTARY_DRAFT_FAILED": ("The analysis was generated, but the commentary draft step stopped on an error. "
                                "Opal Staff have been left a record and will follow up; you do not need to submit the request again."),
    "COMMENTARY_DRAFT_REFUSED": ("The analysis was generated, but the commentary draft step was refused. "
                                 "Opal Staff have been left a record and will follow up; you do not need to submit the request again."),
    "PACKAGER_REFUSED": ("The analysis and commentary were produced, but the final package was refused when it was attached to this ticket. "
                         "Opal Staff have been left a record and will follow up; you do not need to submit the request again."),
    "PACKAGER_FAILED": ("The analysis and commentary were produced, but attaching the final package to this ticket stopped on an error. "
                        "Opal Staff have been left a record and will follow up; you do not need to submit the request again."),
    "DELIVERIES_EXHAUSTED": ("The analysis could not be generated after several tries. "
                             "Opal Staff have been left a record and will follow up; you do not need to submit the request again."),
}


def failure_words(code, step):
    """The words for a failure code at a step: the code's own words, else the step's generic words, else the generate step's; never blank."""
    return FAILURE_WORDS.get(code) or FAILURE_STEP_WORDS.get(step) or FAILURE_STEP_WORDS["GENERATE"]
```

**`ops/owned_status.py`, exactly this:**
1. Add this function directly above `class OwnedJobStatusReader` (two blank lines each side):

```python
def _failure(snapshot, phase):
    """(code, step) of a failure the job row carries, or None. A hop_failure wins: its step must be a known hop, and its code is used when the words
    table knows it (else None: the step's generic words, never blank). A FAILED or ATTENTION job is the GENERATE step; its stored detail code
    is used only when the table knows it (and then only for the words: the phase's own reason code stays)."""
    hop = snapshot.get("hop_failure")
    if isinstance(hop, dict) and hop.get("hop") in status.FAILURE_STEP_WORDS and hop.get("hop") != "GENERATE":
        return (hop["code"] if hop.get("code") in status.FAILURE_WORDS else None), hop["hop"]
    if phase in ("FAILED", "ATTENTION"):
        detail = snapshot.get("detail")
        code = detail.get("code") if isinstance(detail, dict) else None
        return (code if code in status.FAILURE_WORDS else None), "GENERATE"
    return None
```

2. In `OwnedJobStatusReader.read`, replace the final statement (the `return status.build_envelope(...)` with its `actions=[...] if ... else []` argument) so the end of `read` becomes exactly the following (the lines above `public_state, reason = PHASES[phase]` are unchanged):

```python
        public_state, reason = PHASES[phase]
        if dates is not None:
            public_state, reason = "READY", "ANALYSIS_READY"
        actions = ([{"action": "WAIT", "safe": True, "description": "Check this request again later."}]
                   if public_state in ("QUEUED", "RUNNING") else [])
        failure = _failure(snapshot, phase)
        if failure is not None:  # C-HOP-FAILURE: the closed code travels as the reason, the words as one safe NONE action
            code, step = failure
            if code is not None and step != "GENERATE":
                reason = code
            actions = actions + [{"action": "NONE", "safe": True, "description": status.failure_words(code, step)}]
        return status.build_envelope(request_id, "prospect_analysis" if dates and "date_basis" in dates else "analysis_generate",
            str(record["identity"]["revision"]), public_state, None,
            source_dates=dates,
            public_reason_code=reason,
            actions=actions)
```

**Two existing tests change (they assert the old empty or WAIT-only actions for FAILED and ATTENTION, which now carry the generate step's generic words); change only these two assertions in `ops/tests/test_owned_status.py`:**
- In `test_durable_phase_uses_closed_public_status_without_fabricated_dates`, replace the line `assert all(a["action"] == "WAIT" for a in value["actions"])` with:

```python
    if phase in ("FAILED", "ATTENTION"):  # C-HOP-FAILURE: the generate step's generic words, one safe NONE action
        assert [(x["action"], x["description"]) for x in value["actions"]] == [("NONE", owned_status.status.FAILURE_STEP_WORDS["GENERATE"])]
    else:
        assert all(x["action"] == "WAIT" for x in value["actions"])
```

- In `test_a_job_with_only_refused_evidence_answers_attention_and_serves_no_document`, replace the line `assert value["source_dates"] == {} and value["actions"] == [] and opened == []` with these two lines:

```python
    assert value["source_dates"] == {} and opened == []
    assert [(x["action"], x["description"]) for x in value["actions"]] == [("NONE", owned_status.status.FAILURE_STEP_WORDS["GENERATE"])]
```

**Tests.** A NEW file `ops/tests/test_hop_failure_status.py`, offline, using the fixtures of `test_owned_status.py` (`import test_owned_report as support`; `world = support.world`, `retention_world = support.retention_world`, `report_world = support.report_world`), with these exact test function names (the checker looks for each by name): `test_a_hop_failure_reads_as_its_code_and_words` (set `r.job["hop_failure"]` to the DynamoDB map form `{"M": {"hop": {"S": "PACKAGER"}, "code": {"S": "PACKAGER_REFUSED"}, "at": {"S": "2026-10-16T03:00:00Z"}}}` on the default job; the envelope's `public_reason_code` is the code, its last action is the `NONE` action with `status.FAILURE_WORDS["PACKAGER_REFUSED"]`, the envelope validates against the StatusEnvelope schema, and the `at` text is nowhere in it), `test_an_unknown_code_reads_the_steps_generic_words` (a known hop with an unmapped code: the reason code is the one the job had without the failure and the words are the step's generic words), `test_a_generate_failure_keeps_its_reason` (state `FAILED` with `job_detail` code `DELIVERIES_EXHAUSTED`: the reason stays `ANALYSIS_FAILED`, one `NONE` action with `FAILURE_WORDS["DELIVERIES_EXHAUSTED"]`).

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR111-g-AC1" cell_refs="AR-g-111"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g109_checks.py g111</invocation><expect>^AR-G111-OK</expect></criterion>

<criterion id="AR111-g-AC2" cell_refs="AR-g-111"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g109_checks.py regress111</invocation><expect>^AR-G111-REGRESS-OK</expect></criterion>

<expected_criteria>AR111-g-AC1,AR111-g-AC2</expected_criteria>

- AC1 runs the issuer's 15 tests against your tree (every writer code has words and the table is closed; the fallback to the step's then the generate step's words, never blank; each of the five hop codes travels as the reason with its words and leaves the state, the dates and the schema alone; an unknown code reads the step's words; an unknown hop is ignored; no failure leaves a job unchanged; FAILED and ATTENTION keep their reason and read a known detail code's words or the generic ones; running phases keep only WAIT), then checks your three named tests exist and pass. At base it FAILs.
- AC2 runs five existing test files one at a time (123 tests: the owned status, report, requests, entry and ticket contract) and needs all of them to pass, and needs your branch (against the merge-base with `box/dell2`) to change only your three product files, your test file, your folder, your order and the channel file. At base it PASSes. Run it under `timeout` 590000 ms.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ops/status.py
infra/aws/lambda/investor-reporting/ops/owned_status.py
infra/aws/lambda/investor-reporting/ops/tests/test_owned_status.py
infra/aws/lambda/investor-reporting/ops/tests/test_hop_failure_status.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~253/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-111.status-failure-code-and-words.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R30_G.md</decomp_doc> round 30, workstream ~G, cell `AR-g-111`.
<owned_cells>AR-g-111</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR111-g-AC1, AR111-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~253/IRPT_ANLREQ.TO-AR-g-111.status-failure-code-and-words.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-111`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put the `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder (use `kind` `test` for a test file): commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR111-g-AC1,AR111-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the lines you changed in each product file with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `ops/status.py` and `ops/owned_status.py` are members of the `irpt-status` Lambda package (source-map files list) and of the resident package (`ops/status.py` is reached by no resident import; the resident carries the file); `ycharts/generate/durable_job.py`, which `get_state` needs, is also in the `irpt-status` package. Nothing changes live until a release carries the bytes: the Lambda leg is a later cell (re-pin of `status.py`, `owned_status.py` and `durable_job.py` in `lambda-source-map.json`) and pair. Behaviour at release: a job row carrying `hop_failure` reads with the failure's code as `public_reason_code` and one extra safe NONE action holding fixed words; FAILED and ATTENTION jobs gain one NONE action with the generate step's words (no change to their state or reason). Who gains: no principal class and no route; the answer carries fixed strings only (nothing from the row but the closed code: the `at` text and the detail are never echoed).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change; the status Lambda already reads the job row.
comp-routes: DECLARED-NOT-APPLICABLE -- no route and no schema change (public_reason_code and the NONE action already exist in StatusEnvelope). comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- by the issuer's reference build in a scratch tree (15 issuer tests and the 123 regression tests pass; two mutants, a dropped reason override and a blank fallback, are caught by 5 and 4 tests). Traps: an unknown code read as blank words; a row value echoed to the caller (the timestamp, an internal detail code); a failure changing the state or hiding the dates; a code outside the writers' closed sets accepted; the writers' codes and the words table drifting apart (the issuer test cross-checks `HOP_FAILURE_CODES`); an existing FAILED or ATTENTION answer changing its reason code; a new envelope field breaking the schema.
</preflight>

- Cut on CTO msgs 8907 and 8971, `~V2` msg 8974 and the issuer's reference build. Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR111-g-AC1` FAILs and `AR111-g-AC2` PASSes (123), as expected.
- NOT claimed: that the Lambda carries these bytes (a later release); that the page reads them; that any real job row has a `hop_failure`.
