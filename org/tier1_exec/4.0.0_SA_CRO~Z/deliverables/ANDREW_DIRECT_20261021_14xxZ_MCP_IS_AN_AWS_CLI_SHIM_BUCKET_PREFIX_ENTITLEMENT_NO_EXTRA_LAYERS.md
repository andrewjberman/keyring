# ANDREW-DIRECT 2026-10-21 ~14:xxZ -- the MCP is an AWS-CLI shim: query the tables you are permitted, entitlement by bucket and folder, no extra layers

Channel: typed by Andrew at the `4.0.0_SA_CRO~Z` terminal (Claude Code session, site Z), ~14:xxZ (10:xx AM ET). It followed
this seat's answer that a literal AWS-CLI pass-through would bypass the gateway's grant, firm fence and masking, and that the
Schwab DuckDB engine is the in-estate pattern for bounded reads.

## VERBATIM

> So I want to cover how the MCP server is intended to work for a lot of these AWS tables. What it seems like is we're building
> a lot of custom tables that sit on top of the MCP or something and it's getting overly complicated, overly redacted. It loses
> the ability to be business functional. The premise of what we are trying to do here is simply have the MCP, the a shim of
> sorts, uh, to get to an AWSCLI so that users can just query the tables that they have access to. We're not going to try to
> redact tables. We're not going to try to make all these extra layers. The premise is that they simply have have COI style
> query access to the tables, which are permitted in these groups. That's all. There's no custom tables, no nothing. The purpose
> of the tools was just so that they could query these tables quickly and easily. The tools may not even be necessary. Claude
> can just do bash. It's like Quad could just do bash on the spot, which, um, the reason I'm saying this is because we need to
> figure out how, uh, a lot of this stuff is being handled because uh, pagination seems to be a clear issue in a lot of this
> stuff, where I think we've done a fairly good job with our swab stuff, with our swab and Orion and et cetera. We need to see
> how those folders are organized. I don't believe that the, uh, pagination should be a huge issue for most of them in the case
> of the cottonwood file dump. Yes, I could see how that would be an issue. Um, If we need a duck DB solution that's fine, but I
> want to stress that the purpose here is not to make any extra and unnecessary layers. We want this to be liquid access,
> liquid, clean, and clear. The entitlement layer is for accessing whole buckets, accessing buckets or maybe accessing various
> folders within those buckets. It's like that's that's really how we want to organize this. We don't want to be, because what
> happens is it gets very too much complicated when we don't know what what is being redacted and where, and then it loses
> business use, it loses functionality. Like, this is really just an AWSCLI put on top of an MCP. That's the simplest way to look
> at it. We wanted to index it a little just so Claude didn't have to like pull a bunch of shit into its context. But let me
> know what you find. We obviously want to do this in such a way where Claude is not pulling in 5000 million rows into, or
> sorry, like 5000000 rows into context. Like obviously that is completely retarded. Um, There should be a way to do this
> exactly as AWSCLI does. We're just, we're just facilitating that through the MCP. So it's just no code and easy and we can
> retain a control plane.

## Recorded as said, not adjudicated here

1. **Intended design.** The MCP is a shim to AWS-CLI-style query access over the tables a user is permitted. It has no custom
   tables, no redaction and no extra layers. The tools exist to make querying quick and easy, and "may not even be necessary".
2. **Entitlement grain.** Whole buckets, or folders within buckets. That is the organizing unit.
3. **Indexing.** A light index, so Claude does not have to pull a lot into its context.
4. **Size.** No call puts millions of rows into context. Pagination should not be an issue for most tables; the Cottonwood file
   dump is the exception. DuckDB is acceptable where needed, but not as an extra layer.
5. **Retain a control plane.** "it's just no code and easy and we can retain a control plane."
6. **The asks of this seat.** See how the folders are organized (Schwab, Orion, et cetera), find how the current handling
   works, and "let me know what you find".

**Relation to existing records.** This is stated as the premise of the MCP. It bears on the NFRA_OPLGTW contract's per-column,
per-account and masked-reference grant model, and on NFRA_MCPINDEX's typed per-dataset tools. Those are surfaced here, not
adjudicated.
