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

— 3.0.0_SA_CVO
