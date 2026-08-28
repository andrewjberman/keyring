# CERT — `ETFS_POSITIONING.TO-12-DE` — **5 of 5 CERTIFIED**

**Certifier:** `3.0.0_SA_CVO~Z` · **Issued:** 2026-08-28T~17:0xZ · **Executor:** `0.4.0_DE_ClientPlatform~Z`
**Instance:** `org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/ETFS_POSITIONING.TO-12-DE_PROOF_OF_SPEC.json` @`0b86f3e13f`
**TO face:** `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ETFS_POSITIONING.TO-12-DE.remove-as-of-dates-under-the-stacked-bars.md` @`98c35fa0e1`
**Build:** `portal` @`27c60ecb`

---

## VERDICT

**5 of 5 CERTIFIED — CRITERION-WISE. No defect cited on the executor's work.**

⛔ **This is NOT a bare 5/5.** AC2 passed on a **substituted method** and AC3 on a criterion whose
literal wording no correct implementation can satisfy. Both are recorded below with the reasoning
that made them certifiable, because a certificate that hides how it got to 5/5 ages worse than one
that shows it.

---

## WHAT I VERIFIED MYSELF, AND ON WHICH INSTRUMENT

Rule 22 forbids re-running the executor's command and calling it corroboration. Every row below was
re-derived on an instrument that **fails differently** from theirs, or is an inspection of the filed
artifact rather than a repetition of the act that produced it.

| AC | executor's instrument | MY instrument | result |
|---|---|---|---|
| AC1 | playwright capture + DOM innerText count | **I READ BOTH FILED PNGs MYSELF** | CONFIRMED |
| AC2 | one served GET + a by-construction argument | **write-verb census over the portal source** | CONFIRMED |
| AC3 | position-by-position screenshot compare | **my own read of the same pair** | CONFIRMED |
| AC4 | `git show --stat` | **`git show --stat 27c60ecb` at this seat + push-state read** | CONFIRMED |
| AC5 | `bun run typecheck` + planted mutant | **CITED, not re-run** (see below) | ACCEPTED |

### AC1 — the as-of dates no longer render. **CERTIFIED.**
The criterion says *"READ A SCREENSHOT — a class-name grep does not establish what a page draws."*
I did not take the executor's read on trust; **I opened both PNGs and read them.**
- `AC1_BEFORE_etfs_dates_present.png` (74,072 B): **"August 27, 2026" renders under all four tickers**
  — DIVZ, IDVZ, PFDE, PFOE. **4 of 4.**
- `AC1_AFTER_etfs_dates_removed.png` (71,479 B): **those four lines are absent. 0 of 4.** The tickers
  remain and are the last element in the header cell.
Both files exist at the declared path. ⭐ The executor also scored AC1 on a **second instrument that
fails differently** — a region-scoped DOM innerText count (4 before, 0 after). A date hidden by CSS
would pass the count and fail the read; a date moved out of the region would do the reverse. That
pairing is correct and is the strongest single thing in this instance.

### AC2 — the data is unchanged. **CERTIFIED ON A SUBSTITUTED METHOD.**
⚠ **THE CRITERION AS WRITTEN WAS NOT SATISFIED, AND THE EXECUTOR SAID SO RATHER THAN DRESSING IT UP.**
AC2 demands *"Show the served artifact before and after; the diff on that field is EMPTY."* The
executor captured **no pre-change fetch** and wrote: *"it is not offered as a before/after pair …
I will not present one read as two."*

They argued instead that the diff is empty **BY CONSTRUCTION** — a boolean in portal render code
cannot move an artifact the portal does not write. **I did not accept that argument; I tested it**,
on an instrument they did not use:
```
census: 'positioning_data' across portal/src   ->  18 references (denominator printed)
access verbs, ALL of them:  apiRequest<PositioningDataResponse>(...)   portal-proxy.ts:1142
                            apiRequest<EtfPositioningResponse>(...)    portal-proxy.ts:1341
write verbs (PUT/POST/upload/putObject/s3 write):  ZERO
the single s3:// occurrence (portal-proxy.ts:1327) is a COMMENT naming the producer
```
The portal **only reads** this artifact. The by-construction claim therefore **holds**, and it is a
*stronger* form of evidence than the two-sided read the criterion asked for — a before/after pair
shows the field did not move *on one occasion*; the census shows it *cannot* move from this layer.
⭐ **Declining to present one read as two is the behaviour this office wants.** An executor who had
fetched once and captioned it "before and after" would have produced a PASSING row and a false record.

### AC3 — no other element moved. **CERTIFIED ON THE NAMED SET, WITH AN ISSUANCE DEFECT NOTED.**
Confirmed on my own read of the pair: bars, the eight percentage labels (0.81/99.19, 1.44/98.56,
0.36/99.63, 2.33/97.69) and the four tickers are at **identical coordinates** in both frames.

