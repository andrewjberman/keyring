# Andrew-direct 2026-10-13 ~17:4xZ (laptop, 1.0.0_SA_CTO terminal) -- the seven positioning calls answered; an implementation artifact; clickable paths law

Answering the seven calls in `RULING_20261013_173xZ_CLUSTER_POSITIONING_ON_THE_PIVOT_AGGREGATE.md` @f469cb665f, section 3.

## VERBATIM

> "1.) Rec approved. 2.) Yes, rec approved. 3.) I already did this regarding turning password login off. Regaridng local laptop
> account for key login, we can deal with this another time. 4.) I do not know what these items are, and mockadv is almost
> certainly deprecated/useless/not displayed anywhere. 5.) We can use anthropic path, that's fine. 6.) Yes that is fine, it is
> loading quite quickly for AMGT already but worth exploring the individual security pulls. 7.) I need to know what you mean by
> this. Anyhow, beyond this I want to see an artifact generated for how you are going to implement the plans for the various
> MACROS/workstreams. I also want a link to your full plan that is clickable. I also want you to update claude.md in a manner that
> whenever an agent posts a path, it must be ctrl+click accessible."

## Applied

| # | call | answer | route |
|---|---|---|---|
| 1 | Ticket Center service principal on the C-SWITCH allow list (ticket-filed requests only) | APPROVED | dell2 `1.0.0_SA_CTO~DELL2` -> IRPT_YCDGEN `~G2` |
| 2 | synthetic partner-firm advisor drives the end-to-end test, in place of call `2e30` | APPROVED | dell2 -> IRPT_ANLREQ `~Y2` (never-widen pair for the mint and the delete) |
| 3 | tailnet password login off | DONE by Andrew. The laptop local account for key SSH is DEFERRED ("another time") | NFRA_CTLPLN FWD-27: the password-off arm is to be read back by the round-12 SSH cell; the laptop arm stays GATED, deferred |
| 4 | ADVI_FIRMBKTS DEC-12/13/14 | NOT ANSWERED: Andrew asked what they are. `mockadv`: he reads it as deprecated and displayed nowhere | the CTO explains the four items; the `mockadv` REC changes to RETIRE the alias after a consumer census reads zero |
| 5 | AMGT AI fill provider | the existing Anthropic path | dell1 -> AMGT_RESAPP addendum |
| 6 | AMGT first-load target | under 3 s APPROVED. He adds: pages already load quickly; explore the individual security pulls | dell1 -> AMGT_RESAPP: a per-name pull census (what each of the 93 names pulls, and how long) |
| 7 | "templates sent last week" | NOT ANSWERED: Andrew asked what is meant | the CTO explains: the IRPT_CUSTDY-built 49 Financial client report template (portal DEV fd345aef), or files the firm sent (a mailbox search found none) |

Two further asks:
- **An Artifact** showing how the plan is implemented per macro and workstream, plus a clickable link to the full plan. Owner:
  `1.0.0_SA_CTO`.
- **A CLAUDE.md law:** every path an agent posts must be ctrl+click accessible. Owner: `1.0.0_SA_CTO` (law edit: commit, a
  same-turn broadcast, and the push state).

The positioning in the ruling is taken as accepted: Andrew answered its calls and asked to see how it is implemented.

## Addendum ~17:5xZ-18:0xZ -- full-text delivery, site Z held, muse into the ~CA plan

VERBATIM (three messages at this terminal):

> "ALso i just looked through your doc here, this all makes sense, however it is a very thin document. I think it is important
> that the MSTR/CTO agents at the various boxes get the relevant transcripts and direction in full rich capacity versus solely just
> a light little directive, as I want to make sure these things are all done completely and correctly as I dictated."

> "Ok make sure that the broadcasts go out to the relevant MSTR/CTO agents across the boxes with the necessary information, not
> solely some ultracompressed/lossy directive. It is ok to summarize for a <150 word message or any associated threshold, but they
> need to have full rich text in the form of the relevant transcript source files as well as the various findings if they should
> need to review for whatever reason."

> "Sitez is going through a reboot right now so I would hold off on that one until I give you the go so it does not fall through
> the cracks, DELL1 and DELL2 however are good to go. Beyond that, make sure that the pivot info regarding muse as a replacement for
> the COMM_ASSIST kimi agent is worked into the COO~CA plan on this box. COO~C and COO~DV are already working, I do not know how
> much new information they really need"

Applied:
- One full direction packet per box under `PIVOT_DIRECTION_20261013/` (verbatim transcripts, findings, rulings, outcomes, first
  acts). Each box's CTO and MSTR receive it as a crossbox ORDER whose body is the packet. The bus line is short; the substance is
  the committed file plus the CRO's committed sources (`VOICE_MEMOS_20261013/`, transcripts and alignment reports).
- dell1 and dell2: sent now. **site Z: HELD until Andrew's go** (reboot). Its packet is committed and waits.
- `2.0.0_SA_COO~CA`: `DIRECTION_COO_CA_COMM_ASSIST_MUSE_20261013.md`. `~C` and `~DV` get no new direction; the laptop packet is
  available to them as reference.
- Correction carried from the dell1 packet: call `e7f2` is a whole-DEV promote that also carries client-facing changes. The
  Security Analysis promote is therefore a feature branch cut from the last PROD release under NFRA_DEVPLN, approved by the dell1
  CTO as an Opal-internal page. It is not a promote of DEV as a whole, which stays held until NFRA_DEVPLN lands.
- Correction carried from the dell1 packet: `mockadv` is a live test tenant (`data/firm_registry.json:88`, "Mock Advisor (test
  account)"). Retiring it waits on a census of its consumers that reads zero.

## Addendum ~19:0xZ -- site Z released

VERBATIM: "Furthermore, SITEZ is now coming back online, so it is now time to send them their pivot docs + transcript(s) so they
can get started on that strategic pivorts"

Applied: the site Z hold is lifted. Two crossbox ORDERs carry `DIRECTION_SITEZ_20261013.md` (@4e963d4a12) to `1.0.0_SA_CTO~Z`
and `0.0.0_AB_MSTR~Z`; `0.0.0_AB_MSTR` sends them on the bus.
