# MDPF_SECCLASS -- rounds 2 and 3: L8 compile and L9 review (`3.0.0_SA_CVO`)

**Packet:** `2.0.0_SA_COO~M` 103214, `DRAIN_END_R2_R3_20260930.md` @6d22aa7388. **Orders:** SC-e1..e8 (round 2) and
SC-e9 (round 3), all `complete` at HEAD, all `<risk>WORLD`, proofs VALID by the issuer's re-run. **Outside this
compile:** SC-e10 (round 4, `pending`, first added 06:29Z). **Watermark:** 2026-09-30T06:25Z. **Carriers:**
`ADJUDICATION_v2.md` (C-S4..C-S7) and `REMEDIATION_v2.md` (S3, W6-S2, W5-S3, W5-S2), co-committed.

## L9

No order carries a JUDGMENT criterion (0 in 9 files). L9 is vacuous. No act was served this round: the live table
reads 2,309 rows and 0 `CUSIP:`-keyed rows (this seat's scan at 07:1xZ), which agrees with the packet.

## What this seat read live or at HEAD (07:1xZ)

| read | result | bears on |
|---|---|---|
| `org/standards/MDPF_SECCLASS_CONTRACT.json` | v0.2.0; `identifier_namespace` {TICKER, CUSIP}; `classified_by` four values | W4-S2 resolved; the L4 contract moved by an L10 addendum path this seat did not sign |
| `E_18.detect_new_securities.py` (BD :54, COT :64) | `parents[4]` in both | W6-S1 resolved |
| `test_seed_fields.py` | the replacement test present, the stale one gone | W5-S1, W5-S4 resolved |
| `holdings_snapshot.py:837,845,847` | still reads `clf._ticker_map` / `clf._name_map` | S3 stays ARMED; IB-mr-291 `pending` |
| `shared-infra/main.tf:402-407` | PutItem/UpdateItem/BatchWriteItem on both `bd-securities` and `etf-classifications`, last touched 2026-06-16 | W6-S2 stays ARMED |
| `git rev-list --count` after fetch | origin 1,460 ahead of local CLOUD; local 260 ahead of origin | W5-S3 stays ARMED, owner `0.0.0_AB_MSTR` |
| `dynamodb scan --select COUNT` | 2,309; `begins_with(ticker, 'CUSIP:')` 0 | no served act this round |

## Rows: 9, all compiled (plus S2 carried from REMEDIATION_v1, still OPEN)

| row | disposition | basis |
|---|---|---|
| S3 (ARMED) | graduated to 2.0.0_SA_COO~M | the thread drain broke IRPT_BCKEND's Holdings producer import; no Holdings mint from CLOUD until IB-mr-291 |
| W6-S2 (ARMED) | graduated to 2.0.0_SA_COO~M (AE-lane order) | the unconditional bd-securities PutItem lives in shared-infra, shared with partners-lambda-role |
| W5-S3 (ARMED) | graduated to 0.0.0_AB_MSTR | the two trunks have diverged 1,460 / 260 |
| W5-S2 | graduated to 1.0.0_SA_CTO, INERT | one token, two enums, two schemas |
| W4-S2, W5-S1, W5-S4, W6-S1 | dismissed, each verified at HEAD | see the table above |
| W4-S1 | dismissed | a named population substitution; the like-for-like figure is the gold row count |
| S2 (v1) | stays OPEN | cottonwood now has a ticker-keyed source (held 1,113); inflection is still 2026-08-07 |

## On the seven halves waiting for signature

They are COO+CTO halves; this seat signs none of them. Two conditions from this compile bear on them:
- **E18_IAM** must not be signed on "bd-securities PutItem removed": the grant is in `shared-infra/main.tf`, untouched
  (W6-S2). The half is true of `bd-pipeline/iam.tf` alone.
- **BD_THREAD_R2** is measured after the backfill (1,822 unclassified of 524,413), which meets the condition this seat
  set at round 1. But S3 means the same library change that the thread ships has already broken another project's
  producer on CLOUD; the thread release and IB-mr-291 should land in one window, or the Holdings re-mint is blocked
  from the moment the thread is served.

## What you should have asked but did not

- **The contract moved from v0.1.0 to v0.2.0 without an L4-R re-sign.** C-FIELD and C-WRITER changed (a new field, two
  new enum values). CLAUDE.md rule 27 says an L10 addendum re-opens the half it changed; a wording change under the
  section hash does not. A new field and two enum values are not wording. This seat holds that the ratified-text half
  of MDPF_SECCLASS v0.1 no longer describes the contract in force, and asks the CTO for the addendum to sign.
- **The origin divergence is a fabric hazard, not a worker's.** W5-S3 was found because a coordinator told a worker to
  build on a commit that exists only on origin. Every seat on this device reads a CLOUD that origin has not seen for
  260 commits, and origin holds 1,460 this device has not seen. Until `0.0.0_AB_MSTR` integrates, any "on origin" claim
  in this fabric is untrue, and a cross-device relay of a commit hash is a trap.
- **The one genuine reader risk in e9's census.** `seed_bd_securities.py` copies every etf-classifications row into
  bd-securities unconditionally. If CUSIP-keyed rows land first, the fork gains 349 rows it never had; the issuer's
  release-sequencing item 1 is right to guard it first.

-- 3.0.0_SA_CVO
