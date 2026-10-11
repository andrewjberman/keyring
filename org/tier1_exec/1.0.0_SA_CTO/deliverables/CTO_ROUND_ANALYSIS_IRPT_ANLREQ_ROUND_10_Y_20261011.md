# CTO ROUND-10 ANALYSIS -- IRPT_ANLREQ workstream Y -- answering the L10 slug for rounds 5 to 9 (2026-10-11 ~17:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/remediations/REMEDIATION_v5.md`
@7169a2805d (3.0.0_SA_CVO msg 5424). **Prior:** the round-5 (Y) analysis @ca8aa78b88. **No PRD addendum.**

## 1. Where the workstream stands

Release 6 is live (`irpt-commentary-composition-read-lambda` `DbvBUxTG`, this seat's own read at 16:51Z; the issuer's
after-reads msg 5411) and reached by no product path. The form's record step is on portal DEV and unexercised. The
report-to-ticket binding is merged and not released. Nothing from rounds 3 to 7 is on `irpt-status`: release 5's return,
now carrying the binding, waits on portal changes reaching PROD, which is Andrew's word.

## 2. The slug's five items

1. **Row D2-S51, ARMED, disarm owner this seat: the portal change that sends the ticket's id must not reach DEV before the
   service carries its half, and only a message holds it.** A hazard held by a message is not disarmed. **The disarm is to
   make the order not matter:** the Open read sends `ticket_id`, and on the one refusal the live service gives for an unknown
   query member (`UNEXPECTED_OWNED_READ_QUERY`) it repeats the read ONCE without it. Before the service's half is live the
   page then reads exactly as it does today; after, the binding is checked. One portal cell, on the held candidate
   `5f64f409b0`; with it the candidate may land on DEV at any time, and the row closes on that landing. Until the cell is
   merged the candidate stays unlanded, as it is now (this seat's and the reviewer's reads).
   - What the fallback costs, stated: while the service's half is not live, a wrong link is not refused. That is today's
     behaviour, and row TCKT_VNEXT-D2-S40 already says so.
   - The retry is on that one code only. Any other refusal is shown as it is.
2. **Release 6 reached by no product path; two members inferred inert.** Accepted as stated. Its first product read is the
   drafter's, when the analysis-ready binding exists; the issuer reads that first one.
3. **Release 5's return.** One act that waits on Andrew. DSGN_IRPTV1 is writing the PROD candidate record he would be
   approving (this seat's round-23 analysis @b417e9ee3c). When PROD carries it, the return is cut under one pair whose census
   lists release 5's members and the binding's three files together.
4. **Row IRPT_ANLREQ-S1: a laptop agent session can read the packager's secret.** Ruled, and corrected in this seat's half
   @7b039a456b: the sentence "no other reader" was false; the secret is readable by the host's role and by any administrator
   of the account, and the laptop's agent sessions run as one. Nothing in this project changes that. It is not a reason to
   un-mint: the same identity reads every secret. Whether laptop sessions should run as it is put to Andrew.
5. **45 of 51 accepted requests store no ticket id.** The baseline the binding meets, and the reason the binding lets a
   request with no stored ticket id read as today. Nothing is back-filled.

Row D2-W52-S5 (one real filing through the form, read end to end): that is TCKT_VNEXT's fifth run for the service side, and
a staff person's filing for the page itself.

## 3. ENRICHMENT LIST for round 10 (ONE issuance)

1. The fallback cell of item 1, on the held candidate; then its landing, and row D2-S51 closed.
2. Row D2-S34 (the build's parity check is off) and the entry's four unpinned members, as the issuer already lists.
3. The pair for release 5's return, WRITTEN and held, so that Andrew's word is followed by an apply and not by a packet.

## 4. Acts only Andrew can do

- The PROD push that release 5's return waits on (CLAUDE.md, Agent Autonomy).

## 5. What this analysis did not measure

It rests on the slug and the issuer's reports as filed. This seat's own reads are the function's digest and portal DEV.

-- 1.0.0_SA_CTO~DELL2
