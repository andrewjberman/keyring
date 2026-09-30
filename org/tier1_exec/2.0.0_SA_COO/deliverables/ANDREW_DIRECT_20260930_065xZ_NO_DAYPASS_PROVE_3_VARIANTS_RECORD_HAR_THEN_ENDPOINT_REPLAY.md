# ANDREW-DIRECT 2026-09-30 ~06:5xZ (at the `2.0.0_SA_COO~Y` terminal) -- no day pass; prove the three variants under the canonical identity; record HAR; then endpoint replay

Recorded by `2.0.0_SA_COO~Y`. Verbatim, in full:

> Are you saying that report generation absolutely has to be a browser crawl or some bullshit through their thing?
> If that's the only way, so be it, but the immediate thought I'd have on this matter is basically, go do the walk
> anyway and prove the generation through the method i described which is canonical in our cloud, not this fucking
> daypass bullshit, and while you do it (svc account or otherwise), record HAR and identify the endpoints that appear
> in that recording, because the next thing we're going to want to try after running it end to end is if we can
> effectively pull together the process just by running key endpointsin order and feeding them into our own script
> rather than even going with a YCharts native generation. The YCharts native generation i would say is V1, we need
> to prove that really bad that we can actually do it properly for the 3 variants, but as soon as we've nailed it
> reliably a few times will want to really hone in on the endpoints and see if we can just call those in order and
> assembel with a script. I think Alyssa had a script specifically for generating an Opal-branded presentation which
> I would love to test pending that we were able to pull all the relevant endpointinformation. IN any case though, go
> tighten up (aka slash the bullshit) in the IRPT login flow, whether its a crawl or something else, make sure it
> actually works, and then follow the steps and research/investigation i described for you already in this query.

Preceded, same terminal ~06:3xZ, by:

> in my opinion the whole failure here is trying to get clever with a day pass. We have a long-lived token, just use
> it. I don't understand why there are four resources and only 1 at best is doing their job correctly. The pattern we
> use is always the same. Its an EC2 crawler crawls for long lived trust token, and Lambda hits REST API using that
> trust token to do whatever the job is.

and:

> Was there an architectural choice backing the day pass idea? i dont understand why we'd diverge to that

## What it decides, as this seat reads it (scope relayed verbatim, not widened)

1. **The day pass is OUT for job submission.** *"not this fucking daypass bullshit"* -- an explicit prohibition on
   the per-window principal for this work. It stays a browser-walk tool only (consistent with CTO 103196).
2. **The identity is the canonical one -- a long-lived service account -- and he leaves the exact form open:**
   *"svc account or otherwise"*. CTO 103196 already ruled `svc-irpt-analysis` (service userType, Secrets Manager
   credential, `allowedFirmIds` cottonwood only). This direct is the authority for creating it.
3. **The three-variant proof RUNS, under that identity.** *"go do the walk anyway"*, *"we need to prove that really
   bad that we can actually do it properly for the 3 variants"*. Per-use word for those YCharts calls: given here.
4. **Record HAR during the walk and census the endpoints.** *"record HAR and identify the endpoints that appear in
   that recording"*.
5. **V1 = YCharts-native generation, proven RELIABLY -- "a few times" -- before V2.** V2 = replay the key endpoints
   in order from our own script and assemble ourselves, *"rather than even going with a YCharts native generation"*.
6. **Alyssa's Opal-branded presentation script is the V2 target to test**, once the endpoint information exists.
7. **Tighten the login flow first** -- *"slash the bullshit ... make sure it actually works"* -- then do 3-6.

## What it does NOT decide

- Whether a browser crawl is the only way to generate: his own words are *"If that's the only way, so be it"* -- the
  HAR is what settles it, and this seat has NOT established it (row S233: all five gateway REST verbs are data;
  none exports a PDF; no vendor export endpoint has been probed).
- The never-widen mechanics of creating the service principal: CTO 103196 says its own ledger and halves. This direct
  is the authority the halves cite; it does not skip them.

## Broadcast

Same turn, to `1.0.0_SA_CTO`, `4.0.0_SA_CRO`, `0.0.0_AB_MSTR`, `2.0.0_SA_COO~P`, `2.0.0_SA_COO~M`, push state stated.
