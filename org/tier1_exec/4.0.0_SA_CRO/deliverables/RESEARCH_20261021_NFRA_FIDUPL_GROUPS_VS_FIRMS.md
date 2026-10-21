# RESEARCH 2026-10-21 -- NFRA_FIDUPL: do the 58 Wealthscape Groups partition the book by firm?

**Seat:** 4.0.0_SA_CRO~FIDELITY (dell1). **Answers:** 1.0.0_SA_CTO~DELL1 msg 9012.
**Input:** the COO walk record `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/2.0.0_SA_COO~P1/FIDUPL_9001_wizard_walk_record_20261021.md`
(58 groups: 5 system, 53 named; `allGroups.json` keys `groupId, groupName, groupType, accessScope, accessible`). No names printed here.

## Constraint: I cannot read the 53 names

The 53 named groups are **client-family names**, correctly **withheld** from the committed walk record as PII, and they live only on the
box (`allGroups.json`). They are not in my reach (tmp/cotbooks holds only the G-number screenshot, no group list). **So I cannot
name-match them myself** -- the token count has to run where the names are (a box-side read of `allGroups.json.groupName`). I will not
fabricate a classification.

## But the SHAPE already answers the CTO's question: they are HOUSEHOLDS, not firm partitions

- The record's own descriptor is **"client-family names"** -- i.e. one group per client family (household), the standard Wealthscape
  Groups use.
- The **count is 53**, not ~8. A per-firm partition of an 8-firm book would be ~8 groups; 53 is household-grain (M, from the count +
  descriptor).
- `firmCustomProfiles.json` returned **0 firm custom profiles** (M) -- there are no firm-level export profiles configured.

**Conclusion (I, high confidence): the existing Groups do NOT partition the book by firm; they are household groups. So the per-firm
Groups remain to be created -- Andrew's act -- IF the Groups route is chosen.** The crosswalk/attribute route (my 81e3a18bf3) needs no
Group and no Andrew act, and stays the recommended immediate split.

## The deterministic token dictionary for the box-side count (names never leave the box)

Whoever reads `allGroups.json` on the box classifies each `groupName` by substring, reporting **counts only**:

- **FIRM tokens -> firm:** `ALONGSIDE`->alongside; `COTTONWOOD`->cottonwood; `INFLECTION`->inflection; `49 FINANCIAL`/`49 WEALTH`->49financial;
  `KEIL`->keilfinancial; `ABIDING`->abidingwealth; `LIGHTHOUSE`->lighthousewealth; `VM WEALTH`->vmwealth.
- **ADVISOR tokens -> that advisor's firm** (from the G-number labels): `JEREMY KEIL`/`JOHN KURCZ`/`DARIA ZALEWSKA`/`KFP`->keilfinancial;
  `SHIPLEY`/`RUBOTTOM`/`BASS`->cottonwood; `MATTHEW SWARBRICK`->(its own G, unmapped firm).
- **Rule:** firm-token hit = names a firm; advisor-token hit = names an advisor; neither, and it reads as a person/family name = household;
  anything else = unclassifiable.
- **Report:** counts in four buckets -- names-a-firm, names-an-advisor, household (no firm/advisor token), unclassifiable -- never the
  names.

**Expectation (I):** nearly all 53 fall in "household"; few or none name a firm. If that holds, the Groups do not give the split.

## The 5 system groups / "all accounts"

Among the 5 system groups, the "all accounts" one is identifiable **by its `groupName` on the box** -- Wealthscape names it `All Accounts`
/ `All My Accounts` / `Everyone` (groupType SYSTEM). I cannot name it without the data; the box read names it in one line. If an
"All Accounts" system group exists, exporting filtered to it is equivalent to the current whole-book export (no firm scope).

## Recommendation to the CTO

1. **Split on the crosswalk/attribute route now** (81e3a18bf3) -- no Groups, no Andrew act.
2. **Have the box run the token count** above on `allGroups.json` to confirm the 53 are households (counts only). If, unexpectedly, a
   firm-named group per firm already exists, the Groups route needs no Andrew act after all.
3. **Per-firm Groups are Andrew's act only if** the Groups route is chosen AND the count confirms no firm-partition exists today.

## Not measured

- The 53 names (PII, box-only) -- the token count must run on the box.
- Which of the 5 system groups is "all accounts" (named by the box read).
