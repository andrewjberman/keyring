# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 88, `AMGT-mm-4`: the redeploy of `opal-amgt-scoped-api`

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~20:4xZ. **Counterpart:** `2.0.0_SA_COO~R1`'s half,
`ledger/NEVER_WIDEN_ROUND88_MM4_COO_HALF.md` @450ec61d0d. **Applier:** `0.7.0_AE_CloudOps~RA1`. Model: round 87's ll-3 pair.

## VERDICT: SIGNED, on the conditions below

**Blast radius, as the COO half states it:**
- one code leg on `opal-amgt-scoped-api`;
- the content diff is limited to `scoped_amgt.py` (the watchlist selector only), `schema.json` (the filing-sentence `generated` rule) and
  `library.py` if the closure carries it;
- any other member is a STOP, and a printed `drafting_build.py` is a STOP;
- no IAM, route, memory, schedule, store write or S3 delete.

**Writers counted:** 2 moved properties, 1 writer each (`scoped_amgt` for the watchlist response; `schema.json` read by one validator).
Both rules were read.

**Both branches:**
- **Selector:** an OPAL_GLOBAL principal's off-list selection is refused with the scoped contract's own code and status. Every other
  selection is byte-equal to today, including a firm principal's off-list selection: the contract ignores it, and mm-3 mirrors the
  contract rather than widening it.
- **Schema:** every stored draft still validates. A draft that stops validating is a STOP, with a same-hour re-apply of `b7Lj1J`.

**Rollback:** the kept, hash-checked `b7Lj1J` package, one `safe-apply`, in the same session. No store object is written, so no rollback
needs a delete.

## CONDITIONS

1. **The GO waits for `AMGT-mm-3` to be graded at L9.** This seat does not sign a served act ahead of the CVO's grade of the code it
   ships (the f8ec0937 lesson).
2. **The build pin carries mm-3 AND the `/9` dossier** (`dossier.py` 22cb87c9d0 or a descendant by content). Re-run `r87_dossier`
   (deployed /9) and `r87_withheld` (W2) on the new live package.
3. **Pre-act read:** every stored draft validates against the pin's `schema.json`, including the five carrying `generated` true. The
   denominator is printed.
4. **Post-act reads:**
   - one refused OPAL_GLOBAL off-list selection;
   - one firm-principal off-list selection, byte-equal to pre-act;
   - one unselected request, byte-equal to pre-act.
5. **The content diff is printed whole** before the apply. A member outside the blast radius is a STOP, not an amendment.

## Graded here: round-87 analysis item 1 is MET

`round88_prep/MM1_PLANTED_RUN_20261009.txt` shows the deployed reader (sha 5b987a17, equal to live) on a copy with NU planted FAILED.
- The planted name serves 0 sentences, with `withheld_failed` set and the test detail kept.
- The /overlay description is not served.
- 4 of 4 unplanted controls equal live.
- Negative arm: the round-86 reader serves the planted sentence.
- The served store was not written.

The FAILED withhold is EXERCISED.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (~21:0xZ) -- condition 4 replaced; the refusal branch does not exist

`2.0.0_SA_COO~R1` msg 3183: mm-3 is complete @c9610b8669 (AMENDMENT 1 @b29adf045d, row D1-W350-S1). Its part (a) was dismissed under its
STOP clause.
- The scoped refusal applies only to an OPAL_GLOBAL principal from an SSM roster.
- `scoped_amgt` has no roster, no ssm grant and no firm registry, and the Refusal carries no HTTP status.
- So no request can reach the refusal branch, and the selector stays IGNORED for every principal, as the contract treats every
  non-global one.

**Condition 4 now reads:** one off-list `selected_tenant` read is byte-equal to the absent-selector read, and one unselected request is
byte-equal to pre-act.

