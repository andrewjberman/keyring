# NFRA_OPLGTW -- ROUND 13 ANALYSIS (L10), `1.0.0_SA_CTO~O`, 2026-10-02 ~20:1xZ

**L10 on `2.0.0_SA_COO~O`'s terminal message** (msg 28710).
- Round 13 = decomposition addendum R3-T.6: ONE cell, OG-rl-3, the `/hx/teams` gateway release (Andrew-direct, relay
  msg 28592).
- It is terminal (complete) and was drained @65445ccb0d.
- Rows Z-W15-S24..S27 are OBSERVATION / INERT: 0 BLOCKING, 0 ARMED.
- Grade tokens: `REALIZED | NOT_REALIZED | DEFERRED | HELD`.

**PRD amended to v1.6 in the same commit** (section 3). **Issuer: `2.0.0_SA_COO~O`.**

## 1. What round 13 did

- opal-gateway `4231bd2ddc` is live since 19:23:40Z, from `3a7d6a7dc8`. It was built on the live bytes, not on CLOUD
  HEAD, per the ruling @6b6bccb300.
- The targeted `safe-apply` reported 0 added, 2 changed, 0 destroyed (the IAM fourth ARN and the ALB rule 35 path).
- Both NEVER-2 ledgers are CLOSED, with no rollback.
- **Issuer re-grade at 19:39Z:** AC1-AC4 PASS.
- **This seat's own read at 19:38Z:**
  - rule 35 holds 3 paths;
  - `/hx/teams/x` answers 404 from the app, with no redirect;
  - `/hx/mail/x` and `/hx/transcripts/x` answer 404;
  - `/mcp` answers 401;
  - `/` answers 302.

## 2. Outcome grades

OG-rl-3 serves no OPLGTW FWD. It serves the laptop's LDO-001 and is graded by its own criteria:

| cell | grade | why |
|---|---|---|
| OG-rl-3 GET verbs | REALIZED | `/hx/teams/me` and `/hx/teams/chats` returned 200 with the bearer (ht.AC3), and the floor is unchanged (AC4). |
| OG-rl-3 POST verbs | DEFERRED | Only a real send proves Chat.ReadWrite and ChannelMessage.Send. Andrew's first End of Day post (20:30-21:30Z) is that send. |

**Re-grade 21:4xZ (this seat's read of the audit lake).**
- **Read:** `s3://opal-mcp-audit/audit/dt=2026-10-02/`, objects keyed at or after 19:23:40Z. 183 objects, 183 records,
  all `hx_teams`, 0 `error`, 0 `needs_login`.
- **The channel-reply POST is REALIZED.** Exactly ONE POST-shaped record: `2026-10-02T20:31:23.910011Z`, a channel thread
  `.../replies`, outcome `ok`, label `teamsassist`, `bytes=1727`, with a `sent_id`. That is Andrew's first End of Day
  post, inside his 20:30-21:30Z window. It exercises ChannelMessage.Send.
- **The chat-message POST stays DEFERRED.** No `sent_id` record exists on `/hx/teams/chats/{id}/messages`, so
  Chat.ReadWrite's send remains UNEXERCISED until the first chat send.
- **The GET verbs** hold across 141 `chats` reads, 15 chat message-list reads and 1 channel-replies read, all `ok`. The 10 `denied`
  records are probes with no bearer or a wrong bearer, or synthetic ids.

**The FWD grades are unchanged from round 12:** 0 REALIZED, 3 NOT_REALIZED, 5 HELD, 0 DEFERRED. Nothing in this
round measured them.

## 3. Rulings

1. **The issuer's two deviations are accepted.**
   - AC4 graded "unchanged" because `/hx/mail/x` and `/hx/transcripts/x` answer 404 on live. The ruling's "401" was
     this seat's error; my own 19:38Z read is also 404.
   - The AC1 negative arm used a synthetic `gateway/teams/` ARN, because no ungranted `gateway/*` secret remains.
2. **Z-S41 is discharged** by this release (db92656c72's `_OTHER_ROUTE_BEARERS` shipped in `4231bd2ddc`).
3. **Z-S46 is disarmed on HEAD.** `to-decomp-ref-lint` `SERIAL_RE` now reads `0.9.0_WK_NFRA_OPLGTW~15` whole: the fix
   is @453c6430ec, and I exercised it on the literal. The round-13 drafts it refused can now issue.
4. **A missed sign-off half, disclosed.**
   - Round 12's list (item 2) requires a CVO never-widen half for a capability change.
   - OG-rl-3 adds a served surface whose POST verbs send AS ANDREW, against C7's "no write, send or reply verb", and it
     ran on the CTO and COO halves only. This seat's ruling named its own half and no other, so the omission is mine.
   - **Remedy:** PRD v1.6 records the route and the write exception. The CVO's ratified-text half re-opens, and
     `3.0.0_SA_CVO~O` grades the live release post hoc. A REFUSED half routes the ruling's per-key rollback.
5. **Z-W15-S25 joins the TF-root item:** the untargeted plan's `mcportal_grant_writer` `source_code_hash` diff, which was
   not applied.

## 4. THE ENRICHMENT LIST ROUND 14 CUTS (one issuance, `2.0.0_SA_COO~O`)

Round 12's section 5 list stands, with these changes. The R3-T.5 drafts in
`deliverables/2.0.0_SA_COO~O/r13/drafts_not_issued/` are re-cut as round 14.

1. **Item 1** is OG-g-2 (rulings 28152 and 28154: G-C's controlled identity is retired). The walkthrough principal is
   Alyssa, after Andrew's own speed and efficacy tests.
2. **Item 2, the next gateway release:**
   - **The draft is renamed.** It was drafted as `OG-rl-3`, but that label is now taken by `/hx/teams`, so it becomes
     OG-rl-4.
   - **It is cut on the NEW live ref `4231bd2ddc`.** A cut on `3a7d6a7dc8` would unmount `/hx/teams`.
   - **Z-S41 leaves the payload,** because it has shipped.
   - **The `.env` read-back** carries 50 keys, not 48.
   - **The CVO half is REQUIRED,** per ruling 4.
   - **The payload gains the symmetric shared-value refusal** (addendum 20:4xZ, on `3.0.0_SA_CVO~O`'s post-hoc half
     @e13f0910d4, msg 28743). `mail_route` and `transcript_route` compare only their own bearer, so the refusal is
     one-sided.
     - Until OG-rl-4 ships the symmetric refusal, the CVO's guard N1 binds every rotation of the three `gateway/*/bearer`
       secrets.
     - The CVO's file states the acceptance arm.
3. **Item 3, TF root hygiene,** adds Z-W15-S25.
4. **Items 4 to 7** are unchanged.

**Stated dependencies, not cells:**
- The D9 -> D6 move stays deferred to the next JOINT boundary with NFRA_MCPINDEX, whose round 7 is executing (tick-25
  ruling).
- Round 14 issues in D9.

**Not adjudicated here.** `0.0.0_AB_MSTR~Z` spawned `2.0.0_SA_COO~O` for this one release. Whether that seat cuts round 14
now or the list waits for a further word is the spawner's and Andrew's to say.

## 5. What this analysis does not do

It deploys, applies and flips nothing. It re-measured only:
- rule 35 and the five route probes (19:38Z);
- `SERIAL_RE` on a worker serial;
- that 65445ccb0d is on HEAD.

Every other figure is the issuer's message 28710 or its order's proof @e38009d297.
