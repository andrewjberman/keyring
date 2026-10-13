# DIRECTION to 2.0.0_SA_COO~CA (laptop) -- COMM_ASSIST: muse replaces the Kimi/Quo text agent as Andrew's way of working the assistant

**From:** `1.0.0_SA_CTO` (laptop, COMM_ASSIST owner), 2026-10-13 ~18:1xZ. **Authority:** Andrew-direct ~18:0xZ at this terminal
(VERBATIM below), the records of ~14:3xZ and ~14:4xZ, and PRD v0.6 @e7bde907ba (ratified-text half SIGNED by `3.0.0_SA_CVO~L`
@08eb013f09). **Status:** binding on the COMM_ASSIST round-16 issuance and every later round.

Read sections 1 and 2 in full before you issue round 16.

## 1. Andrew's words, in full

### 1.1 Today ~18:0xZ (this terminal)

> "Beyond that, make sure that the pivot info regarding muse as a replacement for the COMM_ASSIST kimi agent is worked into the
> COO~CA plan on this box."

### 1.2 The laptop voice memo, this morning (complete transcript)

Source: `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/LAPTOP_OPS_TRANSCRIPT.md`
(file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/LAPTOP_OPS_TRANSCRIPT.md).
"news" in the auto-transcript is muse (his written word at ~14:3xZ).

> Now finally moving on to the laptop cloud dash vocal box and the expectations on what we're trying to do here. There are three
> projects that matter on the laptop box. They are CTLPLN, the control plane, they are the EVPLN, the developer plane or how we're
> going to manage the dev merges and the various box merges for the portal for the portals dev branch and prod branch. Finally the
> comms underscore assist how we are going to have a agent assistant that is helpful for me to manage all of this stuff. So control
> plane, CTLPLN, I think we're working through that, that's a decent space, DVPLN. We need to, I think we can figure that out today
> in one session that's not a big project that should be very, very simple to get implemented. Finally the comms assist. So the
> issue with this is that the kimi agent simply doesn't really have a harness, it's not really intelligent, it's very limited in
> its capability simply because we just haven't built it out that much and it's a little bit hacky to go through the QUO quow
> channel and doing all that. It's this very rigid and rickety. It's like so I think that there should be a way to handle this all
> through news and tailnet. So I think a big focus here is not only moving forward to the various control planes, CTL and DVPLNs
> but also establishing definitively tailnet ops throughout the cluster. We want to establish how tailnet works, we want to
> establish how news works, all of that needs to get done today.

### 1.3 ~14:3xZ (record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_143xZ_DEVPLN_RECS_APPROVED_AND_COMM_ASSIST_THROUGH_MUSE.md`)

> "I also think that we should ultimately aim to set up COMMS_ASSIST in a manner that I can handle most of it through "muse" on
> tailnet. Muse does not have AWS CLI, which means that information needs to be placed somewhere it can read, I think this can be
> hosted on DELL2 somewhere local on the device, maybe DELL2 has some kind of script that pulls open-calls and other summary info
> from AWS that muse would need on some local schedule to DELL2 local for muse to access through SSH. The issue is that Muse is a
> lot more user friendly/intelligence than Kimi, because the Quo-phone line approach is a little rigid and unintelligent compared
> to coming up with a muse-focused solution, so I also want to figure out how to wrap COMMS_ASSIST into a muse-friendly solution
> based on the work we're doing with the tailnet already and so on"

### 1.4 ~14:4xZ (record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_144xZ_MUSE_DECISIONS_AND_COMM_ASSIST_TO_LAPTOP.md`)

> "Regaridng your four decisions let's go through one at a time: 1.) Yes that's fine, we'd need to asssess how fallbacks work in
> practice and that would be dependent on muse efficacy, because fallback may no longer be necessary if muse is highly effective.
> 2.) Yes agreed. 3.) This is fine. 4.) Yes this is fine. Furthermore, is COMM_ASSIST being handled on this box? I think it should
> be if it is not already. I want this box handling CTLPLN, DEVPLN, and ASSIST, because I need to be overseeing them directly."

The four decisions he answered (brief `docs/briefs/comm-assist-through-muse-midstream-brief-20261013.md` @0ecb2dd97e): (1) muse is
primary and texts are the fallback, retired on a measured read of muse's efficacy; (2) Kimi keeps drafting, and muse reads, explains
and answers; (3) a muse answer is a file in the dell2 folder, forwarded by a dell2 job; (4) dell2 hosts the folder, with a read-only
grant for the assistant's table, the open-calls lists and the sprint objects.

