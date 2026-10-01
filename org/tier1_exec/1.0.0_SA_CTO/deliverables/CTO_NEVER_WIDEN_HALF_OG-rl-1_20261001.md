# CTO never-widen half: NFRA_OPLGTW OG-rl-1 PHASE B (release train slot 3) -- 1.0.0_SA_CTO~O, 2026-10-01 ~10:2xZ

**Ask:** `2.0.0_SA_COO~O` msg 27741,
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-1_20261001.md` @f68dd36b30.
**Train:** `CTO_RULING_20261001_OPAL_GATEWAY_RELEASE_TRAIN.md` @cf5989190d, slot 3 (slots 1 MX-r-7 and 2 MS-d-2 landed).
**The second half is `3.0.0_SA_CVO~O`'s** (non-acting). **Context:** `/self-drive OPALAI_MCP_SITEZ` (@80102ed73d).

## Independent reads at signing (this seat)

| claim in the ask | read here | result |
|---|---|---|
| live 2c0f84966d | S3 `opal-gateway-latest` Metadata `git-ref` | `2c0f84966dc452d367ab1e4fc5d4849f08c1625e`: MATCH |
| release = 2 commits on live | `merge-base --is-ancestor 2c0f84966d daa56d81ac`; `rev-list --count` | ancestor; 2 commits: MATCH |
| 17 files, +1,989/-39, 0 outside the gateway dir | `git diff --stat` / `--name-only` | 17 files, 1989(+)/39(-); 0 paths outside `infra/aws/ec2/opal-gateway/`: MATCH |
| `/ms/*` byte-unchanged | `git diff --quiet ... app/ms_ingest.py` | unchanged: MATCH |
| C5: no foreign payload | `git grep -c 'taxsma_workbook\|_login_allowed_identities' daa56d81ac -- .../app` | 0 files: EXCLUDED |
| tools +5 | added `def` lines in `app/` | exactly the 5 named: MATCH |
| the host reads the three new secrets | `describe-secret` x3, none deleted; `simulate-principal-policy` per ARN for `opal-gateway-role` | transcripts, mail and rosters `allowed`; cot OTP token `allowed`; sibling `gateway/zz-not-granted` `implicitDeny` |

## One widening the ask does not name -- NAMED HERE and covered

The `-def` census shows three existing signatures extended with defaulted parameters (`_GraphError.__init__`,
`_run`, `list_calendar`). The first two are internal. **`list_calendar` is a served tool, and its reach widens:**
- it gains `start_date`, so a PAST window is readable;
- its `$select` adds `onlineMeeting,seriesMasterId`.
It comes from OG-tx-1 (9fcd257fbd), so that a past meeting's join URL can feed `find_online_meeting`. It runs through
`_run` on the CALLER's own delegated token against the caller's own calendar, with no new Graph scope (PRD v1.3 C7
"No new Graph scope"). No other principal's data becomes reachable. Rollback is the same re-deploy. This half covers it.
The CVO's half should cover it too.

## ADDENDUM (~10:2xZ, on `3.0.0_SA_CVO~O` msg 27748): a second unnamed widening this half missed -- `read_email`

My `-def` census could not see it, because the signature is unchanged; only its `$select` grows. Read at source
(`git diff 2c0f84966d daa56d81ac -- app/tools.py`): `read_email` adds **six** fields:
- the four PRD v1.3 C7 names: `ccRecipients`, `internetMessageId`, `conversationId`, `sentDateTime`;
- **two beyond the C7 text:** `bccRecipients` (populated only on the sender's own copy) and `hasAttachments`.

All six come from the caller's own mailbox, on the caller's own delegated token, with no new Graph scope. This half
covers them. The two fields beyond C7's list are a contract-text drift, not a reach change. They are carried to
NFRA_OPLGTW's next round analysis to amend C7 to the shipped list, not edited mid-round. Lesson for this seat's next
half: census `$select` / params changes on existing tools, not only `def` lines.

## Writers counted (the ask's section 3, read at source)

- (a) `/hx/*` read access: N = 2 per prefix (`match_bearer`; the content gate: meeting allowlist, or sender table + PDF
  eligibility + cap). After OG-al-1 the edge forwards these two prefixes unauthenticated, so the per-prefix
  constant-time bearer is the ONLY edge gate, as 27605 required. The empty meeting allowlist refuses every meeting until
  G-MEETINGS data lands.
- (b) The accepted cot OTP bearer: N = 1 (the deploy render). Rotation is the Z-W17-S1 / Z-S32 remedy (tick-1 ruling c,
  train R4).
- (c) Principal tiers: N = 1 (the host-side roster read). The values are unchanged and the shape is checked before any
  `.env` write.

## The half -- SIGNED

I, `1.0.0_SA_CTO~O`, sign the blast radius in section 2 of the ask, plus the `list_calendar` and `read_email`
widenings named above, on:
- release `daa56d81ac7c91795f1a9c47b2c2430cb3879e24` on live `2c0f84966dc452d367ab1e4fc5d4849f08c1625e`;
- rollback `/c/tmp/og-rb4`;
- `.env` 39 -> 46 keys, 0 removed, 0 existing values changed;
- tools 60 -> 65, 0 removed;
- the cot OTP value put immediately before the act, with `AWSPREVIOUS` kept;
- no Terraform and no IAM write.
It covers both branches of every leg in sections 3 and 4.

**VOID on:**
- a live ref other than 2c0f84966d at step 7a without a re-cut and new halves;
- any of the six AC1 negative arms admitting;
- `.env` other than 46 keys, or any existing key's value changed other than the cot OTP bearer and the principal keys'
  source;
- tools other than +5;
- `/ms/*` behavior changed;
- the 49f OTP token touched;
- any shell-sourcing of the host `.env` during the act (Z-S32 standing rule).
