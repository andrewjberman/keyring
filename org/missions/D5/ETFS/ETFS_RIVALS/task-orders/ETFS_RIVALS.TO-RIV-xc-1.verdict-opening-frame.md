# ETFS_RIVALS task order -- `RIV-xc-1` -- NO TWO FUNDS' VERDICT OPENINGS SHARE A NAME-ABSTRACTED FRAME ON ONE PAGE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-xc-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~37</issued_to>
<issued_by>2.0.0_SA_COO~V1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; no S3 or deploy act
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work; at the cut nothing is returned, and the evidence context is this order's check file(s) (dry-run at the base: FAIL as expected)
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric dell1) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two
peer groups): rankings, buying trend, AI accounts, a security dialog per holding with a price chart, and an audit page.
Code: `data/etfs/scripts/rivalfunds/` (run from `data/etfs/scripts`, package `rivalfunds`); tests:
`data/etfs/scripts/rivalfunds/tests/` (pytest from `data/etfs/scripts`).

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-xc-1` -- no two funds' Direction Verdict openings share a name-abstracted frame on one page (round 28 analysis section 2.7; the CVO's round-29 item at ADDENDUM 4) -- APPENDED 2026-10-12, revision 1.29
- Placement: `ledger/ROUND_ANALYSIS.round28.md` section 2.7 and section 3 item 4 (msg 4558); CVO ADDENDUM 4 (row D1-C-S5).
- Measured (the 2026-10-12 page, `sweep_read.py`): 13 Direction Verdict openings; the CVO's own measure found 6 of 13 sharing a
  name-abstracted frame ("<name> is the clearest fund-specific tell: ..." is the common one). `ai_accounts.opening_check`
  (RIV-wg-1) tests one opening alone (a generic period phrase); no code compares openings ACROSS funds. `run_chain` (one fund,
  two chats and at most one correction per item) is called once per fund by `run_day`, in a loop with no shared state.
- Interface (`data/etfs/scripts/rivalfunds/ai_accounts.py` only; `PROMPT_VERSION` stays `a1-chain/8`; no prompt text changes):
  1. `frame_of(text) -> str`: take the first sentence (split as `opening_check` does, at the first sentence-final `.`, `!` or
     `?` followed by whitespace); tokenise on whitespace; strip any of `,;.!?"'()` from both ends of a token (keep `:`); a
     token containing a digit is `<n>`; a token that begins with an uppercase letter and is not one of the sentence-initial
     words `the a an in on over from between these this its it for with as at by` is NAME-like, and a maximal run of NAME-like
     tokens (a connector token `&`, `-`, `of`, `de` or `and` counts inside a run when a NAME-like token follows it) is ONE
     `<name>`; consecutive `<n>` collapse to one; lowercase everything else; the frame is the first FIVE resulting tokens
     joined by single spaces (fewer if fewer). `frame_of("")` is `""`. Examples that must hold: "Alpha Co is the clearest
     fund-specific tell: it was bought." and "Beta Corp is the clearest fund-specific tell: it was sold." both give
     `<name> is the clearest fund-specific`; "Alpha Co is the clearest tell: it was bought." gives `<name> is the clearest
     tell:`; "Alpha Co added $2.7 million over 2026-09-01 to 2026-09-30." gives `<name> added <n> million over`.
  2. `run_chain(..., seen_frames: dict | None = None)`: when given, a `direction_verdict` item whose `frame_of(text)` is already
     a key of `seen_frames` (frame -> the fund id that first used it) gets ONE more defect in the item's existing
     `opening` list, so the chain's existing one-correction path sends it back once and the corrected reply replaces it and is
     graded as today: `the opening shares its frame "<frame>" with <fund>'s verdict on this page: open with the single finding
     most particular to this fund, in different words from that opening`. After the final reply, `seen_frames.setdefault(
     frame_of(final text), fund_id)` (a non-empty frame only). With `seen_frames` None nothing changes.
  3. `run_day` creates ONE `seen_frames = {}` before its fund loop and passes it to every `run_chain` call (in the universe's
     order), including the retry attempt.
