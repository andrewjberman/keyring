# WS-C2 STEP 3 -- the M3 split, and the DEBTLOOPS round-trip

**Program:** NFRA_VELOCITY / CORE, WS-C2. **Author:** `1.0.0_SA_CTO~Z`. **2026-07-31.**
**Closes the two named residuals** from steps 0-2. **Fence:** `ADVI_PERFORMANCE` / `MDPF_GLOBAL` not
drawn on, not opened.

---

## S.1 THE M3 SPLIT -- IT IS NOT TWO MECHANISMS, IT IS AT LEAST FOUR, AND THE MAJORITY IS HOMELESS

`3.0.0_SA_CVO~Z` predicted a **two-way** split: a partition-key proxying content is a `grain`
substitution, a HASH proxying content is *same-grain, different representation* and closer to `plane`.
**I pulled all 9 M3 incidents and read them. The prediction is half right and the residual is bigger
than either of us expected.**

| sub-class | n | instances | types as |
|---|---|---|---|
| **A -- KEY/PARTITION proxies CONTENT** | 2 | *"partition key proxies CONTENT (under-fires)"*; *"`as_of` proxies CONTENT (6 of 69 partitions rewritten in place)"* | **`grain`** -- CVO~Z's first arm, confirmed |
| **B -- HASH proxies CONTENT** | 1 | *"hash dominated by the two date columns under investigation"* | **`plane`** -- CVO~Z's second arm, confirmed |
| **C -- A CHECK'S OWN SHAPE proxies CORRECTNESS** | **5** | *"three agents wrote the defect's SHAPE into their tests"* (x2); *"a test asserted the defect and would have blocked the fix"*; *"four tests asserted a prohibition was still armed"*; *"a check reading 'a 07-24 version appeared' -- **would have passed on the worst outcome**"* | **HOMELESS** |
| **D -- a PHANTOM entity proxies a REAL one** | 1 | *"phantom advisor served as a real advisor on the canonical NNA spine"* | **UNRESOLVED** |

> ### **SUB-CLASS C IS THE MAJORITY (5 of 9) AND IT IS NOT A POSITION PROPERTY AT ALL.**
> *A test that asserts the defect. A check that would have passed on the worst outcome.* **The
> control's own predicate is the proxy** -- it stands in for the property it claims to check.
> **That is a CONTROL property, the same family as M2 and M14, and it has no home.**

**THIS CORRECTS STEP 0, WHERE I TYPED `M3 -> grain` OUTRIGHT.** That was typing from the mechanism's
NAME (*"proxy for the thing"*) rather than from its instances -- **the identical error I made on
MSBEFF's `SUBSTITUTED` in step 2 and caught by sampling there.** I made it twice; sampling caught it
both times. **A mechanism name that reads like a position is not a position.**

### S.1.1 IMPACT ON STEP 1's CROSS-TAB

| bucket | step 1 | corrected | delta |
|---|---|---|---|
| `TUPLE: grain` | 72 | **65** | -7 |
| `TUPLE: plane` | 26 | **27** | +1 |
| **HOMELESS** | **36 (17.3%)** | **41 (19.7%)** | **+5** |
| UNRESOLVED | 0 | 1 | +1 |

**HOMELESS rises from 17.3% to 19.7%; `grain`'s dominance shrinks.** Both move in the direction that
makes my own vocabulary look *worse*, which is the direction a correction to one's own headline
usually does not go. **Untypeable by either scheme rises from 40/208 to 45/208 = 21.6%.**

---

## S.2 THE DEBTLOOPS ROUND-TRIP -- 3 OF 4 SHAPES VERIFY, ONE DOES NOT

**Question:** do the four typed violations landed in the rule bank actually round-trip to their stated
DEBTLOOPS source?

**Landed in the rule bank:** `LEGACY_WRITER`, `CLOBBER`, `TRIGGER_MISSEQUENCE`, `SILENT_RESIDENT` -- all
four present.

**Against the memo + its raw transcript, with a positive control (`recall denominator` = 1 hit):**

| shape | memo | raw | verdict |
|---|---|---|---|
| legacy-writer | 4 | 1 | **PROVENANCE VERIFIED** |
| clobber | 4 | 1 | **PROVENANCE VERIFIED** |
| zombie | 1 | 1 | **PROVENANCE VERIFIED** (landed as `SILENT_RESIDENT`) |
| **misseq / TRIGGER-MISSEQUENCE** | **0** | **0** | **NOT IN THE SOURCE** |
| orphan | 0 | 0 | absent -- consistent with the rename; the PRD's own phrase is *"a C-SILENT resident"* |

> **`TRIGGER-MISSEQUENCE` HAS NO DEBTLOOPS PROVENANCE.** The PRD attributes the shapes to *"the
> DEBTLOOPS memo shapes"*, and three of the four are there. **The fourth appears to originate in the
> PRD itself.** That is not necessarily wrong -- a decomposition may legitimately add a shape -- **but
> it is currently carried as though it were sourced, and it is not.** Flagged, not resolved; the PRD
> is mine and the correction routes to me.

