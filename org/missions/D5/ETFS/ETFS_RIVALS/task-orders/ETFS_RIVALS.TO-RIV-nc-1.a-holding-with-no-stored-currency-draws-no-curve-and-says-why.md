# ETFS_RIVALS task order -- `RIV-nc-1` -- ROUND 17: A HOLDING WITH NO STORED CURRENCY DRAWS NO CURVE AND SAYS WHY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-nc-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~7</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (one constant in a module and one branch in the page's inline script)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check file and the round-16 measurement
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, a security dialog per holding, and a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway. Rounds 15 and 16 built the security dialog's price curve: a per-security price series (`price_series.py`), a per-fund chart object written by the publisher, and the page's one script that draws it (`render.py`, `CHART_SCRIPT`); a holding-implied price is drawn only for a listing whose stored quote currency is USD, and the chart object carries each security's `currency`. All of that is merged. **This order, round 17, is one small cell.** Nothing here deploys, merges or calls a vendor (stub every OpenAI and Bloomberg hook). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-nc-1` -- a holding with no stored currency draws no curve and says why (FWD-22; CTO ruling 30817 term 2)
- Measured (round-16 real run, day 2026-10-06): 96 of 695 fund-securities carry `"currency": null` in their chart object
  (no G4 row in the 365-day window); the script draws their frame as an empty chart with a shaded gap.
- Interface: `price_series.NO_HISTORY = "No price history is stored for this holding yet."`. For a key with no stored
  currency, `series` returns `source_words` equal to `NO_HISTORY` exactly (its points stay all `None`, its `currency`
  `None`, its gaps as today). The page's one script, for a security whose `currency` is `null`: draws NO chart (no
  `<svg>` in the frame, no axis, no shaded gap, no gap-reason list), sets the frame's status line to the object's
  `source_words` (so the sentence comes from the object, and the same sentence is in the script as its fallback when
  `source_words` is absent), and changes nothing else: the range buttons may stay, and the static trade list stays.
  A security WITH a stored currency is drawn exactly as today, whatever its number of priced points.
- Rulings at the cut (issuer): the test is `currency == null` in the object, never "no priced point" (a non-dollar listing
  with 0 closes in a range but a stored currency still draws its frame and gap reason). No change to the chart object's
  keys or to `publish_page.py`. The sentence is not shown on the audit page (it carries no script).
- **Organic trigger:** opening the dialog of a holding that left the funds before the market table began; the issuer's
  real run reads the 96 in a browser.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 0f7e460190 or later)

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/nc-1.AC1.py` and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/_common.py` before you build. Where the docstring and the cell's "Rulings at the cut" differ, the RULING wins and the check accepts it.
- `price_series.py` today: `_currencies(g4, wanted)` gives key -> stored currency; `_words(codes, currency, usd)` writes `source_words`; a key with no stored currency currently gets the non-dollar words ending "(the currency is not on file)". Only the no-stored-currency case changes; a stored non-dollar currency keeps its words.
- `render.CHART_SCRIPT` is the page's ONE inline script (plain text in a Python string). The package suite runs its `plan` and `words` functions under node and `node --check` parses it; `render.validate` refuses a second script, `src=`, `<link`, `@import` and `url(`. It already reads `.currency` and says "currency not on file" beside the axis for a null currency: with this cell a null-currency security never reaches the axis, but the words stay in the script (the check pins them).
- The sentence must appear in the script exactly once as text.
- Where the script decides this, keep it testable under node the way `plan` is: say in the report which function carries the branch and which test exercises it.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-22, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~7/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r17nc1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing; read the file's existing row ids first and take an unused one), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/price_series.py
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the constant and the series' words for a key with no stored currency; the sentence once in the page's script; pc-1.AC1, pc-1.AC2 and md-1.AC2 still PASS; control: the fixture holds no G4 row for that key (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/nc-1.AC1.py`)
- **J1** (judgment, graded by 3.0.0_SA_CVO~RV on the issuer's real run, never by you): in a browser, the dialog of a holding with no stored currency shows no chart and the sentence, and a holding with a stored currency is drawn as before.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-nc-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/nc-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-nc-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~7/ETFS_RIVALS.TO-RIV-nc-1.a-holding-with-no-stored-currency-draws-no-curve-and-says-why.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-nc-1.a-holding-with-no-stored-currency-draws-no-curve-and-says-why`. Report once: the mechanical criterion's verdict line with the output above it; the judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; which script function carries the branch and which test exercises it; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.18 @6e245cbebe (ADMITTED: ratified half signed by 3.0.0_SA_CVO~RV); decomposition v1.7 (round 17 appended). Source: the ruling of 1.0.0_SA_CTO~Z msg 30817 term 2 ("until a key has a stored currency the modal draws no curve and says why in plain words ... never an empty chart"), answering the round-16 packet @f00567cd5f. Term 1 (the backfill's list includes formerly-held keys, inside the bbg_budget ledger, split by day if over one day's allowance) is the issuer's act at the backfill run. Chain `~7`, slot `~7`, position 1 of 1. Check written and dry-run at base 0f7e460190 by the issuer: nc-1.AC1 FAIL 2 failures as expected (arms a, c; arms b, d and the control e PASS).

<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>17</round>
<slot>~7</slot>
<fabric>site-z</fabric>
<status>complete</status>
