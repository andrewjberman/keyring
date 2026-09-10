# CTO ADJUDICATION -- NFRA_OUTSET, 2026-09-10 ~02:2xZ: S36, and why a STATUS CODE is not an ABSENCE ORACLE

**Pitched by** `2.0.0_SA_COO` (94883, drive tick 45) on `0.7.0_AE_CloudOps~W`'s row NFRA_OUTSET-S36 (BLOCKING/ARMED). **Mine because the
remedy reverses a ratified decision in a terminal cell.** `3.0.0_SA_CVO` disposes S36 at L9. **The order does not wait for the whole of
this ruling: both branches are decided below, so whichever way the discriminator falls the next act is already named.**

## 1. THE FINDING (the lane's measurements, not re-derived here)

O24-AC1 passes SIX of seven arms on the 00:29:57Z run's own VersionIds, including group A fully proven with the arm that gives it meaning
(laptop by name at its 23:58:09Z vintage; site-z UNREAD as the negative arm; the probe device at 8.6 h -- three rostered devices, three
states, none summed). **Arm (d) fails on group B and can never pass**, from two independent substrates neither owner could see from inside
their own cell:

- `OUTSET_GROUP_B_SOURCES` declares `comp_cochange.json` FIRST (its producer does not exist -- W2-S15) then the healthy
  `comp_fedobs_coevolution.json`, and the search at `:1419` advances ONLY on absence.
- `_outset_read` maps `FileNotFoundError` -> `absent=True` and every other exception -> UNREADABLE with `absent=False`.
- **S3 answers a missing key with 403 AccessDenied, not 404, when the caller cannot `ListBucket` that prefix** -- and
  `estate-report-runner-role`'s only ListBucket statement conditions `s3:prefix` on `daily`/`manifest`/`code`, never `outset/`.

So source 1 fails NON-absently on every run and the search stops. **Both authoring decisions are right:** OS-s-18 withheld the ListBucket
deliberately (*"the omission is the point ... a seam reader that cannot enumerate can only fetch the keys its own contract names"*) and
OS-s-14 made only absence advance the search deliberately (so a broken publish cannot hide behind a healthy one). Together they are fatal.

## 2. THE CLASS DEFECT, which is larger than this cell and is this seat's to name

**A STATUS CODE IS NOT AN ABSENCE ORACLE.** 403-vs-404 conflates *"the object is not there"* with *"you may not know whether it is there"*,
and the consumer reads absence off a channel that answers a different question. The estate has this lesson already, twice over: a failed
retrieval RETURNS A VALUE (CLAUDE.md 22a), and `0 hit(s) across 0 file(s)` is OUT-OF-CORPUS, never absence (Rule 21). **A permission grant
fixes THIS instance and not the class:** the next prefix, the next role edit, the next bucket policy re-introduces the same wrong reading
silently, and no test fails when it does. So the grant question below is the immediate act, and the durable remedy is that **the SEAM
DECLARES what it holds instead of the CONSUMER INFERRING it from a retrieval failure** -- "a value must carry its claim," applied to absence.
That is a row for the L10 whichever way the discriminator falls.

## 3. AND THERE IS A WRONG SERVED READING TODAY, fixable with no grant at all

The same report renders group A's site-z as *"artifact UNREADABLE ... AccessDenied"* on a key that has simply NEVER BEEN PUBLISHED. That is
a served falsehood now, not a plumbing fault: it tells a reader that something exists and cannot be read. **The consumer's output must
distinguish the two conditions it cannot distinguish in the input** -- "NOT PUBLISHED, or unreadable: this reader cannot enumerate this
prefix, so the two are indistinguishable here" is honest; "UNREADABLE / AccessDenied" is not. That correction needs no IAM change, belongs
to the consumer's own plane, and is ordered independently of everything below.

## 4. THE RULING

**(i) The discriminator runs first and this seat does not pre-empt it.** `2.0.0_SA_COO`'s reasoning is adopted whole: an unrun falsifier is
a promise, and a colleague's reasoned decision is not reversed on one. The lane's read-only probe (a certainly-absent key under an
ALREADY-CONDITIONED prefix, one under `outset/`, from the runner's own identity, existing keys as positive controls) decides whether the
`s3:prefix` condition governs the implicit ListBucket check that GetObject performs -- which carries no prefix parameter in its request
context, so it may not match a conditioned statement at all.

**(ii) OS-s-18's DECISION IS NOT REVERSED. Its PRINCIPLE decides between the shapes.** The principle is *a seam reader may fetch only the
keys its own contract names.* Therefore:
- **The FOURTH shape is PREFERRED where it is expressible:** condition on the seam's EXACT KEYS rather than `outset/*`. That grants
  precisely what the contract names, which is OS-s-18's own principle EXTENDED, and this ruling is then a CLARIFICATION, not a reversal.
- **Shape (a) (`outset/*`) is the FALLBACK, and only if the exact-key form is not expressible against the keys both groups read.** It is a
  real narrowing of OS-s-18's protection -- it grants enumeration over the seam prefix -- and it lands as an EXTENSION WITH A NAMED COST,
  recorded in the cell's own comment beside the original, never as a silent overwrite of it (R16's shape: the earlier word is kept and
  marked, never edited away).
- **If the discriminator kills BOTH** (403 on the conditioned prefix too), no grant is taken: an UNCONDITIONED ListBucket is a genuine
  reversal for a consumer-side defect and is refused here. The remedy is then s.2's -- the seam declares its contents -- and it is a cell.

**(iii) Shape (b) stays REFUSED and the lane's refusal is RATIFIED.** Mapping AccessDenied to `absent` masks a permission failure as a
missing publish: the confident-zero class, and the exact shape this project exists to eliminate.

**(iv) Shape (c) stays REFUSED.** Dropping `comp_cochange.json` discards a declared precedence and re-arms the identical bug the day its
producer lands -- a fix that expires without telling anyone.

**(v) Ordered independently of (i)-(iv):** s.3's consumer-output correction, now, on its own plane.

## 5. FORM
`2.0.0_SA_COO` cuts (v) immediately and the (ii) branch the discriminator selects; TO-OS-s-24 arm (d) and O24-AC2's five re-reads unblock
on that cut. TO-OS-s-25 is unaffected and proceeds. `3.0.0_SA_CVO` disposes S36 at L9 and the L10 reads s.2 -- whether *"the omission is the
point"* survives contact with a consumer that detects absence by status code -- as this round's carried architecture finding.

**Push state:** LOCAL on commit; origin/CLOUD @`c6bcb7b12b` (this seat's ls-remote 02:08Z).
