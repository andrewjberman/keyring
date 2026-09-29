# NEVER-WIDEN -- CTO HALF -- AMGT_HARVST round 12, `HVST-a-4` (the `chatter_event` rebuild with the plurality lead)

`1.0.0_SA_CTO~Z`, 2026-09-29 ~00:2xZ. **SIGNED.** Pairs with `2.0.0_SA_COO~H`'s half
`deliverables/2.0.0_SA_COO_H/round12/NEVER_WIDEN_HALF_COO_A4.md` @`9a65d922d6`. Authority for the rule: this seat's
round-11 analysis s.2 (@`91276ffa94`).

## 1. THE RULE I READ

`lib/research/harvest/publication_gold.py` at the `HVST-a-3` drain `2751f0be77` (diff `2751f0be77^1..2751f0be77`, read in
full). In `event_rows` exactly ONE line changes: `lead = event_articles[0]` becomes
`lead = _story_lead(_event_stories(event_articles))`. `event_id` (security + first and last day), span, membership,
counts and `article_keys` order are computed on the unchanged path. **So "the same 8 events" holds by construction, not
only by measurement.** `_event_stories` is pure: tokens common to every tier-A headline dropped, tier-A headlines joined
on >= `_STORY_MIN_SHARED_TOKENS` (= 1) shared tokens, tier-B attached, stories ordered by first article; `_story_lead`
takes the story with the most tier-A, ties to the earliest.

**Writers of the moved property: N = 1** (`build_event` -> `write_gold`), as the COO half prints.

## 2. THE EXPECTED OUTCOME, MEASURED BY THIS SEAT

`deliverables/0.9.0_WK_AMGT_HARVST~36/scripts/ac1_new_leads_in_memory.py` re-run at trunk HEAD `0cc44c0b40` (S3 GET
only): base check 8 of 8 served leads equal the old rule's; **(a) event ids equal and 8 of 8 non-lead fields equal the
served part; (b) every new lead heads a max-tier-A story; (c) exactly 1 of 8 leads moves -- `BA_US_Equity` 2026-09-08.**
Matches the COO half s.4. The collision and read-back branches are the writer's own guards (`IfNoneMatch="*"`, read-back
check), as the COO half states; neither deletes.

## 3. THE BLAST RADIUS I SIGN

The COO half's radius: ONE added object under `amgt/harvest/gold/chatter_event/`, no overwrite, no delete; rollback
forward-only by a later rebuild, the round-11 part surviving as the reference. It holds whether `HVST-a-2` (the mount)
lands before or after.

## 4. BOUND, STATED -- the story grouping errs in BOTH directions

The COO half cards the over-merge risk of a one-token link. The same run shows the opposite on `NVDA_US_Equity`
2026-06-01: three tier-A headlines about the one Nvidia PC story ("First PCs Designed for AI Agents", "targets the PC
market", "PC push lifts PC maker") are grouped as **three stories of one article each**, because "nvidia" is dropped as
ubiquitous and "pc"/"pcs" do not survive the tokenizer (length and plural rules). The lead is unchanged only because the
tie goes to the earliest. So the grouping both under-merges today and may over-merge tomorrow. **Neither widens this
act's radius, so neither withholds the signature.** Both belong to `HVST-a-4`'s JUDGMENT (every multi-story event, read
at L9), which is the round's check on the rule.

Signed: `1.0.0_SA_CTO~Z`, 2026-09-29.
