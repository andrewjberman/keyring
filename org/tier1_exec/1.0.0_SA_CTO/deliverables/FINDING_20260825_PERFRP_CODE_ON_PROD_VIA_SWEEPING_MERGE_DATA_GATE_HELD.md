# FINDING -- PERFRP CODE IS LIVE ON PRODUCTION VIA AN UNRELATED PROJECT'S PROMOTE; THE DATA GATE HELD, AND IT IS THE ONE NOBODY NAMED AS THE PROTECTION

**Author:** `1.0.0_SA_CTO`. **Date:** 2026-08-25 ~07:1xZ. **Archetype:** VALIDATE.
**Push state:** landed LOCAL, rides MSTR integration. **Distribution:** not CRO.
**Status:** MEASUREMENT + STRUCTURAL FINDING. **AT ANDREW, NOT RULED HERE.**

## 1. THE SOVEREIGN CONDITION

Andrew-direct ~01:1xZ (relayed via `0.7.0_AE_CloudOps~G`): PERFRP *"needs to stay on the DEV branch not
promoted to PROD until we know the data pipeline and all underlying data is verified end to end."*

## 2. MEASURED -- BOTH PLANES, CONTROLS BOTH WAYS

| | |
|---|---|
| DT~Z's DEV->PROD merge `d9a98bcc` | 2026-08-25T05:47:35Z -- subject: *"v2.1.165 -- ETFS_POSITIONING goes to production for the FIRST time"* |
| `index.html` deployed | **2026-08-25T05:55:07Z** (`s3api`, UTC) |
| `assets/index-BfFctj6k.js` deployed | **2026-08-25T05:55:06Z** |
| PERFRP tokens in that shipped chunk | `perfrp` **x6**, `perfrpCardsSlot` **x3** |
| PERFRP data leaves served | **ZERO** under `s3://opal-data-portal-v2/platinum/advi/49financial/` |
| positive control, same prefix | **12 objects present** -- so the zero discriminates |

**A PROD BUILD WAS CUT AND DEPLOYED SEVEN AND A HALF MINUTES AFTER THE MERGE.** `0.4.0_DE_ClientPlatform~D`
found the source plane (`git ls-tree origin/PROD`) and explicitly declined to claim a build was cut. It was.

**THE SCAFFOLDING SHIPPED AND THE NUMBERS DID NOT.** With no leaf, DE~D's own L16 exercise says 4 of 5 cards
render their DECLARED-ABSENCE faces and Gain/Loss is hidden. **No wrong performance figure is reachable,
because no figure exists.**

!! **DO NOT READ THE MANGLED NAMES AS ABSENCE:** `PerfrpCardGrid` / `PerfrpBookView` / `PerfrpTable` all read
**0** in the shipped chunk **because the bundle is minified**. Those zeros are evidence of nothing.

## 3. !! MY FIRST SWEEP WAS BROKEN AND ONLY THE POSITIVE CONTROL CAUGHT IT

I grepped `index-BS3QpgaB.js` -- the entry chunk named in `index.html` -- and measured `perfrp` = **0**.
**I WAS ONE SENTENCE FROM REPORTING "NOT IN THE BUNDLE" ON A SOVEREIGN-WORD MATTER.**

**CONTROLS IN THE SAME RUN: `rfsWindow` = 0 and `AdvisorBookView` = 0 -- BOTH KNOWN PRESENT IN THE APP.**
The app is code-split; the entry chunk does not carry the book views. **A zero from that file means nothing.**

Corrected sweep across all **49** deployed `.js`: subject `perfrp` -> **1 file**; positive controls
`AdvisorBook` 1, `rfsWindow` 1, `ModelPortfolios` 2; negative control `zzzNoSuch9999` **0**.

> **THE FALSE ALL-CLEAR WOULD HAVE BEEN INDISTINGUISHABLE FROM A REAL ONE**, and it would have closed a
> sovereign question in the reassuring direction. *A clean zero from the wrong file is the wrong question
> asked cleanly* -- Rule 21's own clause, on a bundle instead of a bucket.

## 4. !! THE STRUCTURAL FINDING -- IT OUTLIVES THIS INSTANCE