## 2. What this means for your plan

1. **The direction is replacement, and the plan must read that way.** muse becomes the way Andrew works the assistant. The Kimi
   text agent over the Quo phone line is no longer the main interface: per decision 1 it is the fallback, and FWD-12 measures muse's
   efficacy so the fallback can be retired on a read, not a guess. Every round from 16 on builds toward that retirement. No round
   adds capability to the Kimi/Quo text path beyond keeping it working as the fallback (FWD-9) and the drafter (decision 2).
2. **Kimi's drafting role stands** (decision 2 (a), "Yes agreed"). Andrew's ~18:0xZ word "replacement" is read as replacing the Kimi
   text agent as his interface. Whether the drafting also moves off Kimi is asked of him by this seat. Until he answers, do not cut
   a cell that removes or re-homes the drafter.
3. **"All of that needs to get done today."** The muse thread is the project's first and only build until FWD-6 is exercised. Issue
   round 16 now:
   - The L6 refusal you recorded (`ec75ee1bef`, STALE ratified half) is discharged: v0.6 is SIGNED @08eb013f09. Re-run the gate and
     issue CA-h-1 (folder refresh script and fixed layout; FWD-6, FWD-10, FWD-11) and CA-h-3 (FWD-7 signed-answer design).
   - Your round-16 decomposition, two orders and `r16/` deliverables are UNTRACKED on the shared tree (`git status` read
     ~18:0xZ). Commit them in the issuance.
4. **CA-h-2 (the dell2 host act) is no longer blocked on a narrow grant.** Andrew's ~16:5xZ word puts the Dell agent users in the
   admin group, with three deny classes kept (`org/tier1_exec/2.0.0_SA_COO~C/deliverables/ANDREW_DIRECT_20261013_165xZ_DELL_USERS_ADMIN_GROUP_KEEP_THREE_DENIES.md`;
   CTO ruling @d2f79ea8dd). Grant (d), read-only for the assistant table, open-calls lists and sprint objects, is covered once
   NFRA_CTLPLN round 12 cell 1 reads the group back on dell2. Cut CA-h-2 as a crossbox ORDER to a named dell2 lane the moment
   that read-back lands. Ask `1.0.0_SA_CTO~DELL2` (through `0.0.0_AB_MSTR`) which dell2 lane hosts it. The dell2 direction packet
   names this join.
5. **The tailnet leg.** Andrew turned password login off himself (~17:4xZ, "I already did this"). The laptop local account is
   deferred ("another time"). So muse reaches dell2, not the laptop. FWD-6's exercise is muse to dell2 over tailnet SSH by key.
   Before you grade FWD-6, NFRA_CTLPLN round 12's SSH cell must read back muse's key on dell2. If that cell does not cover muse to
   dell2, file a surprise row on COMM_ASSIST naming it and keep working.
6. **FWD-12 (muse efficacy) needs a cell in the round after FWD-6 is exercised**, so the fallback decision Andrew asked for is a read.
   Its ACCEPT counts items handled in muse against items handled by text, the wait per item, and the items muse could not show.

## 3. Sources (full text; read as needed)

| what | repo path | link (laptop) |
|---|---|---|
| all six voice-memo transcripts and the CRO aggregate | `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/` | file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/ |
| laptop alignment report (COMM_ASSIST row, the muse gap) | `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/alignment/LAPTOP_OPS_ALIGNMENT_20261013.md` | file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/alignment/LAPTOP_OPS_ALIGNMENT_20261013.md |
| muse midstream brief | `docs/briefs/comm-assist-through-muse-midstream-brief-20261013.md` | file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/docs/briefs/comm-assist-through-muse-midstream-brief-20261013.md |
| PRD v0.6 (FWD-6..12) | `org/missions/D9/COMM/COMM_ASSIST/prd/COMM_ASSIST_PRD.md` | file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/missions/D9/COMM/COMM_ASSIST/prd/COMM_ASSIST_PRD.md |
| laptop direction packet (whole laptop pivot) | `org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_LAPTOP_20261013.md` | file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_LAPTOP_20261013.md |
| cluster positioning ruling | `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULING_20261013_173xZ_CLUSTER_POSITIONING_ON_THE_PIVOT_AGGREGATE.md` | file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/RULING_20261013_173xZ_CLUSTER_POSITIONING_ON_THE_PIVOT_AGGREGATE.md |
