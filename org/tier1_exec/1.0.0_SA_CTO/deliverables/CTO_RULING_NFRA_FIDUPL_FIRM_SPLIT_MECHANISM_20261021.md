# CTO RULING -- NFRA_FIDUPL: the firm-split mechanism (the G number is not account membership)

**Ruler:** `1.0.0_SA_CTO~DELL1`, 2026-10-21 ~05:5xZ, under `/self-drive` Step 1 (design fork: CRO research, then the driver rules).

## What was measured (the box, 2026-10-21, records under `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/`)
- `accountList.json` answers `available=5204` under every one of the 31 G numbers (step 2Pv2); the endpoint has no pager (the UI says
  "too many results, narrow your search" above 2000; three hand HARs agree).
- The Export Status list carries the SAME six file ids under ordinals 0, 1 and 15, and `account.txt` is byte-identical under all three
  (3,794,367 B, 5009 rows, sha8 94a0f611, equal to the landed 20261019 file) (step 2Gv2).
- `account.txt` is 5009 x 141 with no column near 31 or 8 distinct values (P1 record @6077b873db7).

## What the CRO read (no sign-in; `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261021_NFRA_FIDUPL_HOW_WEALTHSCAPE_SCOPES_PER_FIRM.md` @81e3a18bf3)
The G number is carried only on `cst/view?gNumber` (alerts) and `getDocumentsSearchResult?gnumber` (statements): a reporting and
service-desk context, not an account grouping. The per-firm scope Wealthscape does offer is account GROUPS (entitlements `Create a
Group`, `Group Access Layer`, `Export Groups`; the Custom export wizard's step 3 "Choose Filter"); the group-filtered export's calls
are uncaptured. `accountList.json` rows carry per-account fields (`regRep`, `affiliateInfo`, `fbsiShortName`, `mslaCode`) that may
encode the firm.

## Ruling
1. **The premise of "split by G" is refuted by measurement.** The daily pull is rep-level; the G switch is a view. The PRD's per-G
   language (v0.5, Andrew-direct 2026-10-20 ~20:5xZ) is read as "every firm's accounts under every G attached to the switcher",
   which the rep-level book already covers; the SPLIT needs a membership source the G does not provide. This is an L10 finding for
   the round-3 analysis and a PRD addendum; it changes no cell mid-round.
2. **The split key is custodian-native, measured before chosen:** on the next sign-in (the read-only wizard walk) the box reads the
   per-account fields over the full 2000-row page, distinct counts per field, masked. A field that partitions the book near the 8
   firms is the key. Andrew's COTBOOKS word (record @7fb4f70e80: no Black Diamond dependency for a critical function) binds here:
   the Orion/BD crosswalk (1,418 attributed, 0 conflicts) is the COMPARISON, never the key.
3. **Unattributed accounts land under `alongside/` named as unattributed** (PRD FWD-9) until a native key or Groups exist. Nothing is
   dropped and nothing is guessed.
4. **Account Groups are the durable, full-coverage path.** The wizard walk captures step 3 and any Group option, read-only. Creating
   Groups in Wealthscape is a configuration act under Andrew's name that no word of his names (CLAUDE.md: a vendor use no word of his
   names is his): it is LISTED FOR ANDREW as an act (create one Group per firm, or say the word for a seat to create them from the
   measured membership), with this record as the citation. No seat creates a Group before that word.
5. The backfill (deliverable 2) proceeds at the rep level now; its per-firm split follows the daily's mechanism.

-- 1.0.0_SA_CTO~DELL1
