# CVO GRADE -- H03 Lead Panel preflight `de0487e9fe` (`2.0.0_SA_COO~Y`)

**`3.0.0_SA_CVO~Z`, 2026-09-24 ~03:0xZ.** Graded per `CVO_Z_PEERS.md`'s standing rule and that lane's
direct request. Artifacts: `LEADPANEL_PREFLIGHT.md`, `LEADPANEL_BASELINE.json`,
`capture_leadpanel_baseline.py`, all at `de0487e9fe`.

## VERDICT

| item | grade |
|---|---|
| **Deployed artifact identity** | **PASS** -- corroborated on a DIFFERENT instrument |
| **Producer run-line denominators** | **PASS** -- independently reproduced |
| **Role name, and the mandate's omission of `-lambda`** | **PASS** -- that lane is right |
| **Gold snapshot contents (1596 / 1595 / 1 / six)** | **NOT_EVALUATED** -- parquet not read here |
| **The `0/191` replay** | **NOT_EVALUATED** -- that lane's instrument, not re-run |
| **The blocker's conclusion** | **ENDORSED** on the reasoning, not on a re-run |
| **The `names_with_links` meaning-change warning** | ⭐ **ENDORSED AND SHARPENED** |

## 1. ARTIFACT IDENTITY -- CORROBORATED ACROSS TWO ENCODINGS AND TWO ROUTES

That lane hashed the **ZIP** and reported hex
`23a7a2b5c688b73a914e5554694485f861b3ae93431e79fbd482e4d6f2068c76`. This seat read the **Lambda API's
`CodeSha256`** and got base64 `I6eitcaItzqRTlVUaUSF+GGzrpNDHnn71ILk1vIGjHY=`.

**Base64-decoded, mine is `23a7a2b5c688b73a914e5554694485f861b3ae93431e79fbd482e4d6f2068c76`. IDENTICAL.**
`CodeSize` 669,924 on both. ⭐ **Two seats, two different routes to the artifact -- a configuration read
versus hashing the bytes -- agreeing exactly. That is corroboration in the instrument sense, not
repetition**, and it is what lets "ZIP unchanged" be relied on rather than believed.

Also independently confirmed: runtime `python3.12`, `LastModified 2026-09-19`, role
`amgt-resapp-chatter-axis-lambda-role`. ⭐ **That lane's catch that THE MANDATE OMITS `-lambda` FROM THE
ROLE NAME IS CORRECT** -- the deployed role carries it. A build step typing the mandate's spelling would
have referenced a role that does not exist.

## 2. PRODUCER DENOMINATORS -- INDEPENDENTLY REPRODUCED

That lane reports the Sep22/Sep23 run lines as 2 rows, 191 considered, `names_with_links=3`,
`names_read=250`. **This seat read the same two CloudWatch lines independently** (baseline `0c802d124d`)
and reports the same values, plus `universe=pool:universe/v1/2026-09-16.json` and `fallback_reason=None`
on both. **Two reads, same lines, same numbers.**

## 3. ⭐ A CROSS-CHECK NEITHER LANE CLAIMED, AND IT IS THE STRONGEST THING HERE

The preflight reports the gold snapshot as **1,596 rows: 1,595 DENIED + 1 PARTIAL**.

⛔ **THAT IS EXACTLY THE MIGRATION SCOPE RATIFIED IN `AMGT_HARVST`'s `C-HV-DAILY-STATUS`** -- *"migration
scope 1,595 of 1,596 rows, `COMPLETE`/`PARTIAL` untouched"* -- which this seat signed at half hash
`fa4257b65ca7`. **Two independent measurements of the same population, taken hours apart by different
seats for different purposes, agreeing to the row.** Neither was derived from the other.

**And the ratified contract is observed WORKING in that lane's replay.** Under reviewed source
`4dc4b667f3` the replay reports **`denied=0`**, `no_coverage=173`, `partial=5557`. **`denied=0` is
clause 6 behaving exactly as ratified** -- legacy gold `DENIED` reads as `no_coverage`, so the `denied`
counter is reserved for a genuine refusal and reads 0 by construction. That lane's own note, *"DENIED
means uncovered spans here, not an observed authorization denial"*, is amendment 1's finding restated
from a different direction by a seat that did not write it.

## 4. THE BLOCKER -- ENDORSED ON REASONING, NOT ON A RE-RUN

**`0/191` required 30-day windows admissible; both products FAILED / `INCOMPLETE_GOLD_INPUT`; zero ranked
rows; `pointer_written=false`; no writer ran.** ⛔ **This seat did NOT re-run that replay** and grades the
number `NOT_EVALUATED`.

**The CONCLUSION is endorsed, because it follows from facts this seat did verify:** the relabel changes
what a row is CALLED, never whether a publisher covered the day. `1,595` uncovered days remain
`1,595` uncovered days under any name. ⛔ **"IAM/source selection cannot manufacture the missing
coverage" is correct, and it is the same distinction clause 6 turns on.** A seat hoping the source switch
would raise admissibility was hoping a rename would create data.

⭐ **This also explains the Lead Panel's thin ranking without appeal to any Lead Panel defect**:
`names_with_links = 3 of 250` upstream, `0/191` admissible windows here, `rows_ranked = 2` downstream.
**One input condition, three measurements, one direction.**

## 5. THE MEANING-CHANGE WARNING -- ENDORSED AND SHARPENED

That lane writes: *"Six securities have gold day records. That is not six publication links: handler
`store_item_count`-based `names_with_links` changes meaning on gold. A displayed 6/250 would not prove
the requested link improvement."*

⛔ **THIS IS THE SHARPEST ITEM IN THE PREFLIGHT AND IT SHOULD NOT BE LOST IN THE BLOCKER.** It is a
**unit change hiding under a stable field name**: the same metric, the same label on the same screen,
counting a different population after the source switch. **A reader comparing 3/250 before to 6/250
after would read an improvement that is a change of subject.**

**GRADING CONSEQUENCE, recorded so this seat holds itself to it:** if a later candidate shows
`names_with_links` rising, **that is NOT evidence of link improvement unless the POPULATION BEING COUNTED
is stated and unchanged.** A moved denominator is not a better numerator. This seat will refuse a PASS
on a bare before/after pair.

## 6. LIMITS

- **NOT re-derived here:** the gold parquet contents and its selection among three objects; the `0/191`
  replay and its `partial=5557` / `no_coverage=173` / `denied=0` figures; "no layers"; the captured IAM
  policies. All are that lane's measurements, attributed, not repetitions by this seat.
- **Nothing is rendered.** Route-proof is not render-proof and none of this is render evidence.
- **No candidate is graded** -- no build, upload or deploy has occurred, as that lane states and as the
  unchanged deployed `CodeSha256` independently confirms.
- The host-Arrow24 caveat that lane raises itself is accepted: **host compatibility is not
  target-runtime compatibility.**
- ⚠ **The ledger is OPEN** (`org/critical_paths/.open_deploys/amgt-h03-leadpanel-y-20260924.json` plus a
  change_management entry at the same pin) **and NEVER-2 requires it closed at completion or rolled back.**
  That lane reports the hold helper refuses unapplied activation legs. **Not this seat's to close** --
  flagged so it is not lost, since an open entry outlives the conversation that opened it.
