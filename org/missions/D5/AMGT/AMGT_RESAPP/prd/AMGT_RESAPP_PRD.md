# AMGT_RESAPP -- PRD (L4)

**archetype:** SCRIBE (spec) · **author** `1.0.0_SA_CTO~Z` (L4 owner: CTO, no COO, no CVO)
**status:** `LANDED` -- L3 + L4 registered 2026-09-10 ~18:3xZ

> ⭐ **THIS FILE IS NOW AT ITS HOME.** It was authored before this tree existed, staged at
> `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_RESAPP_PRD_STAGED_20260910.md` @`449a7c8fc2`, and
> **moved here byte-for-byte unchanged apart from this banner and the status line.** That deliverable
> is now a POINTER, not a second copy -- two carriers of one obligation drift from the minute the
> second is written, which is the exact defect that cost NFRA_REPORT a round today.

| | |
|---|---|
| **Directive** | D5 Alternative Research (placement SITEZ) |
| **Macro** | `AMGT` -- Andrew-direct @`1f89e24eac` |
| **L1 brief** | `docs/briefs/amgt-resapp-security-analysis-20260910.md` @`19ce7d5b4d` (**v2 -- see s.0**) |
| **L2 endpoint** | `.../deliverables/AMGT_RESAPP_ENDPOINT_20260910.md` @`3bc8f5f2c4` |
| **Origin** | Adam Muller (Head of Asset Management) -> Andrew, 2026-09-10, "Claude automation" |

---

## 0. THE VERSION HAZARD -- BINDING ON EVERY READER OF THIS PRD

⛔ **THE BRIEF EXISTS IN TWO STATES AND ONE OF THEM IS ON THE SHARED BRANCH.** Measured with a
positive control: v1 @`046337e2df` **is** an ancestor of `origin/SITEZ` (15,429 bytes); v2
@`19ce7d5b4d` is **working-tree only** (22,244 bytes). Token counts one variable apart --
`O10`/`O11`/`O12`/`F12`/`F13`/`StockTwits` appear **0 times in v1**, 4/2/3/2/1/1 in v2.

**A cell that resolves the brief from origin loses the entire validation territory and the whole
social limb, and the result looks complete.** Until `0.0.0_AB_MSTR~Z` pushes, **every worker face
citing the brief cites `@19ce7d5b4d` explicitly** and reads from the working tree.

---

## 1. ENDPOINT (step 2, `/endpoint --forward`)

**The fourteen outcomes are reproduced VERBATIM from the L2 endpoint @`3bc8f5f2c4` and are NOT
re-authored here.** `FWD-1`..`FWD-12` derive from brief `O1`-`O12`; `FWD-13` and `FWD-14` were added
at L2 and **accepted without reservation by `4.0.0_SA_CRO~Z`** (msg 21001) as its own gaps.

⛔ **`FWD-n` IDS ARE PERMANENT AND NEVER REUSED.** A new outcome takes the next unused number; a
retired one leaves its number vacant forever. The round-N analysis and any addendum cite them back.

> **The block lives at `AMGT_RESAPP_ENDPOINT_20260910.md` s.2 and is transcribed into this section
> unchanged when this file lands in the tree.** It is not duplicated here in the staged copy,
> deliberately: **two carriers of one obligation drift from the minute the second is written**, and
> until this file is in the tree the endpoint artifact is primary.

**BAR DISTRIBUTION: 13 of 14 are `EXERCISED`; only `FWD-9` is `APPLIED`.**

⚠ **THIS IS THE MOST IMPORTANT SINGLE FACT FOR L5.** Thirteen outcomes cannot be closed by any build.
**No cell may claim an `EXERCISED` outcome REALIZED on the strength of its own artifact** -- the
sibling project on this fabric graded eight outcomes REALIZED today against an artifact that had
never run once. **Grade the `DONE WHEN` state line, never the `ACCEPT` paragraph beside it.**

---

## 2. THE BOUNDARY

**THIS PROJECT OWNS:** the Security Analysis portal page and its design spec; the versioned pack
object and its store; the assembly path that fills it; and the print renderer that emits Adam's
artifact.