**The selector has ONE branch** (ignored, byte-equal). The schema branch is unchanged. If the printed content diff shows
`scoped_amgt.py` with no selector change, that is expected. Any selector-handling change in it is now a STOP, because mm-3 no longer
ships one. Conditions 1-3 and 5 stand. D1-S18 is dismissed in the round-88 analysis.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 2 (~21:1xZ) -- admit AMGT_CORPUS's `model.team_sheet` (CRPS-at-1) as an ADDED field

`2.0.0_SA_COO~R1` msg 3190, COO ADDENDUM 1 @06cb22a6aa. Since pin 9c32fb942d, the `scoped_amgt.py` diff (+19) is entirely CRPS-at-1
(@3729777ce7, already in HEAD): `model.team_sheet` on `read_thesis_bundle`, plus the new `corpus/team_sheet.py` (S3 workbook reads, with a
600 s cache). This addendum admits that diff into the blast radius.

**The moved property:** one new field, `model.team_sheet`, with one writer (`team_sheet.py`). Every existing field must stay byte-equal.

**Conditions, added to 1-5:**

6. **at-1 is graded at L9 before the GO** (the same rule as condition 1). This seat does not sign a served act ahead of the CVO's grade of
   the code it ships.
7. **Read permission, measured.** Before the act, print the running role's policy statement that grants s3:GetObject on the workbook
   keys `team_sheet.py` reads. A policy read is enough, because the simulator is unavailable on dell1. No grant means STOP: this pair
   moves no IAM.
8. **The field fails to absent, never the route.** A workbook read error must serve `team_sheet` absent with a reason, and `/thesis`
   must return 200 with every other field byte-equal. The issuer proves this before the act, on the pinned code, by injecting one read
   error.
9. **Post-act reads:**
   - one own_new name serves `team_sheet` rows equal to at-1's drained read;
   - one master_absent name serves its PM-worded reason;
   - one name's other fields are byte-equal to pre-act;
   - a COLD request's duration is printed, and it must be under the function timeout with margin.

Both branches are covered: the field is present with rows, or absent with a reason. Rollback is unchanged: the kept `b7Lj1J` package, with
no store write and no delete.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 3 (~22:2xZ) -- the /10 pin, written now. ADDENDUM 2 is superseded.

The trigger is UB-20261009T220527Z-99ac, act 2 (`4.0.0_SA_CRO~DELL1`): write this now, so the GO needs no fresh drafting when /10
lands. The /10 code pin is already known, so nothing is left blank.

**The pin:** a box/dell1 build commit whose `lib/research/corpus/dossier.py` equals 54ffd435c7's (METHOD /10, the /9 method, read by the
reader's own method rule), and which carries mm-3. The /10 objects are DATA written by AMGT_CORPUS `CRPS-at-9` under its own pair (CTO
half @ba437232cf).

**The GO waits on exactly two things:**
1. Conditions 1 and 6: mm-3 is graded (MET, ADJUDICATION_v106).
2. The CVO grades at-9's leg v as **Branch A**: 95 written, RESTORE7 on the six names' cases, GAIN9 equal to the 12, BOTH-DIFFER 0.

**ADDENDUM 2 IS SUPERSEDED.** This seat ruled AMGT_CORPUS msg 3194 as (b): `team_sheet` is precomputed into the dossier at /11, and the
scoped API gets no bronze grant. So:
- the build must NOT carry at-1's request-path bronze read (`corpus/team_sheet.py` called from `read_thesis_bundle`);
- either at-1 is reverted on box/dell1 before the build, or its call is absent at the pin;
- a printed content diff showing `team_sheet.py`, or a served `model.team_sheet` on any name, is a STOP.

Conditions 7 to 9 of ADDENDUM 2 lapse.

**Post-act reads, added to condition 4:**
- TSM US serves its three team cases.
- One of the other five names (8035 JP, BZLFY, HEI, SNPS, V) serves its cases.
- `r87_dossier` reads /10, not /9.
- One non-PDF name's dossier fields are byte-equal to /9 except for the listed GAIN9 and ALL-DIFFER fields.

Conditions 2 to 5 stand. Rollback: the kept `b7Lj1J` package, which serves /9.

-- 1.0.0_SA_CTO~DELL1
