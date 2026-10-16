# L4-R review -- TCKT_MTADTA PRD v0.1, ratified-text half (ENDPOINT + CONTRACTS)

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (dell1), 2026-10-16 ~06:4xZ. Delivered by 1.0.0_SA_CTO~DELL1 msgs 6553 and 6554 (both acked).
**Graded:** `org/missions/D7/TCKT/TCKT_MTADTA/prd/TCKT_MTADTA_PRD.md` @315f7a19af (v0.1, half hash 2d09b07719a4). New project; it supersedes NFRA_WFSPINE, whose v0.1 this seat refused (`L4R_REVIEW_NFRA_WFSPINE_v0.1_RATIFIED_TEXT_20261016.md` @9fbcb7c2bf).

## Verdict: REFUSE -- one gap. The eight's events can store colleagues outside the eight as recipients or sharees

## What is right (most of it)

- **ENDPOINT is VERBATIM:** the FWD-1..FWD-10 block (65 lines) is byte-equal to `ENDPOINT_FORWARD_TCKT_MTADTA_20261016.md` @a7a7df4e6f (diff empty).
  Andrew confirmed it: "yes, only iam globgrph group can access, if you want to access you have to go through the reader/writer lambda"
  (`ANDREW_DIRECT_20261016_062xZ_..._READER_WRITER_LAMBDA.md` @f4fbcdfde4 line 9).
- **The WFSPINE refusal is answered:** C-POPULATION now filters in memory before the first write and counts the drops. FWD-7 reads "not even in
  the first copy written", on Andrew's "all other domains/accounts should be dropped at the outset and not stored"
  (`ANDREW_DIRECT_20261016_054xZ_...` @0092da40fe lines 12-13). That word is his acknowledgement of the R9 departure.
- **C-ACCESS matches his access word:** the group invokes, the Lambda's role is the bucket's only principal, a dedicated key, an explicit
  Deny for every other principal, and the collector writes through the Lambda.
- **C-RESIDUAL is honest:** root, policy editors, Andrew's Cloud Application Administrator reach, and group members are named, with the later
  AWS Organization project placed as the removal.
- **C-FIELDS minimises:** no sign-in feed, keyed-hash subjects, external addresses reduced to a domain, raw IPs replaced by an office/remote flag.

## The gap (every operative constraint present: NO, on one point)

FWD-7's ACCEPT reads: "a colleague who is not on Andrew's list does not appear anywhere in what is kept". C-POPULATION filters on the event's
ACTOR (UserId, MailboxOwnerUPN, SendAs, SendOnBehalfOf). But an event whose actor IS one of the eight can still name a colleague outside the
eight as its target: a mail recipient, a sharing target, or a file's other user (for SharePoint sharing events, the target user field).
C-FIELDS (c) reduces only EXTERNAL recipient, sharee and guest addresses to a domain, and keeps "the eight's own addresses". It says nothing
about an internal `@opalinvest.com` address outside the eight, so as written that address is stored verbatim in bronze. That contradicts
FWD-7 and Andrew's "all other ... accounts should be dropped at the outset and not stored".

**What would make this signable:** C-FIELDS (c) covers every address that is not one of the eight's, internal or external. Each is reduced
before the first write to a team-exit marker (FWD-2 reads "leaving the team, not as a break") or to its domain, with a planted
internal-colleague recipient in the proof. This seat re-signs on a re-read of that row alone.

## For Andrew, not a ground to refuse

- **"all other domains ... dropped":** C-FIELDS (c) keeps external DOMAINS (for example a client's domain on a sent mail). His words say other
  domains are dropped and not stored. Keeping a domain for FWD-2's "leaving the team" is a reasonable reading, but it is a reading; confirm
  it with him or drop the domain to a bare "external" marker.
- **File and site names kept (C-FIELDS (e)):** a file name can carry a colleague's or client's name (C-CLIENTDATA says so). FWD-7's "does not
  appear anywhere" can be breached through a file name. Name it in C-RESIDUAL so the statement Andrew holds stays honest.

## What you should have asked

Whether the access Lambda's query surface lets a member reconstruct a colleague's activity from the eight's events: for example, everything
sent to one non-eight address. The reduction above closes that only if it lands before the first write.

-- 3.0.0_SA_CVO
