# Never-widen, CVO half -- OG-rl-12, opal-gateway release r26 -- SIGNED (3.0.0_SA_CVO~Z, 2026-10-07 ~11:0xZ)

**Ask:** `2.0.0_SA_COO~O` msg 30814,
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-12_20261007.md` @4d9d1208af.
**Why this seat:** `1.0.0_SA_CTO~Z` ruling msg 30780 (`3.0.0_SA_CVO~O` is not live).
**Release sha this half binds to:** `feddb372443adbcf139febab35b69f109e49b664`, on live `240ac2fe5a`.

## SIGNED, for the act the ask's section 2 names and nothing wider

The act may touch: the 5 host files of the release, and the manifest's `deployed_commit`. Rollback per key: redeploy
the rollback tree at `240ac2fe5a`, which restores every one of them.

## What this seat read itself (CLOUD @f00567cd5f, ~11:0xZ)

1. **The release is one commit on live.** `git rev-list --count 240ac2fe5a..feddb37244` = 1; its parent is
   `240ac2fe5a`.
2. **The file set is 10, all in the gateway tree.** `git diff --name-only 240ac2fe5a feddb37244`: 10 files, 0 outside
   `infra/aws/ec2/opal-gateway/`. `git diff --name-only feddb37244 HEAD` on that tree: the CLOUD-only runbook, alone.
3. **The route's 4 files are the bytes I pre-read.** Each release blob equals its blob at `f7f2cb7c2e` (4 of 4). I
   read those hunks whole at 10:0xZ: day and fund are validated before the key is built; the Route line sits after
   `/audit` and before `/rivalfunds/{day}`; one S3 read; no write beside the audit line.
4. **The allowlist diff is one row.** It adds `opal_data_refresh_status` for the one scoped identity, not
   client-qualified, plus its comment. I read Andrew's record
   (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_041xZ_CONCIERGE_MAY_CALL_DATA_REFRESH_STATUS_TOOL_YES.md`):
   "rec approved", applied as one allowlist row for that one tool. The row is that and no wider.
5. **The id check ships in the same release as the row.** `integration.py` at the release sha: `_check_execution_id`
   (fullmatch `[A-Za-z0-9_:-]{1,200}`) runs before the status GET in the tool and inside `_read_status_once`. A slash
   or a dot cannot pass. This is the term row Z-S65's remediation set (REMEDIATION_v11): the wider caller set does not
   land without the check.
6. **The dedupe change, read whole.** The signature is (name, size, hash). With a hash unreadable on either file the
   lookup is skipped and the send fires. The record has one writer (:377) and one lookup (:322).

## What this seat did NOT read, and takes from the ANNOUNCE

The host runs (md5 97 of 97, the BEFORE and REHEARSAL table, the route arms), the test counts (626 passed, 7 failed,
0 new), the rollback tree's equality to the live artifact, and the two `rl12` check exercises. None was re-run here.

## Both branches of each named property, as this half covers them

- **Which tools the concierge may call.** Expected: the status tool admitted; a tool nothing names denied. If either
  reads otherwise after the act: roll back.
- **Which ids reach the status path.** Expected: a malformed id refused with 0 requests; a well-formed id read as
  before. If a well-formed id is refused, the daily send's status read breaks: roll back.
- **What the chart route returns.** On release day live data can reach only the 404 branch (0 chart objects). The 200
  branch rests on in-process tests. If `/rivalfunds/{day}` or `/audit` change status, size or digest: roll back.
- **Whether a re-send fires.** Identical content: no second trigger. Same size, different content: fires. Hash
  unreadable: fires. The third branch means a retry after a dropped transport can trigger twice; the caller texts
  already say to read the status tool before any re-send.

## Conditions

1. All three preconditions of the ask's section 4 hold before any act; live is re-read first and the release is
   re-cut if it moved. A re-cut is a new sha and this half does not carry to it.
2. The post-act record shows, from the installed code: the concierge admitted for the status tool, 0 unnamed tools
   admitted, consent 9, tools 66, a refused id making 0 requests, and the four route arms on their values.
3. Row Z-S65 advances to REMEDIATED only on that installed-code read of the refused id.

## Limits accepted, each already disclosed

- The dedupe has never run against a real send or a real `file.hashes` shape. Its first live exercise is a real
  corrected re-send.
- The route arms ran in-process on the host, not through the ALB (row Z-W28-S6).
- The concierge's token still carries its earlier 17 scopes (row Z-W28-S11, open at the CTO).
- **Row Z-S64 is open at the CTO and this release widens it:** the chart route writes an audit record whose day, fund
  and route are dropped, like the three rivalfunds routes before it. That is not a ground to withhold this half; it
  is one more route the ruling has to cover.
- Row Z-W28-S17 (older committed files carrying the Schwab master account id) is outside this release. It is new to
  this seat and unread; it is owed a disposition at the round-25 slug.

-- 3.0.0_SA_CVO~Z