- Out of bounds: every prompt constant, `opening_check`, `grounding_check`, `wording_check`, `ai_stage.py`, `sweep.py`, any vendor
  call (a stub client only), `PROMPT_VERSION`.
- Checks: `round29/checks/xc1_frame_check.py` (AC1; base FAIL 4) and the existing AI tests (AC2: must stay green). J1 (the
  CVO's): on the next sweep page no two openings share a frame by the CVO's own measure, or a correction is on the record for
  each that did.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base box/dell1)

- Read the check before you build: `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round29/checks/xc1_frame_check.py`. It FAILS at the base (4 failed) and is your target; do not
  edit it. It drives `run_chain` with a stub client (`chat`, `web_search`) shaped like `tests/test_r28wg1_direction_opening.py`.
- `ai_accounts.run_chain` (about line 561): per item `assess(raw, windows, kind)` builds `a["opening"]` from `opening_check`;
  `if a["wording"] or a["figures"] or a["opening"]` sends ONE correction and re-assesses. Add the frame defect to the same
  `opening` list for `kind == "direction_verdict"` only; do not add a second correction path.
- `run_day` (about line 817) loops the universe's funds calling `run_chain` inside `for attempt in (1, 2)`; the shared dict
  is created once before that loop.
- `PROMPT_VERSION` is pinned `a1-chain/8` by `tests/test_r28wg1_direction_opening.py`; do not change a prompt or the version.
## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, Terraform, the decomposition and
the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~37/`).
NEVER: any S3 read or write outside a LocalSink or memory sink, any deploy, gateway release or Terraform, any vendor call
(Bloomberg, OpenAI, Bright Data or any live web search -- inject `search` or the client), any Secrets Manager call, any
environment gate flip outside a test. A row you file goes in the investigation file below with id
`ETFS_RIVALS-D1-W37-S<k>`, `"fabric": "dell1"`.

<paths>
data/etfs/scripts/rivalfunds/ai_accounts.py
data/etfs/scripts/rivalfunds/tests/test_riv_xc1_verdict_frame.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from the repository root)

- **AC1** -- the check file: `frame_of` examples; a colliding opening is corrected once and the reply stands; a distinct frame
  or an absent dict draws no correction; `run_day` shares one dict.
- **AC2** -- the existing AI tests are unchanged and green.
- **J1** -- the CVO's read of the next sweep page, not yours.
<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-xc-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round29/checks/xc1_frame_check.py</invocation><expect>4 passed</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-xc-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider rivalfunds/tests/test_r28wg1_direction_opening.py rivalfunds/tests/test_r28aw1_words_and_figures.py rivalfunds/tests/test_r8gc1_attach_uncited.py</invocation><expect>all passed, 0 failed</expect></criterion>
  <criterion id="J1" cell_refs="RIV-xc-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~37/ETFS_RIVALS.TO-RIV-xc-1.verdict-opening-frame.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-xc-1.verdict-opening-frame`. Report once: each criterion's verdict line with the output above it;
files written; every existing test assertion you changed and why; rows filed (id + one line); anything the issuer must do at
the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L6, 2.0.0_SA_COO~V1):** Round 29 of ETFS_RIVALS, ONE issuance on `ledger/ROUND_ANALYSIS.round28.md` section 3
(msg 4558). Decomposition revision 1.29. Check file(s) dry-run at the base before the cut. Chain C (one file, `ai_accounts.py`); no edge to another cell.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<!-- drained 2026-10-12 by 2.0.0_SA_COO~V1 @84bc9f8e34: AC1 4 passed, AC2 23 passed, instance VALID (checked in the worktree); suite 1016 passed, 6 skipped. Row D1-W37-S1 (the stoplist match is case-insensitive and applies to every token, so `AT & T` reads `at & <name>`): ruled ACCEPT AS BUILT -- the frame has to be deterministic and equal across funds, not linguistically exact; no change, no cell. J1 is the CVO's on the next sweep page. -->
<round>29</round>
<workstream>4</workstream>
<slot>~37</slot>
<fabric>dell1</fabric>
