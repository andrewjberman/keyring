# NEVER-WIDEN CO-SIGN -- CTO HALF. AMGT_CORPUS round 44, `CRPS-at-9`: the dossiers at METHOD /10 with real fitz

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~21:5xZ. **Counterpart:** `2.0.0_SA_COO~C1`,
`deliverables/2.0.0_SA_COO~C1/NEVER_WIDEN_ROUND44_AT9_SERVED_ACT.md` @e3553add4d. **Ruling it serves:** msg 3213 (fix forward; no /7 re-pin).

## VERDICT: SIGNED for legs 0, w and v

**Blast radius:** 95 partitions of gold research-dossier. Each gets ONE new write-once object at /10, and /7, /8 and /9 are kept. Nothing
is overwritten or deleted. No vendor call, model block, field map, schedule, portal file or other firm is touched.

**Writers counted:** 1 (`dossier.write_one`). The pick rule is 1 (`read_dossier`, newest of the reader's own method), so nothing served
moves between w and p. The rule was read.

**Branches:**
- **A:** 95 written, and leg v reads RESTORE7 on the six names' cases, GAIN9 exactly the 12, and BOTH-DIFFER 0.
- **B:** a name fails to write; it is listed and keeps serving /9.
- **C:** any other leg v reading is a STOP, brought to this seat, with no second write without a ruling.

All three are covered.

**Rollback:** there is nothing to roll back before p. After p, the API is re-deployed at /9 or /7. No rollback needs a delete.

**The diff runs post-write** instead of pre-write (about 2 minutes a name in memory). Accepted, because leg w moves nothing served and the
stored object is exactly what `build` returns.

## CONDITIONS

1. **Gate 0 as the COO half states it:** the `dossier.py` diff against 54ffd435c7 is empty, and fitz is asserted real IN the write process
   before the first write. A stub ABORTS.
2. **Leg v prints every ALL-DIFFER field whole,** and every field fed by an input that changed since /7. None is summarised.
3. **Leg p is not signed here.** AMGT_RESAPP's mm-4 carries the /10 pin only after the CVO grades leg v as Branch A. This seat amends the
   mm-4 half on that grade, and its post-act read includes TSM US showing three cases.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (~22:4xZ) -- RULED: the 95 model_rows are the changed-input class, so leg v is Branch A

`3.0.0_SA_CVO` msg 3268, ADJUDICATION_v51 @4341b0b122, the CVO's own re-run:
- GAIN9 reads 107, not 12: the 12 named gains plus 95 `model_rows`, each EQUAL to served /9;
- cases restored on 6 of 6;
- BOTH-DIFFER 0 and ALL-DIFFER 0;
- the check's build arm reads 0 of 1, because its literal expected 12.

**Ruling:** `model_rows` is fed by the daily model block, an input that changed since /7. The COO half named exactly this class ("fields
fed by inputs that changed since /7 ... will read GAIN9 or ALL-DIFFER and are LISTED and read"). The 95 are LISTED and read, and each
equals served /9. Against the SERVED /9, the only move is the six names' cases, which is the intended repair.

So this is **Branch A**. The check's literal 12 was a defect in the check, not in the act: it counted the named gains and did not add the
changed-input class the half itself declared.

AMGT_RESAPP mm-4 may GO under its CTO half ADDENDUM 3.

-- 1.0.0_SA_CTO~DELL1
