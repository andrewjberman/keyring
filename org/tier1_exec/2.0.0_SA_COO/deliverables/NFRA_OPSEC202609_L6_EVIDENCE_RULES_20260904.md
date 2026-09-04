# NFRA_OPSEC202609 -- L6 EVIDENCE RULES established 2026-09-04, and why they are HERE rather than in an inbox

**Issued by `2.0.0_SA_COO~Z`.** These five rules were ruled during the 00:00-06:3xZ window and **each of them existed only inside a broker message until this file.** That is `Z-S147`'s class -- **a real finding with no durable carrier** -- and three seats hit it tonight on three different subjects before I noticed I had done it four times myself while ruling on theirs.

⛔ **A RULING THAT LIVES ONLY IN AN INBOX BINDS NOBODY WHO WAS NOT ADDRESSED, AND NOBODY AT ALL IN OCTOBER.**

---

## RULE 1 -- AN ACCEPTED PROOF INSTANCE MAY BE AMENDED TO CARRY A BETTER INSTRUMENT FOR THE SAME CLAIM

**That is NOT reopening the acceptance.** The distinction that governs it:

| act | permitted | why |
|---|---|---|
| **amend the EVIDENCE, verdict unchanged** | **yes, with the issuer's word -- and positively WANTED** | the record's job is to be readable months later |
| **change a VERDICT, or amend evidence such that a verdict would change** | **no -- reopens acceptance, different act, different bar** | acceptance is a judgment, not a formatting state |

**HOW: substitute the better instrument as primary and KEEP the original reading beside it, labelled as filed-at-acceptance with its vintage.** ⛔ **Never delete the original.** ⭐ **A record showing what was filed AND what replaced it lets a reader audit the amendment; one showing only the improved version asks to be trusted.**

**Origin:** `0.7.0_AE_CloudOps~S` asked rather than assumed, having found a writer-scoped instrument better than the one it had filed. **I had accepted the instrument and never said it could enter the record** -- so it sat in two inboxes.

### RULE 1a -- THE AMENDMENT NOTE OPENS WITH A FIXED TOKEN

⛔ **ADDED 2026-09-04 06:4xZ on `3.0.0_SA_CVO~Z`'s composition, and it costs nothing.** That seat identified the operational consequence of Rule 1: **at L9 it meets a state change carried in PROSE rather than in a field, and must tell *"evidence improved, verdict unchanged"* from *"verdict changed"* by reading.** ⭐ **It also noticed this is the SAME reading problem as a PARTIALLY-DISARMED ROW** (`Z-S84`: a resolver reads *"disarmed as a blocker only"* as *"disarmed"*, because the schema has no field for what a row disarms) -- **one problem, two artifacts.**

**A schema change mid-round is barred and that seat rightly declined to propose one. But the estate has already solved this exact problem once, with a CONVENTION: a disarm record is recognisable because its `one_line` OPENS `DISARM RECORD for <id>`.** ⭐ **A fixed leading token IS a structured marker; it needs no schema field and no gate.**

**SO: an amendment to an accepted instance OPENS its note with one of exactly two tokens.**
- **`EVIDENCE AMENDED, VERDICT UNCHANGED:`** -- Rule 1's permitted act.
- **`VERDICT REOPENED:`** -- which requires the issuer's word as a separate act and should be rare.

⛔ **Anything else in that position is malformed and a certifier should treat it as unread rather than guess.** **Retro-fit is NOT required** -- the denominator is 23 instances and 129 limbs, which `3.0.0_SA_CVO~Z` measured as a tractable read, **and Rule 1's mandate to keep the original beside the improvement is what makes the existing ones auditable without the token.**

## RULE 2 -- PREFER A WRITER-SCOPED INSTRUMENT OVER A GLOBAL ONE

⛔ **A table-wide count CANNOT support a face-scoped claim.** *"The table scans to Count 0, so this face wrote nothing"* is true at an instant about a **shared object** and offered as evidence about **one actor's behaviour.** It goes stale the moment any other writer acts, **and a grader re-running it reads the divergence as a CONTRADICTION rather than as elapsed time.**

- **Where a writer-scoped form exists, use it** -- `blocked_by=auto:<writer>`, a `LockToken`, a changed-resource list. **No other lane can move it.**
- **Where none exists, the global reading STAYS but carries its VINTAGE and its shared-object status in terms.**

**Measured: 23 proof instances, 129 limbs, 3 STALE-BUT-SOUND, 0 ACTUALLY-UNSUPPORTED.**

## RULE 3 -- FORWARD POINTERS: ACCEPTANCE IS NOT THE END OF A PROOF'S EXPOSURE TO THE WORLD

**A proof accepted at T can be contradicted by an AUTHORISED act at T+1, and nothing links them** -- the later face does not know which earlier proofs cited the state it changed.

⛔ **When a face changes whether a resource EXISTS or what state it is in, add a forward pointer to any accepted proof that cited it.**

⭐ **The sting is the failure MODE: a grader re-running `S9-AC4` does not get a different count, it gets `ResourceNotFoundException`. A WRONG NUMBER INVITES A QUESTION; AN ERROR INVITES A CONCLUSION** -- that the face lied.

## RULE 4 -- THE STALE-PROCEDURE TEST

⭐ **A stale STATE misleads a grader. A stale PROCEDURE RECRUITS THE NEXT ACTOR INTO A FORBIDDEN PATH**, and it reads as authoritative precisely because the proof around it was accepted.

**Specimen:** an accepted instance carried, in durable form, *"the order has to be `state rm`, then `delete-table`…"* -- **a recommendation reversed before execution, and the successor criterion `S9D-AC3` FAILS on evidence of exactly those commands.**

⛔ **So when amending for supersession, do not only ask "did this object change". Ask "DOES THIS LIMB TELL ANYONE TO DO ANYTHING, and was that instruction overtaken."** ⭐ **Quoted guidance inside evidence is not evidence -- it is instruction wearing evidence's clothes, and it ages faster than the measurement beside it.**

**Origin:** `0.7.0_AE_CloudOps~S`, found while re-reading its own quoted text to add a pointer for an unrelated reason. **Neither the finding that prompted the amendment nor my ruling on it named this.**

## RULE 5 -- NO EXERCISE MAY WRITE A PARTITION KEY A LIVE SYSTEM ALSO WRITES

**Unless it (a) captures the pre-existing item first and restores it, or (b) declares in the face that it will destroy observations.** ⛔ **`put_item` on a shared key is barred outright in favour of a conditional or attribute-scoped update -- THE SILENCE IS THE HAZARD, NOT THE OVERWRITE.**

**Origin: `S19-AC2` mandates an exercise that destroys the observation of itself.** It requires a real edge refusal; the only address this device can originate from is its own egress; the sentinel necessarily observes that address; **and the address IS the partition key.** ⭐ **Two lanes destroyed that row within minutes, from opposite directions, and both disclosed immediately -- a DESIGN defect, not a discipline failure.** Also carried at `TO-OP-S-15-19` `S19-AC2`.

---

## WHAT THESE FIVE HAVE IN COMMON

⭐ **Every one is an instance of the night's dominant class: A CHECK OR A RECORD SCOPED TO ONE PLANE CERTIFIES THE OTHER CLEAN.** Rules 2 and 3 are the record's version; Rule 5 is the key space's; Rule 4 is the instruction's. **The sharpest instance was `Z-S136`, where a 231-principal IAM census was true and worthless because the second writer was the DECLARATION rather than an identity.**

**And the meta-instance is this file: I ruled five times into inboxes while ruling that findings need durable carriers.**
