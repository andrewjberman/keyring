# 0.4.0_DE_ClientPlatform~Z -- 2026-08-28 23:00-23:45Z -- AC5 LANDED, THEN I FOUND TWO DEFECTS IN MY OWN COMMIT

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

**DELTA LOG.** Prior windows at `laneZ_d3d4_render_defects_2130-2230Z.md` @`d1a970af35`,
`laneZ_promote_marker_set_2220-2235Z.md` @`bbfbbe96f7`, `laneZ_prod_pixel_verification_2235-2300Z.md`
@`2c17973bcf`. Not re-narrated. Written to a file because the whole of it exists only in mail --
`1.0.0_SA_CTO~Z` 14461 s.2: *"a broadcast reaches whoever is live now; a deliverable reaches whoever
comes next."*

---

## Commits

| hash | repo | what |
|---|---|---|
| `3f762bb6` | portal DEV | AC5: a held node may show its TOTAL -- what the STOP holds is the SPLIT |
| `b26c6fe6` | portal DEV | AC5 corrected: the guard expired on the predicate, and its basis was retracted |
| `d671e7083e` | workspace | `TO-S1-DE` proof-of-spec instance -- the face never had one |
| `b3c7b2ff00` | workspace | `TO-S1-DE` face: declare `instance_path` (one line, per CTO 14745) |

PUSH STATE, **MEASURED 23:40:46Z**, `is-ancestor` on a freshly fetched remote **with a positive
control that demonstrably returns YES**: `3f762bb6`, `b26c6fe6` **ON `origin/DEV`** (tip
`b26c6fe645`); `d671e7083e` **ON `origin/SITEZ`**; `b3c7b2ff00` **LOCAL** (committed ~23:38Z).
⚠ **Perishable and demonstrated so:** my AC5 pair went LOCAL -> ON ORIGIN inside this session and a
new commit was LOCAL again three minutes later. **"On origin" here is a reading with a timestamp.**

---

## OK: AC5 LANDED, SCOPED BY MEASUREMENT RATHER THAN BY THE PREDICATE

`2.0.0_SA_COO~Z` 14587 ruled (A) at cottonwood, (B) held at global. My original refusal of (A) rested
on my own inference that the residual was untrustworthy -- **`0.4.0_DS_ClientPlatform~Z` 14583 s.3(b)
read it at source and the inference did not survive**: `Client.aum` is `non_model - sma_aum`,
arithmetic off the timeseries, never touching the held Rebalancer feed. **WHAT IS HELD IS THE SPLIT,
NOT THE TOTAL** -- so my gate had been hiding a correct $294.9M figure for hours, for the wrong reason.

Both branches exercised and READ. **The committed fixture could not do it** -- its cottonwood Client
is `predicate: available`, so neither branch would have fired and a render there would have been a
green proving nothing. Built a scratch fixture mirroring the MEASURED served shape instead.

## WARN: TWO DEFECTS IN MY OWN 20-MINUTE-OLD COMMIT

**(1) THE GUARD EXPIRED ON A CONDITION THE PENDING WORK EXISTS TO FLIP.**
```
  WAS  showFigure = !unavailable || figureIsTrustworthy      <- SHORT-CIRCUITS
  NOW  showFigure = figureIsTrustworthy
```
`item 1` exists to make global's Client predicate AVAILABLE. **The guard would have stopped guarding
at the exact moment the work it was written for landed** -- silently, in production, nothing failing.
I tested only the dark case, which passed. ⛔ **And `2.0.0_SA_COO~Z` 14638 s.2 had already told the
fabric the risk was "already contained", paired with "do not re-solve it"** -- true of today, false
of next week. That office named the pairing as the error rather than the claim.
**Caught by building the negative control out of the FUTURE state** (predicate available + children
populated), which is the case the first commit failed.

**(2) THE STATED BASIS WAS RETRACTED WHILE SITTING IN SHIPPED CODE.**
`CLIENT_AUM_UNDERFOLDED_SCOPES` asserted, in a comment, with a dollar figure, that global's Client
under-folds by $359,773,356.74. **Retracted at 14657/14653**: global is 49F-only by ANDREW-DIRECT
2026-07-22 basis B, correct by construction, and "fixing" it would re-open the P0 basis B closed.
**I was one of four seats who held the wrong reading, and my own 14573 is where it got its second
seat.** Renamed `CLIENT_AUM_SCOPE_LIMITED_BY_RULING`, rationale rewritten to the ruled fact.
⭐ Behaviour deliberately unchanged: `2.0.0_SA_COO~Z` reaffirmed suppression AFTER the retraction on
the better ground -- correct-but-scope-limited under an "All partners" label is a PRODUCT call.

## OK: TO-S1-DE -- AN UNCLOSED ACCEPTANCE OBLIGATION OVER WORK ALREADY IN PRODUCTION

Found while reading the face after 14709 s.2 flagged the same class on `TO-R1-AE`. **No instance, and
no declared `instance_path`** -- positive control first (18 other instances in the same directory),
because a false ABSENT on this check happened tonight.

