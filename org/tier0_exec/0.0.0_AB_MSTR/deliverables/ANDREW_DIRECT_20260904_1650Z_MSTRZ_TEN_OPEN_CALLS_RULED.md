# ANDREW-DIRECT 2026-09-04 ~16:5xZ — all ten `/open-calls` cards RULED in one message

**Seat:** `0.0.0_AB_MSTR~Z` (site-Z terminal, spoken).
**Frame ruled on:** the 10-card `/open-calls` frame this seat delivered ~16:4xZ, built after
confirming nothing had been answered since the prior frame (no new Andrew-direct records, no inbox
rulings since 14:50Z).
**Status:** 10 of 10 ruled. Zero carried.

> **THIS FILE IS THE PRIMARY CARRIER OF THESE WORDS.** A bus frame quoting cards 2, 8 and 9 went to
> the laptop fabric at ~16:4xZ, ahead of this record, because that fabric was blocked on card 2 and a
> word that unblocks another seat should not wait behind bookkeeping. Its transcription of those
> three carries more of the spoken disfluency than the text below; the SUBSTANCE is identical and
> this file governs where they differ. Two carriers of one obligation diverge from the minute they
> both exist, so the primary is named here rather than left to be worked out later.

---

## CARD 1 — the egress-address list for the WordPress edge

**RULED: THERE ARE NONE — and source-restriction is the wrong control for this surface.**

> *"there are none is probably the best we can do at this time. The issue is that there are really
> just are no stable IPs. There are opal users who don't... who do not even come to the office. So
> it's just not really viable to approach it that way."*

**This is not a null answer, it is a design verdict.** The call was framed as "which addresses go on
the list"; the answer is that the population has no stable addresses to enumerate, because Opal users
include people who never come to the office. **Any control keyed on source address is therefore
measuring something that does not exist**, and would fail closed on legitimate users.

**CONSEQUENCE, which is larger than the card:** the `/wp-admin` derived allow-list must NOT be
applied, and the sentinel BLOCK arm, the partner allow-list and TO-OP-S-20/23 all rest on a control
their own population cannot support. Those need re-deriving on an axis that exists — identity, not
origin. Routed to `2.0.0_SA_COO~Z` and `1.0.0_SA_CTO~Z`; the re-derivation is theirs, not this seat's.

## CARD 2 — the second cross-fabric push window

**RULED: OPEN.**

> *"Yeah. I... that's that's fine. I I don't mind that."*

Sent to the laptop fabric immediately and ahead of this record. The reconcile runs
laptop-merges-first (site Z measured the three deploy-scope files as CLOUD's, which inverted the
proposed order); site Z's return leg follows at a ceiling it measures ZERO and states again in the
same breath as its push.

## CARD 3 — the opalinvest.com apex

**RULED: CONDITIONAL — AWS-only is fine, anything through GoDaddy/Patricia is declined.**

> *"if if there's possible to do things solely from AWS, then that's fine. But if we have to go and
> talk to Patricia and deal with stuff in GoDaddy that I don't have immediate access to, then, no, I
> don't wanna spend any time on that."*

⛔ **THIS RULING KILLS THE RECOMMENDATION THIS SEAT GAVE ON THE CARD, and that is recorded here
rather than quietly re-planned.** The rec was *serve on `www`, redirect the apex via GoDaddy
forwarding* — which is precisely the branch he declined. The Route53 alternative is no better: moving
the zone means changing nameservers **at GoDaddy**. Both routes for the apex terminate in the surface
he does not want touched.

**HONEST DISPOSITION: the apex is PARKED, not planned.** The condition he set is satisfiable for the
edge itself but not for apex DNS, and no AWS-only path to it exists that this seat can name. The
pending ACM validation CNAME is the same class and parks with it. The edge stays built and not
carrying apex traffic, which is already its state. If someone can show an AWS-only route, the
condition re-opens it without needing him again.

## CARD 4 — the trade-submission API credential

**RULED: KEEP.**

> *"I would keep it for now."*

Not retired. **The exposure does not close by itself and the ruling does not close it**: the
credential still needs rotating and moving into a secret store, which is now a task under
`1.0.0_SA_CTO~Z` rather than a question for him. "Keep" answers whether the surface lives, not
whether it is safe.

## CARD 5 — who owns the desktop fit of the daily report

**RULED: `0.0.0_AB_MSTR~Z` TAKES IT — and a new measured symptom came with the ruling.**

> *"You should take it. You just have to figure out how to, yeah, make sure that the desktop view is
> functional because it looks great on mobile. The mobile concept is great, but I opened it on my
> computer, and it basically kept the same shape. So that needs to be fixed."*

**DISCHARGED THIS TURN, @`63f77d0a56`.** The symptom was a regression this seat shipped this morning:
widening the mobile threshold to 1024px to catch tablets also caught mouse-driven desktop windows, so
his computer was served the PHONE page. Fixed by discriminating on pointer capability rather than
width; the desktop page was additionally a fixed 1180px slab with no media query, so correcting the
chooser alone would have moved him from the wrong page to a clipped one. 18 widths 640..1600 now
show zero horizontal scroll. **His existing link needs no replacement** — a presigned URL signs the
key, and the corrected chooser sits at the key he already holds.

## CARD 6 — the Azure billing-profile address

**RULED: MEASURE IT BEFORE CONCLUDING ANYTHING — he has already done work here.**

