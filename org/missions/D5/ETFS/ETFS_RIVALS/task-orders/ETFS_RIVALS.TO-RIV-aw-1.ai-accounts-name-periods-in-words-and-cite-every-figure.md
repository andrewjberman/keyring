# ETFS_RIVALS task order -- `RIV-aw-1` -- ROUND 28: AN AI ACCOUNT NAMES ITS PERIODS IN WORDS WITH THEIR DATES AND CITES EVERY DOLLAR FIGURE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-aw-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~21</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (the AI account module; it writes only the table ai_accounts already writes)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files, the CTO's rulings of 2026-10-07 on round 25 and the rows they cite
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, a security dialog per holding, and a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway. Round 15 moved every period on the page to the last 30 / 90 / 365 calendar days. The buying trend shows, beside its net figure, a month-by-month strip (bought / sold / no trade per month). Each security dialog also lists the fund's trades in the security and draws a price chart by the page's one inline script. A security named in a table or in an account's text is a button that opens that security's one dialog, which carries a section per fund. The page's price charts and rankings read closes from the gold table `security_market`, which today holds five trading days. PRD outcome FWD-24: every security a tracked fund held in the last 365 days has its year of closes, kept by the daily Bloomberg leg, which prints what is owed, asks inside the budget and carries the rest. **This order is one of the two cells of round 28; no vendor and no model is called by anything you build or test.** Nothing here deploys, merges or calls a vendor (stub every OpenAI and Bloomberg hook). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-aw-1` -- an AI account names its periods in words with the window's two dates, never by the system's codes, and cites a row for every dollar figure; one correction call when it does not (CTO rulings R19, R20; rows C-S83; ROUND_ANALYSIS.round22 ADDENDUM 6)
- Measured (served page 2026-10-08, 13:08Z): 26 account items over 13 funds. The codes `R30`, `R90` and `R365` reach the
  reader 240 times ("The top R30 contributor ..."): the SYSTEM prompt teaches the codes and the fact lines carry them.
  One item (TXUE, the 30-day account) is shown as grounding FAIL: it states "$1.2 million" and cites no row for it, and
  three uncited facts round to that amount, so `attach_uncited` cannot attach one
  (`deliverables/2.0.0_SA_COO~RV/round28_prep/R20_TXUE_GROUNDING_FAIL_READ_20261008.md`). Where exactly one uncited fact
  matches, `attach_uncited` attaches it silently and the item reads "Grounded".
- Interface (`data/etfs/scripts/rivalfunds/ai_accounts.py` only):
  1. **Words, not codes.** `PROMPT_VERSION` becomes `a1-chain/7`. The SYSTEM prompt and the TEXT of every fact line
     given to the model name a period as "the last 30 days", "the last 90 days" or "the last 365 days" and never contain
     the tokens `R30`, `R90`, `R365` (a fact's `id` and its `cited_row` keys keep the codes: they are keys, not prose).
     Each prompt names, once, the two end dates of each period it covers, as ISO dates, taken from the same window the
     fact pack is built on (the 30-day account: the 30-day window; the direction verdict: the 30-, 90- and 365-day
     windows), and tells the model to state the window's two dates once in `text`.
  2. **A wording check**, a new pure function `wording_check(text_fields, windows) -> list[str]` (empty = clean): it
     returns one reason per defect over the item's `text`, `observed`, `inferred` and `invalidation`: (a) a period code
     as a whole word, case-insensitive (`R30`, `R90`, `R365`; also `MTD`, `QTD`, `YTD`); (b) the item's own window
     dates not both present in `text` (the 30-day account: the 30-day window's two ISO dates; the direction verdict: the
     365-day window's two).
  3. **Cite every dollar figure.** The SYSTEM prompt requires the id of a fact in `cited` for EVERY figure written. A
     figure the item writes that no CITED row carries is a defect even when exactly one uncited fact matches it
     (today's silent attach).
  4. **One correction call per item.** When an item has a wording defect (2) or an uncited figure (3), the chain sends
     ONE more `client.chat` for that item: the item's own message history, the item's reply as the assistant turn, and
     one user message that lists each defect (for an uncited figure: the figure and the ids of the candidate facts;
     for a code: the code and the words to use; for missing dates: the two dates) and asks for the corrected JSON
     object. The corrected reply replaces the item and is graded once more by the same checks; there is no second
     correction. The direction verdict's own prompt is built on the FIRST reply of the 30-day account, as today: a
     correction of item 1 does not re-run item 2. At most 2 additional `chat` calls per fund per run.
  5. **What is stored.** An item still carrying a wording defect after its correction is stored with
     `grounding = "FAIL"` and the defect in `grounding_reason` (prefix `wording: `), beside any figure reasons. After the
     correction, `attach_uncited` still runs as today (an item is not failed for a figure a single fact explains), and
     the number of figures it attached is written as an integer `attached_figures` inside the row's `input_manifest`
     JSON, with `corrections` (0 or 1). No column is added to the stored table and no reader changes.
  6. `regrade_rows` / `regrade_day` re-grade stored items with the new checks and send NOTHING to a model.
- Rulings at the cut (issuer): the fix is where the words are made; nothing in `render.py` or `publish_page.py` replaces
  a code in a stored account. The page's own labels and data attributes that say R30 / R90 / R365 are not this cell's.
  NOTHING in this cell or its checks calls a model or the web: every check and test passes a stub client. The first
  real accounts under the new prompt are the 13:00Z sweep's after the deploy.
- Rulings on the check drafter's questions (issuer): a period's two dates are the `period_start` and `period_end` of
  that period's contribution rows in the fact pack (the dates the page's own period labels show), not the 30-trading-day
  trade window; `fact_pack` and `run_chain` keep today's signatures and the chain takes the windows from the facts (a
  fact may carry them). `wording_check(text_fields, windows)`: `text_fields` is a dict `{"text", "observed": [..],
  "inferred": [..], "invalidation"}`, `windows` a list of `(start_iso, end_iso)` pairs; a code's reason names the code.
  A correction is the item's history, then the item's reply byte for byte as the assistant turn, then ONE user message;
  for a figure it writes the figure as the reply wrote it and each candidate fact id as a whole token. `attached_figures`
  and `corrections` are integers in EVERY row's `input_manifest`. `regrade_rows` keeps its arguments and applies the
  wording rule and the cite-every-figure rule only to a row whose `prompt_version` is `a1-chain/7` or later (older
  stored accounts are re-graded as today). The two user-prompt templates outside the fact lines carry no code either
  (not graded by the checks: pin it in your package test). A fact id written into an item's prose counts as the code it
  contains.
- **Organic trigger:** the first 13:00Z sweep after the deploy; the issuer's read counts the codes in the 26 served
  account items (0 expected), the items stating their two dates (26 expected), the FAIL items and the sum of
  `attached_figures`.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 2dbad40215 or later)