⛔ **AND I CAUGHT A PREMISE ERROR BEFORE IT CAUSED AN EDIT.** 14719 s.3 classified the face as
carrying *"no `<proof_of_spec>` block ... no criteria, no `expected_criteria`"* and offered to cut
one. **Measured: `TS1-AC1`..`AC6` are all declared, each with a `<criterion>` element and a cell_ref,
plus `<expected_criteria>`. Only `instance_path` was absent.** `1.0.0_SA_CTO~Z` 14745 ruled add the
line, do not cut the block -- *"cutting would duplicate six criteria or replace them with re-authored
ones -- the 'spec becomes a description' failure, reached from the other side."*
⭐ **THE CATCH WAS NOT DILIGENCE.** I ran `proof-of-spec-check` to validate my own instance and it
printed `6/6 criteria carry >=1 cell_ref` about a face I had just been told had none. **An instrument
pointed elsewhere disagreed in passing.** Two of tonight's catches have that shape.

Instance filed: **5 PASS, 1 UNVERIFIABLE-BY-INSTRUMENT, 0 FAIL**, VALID, coverage 6/6.
⚠ **`TS1-AC2`'s event gate discharged hours ago by a route nobody re-scored:** the face says it waits
on the ~13:50Z publisher fire; **the RELAND's publisher wrote at 22:17:55Z** -- same condition,
different route. The face has been passable since ~22:18Z while reading blocked.
⛔ **`TS1-AC3` refused:** the AFTER (4/4 PROD scopes) and the whole colour-law half are discharged,
but the served pre-fix object was overwritten by the reland and my pre-suppression renders were
against the FIXTURE proxy. **A fixture BEFORE with a PROD AFTER is two planes presented as one
comparison** -- tonight's most-corrected error. Recorded with its reason, not scored around.

## WARN: A MISATTRIBUTION IN MY FAVOUR, CORRECTED

14756 credited this lane with the promote-readiness census (14751), the two-repo resolution and the
23:35Z local-only catch. **None of it is mine** -- my sends that block were 14737/38/39 and
14748/49/50, and no dispatch ever handed me five hashes (checked by content across the whole `read/`
dir, not by recollection). **It is `0.4.0_DT_ClientPlatform~Z`'s**, corrected at 14779.
>> **A misattribution IN YOUR FAVOUR never self-corrects -- nobody writes in to say they did less
   than the record claims.** And the operational half matters more: it MISROUTES THE NEXT DISPATCH.
   Promote-readiness is DT's; the render/pixel plane is this lane's. <<
⭐ Root cause named by its author: *"you"* written into a four-recipient message about one seat's
work. CLAUDE.md states the rule in terms and the office had it banked -- **the rule was right and the
TRIGGER was missing at composition time.**

---

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `bun run typecheck` | `tsc -b --noEmit` x3 (AC5, the fix, post-rename) | PASS rc=0; instrument proven failable earlier this session on this same file |
| `ui-smoke.mjs` | scratch fixtures built to the MEASURED served shape, and to the POST-ITEM-1 shape | PASS -- both AC5 branches + the negative control, all READ |
| `proof-of-spec-check` | instance + the face's own 6-criterion set, positionally | VALID, 0 violations, alignment closed both directions |
| `git merge-base --is-ancestor` | both repos, freshly fetched, with a positive control | PASS -- 3 of 4 commits on origin, 1 local, read-time stamped |

**What worked:** building the negative control from the FUTURE state rather than the present one --
it is the only reason defect (1) was found before it shipped.
**What failed:** nothing this window; the two defects were mine, not the tools'.
**Gap found:** `sed -i` on a repo file emitted a CRLF warning; the diff stayed targeted (42/26) so no
whole-file rewrite, but the safer path on this tree is Read+Edit, which is what the one-line face edit
used (diff: literally `1 insertion(+)`).

---

## Blockers

**None at this lane.** Everything outstanding sits elsewhere and is named: item 1 + item 3 at Andrew;
the I2-row re-cut at `1.0.0_SA_CTO~Z`; cottonwood's OPAL-predicate measurement at
`0.4.0_DS_ClientPlatform~Z`; `TO-S1-DE`'s close at `2.0.0_SA_COO~Z`.

---

## Current State (written for zero prior context)

`TO-F1-DE` **CLOSED** @`82069d354c` (5/5 terminal, zero FAIL). `TO-S1-DE` **measurable end-to-end for
the first time** -- face declares its instance path, instance exists and validates, 5 PASS / 1
UNVERIFIABLE / 0 FAIL; **closing it is the issuer's act and I did not.** AC5 is landed and corrected
on `origin/DEV`; both AC5 commits travel together and the earlier "promote the first alone and you
ship the hole" risk is closed as of the 23:40Z read.
Not seated on increment 2 and not manufacturing work against it.

---

## Next Steps

- [`0.0.0_AB_MSTR~Z`] `b3c7b2ff00` is the only commit of mine still local.
- [`2.0.0_SA_COO~Z`] `TO-S1-DE` close -- 5/6 with the sixth explained is a decision only the issuer
  can make; and the face's status prose still names the 13:50Z fire, which is now a stale carrier.
- [`1.0.0_SA_CTO~Z`] the I2 row. **It has a third branch** (predicate derivable but children NOT
  emitted -> still no split), which scores a correct build FAIL and which the binary framing misses.
  Two-sided form proposed at 14775.
- [`0.4.0_DT_ClientPlatform~Z`] re-measure push state at the moment of any promote; never off a table.
- [this seat] available for the render/pixel plane on measurement. **Surprise S1 still ARMED**
  (`IDVZ`/`PFDE` share `#f43f5e` in one card; the SMA reland is what makes it visible).
