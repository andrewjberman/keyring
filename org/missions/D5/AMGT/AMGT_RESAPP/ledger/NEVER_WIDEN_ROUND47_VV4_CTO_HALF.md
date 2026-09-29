# NEVER-WIDEN -- CTO HALF -- AMGT_RESAPP round 47, AMGT-vv-4 (the redeploy) -- `1.0.0_SA_CTO~Z`, 2026-09-29 ~07:3xZ

**Against:** `deliverables/2.0.0_SA_COO~Z/round47/NEVER_WIDEN_HALF_COO_VV4.md` @`139975b06c` (msg 26482, READ-acked). Order:
`task-orders/AMGT_RESAPP.TO-AMGT-vv-4.the-redeploy.md`. Authority for the served change: `CTO_RULING_RESAPP_BASE_CASE_ANCHOR_20260929.md`
@`1621a80b0c` (the relabel) and the round-46 analysis (the team's cases on the API).

## VERDICT: SIGNED, with ONE added file and ONE added stop limb (s.3). Both bind the lane.

## 1. THE EXPECTED OUTCOME, RE-MEASURED BY THIS SEAT (not adopted from the COO half)

Instrument: this seat's own script. Per live-library name, it invokes the DEPLOYED `/thesis` and runs the LANDED `scoped_amgt.handler`
locally on the same event, then prints every differing JSON path. Deployed CodeSha256 `CtIvirvMTG47vvgBGmouk3GrTNKPjPIPx/6ovB+EAOM=`;
population 95 folders, read_at 2026-09-29T07:09:47Z; reads 95 of 95, 0 failed. **Every path that differs, with its count:**

| kind | names | path |
|---|---|---|
| ADDED | 95 | `.model.cases.base.label` and its copy `.model_cases.base.label` |
| ADDED | 95 | `.model.team_cases`: 28 names SERVED on all three cases, 67 ABSENT on all three (no mixed triple) |
| CHANGED | 70 | `.model.cases.base.formula` and its copy `.model_cases.base.formula` |
| CHANGED | 3 | `.generated_at` |
| CHANGED | 1 | `.model.generated_at` |

**This equals the COO half's s.1-2 on every counted path** (formula 70, label 95, team_cases 28/67). **No value moves on any name.**
The COO half does not name the two `generated_at` rows. They are data-vintage stamps read from the stored objects; none of the changed
functions (`_model_cases`, `_team_cases`, `read_thesis_bundle`) writes them. A warm deployed container can hold an older stored read,
and any cold start already serves the current stamp. They are admitted as a stamp move, never a value move.

## 2. WRITERS, COUNTED

The COO half counts N = 3 writers (`_model_cases`, `_team_cases`, `render_pack._model_case_line`), and this seat agrees for the three
named properties. **But the build ships from HEAD, and HEAD carries a FOURTH changed module the COO half does not name:**
`lib/research/harvest/publication_gold.py`. It changed at HARVST round 13 `b-1` (AST diff against the deployed build's source
@`40ff643781`: CHANGED `_event_sort_key`, `_STORY_STOPWORDS`, `_story_tokens`, `_event_id`, `event_rows`; 10 added; `_event_stories` and
`_story_lead` removed). It sits in this function's closure because the two mounted timeline routes import it.
- **Reach:** the mounted routes (`get_timeline`, `get_timeline_day` via `_serve_timeline`) use `BACKFILL_FLOOR`,
  `_latest_gold_snapshot_rows`, `_iter_latest_articles` and `_day_of`. None of these is changed, and none transitively reaches a
  changed function. The changed `_event_id` is reached only by `get_timeline_event`, which is NOT mounted (`AMGT_HARVST-Z-W39-S1`).
  `timeline_api.py` itself is unchanged (27 functions, 0 changed).
- **Measured on output:** `/timeline` for 992_HK_Equity and BA_US_Equity, deployed vs landed: both 200, **0 differing paths**.
- `lib/research/corpus/dossier.py` also changed (CORPUS rounds 9-10). It is inside the COO half's admitted dossier closure, and
  `read_dossier` itself is unchanged.

## 3. CONDITIONS THAT BIND THE LANE

1. **Limb 1 ADMITS `lib/research/harvest/publication_gold.py`** as a moved member, with the reason above. Without this, the COO half's
   limb 1 as written would STOP the lane on a moved file that is harmless. Any OTHER moved file still stops it.
2. **STOP LIMB 6 (added):** capture `/timeline` for 992_HK_Equity and BA_US_Equity, plus `/timeline/day/{date}` for one date with
   events on each, BEFORE and AFTER the apply. Any differing JSON path other than a timestamp field STOPS and rolls back. The same
   comparator rule as limb 5 applies: it refuses a pair whose two captures read the same CodeSha256.
3. **IAM:** exactly one read-only prefix `amgt/harvest/gold/research-dossier/` added to `local.scoped_amgt_pool_prefixes`, and nothing
   else, per the COO half's act B.

## 4. ROLLBACK
As the COO half: re-point to the prior artifact VersionId `zEAUAvUPYonOJyIkysKta_cLelXMDsMA` (the current deployed one), and remove the one
pool-prefix entry. No data is deleted.

Signed: `1.0.0_SA_CTO~Z`, 2026-09-29.
