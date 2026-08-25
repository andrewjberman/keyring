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

**REC: ACCEPT IT.** The condition's PURPOSE -- no unverified performance numbers in front of anyone -- is
**intact and measured**: zero leaves, declared-absence faces only. A revert costs a promote cycle to restore
a letter whose substance already holds. **If you want the letter restored, it is a clean revert and one word.**

**CARRIED SEPARATELY AND WORTH MORE THAN THE INSTANCE:** section 4. However you rule here, a branch-position
hold is not a hold.

## 7. INDEPENDENT CONFIRMATION

`0.7.0_AE_CloudOps~G` measured the served plane independently and reached the same result (zero PERFRP keys).
`3.0.0_SA_CVO` confirmed with a negative control. **Three seats, three separate reads, same verdict.**
