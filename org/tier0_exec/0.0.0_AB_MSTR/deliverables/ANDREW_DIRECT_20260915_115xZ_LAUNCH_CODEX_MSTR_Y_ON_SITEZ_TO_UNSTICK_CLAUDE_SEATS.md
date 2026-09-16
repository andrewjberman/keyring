# ANDREW-DIRECT 2026-09-15 ~11:5xZ -- instantiate a Codex 0.0.0_AB_MSTR~Y on the site-Z box, and have it /unstick the Claude seats

**Seat:** `0.0.0_AB_MSTR` (laptop) · **Channel:** typed at this terminal, mid-turn, right after the promote GO (LD-0568) ·
**Recorded:** the same turn it was given.

## VERBATIM AND ENTIRE

> "Yes , i wonder if you can somehow instantiate a codex 0.0.0_AB_MSTR~Y on the sitez box. Could you remotely run ajb2
> launcher to the sitez box then have that agent read /unstick to see if Claude agents hit usage limit?"

## CONTEXT, measured

- `0.0.0_AB_MSTR~Z` has been silent on the agentbus since 10:27Z.
- Two laptop -> site-Z frames were still unread in its queue at 11:51Z (`ApproximateNumberOfMessages` 2). A third
  was added with the GO frame.
- Site Z's promised third characteristics re-serve had not landed by 11:51Z.
- Andrew's hypothesis: the site-Z Claude seats hit a usage limit.

## WHAT IT ASKS, READ NARROWLY

1. Instantiate a **Codex** seat `0.0.0_AB_MSTR~Y` on the **site-Z box**, by running the `ajb2` launcher
   (`.tools/ajb2.ps1`, the Codex peer of `ajb`) there, remotely from the laptop.
2. That seat reads `/unstick` (`.tools/unstick.ps1`, which finds a serial-titled terminal tab and peeks or keys it)
   and uses it to see whether the site-Z Claude seats are stopped at a usage limit.

"Yes" answers this seat's ~11:4xZ note (the 11:50Z GO cutoff, with the hold option): the GO stands.

## WHAT THIS SEAT MUST ESTABLISH BEFORE ACTING

- **A remote-execution path from the laptop to the site-Z box.** `/unstick` and `ajb2` are LOCAL tools (window focus,
  SendKeys, a local launcher), so they must run ON that box.
- **That the act stays inside what he asked:** one Codex seat, and a peek before any keystroke, per `/unstick`'s own
  diagnosis rule. `/unstick --peek` sends nothing.

The findings and the outcome are appended below as they land.

## FINDINGS, measured 11:5xZ-12:0xZ from the laptop

- **Two more Andrew lines followed, verbatim:** "I know that cvo~z on that box is codex and Alive" and "Not sure how to
  reach them".
- **Site Z is online on the tailnet:** `tailscale status` shows `opal-bloomberg` at 100.99.180.19.
- **There is no AWS SSM path.** `ssm describe-instance-information` lists 6 managed nodes, all EC2, and no site-Z node.
- **Only Remote Desktop is reachable.** A connect-only TCP probe to 100.99.180.19 read: 3389 (RDP) OPEN; 7800
  (broker), 22 (ssh) and 5985 (WinRM) closed or filtered.
  - So there is no command channel into site Z from here. The one open door is RDP, which is an interactive desktop
    under Andrew's own login.
  - 0.0.0_AB_MSTR~Z's 2026-09-10 briefing states the principle: "an agent should not be the thing that opens [remote
    access]".
- **The site-Z bus consumer stopped around 11:05Z.** SQS metrics on agentbus-ajbdev-laptop-to-sitez.fifo, in 10-minute
  bins: NumberOfEmptyReceives ~28 per bin, then 4, then 0 from ~11:05Z. The last NumberOfMessagesReceived was ~10:5xZ.
  - A consumer that stops polling while the process should still be running is consistent with a session that can
    take no turns, so it cannot re-arm its 30-minute Monitor. Andrew's usage-limit hypothesis fits.
  - It is not proven. Only a look at the tab proves it.
- **Consequence:** this seat cannot launch `ajb2` on site Z, or run `/unstick` there. Both are local desktop tools. The
  act goes to Andrew over RDP, with the exact lines this seat supplies.
