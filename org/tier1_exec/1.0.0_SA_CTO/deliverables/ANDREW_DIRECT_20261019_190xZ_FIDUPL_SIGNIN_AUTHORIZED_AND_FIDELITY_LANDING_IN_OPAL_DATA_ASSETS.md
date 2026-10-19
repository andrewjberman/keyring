# ANDREW-DIRECT 2026-10-19 ~19:0xZ -- NFRA_FIDUPL: automated sign-in authorized; Fidelity lands in opal-data-assets per client

Given at the laptop 1.0.0_SA_CTO terminal, answering this seat's relay of dell1's two answers (1.0.0_SA_CTO~DELL1 msg 8457: the Wealthscape
Terms of Use as dell1 act c3a6; one Fidelity home through the FIRM scope 'alongside', bucket opal-data-alongside). VERBATIM:

> "We can absolutely do the automated sign in, we are authorized users of the application. On the Fidelity storage, I would recommend that we
> drop it in opal-data-assets, using the fidelity channel and essentially pulling them to the relevant bronze buckets per client. THe issue
> becomes whether or not we have a clear mechanism by which to do that. If we do not, and need to use alongside as a staging bucket for the
> full pull, and afterward we effectively parse out what goes to fidelity-bronze-49financial and fidelity-bronze-inflection and so on in the
> relevant paths in opal-data-assets, then so be it."

## What it settles

1. **The automated sign-in is authorized.** "We are authorized users of the application." This is his answer to dell1 act c3a6 (Wealthscape
   Terms of Use); dell1 closes c3a6 on it.
2. **The landing preference:** `opal-data-assets`, the `fidelity` channel, per-client bronze paths.
3. **The fallback, also authorized:** if there is no clear mechanism to land per client directly, stage the full pull under Alongside, then
   parse each firm's accounts out into its own Fidelity bronze path in `opal-data-assets`.

## The mechanism question, measured by this seat (~19:0xZ)

`lib/opal_naming.py address()` on laptop HEAD, `origin/CLOUD` @2700c23637 and `origin/box/dell1` returns, identically on all three:
- `address('fidelity','49financial','bronze','positions','date=2026-10-16')` -> `s3://opal-data-assets/fidelity/49financial/bronze/positions/date=2026-10-16`
- `address('fidelity','inflection','bronze',...)` -> `s3://opal-data-assets/fidelity/inflection/bronze/...`
- `address('fidelity','alongside','bronze',...)` -> `s3://opal-data-assets/fidelity/alongside/bronze/...`

So the ADDRESSES for both his preference and his fallback already exist in the builder (rule 30). The open part of "a clear mechanism" is
the split rule: which firm owns each account in a full Alongside export. That is dell1's to measure: does the Wealthscape export carry a
field that names the firm, or a rep or account-group code that maps to one?

## What it changes on dell1

dell1's stated home (msg 8457) was the bucket `opal-data-alongside`. His word puts Fidelity in `opal-data-assets` (the builder's own home for the
fidelity source). Whether `opal-data-alongside` is still needed at all is dell1's to rule. NFRA_AWSFTP (held) follows the same landing when it
lifts.

-- 1.0.0_SA_CTO (laptop)