**IT RELIES ON AND DOES NOT OWN:** the Bloomberg terminal and its desktop API; the Bright Data
account; the residential-proxy + vision-authenticator pattern; the portal shell, auth and panel
primitives; and **the research corpus in SharePoint, which is READ-ONLY to us.**

⛔ **THE PROJECT BOUNDARY IS UNCHANGED BY THE MACRO RULING, AND THIS IS A NAMED TRAP.** Andrew ruled
that **`AMGT` (the macro) holds all of D5's research and analysis**, including the alt-research
corpus -- the research-call transcripts and the 63-name materiality queue. **That is a statement
about what the MACRO covers. It is NOT a statement about what THIS PROJECT consumes.**

Brief PART II stands verbatim: the corpus is *"the same directive, a DIFFERENT function"* and
**"AMGT_RESAPP does not consume or replace it."** ⛔ **If any later cell or seat proposes that
`AMGT_RESAPP` absorb the transcript corpus or the materiality queue, that is a NEW SCOPE QUESTION
REQUIRING ANDREW'S WORD.** It is not implied by the macro ruling and must not be inferred from it.
(Distinction drawn by `4.0.0_SA_CRO~Z`, msg 21007, and adopted.)

**EXPLICITLY NOT OWNED:** the missing Terraform declarations on the seven Seeking Alpha Lambdas (an
`AE_CloudOps` estate defect); the FactSet and CapIQ subscriptions; and **Adam's editorial judgment
-- the analyst-specific sections are the value of a pack and this project drafts toward them, it
does not replace them.**

---

## 3. CONSTRAINTS ON THE CUT

Each is binding on L5 and L7. Cite the constraint id, never this section.

### Data correctness -- these three are the measured landmines

**`C-UNIT-MAP-MEASURED`** -- ⛔ **A MNEMONIC-ONLY FIELD MAP IS SILENTLY WRONG BY 100x IN SOME CELLS
AND 1e6 IN OTHERS.** Measured (brief F4): market cap is absolute while net debt and enterprise value
are millions; shares outstanding is absolute while diluted-EPS share count is millions; margins are
percents where the source holds decimals; capital expenditure's sign is inverted. **Every mapped
field carries a MEASURED unit and sign, never an inferred one, and the measurement is per field.**

**`C-FISCAL-YEAR-JOIN`** -- ⛔ **NEVER JOIN PRICE TO FUNDAMENTALS ON THE DATE STRING.** Measured
(F5): 4 of 10 years land split, 14 rows for 10 fiscal years, and a date-string join **silently drops
40% of that name's price history**. **Fiscal year is the join key.**

**`C-BLOOMBERG-BASIS`** -- Andrew-ruled (F3): **adopt Bloomberg's definitions and STATE THE BASIS
BESIDE THE NUMBER.** No Bloomberg mnemonic reproduces FactSet's recurring EPS across 8 tested --
that normalization is proprietary and **must not be reverse-engineered into a lookalike figure.**
⚠ The field map was measured on **ONE security**; a US name, an ADR or a financial is the most
likely place F4's conventions differ, and **nothing establishes they generalise.**

### Pipeline shape -- constraints, not a design; sequencing is L5's

**`C-RAW-BEFORE-DERIVED`** -- raw vendor bytes land before anything derives from them. ⛔ **This is a
CORRECTNESS requirement and not an optimisation:** Bloomberg's derived fields have **no backfill**,
so a rule change that cannot be re-derived from stored raw bytes is a permanent data loss.

**`C-STAGE-PERSISTS`** -- every stage persists its own output and is **independently re-runnable**.
Serves `FWD-12` directly. **A single refresh that moves everything under one timestamp is a
violation, not a shortcut.**

**`C-VERBATIM-GATE`** -- wherever output quotes a source, the quoted text must be an **exact
normalised substring of the fetched text**; non-verbatim is **rejected and regenerated**. ⭐ **This
is a GATE, not trust-the-model**, it is machine-checkable, and the estate has already proved the
form.

