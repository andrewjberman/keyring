# L4-R ratified-text half -- RE-SIGN on the fix lines: DSGN_AMGTV1 v0.10, AMGT_HARVST v0.15, AMGT_RESAPP v0.34 -- SIGN x3

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~19:1xZ
**Deliveries:** `1.0.0_SA_CTO~Z` msgs 28675, 28676 and 28677 at `642f65df23`, plus 28678. The half hashes, recomputed by this seat,
equal each delivery: DSGN `cdb87b04f0a6`, HARVST `6275438cc62e` and RESAPP `0cedf61708ab`.
**Prior review:** `L4R_RATIFIED_TEXT_REVIEW_20261002_DSGN_v0.9_HARVST_v0.14_RESAPP_v0.33_Z.md` @`afd31a71b8`.
**Method:** the ratified-text sections at `82d1cb21e2`, diffed against `642f65df23` (`prd_signoff_lib` section cut).

| PRD | ratified diff | what moved | verdict |
|---|---|---|---|
| DSGN v0.10 | +9 / -7, FWD-21 only | The no-tone case: "a name whose served tone is null (no voters) is filled apart from the ramp's neutral centre and reads 'no clear tone' on hover". The ACCEPT: "says which names were collected most in the window, switches 30D to 90D and says what changed". SOURCE gains N7, N8 and N10. Both refusal defects are closed, and FWD-21 now agrees with HARVST FWD-17. | **SIGN** |
| HARVST v0.15 | +4 / -3, FWD-17 only | The window ends at the last trading day (T-1, `lib/trading_calendar.py`), matching RESAPP FWD-36. A voter is a non-neutral label, with no threshold added: Andrew's 09-16 rule as given. | **SIGN** |
| RESAPP v0.34 | +7 / -1, FWD-37 only | The earnings path is a QUALIFIED WAIT on Andrew's vendor word, carded to him, with its reason stated on the outcome. The interim grade "is NOT a read of the earnings path (ABSENT != EXERCISED)". | **SIGN** |

Nothing else moved in any of the three halves.

-- 3.0.0_SA_CVO~Z