**The memo's real contribution is verified verbatim and is the WS-C7 seed** (`:166-167`):
> *"No detector in the estate has a measured **recall denominator**. Every tool reports what it FOUND;
> none reports what it COULD NOT HAVE FOUND."*

**That single sentence is now measured twice over:** step 2's MSBEFF walk found **50.6% of 718 findings
are recall/coverage**, and step 1 found the rails type none of it. **The memo asserted it; the corpus
measures it.**

### S.2.1 MY FIRST PROBE RETURNED A FALSE ABSENCE

I grepped the exact hyphenated forms (`LEGACY-WRITER`, `TRIGGER-MISSEQUENCE`) and got **zero across
both artifacts** -- and was one step from reporting *"the memo does not contain the shapes it is cited
for."* **The memo writes them as `legacy writer` / `clobber` in prose; only the PRD uses the canonical
hyphenated caps.** A positive control plus a looser probe found 3 of 4 immediately.

**Eighth M2 of the night, mine, same shape as the other seven:** an exact-string query returning a
well-formed wrong answer. **Had I published it, I would have accused a source document of not saying
what it says** -- and the accusation would have been footnoted with a grep.

---

## S.3 WS-C2's CORPUS WALK IS NOW MATERIALLY COMPLETE

| corpus | status |
|---|---|
| 210-incident INCIDENT_TAXONOMY | walked (step 1); five populations, no canonical artifact; **cause open, routed to MSTR** |
| MSBEFF 718 | walked by class (step 2); canonical artifact; every published figure reproduces |
| DEBTLOOPS shapes | round-tripped (this step); 3 of 4 verified, 1 unsourced |
| M3 split | resolved (this step); 4-way, majority homeless |

**THE CONSOLIDATED EXPRESSIVENESS RESULT, all three corpora agreeing:**
- **The rails type WHERE AN ASSERTION SITS. They do not type INSTRUMENT FALLIBILITY, by construction.**
- Incident taxonomy: **21.6% untypeable** (corrected).
- MSBEFF: **50.6% recall**, only **6.4% tuple-typed**.
- **`rail` types ZERO in either corpus.**
- **The residual has ONE shape across all three: properties of a CONTROL, not of an assertion.**

**REMAINING OPEN, and none of it blocks:** the `+2`/five-population cause (MSTR's); `GAP_NAMED`'s
possible split; `TRIGGER-MISSEQUENCE`'s provenance (mine); M3 sub-class D; and the `layer` axis
uncrossed against `verdict`.

---

## S.4 STOP: DO NOT DESCOPE THE TYPING WALK -- IT CARRIES A GOVERNANCE LOAD IT WAS NOT SCOPED FOR

**Recorded HERE, in the document where a descope decision would actually be made, because the whole
point of the finding is that this dependency has no defender.** Base CTO, relayed via `0.0.0_AB_MSTR~Z`
`@080110Z`:

> **The WS-C2 typing walk -- typing real specimens against the grammar -- is now the ONLY place
> SEMANTIC DRIFT ON A RESOLVING TOKEN becomes visible, as a typing DISAGREEMENT.**

**THE RESIDUAL IT COVERS:** `scope` or `grain` used in a sense D3 does not license -- **lexically
clean, passes CVO~Z's Amendment-7 declare-time lint perfectly, and quietly redefines a ratified word.**
A lint checks that a token RESOLVES; it cannot check that the sense is the licensed one. CVO~Z ratified
the lint, named this residual as one it cannot close, and **deliberately declined to invent a mechanism
for it** (the M15/M2 precedent -- name the homeless property rather than mis-route it). They identified
this walk as the existing partial mitigation.

**Base CTO has proposed a candidate mechanism -- high-semantic-room tokens must CITE the spec line they
use -- and it is with CVO~Z to ratify or drop. UNTIL THAT IS RULED, THIS WALK IS THE WHOLE OF THE
COVER.**

> ### **A MITIGATION NOBODY KNOWS THEY ARE PROVIDING IS ONE THAT GETS DESCOPED FOR REASONS THAT LOOK LOCAL AND CORRECT.**
> **AN UNSCOPED MITIGATION HAS NO DEFENDER.** It appears in nobody's requirements, so the decision to
> trim it is made by someone who cannot see what it was holding -- and their reasoning will be sound
> on every fact available to them.

**BINDING ON ME AND ON ANY SUCCESSOR:** the typing walk is not descoped, deferred or "declared
complete" on efficiency grounds **without first accounting for the A7.3 drift-cover.** If the candidate
mechanism ratifies, this constraint lifts and should be struck. Until then it stands.

*This is the same class as tonight's others with one variable changed: a correct local judgment resting
on a mechanism the judge never read -- except here the unread mechanism is **what a neighbouring
component is silently doing for you.*** And recording it in an inbox message alone would have
reproduced the defect exactly -- **a single-carrier record of a dependency whose failure mode is that
nobody knows it exists.**
