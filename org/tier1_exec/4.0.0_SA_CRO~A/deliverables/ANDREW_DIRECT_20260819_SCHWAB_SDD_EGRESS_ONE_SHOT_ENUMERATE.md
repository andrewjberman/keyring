# ANDREW-DIRECT 2026-08-19 ~1450Z (CRO~A terminal) -- SCHWAB SDD EGRESS GRANTED, one-shot enumerate

**Channel:** Andrew live at the 4.0.0_SA_CRO~A terminal, in the FAM feed-hole thread (following the
triage + FAM explainer, where the option was framed: "your egress word for a one-shot vendor-side
enumerate (ask Schwab's endpoint directly what it has listed)").

## VERBATIM

> "I give you egress to go check it out"

## SCOPE AS STATED (recorded, not adjudicated)

The word answers the framed option it replies to: a VENDOR-SIDE READ of the Schwab SDD (Schwab Data
Delivery) endpoint to check FAM availability for account 08335338 -- i.e., enumerate what Schwab
lists, specifically whether FAM files after CS081026 (as_of 08-10) exist. It is a per-use grant for
THIS check ("go check it out"); it does not add Schwab SDD to the standing lifted-vendor list, and it
is a READ -- any landing of files remains the scheduled puller's job (which downloads whatever the
vendor lists, next fire 21:45Z).

**Executor:** 4.0.0_SA_CRO~A (the addressed seat). **Broadcast:** CTO + COO + MSTR inbox, same turn.

---

## EXECUTED + RESULT (2026-08-19 14:54:41Z, same grant)

**Mechanism:** the deployed `sdd-daily-pull.ps1`'s own `-Mode enumerate` (downloads nothing; search
half only), fired via the IDENTICAL applied SSM recipe the schedule uses (fresh S3 pull of the script
-> interactive Administrator task), SSM command `1c1fce17-06de-4d10-9f86-bf596edde858` on
`i-0f3d57a97f14727af`. rc=0, stderr empty. One vendor call (the single wide search 2026-07-20..08-19,
never chunked), 284 files enumerated.

**RESULT -- the vendor-side verdict is now CONFIRMED AT THE ENDPOINT ITSELF:**

```
/acc  n=22  20260720..20260818     <- siblings run to the T-1 frontier (2026-08-18)
/fam  n=15  20260720..20260807     <- FAM STOPS at AsOfDATE 2026-08-07 (Fri)
/rps  n=22  20260720..20260818
/sec  n=22  20260720..20260818     (slm/tcf/tcfx/trn/uln/ult/upn/upt likewise n=22 to 08-18)
```

Schwab's SDD endpoint LISTS NO FAM FILE for master 08335338 with AsOfDATE after 2026-08-07 -- while
every daily sibling type lists 22 files through 2026-08-18. The differential (15 vs 22, same search,
same window) is the proof: not our pull, not boundary-loss, not a lane defect. Date framing: last FAM
= AsOfDATE 2026-08-07 (content date; the CS081026 delivery), so the hole is 7 trading days at content
grain / 6 at delivery grain as previously counted. **Consequence: no pull mode can fetch what the
vendor does not list -- SCHWAB CONTACT is the only path to R.** Tonight's 21:45Z fire lands nothing
FAM-wise unless the vendor resumes.

**Grant retired:** one vendor call made, read-only, session lock acquired/released cleanly; the
per-use egress is now CONSUMED. Surprise (banked, no chase): the enumerate display shows `/rly n=1
2..1` and `/rty n=1 2..1` -- a malformed-looking date-range render on two sparse types; canonicalizer
raised nothing (284/284), so likely a display artifact of the enumerate branch; owner of the script =
0.6.2/AE lane.
