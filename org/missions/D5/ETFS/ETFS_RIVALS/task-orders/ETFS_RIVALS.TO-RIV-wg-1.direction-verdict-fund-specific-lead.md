# ETFS_RIVALS task order -- `RIV-wg-1` -- WORKSTREAM 3: THE DIRECTION VERDICT LEADS WITH WHAT IS PARTICULAR TO THE FUND; NO BELOW-TOLERANCE ROW IS OFFERED AS A TRADE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-wg-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~30</issued_to>
<issued_by>2.0.0_SA_COO~V1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; no S3 or deploy act
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work; at the cut nothing is returned, and the evidence context is this order's two check files (dry-run at the base: FAIL as expected, each control arm PASS)
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric dell1) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two
peer groups): rankings, buying trend, AI accounts, a security dialog per holding with a price chart, and an audit page.
Code: `data/etfs/scripts/rivalfunds/` (run from `data/etfs/scripts`, package `rivalfunds`); tests:
`data/etfs/scripts/rivalfunds/tests/` (pytest from `data/etfs/scripts`).

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-wg-1` -- the Direction Verdict leads with what is particular to the fund; a below-tolerance row is never offered to the model as a trade (WS3 item 8; row W26-S1's ai_accounts half) -- APPENDED 2026-10-09, revision 1.24
- Measured: on the served 2026-10-08 page, 13 of 19 distinct Direction Verdicts open "The last thirty days ..."
  (`ws3_item8_prep/verdict_openers_check.py`: FAIL, limit one quarter). Andrew-direct comment 7: "when every single
  fund is saying the same thing, its not very interesting for the reader ... We may need to give more token budget or
  more specific prompting". `P_DIRECTION` (ai_accounts.py ~line 90) asks four questions in a fixed order and SYSTEM caps
  every item at 120-180 words. Row W26-S1: `fact_pack`'s trade facts (~line 170) keep `below_tolerance` rows (RIV-wd-1),
  so on a fixture a below-tolerance row is trade fact T1, ahead of the real buy and sell.
- Interface:
  1. `P_DIRECTION` asks the verdict to OPEN with the single finding most particular to this fund (a named security,
     sector or trade and its fact), and never with a sentence about the periods agreeing or disagreeing in general. The
     verdict's `text` budget is 180-260 words; the 30-day account keeps 120-180.
  2. `wording_check` (or a sibling the chain calls for the `direction_verdict` item only) names a GENERIC OPENING as a
     defect: the text's first sentence begins with a period phrase ("the last thirty days", "the last 30 days", "over the
     last", "these trades", "the trades") followed within its first twelve words by one of "add to", "support",
     "contradict", "borne out", "bear out", "bore out", "confirm"; OR the first sentence begins with the period's dates
     ("From <date> to <date>", "Between <date> and <date>", "Over <date> to <date>") -- the lead the live prompt
     a1-chain/7 produced on 2026-10-09 for both funds of the issuer's two-fund base run (CGIC, IDVZ), and on the
     served 13:00Z sweep for 13 of 13 funds (row D1-S8). The two dates are
     still stated once in `text` (RIV-aw-1), just not as the lead. The ONE correction already in `run_chain` sends it back
     quoting the opening. A generic opening never sets grounding FAIL by itself: after the correction the reply stands.
  3. `fact_pack` drops trade rows whose `action` is `below_tolerance`, as `publish_page` already does for the trade log.
  4. `PROMPT_VERSION` moves to `a1-chain/8`.
- Out of bounds: `publish_page.py`, `render.py`, `gold_trade_schedule.py`, `enrichment_bloomberg.py`; no vendor call, no S3,
  no deploy (WS2 guards). The real-model read is the issuer's, at the drain.
- Checks: `ws3_item8_prep/item8_generic_opener_check.py` (AC1; base FAIL 3 on arms A and C, control arm B PASS) and
  `ws3_item8_prep/w26s1_ai_below_tolerance_check.py` (AC2; base FAIL 1, control arm PASS). J1 (CVO): on the issuer's real
  run over the 13 funds, no opening leads more than a quarter of the verdicts (`verdict_openers_check.py`), and the
  verdicts read as fund-specific.

### The workstream's guards (verbatim)

GUARDS on every cell: (1) no deploy and no served write before both round-28 J1 reads (tw-1 at the 2026-10-09 11:00Z
vehicle run, aw-1 at the 13:00Z sweep); (2) no edit to `data/etfs/scripts/rivalfunds/enrichment_bloomberg.py` (a cell that
finds it must, files a row and stops); (3) every deploy or served write goes under its own never-widen pair.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base box/dell1)

- Read both checks before you build. Each FAILS at the base and is your target; do not edit them.
  `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws3_item8_prep/item8_generic_opener_check.py` drives
  `run_chain` with a scripted client; `.../ws3_item8_prep/w26s1_ai_below_tolerance_check.py` builds `fact_pack` on a fixture.
  Each has a control arm that passes at the base and must keep passing.
- `ai_accounts.py`: `SYSTEM` (~line 67; its rule 6 states the 120-180 word budget for `text`), `P_DIRECTION` (~90),
  `fact_pack` (~146; the trade filter ~170), `wording_check` (~460), `run_chain` (~517; the ONE correction loop ~566 calls
  `assess`, which calls `wording_check`; a wording defect after the correction sets grounding FAIL at ~580 -- a generic
  opening must NOT reach that line). Existing tests that pin prompt text or `PROMPT_VERSION` live in
  `rivalfunds/tests/` (e.g. test_r6ui4_ai_account_cards.py, test_regrade_call11.py).

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, `publish_page.py`, `render.py`,
`enrichment_bloomberg.py`, the decomposition and the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~30/`).
NEVER: any S3 read or write outside a memory sink, any deploy, gateway release or Terraform, any vendor call (Bloomberg,
OpenAI, a live web search), any environment gate flip outside a test. A row you file goes in the investigation file below
with id `ETFS_RIVALS-D1-W30-S<k>`, `"fabric": "dell1"`.

