# CTO ruling (cluster lead) -- COMM_ASSIST through muse: the two cross-box parts. dell2 hosts the reader folder on Andrew's word; dell2's read grant joins the Dell-grants cell as grant (d), identical on both dell users; muse -> dell2 SSH is FWD-27 v0.29 as written

From `1.0.0_SA_CTO` (laptop), 2026-10-13 ~14:4xZ. Brief: `docs/briefs/comm-assist-through-muse-midstream-brief-20261013.md`
(`4.0.0_SA_CRO`, midstream on COMM_ASSIST, D9/COMM, placed site Z). Andrew's words ~14:3xZ at the CRO terminal, record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_143xZ_DEVPLN_RECS_APPROVED_AND_COMM_ASSIST_THROUGH_MUSE.md`
@0ecb2dd97e: "I think this can be hosted on DELL2 somewhere local on the device, maybe DELL2 has some kind of script that pulls
open-calls and other summary info from AWS that muse would need on some local schedule to DELL2 local for muse to access through SSH."

The brief's L2 (the COMM_ASSIST PRD addendum) and its four open decisions are `1.0.0_SA_CTO~Z`'s, site Z's fabric; nothing here
rules them. This record rules only what crosses boxes.

## 1. dell2 hosts the folder and the refresh script for a site Z project -- RULED YES, on his word

- A reader folder on dell2 for a project placed on site Z is not the cross-box CloudOps pattern Andrew refused at 13:1xZ (a seat on
  one box doing another box's project work); it is a host he named for a file muse reads. COMM_ASSIST stays placed on site Z and
  stays the ONE assistant (brief PART II); dell2 runs a READER of it on a local schedule.
- The folder, the script and the schedule are cut by site Z's issuer as COMM_ASSIST cells and executed by dell2's seats as orders
  addressed to dell2's lanes (its CloudOps lane for the scheduled task, `0.0.0_AB_MSTR~DELL2` for the seat). That is a project on
  one box ordering a named host act on another, which the control plane already allows (NFRA_CTLPLN C-SEATS; the IRPT read orders
  ran the same way); the order names its box, its paths on dell2, and the file layout muse is told once.
- Non-ASCII, secrets and client content: the folder carries summaries and draft text only (brief O6); no key, token or client
  address is written to it, and the refresh script's reads are status and text, never credentials. A file that could not refresh
  says so in its own bytes (brief O5): absent is not empty.

## 2. dell2's read grant -- RULED: grant (d) of the Dell-grants cell, identical on both dell agent users

Ruling @1161dc05fc (13:2xZ) already cuts three grants for the dell identities as NFRA_CTLPLN round-12 cell 1 under one never-widen
pair. This adds a fourth statement to the same cell and the same pair, so the rule "the dell agent users are identical" still holds
and no second pair is opened:

(d) READ-ONLY on exactly the three sources the brief names, each scoped to its resource:
    - DynamoDB `teams-global-chat-assist-table` (`dynamodb:GetItem`, `Query`, `Scan` on that table ARN only; no write action);
    - the open-calls cluster copies, `s3://opal-313476888478-globgrph/fabric/open-calls/v1/*` (`s3:GetObject`, `s3:ListBucket`
      with a prefix condition on `fabric/open-calls/v1/`);
    - the sprint pages, `s3://opal-data-portal-v2/daily-reports/*` (`s3:GetObject`, `s3:ListBucket` with the prefix condition).
    Nothing wider: not the table's write actions, not the bucket roots, not the IRPT key (that is grant (a)).

- `2.0.0_SA_COO~C` adds (d) to cell 1's build cell; the CTO half (this seat) and the COO half cover four statements; applier
  `0.7.0_AE_CloudOps~U7` by `safe-apply` after the managed policy's oldest non-default version is pruned (5 of 5 today). The
  read-back for (d) is dell2's own: one `GetItem` on the `eod:<today>` row (status only), one `ListObjectsV2` on each prefix
  (count only), three lines, no content. Where F7 of the brief reads "NOT measured", the read-back is the measurement.
- The grant lands before any COMM_ASSIST cell writes the folder: a refresh script that runs under a denied identity writes an
  "unreadable" file, which O5 permits, but the cell is not graded on it.

## 3. muse -> dell2 over SSH -- already FWD-27 v0.29; nothing to add

NFRA_CTLPLN ADDENDUM v0.29 (@aca7293eed) names muse as a source and every box as a target, tailnet-only; `0.0.0_AB_MSTR` measured
(msg 108757) that muse's key login to dell2 already answers. The remaining FWD-27 work on dell2 is the cell's (password login off
once the key is in place, the non-tailnet refusal arm), not this brief's. The brief's O6 bound ("SSH to dell2 answers tailnet
devices only") is FWD-27's ACCEPT verbatim in substance.

## 4. The muse answer path (brief decision 3) -- a note for the site Z ruling, not a ruling

If `1.0.0_SA_CTO~Z` takes REC (a), muse writes an answer file into the dell2 folder and a dell2 job forwards it into LDO-001's
event routes. That forwarder needs a WRITE from dell2's identity to the assistant's event entry; it is not in grant (d) and is not
granted by this record. When site Z's L2 names that entry, its grant comes to this seat under C-ROLE-REQUEST as one more
statement, read at its bytes. Flagged so that the addendum does not inherit (d) as if it covered the write.

## Acts

- `0.0.0_AB_MSTR`: relay the brief and this record to `1.0.0_SA_CTO~Z` (COMM_ASSIST's L2 addendum and the four decisions are
  theirs; cross-box parts are ruled here) and to `0.0.0_AB_MSTR~DELL2` / `1.0.0_SA_CTO~DELL2` (dell2 is the host; its lanes take
  the folder and refresh orders when site Z issues them; its read-back of grant (d)).
- `2.0.0_SA_COO~C`: grant (d) into round-12 cell 1; the COO half re-cut over four statements.
- No act for Andrew: the host is his word; the grant is Opal's own IAM under the pair.
