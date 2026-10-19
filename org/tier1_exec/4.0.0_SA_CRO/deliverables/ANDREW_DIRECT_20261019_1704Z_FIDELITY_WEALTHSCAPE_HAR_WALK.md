# ANDREW_DIRECT 2026-10-19 ~17:04Z -- Fidelity Wealthscape HAR walk for an Auto-Schwab-shaped daily loader

- **Channel:** in-session, Claude Code terminal, dell1, to `4.0.0_SA_CRO~FIDELITY`
- **Time:** 2026-10-19 ~17:04Z (1:04 PM ET)
- **Receiving seat:** `4.0.0_SA_CRO~FIDELITY`

## Verbatim

> What I need from you here is we need to do some walking of the Fidelity Wealthscape portal to see what kind of
> solution can be built from it in the same manner as the Auto-Schwab EC2 loader that we built for the Schwab masters.
> We hope to get a FTP solution from Fidelity and SChwab, but in the meantime we need to assess how to generate the same
> kind of daily autoloading solution that we built at Schwab. I will send you a HAR of me walking through their
> Wealthscape platform and I need you to analyze it and identify where the endpoints are so that we can build a
> comparable solution for authentication and daily morning pulls, same time as the auto schwab solution and same
> design. Like Schwab, we will need to identify the shape of the data we are able to get from them in the interest of
> telling whether the shape is similar so that we can in essence run the exact same data engineering.

## Scope as given (surfaced, not adjudicated)

1. Analyze Andrew's Wealthscape HAR (to be sent): the authentication flow and the data endpoints.
2. Assess a daily morning autoloader for Fidelity, same schedule and same design as the Auto-Schwab EC2 loader.
3. Characterize the shape of the Fidelity data reachable, compared against the Schwab masters' shape, to judge
   whether the same data engineering runs on it.
4. Interim: the hoped-for FTP feeds from Fidelity and Schwab would supersede this.

Handling note: a HAR carries session cookies, tokens and client PII. It stays in the session scratchpad; it is never
committed. Only the redacted endpoint map and shape analysis land in the repo.
