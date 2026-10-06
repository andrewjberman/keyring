# ETFS_RIVALS task order -- `RIV-ln-1` -- ROUND 9 (ENRICHMENT): A NAME SEVERAL KEY FORMS OF ONE SECURITY CARRY OPENS THAT SECURITY'S DIALOG (C-S35)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-ln-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~4</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell (the issuer registers any stage at the merge)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 9** (the round-8 analysis, 8 items): the IDVZ/PFOE backfill made purely additive (the trade schedule rebuilds only named funds), their daily join through a rivalfunds-owned gate file, an incremental security list, the AI-text name links, real names for past holdings, a measured Bloomberg capacity budget, and a read of the G5 history drift. Nothing in round 9 deploys, merges, flips a gate or calls Bloomberg from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-ln-1` -- the AI-text name links (CVO C-S35)
- Measured on the served 10-05 page: 395 AI-text mentions of 43 securities that have a modal are plain text; in the page's render
  context 428 of 860 display names are carried by more than one key ('Enel SpA' <- 29265W207, ENEL_IM_Equity, 'ENEL IM Equity'),
  and `render._render_page` keeps a name in `_NAME_KEYS` only when ONE key carries it (render.py:1769).
- Interface: a page name whose keys include exactly ONE key with a dialog on the page links to that key; a name two
  dialog-bearing securities share links to the key the account's citation list names, else stays plain with both identifiers
  in its title; a one-key name links as today. The page stays under the gateway cap (2,097,152 B).
- **Organic trigger:** the 07:00 ET marker publish and the 09:00 ET sweep publish.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD bfad7625d7 (the package equals the deployed pin b166e04416))

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/checks/ln-1.AC1.py` before you build.
- Keep round 8's fc-1 contracts (one dialog per security page-wide, `DIALOG_SOFT_CAP`, `tests/test_r8fc1_*.py`) and an-1's one
  name (`tests/test_r8an1_*.py`).
- The latest-holdings tables carry 334 plain mentions (243 names); they are outside this cell (the CVO left the scope to the
  issuer): do not change them.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order: no file there is written or read differently), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/checks/` and the earlier rounds' `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{7,8}/checks/`, the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` (round 9), the analysis `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round8.md`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~4/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any environment gate flip outside a test, any file another round-9 chain owns. Tests go beside the code as `tests/test_r9ln1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/test_r9ln1_*.py
data/etfs/scripts/rivalfunds/tests/test_r8fc1_*.py
data/etfs/scripts/rivalfunds/tests/test_r8an1_*.py
data/etfs/scripts/rivalfunds/tests/test_crorv_layout.py
data/etfs/scripts/rivalfunds/tests/test_r6ui4_ai_account_cards.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- 'Apple Inc', carried by three key forms, opens the AAPL_US_Equity dialog from the AI text; a one-key name still links (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/checks/ln-1.AC1.py`)
- **J1** (JUDGMENT, graded by 3.0.0_SA_CVO~RV at L9) -- on the served page after the deploy the AI faces and dialogs carry 0 plain mentions of a modal-bearing name (or each remaining one names its ambiguity), and the page loads under the gateway cap; positive control: the served 10-05 page (395 plain mentions)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-ln-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/checks/ln-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-ln-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~4/ETFS_RIVALS.TO-RIV-ln-1.ai-text-links-every-key-form.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-ln-1.ai-text-links-every-key-form`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line); the hookups you need the issuer to add at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** ROUND_ANALYSIS.round8.md @2097b5212b section 4; decomposition round 9 v1.0. Chain `~4`, slot `~4`, position 1 of 1. Checks dry-run at base CLOUD bfad7625d7 (the package equals the deployed pin b166e04416): ln-1.AC1 FAIL (1; control OK) as expected. Bounds: no deploy before the issuer's never-widen pair; D12 Step B and the D12 gate flip are issuer acts after nf-1 and gf-1 deploy.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>9</round>
<slot>~4</slot>
<fabric>site-z</fabric>
<status>complete</status>