> **A DEV->PROD MERGE CARRIES EVERYTHING ON DEV BY CONSTRUCTION. THEREFORE A HOLD EXPRESSED AS "KEEP IT ON
> DEV" IS ONLY AS STRONG AS THE NEXT UNRELATED PROMOTE.**

It is not a hold. **It is a coincidence that has not been disturbed yet**, and it is disturbed by any team
shipping any other project -- correctly, on their own schedule, with nothing in their promote's subject or
scope naming the passenger.

**WHAT ACTUALLY HELD TONIGHT WAS THE DATA GATE**, and nobody named it as the protection: `0.7.0_AE_CloudOps~G`
declined the scoped first publish twice, including when a path was open to them. **The protection everyone
was relying on (branch position) failed silently; the protection nobody had designated (unpublished leaves)
is the one that held.**

*This matters independently of how the instance is ruled, because it changes how a future hold should be
expressed: a branch-position hold needs a mechanism, or it needs to be a data-plane hold instead.*

## 5. WHAT THIS SEAT DID NOT DO

- **DID NOT ADJUDICATE THE BREACH.** Whether a sweeping merge for another project is *"promoted to PROD"*
  within the meaning of his word is **HIS interpretation**. Reading it either way from this seat is the
  gate-manufacture / gate-narrowing pair CLAUDE.md names **in both directions**. DE~D refused first and
  routed it up; **the same refusal binds an exec seat harder, not less.**
- **DID NOT REVERT.** A revert on a shared branch, over another project's promote, on my own reading of his
  word, is precisely the forbidden act.
- **DID NOT HOLD ANY WORKSTREAM.** Nothing stops on this.
- **DID NOT FAULT `0.2.0_DT_PortfolioAnalytics~Z`.** They promoted their own project correctly. The merge
  mechanism did the rest, and their commit is named here because the record needs the mechanism, not because
  the act was wrong.

## 6. AT ANDREW -- THE CALL, WITH THE RECOMMENDATION

**THE CALL:** does a sweeping DEV->PROD merge for an unrelated project constitute "promoted to PROD" within
your condition, and if so do you want the PERFRP files reverted off PROD?

!! **REC REVISED ~07:2xZ -- MY FIRST RECOMMENDATION WAS "ACCEPT IT" AND IT RESTED ON AN INCOMPLETE READ OF
THE RENDER PLANE. `0.4.0_DE_ClientPlatform~D` 69521 supplied the literal strings and they change the answer.**

**WHAT AN ADVISOR ACTUALLY SEES ON PRODUCTION** (read at `origin/PROD`, from source -- unreadable from the
minified bundle, which is why it had to come from the author):

| card | subtitle, verbatim |
|---|---|
| Activity Summary | *"Beginning value, net additions, gain/loss, ending value"* |
| Performance | *"Time-weighted return, net of advisory fees"* |
| Allocation | *"Allocation by class, of total and of level"* |
| Transactions | *"Per-relationship, paged"* |

*(Gain/Loss is `requiresLeaf:true` and is HIDDEN -- **the one card that is invisible is the only one whose
absence anyone designed for.**)*

**THESE READ AS FINISHED PRODUCT.** Nothing says provisional, preview, or coming soon -- **on DEV the
audience was us and no such label was needed.**

!! **AND THE TRANSACTIONS CARD RENDERS INTERNAL TAXONOMY ON ITS FACE, IN AMBER:**
`Notes -> PII-EXCLUDED-PERMANENT` - `Description -> NO-SOURCE-TODAY`, plus verbatim from `cards.ts`:
*"Every candidate source is client-sensitive (transaction memo and wire instructions). Deliberately not
served, and not a gap to be closed later."*

> **AN ADVISOR ON PRODUCTION READS "PII-EXCLUDED-PERMANENT" AND A SENTENCE ABOUT WIRE INSTRUCTIONS.**
> **NO CLIENT DATA IS EXPOSED AND NOTHING LEAKS** -- it is **internal engineering vocabulary and internal
> PII rationale rendered on a client-facing surface.** DE~D wrote those strings deliberately and Andrew
> ratified the two-state form at 04:00Z; **they are correct FOR AN AUDIENCE OF US.**
> **THE AUDIENCE CHANGED WITHOUT THE STRINGS CHANGING** -- the same shape as everything else here: nothing
> became wrong, an environment assumption under it was invalidated by an act in another lane.

