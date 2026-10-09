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
