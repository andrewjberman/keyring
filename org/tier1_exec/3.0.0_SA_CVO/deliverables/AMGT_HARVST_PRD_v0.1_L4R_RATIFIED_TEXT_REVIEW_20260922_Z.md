# L4-R review -- AMGT_HARVST PRD v0.1, ratified-text half (`3.0.0_SA_CVO~Z`)

**PRD:** `org/missions/D5/AMGT/AMGT_HARVST/prd/AMGT_HARVST_PRD.md` @`16db74edea`. **Half:** ratified-text, hash
`68e8ec7ac41d`, measured from the committed bytes. **Delivery:** `1.0.0_SA_CTO~Z` msgs 24272, 24273.
**Verdict: REFUSE.** Two defects against the counterpart PRD and the estate's own key rule, and two gaps. Each has a
bounded fix; none questions the design.

## What holds

- **ENDPOINT, FWD-1..FWD-8:** each is provable by an act a seat can take on demand, and none is a wait. Each names its
  brief section or Andrew's words.
- **Rule 30:** every address the contracts print is the builder's output. Ten calls to `lib/opal_naming.py address()`
  covered bronze `article` and `news_listing`, silver `article` and `listing_hit`, gold `article_security_mention`,
  `chatter_daily` and `chatter_event`, and bronze `article` for barrons, ft and bloomberg. **10 of 10 print the
  address as written, and none refuses.**
- **C-HV-BOUNDARY:** AMGT_RESAPP s.12 names stage 9 only as "the publications harvester (one run for Lenovo)", so
  having this project's harvester execute it contradicts no ratified text. **Note:** it reverses msg 24270 ("stays in
  AMGT_RESAPP as the trial's one pass on today's harvester") 4 minutes later. The Lenovo trial's stage 9 now depends
  on two HARVST contracts landing. AMGT_RESAPP's brief half should say so. That is the CRO's half, not this one.
- **C-HV-MENTION-GRADE's defaults:** the contract fixes the columns and the rule's SHAPE, and names the values as
  Andrew's to re-set. Accepted.

## Refusal items

### R1. C-HV-LINK-IS-GOLD and C-HV-AXIS-PROJECTION contradict AMGT_RESAPP's ratified `C-ONE-STORE`, which is not named

AMGT_RESAPP's C-ONE-STORE (ratified, signed at v0.21) fixes the read path. The chatter axis producer and the coverage
reader read the pool through ONE shared adapter:
- the association at `publication-links/v1/{security_key}/{publisher}/{digest}.json`;
- the body at `publications/v1/{publisher}/{digest}.json`.

This PRD moves the association into gold (`article_security_mention`, "which company an article is about ... lives in
gold, never in silver"). It then makes the axis ranks a projection of `chatter_daily`. It names only the supersession
of rk-85's silver WRITER, not C-ONE-STORE. **So two ratified texts would each state where the axis reads from, and
they differ.**

**Fix:** name C-ONE-STORE in C-HV-AXIS-PROJECTION and C-HV-LINK-IS-GOLD. State what replaces its association path and
its adapter, and when. State what happens to `publication-links/v1` and `publications/v1`: read-only until repointed,
then retired under C-FORMAT-SEQUENCE's meaning of "retire". The matching amendment to C-ONE-STORE is owed in
AMGT_RESAPP's CONTRACTS, in the same bump or before this one is admitted.

### R2. `article_hash = sha256("<publisher>:<article_id>")` does not say which publisher token, and the obvious reading is wrong for two of five

The estate already fixes this. `lib/opal_data_harvest/harvest_grammar.py` @`c452d99d98` `article_hash(publisher_code,
article_id)` uses the PUBLISHER CODE. `SOURCE_FOR_PUBLISHER` maps the code to the path source:

| code | source |
|---|---|
| sa | seeking-alpha |
| bbg | bloomberg |
| barrons | barrons |
| wsj | wsj |
| ft | ft |

The live object's hash equals `sha256("sa:4635742")`, not `"seeking-alpha:..."` (the module's own ruling and test).

The contract writes `{source}` in the path and `<publisher>` in the hash, and the example uses a source name. A writer
reading it would hash `seeking-alpha:<id>` and `bloomberg:<id>`. Every held SA and Bloomberg article would then
re-fetch under a new hash, which breaks FWD-3 ("fetches no article we already hold") and FWD-8 ("none duplicated").

**Fix:** state that the hash takes the publisher CODE, and point at `harvest_grammar.py` @`c452d99d98` as the one
implementation. That is Build Ladder rung 2: the estate already has it.

### R3. The tier rule has an unassigned case, and it is the one Andrew named

A: title and lead. B: lead, or density >= 0.3. C: 2+ mentions elsewhere. D: one passing mention.

**A mention in the TITLE but not in the lead** matches no tier by rule. With one mention, and density below 0.3, it
falls to D, "one passing mention". Andrew's own test is *"is it mentioned in headline?"*, so a headline mention graded
"passing" inverts his criterion.

**Fix:** write the rule as a partition over (title, lead, count, density), with every combination assigned. Title-only
belongs in A or B; the values stay his. Also state that the tiers are evaluated in order A -> D and the first match
wins.

### R4. Silver does not say which date partitions it, or that AMGT_RESAPP's `C-SILVER-PARQUET` binds

C-SILVER-PARQUET, in the counterpart PRD, fixes silver partitioned `date=` by FETCH date, and requires `bronze_key`,
`fetched_at` and `record_hash` on every row. This PRD's silver carries three clocks, writes `date=<d>` without saying
which clock, and names no lineage columns. It says C-BRONZE-AS-RECEIVED binds unchanged, but says nothing about
C-SILVER-PARQUET.

**Fix:** either "C-SILVER-PARQUET binds unchanged: `date=` is the fetch date; the lineage columns are carried", or a
stated departure, with the reason.

## Not refusal items (for the same bump if convenient)

- **C-HV-DAILY-DENSE:** "an empty day is a zero row" needs a START day per security (first article held? coverage
  start?). Without one, "dense" has no lower bound.
- **C-DEDUPE-BY-KEY:** this binds from the counterpart PRD. Name each channel's FETCH key: `news_listing` by date and
  query, `article` by `article_hash`.

-- `3.0.0_SA_CVO~Z`
