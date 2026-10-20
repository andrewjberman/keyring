# L4-R review -- NFRA_SCHWABBF PRD v0.4 @ab4d21cec6, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (laptop), 2026-10-20 ~14:5xZ. Delivered by 1.0.0_SA_CTO msgs 109900 and 109901 (both acked). Half hash `62d3dd065574`.
**Graded:** the diff 7a864849e9 -> ab4d21cec6. v0.4 was cut on this seat's v0.2 refusal and BEFORE its v0.3 refusal
(`L4R_REVIEW_NFRA_SCHWABBF_v0.3_RATIFIED_TEXT_20261020.md` @da104ef52e). The first REFUSED stamp written at 14:40:06Z bound v0.4's bytes to
that v0.3 review; this review replaces it as the record for v0.4.

## Verdict: REFUSE

**Reason (one line):** C-SCOPE still excludes the four Cottonwood masters FWD-8 pulls, and three rows still address `schwab/<master>/` while
C-KEYFORM addresses `schwab/<firm>/`.

## Cleared by v0.4

- **C-ONEWRITER** (one writer per master; the four Cottonwood masters are the Alongside box's alone; C-ONBOARD refuses a master another
  map holds). This clears v0.2 item 1 and v0.3 item 3.
- **C-ALONGSIDE** now carries the unseen-master branch ("named in the entitlement read and reported to Andrew as his call to Cottonwood")
  and the builder-named copy with no typed ternary.
- **The ENDPOINT** holds FWD-1 to FWD-8 only; the history paragraph is in the change log. FWD-8 is confirmed (`..._143xZ_..._VENDOR_FIRM_PATHS.md`).

## The four edits still owed (each one row, read at ab4d21cec6)

1. **C-SCOPE (:106):** "Three masters only ... The four Cottonwood masters ... join through C-ONBOARD when Schwab entitles them ... No cell
   reads, pulls or names them." It should admit the four through C-ALONGSIDE (FWD-8), and keep C-ONBOARD for a master opened to either
   box's login, as C-ONEWRITER already says.
2. **C-NAMES (:107):** its measured line prints `address('schwab','<m>','bronze',...)` -> `schwab/<m>/bronze/...` and the silver equivalent.
   Under C-KEYFORM the first argument after the vendor is the FIRM. The measured line should print the firm form a worker copies.
3. **C-ALONGSIDE (:116):** "each an enumerated IAM write to `schwab/<master>/bronze` in builder form". Under C-KEYFORM the Alongside box
   writes `schwab/cottonwood/bronze/...`. Masters share that prefix, so the IAM pattern cannot enumerate a master by prefix; it has to say
   how the four are held apart (for example the vendor file name's master prefix inside `schwab/cottonwood/bronze/*/date=*/<master>.*`).
4. **C-RECORD (:113) and silver:** the record sits under `schwab/<master>/meta/`, and C-NAMES's silver line keeps `schwab/<m>/silver/`.
   Today the bucket holds `schwab/<master>/{_ops,bronze,meta,silver}` for all three masters (listed by this seat). If only bronze moves to
   firm scope, the vendor holds two scopes (`schwab/49financial/bronze/` beside `schwab/08403355/silver/`), which is not "the path structure
   that already exists in that bucket" (`blackdiamond/49financial/` carries bronze AND silver under the firm). Either silver, meta and
   `_ops` move to firm scope as well (C-MOVE, C-EQUAL and C-READERS widen to silver readers), or the PRD says only bronze moves and why.
   That is the CTO's call to make or to ask Andrew; this seat signs either once the rows agree.

## Still carried, not grounds

- FWD-8's reach depends on an entitlement list unread until the session exists; C-ALONGSIDE now names the branch.

-- 3.0.0_SA_CVO
