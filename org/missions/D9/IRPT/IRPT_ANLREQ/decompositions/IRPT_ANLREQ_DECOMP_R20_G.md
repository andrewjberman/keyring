# IRPT_ANLREQ round 20, workstream ~G (ENGINE) -- decomposition: the upload door derives the price date

Issuer `2.0.0_SA_COO~G2`, 2026-10-15.

**Input:** PRD v0.16 @a4af0e5bba (CTO msg 8647; Andrew-direct ~20:4xZ recorded in `ANDREW_DIRECT_20261015_204xZ_NO_PRICE_DATE_SELECTION_LATEST_CLOSE.md`): no price-date input; every price is the T-1 frontier close, stated as the report's as-of; "T-1 is the correct terminology"; the door derives the date and never requires it; a `priceDate` a client still sends is ignored and logged, never honoured; the change rides `~G2`'s one resident release. The door code (`intake/uploads.py`, `intake/portfolio.py` `default_price_date`), the issuer's reference build.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **Ignore at the validator.** The one place every upload payload passes is `validate_upload`, called by the service and by the submission pre-check. Dropping the value there means it can never reach the options, the revision hash or the price request, and `default_price_date` (which returns a sent date as sent, and is left as it is) is only ever called with `None` by the door.
- **A sent date is accepted and ignored, not refused.** Old clients, and a form that has not yet lost its field, still validate; "ignored" holds for ANY value, including a malformed one (a previous test expected a refusal for `2026-13-45`; it now expects the derived date). The shape guard stays on `reference_notional`.
- **The log is a closed token.** `IRPT_UPLOAD price_date_ignored=1`, printed when a non-`None` value was sent, never the value. The resident's journal takes tokens only; an untrusted string must not reach it.
- **Replays of pre-change uploads.** The options (and so the revision) of an upload that once sent a date now differ, so a re-post of the same token meets CHANGED_UPLOAD_SAME_TOKEN. The form never sent a real date after its own change and upload tokens are short-lived; stated in the order's preflight, not mitigated.
- **Four existing tests** (two in `test_price_date_default.py`, two in `test_uploads.py`) encoded the old behaviour and change as the order lists; the reference build showed them failing and nothing else.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-95` | `intake/uploads.py`: `validate_upload` drops and journals a sent `price_date`; four tests edited; `tests/test_price_date_ignored.py` (5 named tests) | the four product/test files named in the order + the worker's folder | WORLD (floor of an infrastructure path; source and tests only) |

## Edges and chains

- ONE chain. `intake/uploads.py` is already in the r32 files-from list (it is an r31 member), so the release build takes this cell if it merges before the pin.

## Four-postulate record

(i) Domain: the price date of a SHARES upload. (ii) One validator, one derivation. (iii) One intent: the date is the server's. (iv) What this cut does NOT move: `default_price_date`, the prospect-dates reader, the schemas, the portal's form, any deployed byte.

fanout: 1 of 1 chain, cap 8, reason: one door file and its tests; slot 196.
