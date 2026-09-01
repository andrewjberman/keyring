# ANDREW-DIRECT 2026-09-01 ~02:4xZ -- D8 PLACEMENT, D2 SCOPE, AND THE COT EGRESS WORD

**Seat:** `1.0.0_SA_CTO` (CTO terminal, Andrew present)
**Recorded:** 2026-09-01 ~03:0xZ, after the authorized act had already fired and returned
**Why this file exists:** `0.6.2_AE_PartnerETL` (msg 90586) correctly flagged that it executed a
vendor-egress order for which **no committed durable record existed** -- its four-condition test's
condition 3 was UNMET at fire time. The 23:20Z order it compared against had `fad321cf07` and told
that seat to READ the record rather than trust an assertion. This one had nothing. That gap is
this seat's, and this file closes it.

---

## 1. THE WORDS, VERBATIM

Andrew's free-text direction at 02:4xZ:

> "D8 should be on this device. I want everything done on D2 first, and then D8 self-heal work all
> done and ad hoc run issued."

Two follow-on rulings were taken on a **structured multiple-choice ask** put by this seat, not as
free text. **The distinction is recorded because it changes the evidentiary weight**: the wording of
each option was authored by this seat, so what Andrew ratified is the option text, and any defect in
that text is this seat's, not his.

**RULING A -- D2 scope.** Selected option, verbatim:
> "The 22 open TOs only -- Narrowest reading. Finishes everything in flight, fastest path to D8.
> Leaves the roster columns unpopulated and Cottonwood unkeyed -- both survive the publish."

Consequence he accepted with the cause in front of him: **at D2 completion the Net Worth roster
still shows 6 of 8 columns unavailable.** `ADVI_ROSTERCOLS` and `ADVI_COTKEY` draw no seat.

**RULING B -- the Cottonwood hole and the vendor-egress word.** Selected option, verbatim:
> "Close it now as a carve-out -- Fire the one-shot --date 2026-08-31 re-run ahead of D2; everything
> else in D8 still waits. Treats your sentence as the vendor-egress word 0.6.2_AE_PartnerETL is
> holding for. The hole is a permanent bronze gap that does not self-heal."

with the detail line: **"Egress: this answer = the per-use word."**

**SCOPE OF THE EGRESS WORD, as relayed at msg 90576:** ONE run, `--date 2026-08-31`, no `--force`,
no adjacent date, no backfill. Explicitly NOT the `ADVI_BDPARITY` W2 census pull, which remains
open at Andrew. **SPENT AND LAPSED** as of 02:49:51Z.

---

## 2. PLACEMENT: D8 -> THIS DEVICE (LAPTOP)

Reverses the 2026-08-26 move to SITEZ, **and lifts a standing directive** -- `DIRECTIVES.yaml:57`
carries Andrew-direct 2026-08-27 ~00:0xZ verbatim: *"D0 D2 D3 D5 D10 D11 stay here until I say
otherwise. the rest is all on sitez."* D8 is in "the rest"; the clause is his to lift and nobody
else's; at 02:4xZ he said otherwise, for D8. **Scoped to D8 -- no other member of "the rest" moves.**

**Device-identity grounding (CORRECTED, per `3.0.0_SA_CVO` 90584 -- accepted in full).** The
original three-carrier claim was wrong at the width stated: `hostname` and
`.register-owner: owner_hostname` are ONE carrier sharing the string `Andrew`, and D8's own cell
establishes D8's history rather than this device's identity. The grounding that holds is
BEHAVIOURAL and survives the string being wrong:

- `DIRECTIVES.yaml:21` -- `SITEZ = D6/D7/D9/D8; LAPTOP = D0/D1/D2/D3/D4/D5`
- `DIRECTIVES.yaml:57` -- D2 placement LAPTOP, Andrew both consoles: *"D2 is certainly laptop
  fabric"* / *"sitez does not work on advi, D2"*
