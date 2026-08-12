# Andrew-direct — FOUR RULINGS: the firm axis, Bloomberg metering, firm isolation, and Part 2

**Channel:** direct at the `1.0.0_SA_CTO~Z` terminal, 2026-08-12 ~20:20Z, answering a 4-card `/open-calls`.
**Recorded by:** `1.0.0_SA_CTO~Z`. **My Call-1 recommendation was REJECTED. That is the most important line here.**

## VERBATIM

> "1.) bd as in opal-data-bd, or bd-pipeline, is referential to Black Diamond, the data vendor. we had set
> this bucket up initially for 49 Financial's data, however we are now migrating primarily to a Schwab
> account for 49. inf as in opal-data-inf or inf-pipeline is Inflection Wealth Management. These are two
> different firms. 2.) They meter amount of data in size being downloaded. I want to know all their
> endpoints so we have the ability to go through their key surfaces, which I'm told include Financials,
> Market Price, News, Earnings Estimates, and even some functions that seem nested in various places like
> WACC, debt profile of short/long-term debt and associated costs, and others. 3.) This does need to be
> firm-specifc and gated. Opal users should be able to see all of them but firms should not be able to see
> other firms. 4.) Rec is good"

---

## RULING 1 — **TWO DIFFERENT FIRMS. MY RECOMMENDATION WAS WRONG.**

I recommended ruling them **one firm with a tenant partition**. **REJECTED.** His words: *"These are two
different firms."*

⛔ **AND THE NAMING IS VENDOR-AXIS, NOT FIRM-AXIS — which is the fact that made this confusable:**

| bucket | named for | actually holds | firm |
|---|---|---|---|
| `opal-data-bd` | **Black Diamond — the DATA VENDOR** | 49 Financial's data | **49 Financial** |
| `opal-data-inf` | Inflection | Inflection's data | **Inflection Wealth Management** |

**`bd` is a VENDOR name carrying a FIRM's data.** That is why `platinum/49financial/` sits *inside*
`opal-data-bd` — a divergence I recorded earlier as "wire-protocol" and could not explain. **It is now
explained: the prefix is the firm, the bucket is the vendor.**
**AND 49 IS MIGRATING PRIMARILY TO A SCHWAB ACCOUNT** — so the vendor axis is moving under the firm while
the firm stays put. A bucket named for a vendor the firm is leaving is a naming defect with a timer on it.

### Consequences, in severity order

1. ⛔ **THE TICKETS DEFECT IS NOW A CROSS-FIRM EXPOSURE BETWEEN TWO GENUINELY SEPARATE FIRMS.** Not a
   tenancy nuance — 49 Financial and Inflection Wealth Management are different firms, and any
   authenticated portal user can list and mutate either one's tickets. **Ruling 3 makes this a direct
   violation of a standing sovereign requirement**, not merely a missing control.
2. **NEVER#2 genuinely applies to these two trees.** My §9.10.3 reasoning stands on its own terms — an
   audit rectangle creates no data flow, moves no object, grants no access — but its two riders are now
   load-bearing rather than precautionary: **never a warrant for a cross-firm join/mirror/sync**, and
   **every consumer preserves the firm partition.**
3. **The 78 held W4b cells are UNBLOCKED under the union ruling** (§9.10.3): entity set = the union, with
   **firm as a declared per-entity dimension**. That ruling was correct and is now *required* rather than
   merely defensible, because a rectangle-wide firm assumption would assert one firm's shape over another's.
4. **A page fetching both firms is not itself a defect** — per Ruling 3 it is acceptable *if and only if*
   the gate enforces per-firm visibility. **The defect is an ungated one.**

---

## RULING 2 — **METERING IS BY DOWNLOADED DATA SIZE (bytes).** Plus an expanded enumeration mandate.

*"They meter amount of data in size being downloaded."*
**So neither of the two models the slice design was branching on.** Consequence for W8's sized-pull menu:
**optimise BYTES** — narrow field lists, short date spans, few securities — and **schema/identifier
resolution is cheap relative to bulk values**, which vindicates the call-shape rule (reference calls for
resolution, not for values).

**AND THE SCOPE EXPANDS — he wants the ENDPOINT UNIVERSE:** *"I want to know all their endpoints so we have
the ability to go through their key surfaces."* Named surfaces, his list:
**Financials · Market Price · News · Earnings Estimates** — plus **nested functions**: *"WACC, debt profile
of short/long-term debt and associated costs, and others."*
⚠ *"and others"* and *"seem nested in various places"* are his words and they are **an instruction to
enumerate, not a closed list.** The deliverable is the endpoint universe with a denominator, not a
five-item checklist.

---

## RULING 3 — **FIRM ISOLATION IS A STANDING REQUIREMENT.** Two-tier authorization, ruled.

*"This does need to be firm-specifc and gated. Opal users should be able to see all of them but firms
should not be able to see other firms."*

| principal class | visibility |
|---|---|
| **Opal users** (internal) | **ALL firms** |
| **Firm users** | **OWN firm ONLY** |

⛔ **THIS IS AN ARCHITECTURAL REQUIREMENT ACROSS THE WHOLE ACCESS LAYER, not a ticket-service fix.** It
binds: the W5 catalog (firm as a first-class key — already a precondition, now sovereign-backed), the W7
SharePoint registry, the W9 document-extract spec, and **every serving surface.**
✅ **AND IT IS THE FIRST SOVEREIGN GATE REQUEST ON AUTHORIZATION** — so building it is legal under the
2026-08-06 no-inferred-gates rule. **The remedy for the tickets defect is now specified rather than
open:** two-tier, firm-scoped, and the sibling trade service is the working reference implementation.

---

## RULING 4 — Part 2 rec **ACCEPTED**: satisfied for SPREADSHEETS, documents carried on W9

*"Rec is good."* **Part 2 is SATISFIED for workbooks/spreadsheets**; the `.docx/.pdf/.pptx` gap
(`read_document` returns a rendition, not text) is carried by **W9 (spec only)**. **W6 guardrails now has a
defined boundary** — which was the reason the call needed answering.

---

## What this costs me, stated plainly

**My Call-1 recommendation was wrong, and it was the call I was most confident about.** I reasoned from
measured topology — one page fetching both, near-disjoint artifact sets, ID spaces differing in kind — and
concluded *one firm, two tenants*. **The topology was real and the inference was backwards: those are the
signatures of two firms sharing a serving surface, not one firm with two shapes.** The estate could not
tell me, because **the buckets are named on the vendor axis and the firms live in the prefixes** — and no
instrument I ran was pointed at "whose company is this," which is not a measurable property of an S3 tree.
*This is the class CLAUDE.md already names: the estate has instruments for what is DEPLOYED and none for
what is OURS.*
