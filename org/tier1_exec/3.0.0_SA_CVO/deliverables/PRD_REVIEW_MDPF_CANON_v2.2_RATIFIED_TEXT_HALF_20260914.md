# PRD REVIEW -- MDPF_CANON v2.2 @ef21e34660 -- the RATIFIED-TEXT half (ENDPOINT + CONTRACTS; L4-R) -- 3.0.0_SA_CVO

**Archetype:** VALIDATE.
**Reviewer:** `3.0.0_SA_CVO`.
**Requested by:** the L4 notifier, msg 96561.

**Prior:** v2.1 was REFUSED on R2, the route row. The review is @`e6462c2f67` and the stamp @`95ba6c9f91`.

**Read, UTC 2026-09-14, after 09:53:53Z:**
- The PRD @`ef21e34660`. The working copy is identical to the pin.
- A section-by-section diff against v2.1 @`6ab0a19bd4`, through `.tools/prd_signoff_lib.py`'s own `top_sections` parser.
- The route row in full.
- The sources it cites, as read for v2.1: `ModelPortfolios.tsx` @portal `ca8524a1` and `shared-advisor-router/index.mjs` @`40697fe79d`.

**Half hash reviewed:** ratified-text `d5177552975dceaaca733a6e8d5a790765891b9fcf7b6ef5e77ccece7b5e1fac`. It matches the
notifier's `d5177552975d`.

## VERDICT: SIGN -- R2 is closed; one new non-blocking note (N5)

## THE DIFF OF THIS HALF, v2.1 -> v2.2

- **ENDPOINT is byte-unchanged.** 8 of 8 outcomes are still verbatim.
- **CONTRACTS changed on one row, the route row, and only that row.** The key-string row is unchanged, so R1's closure (@`e6462c2f67`) carries.

## R2 -- CLOSED

| what the v2.1 review asked | v2.2's route row |
|---|---|
| resolve the segment the way the router does, aliases included | *"a firm segment resolves through the registry, aliases included, to one firm"* |
| serve the firm's own tenant | *"a session whose validated tenant resolves to that same firm"* |
| serve internal Opal staff, with the path segment as their selection | *"an internal Opal staff session (tenant `opal-capital`), for which the path segment IS the selection because the frozen portal's selector sends no `?firm=` on these requests"*. It cites `ModelPortfolios.tsx:357-358` and Andrew's MDPF_SCOPED.S5 |
| refuse any other firm | *"Any other firm's session is refused"* |
| state the router's boundary, never the bare test | *"the boundary the scoped router already enforces by comparing resolved buckets (`index.mjs:367-373`) ... never a bare segment-equals-tenant test"* |

**Carried unchanged, and correct:** `global` keeps its general handling; *"Keeping the old URL never keeps general
authorization for firm data"*; and the counterpart list.

**Both cited lines resolve** to the text quoted, at the vintages read for v2.1.

**The row now agrees with DEC-5** (*"the assertion ... the scoped router already applies"*) **and with FWD-2.**

## NOTES (non-blocking)

- **N1-N4:** carry from v2.1 (@`e6462c2f67`), unchanged.
- **N5 (new) -- is a dev superadmin session admitted?**
  - The page treats `isInternal() || isDev()` as internal (`ModelPortfolios.tsx:352-353`), and its comment at `:534` calls isDev a "superadmin".
  - The row admits staff by tenant `opal-capital`. Which tenant a dev superadmin session carries is NOT MEASURED.
  - If it is not `opal-capital`, that session keeps the page's selector and is refused by this row.
  - Fix, at L5 when M9 reads the live router: settle whether dev superadmin is admitted. The router's admin bypass (`index.mjs:153-156`) sits on the tier check, not on tenancy.

## NOT CLAIMED

- **The brief half.** It is `4.0.0_SA_CRO`'s. Its DECISIONS and CELL CANDIDATES sections changed in v2.2, and they are not graded here.
- **That the compatibility mapping can be built.** M9 reads the live behaviours at L5.
- **That the key vector runs.** `lib/opal_naming.py` does not exist yet.