> *"I've already done a lot with this, and you can try checking into it and see if you can do
> anything… I already did the billing address and stuff. Somebody needs to look into that and see
> what status it's at… before making any conclusions."*

⚠ **THERE IS A LIVE DISAGREEMENT AND THE RULING IS THE INSTRUCTION TO RESOLVE IT.** `4.0.0_SA_CRO~Z`
measured the billing profile's `billTo` as not set, minutes before the card. He says he did it. The
most likely reconciliation is the distinction that seat itself drew — **the ACCOUNT (`soldTo`) and
the PROFILE (`billTo`) are different objects** and doing one leaves the other unset. That is a
hypothesis, not a finding. Routed to `4.0.0_SA_CRO~Z` to re-read the live profile and report STATUS,
with the explicit instruction that no conclusion is drawn until it is read.

## CARD 7 — the Azure account-type ticket

**RULED: BLOCKED ON LDT, and a fact this seat did not have.**

> *"I actually set up a developer subscription, but it's very unclear how to write a ticket, and it
> would appear that there's no way to send via API. So kind of waiting on little dog tech LDT for
> this."*

A developer subscription EXISTS — the card assumed otherwise. The block is not the subscription, it
is the absence of a route to file the ticket, and no API route appears to exist. **Genuinely external:
this stays blocked and no agent action moves it.** It is a real BLOCKED item, not a slipped one.

## CARD 8 — should a vendor-egress approval name the seat that will spend it

**RULED: NO — and the reasoning retires how this fabric has been treating the whole class.**

> *"I'm actually not really concerned about this at all. I've just never had an issue with the vendor
> egress… The issue is just about volume… it's good that we made something where there's always an
> ask for approval because then it's automatically a check or a balance on the subject. But generally
> speaking, the only case that would be problematic is if we downloaded a huge amount of information
> from Bloomberg or if we were doing something like very problematic with concurrent API hits for a
> data vendor or something. But other than that, and those two things have never happened, the vendor
> egress is really not a big deal."*

**TWO HALVES, AND THE SECOND IS THE IMPORTANT ONE.**
1. The clause is not added. The proposal is dropped.
2. **THE SOVEREIGN CONCERN IS VOLUME, NOT AUTHORIZATION BOOKKEEPING.** The named risks are a large
   Bloomberg download and concurrent hits against a data vendor; **neither has ever happened.** The
   approval-ask KEEPS ITS VALUE — he names it explicitly as an automatic check — but its value is the
   pause it creates, not a ledger of who spent which grant.

⛔ **STANDING EFFECT: no seat carries "we double-called a vendor" upward as a finding again unless
VOLUME is the actual issue.** Today's double-fire was two calls of trivial volume and is not the class
he cares about. Broadcast to both fabrics.

## CARD 9 — make a non-integrator push mechanically refuse

**RULED: YES, SCOPED TO ajb_workspace ON BOTH BRANCHES. NOT THE PORTAL.**

> *"I don't know about this. It's… I want to say yes, but I need… that only goes for AJB workspace.
> So that can go for site z AJB workspace and cloud AJB workspace. But the portal, like the dev ops,
> the zero point four point zero underscore DT, the DT agents, those need to be able to /prod-deploy
> the portal. They need to be able to deploy the portal. So, yes, I agree for AJB workspace, but not
> for the portal."*

⛔ **THIS NARROWS THE RECOMMENDATION THIS SEAT GAVE.** The proposal was unscoped and would have
blocked `0.4.0_DT` seats from `/prod-deploy` on the portal submodule — a working capability those
seats need. **The carve-out is part of the build, not a later fix.** Neither fabric has built this
yet; flagged to the laptop in the same frame as card 2 so whoever builds it builds the carve-out in
rather than discovering it when a DT seat is blocked from a deploy.

## CARD 10 — is `confirm` permitted on the BG data-refresh path

**RULED: PERMITTED.**

> *"Confirm is permitted. That's fine."*

This seat's gate reading stands. No change to `0.0.3_BG_BBGTerminal`'s fence.

---

## Disposition summary

| # | Ruling | Owner of the next act |
|---|---|---|
| 1 | THERE ARE NONE; source-restriction is the wrong axis | `2.0.0_SA_COO~Z` + `1.0.0_SA_CTO~Z` — re-derive on identity |
| 2 | Window OPEN | laptop `0.0.0_AB_MSTR` merges first — SENT |
| 3 | AWS-only or dropped | PARKED; no AWS-only apex route exists |
| 4 | KEEP | `1.0.0_SA_CTO~Z` — rotate + secret-store |
| 5 | MSTR~Z takes it | **DONE @`63f77d0a56`** |
| 6 | Measure before concluding | `4.0.0_SA_CRO~Z` — re-read the live profile |
| 7 | Blocked on LDT | external; no agent act moves it |
| 8 | NO clause; the concern is VOLUME | both fabrics — standing effect |
| 9 | YES for ajb_workspace, NOT the portal | unbuilt; carve-out is part of the build |
| 10 | PERMITTED | none; reading stands |

**Two of the ten rulings correct recommendations this seat made** (3 and 9). Both are recorded as
corrections rather than re-planned quietly, because a rec that was declined and a rec that was
narrowed are the two shapes most likely to be executed as originally written by whoever picks them up.

Push state: stated at the push in the same window.
