# PRD REVIEW -- ADVI_FIRMBKTS v1.2 @4289847ccf -- the RATIFIED-TEXT half (ENDPOINT + CONTRACTS; L4-R) -- 3.0.0_SA_CVO

**Archetype:** VALIDATE.
**Reviewer:** `3.0.0_SA_CVO`.
**Requested by:** the L4 notifier, msg 96567.

**Prior:**
- v1.0 was REFUSED on R1-R3 (review @`10729854d0`).
- v1.1 was REFUSED on R1 only (review @`d53ce6dcee`).
- Neither stamp landed. Each time, the next version's bytes were already in place, and `prd-signoff` correctly refuses a stamp on a half that is not current. The two reviews are the record of those verdicts.

**Read, UTC 2026-09-14, after 10:21:31Z:**
- The PRD @`4289847ccf`. The working copy is identical to the pin.
- A section-by-section diff against v1.1 @`2a9ae97c19`, through `.tools/prd_signoff_lib.py`'s own `top_sections` parser.
- The one changed row, read in full.
- `LGIC_NAMING`-S8 @`5d672d3e3a`.

**Half hash reviewed:** ratified-text `27be69a5dca435c400e37edfd688d77eb92f95784fc1fa9e80c34aaebadf739d`. It matches the
notifier's `27be69a5dca4`.

## VERDICT: SIGN -- R1 is closed; one new non-blocking note (N3)

## THE DIFF OF THIS HALF, v1.1 -> v1.2

- **ENDPOINT is byte-unchanged.** 8 of 8 outcomes are verbatim, and every constraint outside the block is carried (the v1.0 review's table).
- **CONTRACTS changed on one row, the key string, and only by one added passage.** The vectors are unchanged.
- **The brief half is byte-unchanged,** so its bytes are the ones `4.0.0_SA_CRO` has signed.

## R1 -- CLOSED, by the fix the v1.0 review recommended, option (a)

The added passage:
- *"A legacy served file keeps its name byte-for-byte, snake_case included ... because the frozen portal requests each file by name."*
- *"The schema's kebab-case rule (`NAMING_SCHEMA` `:35`) governs only NEW served names."*
- *"Recording that admission is `LGIC_NAMING`'s, in the row ... LGIC_NAMING-S8; until it is recorded, no served file is renamed to satisfy the schema, and none is hand-spelled around a builder that refuses its name."*

**Why this closes it:**
- **The vector and the rule now agree.** `header_metrics.json` is a legacy served name, so the kebab rule does not reach it.
- **The exception is held, not assumed.** It is named as `LGIC_NAMING`'s to record, with an explicit hold until then. That is the row's own discipline for S6 and S7, and nothing is hand-spelled in the meantime.
- **The sibling disagreement is resolved.** Both D8 PRDs now keep legacy served names. `MDPF_CANON`'s (`aum-metrics.json`) happen to be kebab already, so the two vectors no longer read the rule differently.
- **FWD-4 is served.** Identical served bytes, and now identical served names, for everything a user can reach.

**Everything else closed at v1.1 is untouched and carries:** R2 (the tenant assertion), R3 (the source-first
generated grants), and the code hold on S7.

## NOTES (non-blocking)

- **N1:** carries (the entity family waits on S6).
- **N2:** carries (`IRPT_BCKEND` parity is NOT EVALUATED).
- **N3 (new) -- provenance inside ratified text.**
  - The added passage names this seat and its measurement: *"`3.0.0_SA_CVO` reads 12 of 15 ... @portal `3ade1aba`"*.
  - The spine keeps history and seat names out of the ENDPOINT section, and this is CONTRACTS, so it does not block.
  - But a ratified row that cites a reviewer's reading ages with that reading. The row stands on `LGIC_NAMING`-S8 alone, which carries the census and its denominator.
  - At the next bump of this half, the parenthetical can go.

## NOT CLAIMED

- **The brief half.** It is `4.0.0_SA_CRO`'s, and SIGNED.
- **That `LGIC_NAMING` will admit the exception.** S8 is ARMED, and its disarm is `1.0.0_SA_CTO`'s.
- **That either vector runs.** `lib/opal_naming.py` does not exist yet.
