# ETFS_RIVALS task order -- `RIV-ui-4` -- ROUND 6 (ENRICHMENT): THE AI ACCOUNT CARDS (RFW-U08, RFW-U09, RFW-U10, RFW-D09 render half, RFW-U18, the CTO's vintage line)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-ui-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~6</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-02 ~15:2xZ, --drift) -- carrier C1: 31 sentinels scanned, 12 gates armed, none names rivalfunds/, etfs-rivalfunds or this cell's files; C2-C5 not scanned inside the 90 s budget (blind there); the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 6** makes the A1 tables follow their inputs, puts the AI accounts into the scheduled path, adds the plausibility guard, fixes dividend currency and exit pricing, gives the census three states and the page real names, and carries the 33-item page walk (PRD v0.12). Nothing in round 6 deploys from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-ui-4` -- the AI account cards (RFW-U08, RFW-U09, RFW-U10, RFW-D09 render half, RFW-U18; the CTO's vintage line)
- The cited-rows dump and provenance fields sit behind a collapsed details element.
- A stored reading key in the text DISPLAYS as its label (`ai_accounts.reading_label` or a render map); the stored text is
  not rewritten.
- The grade is a badge at the top; a FAIL account is collapsed by default, its reason in the summary.
- An account opens to its first two sentences.
- The card states the table vintage it was written against when that differs from the tables served.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD bdbd7a257b (rv-fast; render.py unchanged since the deployed 722f0db291))

- DOM hooks: audit material in closed `<details data-sources>` with summary "Sources and checks"; each label carries `title="<source>/<name>"`; a `data-grade="PASS|FAIL"` badge before the prose; a FAIL account is a closed `<details>`.
- The label map: `ai_accounts.reading_label(row)` exists (round 5 F5); you may import it, never edit ai_accounts.py (chain ~1's).
- Keep the round-5 re-grade line (`data-regrade`, "Superseded grade: ...") and the trade-log notes (`data-no-move`, `data-cash-equiv`); their tests are in your paths.
- The vintage line: each research_hypotheses row carries `input_vintages` (JSON, keys `<source>/<name>`, values revision ids); the page's served A1 objects are in the manifest's `a1_produced`. State the vintage when they differ; never rewrite the account.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/` and round 5's `.../round5/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.12), the walk brief `docs/briefs/rivalfunds-ui-data-walk-20261002.md` and its register `docs/briefs/rivalfunds-ui-data-findings-20261002.json`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~6/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-6 chain owns, and none of the merge hookups the decomposition names (the issuer adds them). Tests go beside the code as `tests/test_r6ui4_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file, never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/test_r6ui4_*.py
data/etfs/scripts/rivalfunds/tests/test_p1_page_and_guardrails.py
data/etfs/scripts/rivalfunds/tests/test_p2_page_grouped_by_fund.py
data/etfs/scripts/rivalfunds/tests/test_regrade_call11.py
data/etfs/scripts/rivalfunds/tests/test_g83_cash_equiv_trades.py
data/etfs/scripts/rivalfunds/tests/test_no_shares_moved_g82.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the cited-rows dump and provenance sit in closed details data-sources ('Sources and checks'), at most one per account plus one for the run (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ui-4.AC1.py`)
- **AC2** -- a stored reading key displays as its label with title='<source>/<name>'; the stored text and its figures are unchanged (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ui-4.AC2.py`)
- **AC3** -- a data-grade badge comes before the prose; a FAIL account is a closed details with its reason in the summary (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ui-4.AC3.py`)
- **J1** (JUDGMENT, graded by 3.0.0_SA_CVO~RV at L9 on the served page) -- RFW-U18 (each account opens to its first two sentences) and the vintage line (the card states the table vintage it was written against when that differs from the tables served); positive control: the served 2026-10-02 AI cards, open in full, written against the 11:03Z tables while the page serves the rv-publish-1002g rebuild

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-ui-4"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ui-4.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-ui-4"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ui-4.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-ui-4"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ui-4.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-ui-4" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~6/ETFS_RIVALS.TO-RIV-ui-4.ai-account-cards.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-ui-4.ai-account-cards`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-5 analysis @56c99763bb (msg 28485) section 4 + PRD v0.12 @afc2bed44f
(RFW register, msg 28535); decomposition round 6 v1.0; Andrew-direct "/canonical-drive with max parallelization on
subagents" (cooRV record 141xZ). Chain `~6`, slot `~6`, position 4 of 5 (ui-1 -> ui-2 -> ui-3 -> ui-4 -> ui-5). Checks dry-run at base CLOUD bdbd7a257b (rv-fast; render.py unchanged since the deployed 722f0db291):
ui-4.AC1 FAIL (3; first-sentence controls PASS) as expected; ui-4.AC2 FAIL (3; stored-text control PASS) as expected; ui-4.AC3 FAIL (3; PASS-account control PASS) as expected.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>6</round>
<slot>~6</slot>
<fabric>site-z</fabric>