- this fabric executed D2/`ADVI_PERFRP` work continuously through the night

**This device does D2; D2 is ruled LAPTOP; therefore this device is the LAPTOP.**

⛔ **STRUCTURAL FINDING, ruled open:** the estate has NO machine-readable hostname-to-token map.
`comp-find "owner_hostname|device_token"` returns 3 hits across 381 files and `device_token` returns
ZERO. The join exists only in an agent's head and in one parenthetical in an 8-day-old session log.
**The join must become machine-readable; `0.0.0_AB_MSTR` owns `.register-owner` and the act is its
call.** Proposing is legal, installing is not.

---

## 3. ⛔ WHAT THE AUTHORIZED ACT ACTUALLY PRODUCED -- AND THE DEFECT IN HOW IT WAS PUT

`0.6.2_AE_PartnerETL` fired at 02:49:51Z on order 90576 and returned **NOT-CLOSED**, verified on the
artifact with a named positive control (2026-08-30, a date known complete, read through the
identical query shape): 08-31 shows `rebalancer_model_detail` 0 against the control's 83, and the
`meta/<date>-complete.json` stamp ABSENT against the control's PRESENT. **The hole is OPEN; 0 of 3
feeds complete.** The failure was byte-identical to a run 3.4 hours earlier -- same strategy, same
`roster 15 / observed 14`.

>> ⛔ **THE SPENT WORD IS THE FINDING, NOT THE FAILED RUN.** `0.6.2_AE_PartnerETL` had recorded a
   FALSIFIABLE PREDICTION at msg 90345 that a re-fire would fail identically. It was fired and the
   prediction was not falsified. **Andrew spent a per-use vendor-egress word on an act that was
   predicted, on the record, to be incapable of succeeding.** <<

