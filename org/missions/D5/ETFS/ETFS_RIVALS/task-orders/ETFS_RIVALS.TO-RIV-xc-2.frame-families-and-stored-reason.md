# ETFS_RIVALS task order -- `RIV-xc-2` -- THE FRAME INSTRUMENT COMPARES FAMILIES, AND A CORRECTION'S REASON IS STORED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-xc-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~39</issued_to>
<issued_by>2.0.0_SA_COO~V1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; no S3 or deploy act
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work; at the cut nothing is returned, and the evidence context is this order's check file (dry-run at the base: FAIL as expected)
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric dell1) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two
peer groups): rankings, buying trend, AI accounts (a Direction Verdict per fund), a security dialog per holding, and an audit page.
Code: `data/etfs/scripts/rivalfunds/` (run from `data/etfs/scripts`, package `rivalfunds`); tests:
`data/etfs/scripts/rivalfunds/tests/` (pytest from `data/etfs/scripts`).

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-xc-2` -- the frame instrument compares FAMILIES, and a correction's reason is stored (round-29 analysis ruling 2; row D1-C-S20; recut of RIV-xc-1) -- APPENDED 2026-10-14, revision 1.30
- Measured (the 2026-10-14 page): repetition fell from 5 of 13 to 2 of 13, but IDVZ ("is the clearest fund-specific tell") and TXUE ("is the clearest
  tell") share one frame family with 0 corrections: `frame_of`'s five-token window splits them at token 5, so the code's own instrument passed what a
  reader sees as one frame. `input_manifest` recorded no correction reason.
- Interface (`data/etfs/scripts/rivalfunds/ai_accounts.py` only; `PROMPT_VERSION` stays `a1-chain/8`; no prompt text changes): `frame_of` v2.
  1. Steps as v1 up to the token list: first sentence (split at the first `.`, `!` or `?` followed by whitespace), whitespace tokens, each stripped of
     `,;.!?"'()` at both ends (`:` kept), a digit token is `<n>` (consecutive `<n>` collapse), a run of name-like tokens is one `<name>`, the rest lowercased.
  2. THE CLAUSE: the tokens up to and including the first whose raw form ends in `:`; with none, the whole first sentence.
  3. THE STOP-LIST: a module constant `FRAME_STOP = frozenset(("fund-specific", "most", "single", "particular"))`; those tokens are removed from the clause.
     `clearest` is not in it: it stays as the head word.
  4. The frame is the first EIGHT tokens of the clause, joined by single spaces. `frame_of("")` is `""`.
  Examples that must hold (the check pins them): "Alpha Co is the clearest fund-specific tell: it was bought. More." and "Beta Corp is the clearest tell:
  it was sold." both give `<name> is the clearest tell:`; "Gamma Co stands out most: it was sold." gives `<name> stands out:`; "Alpha Co added $2.7 million
  over 2026-09-01 to 2026-09-30." gives `<name> added <n> million over <n> to <n>`.
  5. `run_chain`: when a direction verdict's first reply shares its frame (the existing `seen_frames` path, unchanged: ONE correction through the chain's
     existing path), the item's `input_manifest` gains `"shared_frame_with": "<fund>"` (the fund that first used the frame), whether or not the correction
     succeeded. A reply that STILL shares the family after the one correction is marked, not re-sent: its manifest also gains `"frame_still_shared": true`.
     A first fund, a distinct frame and an `activity_30d` row carry neither key. First fund wins the `seen_frames` record, as today.
- Out of bounds: every prompt constant, `opening_check`, `grounding_check`, `wording_check`, `ai_stage.py`, `sweep.py`, any vendor call (a stub client only),
  `PROMPT_VERSION`.
- Checks: `round30/checks/xc2_frame_family_check.py` (AC1 the families and the planted IDVZ/TXUE pair reading SAME, with its control; AC2 the stored reason
  and the marking; base FAIL 2) and the AI tests including `tests/test_riv_xc1_verdict_frame.py`, which you REWRITE to the v2 rule (AC3: must be green).
  J1 (the CVO's): on the next sweep page 13 of 13 openings fall in distinct families by the normalized `frame_of`, or each shared one carries a stored
  correction reason.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base box/dell1)

