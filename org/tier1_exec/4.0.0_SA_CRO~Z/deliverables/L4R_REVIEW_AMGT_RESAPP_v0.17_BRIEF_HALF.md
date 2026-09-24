# L4-R REVIEW -- AMGT_RESAPP PRD v0.17, BRIEF HALF -- verdict: SIGN

**Reviewer:** `4.0.0_SA_CRO~Z`. **PRD:** `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` @`6f39881c3c`,
v0.17, brief half hash `55a95855d29c` (msg 24089). **Brief:** @`19ce7d5b4d`, unchanged. **Prior signature:** v0.16,
`85c4ec503a`.

## Scope

One commit since v0.16 (`2d0da569e7..6f39881c3c`). Brief-half hunks: the v0.17 change note (`:204-218`) and section 11's
"Landed" and "Closed" paragraphs and its open items. The `C-HARVEST-HOME`, `C-LUSHA-EXCEPTION` and `C-FORMAT-SEQUENCE`
hunks sit under `## CONTRACTS` and are `3.0.0_SA_CVO~Z`'s to grade. **No BRIEF COVERAGE entry and no brief pin moved.**

## Section 11's claims against this seat's own measurements

| claim | this seat's measurement | result |
|---|---|---|
| GENERAL tenancy (every tier home:scope) and the five vendor rows are on SITEZ | measured at HEAD `55c24a8b8a` (msg 24079): GENERAL all six cells `scope`; `barrons`, `wsj`, `ft`, `filings-xbrl`, `issuer-site` present | agrees (section 11 cites the later `39731fbda7`) |
| two `harvest` rows; `lookup()` takes the PRODUCT one; bronze/silver print `opal-data-assets`, platinum `opal-data-portal-v2` | same, measured | agrees |
| deleting that one row puts every tier in `opal-data-harvest`, validate 0 refusals, controls unmoved | this seat's scratch-registry run (msg 24079) | agrees, and it is correctly attributed |
| 1,461 objects in `opal-data-harvest`, 0 AMGT objects in the vetoed buckets | this seat's 17:1xZ census gave 1,461 objects and 0 under five `opal-data-assets` prefixes; `2.0.0_SA_COO~Z`'s 21:19Z census is a separate instrument | agrees |
| Lusha closed on Andrew's word | `ANDREW_DIRECT_20260921_195xZ_...` (msg 24041), verbatim "Yes on Exception" | faithful |

## Notes, none a ground for refusal

1. **Section 11, open items:** row Z-S203's remedy has two parts, the row deletion AND a duplicate-key refusal in
   `validate()` (the reason the duplicate read green). Only the deletion is listed. Recommend adding the validator
   refusal at the next bump.
2. **Section 11, the "simulated tenancy" sentence** ("Each prints `opal-data-harvest` only under the simulated
   tenancy") has been overtaken: the tenancy has landed, and the remaining condition is the duplicate row, as the next
   paragraph says. It is true of the plan's run, but it now reads as a current condition. Cosmetic.
3. **For `3.0.0_SA_CVO~Z`'s half, flagged because the brief cites the plan as specification:**
   - `C-FORMAT-SEQUENCE` says the DERIVED `filings/v1` records move to silver. The plan puts the filing SECTIONS
     (`.source.json`'s parse) in silver and the filing ANALYSIS (`.analysis.json`, Claude's reading) in GOLD (plan
     s.5.9; R10 "never what Opal cares about"). If the contract means `.source.json` only, it agrees; if it covers
     `.analysis.json`, it overrides the plan and contradicts R10. Worth one word.
   - `C-LUSHA-EXCEPTION` keeps a "profile link" while dropping "any other channel for reaching a person". Whether a
     personal profile URL is such a channel is not stated. Worth one word, since the exception exists to minimise
     personal data.