**THIS SEAT'S SHARE, stated plainly.** The option text Andrew ratified said *"The hole is a permanent
bronze gap that does not self-heal"* -- true, and the reason to act -- but it **did not disclose that
the re-run was predicted to fail.** This seat authored that text. It built the recommendation from
the `MDPF_HEALGAP` registry record ("Today's hole stays open until Andrew rules on the one-shot
re-run"), which frames the act as awaiting his word and **does not carry the executing seat's
prediction about the act's outcome.** This seat did not ask the executing seat before framing the
option as Recommended.

⭐ **THE TRANSFERABLE LESSON, and it is new:** **THE REGISTRY RECORD SAYS AN ACT IS AWAITING A WORD.
IT DOES NOT SAY WHETHER THE ACT WILL WORK. Only the seat holding the staged act knows that, and its
prediction lives in ITS session, not in the record the decision-maker reads.** Before converting a
staged act into a sovereign question, ASK THE STAGED SEAT WHETHER IT EXPECTS THE ACT TO SUCCEED.
A sovereign word is a finite resource and this one was spent on a foregone conclusion.

**WHAT WOULD ACTUALLY CLOSE THE DATE -- neither is ours:** BD's roster catching up to its own account
book (15 -> 14), which is vendor-side and unchanged across 3.4 h; or the vendor-stale classification
discriminator, **which by this seat's own ruling still would not stamp the date** ("both worlds still
stop the stamp"). **A third fire against unchanged vendor state will fail a third time.**
`0.6.2_AE_PartnerETL` is not asking for another word and would decline to spend one; that judgment
is endorsed here.

---

## 4. STATUS OF ANDREW'S ENDPOINT AFTER THIS

- **"ad hoc run issued"** -- SATISFIED as literally stated. The run was issued and fired.
- **The hole it was issued to close** -- STILL OPEN, and **not closable by us** under present vendor
  state. If his intent was the closed hole rather than the issued run, the endpoint is NOT met and
  the remaining path is vendor-side.

**That distinction is his to resolve and is not resolved here.**

---

## 7. ⛔ CORRECTION 2026-09-01 ~03:3xZ — THE PREMISE OF SECTIONS 1(B), 3 AND 4 IS FALSIFIED. APPENDED; ALL PRIOR TEXT PRESERVED VERBATIM.

**ANDREW-DIRECT ~03:2xZ, VERBATIM:**
> *"remember how data is always D+1? today is 8/31 eastern, so all this talk about 8/31 not existing
> is not a data hole"* · *"we wouldnt be able to get that until tomorrow 9/1"* · *"8/28 is Friday, it
> is the last day we have data"* · *"because its the last trading day"* · *"prior to today"*

**MEASURED ON THE CALENDAR THIS TURN:** 08-27 Thu · **08-28 FRIDAY, the last TRADING day** · 08-29
Sat · 08-30 **SUNDAY** · 08-31 **MONDAY** · 09-01 Tue.

>> **DATA IS T-1. THE LATEST AVAILABLE DATA DATE IS 2026-08-28. A 2026-08-31 PARTITION CANNOT EXIST
   UNTIL 2026-09-01. THERE IS NO 2026-08-31 COT HOLE. The absence is the EXPECTED state.** <<

⛔ **CLAUDE.md §5 HARD STOPS SAYS THIS IN TERMS, AND THIS SEAT DID NOT APPLY IT:** *"NEVER call a
pipeline stale/broken until you resolve the TRADING CALENDAR — count trading days. Everything is
`T-1` unless declared; **Friday IS Monday's answer**."* One frontier exists for exactly this:
`lib/trading_calendar.py`. **This seat maintains the law file and never reached for the rule.**

**WHAT THIS FALSIFIES IN THIS RECORD:**
- §1 RULING B's ratified option text — *"The hole is a permanent bronze gap that does not
  self-heal"* — **was false at the premise. This seat authored it.** The defect recorded in §3 was
  real but was diagnosed one layer too shallow: not merely *"predicted to fail on a stale vendor
  roster"* but **"asked a vendor for a date that cannot exist yet."**
- §3's *"the blocking condition is VENDOR-SIDE"* — itself downstream of the same error.
- §4's endpoint distinction is **moot as posed**: there was no hole for the run to close.

**WHAT IS NOT FALSIFIED — the retraction is scoped to the DATE PREMISE and no wider:**
- The runner's `COUNT-RECONCILE SELF-GATE FAILED — roster 15 / observed 14` fired twice,
  byte-identically. **Whether that is a genuine roster/book defect or an artifact of requesting an
  unavailable date is UNRESOLVED**, and belongs to `0.6.2_AE_PartnerETL`, which holds the runner.
- **`MDPF_HEALGAP` as a PROJECT is not void.** Its subject — a transient auth gap converting into a
  permanent hole because nothing re-runs after the heal — is a real class. **What is falsified is
  that 2026-08-31 is an instance of it.**
- §2 (D8 placement) and §1 RULING A (D2 scope = the 22 TOs) are untouched by this correction.

⚠ **AND A CONTROL TO RE-EXAMINE THAT NOBODY QUESTIONED:** the NOT-CLOSED verdict was validated
against **2026-08-30 as "a date known COMPLETE"** — **a SUNDAY**. This estate already records that BD
silver partition KEYS are WRITE dates, not CONTENT dates, so a Sunday partition can legitimately
exist carrying Friday's content. **That is not a contradiction — it means the control was not the
control it was labelled**, and a partition-date read and a content-date claim were treated as one
measurement. Owner `0.6.2_AE_PartnerETL`. **No re-fire to resolve it; NO-THIRD-FIRE now has a second
and stronger reason.**

**THE TRANSFERABLE LESSON:** the estate had a NEVER rule, a named frontier module, and a proverb
(*"Friday IS Monday's answer"*) all pointed at this exact error — **and none of them fired, because
nothing in the chain from registry record to option text to executing seat asks "is this date
supposed to exist yet?"** A rule that must be *remembered* by the one seat framing the question is a
rule with a single point of failure, and tonight it failed at that point.
