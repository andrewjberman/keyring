# ANDREW-DIRECT 2026-10-19 ~18:4xZ -- cluster priorities, one box at a time (coherence)

Given at the laptop 1.0.0_SA_CTO terminal, after he sat at each box 14:10-14:30 ET (18:10-18:30Z). VERBATIM:

> "We have a lot going on across the various boxes and we need to tighten up and gain coherence. Accordingly I am going to describe to you
> what is happening across the various boxes via me sitting at each one of them over the last 20 minutes or so from 14:10-14:30 ET.
> Starting with DELL1, the highest priority projects that this box is working on currently is figuring out how to structure an
> auto-fidelity uploader in the same infrastructure form as we built for the auto-schwab uploader. Once this is done, we are going to need
> to test it for a few days as well as figure out how to run a full backfill and what that backfill looks like and how far back it goes.
> Depending on the content of this backfill, it may provide a meaningful solution for the struggles we've been having trying to figure out
> Cottonwood account performance through Black Diamond. Ideally we can figure out performance reporting direct from Fidelity for all
> Alongside accounts that come through there. Important to note here that Alongside is the RIA under which 49 Financial, Inflection Wealth
> Management, Cottonwood Capital Advisors, and many others sit. As a result this Fidelity solution (and eventually a potential FTP solution
> as researched on this box by CRO) could be the way we finally get rid of Black Diamond. Moving along to DELL2, the issue with this box is
> that there were numerous unmerged worktrees that were causing chokes all along the system. As a result, I have halted all work on that
> box until these various workstreams are merged and otherwise drained, because we need to know the true state of the ticket center,
> particularly the analysis request flow, but also the trade and meeting request flows. Beyond that, the DELL2 box is also responsible for
> all the work going into the Performance Reporting tab on the INvestor Reporting page of the opalinvest.dev portal. We currently only have
> 49 Financial on a regular, functioning schedule for performance reporting. Cottonwood performance reporting is failing big time because
> we are duplicating transactions somehow, the bug for which has yet to be identified. Ideally, the Fidelity solution will render all this
> black diamond work moot and we can just pull the performance reporting or at least the clean fact table data for Cottonwood and others
> direct from there instead of having to mess around with Black Diamond at all. Moving from there onto SITEZ, this box is currently working
> through the opalgateway server. We need to start testing this and optimizing it for Opal users, and that is their principal priority.
> Finally back to laptop here, we are just working as a control plane and loosely doing some research here and there, nothing serious to
> report."

## The picture, one line per box (his words compressed; nothing added)

| Box | Principal priority | Then | State he set |
|---|---|---|---|
| **dell1** | NFRA_FIDUPL: the auto-Fidelity uploader, built in the same infrastructure form as the auto-Schwab uploader | test it for a few days; design the full backfill (what it holds, how far back) | highest priority on the box |
| **dell2** | drain: merge every unmerged worktree and workstream, so the true state of the Ticket Center is known (Analysis Request first, then Trade and Meeting Request) | the Performance Reporting tab on Investor Reporting (opalinvest.dev) | ALL NEW WORK HALTED until drained |
| **sitez** | the opal-gateway: test it and optimize it for Opal users | (the larger-EC2 move, his ~18:3xZ word) | principal priority |
| **laptop** | control plane; light research | -- | nothing serious |

## The thread that ties them (his reasoning, stated once)

- **Alongside is the RIA** over 49 Financial, Inflection Wealth Management, Cottonwood Capital Advisors and many others.
- **Fidelity direct is the route off Black Diamond.** First the dell1 uploader (NFRA_FIDUPL), then possibly the SFTP feed (NFRA_AWSFTP, laptop,
  on HOLD since his ~16:5xZ word until an FTP solution exists).
- **Cottonwood performance is the first payoff.** On dell2, Cottonwood performance reporting fails on duplicated transactions, cause not yet
  found. Only 49 Financial runs on a working schedule. "Ideally" the Fidelity data makes that Black Diamond work moot.

## What this record does NOT rule (relayed verbatim scope, never wider)

- It **does not stop** dell2's Cottonwood duplicate-transaction investigation. He said "ideally" the Fidelity route makes it moot, and dell2 is
  halted anyway; whether that bug is worked or parked after the drain is his call or dell2's CTO's.
- It **does not lift** the NFRA_AWSFTP hold.
- It **does not move** any directive or seat.

## Carried facts the boxes should hold together (measured from git, 2026-10-19)

- NFRA_FIDUPL is registered on dell1 (L2+L3 by 1.0.0_SA_CTO~DELL1, PRD v0.1 DRAFT). Its CRO research finds that **Wealthscape's Terms of Use
  prohibit robots and agentic AI without Fidelity's approval**. That is a gate on the uploader's design and possibly Andrew's to clear with
  Fidelity. It is the same question NFRA_AWSFTP's held brief asks about the direct feed.
- The two Fidelity routes must land in the same place. NFRA_AWSFTP's endpoint (FWD-6, FWD-8) and NFRA_FIDUPL both write Fidelity data for
  Alongside's firms, so one landing home and one per-firm split should serve both, never two.

-- 1.0.0_SA_CTO (laptop)