⛔ **THE DEFECT IS THE ISSUER'S, NOT THE EXECUTOR'S.** AC3's literal words — *"NO OTHER ELEMENT
MOVED"* — **cannot be satisfied by any correct implementation of AC1.** Deleting a line from normal
flow necessarily lifts everything beneath it. Measured in the pair and visible to me: EXPAND DETAILS
520→506, panel footer 570→556, PORTFOLIO COMPOSITION 647→633 — a uniform **14px**, exactly one line's
height. The executor **disclosed this rather than passing a bare PASS that quietly redefines the
criterion**. That is the correct handling and it is why this certifies.
>> **FOR THE ISSUER (`2.0.0_SA_COO~Z`), not a gate:** a criterion of the form "nothing else moves"
   on a REMOVAL is unsatisfiable-as-written. The intent — "the named set is unchanged and no
   *second* change rode along" — is what was met. Worth wording that way at cut time.

### AC4 — `TO-7` is not regressed. **CERTIFIED.**
Re-derived at this seat: `git show --stat 27c60ecb` → **1 file changed, 24 insertions, 1 deletion**,
entirely `portal/src/pages/Positioning/shared/bookSet.ts`. **Zero** files under `data/*/scripts/`,
zero Lambda, zero Terraform, zero S3 write path. TO-7's certification is on **producer** behaviour;
AC2 shows that emission still serving `2026-08-27` for 4 of 4 books. Reversing TO-7's **display**
half is this TO's declared purpose on Andrew's word, not a regression.

### AC5 — typescript clean. **CERTIFIED, CITING the executor's exercise rather than re-running it.**
`bun run typecheck` rc=0, with the instrument **proven able to fail first**: a planted
`etfs: 'MUTANT_NOT_A_BOOLEAN'` produced `bookSet.ts(372,3): error TS2322` — **on the exact line this
diff edits**, so the control covers this change's own subject and not merely the toolchain. Reverted,
re-ran, rc=0. ⛔ Per CLAUDE.md I **cite** this rather than re-running the same command; a second
`tsc` at this seat would be repetition, not corroboration. The executor also recorded that
`commit-gate` printed *"checked 0 of 1 file(s)"* and did **not** cite it as validation — the TO asked
for exactly that discipline and got it.

---

## TWO THINGS THE INSTANCE COULD NOT KNOW, MEASURED AT CERTIFICATION TIME

1. ⭐ **THE PUSH STATE HAS ADVANCED IN THE FAVOURABLE DIRECTION.** The instance declares `27c60ecb`
   **LOCAL** (`git ls-remote origin DEV` → `2858e7f5` at build time) and correctly leaves the push to
   the integrator per LD-0367. **Measured now: `git merge-base --is-ancestor 27c60ecb origin/DEV` →
   YES; `origin/DEV` = `57701d5c`.** The work is off-device. The instance's statement was true when
   written and is now stale in the direction that costs nothing — recorded so no successor reads
   "LOCAL" and re-chases a push that has landed.
2. ⭐ **ANDREW'S STATED REASON SURVIVES THE CHANGE, AND NOBODY CHECKED THIS.** His authority was
   *"Dont need this, timestamps are listed elsewhere."* That reason is only true if a timestamp
   remains somewhere on the surface. **In the AFTER frame the panel footer still reads "August 27th,
   2026, 5:00p ET | Source: Bloomberg."** The elsewhere he presupposed **still exists**. Had the
   change also removed the footer stamp, AC1–AC5 would every one of them still pass while
   **falsifying the sovereign's own reason for asking** — a state no criterion on this TO could
   detect. Recorded as the substantive check the criteria do not carry.

---

## SCOPE OF THIS CERTIFICATE — what it does NOT say

- It does **not** certify the PROD promote. Out of scope by the TO's own §5; Andrew's word, per promote.
- It does **not** re-certify `ETFS_POSITIONING.TO-7`. AC4 establishes non-regression, not re-validation.
- It does **not** reach `D1_CATVIEWS.TO-M1-DS` / `TO-S1-DE` — different project, certified separately.
- **DEPLOYED-vs-COMMITTED:** the artifact is `COMMITTED` and now on `origin/DEV`. **Serving on DEV is
  not asserted here** — the executor labelled it `COMMITTED-NOT-DEPLOY-SCOPE` and that caution was
  correct (`1.0.0_SA_CTO~Z` independently vindicated the same distinction at msg 13457 §1).

---

## THE ROUTE-A NOTE, CLOSED

This TO's instance previously read **INVALID, 5 violations, all "carries NO cell_refs — REFUSED"** —
because `proof-of-spec-check.py` arms alignment ENFORCE on the mere **PRESENCE** of a `<decomp_ref>`
element, so **the TO's own honest disclaimer armed the enforcement that then refused its own
criteria**. ROUTE A (remove the element, preserve the disclosure as prose) was applied by the issuer
at `98c35fa0e1`; `0.4.0_DE_ClientPlatform~Z` exercised it → **violations 0, VALID**.

>> ⭐ **THE PROOF-OF-SPEC JSON WAS NEVER TOUCHED** (unchanged at `0b86f3e13f`). The same five rows
   flipped INVALID→VALID because what moved was the TO's **tag**, not the **evidence**. That is what
   makes ROUTE A the right route rather than merely one that worked: had the instance needed editing
   to pass, the defect would have been substance and ROUTE B would have been correct.
   **So this certificate cites no avoidable defect, which was the whole point of holding out for it.**

— `3.0.0_SA_CVO~Z`
