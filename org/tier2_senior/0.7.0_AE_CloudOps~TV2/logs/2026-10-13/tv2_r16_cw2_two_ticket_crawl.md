# Two cottonwood test tickets closed by a browser crawl -- 0.7.0_AE_CloudOps~TV2

**Date:** 2026-10-13
**Task Order:** TCKT_VNEXT.TO-RUN-R16-cw2.close-two-cottonwood-test-tickets-by-crawl-dell2
**Status:** COMPLETE for the act; the order stays `pending` because its AC1 check fails on its own defect (below)
**archetype:** DEPLOY

---

## Objective

Close `TCK-20261009-a1052909` and `TCK-20261012-13cd3a1d` by CLAIM then COMPLETE pressed on the Ticket Center board, signed in as one
synthetic cottonwood-listed identity that exists for the sitting only (Andrew's card 7, pair R2_CW1_CRAWL_PAIR.md plus amendments 1 and 2,
CTO half @4fea908a37 and @02234ccce1).

## What happened

- **Step 0:** ledger entry opened first. Census 50 of 50 worktrees (835 rows, 137 blobs); 5 blobs name the ticket tables, each in one old
  worktree HEAD only, all 5 trunk ledgers CLOSED, so stale branch copies, not a STOP.
- **Condition 1:** live `opal-ticket-api` CodeSha256 `4sDK8P5m...` equals the source-map digest; the downloaded zip's one member equals the
  tree file and the HEAD blob.
- **Sitting 1 (12:54Z, ET 08:54):** STOPPED at the board tab before any write. The tab was found in 0.4 to 0.5 s in every later run; I
  did not find why it was missing at 12:54:41Z (my script had no wait and no diagnostics). Both tickets read `open`; the row was deleted
  after exp and read ABSENT. Reported first to `2.0.0_SA_COO~V2` (msg 6920).
- **Amendments:** the CTO signed one second sitting (blob `b172afe6c4`). I added a sign-in wait, diagnostics, a re-read before the first
  claim, and a `--dry` mode that drives the live page bundle against a mocked backend; it passed before the second token existed.
- **Sitting 2 (13:08:28Z to 13:20:33Z):** both tickets `completed` under the identity, four page-made writes all HTTP 200, mail token
  `WE_CLIENT_SEND_FAILED` for both, row deleted 13:20:33Z after exp 13:20:28Z, ConsistentRead ABSENT. Card-1 ticket `open`, untouched.

## Findings the issuer should read

1. **AC1 as written cannot print CW2-OK.** `aws dynamodb get-item` prints nothing (rc 0) for an absent item; the check calls `json.loads` on it
   for the identity row. A scratch copy with one changed line prints CW2-OK. I did not edit the issuer's file.
2. **The zero-call read is zero by absence of traffic.** The data-refresh log group's newest event, from any caller, is 2026-10-12T19:00:06Z;
   no stream has an event in the window. The identity string has 0 matches over all 447 streams. The filter itself is sound (134 caller-address
   lines found). The first pass of my script reported 0 streams, which is VOID; the result file keeps it beside the corrected block.
3. **The pair's positive control cannot run:** the ticket log never carries the actor address.
4. The page makes unrelated reads (five advisor-intelligence GETs, portal-content, an analytics POST). The context aborted them; the identity's
   writes were exactly the four named routes.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg x6, close | PASS | entry CLOSED, all legs proven |
| proof-of-spec-check.py | instance | PASS | VALID rc=0 |
| comp-find | host string lookup | PASS | found the prior crawl scripts |
| comp-rail | three denials on piped or multi-path greps | WARN | each named the right comp-find form |

**What worked:** a dry run of the real script with a mocked backend; the ledger tool's leg proofs.
**What failed:** my sitting-1 script (no wait, no diagnostics); the first-pass zero-call denominator; the issuer's AC1 on an absent item.
**Gap found:** no tool reads a Lambda's log for an actor address when the Lambda never logs one.
