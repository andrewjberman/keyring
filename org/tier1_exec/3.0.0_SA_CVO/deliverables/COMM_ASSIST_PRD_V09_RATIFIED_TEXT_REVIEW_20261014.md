# COMM_ASSIST PRD v0.9 -- ratified-text half (ENDPOINT + CONTRACTS) review

**Reviewer:** `3.0.0_SA_CVO~L` (laptop), on 1.0.0_SA_CTO msg 109107. 2026-10-14 ~12:0xZ.
**Verdict:** REFUSED. FWD-13 needs three one-clause fixes. Nothing else in the half moved.

## What was read

- PRD at `98f61b8a2e` (v0.9), half_hash `2ecbb13c8f5b`. `git diff e7bde907ba 98f61b8a2e` (from this seat's last signed pin, v0.6): the
  header gains FWD-13, the ENDPOINT gains the FWD-13 card, and the addenda v0.7, v0.8 and v0.9 are appended. FWD-1 to FWD-12 and CONTRACTS
  are byte-unchanged.
- Andrew's words: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_114xZ_EIGHT_OPEN_CALLS_ANSWERED.md`, VERBATIM item 5:
  "Rec approved, I have not yet seen muse alert me with new emails/teams."
- v0.7 and v0.8 state limits and change no ENDPOINT byte. They are carried into FWD-7's grade as written, and this reviewer measured
  both deploys they describe (CVO halves for CA-i-4, CA-i-12, CA-i-14, CA-j-3, CA-j-8, CA-j-10).

## Findings on FWD-13

1. **The mail scope matches neither C-MAIL nor Andrew's words.** FWD-13 alerts on "a mail that names him". C-MAIL, in this PRD, admits
   a message ONLY when its sender's domain is one of the five he named AND its body names "Andrew"; nothing else enters the assistant.
   FWD-13 drops the domain test, so it promises alerts on mail the assistant never reads, and its ACCEPT confines the source to the
   folder fed by the assistant. Andrew's own word, "new emails", is wider than both.
   **Fix:** FWD-13 reads "a mail C-MAIL admits (from one of the five, naming him)". If Andrew means every new email, that is wider
   than C-MAIL and needs his word on an open call; the PRD neither narrows nor widens his words for him.
2. **"Soon after it lands" cannot be graded.** DONE WHEN reads each alert's age, but nothing states the age it must be under. A
   five-hour-old alert would pass as written.
   **Fix:** state the bound in minutes (for example, the refresh interval plus muse's watch interval), and DONE WHEN reads each
   alert's age against it. Or drop "soon" from the card.
3. **"One item NOT for him" is undefined.** The negative arm cannot be chosen without it.
   **Fix:** name it: for mail, a message C-MAIL refuses; for Teams, a channel message that does not mention him (or whatever class
   the CTO intends, stated).

## Checked and sound

- FWD-13 traces to Andrew's ~11:4xZ word, and the CTO's record states the reading (pull today, push expected).
- The ACCEPT keeps FWD-6's folder, FWD-11's no-cloud-access rule, FWD-9's fallback and C-ONE-YES ("nothing is sent in his name by an
  alert").
- No seat name or history sits inside the ENDPOINT section.

-- 3.0.0_SA_CVO~L
