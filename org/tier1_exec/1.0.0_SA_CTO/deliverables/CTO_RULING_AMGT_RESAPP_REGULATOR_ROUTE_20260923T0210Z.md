# CTO RULING -- the filings battery gains a REGULATOR route, and HKEX is its first instance

**2026-09-23 ~02:1xZ, `1.0.0_SA_CTO~Z`.** The scope call I named as mine in the round-33 analysis (@`6c2ec34633`)
and said I would take next. Authority: Andrew's AMGT adjudication word (@`c5f33fe8a3`); this is a contract question
on `AMGT_RESAPP`'s filings battery, which msg 24257 scoped issuer-site-only -- **my ruling to change.**

## THE BLOCKER, and what it blocks

`rk-118` ran correctly and established a **trial finding**: Bloomberg CIK **932477** resolves to the EDGAR entity
**"LENOVO GROUP LTD"** -- **and no 10-K exists**, because Lenovo is HK-listed and files with **HKEX**, which msg
24257 excludes. Measured tonight: `filings/v1/992_HK_Equity/` holds **one object, `UNRESOLVED-SOURCE.json`**;
`issuer-site/harvest/bronze/document/` is **0 estate-wide**.

**It blocks three things at once:** Lenovo's filings source; `rk-127`'s first HELD marker (nothing produces one
until the battery re-runs); and **the Thesis tab -- the page's DEFAULT tab** for the trial's only security.

## RULING: THE BATTERY GAINS A **REGULATOR** ROUTE. HKEX IS ITS FIRST INSTANCE, NOT A SPECIAL CASE.

**The ground is Andrew's own universe word, not Lenovo's convenience.** He set the universe as **IEFA -- global** --
and said *"we should be foreign-friendly non-US from the start with that in mind."* ⛔ **A filings battery whose
only regulator is EDGAR cannot serve a non-US universe**, and Lenovo is **the first name to expose that, not an
exception to it.** Building the route for one name would be scope creep; building it because the universe is global
is the PRD's own premise catching up with itself.

**Measured at the bytes before ruling:** the battery today has `_sec_ticker_table` and `_edgar_annual_filing`
(`battery.py:597`, `:639`) and `sec_filing` (`fetch.py:242`) -- **EDGAR and the issuer site. There is no regulator
abstraction at all**, so this is a new route rather than a new entry in an existing table.

## ⛔ MECHANISM: A REGISTRY ROW, NEVER A HAND-TYPED ADDRESS (Rule 30)

**Measured: `infra/logic/registry/` carries SIX files and ZERO of them mention `hkex` or `regulator`.** So the
first act is **a registry row**, and the builder's refusal is that row's absence -- **exactly the case Rule 30
names: *"a builder REFUSAL is a missing registry row to add, never a hand-typed workaround."*** ⚠ **A cell that
hand-types an HKEX address is refused at the cut**, whatever it otherwise achieves.

## SCOPE -- deliberately narrow, and the three limits are the ruling

1. **ONE regulator route, generalised**, not an HKEX special case: the battery gains a REGULATOR step whose
   implementation for HKEX is its first instance. **A second regulator is a registry row, not a code change.**
2. **The route is ADDITIVE and ordered LAST.** EDGAR and issuer-site are unchanged and keep their precedence, so
   **no name that resolves today can resolve differently tomorrow.** ⚠ A change to any existing route's behaviour
   is a rollback trigger, not a bonus.
3. **`filing_attempt` stays write-once and overwrite-refusing.** Lenovo's existing `UNRESOLVED-SOURCE` record is
   **not overwritten** -- a resolved outcome supersedes it under the newest-wins rule, and the stale served reason
   corrects through `rk-127`'s held-marker, which is what that mechanism was built for. ⭐ **The two blocked things
   unblock each other once this lands.**

## WHAT THIS DOES NOT DO

**No vendor word is needed** -- HKEX filings are public, like EDGAR. **No Bloomberg call, no Lusha, no SERP, no
model call.** It does not touch the universe, the crosswalk, the model block or any served numeric surface. ⚠ **And
it does not promise Lenovo a Thesis:** it makes the SOURCE reachable. Whether a drafting document follows is the
drafting stage's, and `C-CITED-OR-ABSENT` still governs -- **a fixture-produced thesis remains refused at any
price.**

## WHY NOW, AND WHY IT MATTERS BEYOND LENOVO

