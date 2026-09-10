# ANDREW-DIRECT 2026-09-10 -- AMGT_RESAPP, all five open calls ruled

**Recorded by:** `4.0.0_SA_CRO~Z` at its own terminal, same turn as the ruling.
**Frame:** `/open-calls` was run at this lane and returned 5 cards (3 BLOCKING, 2 CARRIED).
Andrew answered all five in one message. **His words are reproduced VERBATIM below and are the
authority; everything under "READ" is this seat's reading and is subordinate to them.**

## THE RULING, VERBATIM AND COMPLETE

> *"1 Rec approved + make sure that its stored somewhere so we dont need to do it twice, also test
> on one security at a time initially to assess the actual payload volume so in case it turns out
> really heavy we dont get in trouble with bloomberg on quota. 2 A first, B sure maybe just based
> on recency and frequency of mentions. C can come later after we've discussed. 3 we can include a
> print renderer/export pdf preview appear in a popup modal with a download option. 4 We can do a
> scan for IR pages associated with the 89 and enumerate from there. 5 do not talk to adam."*

---

## CALL 1 -- universe bounds. RULED: REC APPROVED = option (c).

**READ:** pre-compute the 89 covered names on the daily vehicle that already runs on this box;
queue anything outside the 89 to a desktop agent; the UI states which it served.

**TWO NEW STANDING INSTRUCTIONS RIDE ON THIS ANSWER** -- they are not part of the (c) choice and
must not be collapsed into it:

- **STORE IT SO IT IS NOT DONE TWICE.** *"make sure that its stored somewhere so we dont need to do
  it twice."* Applies to the field-mapping work AND to the pulled data. The map is persisted at
  `AMGT_RESAPP_BLOOMBERG_FIELD_MAP_20260910.md` @ `4ca943547e`. The DATA half is not yet -- every
  Bloomberg response this project pulls must land in `opal-data-research` on first pull and be read
  from there afterwards. **This makes the cache a correctness requirement, not an optimisation.**
- **QUOTA IS A LIVE RISK. MEASURE PAYLOAD BEFORE SCALING.** *"test on one security at a time
  initially to assess the actual payload volume so in case it turns out really heavy we dont get in
  trouble with bloomberg on quota."* **=> A payload-volume assessment is now a precondition on any
  multi-security run.** The one-security-at-a-time constraint from the original egress grant is
  re-affirmed and given its reason: not politeness, quota exposure.

## CALL 2 -- what the AI Analysis is. RULED: (a) first, (b) yes, (c) deferred.

*"A first, B sure maybe just based on recency and frequency of mentions. C can come later after
we've discussed."*

**READ:**
- **(a) is the primary deliverable** -- draft Adam's five limbs as prose. "First" is sequence, not
  merely priority.
- **(b) is in, with its ranking function NAMED BY ANDREW: recency and frequency of mentions.** That
  is a specification, not a preference -- it is buildable as written and should not be embellished.
- **(c) house-framework scoring is DEFERRED pending a discussion that has not happened.** It is not
  rejected. **No seat may self-start (c).**

**This unblocks the data contract (Option 4), which was gated on this call.**

## CALL 3 -- print artifact in v1. RULED: IN, and the shape is specified.

*"we can include a print renderer/export pdf preview appear in a popup modal with a download
option."*

**READ:** this OVERRIDES this seat's REC, which had proposed deferring the print renderer to a
later project. It is in v1, as a **PDF preview in a popup modal with a download option** -- so the
pack object must carry everything the PDF needs from day one, and the modal is a named component in
the design spec. The half of the REC that said "tell Adam that now" is void under Call 5.

## CALL 4 -- web-search source allowlist. RULED: derive it, do not ask for it.

*"We can do a scan for IR pages associated with the 89 and enumerate from there."*

**READ:** the allowlist is **DERIVED from the 89-name coverage universe**, not authored and not
requested from anyone. A scan resolves each covered name's investor-relations page and the
enumeration falls out of that. This is a buildable task with a printable denominator (89), and it
disposes of "who decides what is trusted" by making the coverage list itself the answer.

## CALL 5 -- who contacts Adam. RULED: NOBODY.

*"do not talk to adam."*

**READ:** an absolute standing instruction on this project's outward comms. **No message, no email,
no Teams, no reply, direct or relayed, to Adam Muller from this seat or any seat acting on this
project's behalf** until Andrew says otherwise. Consequences carried honestly:

- The CSC peer-set question (`AMGT_RESAPP_PRE_BRIEF_NOTES_20260910.md` §3.2) **cannot be resolved by
  asking.** It stays a flag, or it gets settled by measurement against the packs themselves.
- Whether the peer set is analyst judgment or derivable must now be **inferred from the 89-name
  corpus**, not confirmed by its author.
- Adam's own acceptance test ("we want it to print cleanly") stands as written in his email and is
  the only statement of his requirements this project may rely on.

---

## WHAT CHANGED IN THE WORK, as a result

| Item | Before | After |
|---|---|---|
| Universe | open | 89 pre-computed / others queued |
| `opal-data-research` cache | a design nicety | **a correctness requirement** (Call 1) |
| Payload volume | unmeasured | **a precondition on multi-security runs** (Call 1) |
| AI Analysis | undefined, blocking | (a)+(b) defined, (b)'s ranking specified, (c) parked |
| Print artifact | proposed for a later project | **in v1, as a PDF-preview modal with download** |
| Web-search allowlist | an open question | a derivable scan over the 89 |
| Adam contact | an open question | **prohibited** |
| Option 4 (data contract) | gated on Call 2 | **unblocked** |

## STILL OPEN AFTER THIS RULING

1. **The normalization call** raised by the field map (`..._BLOOMBERG_FIELD_MAP_20260910.md` §5):
   Bloomberg cannot reproduce FactSet's recurring EPS across 8 mnemonics tested. Not among the five
   cards -- it was surfaced by work done after they were cut, so Andrew has not seen it. **Carried
   to the next `/open-calls`.** Under Call 5 the fallback of asking Adam is closed.
2. **(c) of Call 2** -- parked pending the discussion Andrew named.
