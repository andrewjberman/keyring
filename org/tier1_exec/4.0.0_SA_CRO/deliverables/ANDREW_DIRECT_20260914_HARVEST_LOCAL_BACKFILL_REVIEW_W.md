# Andrew-direct: harvest backfill prior-art review

**Author:** 4.0.0_SA_CRO~W
**Channel:** direct user message at this Codex terminal
**Recorded:** 2026-09-14 (US Eastern; exact message timestamp unavailable)

## Instruction (verbatim)

> I'm bringing you online specifically to look into any prior art we have established regarding enacing a "opal-data-harvest" backfill. This would be an operation to pull data from the various 4 primary publications, I believe that we should test it locally; i do not believe large scale backfill should be pursued in the cloud. the truth of the matter is that we could make this a scheduled or otherwise ongoing job from the BBG Terminal sitez device because its always on, which may be the way to go until we are sure that a cloud solution would actually work reliably. Before initiating any type of backfill, I would want to know exactly the nature of collection and the shape of the data we are collecting to make sure we can get it without any html or bullshit, which shouldnt be an issue because we're using REST API for pretty much everything except for WSJ. Look into the prior art, the bucket shape and api puller shapes, and lets discuss.

## Current act

Inspect prior research, the existing bucket contract and API pullers; report data shapes, evidence limits and local-run implications for discussion. No backfill or recurring job is initiated by this review. The SiteZ scheduled-job idea remains a proposal in the instruction's own terms.

## Subsequent direction (verbatim, same terminal and date)

> Dont worry about anything stored already, you are looking for *harvest scripts. there should be briefs specifically on these harvest scripts, they have not been employed in a comprehensive basis yet, only tested. We probably have to start attempting a fill to see how they perform in a live fire environment.

> What I mean to say is that any pulls done on these sources, may or may not be the product of these scripts. These scripts need to be tested on batches of securities live on this device so we can see how they fare on say, a batch of 5 securities from the list of 89.

## Updated act

Test the documented four-publication scripts live on this device with five securities selected from the 89-name universe. Attribute results to the exact tested script bytes and retain outputs locally. Existing bucket specimens do not establish these scripts' current behavior. No broad backfill or recurring job is started.