⭐ **The round-33 analysis found that this project had run out of work it could finish alone** -- two half-fixes in
three rounds, both blocked outside the boundary, and round 34 correctly issued **zero orders**. ⛔ **This route is
real, in-boundary, server-side work that is blocked by nothing but this ruling.** It gives round 35 something to
cut that is neither padding nor waiting on Andrew.

**And it is the trial's own purpose:** Andrew's word was *"run Lenovo through the entire pipeline ... every single
thing for Lenovo."* **A component that can never resolve for the only security in the trial is not a trial of that
component.**

## ACTS

- This record, committed and broadcast to `2.0.0_SA_COO~Z`, `3.0.0_SA_CVO~Z`, `0.0.0_AB_MSTR~Z`.
- **A PRD amendment carries the route into `C-`-space with the registry-row requirement stated**, landing with the
  next amendment alongside the Lenovo/EDGAR correction already owed -- **not mid-round.**
- `2.0.0_SA_COO~Z` may cut it in round 35. **The registry row comes first and its absence is the cell's own AC0.**

-- `1.0.0_SA_CTO~Z`

---

## ⛔ CORRECTION, 2026-09-23 ~04:3xZ, BY THE SEAT THAT ISSUED THIS RULING -- ACT 2 IS VOID AS UNNECESSARY

**Read this before executing anything above.** The ruling's SUBSTANCE stands. **One of its three ACTS does
not, and the error is instructive enough to state rather than quietly drop.**

**What is void:** *"A PRD amendment carries the route into `C-`-space with the registry-row requirement
stated."* **There is nothing to carry.** `C-FILINGS-ANALYZER` has read, since Andrew ratified the
international battery on 2026-09-18
(`ANDREW_DIRECT_20260918_194xZ_AMGT_RESAPP_SIX_CARDS_ANSWERED.md@4de34f0d95`):

> **"(5) the national regulator, one adapter per jurisdiction, built only for a name that step 4 fails."**

Printed at its bytes: `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md:782-784` @`8cef65cc00`,
inside the `## CONTRACTS` section (lines 624-995) -- **the ratified-text half.**

⛔ **THE ERROR IS A GRAIN ERROR AND IT PASSED EVERY CHECK I RAN.** The ruling's own evidence line is sound
and I would run it again: `battery.py:597`, `:639` and `fetch.py:242` **do** hold only EDGAR and the
issuer site, and there **is** no regulator abstraction in the code. ⭐ **Every one of those reads was
correct. I measured the CODE and wrote a sentence about the CONTRACT** -- two objects, two owners, two
vintages -- **and because the measurement was real, the conclusion arrived looking measured.** Rule 22's
GRAIN axis, in the exact shape the night kept producing: an instrument answering the question adjacent to
the one asked.

⚠ **AND THE CHEAP CHECK EXISTED THE WHOLE TIME.** One read of the contract the ruling was amending would
have caught it. I read the code because the code was the thing that was broken; **the question was whether
AUTHORITY existed, and code cannot answer that question in either direction.**

**What this CHANGES, all of it in the project's favour:**
- the true state is **RATIFIED AND UNBUILT** -- a CELL, not a scope change;
- **no ratified-text re-signature is owed** (measured: the half hash is byte-identical across the v0.24
  amendment, `8d23896506...`), so `3.0.0_SA_CVO~Z` is not re-opened;
- **round 35 needs no new authority from Andrew and no sign-off round trip to cut the regulator cell.**

**What STANDS, unchanged:** the ground (Andrew's IEFA/global universe word, not Lenovo's convenience); one
generalised route with HKEX as its first instance; ADDITIVE and ordered LAST with EDGAR/issuer-site
precedence untouched; `filing_attempt` write-once and overwrite-refusing; and **Rule 30's registry row as
the cell's own AC0** -- which binds as LAW and is deliberately NOT restated as a contract, since a PRD
repeating it would create a second carrier of one obligation.

**A second correction rides with it,** recorded in full at PRD s.12a: the PRD's `(not an SEC filer)` was
**FALSE**. Measured at `data.sec.gov` (CIK 0000932477, HTTP 200): **LENOVO GROUP LTD, 63 filings
all-time, 0 of 10-K/20-F/40-F/6-K, and six `ARS` paper placeholders whose newest is 2007.** The entity
RESOLVES at step (2) and fails acceptance test **(b) CURRENT**. ⛔ **This ruling repeated "no 10-K exists"
from `rk-118`'s trial finding without exercising it** -- true as far as it went, and it licensed a
downstream sentence that was not.

-- `1.0.0_SA_CTO~Z`, correcting itself.
