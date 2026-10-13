# L4-R review, NFRA_MCPINDEX PRD v0.9, ratified-text half -- REFUSE (3.0.0_SA_CVO~Z, 2026-10-13 ~19:4xZ)

**Asked by** `1.0.0_SA_CTO~Z` msg 33702 (acked). **Bytes reviewed:**
`org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md` @4b929a4476; `git diff a71e82b221 4b929a4476`, whole
(the version bump, FWD-20 and FWD-21 in ENDPOINT, the v0.9 addendum). Half hash at delivery: `0fa643617bfd`.

## Sources read at their pins

- **Andrew's memos**, `DIRECTION_SITEZ_20261013.md` @4e963d4a12: `:50-52` carry FWD-20's quote ("We need to be able to
  see all indexes for all vendor slash channels ... the depth and breadth of channels and indexes and tools available per
  vendor"); `:101-102` carry FWD-21's ("set up the MCP index for that bucket ... so that the asset managers can use that
  with their cloud"). Both match. The elisions do not change the meaning.
- **Servable-prefix list v3** @0b2778751a: 24 of 24 rows classed; 11 SERVE (rows 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 22);
  row 8 is the six named gold tables, never `amgt/harvest/gold/` whole; `management/v1/` SERVEs only once its view
  exists. This matches FWD-21's ACCEPT and addendum item 1. Andrew's ~19:0xZ word is quoted verbatim in the list.
- **Positioning ruling** @f469cb665f and the round-10 ruling (in 4b929a4476): one short round, FWD-19 and FWD-11 parked.
  This matches the addendum.
- **`infra/aws/ec2/EC2_MANIFEST.json`**: `services.opal-gateway.deployed_commit` exists (185dc04888 at read). Addendum
  item 3 names a real key.
- **Counterpart, NFRA_MCPORTAL PRD** @cdb5ff66b1: its FWD-20 lists each channel's tools and catalog indexes from
  `refs/DATA_CATALOG.yaml`, and its C15 generates the map from the deployed gateway's definitions. The two PRDs agree on
  source and reader.

## Verdict: REFUSE -- one defect, in FWD-20's partition

FWD-20 DONE WHEN reads "N tools served and N naming a catalog entry (or a GAP entry)". That two-member partition does not
cover the domain (TAXONOMY LAW, postulate i), and its second member is at the wrong grain (postulate ii).

1. **Wrong grain.** This PRD defines a GAP entry as "a need with no tool" (v0.7 addendum item 1, `:511`; also `:127`,
   `:233`, `:291`). FWD-20 asks about the opposite case, a TOOL with no index. Filing that case as a GAP entry gives one
   word two meanings in one catalog.
2. **Uncovered member.** A tool that reads no dataset has neither a catalog index nor a gap: `send_email`, `reply_email`,
   `create_draft`, `send_chat_message`, `send_channel_message`, `upload_text_to_site`, `copy_site_file_to_s3`,
   `save_email_attachment_to_site`, `whoami`, `opal_data_refresh_upload`. That is 10 in this session's opalgateway tool
   list. It is an instance count, not a census of the deployed definitions. As written, each of these must be given a
   GAP entry to reach N of N. The census would then pass, and MC Portal would show these action tools as missing an index.

**The fix (one clause, an ENDPOINT change, so this half re-signs):** split the partition into three named members that
sum to N, each counted with the denominator printed:
- (a) names its catalog index;
- (b) is a data read with no index yet, owner named or `unowned`;
- (c) reads no dataset ("no index: not a data read").

Depth and freshness bind on (a) only, and (b) states them as absent. Classify each tool from the tool's own definition,
never from its name.

Everything else in the half would sign. FWD-21 carries the list at its width. Addendum items 1-5 agree with C1, which
remains the single writer of `DATA_CATALOG.yaml`, and with rule 30. Item 4 (no two parallel catalog writers) is correct.

## Carried (not grounds)

1. **A seat reference inside ENDPOINT.** FWD-20 SOURCE says "via the laptop CTO's direction". FWD-21 cites only
   "XB-4d72 Z4/Z5", and the FWD-20 line can do the same. Strip it in the same bump.
2. **Z4(a) is not closed by either PRD alone.** Andrew's done-when is "on MC Portal, every tool ... names its catalog
   index and that index's history depth and freshness". MCPINDEX FWD-20 makes depth and freshness readable. MCPORTAL
   FWD-20's ACCEPT lists tools and indexes but not depth or freshness. Displaying them is an MCPORTAL enrichment item, or
   Z4(a) stays half-met.
3. **FWD-21, a row whose read is a GAP.** Row 8's tables are Parquet. If no existing read tool reaches them, ACCEPT makes
   them GAP-read rows. DONE WHEN still needs `opal_discover` to return them as catalogued datasets. The decomposition
   should say whether a row whose read tool is a GAP satisfies "catalogued".
4. **The list's first catalog act** ("read one object and confirm the class"; the list's sample is 1 per row) is not in
   FWD-21's ACCEPT. The COO's battery can carry it.

-- 3.0.0_SA_CVO~Z
