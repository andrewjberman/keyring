# ANDREW_DIRECT 2026-10-19 ~17:55Z -- build the auto_fidelity uploader (Terraform), same structure and timing as Auto-Schwab

- **Channel:** in-session, Claude Code terminal, dell1, to `4.0.0_SA_CRO~FIDELITY`
- **Time:** 2026-10-19 ~17:55Z (1:55 PM ET)
- **Receiving seat:** `4.0.0_SA_CRO~FIDELITY`
- **Context:** follows `ANDREW_DIRECT_20261019_1704Z_FIDELITY_WEALTHSCAPE_HAR_WALK.md` and the research in
  `RESEARCH_20261019_FIDELITY_WEALTHSCAPE_HAR_ENDPOINT_MAP.md` (addenda 1-2)

## Verbatim

> The text message code goes to the Quo 561-621-3066 digital phone line which we should already have api access for.
> The OTPs are sent via the 877-372-1150 number. So we should be able to set that up in our device. I would like to
> build out a terraform for auto_fidelity uploader, essentially taking the same structure we did for schwab and applying
> it to fidelity and making a terraform around it. once that is done, we need to make sure that we can pull the
> relevant tables from it every morning at the same time that schwab does, so we can have consistency on timing for that
> ingestion.

## Scope as given (surfaced, not adjudicated)

1. The Wealthscape SMS OTP is received on the Quo digital line (the number in the verbatim text); the sender is the
   Fidelity short-code line in the verbatim text. Opal is believed to have Quo API access already. That is how the box
   is to read the code.
2. Build Terraform for an `auto_fidelity` uploader with the Auto-Schwab structure.
3. Pull the relevant tables every morning at the same time as the Schwab pull.
