# ETFS_RIVALS task order -- `RIV-an-1` -- ROUND 8 WORKSTREAM A (ENRICHMENT): THE AI PROSE READS EACH SECURITY UNDER THE PAGE'S ONE NAME (item 2 + RFW-U14 AI-text residue)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-an-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~2</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L6 (2026-10-04 ~21:1xZ, --drift) -- WITHIN BUDGET, 6 of 6 carriers scanned (C1=29 C2=32 C3=12 C4=21 C5=334 C6=1); 1 gate armed, not on this project; the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 8, workstream A** (Andrew-direct 2026-10-04 "yes, build round 8 tonight"): the AI step can no longer cost the page its republish, the AI prose reads every security under the page's one name, the render remainder, the census price repair, and the Bloomberg leg sized for the benchmarks ACWI and IWM with its gate split in two. Nothing in round 8 deploys, merges or flips a gate from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-an-1` -- the AI prose reads each security under the page's one name (item 2 + U14's AI-text residue)
- The 3 money-market keys (DGCXX x2, IJGXX) sit in the stored prose; 13 casing clashes in the opening lines, 26 in the full
  text.
- Interface: `render._rich` maps whole security keys and casing variants to `_NAMES`; a cash-like key reads
  "<TICKER> money market fund" with the original in a title; the stored row is unchanged; the `.rf-cite` citation list
  keeps its keys.
- **Organic trigger:** the 07:00 ET marker publish and the 09:00 ET sweep publish; the page they write is the evidence.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 1c31a5f6ce (the package equals the deployed pin 75ad1e4d2e))

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/an-1.AC1.py` before you build.
- Round 7's rd-1 fixed the `_render_page` shadow, so `_NAMES` is filled by `render_page`; go through `render_page` in your
  test, never set `_NAMES` by hand.
- Keep the round-6/7 contracts and CRO~RV's layout (`tests/test_crorv_layout.py`, `test_r6ui4_ai_account_cards.py`,
  `test_r7rd1_page_walk_remainder.py`): the reading-key labels with title = the key, the AI dialogs, DIALOG_SOFT_CAP.
- Your next order on this slot (rw-1) also edits `render.py`; finish and commit this one first.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/` and the earlier rounds' `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{5,6,7}/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.14 @4cc8e40575), the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` (round 8 A), and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~2/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any environment gate flip outside a test, any file another round-8 chain owns. Tests go beside the code as `tests/test_r8an1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/test_r8an1_*.py
data/etfs/scripts/rivalfunds/tests/test_r6ui4_ai_account_cards.py
data/etfs/scripts/rivalfunds/tests/test_r7rd1_page_walk_remainder.py
data/etfs/scripts/rivalfunds/tests/test_crorv_layout.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- every security key and casing variant in the AI prose reads the page's one name; a money-market key reads '<TICKER> money market fund' with the key in a title; the stored row and the citation keys are unchanged (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/an-1.AC1.py`)
- **J1** (JUDGMENT, graded by 3.0.0_SA_CVO~RV at L9 on the served page) -- the served page after the deploy shows each security under one name in the AI accounts and no raw money-market key; positive control: the served 2026-10-02 page (DGCXX x2, IJGXX; 26 casing clashes in the full text)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-an-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/an-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-an-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~2/ETFS_RIVALS.TO-RIV-an-1.ai-prose-one-name.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-an-1.ai-prose-one-name`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-7 analysis @115645c4b4 section 3 (items 1, 2, 4) + Andrew-direct @0a4321b843 ("yes, build round 8 tonight"); decomposition round 8 workstream A v1.0. Chain `~2`, slot `~2`, position 1 of 2. Checks dry-run at base CLOUD 1c31a5f6ce (the package equals the deployed pin 75ad1e4d2e): an-1.AC1 FAIL (3; control OK) as expected. Bounds: no merge before the 2026-10-05 07:00 ET vehicle pull; no deploy before the 13:30Z grades.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>8</round>
<slot>~2</slot>
<fabric>site-z</fabric>
