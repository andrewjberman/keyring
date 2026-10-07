# ANDREW-DIRECT 2026-10-07 ~06:5xZ-07:4xZ at the 0.0.0_AB_MSTR~DELL2 terminal -- dell2 seating, the CTO and COO loops, the manager's arms

**Channel:** typed at the `0.0.0_AB_MSTR~DELL2` terminal on dell2 (tailnet dell2), except where a relay is named.
**Recorded by:** `0.0.0_AB_MSTR~DELL2`. **Why this file exists:** laptop `1.0.0_SA_CTO` lands LIVE_ARMS rows from a record it can
read (CTO_RULINGS_FOR_THE_DELLS_20261007_0740Z.md ruling 4). The words below were typed here and existed nowhere in git.

## 1. The session handoff (pasted by Andrew as his first message, ~06:5xZ)

Andrew pasted the previous dell2 manager session's handoff as the new session's opening message. Its STARTUP list, VERBATIM in part:

> "4. /git-pull loop (15 min, ff-only, covers ajb_workspace CLOUD + portal DEV + opal_ai DEV). Use the hardened
>  body: export GIT_TERMINAL_PROMPT=0 GCM_INTERACTIVE=never, `timeout 120 git fetch`, report FETCH FAILED/BLOCKED
>  by rc."
> "5. Taildrop monitor (tailscale file get --conflict=rename ~/Taildrop every 5 s + watch ~/Downloads) -- Andrew sends
>  credentials this way. Report name+size only; never print a secret."

and its STANDING DIRECTIVES: "Credentials arrive by Taildrop; Taildrop monitor is a standing arm at launch on this box."

Armed by this seat as session Monitors: the fast-forward pull loop and the Taildrop receive monitor.

## 2. /govern 60m (relay of Andrew-direct at the 0.0.0_AB_MSTR~DELL1 terminal, ~07:10Z)

Bus 900b6ce0 from `0.0.0_AB_MSTR~DELL1`, VERBATIM: "Also tell DELL2 to run the same /govern loop that you are running, with verbatim
text and same 60m interval." The loop text, VERBATIM: "/govern [60m] <Manage your local fabric and keep in touch with the managers
across the other devices. The cloud-local device is the cluster's control plane who you refer to for assistance as needed.>"

Armed by this seat as a session cron, hourly.

## 3. The dell2 CTO and its /self-drive (~07:14Z)

VERBATIM: "I just brought CVO online to handle the surprise channel/investigations of the projects your COO spawns will be
undertaking. Bring on a CTO with instructions to /self-drive the projects of the COOs you spawn, 60m interval, with instruction to
manage adjudications for open calls."

Seated: `1.0.0_SA_CTO~DELL2`. Its own arming record is @66a57498d9. "The projects of the COOs you spawn" is, at this record:
IRPT_CUSTDY, IRPT_BCKEND, ADVI_COTBKF, IRPT_YCDGEN, IRPT_DASHBD.

## 4. The dell2 COOs and /canonical-drive (~07:16Z)

VERBATIM: "I also recommend that when you bring on the COOs, they should have /canonical-drive on their respective projects."

Seated on dell2, each told to run /canonical-flow then /canonical-drive on its own project. He named no interval.

| Serial | Project | Seated on |
|---|---|---|
| `2.0.0_SA_COO~K2` | IRPT_CUSTDY | relay of 1.0.0_SA_CTO msg 106023 (bus d186faa0) |
| `2.0.0_SA_COO~C2` | ADVI_COTBKF | same relay |
| `2.0.0_SA_COO~P2`, `~Y2`, `~M2` | IRPT_BCKEND workstreams P, Y, M | same relay; record 85c7ee8c99 |
| `2.0.0_SA_COO~G2` | IRPT_YCDGEN | 1.0.0_SA_CTO msg 106011 (bus b8f8ecba) |
| `2.0.0_SA_COO~D2` | IRPT_DASHBD | same |

"Recommend" is recorded as written. This record does not convert it into an order; the COOs and the LIVE_ARMS writer read it.

## 5. Defender (~07:3xZ, for the record only; no arm)

VERBATIM: "Keep an eye on this antimalware executable service from microsoft defender. It is taking up a dominant amount of cpu and
I am not sure that is in our best interest." This seat armed a session Monitor sampling MsMpEng CPU each minute.