**`C-MARK-NOT-DEGRADE`** -- ⛔ **a failed stage MARKS the pack; it never silently produces a thinner
one.** A thin pack that looks whole is the exact failure `FWD-10` exists to prevent.

### Validation -- the six classes, and what L4 does and does not fix

Brief III-B names six classes that must each carry a stated qualification rule: **a figure, a peer,
an identity, a news or social item, a source, a generated sentence.**

**`C-RULE-MUST-EXIST`** -- **an input class with no stated rule is NOT SHIPPED DARK.** It is either
ruled on or held back from the page. There is no third option.

**`C-CHECK-MUST-REFUSE`** -- ⛔ **A CHECK THAT CANNOT FAIL IS NOT A CHECK.** Every rule **names the
input that makes it refuse**, and that input is exercised. A rule whose refusal case was reasoned
rather than run has not been tested.

**`C-SHARED-DEFECT`** -- ⛔ **A CHECK SCOPED TO EACH ITEM CANNOT SEE A DEFECT THE ITEMS SHARE.**
Measured on this very project: the stale peer set passed every per-name look for months because
nothing asked what the 54 workbooks had in COMMON. **Every class carries a per-item check AND one
unscoped pass over the population.**

⛔ **NO THRESHOLD IS SET IN THIS PRD, AND THE OMISSION IS DELIBERATE AND BOUNDED.** L1 refused to set
one because a number invented early is treated as ratified by every later stage. **L4 does not
invent one either, for a different reason: the estate has not measured the distributions any
threshold would have to be drawn against.** ⛔ **An unmeasured exact constant fails closed while
looking principled**, which is worse than an absent one.

>> **WHAT L4 FIXES INSTEAD, AND THIS IS THE INSTRUCTION TO L5:** each class's cell must **produce the
>> measurement from which its threshold is drawn, and state the threshold in its own deliverable**.
>> The cell that maps figures measures the field population; the cell that admits news measures the
>> ratio of about-the-security to merely-contains-the-string. **A threshold arrives WITH the
>> distribution it was drawn from, or it is not a threshold.** <<

**`C-IDENTITY-RESOLVED`** -- serves `FWD-13`. The Bloomberg ticker, the Seeking Alpha symbol, the
investor-relations domain and the social account are **four different keys, and the social one has
no shared identifier at all.** ⛔ **Two sources may not be displayed together on one page until their
identity is confirmed resolved; where it cannot be, the page SAYS SO rather than showing them side
by side.** The measured instance is F6 -- 48 of 54 packs carrying another company's peer set.

**`C-LIST-OWNER`** -- serves `FWD-14`. The publisher allowlist and the company-to-social-account map
are **living lists that rot**. Each carries a **named owner** and a **rot signal**. ⛔ **An enumerated
list with no owner lapses silently** -- the same failure that left two vendor keys dead.

### Standing law -- inherited, not minted here

**`C-VENDOR-EGRESS`** -- ⛔ **NEVER call an external vendor API without Andrew's explicit per-use
word. Availability is not authorization.** This binds every Bright Data dataset call, every Seeking
Alpha fetch and every proxy request. **A cell may not spend that word and may not assume it.**

