# CTO ROUND-5 ANALYSIS -- IRPT_ANLREQ workstream Y -- answering the round-4 (Y) L10 slug (2026-10-11 ~12:0xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/remediations/REMEDIATION_v4.md`
@e41eab5325 (3.0.0_SA_CVO msg 4866). **Prior:** the round-4 analysis (committed with tick 9's log @9da283e89f).
**No PRD addendum.**

## 1. Where the workstream stands

Nothing built in rounds 3 or 4 is live on the service. Release 5 was live for 61 minutes (10:25:40Z to 11:26:53Z) and rolled
back because the portal's history reader on PROD refuses its answer. The reader that takes both answers is on portal DEV
`8ed372cb`; PROD reads `37aa1247ee`. FWD-1's journey has not run end to end.

## 2. Row D2-S48 (owner this seat): who met the refused history view

**Measured by this seat at ~12:0xZ**, one `filter-log-events` on `/aws/lambda/irpt-status` over the window, 688 events:

| measure | value |
|---|---|
| invocations (START lines) | 191 |
| structured events | 110: 55 `irpt_internal` and 55 `irpt_error`, in pairs |
| error events naming `analysis-request-history` | 6, every one `NOT_FOUND` |
| invocations with no structured event | 136 |

**What this does and does not say.** The function logs an operation only when it REFUSES. A history read that succeeded, the
case the PROD page would then refuse, writes no line that names its route. So the count asked for is **NOT MEASURABLE from
this log**: it is at most 136 and this instrument cannot say how many of those were history reads, or whose. The 6 `NOT_FOUND`
lines are refusals by the service, a different event.

Much of the 191 is seats' own traffic in that hour (the laptop applier's after-reads, the appliers' R8 controls, the
TCKT_VNEXT precheck and census); none of it is separable here by caller.

**Not yet read, and where the answer may be:** an API access log carrying the route and the caller's class, if the gateway
keeps one for this API. 2.0.0_SA_COO~P2 states whether one exists and, if so, counts history-route 200s in the window by
caller class (internal sign-in, firm sign-in, service). **This seat does not decide whether anyone is told until that read
is in or is shown impossible.** If impossible, it says so to Andrew as an unknown, with the window and the page.

## 3. The slug's other items

**"Exercised" was measured at the service, not at the consumer.** Accepted, and it is this seat's own finding of the same
miss (the record appended to the release-5 half @b54f838d09). The re-release's pair carries, as named after-reads: the PROD
page's reader given the live answer (the reader's own function run on the fetched body), and one rendered read of the
history view through the managers. A pair without them is not signed.

**Nothing from rounds 3 or 4 is live.** The issuer asked whether the project goes to `/closer` (msg 4857). Ruled in msg 4860:
the read-only trace first, which needs no word; the closer is carried to Andrew on that table if the trace shows hops no
lane is building.

**Rows:** D2-W51-S6 and S7 are DSGN_IRPTV1's by msg 4797. D2-S39 is IRPT_BCKEND's: the live bytes are identified (104 of 104
members matched) and the one-tree candidate is being built.

## 4. ENRICHMENT LIST for round 5 (ONE issuance, in this order)

1. **The FWD-1 trace table** (msg 4860): each hop live, built and not live, or no code, with its owner.
2. **The re-release packet for release 5, written and not applied:** the same build, the two consumer after-reads above, and
   its ordering condition stated as a measured read: `git ls-remote` of portal PROD names a commit that contains `8ed372cb`.
3. **The un-pin** of the two members in the map rides that release, not before.

## 5. Acts only Andrew can do

- The portal PROD push of the history reader (CLAUDE.md, Agent Autonomy: a client-facing page). Release 5 returns on it.

## 6. What this analysis did not measure

Section 2's counts are this seat's own. Everything else rests on the slug and the reviewer's read as filed.

-- 1.0.0_SA_CTO~DELL2
