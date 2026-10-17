# SOC2_MSLOGS -- ROUND 1, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-17 ~06:1xZ)

**Input:** the `3.0.0_SA_CVO` slug (msg 7369), with `surprise-channel/adjudications/ADJUDICATION_v1.md` and `remediations/REMEDIATION_v1.md` @94d3a6ce41.
round-close-check reads MAY-CLOSE (graded 1, not met 1). **Also read:** `2.0.0_SA_COO~S1`'s drain-end packet
`org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_L8_DRAIN_END_PACKET_R1_20261017.md` @f842ea3a7c. The release ledger
`soc2-mslogs-r1-raw-switch-20261016` is CLOSED (10 legs, 9ad6102a36).

## 1. Graded

| FWD | Verdict | Read |
|---|---|---|
| **FWD-1** | **NOT MET, one act from REALIZED** | The thread is built and live: collection runs raw for every account (9,534 records over 8 dates, four feeds including the sign-in feed), silver is rebuilt, and the door (member v5, 10240 MB) returns whole records. Andrew's first read worked but could not say who acted. That read produced door amendment 2 (detail), and the enriched block reached him at 02:37Z. **Nothing records his read of it.** The criterion is his recognition, and no build closes it. |
| FWD-2..9 | not in round 1 | Round 1 built the thread only (spine v3.16). |

**The close path is an act only Andrew can do:** he runs the enriched block delivered at 02:37Z against his own account for one day he
remembers, then says in one line whether it shows who did what, from where and when. This is his own Microsoft 365 account and his
recognition, so it is on the cited act list. No round-2 cell waits on it, and round 2 proceeds.

## 2. What round 1 taught (issuer defects first, from the packet)

- **A Terraform cell without `terraform validate` let a dependency cycle through** (door versus collector). From round 2, every
  Terraform-touching cell carries `terraform validate` on a scratch copy of its root as a criterion. The issuer adopted this. It is
  standing practice for this project.
- **Collector timing defects** (starved derive, five-times re-invocation, cursor after derive) were fixed inside the round by c1
  amendments 2 and 3. The 10240 MB door is Andrew's word (00:55Z). Item 3 below removes the need for it.
- **Measurement:** the first blob estimate was made without paging (about 1,136 against about 9,500 real). The switch threshold was
  unaffected. The listing-pages-first rule (CLAUDE.md, put the control on the retrieval) applies.

## 3. ENRICHMENT LIST -- round 2 (ONE issuance by `2.0.0_SA_COO~S1`)

1. **The read client** (FWD-1's second half, and FWD-3/6 groundwork): fold the paging, detail-aware reader from the CloudShell block into
   `read_timeline.py`. Add the Desktop print-out option (CTO-carried,
   `ledger/CTO_CARRIED_ROUND2_DESKTOP_PRINTOUT_20261016.md`). Retire the stopgaps `derive_days.py` and `read_timeline_to_desktop.ps1` into it.
2. **Silver `client_ip` reads Exchange's `ClientIPAddress` as well.** It was blank on 4,307 of 5,000 rows of Andrew's first read. Then
   re-derive the 8 days. FWD-2 and FWD-3 depend on "from where".
3. **A memory-bounded (streaming) derive in the door,** so a busy day runs at a stated ceiling well under 10240 MB. Once the streaming derive
   is proven on the busiest of the 8 days, the memory comes down in the same release.
4. **The collector's async retry is set to `maximum_retry_attempts = 0`,** so a timed-out fire is never re-run on old code.
5. **The door's bronze prefixes come from `lib/opal_naming`** (row D1-W2-S3, graduated).
6. **Text:** README, RUNBOOK and main.tf comments drop the eight-account list, filter.py and the "unsubscribed sign-in feed" (rows
   W1-S1, W5-S1, W7-S1, graduated).
7. **FWD-2 (exposure) starts:** the `exposure` read through the door (what one account touched in a window) over silver, reusing the
   timeline reader. It is the first enrichment of the thread.

**Not cut, noted:** dell1's default AWS profile is the agent user, so a member's CLI read on dell1 needs Andrew's own named profile.
CloudShell avoids this. It goes into the read client's README as a usage line, not a cell.

## 4. Acts only Andrew can do (cited)

- **FWD-1 recognition:** one line on his read of the enriched block against his own account (his account and his recognition).
- **The FWD-3 and FWD-4 drills** (an unusual sign-in; setting then removing a forwarding rule): acts on his own account, needed by round 3
  or 4.

-- 1.0.0_SA_CTO~DELL1
