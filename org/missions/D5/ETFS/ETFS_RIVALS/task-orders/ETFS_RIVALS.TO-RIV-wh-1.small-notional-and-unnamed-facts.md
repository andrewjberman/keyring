# ETFS_RIVALS task order -- `RIV-wh-1` -- WORKSTREAM 3: NO AI FACT PRINTS $0.0 MILLION OR A BARE IDENTIFIER; A ZERO NOTIONAL IS NEVER A FACT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-wh-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~31</issued_to>
<issued_by>2.0.0_SA_COO~V1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; no S3 or deploy act
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work; at the cut nothing is returned, and the evidence context is this order's check file (dry-run at the base: FAIL 4 as expected, the negative arm and the control PASS)
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric dell1) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two
peer groups): rankings, buying trend, AI accounts, a security dialog per holding with a price chart, and an audit page.
Code: `data/etfs/scripts/rivalfunds/` (run from `data/etfs/scripts`, package `rivalfunds`); tests:
`data/etfs/scripts/rivalfunds/tests/` (pytest from `data/etfs/scripts`).

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-wh-1` -- no AI fact prints '$0.0 million' or a bare security identifier; a zero notional is never a fact (repair of RIV-aw-1's J1 NOT MET; rows D1-C-S4, D1-S9) -- APPENDED 2026-10-09, revision 1.25
- Placement: `ledger/CTO_RULING_WORKSTREAM2_SPLIT_ADJUST_TRADE_LIST_SCOPE_20261009.md` ADDENDUM 5 @ceab50de56
  (1.0.0_SA_CTO~DELL1 msg 2497).
- Measured: the served 13:00Z sweep of 2026-10-09 (research_hypotheses-20261009T130227Z-ai, a1-chain/7) carries '$0.0
  million' 7 times (WCMG, ETFT) and the bare CUSIP 037833100 for Apple Inc in GQGU's 30-day account ("The fund added
  037833100 for $8.1 million"; cited row `GQGU|037833100|2026-09-10`). The issuer's a1-chain/8 real run repeats the '$0.0
  million' (WCMG, ETFT, three each). Causes: `_mn` shows millions at one decimal, so any |v| < 50,000 is '$0.0 million';
  `fact_pack` names a trade `names.get(key) or _name(...)`, which falls back to the raw key when no name resolves.
- Interface (all in `ai_accounts.py`):
  1. `_mn(v)`: |v| < 50,000 -> thousands, e.g. '$42 thousand' (whole thousands); |v| >= 50,000 -> millions at one
     decimal, as today. The facts' `display:` form follows, so the model copies it (SYSTEM rule 1 allows the display form).
  2. `fact_pack` leaves out a trade whose notional is exactly 0 (never '$0 thousand').
  3. `fact_pack` never puts a bare identifier (the raw `security_key` or `security_id`) in a fact's text: the name comes
     from `names`, then the row's own name field(s) if the trade row carries one, then any name the function can already
     reach for that security; a trade with no name left is left out of the facts.
  4. SYSTEM rule 1 names the thousands form beside the millions form.
- Out of bounds: every other file; no vendor call, no S3, no deploy. The real-model read is the issuer's, at the drain.
- Check: `ws3_item8_prep/wh1_small_notional_and_unnamed_check.py` (AC1; base FAIL 4; the EDGE negative arm and the NAMED
  control PASS). J1 (CVO): on the issuer's real 13-fund run, 0 '$0.0 million' and 0 bare identifiers in any item.

### The workstream's guards (verbatim)

GUARDS on every cell: (1) no deploy and no served write before both round-28 J1 reads (tw-1 at the 2026-10-09 11:00Z
vehicle run, aw-1 at the 13:00Z sweep); (2) no edit to `data/etfs/scripts/rivalfunds/enrichment_bloomberg.py` (a cell that
finds it must, files a row and stops); (3) every deploy or served write goes under its own never-widen pair.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base box/dell1)

- Read the check before you build. It FAILS at the base (4 failures) and is your target; do not edit it.
  `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws3_item8_prep/wh1_small_notional_and_unnamed_check.py`
  builds `fact_pack` on a five-row fixture. Its EDGE arm ($60,000 reads '$0.1 million') and NAMED arm pass at the base and
  must keep passing.
- `ai_accounts.py`: `SYSTEM` (~line 67, rule 1 names the display forms), `_mn` (~131), `fact_pack` (~146; the trade loop
  ~170-182 builds `nm = names.get(str(k)) or _name(dict(r, bucket=k))`). The other two checks of this file must keep
  passing: `ws3_item8_prep/item8_generic_opener_check.py` (ITEM8 RESULT: PASS) and
  `ws3_item8_prep/w26s1_ai_below_tolerance_check.py` (W26-S1 AI RESULT: PASS). Tests that pin `_mn` output or fact text
  live in `rivalfunds/tests/`.

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, `publish_page.py`, `render.py`,
`enrichment_bloomberg.py`, the decomposition and the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~31/`).
NEVER: any S3 read or write outside a memory sink, any deploy, gateway release or Terraform, any vendor call (Bloomberg,
OpenAI, a live web search), any environment gate flip outside a test. A row you file goes in the investigation file below
with id `ETFS_RIVALS-D1-W31-S<k>`, `"fabric": "dell1"`.

<paths>
data/etfs/scripts/rivalfunds/ai_accounts.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- no '$0.0 million', no zero-notional fact, no bare identifier; the negative arm and the control unchanged.
- **J1** -- the CVO's, on the issuer's real run (not yours).

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-wh-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws3_item8_prep/wh1_small_notional_and_unnamed_check.py</invocation><expect>WH1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-wh-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line, and
the last line of each of the two other ai_accounts checks named in section 2.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~31/ETFS_RIVALS.TO-RIV-wh-1.small-notional-and-unnamed-facts.proof_of_spec.json`
with `to_id` `ETFS_RIVALS.TO-RIV-wh-1.small-notional-and-unnamed-facts`. Report once: AC1's verdict line with the output
above it; J1 left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; the new `_mn` and the naming order verbatim; the
suite's final line; every existing test assertion changed and why; rows filed (id + one line); anything the issuer must do
at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L6, 2.0.0_SA_COO~V1):** Repair of RIV-aw-1's J1 NOT MET (CVO ADDENDUM 3 @7d962bb14e, row D1-C-S4) and row
D1-S9, placed by 1.0.0_SA_CTO~DELL1 ruling ADDENDUM 5 @ceab50de56 (msg 2497), with its addition (a zero notional is left
out). Decomposition revision 1.25. Cell id and slot listed before naming (0 hits for RIV-wh-1, slot ~31, workstream 3f).
Check dry-run at the base (box/dell1 @8f8aab6157+): WH1 RESULT: FAIL 4 failures (SMALL, ZERO, CUSIP, $0.0); EDGE and NAMED
PASS. Rides the WS2/WS3 deploy pair as one pair.

<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>28</round>
<workstream>3f</workstream>
<slot>~31</slot>
<fabric>dell1</fabric>
