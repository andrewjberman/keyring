# ANDREW-DIRECT 2026-09-11 ~05:2xZ-05:3xZ -- TIGHTEN THE SIGN-OFF PROCESS; CVO ALWAYS; COO FOR CRO WHEN OFFLINE; WORK IT INTO THE SPINE, RULE 27 AND THE DOCS; SCRIPTS AND STAMPS THAT WORK; CLEAR EXPECTATIONS

**Terminal:** `1.0.0_SA_CTO`. **Recorded by:** `1.0.0_SA_CTO`, same turn. Landed as spine v3.15 at `e7e552f7c4`.

## VERBATIM AND ENTIRE, in order

> I want you to look critically at the "sign-off" process, what literature is there on this? it is very loose right
> now and unclear. I want to tighten it up. How do we move the gating process along naturally so i dont have to be
> buzzing around asking agents what theyre doing? What comes right before this stage? on iteration it would in theory
> be L3 into L4, which proceeds naturally enough. In multi-round, we'd be coming off L10, where all of the TOs have been
> done and we have a big slug in from CVO, so the question then becomes you get the slug and write an addendum or
> something. It may be the case where the easiest thing to do is just mcp two of potentially three execs, depending on
> who has the best context. For example, if CVO is active and writing lots of briefs that are feeding the projects then
> they should be included. CVO should always be included. If CRO is not online, can do COO in their stead.

> but this needs to be worked into /canonical-flow , into Rule 27, into any reference docs. make sure the spine
> operation works properly, that the scripts work properly and the agents know how to use them to do their stamp. make
> sure there are clear expectations here

## THE CRITICAL READ OF v3.14, MEASURED

- Thirteen PRD versions between 16:22 and 00:46 local. The reviewers signed v0.4 at 17:36 / 18:07, then nine bumps
  went by with no signature because every bump re-opened BOTH files by construction, even when a reviewer's half had
  not changed a byte. The CRO's brief half was unchanged from v0.11 to v0.13 and was re-signed twice.
- Nothing measured "review overdue". The notifier re-offered a delivery until READ, and READ is not SIGNED; the
  reviewers moved when Andrew said "nudge the reviewers" at 04:1xZ.
- The sign-off file was hand-written JSON with a prose spec; the pin was a full hash in one file and could have been
  anything in another; the gate matched on prefix.
- Reviewer selection was fixed (CRO + CVO) with no liveness or substitution rule.
- The notifier's post-commit wrapper never triggered on a sign-off commit, so the release branch never fired
  (fixed at 973ad3770f before this word).
- The L10 addendum path was correct in the spine's text but, being version-bound, would have re-opened both
  halves on an ENDPOINT-only addendum.

## WHAT HIS WORD SETTLES AND WHAT LANDED

Two halves bound to their bytes; the CVO always on the ratified-text half; the CRO on the brief half or a live COO
not holding the round in its stead; one stamp tool; one status read; a window with automatic nudges and re-routing;
the addendum path re-opening only the half it changed; the vintage boundary in code; one rule in one library. The
literature: the spine's L4-R block (v3.15), Rule 27's L4-R clause, the canonical-flow skill's owner rows, the Codex
load skill's step 8, the header schema's consumer (4), and this record.
