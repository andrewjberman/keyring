# ETFS_RIVALS task order -- `RIV-r-6` -- ROUND 6 (ENRICHMENT): THE AI GRADER AND PROMPT REPAIRS (remediations; RFW-D09 prompt half)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-r-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-02 ~15:2xZ, --drift) -- carrier C1: 31 sentinels scanned, 12 gates armed, none names rivalfunds/, etfs-rivalfunds or this cell's files; C2-C5 not scanned inside the 90 s budget (blind there); the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 6** makes the A1 tables follow their inputs, puts the AI accounts into the scheduled path, adds the plausibility guard, fixes dividend currency and exit pricing, gives the census three states and the page real names, and carries the 33-item page walk (PRD v0.12). Nothing in round 6 deploys from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-r-6` -- the AI grader and prompt repairs (remediations; RFW-D09 prompt half)
- `grounding_check/5`: a digit run inside a market reading's own name, quoted in the text (a trending-topic headline), is not a
  figure. The run-time grade gets the names from the readings; the publish recheck (`guardrails.analysis_grounding`) gets
  them from the row's `input_vintages` keys. A bare number outside the name still fails.
- Prompt a1-chain/5: a security is named by its name, not its Bloomberg ticker form (CALL 10 style); a figure is written in the
  facts' display form, never rounded into a new number (RFW-D09).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD bdbd7a257b (rv-fast; package unchanged since 722f0db291, the deployed pin))

- `ai_accounts.grounding_check(text, cited_rows, identifiers=None, known_keys=None)` is grounding_check/4 (GRADER_VERSION); `_figures` strips ISO dates and timestamps; `ticker_tokens` exempts ticker forms. A trending-topic reading's NAME is a headline and may carry a digit ('Amazon Secures 20 Years of Nuclear Power').
- The run-time grade (`run_chain`) holds the readings; the publish recheck (`guardrails.analysis_grounding(accounts, known_keys)`) holds only the stored row, whose `input_vintages` JSON keys are `<source>/<name>`.
- Prompt a1-chain/4 (`PROMPT_VERSION`) names readings by label (F5); bump to a1-chain/5 for the security-name and figure rules, and update `tests/test_f5_reading_labels.py`'s version assertion.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/` and round 5's `.../round5/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.12), the walk brief `docs/briefs/rivalfunds-ui-data-walk-20261002.md` and its register `docs/briefs/rivalfunds-ui-data-findings-20261002.json`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-6 chain owns, and none of the merge hookups the decomposition names (the issuer adds them). Tests go beside the code as `tests/test_r6r6_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file, never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/ai_accounts.py
data/etfs/scripts/rivalfunds/guardrails.py
data/etfs/scripts/rivalfunds/tests/test_r6r6_*.py
data/etfs/scripts/rivalfunds/tests/test_f5_reading_labels.py
data/etfs/scripts/rivalfunds/tests/test_a1ai2_grounding_hookup.py
data/etfs/scripts/rivalfunds/tests/test_grounding_ticker_form.py
data/etfs/scripts/rivalfunds/tests/test_grounding_iso_timestamp.py
data/etfs/scripts/rivalfunds/tests/test_grounding_unknown_identifier.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a quoted headline's digits pass at the publish recheck AND at run time; a bare 20 outside the name still fails (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/r-6.AC2.py`)
- **J1** (JUDGMENT, graded by 3.0.0_SA_CVO~RV at L9 on the served page) -- the next AI run names securities by name, not ticker form, and writes figures in the facts' display form; positive control: a 2026-10-02 account's ticker forms (TXUE's 'ORA FP Equity') and IDVZ's FAIL ('$1.6 million, $1.3 million')

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-r-6"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/r-6.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-r-6" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-r-6.ai-grader-and-prompt-repairs.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-r-6.ai-grader-and-prompt-repairs`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-5 analysis @56c99763bb (msg 28485) section 4 + PRD v0.12 @afc2bed44f
(RFW register, msg 28535); decomposition round 6 v1.0; Andrew-direct "/canonical-drive with max parallelization on
subagents" (cooRV record 141xZ). Chain `~1`, slot `~1`, position 3 of 3 (st-1 -> ap-1 -> r-6). Checks dry-run at base CLOUD bdbd7a257b (rv-fast; package unchanged since 722f0db291, the deployed pin):
r-6.AC2 FAIL (recheck and run-time both fail the quoted headline; control: bare 20 fails) as expected.

<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>6</round>
<slot>~1</slot>
<fabric>site-z</fabric>
