# CERT -- `D1_CATVIEWS.TO-R1-AE` **4 of 4** -- the reserved-category reland

**Certifier:** `3.0.0_SA_CVO~Z` - **Issued:** 2026-08-28T~23:4xZ
**Executor:** `0.7.0_AE_CloudOps~Z` - **Instance:** `.../0.7.0_AE_CloudOps/deliverables/D1_CATVIEWS.TO-R1-AE_PROOF_OF_SPEC.json` @`7c827e64e8`
**Face:** `.../0.7.0_AE_CloudOps/task_orders/D1_CATVIEWS.TO-R1-AE.reland-and-refire-on-andrews-word.md`

```
rc 0  VALID  (captured UN-PIPED)   acceptance rows 4   violations 0
alignment ENFORCE:  forward-1 4/4 . forward-2 2/2 . backward 2/2
decomp id space 10 . vintage_commit 42ea71d3de RESOLVES
instance sits EXACTLY at the face's declared <instance_path>
```

## 1. WHAT THIS TO DID

Executed `mdpf_refresh.py --reland --confirm` against the 16 conflict-held gold keys **on Andrew's
explicit in-session word** (*"yes reland once all fixes are in"*), then re-fired the floor. It is the
only reserved-category act of the session. The served plane it produced is what
`cvoZ_FINAL_RATIFICATION_20260828.md` ratifies at AC1/AC2.

## 2. STOP: MY FIRST RUN RETURNED **INVALID** AND THE FAULT WAS MINE

```
  my regex        '[A-Z0-9]+-TOR1-AC[0-9]+|CATV-[A-Za-z0-9]+-AC[0-9]+'
  scraped         CATV-TOR1-AC1..AC4  PLUS  CATV-TON1-AC7
  produced        "expected=5 carried=4" + "VIOLATION: CATV-TON1-AC7 ... SILENT OMISSION"
  THE TRUTH       <expected_criteria> declares FOUR. CATV-TON1-AC7 appears ONLY IN PROSE
                  at :49 and :54, discussing a DIFFERENT TO's criterion.
```
>> **A fully-formed INVALID worded as "silent omission" -- which describes a careless filer -- against
   an executor who did nothing wrong.** <<

**FOURTH INSTANCE OF THIS SHAPE AT THIS SEAT TONIGHT.** I wrote the warning myself in
`cvoZ_ETFS_INGEST_TO6_TO8_FULL_CERTIFICATION_20260828.md`: *"an empty expected set does not error --
it produces a fully-formed INVALID that blames the executor."* Tonight's variants were **EMPTY** (an
`ls` classify `*` broke the grep) and now **POLLUTED** (a regex matched prose). **Same output,
opposite causes.**
**STANDING FIX, and it is the only way this seat does it now:** parse `<expected_criteria>` -- the
DECLARED element the checker itself treats as authority. **A face is prose plus a declaration, and
only one of them is the spec.**

## 3. WARN: AND THE TO ID IS NOT UNIQUE ESTATE-WIDE

```
  find -name "*TO-R1-AE*"  ->  FOUR faces:
    D1_CATVIEWS . WSE_COTMDL . ADVI_PERFRP . MDPF_COTREMEDIATION
```
My first lookup returned `MDPF_COTREMEDIATION.TO-R1-AE` and I nearly read **its** closed-status block
as this TO's. **A bare `TO-R1-AE` is not an address; `D1_CATVIEWS.TO-R1-AE` is** -- the same class as
the full-serial rule for agents.

## 4. SCOPE

- Certifies the INSTANCE against its face. It does **not** re-certify the served data -- that is
  `cvoZ_FINAL_RATIFICATION_20260828.md`, AC1/AC2, 28/28.
- `2.0.0_SA_COO~Z`'s 14721 classification of this face as a REAL GAP was **correct at its vintage**:
  the instance was filed 23:38Z, six minutes after that measurement. Nothing to retract.
- Push state: LOCAL at authorship; push is the integrator's leg.

-- `3.0.0_SA_CVO~Z`
