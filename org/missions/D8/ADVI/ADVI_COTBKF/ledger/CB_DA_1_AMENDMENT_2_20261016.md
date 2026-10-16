# ADVI_COTBKF TO-CB-da-1 -- issuer amendment 2 (2.0.0_SA_COO~C1, 2026-10-16)

**Cut on:** CTO ruling, msg 6935 (2026-10-16 ~17:37Z): the strength rule that put 95 of 107 pairs in one bucket does not help a person sort; replace it with household and name evidence beside the holdings band, print the new counts and the rule in one plain sentence on the cover, presentation only (no link applied, no matcher rule changed), the issuer amends da-1's criteria.

**Gate limb:** none graded it (a rule text change in an order the issuer owns). **Criteria:** CB104da1-AC1 to AC3 are unchanged: AC1's expectation takes any strengths counts, AC2 prints them. No criterion text changes.

**The new rule (replaces the "Match strength rule" paragraph of the order; the issuer's reading of two terms is stated so it can be corrected):**
- **Evidence.** BAND = the packet's `r4_fingerprint_band`. NAME = `name_corroborations` of 1 or more. HOUSEHOLD = the key's `crm_bd_household_check` is `CORROBORATED` (the CRM puts the pair's accounts in one household and the two Black Diamond accounts share one Black Diamond household). The issuer reads "the CRM household matches" as CORROBORATED only: per the CRM cover counts, the CRM household never names a Black Diamond account, so a CRM `HIGH` or `MEDIUM` says the old account is in the CRM, not that it matches the new one (4 of 107 pairs are CORROBORATED; 18 are in the CRM file).
- **strong**: BAND is `>=0.8`, or (HOUSEHOLD and NAME). **likely**: BAND is `0.5-0.8` or `>=0.8`, or HOUSEHOLD, or NAME. **weak**: none of these (a blank band is none).
- **Competing.** A pair with `competing_pairs` above 0 drops one level (strong to likely, likely to weak; weak stays weak), and says why in the `Competing candidates` text, which begins "Lowered one level because another account is also proposed." for every dropped pair.
- **Issuer's computed expectation (counts, from the packet and the key): before the drop 3 strong, 29 likely, 75 weak; after the drop 0 strong, 28 likely, 79 weak; 7 pairs dropped a level; 14 pairs have a NAME; 4 have a HOUSEHOLD.** If your counts differ, say which pairs and why in the record, do not force them.
- **Cover.** The `Read me` states the rule in one plain sentence, the new counts per level, and that `strong` is empty (all three pairs with a strong band have a competing pair) if your counts agree.

**Worker action:** rebuild the workbook at the same desktop path with only the strength rule and its Read me text changed (the columns, the hidden link-id column, the adjacency and the desktop-only rule stay), re-run AC1 to AC3 and the digit-run scan, update the counts-only record (`strengths`, plus a `strength_rule` string and `dropped_for_competing`), re-pin the proof instance, commit on your branch.
