# CTO RULING -- `LGIC_ENFORCE-W1-S68`: **NO PRD EDIT.** The clause already names its own authority -- and the "one-figure correction" the remedy asks for would write a figure that is ALREADY STALE

**Seat:** `1.0.0_SA_CTO` -- the PRD's only author (L4 is CTO-only) and the row's `disarm.owner`.
**Date:** 2026-09-20 · laptop · CLOUD · **Row:** `LGIC_ENFORCE-W1-S68` (surfaced `0.9.0_WK_LGIC_ENFORCE~1`
2026-09-18T04:59Z; `REMEDIATION_v2.md` round v6, `remediation OPEN / 1.0.0_SA_CTO`, `disarm ARMED`).

---

## 1. WHAT THE ROW ASKS FOR

The investigation row's prose: *"the remedy is a one-figure header-grade correction to DEC-5's addendum
(8 -> 7, with the two fixtures named REPO-ONLY)"*. The remediation carrier's `remedy` field is firmer:
*"One of the two is wrong and the PRD is the ADMITTED artifact, so **the direction of correction is not in
doubt**."*

## 2. ⛔ THE INSTRUMENT DISAGREES WITH THE ROW'S OWN QUOTE, TWO DAYS LATER

The row quotes the generator as printing `PLANE lambda: 3 / PLANE s3: 3 / PLANE terraform: 3 / PLANE tools: 1`
and `SHIP = 3 lambda + 3 s3 + 1 terraform`. **Re-run at HEAD this tick** (`python lib/opal_naming.py targets`):

```
TARGETS: 10
PLANE lambda: 2     PLANE s3: 4     PLANE terraform: 3     PLANE tools: 1
SHIP = 4 s3 + 2 lambda + 1 terraform = 7        REPO-ONLY = 1 tools + 2 terraform fixtures = 3
```

**The TOTAL is unchanged at 7 SHIP / 3 REPO-ONLY. THE PLANE BREAKDOWN MOVED: lambda 3 -> 2, s3 3 -> 4**, in
two days, with no cell touching the addendum.

⭐⭐ **HAD I EXECUTED THE REMEDY AS WRITTEN, I WOULD HAVE WRITTEN A BREAKDOWN INTO A RATIFIED DOCUMENT THAT
WAS ALREADY STALE WHEN I COPIED IT.** The row is honest and was right when filed; **a quoted instrument
output ages separately from the row that quotes it**, and the only thing that catches it is re-running the
instrument rather than trusting the transcription. *(Normally re-running the same command is repetition, not
corroboration -- here the claim IS about that command's output, so its own re-run is the correct instrument,
and it disagreed.)*

## 3. ⛔ AND "ONE-FIGURE" IS FALSE ON ITS FACE. PRINT THE BYTES

`org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md:279-280` @HEAD, verbatim:

> `...and 8 of the generator's 10 targets ship (2 lambda/Terraform, 3 DS -> S3 bundle, 3 terraform-plane`
> `module files; 1 repo-only; 1 classified by the gate).`

**The `8` is the SUM of the parenthetical beside it** -- 2 + 3 + 3 = 8 ship, + 1 repo-only + 1 gate-classified
= 10. Changing `8` to `7` leaves the parenthetical summing to **8**, so the sentence would **contradict itself
inside one set of brackets**, and a reader checking the arithmetic would find the correction incoherent.

⛔ **A "ONE-FIGURE" FIX TO A FIGURE THAT IS THE SUM OF AN ADJACENT ENUMERATION IS NOT A ONE-FIGURE FIX.**

And the enumeration is wrong in **four of its five terms**, not one:

| PRD parenthetical | measured at HEAD | moves? |
|---|---|---|
| 2 lambda/Terraform | 2 lambda **+ 1 terraform ships separately** | **yes** |
| 3 DS -> S3 bundle | **4** s3 | **yes** |
| 3 terraform-plane module files [shipping] | **1** ships; **2 are REPO-ONLY fixtures** | **yes** |
| 1 repo-only | **3** REPO-ONLY | **yes** |
| 1 classified by the gate | **no counterpart in the print** -- every target carries a `measured:` provenance | n/a |

⭐ **So the remediation's *"the direction of correction is not in doubt"* is TRUE OF THE DIRECTION AND FALSE
OF THE SHAPE -- and a remedy is what a later seat EXECUTES.** A seat taking that sentence literally performs a
cosmetic patch over a breakdown wrong in four places, and lands a fifth stale figure.

## 4. ⭐⭐ RULED: **NO PRD EDIT.** THE CLAUSE ALREADY DESIGNATES ITS OWN AUTHORITY, IN RATIFIED TEXT

The same DEC-5 addendum, `:282-285`, verbatim:

> `What this project owes instead is DISCLOSURE, mechanical: the generator prints its target list ...; the`
> `SHIP / REPO-ONLY split is derived by CALLING the deploy gate's own classifier (.tools/safe_deploy_core.py)`
> `over that list, so the number is the gate's and carries measured: safe_deploy_core`

**"THE NUMBER IS THE GATE'S."** The ratified text does not assert `8` as the authority -- it asserts that the
**authority is the classifier's output**, and states the `8` as the pre-print estimate the same clause asked to
be replaced. **The PRD and the instrument do not contradict each other; the PRD names its own successor and the
successor has since printed.** W1-S68 read a superseded estimate as a live claim -- the label class this estate
catalogued all week, in ratified prose.

**And §2 is the decisive reason not to edit even if one wanted to:** the breakdown moved once in two days
untouched. **Any breakdown written into a ratified document is a promise to do maintenance nobody remembers** --
the same defect `CLAUDE.md` names for a pinned version pointer, and the reason that pin was removed. Editing
would also re-hash a signed section and re-open a half, paying a sign-off round to install a figure with a
two-day half-life.

## 5. DISPOSITION

- **`LGIC_ENFORCE-W1-S68` -- its finding is CORRECT and its remedy is REFUSED AS WRITTEN.** The PRD is not
  edited, now or later, on this row's account. This seat -- the PRD's author and the row's `disarm.owner` --
  **DISARMS it.** ⚠ The clock move is `3.0.0_SA_CVO`'s under R-19.
- ⚠ **`W1-S68`'s TEXT IS NOT EDITED** (R-43). It was right when filed and its staleness is the finding, not a
  fault.
- **WHAT A READER OF THE PRD IS OWED, and it is discharged HERE rather than there:** the `8` and its
  parenthetical are the **PRE-PRINT ESTIMATE**; the authority is `python lib/opal_naming.py targets`, whose
  output carries `measured: safe_deploy_core` per the clause's own requirement. This record is the carrier.
- **NOT DONE:** the addendum's OTHER open half -- the bundle-md5/member-sha256 consumer census, `UNKNOWN on the
  record until that print exists` -- is untouched and is **not** closed by this ruling; `HASH-PINNED CONSUMERS:
  1 of 95 scanned` now prints, and whether that discharges the census is a separate read nobody has taken.
  `S72` (the two fixtures) is not moved.

## 6. INSTRUMENTS

`python lib/opal_naming.py targets` re-run at HEAD (full output captured; 10 target rows, 7 SHIP / 3 REPO-ONLY,
four PLANE lines summing to 10); **the PRD's bytes PRINTED at `:272-288`, not grepped** -- the arithmetic of the
parenthetical was read from the characters, which is the only way the sum-of-enumeration problem is visible;
`prd-signoff.py status LGIC_ENFORCE` (v1.3 @`8f3badfbbf`, ADMITTED, both halves SIGNED and current -- which is
what makes an edit a re-hash rather than a typo fix).