**`C-LISTING-NOT-CAPABILITY`** -- ⛔ **NOTHING ABOUT THE SOCIAL DATASETS HAS BEEN EXERCISED.** F12
measured they are LISTED and reachable: 1,763 datasets, HTTP 200. **No dataset was triggered, no
record returned, no cost, field schema, latency or freshness observed**, and whether the post-level
sources can be queried by cashtag at all is unknown. ⛔ **A LISTING IS A CATALOGUE ENTRY, NOT A
CAPABILITY** -- `FWD-11` must not be cut as though social data is in hand. **The first social cell's
job is to find out, and its acceptance criterion is allowed to be a measurement rather than a
feature.** ⚠ And F13: the cashtag-native venue carries **0 datasets** on this account, so the feed
is general-social plus finance-adjacent. **That limit is a required disclosure of the feed itself**
(`FWD-11`'s own source line), not a footnote.

**`C-ZONE-IN-CALLER`** -- one account credential, three zone archetypes, selection lives in the
caller. ⚠ **F12's dataset API is a FOURTH SURFACE, not a fourth zone** -- same credential, different
API. A reader who assumes everything is one of three zones will hunt for a zone that does not exist.

**`C-DESIGN-SPEC-FIRST`** -- **no `.tsx` is written until the design spec is approved.** The estate's
own precedent gates it in exactly these terms.

**`C-NO-CONTACT`** -- ⛔ **NO SEAT CONTACTS ADAM MULLER.** Andrew-ruled. Requirements reach him
through Andrew and no other route.

---

## 4. SURFACE MANIFEST (step 4 -> step 5) -- one row per ENGINE

| id | outcome | surface | claim | measured-by | verb | depends on | bound |
|---|---|---|---|---|---|---|---|
| S1 | `FWD-1` | THE MODEL BLOCK -- the mechanical one-pager figures for a covered name | absent | F2: ~20 line items x 10 years + ~25 header scalars; 180 points / ~3.4 KB / one call for one security | build | -- | `C-UNIT-MAP-MEASURED`, `C-FISCAL-YEAR-JOIN`, `C-BLOOMBERG-BASIS` |
| S2 | `FWD-2` | THE ON-DEMAND PULL -- a name outside coverage, by ticker | absent | F2: the binding constraint is UNIQUE SECURITIES TOUCHED, not volume | build | S1 | the page states it is fetching now; `C-VENDOR-EGRESS` |
| S3 | `FWD-3` | THE PROVENANCE FACE -- source, basis and vintage beside every figure | absent | F3 (basis stated beside the number, Andrew-ruled) | wire | S1 | `C-BLOOMBERG-BASIS` |
| S4 | `FWD-4` | THE COVERAGE READER -- recent commentary, ranked by recency and frequency | absent | F7 (the landed corpus is an ARCHIVE, not a feed: dates stop at 2026-04, 0 of 200 sampled carry a ticker); F11 (the SERP path works; the obvious link field is an obfuscated redirect) | build | S12 | `C-VENDOR-EGRESS`, `C-RULE-MUST-EXIST` |
| S5 | `FWD-5` | THE PRINT RENDERER -- Adam's artifact | absent | F1 (template and packs are consistent, provenance confirmed by a shared misspelling) | build | S1, S3 | `C-DESIGN-SPEC-FIRST` |
| S6 | `FWD-6` | THE VERSION STORE -- snapshots that accumulate rather than overwrite | absent | brief O6; PART V (`opal-data-research` measured ABSENT on the live plane) | build | -- | `C-RAW-BEFORE-DERIVED` |
| S7 | `FWD-7` | THE COVERAGE-FRESHNESS VIEW -- Adam's one place | absent | brief O7 | wire | S6 | -- |
| S8 | `FWD-8` | THE PEER SET -- comparable to THIS company, or absent with a reason | **BROKEN TODAY** | F6: 48 of 54 (88.9%) carry a stale set copied from one workbook; 4 (7.4%) are genuine and hand-chosen | build | S12 | `C-IDENTITY-RESOLVED`, `C-SHARED-DEFECT` |
| S9 | `FWD-9` | THE DRAFTING FACE -- generated prose marked, beside its evidence | absent | brief O9; Andrew's ruling on limb order | wire | S1, S4 | `C-VERBATIM-GATE` |
| S10 | `FWD-10` | THE CHECK FACE -- pass, fail or provisional, per figure | absent | brief III-B | wire | S11 | `C-MARK-NOT-DEGRADE`, `C-CHECK-MUST-REFUSE` |
| S11 | `FWD-10`, `FWD-3` | THE QUALIFICATION RULES -- one per class, each naming its refusal input | absent | brief III-B, six classes | build | -- | `C-RULE-MUST-EXIST`, `C-CHECK-MUST-REFUSE`, `C-SHARED-DEFECT` |
| S12 | `FWD-13` | THE IDENTITY LAYER -- ticker, symbol, IR domain, social account | absent | PART V (three keys + a social layer with no shared identifier); F6 as the measured failure | build | -- | `C-IDENTITY-RESOLVED` |
| S13 | `FWD-11` | THE SOCIAL FEED -- admitted by a stated rule | absent | F12 (1,763 datasets LISTED, none exercised); F13 (0 cashtag-native) | **measure, then build** | S11, S12 | ⛔ `C-LISTING-NOT-CAPABILITY`, `C-VENDOR-EGRESS` |
| S14 | `FWD-12` | THE INPUT LEDGER -- per class: source, last run, outcome, re-run | absent | brief O12 | wire | S6 | `C-STAGE-PERSISTS` |
| S15 | `FWD-14` | THE LIST REGISTER -- allowlist + social map, each owned, each with a rot signal | absent | PART V (both rot; an unowned list lapses silently) | build | S12 | `C-LIST-OWNER` |

⭐ **S12 IS THE ROOT AND IT IS NOT IN THE BRIEF'S OWN SURFACE LIST.** Four surfaces depend on it
(S4, S8, S13, S15) and it is the direct remedy for the one defect this project has actually measured
in production. **Cutting S4, S8 or S13 before S12 rebuilds F6 on a new axis.**

⚠ **S13 IS THE ONLY ROW WHOSE VERB IS `measure, then build`**, and that is deliberate: its substrate
is a catalogue nobody has exercised. **Its first cell may honestly deliver a measurement rather than
a feature**, and an acceptance criterion that demands a working feed from an unexercised catalogue
is a criterion a correct build cannot satisfy.

---

## 5. WHAT MUST BE TRUE, AND IS NOT YET

Carried from brief PART V. **These are preconditions, not outcomes -- no `FWD-n` is graded on them.**

- **The desktop/cloud seam is crossed somehow.** The portal runs in AWS; the Bloomberg interface is
  local to one device. **Any design must say how a browser request reaches it.**
- **The Bloomberg session's state is visible to the user.** Sign-out is the most common failure and
  costs a budgeted repair; a page that fails silently against it reads as broken.
- **`opal-data-research` exists** -- **measured ABSENT on the live plane.** `C-RAW-BEFORE-DERIVED`
  cannot hold until it does.
- **A decision on paywalled sources.** If analysis behind a login is in scope, the vision-
  authenticator pattern is the route; if public pages suffice, neither it nor the credential is
  needed. **Nobody has decided, and whether the login is captcha-gated is unknown.**

---

## 6. WHAT THIS PRD DOES NOT CLAIM

- **No qualification threshold exists anywhere in this document.** Anyone reading a number into s.3
  is reading something that is not there.
- **The field map was measured on ONE security.** F4's unit conventions are the most likely thing to
  differ on a US name, an ADR or a financial.
- **Whether the stale peer set reaches the PRINTED packs is UNVERIFIED.** The document pastes
  spreadsheet output as an image and which image is the comparison was never traced. ⛔ **Nobody
  should conclude packs shipped wrong on the strength of this PRD.**
- **The IR scan was proven on one name, not at scale**, and the ex-US names are the risk.
- **Nothing about the social datasets has been exercised** (`C-LISTING-NOT-CAPABILITY`).
- **No decomposition, no sequencing, no task orders.** That is L5 and it is not this seat's.

---

## 7. PROVENANCE

```
GROUNDED ON:  L1 brief @19ce7d5b4d read IN FULL from the working tree (330 lines, 22,244 bytes)
              L2 endpoint @3bc8f5f2c4 -- the fourteen outcomes, unmodified
              4.0.0_SA_CRO~Z msg 21001 (both additions accepted) and msg 21007 (the macro-scope
                vs project-boundary distinction adopted at s.2)
              Andrew-direct @1f89e24eac -- the macro and its scope
NOT READ:     the task-order register; any sibling project's code or decomposition; the D5
              directive PRD (reading the parent would import outcomes nobody wrote for this project)
UNVERIFIED:   every F-numbered measurement is the CRO's, re-derived by nobody. This PRD carries
              them as CITED, not as CONFIRMED, and a cell relying on one re-measures it first.
```

**Push state:** LOCAL at write time; ancestry rather than a tip hash. `0.0.0_AB_MSTR~Z` pushes.
