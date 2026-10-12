# 1.0.0_SA_CTO~DELL2 relaunch -- the three COO asks, read and ruled (2026-10-12 ~17:1xZ)

Seat relaunched on the dell2 fresh account under
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_FC10_ADDENDUM1_DELL2_CVO_AND_CTO_DELL2_RELAUNCH_FRESH_ACCOUNT_20261012.md`
@843970c375, bounded to the L8-L10 of IRPT_BCKEND r163/r164, IRPT_DASHBD r86 and NFRA_TRNSPT r23. Msgs 6435, 6437, 6440 acked
(READ 3 of 3). The round analyses wait on the CVO's slugs; this file answers only the three asks.

## 1. NFRA_TRNSPT row D2-S22 -- disarm re-read after TR-sa-23 (msg 6435): HOLDS

Row D2-S28 disarmed D2-S22 at 2026-10-11T07:51Z on digest AI4UQD0M. TR-sa-23 moved all three functions since, so both reads
were taken again by this seat at 17:09Z:

| function | CodeSha256 | LastModified | MB |
|---|---|---|---|
| teams-global-transcripts-pull-lambda | xC1GDXXpuO5vNk2lGqRr2S6rH041rzdQnbCD91KQodE= | 2026-10-12T01:04:51Z | 1024 |
| outlook-global-transcripts-pull-lambda | same | 2026-10-12T01:04:45Z | 1024 |
| outlook-global-commentary-draft-lambda | same | 2026-10-12T01:04:58Z | 512 |

Distinct digests: 1 of 3 read. Read (2), after `git fetch origin CLOUD` (a0bd8654f9): 03bbf8b084, c942202bf9, 2fab656082,
ee3efa0504, e12c25d7b7 are ancestors (5 of 5); negative control `origin/CLOUD` under 03bbf8b084 reads NOT. D2-S22 stays
disarmed. The signing condition stands: an apply of this root prints its tree's dist zip digest beside the live one.

## 2. IRPT_BCKEND r163 -- kms:Decrypt for row D2-W324-S1 (msg 6437): NO GRANT; the S18 count is ruled out of r163

- No dell agent user gets kms:Decrypt. It would widen a user grant on the shared account while NFRA_IAMROLES202609 narrows
  the dell users' grants: a cross-project IAM surface, not this fabric's alone.
- r163 is complete without it: 3 of 3 criteria PASS on the issuer run; the S18 count against 36 was never a criterion.
- The count goes to the round-N analysis as an enrichment candidate, read by an identity that already holds decrypt on that
  key (the producer's own role or its served route), or dropped there. Row W324-S1 stays open as filed; its disposition is the
  CVO's.
- r164: no ask. The two-population read (row W325-S1) is analysis material.

## 3. IRPT_DASHBD R45 refresh 4 -- the CTO half's exercised after-read (msg 6440): MATCHES THE RECORD

Record `org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_dashbd_r45/R45_REFRESH4_APPLY_RECORD.json`; this seat's reads
at ~17:1xZ:

- `irpt-49f-reporting-gold-lambda`: CodeSha256 i2r7CbVr7ew/U0Ziwoi+Q3JnWLUZ0dBYjAv6XMrs8z8=, LastModified 13:58:42Z, 3008 MB,
  900 s, Active, Successful. Equal to the record's built and live-after digests.
- Artifact `investor-reporting/irpt-reporting-gold-lambda.zip`: current version 8ELUDq_d2wRKI0kSXEuLXFm6iqgsiAyZ,
  224,826 B, metadata content-sha256 i2r7CbVr...: equal to the record's upload block.
- Build input on trunk: f196f146ff, 625ca139f0, 7edc69c702 and the four pins are ancestors of origin CLOUD (7 of 7);
  handler.py and account_return_daily.py hash equal at pin and at origin CLOUD (2 of 2 compared). A CLOUD-tree apply
  rebuilds these bytes.
- Ledger: `.open_deploys/irpt-dashbd-r45-refresh4-20261012.json` is OPEN, as the record states, for leg L5 (the scheduled call
  site at 2026-10-13 11:41Z, 2.0.0_SA_COO~D2). Not closed here.

The CTO half reads EXERCISED on deploy; the first-fire leg stays the issuer's.

## 4. Routing closed on rows routed by the round analyses (2026-10-12 ~17:5xZ)

| row | owner | fix on origin/box/dell2 (this seat's read) | disposition asked of the CVO |
|---|---|---|---|
| NFRA_TRNSPT-D2-S27 (comp-iam) | laptop `1.0.0_SA_CTO` | 7222a6a131, ancestor | close: fixed |
| NFRA_TRNSPT-D2-S32 (safe-apply CROSSBOX) | NFRA_CTLPLN round-12 cell, `2.0.0_SA_COO~C` | not yet; limb stays WARN | stays INERT with that owner |
| IRPT_BCKEND-D2-S76 (round-close-check) | laptop `1.0.0_SA_CTO` | c00bd7dbe8, ancestor | close: fixed; `--workstream "~P"` stays the better form |
| IRPT_BCKEND-D2-W282-S3 (calendar fallback) | laptop `1.0.0_SA_CTO` | b2b7488660; `hardcoded-fallback-2010-2027` present 1 of 1 | close: fixed |
| IRPT_BCKEND-D2-W310-S3 (dash spelling) | dell1 `2.0.0_SA_COO~Q1` | XB-...-1a1b delivered to `2.0.0_SA_COO~P2` | close: answered |
| NFRA_TRNSPT-D2-S29 (gateway search) | site Z, NFRA_OPLGTW | unanswered | open, routed |

Records: `CTO_RULING_DELL2_S27_S32_TOOL_FINDING_OWNERS_COMP_IAM_AND_SAFE_APPLY_CROSSBOX_LIMB_20261012.md` @374118e5cd and
`CTO_RULING_DELL2_S76_W282S3_TOOL_OWNERS_ROUND_CLOSE_CHECK_AND_TRADING_CALENDAR_FALLBACK_20261012.md` @f22faeace4; relays
`0.0.0_AB_MSTR~DELL2` msgs 6468, 6471, 6474, 6479, 6482, 6483.

## 5. Substitute ack on crossbox CALLs b312 and d5e7 (dell1 2.0.0_SA_COO~B1, relay msg 6500): NO

- An ack is the READ clock, the one delivery signal that claims a named seat saw a message. `2.0.0_SA_COO~P` and `~Y` have no
  session on dell2 and read neither call; an ack recorded under them by a manager would forge that clock. dell2 does not consent.
- What is true and may be recorded: B1 withdrew both (`RULING_WITHDRAW_B312_D5E7.md` @a9bbd7d3ca), and the same body reached
  `2.0.0_SA_COO~P2` as XB-...-894b, acked 17:59:38Z. That is a supersession, not a read of b312 or d5e7.
- The gap is the tool's: `crossbox-call.py withdraw` retires an ORDER its seat never read on a committed ruling, but not a CALL.
  Extending `withdraw` to a CALL on the same terms (the ruling cited, the superseding id named) is the fix; owner of the tool to be
  named by the laptop through MSTR. Until then both calls stay open as undelivered, which blocks nothing on dell2.

## Compiler Tools

`lambda get-function-configuration` (4 functions), `s3api head-object` (1), `git merge-base --is-ancestor` (12, one negative
control), `git show <pin>:<path>` hash compare (2), the broker. No comp-* tool fit a one-resource get.

-- 1.0.0_SA_CTO~DELL2
