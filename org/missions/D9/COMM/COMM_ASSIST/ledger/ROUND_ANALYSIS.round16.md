# COMM_ASSIST -- ROUND-16 ANALYSIS (1.0.0_SA_CTO, 2026-10-13 ~22:1xZ)

**On:**
- the CVO's L10 slug `surprise-channel/remediations/REMEDIATION_v3.md` @8434c13e07 (watermark 21:58Z; ADJUDICATION_v1: CAh3-AC2
  FAIL; ADJUDICATION_v2: three INERT rows graduate);
- the issuer's packet `deliverables/2.0.0_SA_COO~CA/ROUND16_L8_PACKET_20261013.md`, parts 1 to 3.

**PRD:** v0.6, plus the stated limit in section 2 (recorded as addendum v0.7, no ENDPOINT byte change). **Next:** round 17, cut by
`2.0.0_SA_COO~CA` in ONE issuance on section 3.

**Andrew's direction, binding on this and every later round** (`org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_COO_CA_COMM_ASSIST_MUSE_20261013.md`):
muse replaces the Kimi text agent as his way of working the assistant. Whether Kimi also stops drafting is HELD at him (laptop row
`87a2`). Until he answers, no cell re-homes the drafter.

## 1. What round 16 moved

The muse thread's dell2 end is LIVE:
- CA-h-1 built the refresh script and folder layout.
- CA-h-2 (workstream DELL2HOST, `0.7.0_AE_CloudOps~CA2`) is complete @161b3cf8b7:
  - the dell2 identity is in the admin group;
  - task `MuseReaderRefresh` runs every 15 minutes with `last_result=0` and 4 of 4 sources `ok`;
  - sshd listens with 3 keys.
- The issuer read the folder over the tailnet by key from the laptop: six files, `INDEX.json` run 21:41:24Z, every source `ok`.

What FWD-6 still lacks is its own exercise: one real read **in muse**, with every item carrying its age.

CA-h-3 delivered the signed-answer design. Its judgment criterion FAILED (CAh3-AC2): the design verifies muse's signature in the
dell2 forwarder, but the dell2 identity can send an `sms.reply` straight to the queue, and `on_sms_reply` checks no origin.

## 2. The CVO's ENDPOINT question, ruled

**Question:** with the signature verified at the RECEIVER (`on_sms_reply`, against muse's public key pinned in the assistant's
deployed config), an identity holding admin can still change the handler or its config. That change is visible in CloudTrail. Does
that meet FWD-7's "nothing else can answer in his place"?

**RULED: yes, with the residual named as a stated limit.** FWD-7 bounds the ANSWER PATH:
- every answer that acts carries muse's signature and is verified where it acts;
- an unsigned or mis-signed answer is refused and recorded, whether it came through the forwarder or straight onto the queue.

Rewriting the handler is a different act, a DEPLOY. It cannot ride the answer path silently. It is a code or config change, and it
is recorded:
- in the org trail's management events (read and write, all regions);
- in the NEVER-2 change-management ledger, since Lambda code moves by Terraform only;
- under Andrew's own ruling that the Dell agent users hold admin (~16:5xZ).

No design inside one account can make an admin unable to change code. Demanding that would make FWD-7 unsatisfiable, and that is
not what Andrew asked for. What he asked for is that no one answer in his place, and the receiver check gives that.

**The stated limit (addendum v0.7, CONTRACTS-level, carried into FWD-7's grade):** an identity with admin rights can change the
receiver's code or its pinned key. That is a deploy, visible in CloudTrail and the change ledger, never a silent answer. The key is
rotated by the same change-managed path.

## 3. ENRICHMENT LIST for round 17 (thread-breaking first)

1. **FWD-6's exercise: one real read in muse.** Andrew (or Muse, now an accepted agentbus sender `ms`, @a6ad187452) asks "what is
   waiting on me?" in muse and reads the dell2 folder over the tailnet by muse's own key. Every item carries its age.
   - First, muse's public key goes on record: row W8-S7 says it is in no repo file. The key is read back against CA-h-2's AC3
     fingerprints.
   - Andrew's act, if muse cannot run it alone, is one question asked in muse. The issuer cards it on the laptop list as an act.
2. **FWD-7's build, receiver-verified (the CAh3-AC2 repair):**
   - `on_sms_reply` verifies muse's signature against the pinned key and refuses and records every other answer;
   - the forged-answer test gains a direct-send arm (an `sms.reply` put straight on the queue by the dell2 identity), which must
     refuse;
   - the design names the section-2 limit.

   In the same cell: W8-S6 (a versioned edit answer is checked by `unseen()`) and W8-S8 (the drafts.json rows carry `object_id`).
3. **The answer folder** (W8-S9): `answers/` and `answers/done/` on dell2, writable by muse's account, untouched by the refresh job.
   The dell2 forwarder job follows it. This is a crossbox order to `~CA2`.
4. **FWD-12 (muse efficacy)** is cut the round after FWD-6 is exercised, so the fallback decision Andrew asked for is a read.
5. Carried, Andrew's acts: `44eb` (one Teams @mention) and `e435` (one colleague email).
