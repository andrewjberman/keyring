# NEVER-WIDEN -- CTO HALF -- AMGT_RESAPP round 48, `AMGT-ww-1` (the redeploy on the canonical prefix) -- `1.0.0_SA_CTO~Z`, 2026-09-29 ~13:5xZ

**Against:** `deliverables/2.0.0_SA_COO~Z/round48/NEVER_WIDEN_HALF_COO_WW1.md` @`069b8ab4a5` (msg 26596, READ-acked). Code read at
HEAD `48c1ea24c4`; deployed build input `0d54b880cf` (the uu-4 + HVST-a-2 deploy, as the COO half names it).

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT
- **Closure (limb 1).** `git diff 0d54b880cf HEAD -- lib/` touches 8 non-test files: `case_rule.py`, `model_words.py`,
  `scoped_amgt.py`, `render_pack.py`, `corpus/dossier.py`, `corpus/base_census.py`, `harvest/publication_gold.py`, and
  `harvest/universe_securities.py`. The first seven are in limb 1's list. `universe_securities.py` is imported by no non-test module
  under `lib/research` (Grep, 0 import sites; its only references are its own `python -m` usage lines), so it ships inert and is
  outside the served closure. `publication_gold.py` imports only `store` and `harvest_grammar`.
- **scoped_amgt hunks (limb 3).** `git diff -U0`: the one replaced line is inside `read_rankings` (`payload["rows"] = served`); every
  other hunk is an addition. The new definitions are `CLASSIFICATIONS_TABLE`, `_classification_for_ticker`, `_join_classification`,
  `_model_line_names`, `_formula_words`, `_case_with_words`, `_team_case_absent_all`, `_team_cases`, and the module constant
  `_TEAM_CASE_NAMES`. That constant is not in limb 3's list; it is an addition read only by `_team_cases`. I admit it under this half.
- **The pdf (limb 5).** `render_pack.build_pack` does reach both changed functions (`_figures_table <- build_rich_text`,
  `_model_case_line <- _model_cases_markdown <- build_rich_text`), but only in the `.md` branch at `render_pack.py:350`, which runs
  only when a `thesis_bundle`, `peer_set` or `posture` is passed. The served `/print` route calls `build_pack(display_form, block)`
  (`scoped_amgt.py:4449`) with none of the three. The COO half's "build_pack calls neither" is imprecise, but its conclusion holds
  for the served route: the PDF bytes do not reach the changed code. Limb 5 still grades the output.
- **The DynamoDB statement.** `_classification_for_ticker` makes one call, `Table("etf-classifications").get_item(Key={"ticker": bare})`.
  Live `describe-table`: key schema `ticker` HASH only, ARN `arn:aws:dynamodb:us-east-1:313476888478:table/etf-classifications`
  (285 items). This equals the half's one `GetItem` statement. No other action is needed.
- **Writers.** The five writers in the half, (a) to (e), agree with the code read above. N = 5.

## 2. CONDITIONS
1. The Terraform diff adds exactly one `scoped_amgt_pool_prefixes` entry, `amgt/harvest/gold/research_dossier/`
   (`scoped-amgt-api.tf:118`), and exactly one statement, `dynamodb:GetItem` on the ARN above. The plan must show nothing else.
2. The artifact is built from a commit whose `lib/research` equals HEAD `48c1ea24c4` on the files listed above. A later commit to
   any of those files before the build needs a re-read by this seat.
3. `/timeline` (limb 6) and `/print` (limb 5) are captured before the apply and read byte-equal after it. Either one moving is a
   ROLLBACK, not a note.

## 3. ROLLBACK
As the COO half states: re-apply at the recorded prior artifact VersionId, and remove the prefix entry and the DynamoDB statement.
No data is deleted.

Signed: `1.0.0_SA_CTO~Z`, 2026-09-29.