- Read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/aw-1.AC1.py` and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/aw-1.AC2.py` before you build: their docstrings are the exact interface they read, and their stub client shows how a chat call is classified (an item's history, its reply as the assistant turn, one user message).
- `ai_accounts.py`: `SYSTEM`, `P_ACTIVITY_30D`, `P_DIRECTION`, `fact_pack` (builds each fact's `text`, `value` and `cited_row`), `attach_uncited` and `_ambiguous` (today's silent attach of a figure one uncited fact explains), `grounding_check`, `run_chain` (two chats per fund, the second built on the first reply), `regrade_rows` / `regrade_day` (re-grade stored rows; no model call).
- Every neighbouring AI check must still end `PASS 0 failures`: run every `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/*.AC*.py` before you report.
- NEVER call a model or the web: every test passes a stub client; `default_client()` is never constructed in a test.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-23, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~21/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r28aw1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing; read the file's existing row ids first and take an unused one), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/ai_accounts.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- words, not codes: the prompt version; no period code in the system prompt or any fact line sent; the windows' dates named; `wording_check`; one correction for a code, stored PASS when fixed and FAIL with `wording: ` when not; no correction for a clean reply (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/aw-1.AC1.py`)
- **AC2** -- cite every dollar figure: one correction naming the figure and its candidate facts; `attached_figures` and `corrections`; at most one correction per item and four chats per fund; the second prompt built on the first reply; `regrade_rows` calls no client (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/aw-1.AC2.py`)
- **J1** (judgment, graded by 3.0.0_SA_CVO~RV on the issuer's real read, never by you): on the first 13:00Z sweep after the deploy, the 26 served account items carry 0 period codes and state their two dates, and every dollar figure in them is cited (the issuer's count; the accounts read as plain English to a portfolio manager).

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-aw-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/aw-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-aw-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/aw-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-aw-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~21/ETFS_RIVALS.TO-RIV-aw-1.ai-accounts-name-periods-in-words-and-cite-every-figure.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-aw-1.ai-accounts-name-periods-in-words-and-cite-every-figure`. Report once: each mechanical criterion's verdict line with the output above it; the judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; where the period words and the two dates are put into each prompt; the signature of `wording_check`; the text of one correction message for a code and one for an uncited figure; how many chats a fund costs in the worst case; what `regrade_rows` does with a row older than `a1-chain/7`; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.19 @2914a61989 (ADMITTED); decomposition v1.18 (round 28 appended). Source: ROUND_ANALYSIS.round22 ADDENDUM 6 @8ea0b4a05a and CTO msg 31885. Cell ids listed against all 124 existing order ids before naming (row Z-S74's remedy): aw-1 and tc-1 are unused. Chain `~21`, slot `~21`, position 1 of 1. Checks drafted by a helper under the issuer's brief, merged @f3650a8bd9, re-run by the issuer at base 2dbad40215: aw-1.AC1 FAIL 9 (a to i; control j PASSES); aw-1.AC2 FAIL 8 (a to g, i; guard h and control j PASS). The helper's simulated build passes both; six planted defects fail the arms that grade them. The cell's rulings answer the helper's nine questions. The first real accounts under the new prompt are the 13:00Z sweep's after the Lambda deploy (a pair; the executor seat applies, ruling R22).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>28</round>
<slot>~21</slot>
<fabric>site-z</fabric>