**REVISED REC: REVERT THE PERFRP FILES OFF PROD.** Three reasons, and the first is new since my original rec:
1. **It is the only option that removes the internal-vocabulary exposure without shipping a further change.**
   Editing the strings is also a DEV change needing its own promote, so it is not faster and it leaves
   finished-looking cards with no data on a client surface.
2. It restores the letter of his condition, not only its substance.
3. **Four cards with finished product names and no figures is its own poor look on a client surface**,
   independent of the vocabulary question.
**IF HE PREFERS TO ACCEPT IT, THE SUBSTANCE STILL HOLDS** -- zero leaves, no wrong number reachable -- and
that reading remains defensible. The call is his either way; only my recommendation moved.

> **THE HONEST ONE-LINE SUMMARY, AND IT IS DE~D'S:** *four performance cards with finished-looking product
> names, no figures, and two lines of internal data-governance vocabulary visible on one of them.* **"The
> code reached PROD" understates it; "wrong figures are showing" overstates it; AND "four empty cards"
> UNDERSTATES IT TOO** -- which is what my first recommendation rested on.

**CARRIED SEPARATELY AND WORTH MORE THAN THE INSTANCE:** section 4. However you rule here, a branch-position
hold is not a hold.

## 6b. !! SCOPE WIDENED ~07:2xZ -- THE SAME PROMOTE CARRIED A SECOND LANE, AND ITS FACE IS LOUDER

**THIS IS NOT ONE PROJECT'S SLICE.** `0.4.0_DE_ClientPlatform~C` 69534 measured their own lane against the
same merge and found **SEVEN OF THEIR NINE COMMITS ON `origin/PROD`**, including **`d1f8f38a`, the commit
that wires their panel into `ModelPortfolios.tsx`.** Same merge `d9a98bcc`, same mechanism, and **its subject
named nothing of theirs either.**

**SERVED DATA ABSENT ON EVERY SCOPE, CONTROLLED BOTH WAYS:** `platinum/mdpf/{49financial,inflection,
cottonwood,global}/` category-views leaves = **0, 0, 0, 0**; positive controls in the same prefixes = **3, 3,
4 objects present.** Same conclusion as PERFRP -- no wrong number, because there is no number.

!! **BUT THE DECLARED-ABSENCE FACE IS LOUDER THAN PERFRP'S, AND THIS IS THE PART THAT CHANGES THE PICTURE.**
Their accessor returns `{status:'absent_by_scope'}` on a 404 -- **a TRUTHY object** -- so the mount guard
`{categoryViews && <CategoryViewTree .../>}` passes and the component renders. What renders is **not a hidden
card: it is a full `Panel variant="chart"` titled `ASSET CATEGORY VIEWS`, carrying the line "No category view
tree is published at this scope." On every firm, today.**

> **AN ABSENT CARD READS AS INTENTIONAL; AN EMPTY TITLED PANEL READS AS BROKEN.** PERFRP's absence faces sit
> inside an existing surface. **This ADDS A NEW TITLED PANEL to a client-facing page that then says it has
> nothing.**

**AND DE~C'S OWN CODE COMMENT PREDICTED THE MECHANISM AND MISSED THE EXPOSURE:** they had written that a
stale observation *"goes stale VISIBLY -- the panel starts showing a tree."* Correct. **They never asked
WHERE that panel would be visible FROM**, because they were reasoning about the DEV surface they were working
on. *The same audience-changed-without-the-artifact-changing shape as DE~D's strings.*

**THIS STRENGTHENS THE REVISED REC RATHER THAN COMPLICATING IT** -- and it means the revert question is not
PERFRP-shaped but **promote-shaped.** Whatever else was on DEV at 05:47:35Z rode the same merge, and **only
two lanes have checked.**

## 7. INDEPENDENT CONFIRMATION

`0.7.0_AE_CloudOps~G` measured the served plane independently and reached the same result (zero PERFRP keys).
`3.0.0_SA_CVO` confirmed with a negative control. **Three seats, three separate reads, same verdict.**
