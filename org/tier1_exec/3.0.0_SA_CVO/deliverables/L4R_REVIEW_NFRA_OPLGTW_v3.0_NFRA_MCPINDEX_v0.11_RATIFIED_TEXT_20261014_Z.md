# L4-R review, NFRA_OPLGTW PRD v3.0 and NFRA_MCPINDEX PRD v0.11, ratified-text halves -- SIGN both (3.0.0_SA_CVO~Z, 2026-10-14 ~13:2xZ)

**Asked by** `1.0.0_SA_CTO~Z`, msgs 34072, 34073 and 34075, all acked.

**Bytes reviewed:** both PRDs at @7878037d98 (the working tree equals the pin).
- NFRA_OPLGTW: `git diff e5e2ce91ec 7878037d98`, read whole. It spans:
  - v2.9 C-PERSON, read at the MCPORTAL v0.8 re-read;
  - 7f90a792ea, the v2.8 role-name correction per row Z-S107;
  - v3.0, which adds FWD-22.
  - Half hash `ff3fc7b649d7`.
- NFRA_MCPINDEX: `git diff 301af339c7 7878037d98`, read whole: v0.11 adds FWD-22. Half hash `664ba1c9b0f5`.

## Sources read

Andrew-direct ~12:4xZ, `ANDREW_DIRECT_20261014_124xZ_GATEWAY_DATA_CONTRACTS_CENSUS_CRO_FANOUT.md` @06ae2a3485. Each of
the following is present in his verbatim (the pasted transcript at `:26`, or the message at `:8-14`):
- "accessible with fluid tooling";
- "forking by firm and by last 4 digits account absolutely needs to be included in any kind of client data bucket";
- "what platform we are looking for", which is the source of the `platform` fork key;
- "a table of contents for Opal Data assets";
- "I would prioritize that as number one".

"By the end of this week" is in his message, and 2026-10-16 is the recorder's working date. The 7f90a792ea correction
now names `gateway-global-internal-reader-role`, matching OG-hv-2 A5 and row Z-S107.

## Verdict: SIGN both

- **NFRA_OPLGTW FWD-22.** Typed tools are proposed by the census contracts, each marked keep, extend or retire against
  the deployed `tool_index`. Admission is unchanged and evaluated first: Opal-only, C2, tier, then C-PERSON. The
  client-data fork refuses a call that names no firm or two firms before any read, and an ambiguous last-4 returns
  candidates rather than a guess. Every new gateway read is a never-widen act. G1 item 3, the Lambda invoke of
  `opal-amgt-scoped-api`, is held to its own ask and ships separately. G1 item 4 reads Bloomberg bronze from the
  bucket and calls no Bloomberg API.
- **NFRA_MCPINDEX FWD-22.** The catalog moves to table grain: the contracts live in the catalog rows, so there is no
  second registry. `read_tool` names only a DEPLOYED tool. A retired dataset is never offered. The negative arm and the
  per-group denominators are present.
- **The two PRDs agree.** OPLGTW G1 item 2 drops `harvest_describe_dataset` in favour of `opal_describe`, and MCPINDEX
  FWD-22 makes the catalog serve that. Both retire the same two prefixes as tool targets. MCPINDEX G1 item 3 names
  `harvest_read` until each typed tool deploys, which matches OPLGTW's order: OG-hv-2's grant first, then the G1 tools.

## Carried (not grounds)

1. **"Every contracted table" in the title against "each group that lands" in DONE WHEN (OPLGTW FWD-22).** As worded,
   the outcome can be read as met once G1 alone has landed. This seat will grade FWD-22 REALIZED only when all six
   census groups (G1-G6) have landed, or when a group is retired on Andrew's word. Until then each landed group is
   graded as progress. The next addendum should state "6 of 6 groups" in DONE WHEN so the text says what the grade
   will require.
2. **"Answers project to 50 KB by default" is not in Andrew's words or the directive.** It is a reasonable default, but
   it is an operative constraint inside ENDPOINT with no source. Either source it (the gateway's existing response cap)
   or move it to CONTRACTS.
3. **Later groups land as CONTRACTS-only enrichments, so this half does not re-open for them.** Each group's new reads
   (S3, Lambda, DynamoDB) still carry their own never-widen asks. Those asks, not this half, are where this seat reads
   each group.
4. **NFRA_MCPINDEX FWD-20 depth (Z-W34-S3) is still OPEN.** The G1 contracts' freshness fields are inputs to it, but
   they do not close it.

-- 3.0.0_SA_CVO~Z
