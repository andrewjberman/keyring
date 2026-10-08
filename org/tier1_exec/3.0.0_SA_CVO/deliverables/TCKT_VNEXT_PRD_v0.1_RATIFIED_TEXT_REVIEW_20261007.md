# TCKT_VNEXT PRD v0.1 -- ratified-text half review (L4-R)

**archetype:** VALIDATE

Reviewer: `3.0.0_SA_CVO` (seated on dell2; NFRA_CTLPLN ADDENDUM v0.12), 2026-10-07 ~17:2xZ. Subject:
`org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md` v0.1 @a6978b2ac2 (`1.0.0_SA_CTO~DELL2`), read whole; the brief
`docs/briefs/d7-ticket-center-request-types-analysis-request-first-brief-20261007.md` @750ec86588 read for O1-O8 and I.0. Asked by msg 903.

**Verdict: REFUSE, narrowly.** Two ENDPOINT corrections are required (R1, R2); each is a wording change. One contract finding (P1) is for
L5 and is not a ground for this refusal. Everything else checks and would sign as written.

## Required corrections

**R1 -- FWD-2 is a wait that is not qualified.** DONE WHEN reads "a real sign-in from another firm tries both and is refused, in front of
Andrew"; ACCEPT, "Andrew watches someone signed in for a different firm ...". No seat can make that happen on demand:
- it takes another firm's real principal, and minting one is a write to the production auth plane (opal-users-v2), the same block row
  IRPT_BCKEND-S382 hit today;
- it takes Andrew's presence.

Spine L2 (CLAUDE.md rule 27): "NO FWD IS A WAIT ... A genuinely essential wait is expressly qualified on the outcome with its reason and
Andrew's word." FWD-8 carries such a line; FWD-2 does not. Either:
- (a) add a WAIT line quoting the word that asks for Andrew to watch, and naming the other-firm principal he provides; or
- (b) make the DONE WHEN seat-drivable: a designated other-firm test principal that Andrew names, refused on the ticket and the report
  reference. Andrew watching then becomes the organic case.

The brief's O2 ("Andrew sees it refused; it is not asserted") is the CRO's phrasing; this seat found no quotation of Andrew asking for it.

**R2 -- FWD-1, FWD-3 and FWD-4 have one named person as the only actor.** "Alyssa files ...", "Alyssa's known-bad sheet ...", "Alyssa files
a request and then claims and completes". Alyssa as the first requester IS Andrew's word (brief I.0, 2026-09-30), and that is a sound
SOURCE. But as written, each DONE WHEN is met only when she acts. Either:
- (a) a seat drives each with an internal principal on DEV (filing, the two sheets, self-claim), with Alyssa's real use as the organic
  arm; or
- (b) a WAIT line on each, quoting that word.

FWD-5, FWD-6 and FWD-7 already read "an Opal person" / "someone" and need no change.

## P1 for L5 (not a ground for refusal): the upload door may refuse the thread as drawn

The thread has an internal Opal person file on behalf of an advisor (step 1). A second person opens the same file (step 2), and the person
working the ticket submits the report with the ticket's `input_id` (C-HANDOFF). In the door's code at dell2 CLOUD:
- `intake/uploads.py:188-195` (`_allow`) refuses any owner whose `firm_id` is `global` or `opal-capital`;
- `:223-234` (`create`) admits a principal acting for a different owner only on the same home firm, principal class and advisor;
- every read (`read_input`, `_load`) re-runs `_allow`.

So an `opal-capital` filer either owns the upload (refused at `:193`) or files for a client-firm owner (refused at `:227-234` unless the
home firms match). Whether a second Opal person can read or submit against it was not exercised. R8 states "the uploader is the actor with
matching firm", and C-HANDOFF already asks IRPT_YCDGEN to confirm at L5. The question belongs with IRPT_BCKEND's door as well, before the
round-1 thread is cut on it.

## Checked and holding

- Every FWD traces to the brief: O1/O4 to FWD-1, O2 to FWD-2, O3 to FWD-3, F4 to FWD-4, O6 to FWD-5, O5 to FWD-6, O7 to FWD-7, O8 to FWD-8.
- Andrew's self-claim word (2026-09-30) is the brief's quotation. C-SELF-CLAIM keeps the other `_sod_block` clause.
- C-ONE-DOOR adds no new address (rule 30), and C-MORATORIUM builds no new notification.
- Round 1 is internal-only, with the client surface on Andrew's word: FWD-8's WAIT line is properly qualified.

-- 3.0.0_SA_CVO
