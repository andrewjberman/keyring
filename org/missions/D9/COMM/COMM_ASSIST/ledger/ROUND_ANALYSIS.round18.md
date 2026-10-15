# COMM_ASSIST -- ROUND-18 ANALYSIS (1.0.0_SA_CTO, 2026-10-14 ~22:0xZ)

**On:**
- the issuer's L8 packet `deliverables/2.0.0_SA_COO~CA/r18/ROUND18_L8_PACKET_20261014.md`: 14 of 14 orders complete,
  MAY-CLOSE, no judgment criterion;
- the CVO's L10 slug `surprise-channel/remediations/REMEDIATION_v5.md` @e4b0f0d878, with ADJUDICATION_v7.

**PRD:** v0.10, unchanged. **Standing:** the laptop drives COMM_ASSIST at normal pace (Andrew ~18:4xZ).

## 1. What round 18 moved

- **The SMS ingress mark is live in `enforce`.**
  - The key is narrowed to the execution role, with both Dell users explicitly denied.
  - The mark is valid for 4 hours, held by age.
  - A forged unmarked `sms.reply` was refused and recorded with no side effect. Andrew's real tagged reply was accepted.
  - The first End of Day under `enforce` was accepted (`unmarked_seen` 0).
  - **W10-S2 is disarmed with evidence.** My R18D conditions C1-C3 all read clean.
- **FWD-13's assistant half is live.** The metadata-only mention record and considered-mail log were deployed with the
  dead-letter queue unchanged, and dell2's reader picks up both files.
- The forwarder creates `answers/` (D2-S1). The unstamped LDO-001 sender item is closed.

## 2. Outcome coverage (only what moved)

- **FWD-7** (only Andrew's own channels can answer in his place): the text path is now covered by the mark. The residual
  stated in v0.8 stands: an administrator can rewrite the key policy, as a recorded management write.
- **FWD-13** (muse alerts Andrew within 30 minutes): the assistant half is APPLIED and its reader is live. NOT EXERCISED:
  - muse's own three pieces (a scheduled folder read, an alert ledger, a wake) are muse's to build;
  - one real `@mention` and one real C-MAIL mail are Andrew's acts (calls `44eb`, `e435`).
- **FWD-6/FWD-7's real muse acts:** the one sitting, call `8f2b`, is Andrew's.
- **FWD-12:** waits on a period Andrew names. Kimi keeps drafting until then.
- **Not run live, stated:**
  - the owner-reply confirm path (`#1`);
  - age pruning of the single-use record. It prunes on a write to that object, and none has come.

  Both are read at the first natural event. Neither is a cell.

## 3. Rulings

1. **W21-S1 (ARMED): every laptop commit is unchecked for client account ids, because the hashed list is absent.**
   - **P1, owner `0.0.0_AB_MSTR`, as the CVO names.**
   - Place the list on the laptop.
   - Read dell2 and site Z for the same absence. dell1 showed it on 10-13, so read dell1 too.
   - Re-sweep every laptop commit made while it was absent, and record the result with its denominator.
   - Done when a laptop commit prints the check as run against a list with a stated count.
   - The list's source is the box manager's to state, never a value typed into the repo.
2. **The single pending mail draft is replaced by a newer one: CUT as a product fix.** The mail object holds a LIST of pending
   drafts keyed by seq. A newer considered mail adds to the list and never overwrites. It serves FWD-4's draft loop. This is
   one cell, with a negative case: two mails considered within one minute both keep their drafts.
3. **The trunk's mode default against AWS (the standing `module.ldo_001` second writer): CUT as a mechanism.**
   - The pre-apply check of any `module.ldo_001` plan refuses when the trunk's `chat_assist_ingress_mark_mode` default
     differs from the live environment's `INGRESS_MARK_MODE`.
   - It is a gate, not an alert.
   - It turns my R18D C2 hold into a mechanism, so NFRA_CTLPLN's applies are covered too.
4. **CA-j-18, the stale mail test scripts:** folded into the round's batch repair cell, as hygiene. It serves no outcome on its
   own.

## 4. ENRICHMENT LIST for round 19 (one issuance)

1. The pending-drafts list (ruling 2).
2. The mode-default gate (ruling 3).
3. One batch repair cell: CA-j-18's 4+1 stale test arms, plus any INERT rows the CVO's v7 adjudication left for the issuer.
4. FWD-13's exercise: cut the moment muse reports its three pieces built. Until then, the issuer keeps its thread with muse
   (the 5-minute read inside the 30-minute bound). No cell waits idle on it.

W21-S1 is the box manager's, not a cell of this project.

## ADDENDUM 1 (~22:1xZ): ruling 1 WITHDRAWN -- W21-S1 closes on Andrew's 2026-10-09 word

`0.0.0_AB_MSTR` held before acting and cited this seat's own record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_192xZ_CLIENT_DATA_IN_PRIVATE_GIT_NOT_WORTH_TIME.md`, item 3:
`client-data-check.py` stays wired and WARN-only, and its hashed id list is deliberately NOT built, so it never refuses a commit.
Placing the list would make the check BLOCK, against that word.

- **W21-S1 closes as by design, on Andrew's word.** The CVO records it as CLOSED, not remediated, citing that record.
- The list copy pulled into the laptop's Downloads is deleted. dell1's live list makes its own check block, against the same
  word, so dell1 moves it aside as dell2 did on 10-11, unless Andrew says otherwise.
- This seat's error: ruling 1 was written without reading the standing record.

## ADDENDUM 2 (~08:5xZ 2026-10-15): ruling 2's premise was false

Read by `2.0.0_SA_COO~CA`: `mail_poll.py:132` sends each mail as `ldo.send("mail:<message id>")`, so every mail is its own state
object. The live table holds 59 distinct mail objects, and each real considered mail has `draft_seq` 1. A newer mail never
overwrote an older draft; `mail:owner` existed only in a test fixture. The defect that round 19's pending-drafts list fixed
(CA-k-1, deployed CA-k-4) never existed live. This seat ruled on that premise without reading the producer.

- **The deployed `pending_list` stays.** It is harmless, at one entry per object. Removing it now would cost a deploy for no
  benefit, so it is removed only as part of the next deploy that already touches `mail_requests.py`, never as its own act.
- FWD-13 is unaffected: `mail_log` and one drafts row per object serve it.
- **The lesson for this seat:** a ruling that cuts a product fix reads the producer that creates the state first, not only the
  call's description of it.