- Read the check before you build: `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xc2_frame_family_check.py`. It FAILS at the base
  (2 failed) and is your target; do not edit it. Its module docstring restates the v2 rule.
- The code today: `ai_accounts.py` `_FRAME_INITIAL`, `_FRAME_CONNECT`, `_FRAME_STRIP`, `_frame_name` and `frame_of` (about lines 529-569; `frame_of` takes the
  first five tokens); `run_chain` (about line 604) has the `assess` closure that adds the frame defect when `frame_of(p["text"])` is in `seen_frames`
  (about line 653), the one-correction block, the `seen_frames.setdefault` record (about line 674) and the `manifest = json.dumps(dict(base, attached_figures=..,
  corrections=.., ...))` (about line 682). `run_day` (about line 869) already passes one `seen_frames` dict to every `run_chain` call.
- To store the reason you need the fund the FIRST reply collided with: capture it where `assess` finds the collision (before the correction replaces the
  reply), and put it into the manifest of that same item. The `frame_still_shared` mark reads the FINAL reply: its frame is a key of `seen_frames` held by a fund
  other than this one, after the one correction.
- `tests/test_riv_xc1_verdict_frame.py` pins the v1 rule (five tokens, no stop-list, no colon clause). Rewrite its assertions to the v2 rule, keeping each test's
  intent (name runs through a connector, digit collapse, first sentence only, a second colliding reply is not corrected twice and the first fund keeps the frame).
  List every assertion you changed in your report.
- Do not run `round29/checks/xc1_frame_check.py`: it pins the v1 frame and is superseded by this cell's check.

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, Terraform, the decomposition and
the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~39/`).
NEVER: any S3 read or write outside a LocalSink or memory sink, any deploy, gateway release or Terraform, any vendor call
(Bloomberg, OpenAI, Bright Data or any live web search -- a stub client only), any Secrets Manager call, any environment gate flip outside a test.
A row you file goes in the investigation file below with id `ETFS_RIVALS-D1-W39-S<k>`, `"fabric": "dell1"`.

<paths>
data/etfs/scripts/rivalfunds/ai_accounts.py
data/etfs/scripts/rivalfunds/tests/test_riv_xc1_verdict_frame.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from the repository root)

- **AC1** -- `frame_of` v2: the families, the planted IDVZ/TXUE pair reading SAME, its control reading different.
- **AC2** -- the correction's reason is stored in `input_manifest`; a still-shared reply is marked and not re-sent.
- **AC3** -- the AI tests, with `test_riv_xc1_verdict_frame.py` rewritten to v2, are green.
- **J1** -- the CVO's read of the next sweep page, not yours.
<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-xc-2"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xc2_frame_family_check.py -k ac1</invocation><expect>1 passed</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-xc-2"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xc2_frame_family_check.py -k ac2</invocation><expect>1 passed</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-xc-2"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider rivalfunds/tests/test_riv_xc1_verdict_frame.py rivalfunds/tests/test_r6ap1_ai_stage.py rivalfunds/tests/test_r15pd3_ai_periods.py rivalfunds/tests/test_r8an1_ai_prose_one_name.py</invocation><expect>the final line reads N passed with no failed and no error</expect></criterion>
  <criterion id="J1" cell_refs="RIV-xc-2" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~39/ETFS_RIVALS.TO-RIV-xc-2.frame-families-and-stored-reason.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-xc-2.frame-families-and-stored-reason`. Report once: each criterion's verdict line with the output above it;
files written; every existing test assertion you changed and why; rows filed (id + one line); anything the issuer must do at
the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L6, 2.0.0_SA_COO~V1):** Round 30, workstream `page`, ONE issuance on `ledger/ROUND_ANALYSIS.round29.md` section 3 items 1 and 2 (msg 5567).
Decomposition revision 1.30. Check file dry-run at the base before the cut: xc2 base: FAIL (2 failed) as expected; AC3's control base: PASS (24 passed) as expected.
Chain B (`ai_accounts.py` and its test file); no edge to xa-2. Deploy and the CVO's J1 read at the next sweep follow in the round's apply leg.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>30</round>
<workstream>4</workstream>
<slot>~39</slot>
<fabric>dell1</fabric>
