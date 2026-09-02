# ANDREW-DIRECT 2026-09-02 ~18:12Z — rulings on the three `/open-calls` cards (CVO base terminal)

**Channel:** CVO base terminal, in response to `/open-calls` rendered at ~18:0xZ.
**Recorded by:** `3.0.0_SA_CVO` · **Broadcast:** same turn, to `1.0.0_SA_CTO`, `2.0.0_SA_COO`, `0.0.0_AB_MSTR`,
`0.8.0_AE_CloudComp`.

> **NEVER A PARAPHRASE. THE PHRASING *IS* THE RULING.**

---

## THE WORD, VERBATIM

> recs approved except 2, right now i think the estate pipeline is probably junk for the most part, until the tools
> at the front of that pipeline are properly rectified and generating real outputs/data, i dont think that pipeline
> makes sense to analyze analyses from.

## THE CARDS IT ANSWERS (as rendered to him, minimal decision + REC)

```
CALL 1  comp-kuzu consolidation: (a) collapse to `comp-kuzu --mode inc|full` and retire the two
        name-wrappers, or (b) keep the names as thin aliases?
        REC (a), with the NEVER-full guarantee moved onto `--mode inc` explicitly and KUZUSPLIT
        P1/P3 + comp-which/comp-describe routing + comp-manifest-check amended in the same commit.
                                                                          -> APPROVED  (a)
CALL 2  Run the /estate-pull adjudication loop on the 24 PENDING manifest days now, or leave them?
        REC yes, one sitting, oldest first.
                                                                          -> REJECTED
CALL 3  Re-arm the step-8 surprise-channel notifier (`surprise-watch.sh` Monitor) this session
        -- yes/no?   REC yes.
                                                                          -> APPROVED
```

---

## THIS SEAT'S READING (marked as such)

**CALL 1 — APPROVED (a).** His 07-17 word (two named commands) and his word today (flags) are reconciled by HIS
choice: the engine's existing `--mode inc|full` becomes the surface; `comp-kuzu-inc` and `comp-kuzu-full` retire;
the **NEVER-full property moves from the `-inc` NAME to `--mode inc` explicitly**; `NFRA_KUZUSPLIT_PRD.md` P1/P3,
`comp-which` routing (`:614`, `:620-621`), `comp-describe` (`:24`) and the `comp-manifest-check` registration all
move **in the same commit**. Row T-22 goes CARRIED → executable. Executor `0.8.0_AE_CloudComp` (engine owner);
callers to notify: `1.0.0_SA_CTO` (7), `4.0.0_SA_CRO` (6), `1.0.0_SA_CTO~B` (1) — measured 30d.

**CALL 2 — REJECTED, and the reason is a ruling about the Semantic Evolution Pipeline itself.** *"the estate
pipeline is probably junk for the most part, until the tools at the front of that pipeline are properly rectified
and generating real outputs/data."* Reading: **the daily estate report is DOWNSTREAM of `NFRA_COMPEFFICACY`.** Its
inputs are the comp-tools this project audits; adjudicating its outputs before those inputs are cleared would be
"analyzing analyses" of unrectified instruments. The 24 PENDING days stay PENDING by his word. This is consistent
with the measurement already in the PRD draft: the runner's propagation stratum returns `INSTRUMENT_UNAVAILABLE`
daily and invokes zero comp-tools (§5b of the review; PRD row G-rows). **PRD amendment:** FWD-7 / §1 carry this as
a binding statement — the estate report is a CONSUMER of this project's outcome, not a parallel workstream.
⚠ **NOT read into it:** that the pipeline is to be stopped, retired, or changed. He said its analyses are not worth
adjudicating *until* the front tools are rectified. The runner keeps running; nobody acts on its output.

**CALL 3 — APPROVED.** Re-arm `org/surprise_channel/surprise-watch.sh` as a persistent Monitor this session. The
NEVER-monitor moratorium's condition ("unless Andrew explicitly asks") is met by this word for THIS notifier. Not a
general lift.

**Aftercare:** CALL 1 executes via a delegated unit to `0.8.0_AE_CloudComp` (unhold). CALL 3 executes at this seat
now. CALL 2 records; nothing executes.

---

## FOURTH WORD, SAME TERMINAL, ~18:38Z — the §4.4 posture APPROVED + a reconciliation instruction

> I agree with this posturing, incorporate it into the document, also make sure that the document is updated as
> needed based on 0.8.0_AE efforts this session so that it is not deprecated on those surfaces considering it is
> written before their work to some extent. It looks like they've just committed T-16 for refrerence, you should
> get in touch with them and have them clarify what they've done and what is still pending so that the document
> can be updated properly.

**"This posturing" =** the two-rule proposal put to him in the same thread: **Rule P** (comp-find's page contract as
the shared output contract — `--limit/--page/--all`, `PAGE i of N`, true total on every page; a bare `--top N` is
non-conforming) and **Rule T** (a tool never exceeds a ceiling it was not told — accept a budget defaulting to the
harness's 120s, spend it against work, print the reached denominator + resume cursor at expiry; internal timeouts
≤ the declared budget). Landed as PRD draft §4.4 + §4.4.1 the same turn.

**Reading:** two acts — (1) amend §4.4 (done); (2) reconcile every row `0.8.0_AE_CloudComp` touched this session
to its landed state, sourced from that seat's own account (asked, 92670), not from this seat's memory of the
thread. **Not read into it:** any change to scope, rows, or dispositions beyond what their work made true or false.

---

## FIFTH WORD, SAME TERMINAL, ~20:4xZ — `/next-steps` + `/open-calls`: "All approved go"

> All approved go

**Answers, as rendered to him:** four `/next-steps` options — (1) watcher pass 2, cross-poll provisional-then-confirm
+ the recovery and concurrent-append controls [DEFAULT, self-executable]; (2) session log; (3) unit 3 to
`0.8.0_AE_CloudComp` (comp-adversary `comp_log_auto` emit + a comp-find battery) [sequencing `2.0.0_SA_COO`];
(4) marquis retire/elevate proposal DRAFT from s.7 evidence [acting on it stays his word per FWD-5] — **all
approved.** And `/open-calls` CALL 1 — keep the fabric-workflow lane MERGED at CVO base vs spawn a replacement
~A; REC keep merged until step-5 deliverables start landing for grade — **approved as recommended.**

**Reading:** the four options are DIRECTION (executed in rank order at this seat; (3) delegated now, landed on COO's
sequencing). CALL 1 is RULING-shaped (staffing): recorded here verbatim, broadcast same turn. **Not read into it:**
authority to act on the marquis draft — the draft is produced; retirements beyond those separately ruled remain his.

— 3.0.0_SA_CVO
