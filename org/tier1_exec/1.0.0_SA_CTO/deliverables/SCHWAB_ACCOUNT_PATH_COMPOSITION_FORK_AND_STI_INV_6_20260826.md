# The schwab account-path composition fork -- three readings, and the standing control whose fate rides on it

**Seat:** `1.0.0_SA_CTO`. **When:** 2026-08-26 ~03:3xZ UTC.
**Status:** OPEN. **Not mine to rule** -- see s4.

> ⛔ **RECORDED BECAUSE IT EXISTED ONLY IN A MESSAGE (71964).** I spent last night telling four seats
> that the message scrolls and the artifact persists, then recorded my own gate verdicts
> (@`de631c0a28`) for exactly that reason -- and left this one in an inbox. Second instance, same
> seat, same night.

---

## 1. THE MEASUREMENTS (two seats, two instruments, neither re-running the other)

**`0.4.0_DS_ClientPlatform~Q` / `2.0.0_SA_COO` (71953) -- ROW COMPOSITION:**
```
  schwab/silver/account_xref, 7,486 rows:
     0008242234 (MDPF Model Portfolios)  6,997  |  <NA> 489  |  0008335338 (ADVI)  ZERO
  the dataset under s3://opal-data-assets/schwab/08335338/gold/dimensions/dim_account/
     overlaps the 08242234 subset at 6,926 of 6,997, and the 08335338 subset at 0 of 0
```
**A dataset under the ADVI (`08335338`) path populated entirely with MDPF (`08242234`) accounts.**

**`1.0.0_SA_CTO` (71964) -- TREE TOPOLOGY, `s3 ls`:**
```
  s3://opal-data-assets/schwab/  ->  PRE 08242234/   PRE 08335338/     both trees exist
  schwab/08335338/  (ADVI)       ->  _ops  bronze  GOLD  meta  silver
  schwab/08242234/  (MDPF)       ->  _ops  bronze        meta  silver   <-- NO GOLD LAYER
```
⛔ **There is exactly ONE gold layer under `schwab/` and it sits on the ADVI path.** So the measured
dataset is **not a duplicate of an MDPF gold tree -- it is the only schwab gold tree there is.**

⚠ **LIMIT PRINTED RATHER THAN LEFT IMPLICIT:** `s3 ls` at one prefix level shows which layer
directories EXIST. It does not show what writes them, what reads them, or whether an MDPF gold home
exists under a different bucket or grammar. **I searched `opal-data-assets/schwab/` and nothing else.**

## 2. THE FORK -- THREE READINGS, NOT TWO

`2.0.0_SA_COO` offered two; the topology makes a third equally live, and **they take opposite actions:**

| | reading | action it implies |
|---|---|---|
| (a) | the tree is MISFILED | MOVE data -- and moving a served key is NEVER#3 |
| (b) | `account_xref` is legitimately MDPF-scoped; the 49F linkage lives elsewhere | leave it; go find the linkage |
| (c) | **the schwab gold tree is a SINGLE SHARED HOME and the account-number path segment is NOT A SCOPE BOUNDARY AT ALL** | leave the data; fix what the PATH is allowed to IMPLY |

**Under (c), "repairing" it by moving the tree would BE the defect.** `2.0.0_SA_COO` accepted the
non-MECE finding against their own taxonomy at 71966: *a fork is a classification schema, and mine
failed Rule 24(i).*

## 3. ⛔ THE COUPLING I DID NOT NAME, AND `3.0.0_SA_CVO` DID (72050)

`ADVI_STITCH`'s decomp carries **`STI-inv-6`**:
> *FIRM + ACCOUNT-SET SEPARATION: 49F only; **08242234 rows are EVIDENCE, NEVER A SUBSTITUTE** for
> 08335338.* Oracle: *"CVO-class control -- no 08242234 key in any landed path or census input; the
> two account sets never summed."*

**IT WAS NEVER CUT INTO A TASK ORDER.** `3.0.0_SA_CVO` executed its PATH arm anyway rather than filing
it:
```
  bronze_legacy   0 of   931 | silver_legacy 0 of 7,921 | gold/advi/reference 0 of 7,283
  POSITIVE CONTROL  s3://opal-data-assets/schwab/08242234/  ->  17,378 keys
  => the token is emphatically findable; the three zeros are MEASURED ABSENCES, not dead filters
```

⛔ **THE CONSEQUENCE I MISSED WHEN I MINTED READING (c).** My 71964 said the three readings "take
genuinely different actions" and listed them. **It did not trace what (c) does to `STI-inv-6`.**
**If the account-number path segment is ruled NOT a scope boundary, `STI-inv-6` LOSES ITS MECHANICAL
CARRIER** -- the path-arm oracle (*"no 08242234 key in any landed path"*) is only meaningful if the
path segment MEANS something. **The control then survives on prose alone, guarding two account
numbers four digits apart.**

>> **I HUNTED THE UNCOVERED MEMBER AND DID NOT TRACE ITS DOWNSTREAM EFFECT. Finding the third value
>> of a schema is half the act; the other half is asking what ELSE that value decides.** A fork that
>> silently re-rules a standing control is worse than a two-member fork, because it looks more
>> complete. `3.0.0_SA_CVO`'s framing is the correct one and I am adopting it: **the two questions are
>> ONE question and must not be settled separately.** <<

## 4. DISPOSITION -- NOT MINE, AND THE REASON IS A STANDING RULE

**PRODUCT-vs-FIRM SHAPE IS NOT A RULE IN THIS ESTATE.** Andrew specifies it per instance; no seat
derives one. D8/D10's PRD says the same about gold homes and explicitly does not authorise migration.
**So the home question routes to Andrew via the tree's owner.**
Both measurements are of COMPOSITION and TOPOLOGY. **Neither is INTENT, and no measurement I can take
is** -- the question is what the tree is FOR.

**WHAT THE RULING MUST ALSO DECIDE, or it is incomplete:** what carries `STI-inv-6` under the reading
chosen. Under (a)/(b) the path arm stands. **Under (c) it needs a different carrier or an explicit
acceptance that the invariant is prose-only.**

## 5. STILL UNCARRIED AND UNOWNED -- the summation arm

`STI-inv-6`'s oracle has a SECOND clause: **"the two account sets never summed."** That is a claim
about **COMPUTATION, not paths.** `3.0.0_SA_CVO` did not test it and explicitly declined to absorb it
into a cert that cannot support it -- correct. **It needs a read of the census inputs and every
summation site, and it has no owner.**
⛔ **AN UNCARRIED CELL IS INVISIBLE TO EVERY DOWNSTREAM CHECK, BECAUSE EVERY CHECK JOINS ON THE
CRITERIA.** This is shape 1 of the join-hole family (@`8ca4e07f00`) with a live instance and a
standing NEVER-SUBSTITUTE control as its subject. **Seating is `2.0.0_SA_COO`'s.**

## 6. WHY THIS INVARIANT SPECIFICALLY

`08335338` = ADVI Advisor Intelligence. `08242234` = MDPF Model Portfolios. **Held distinct BY
STANDING RULE -- never substituted, never truncated, never summed.** The measured composition is not
a near miss on that rule: it is the whole population on the wrong side of it, under a path that names
the other account. Whether that is a violation or a misleading path is precisely the fork above.
