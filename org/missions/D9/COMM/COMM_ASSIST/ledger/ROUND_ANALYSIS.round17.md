# COMM_ASSIST -- ROUND-17 ANALYSIS (1.0.0_SA_CTO, 2026-10-14 ~02:5xZ)

**On:** the CVO's L10 slug `surprise-channel/remediations/REMEDIATION_v4.md` @bd4d7b90e4 (watermark 02:45Z; 14 of 14 orders
complete; MAY-CLOSE; three rows graduate, one ARMED). **PRD:** v0.7. **Next:** round 18, cut by `2.0.0_SA_COO~CA` in ONE issuance on
section 3. **Andrew's direction stands** (muse replaces the Kimi text agent as his interface; whether Kimi also stops drafting is
held at him, `87a2`).

## 1. What round 17 moved (three deploys, each signed on both halves and closed)

- **CA-i-4:** the receiver verifies muse's signature against the pinned key.
- **CA-i-4:** the received-mail paste loop (J290, nothing sent).
- **CA-i-4:** the `ldo-001` agentbus stamp.
- **CA-i-12:** an answer acts at most once and is bound to its draft's `seq`. This closes C-S5, measured live.
- **CA-i-14:** a `signed_at` bound of 24 hours back and 5 minutes forward on the receiver's clock. This closes C-S6, measured live.
- **The dell2 forwarder and the answers folder** exist (CA-i-5; the folder was made by hand there, see D2-S1).

Not exercised in the round: Andrew's own read and answer in muse.

## 2. Rulings

- **`W10-S2` (ARMED; a forged `sms.reply` put on the queue acts as his text):** as ruled at ~23:1xZ
  (`CTO_RULING_20261013_231xZ_COMM_ASSIST_SMS_FORGERY_AND_J290_DRAFTS.md`), the SMS ingress marks each `sms.reply` it forwards, and
  `on_sms_reply` refuses and records an unmarked one. This is round 18's FIRST cell. The row stays ARMED until it lands. The interim
  limit stands as written.
- **`W18-S2` (muse's signer is not in the repo):** before Andrew's first real muse answer, ONE real signed answer from muse must be
  shown to carry `signed_at`, `version`, `seq` and `tag`, and the live receiver must ACCEPT it.
  - muse is a sender-only identity with no inbound queue, so the request reaches muse through Andrew.
  - The issuer folds it into the existing act `8fb2` (ask muse once) as one sitting: muse reads "what is waiting on me?" (FWD-6), then
    signs one answer, a `drop` on a test draft, which the receiver must accept.
  - If muse's payload lacks a field, every answer is refused (safe). The fix then sits on muse's side and is named to Andrew in plain
    words.
- **`D2-S1`:** the forwarder creates `answers/`, `answers/done/` and `answers/rejected/` when absent. This goes in the batch cell.

## 3. ENRICHMENT LIST for round 18 (thread-breaking first)

1. **W10-S2: the SMS ingress mark** (P1, a WORLD deploy under its own pair).
2. **FWD-6 and W18-S2 in one Andrew sitting** (act `8fb2`, re-worded as above). FWD-6 is the thread's own exercise; until it is read,
   FWD-12 (muse efficacy) is not cut.
3. **J290's first real use:** Andrew finishes the Keith Wagner (TIFIN) reply with the paste loop. That is his act, carded. After it,
   the draft-only Outlook route is asked of NFRA_OPLGTW through `0.0.0_AB_MSTR` as ruled.
4. **A read, not a cell:** the agentbus shows no `unstamped sender=LDO-001` WARN since CA-i-4, on every box's consumer log. Any WARN
   seen is a row.
5. **ONE batch cell:** D2-S1.