<paths>
data/etfs/scripts/rivalfunds/ai_accounts.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a generic Direction Verdict opening is sent back once and replaced; a specific one is not.
- **AC2** -- a below-tolerance row is never a trade fact; the buy and the sell stay.
- **J1** -- the CVO's, on the issuer's real run (not yours).

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-wg-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws3_item8_prep/item8_generic_opener_check.py</invocation><expect>ITEM8 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-wg-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws3_item8_prep/w26s1_ai_below_tolerance_check.py</invocation><expect>W26-S1 AI RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-wg-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~30/ETFS_RIVALS.TO-RIV-wg-1.direction-verdict-fund-specific-lead.proof_of_spec.json`
with `to_id` `ETFS_RIVALS.TO-RIV-wg-1.direction-verdict-fund-specific-lead`. Report once: AC1's and AC2's verdict lines
with the output above them; J1 left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; the new `P_DIRECTION` text and
the generic-opening rule verbatim; the suite's final line; every existing test assertion changed and why; rows filed
(id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L6, 2.0.0_SA_COO~V1):** WS3's second issuance (decomposition rev 1.20: item 8 cut only after aw-1's J1
read at the 13:00Z sweep; read 13:1xZ, ledgers closed @4bbd1fb88b, counts to the CVO), joined with row W26-S1's ai_accounts half because both write `ai_accounts.py` (cut by write
set). Andrew-direct comment 7 (@588865eef8). Decomposition revision 1.24. Cell id and slot listed against every existing
id in the project tree before naming (0 hits for RIV-wg-1, slot ~30, workstream 3e; control: slot ~29 found in wf-1).
Checks dry-run at the base: item8_generic_opener_check FAIL 3 (arms A and C; control arm B PASS);
w26s1_ai_below_tolerance_check FAIL 1 (control arm PASS) @a3bf5a8596.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>28</round>
<workstream>3e</workstream>
<slot>~30</slot>
<fabric>dell1</fabric>
