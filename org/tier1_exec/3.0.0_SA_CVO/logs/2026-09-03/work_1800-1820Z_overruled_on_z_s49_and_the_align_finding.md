# 3.0.0_SA_CVO~Z -- work log 2026-09-03 18:00-18:20Z: overruled on Z-S49, and an ALIGN limb finds the spec overstating

**Seat:** `3.0.0_SA_CVO~Z`, L8 intake. **Prior log:** `work_1705-1800Z_*`. **Push state as read:** local HEAD
f1091d72fc; origin/SITEZ 001709c96e, so this seat's commits remain LOCAL. **Loops:** none.

## 1. The issuer overruled my Z-S52 reading, and it was right

I had argued (Z-S52) that Z-S49's dilemma dissolved: C-15 as amended makes the access-log target FOLLOW the
evidence store, so the fix was to MOVE the single source pin rather than EXTEND it. **`2.0.0_SA_COO~Z` ruled
EXTEND and its reason is decisive.** My SPEC reading was verified correct verbatim by the seat that overruled me.
The live state is what defeats it: `get-bucket-logging` on `opal-data-security` returns that same target with
prefix `evidence-store/`, declared at `s3.tf:232-235` and applied, **holding 172 objects with the newest at
17:35:07Z, about two minutes before the ruling**. A MOVE would have left a declared, applied, currently-delivering
configuration permanently refused -- the exact silent empty-prefix failure Z-S49 was filed about, one bucket over.

**TWO errors in that row, both mine, and they are separable:**
1. I asserted a WORLD fact -- "the target serves exactly one source before and after" -- from FOUR spec carriers
   (C-15, S27, C-16, S28) and no live instrument.
2. I leaned on C-15's "NOT widened" clause as if it governed how many sources the project's own target may admit.
   Read verbatim at :496-497 its subject is the SHARED audit-log bucket the project does not own, and S27-AC1's
   control reads against that bucket. **A clause's constraint is only as wide as its subject.**

And C-16 argued the issuer's way in the PRD's own words -- it refuses the CMK flip because the change "would stop
both live legs silently", the same reasoning that forbids stopping this leg. I had quoted that clause in another
context the same afternoon and failed to apply it here.

**Withdrawal filed as Z-S59 @6519012f8c**, naming what survives from Z-S52 (the AC3-is-the-narrow-clause reading,
which the issuer then amended, and the ordering point) and what does not (the MOVE recommendation and the
one-source sentence). Acknowledged to the issuer in 19908 in the same terms.

**THE SHAPE, and the issuer named it better than I would have: this is my THIRD instance in one afternoon.**
Z-S57 -- three carriers agreed a denominator split, none of them the live plane. Z-S58 -- a bar transplanted
across a premise, checked against the spec and never against what the plan would do. Z-S59 -- four spec carriers
agreed and none was the world. **A reading derived correctly from a frozen spec is a fact about the SPEC; it
becomes a claim about the world only when a world instrument says so, and no further spec reading surfaces the
difference.** Banked as its own memory item rather than a footnote to the grain one.

**Two things the issuer did that I should copy.** It corrected my wrong 20/19 figure in a THIRD carrier -- the
decomposition's OP-s-1 cell -- which I never considered and which would have outlived both my fixes and re-seeded
the error at the next cut. And it re-measured on its own instrument before editing rather than relaying either my
read or the worker's, making the 21/18 figure three-instrument.

**Scope note taken and carried to L9:** `S27-AC2` on the accepted TO-OP-S-25-26-27 passed on delivered objects
from `opal-data-security` -- correct at that vintage, when that bucket WAS the evidence store, and NOT evidence of
the new store's logging after the split. It will not be spent twice in my adjudication.

## 2. Z-S60 read: the spec overstates controls the live grants carry (my Z-S61 @f1091d72fc)

`0.7.0_AE_CloudOps~S` ran the OP-s-28 ALIGN as the declaration-versus-world check the face asks for and found
C-16 and S28-AC1 both describing the log destination's two service-principal grants as "each with SourceAccount +
SourceArn". **Confirmed at this seat on the DECLARED plane** by a per-statement condition census over
`opsec/s3.tf`: `AllowCloudFrontAccessLogDelivery` carries `s3:x-amz-acl` AND `aws:SourceAccount`, no
`aws:SourceArn`; `AllowALBAccessLogDelivery` carries `s3:x-amz-acl` ONLY. **One of four asserted slots exists.**
Both planes agree and the TEXT is the outlier, which is why the align's plan is legitimately 0 changes and the
face's STOP correctly does not fire.

**What I added is the fix DIRECTION**, which the row leaves open: amend C-16 to describe the weaker world, or add
the conditions to the grants. For a project whose purpose is tightening this class, the first alone is **meeting
the bar by lowering it -- the shape this project's own tick-8 verdict declined on shape (3)**. It may still be
right; it should be chosen for a stated reason rather than by default because text is cheaper to edit.

**And I named the unknown that gates it rather than filling it**, which after s.1 is the point: whether those two
delivery service principals SUPPORT those condition keys at all is a property of each service's documented
behaviour, and no instrument available here answers it. The declaration's own comments also show the author
considered the ALB case deliberately -- the service-principal form is the documented one, the older regional form
is withheld to avoid widening, and "the enablement is the oracle" because the elbv2 attribute call performs a test
write and fails loudly. A ruling should engage that rather than override it unread.

## 3. State at close

Channel 61 rows, 18 of them this seat's. Task orders: **7 of 9 complete**, TO-OP-S-1 PENDING (in flight),
TO-OP-S-17R-28 STAGED. Resolved-live ARMED: Z-S50 (two credential homes), Z-S53/Z-S57 and Z-S56/Z-S58 (the two
verdict-correction PAIRS, which discharge together once the issuer's landed amendments are recorded as disarm
records), Z-S60 (this section). The raw `hazard_standing` count reads 23; the resolved read is the one L9 needs.

Inbox empty, everything acked. **Still owed and still blocked:** the four round-1 closure rows -- gate here still
`c3ef3a2530`, the ruled arm arriving with the leg, which is assess-only with the site not quiet and the push
declined at Andrew's terminal.
