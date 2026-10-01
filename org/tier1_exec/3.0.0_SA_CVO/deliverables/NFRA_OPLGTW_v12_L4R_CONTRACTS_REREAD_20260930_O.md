# NFRA_OPLGTW PRD v1.2 -- re-read of the changed CONTRACTS (C7) (3.0.0_SA_CVO~O, 2026-10-01 ~00:1xZ)

**Subject:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` @725230b531 (v1.2), against this seat's signed v1.1
@c80b5c85b6 (review @7940709bef). Asked by 1.0.0_SA_CTO~O msg 27440. The ENDPOINT is unchanged: `prd-signoff status`
reads "current by ENDPOINT hash", so nothing is withheld and the v1.1 stamp STANDS. The v1.1 -> v1.2 diff is +82/-1,
all in the new C7 and its addendum.

**VERDICT: no re-sign yet.** One finding (F1) and one wording note (N1). Everything else in C7 agrees.

## What agrees (checked)

- **Andrew's route word.** "the daily pull runs through the EXISTING Opal gateway under Andrew's account; no new app
  registration, no IT" is verbatim in the counterpart, NFRA_TRNSPT PRD C-IDENTITY (`NFRA_TRNSPT_PRD.md:108`), and in its
  brief v3, item 6.
- **The `/ms/*` claim.** It matches `app/ms_ingest.py`: the docstring says "NEVER echo file content, a body/preview, or
  any comms field", and :147 says "NEVER the file's bytes/content". So C7 keeps `/ms/*` structure-only and adds new
  prefixes. That is a new capability, not a widening of an existing surface.
- **The transcript tools** cite `docs/briefs/opal-gateway-meeting-transcript-tools-spec-20260929.md` (present).
  Counterpart S04/S05 asks for exactly these tools and the sign-in-lifetime measurement (O3).
- **The mail tools (O4)** match counterpart C-GATEWAY-TOOLS: the filtered paged list (sender, received date,
  has-attachment, following `@odata.nextLink`) and `ccRecipients`.
- **The attachment bytes.** The counterpart asks for "an attachment-download tool". C7 serves PDF bytes only on the
  headless O5 route and keeps the MCP tool inspect-only. The counterpart's consumer is the scheduled pull, which is
  headless, so O5 serves that need. This is a deliberate narrowing, and C7 states it ("the byte-returning `$value`
  download NFRA_TRNSPT needs for bronze"). See N1.

## F1 -- the headless mail route reaches wider than the counterpart's criterion

- **C7 (O5):** "ONLY messages whose sender is on NFRA_TRNSPT's sender table ... are reachable, **plus messages that
  share a `conversationId` with one of them**."
- **Counterpart C-CRITERION (`NFRA_TRNSPT_PRD.md:110`, Andrew-direct):** "An email is ingested when the SENDER is on a
  named author table ...". The counterpart has no thread-sibling reach, and neither does its brief or its gateway-
  dependency list (`R1_GATEWAY_DEPENDENCIES_FOR_SITE_Z_20260930.md`).
- **Why it matters.** The thread clause makes reachable, by a static bearer under Andrew's delegated token, the bodies
  of messages from ANY sender who replies in a thread an author started. That includes clients and outside parties.
  It is a content surface the counterpart never asked for, and the route's own negative arm ("a message from a sender
  off the table refused") would PASS while thread replies stay reachable.
- **Fix, one of:**
  - (a) drop the clause, so the bound is the sender table only, as the counterpart states;
  - (b) cite the counterpart need it serves, and bound it (for example, siblings whose sender is also on the table, or
    an Opal domain), with an added negative arm: an off-table sender inside an author's thread is refused.

## N1 -- wording (non-blocking)

- C7 names the sender table as "Manav's and Yang's addresses". The counterpart says "Manav; Yang if her addresses are
  supplied". C7 should carry the condition.
- Counterpart C-GATEWAY-TOOLS still says "attachment-download tool". The laptop CTO can align it to C7's O5 route at
  its next bump.

This seat re-signs on the bump that closes F1.

-- 3.0.0_SA_CVO~O
