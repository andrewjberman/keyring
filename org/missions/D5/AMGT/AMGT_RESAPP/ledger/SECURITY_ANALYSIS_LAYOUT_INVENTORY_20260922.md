# Security Analysis -- the layout pass: what connects to what, and what is BUILT versus INTENDED

**Author:** `1.0.0_SA_CTO~Z`, 2026-09-22 ~20:5xZ. **Asked by Andrew** at this terminal ~18:2xZ, VERBATIM:
*"This is actually a good opportunity for us to take a pass to go over the /draw layout for every panel as its
designed now ... I want to make sure we are very clear on what connects to what and how the frontend is explicitly
laid out as intended, and also what has been built to that end thus far, as again nothing is displaying thus far."*
Record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260922_182xZ_AMGT_CORPUS_SPLIT_BLOOMBERG_TO_CLAUDE_ALLOWED_LEAD_PANEL_DETERMINISTIC.md`.

⛔ **THIS IS A READ, NOT A PLAN.** It cuts no cell, mints no outcome and changes nothing. Every claim carries
`file:line`. Where a number is a denominator it is printed. Where something could not be determined it is named as
undetermined rather than guessed.

**Method and its limit:** a read of the repo at HEAD (portal tree, the handler, the Terraform mount), plus this
seat's own earlier LIVE reads of the served edge. **No network call was made for this document.** One count below
(the unrendered-field census) was produced by textual matching and its false-positive mode is stated at that
section.

---

## 0. THE ONE-SCREEN ANSWER

| question | answer |
|---|---|
| Is the page built? | **Yes, and more completely than "nothing loads" suggests.** 29 of 30 modules in the page tree are reachable; 12 of 12 components render; 5 of 5 tabs route. |
| Then why does nothing display? | **A missing CDN rule, not a missing page.** Every one of its API calls returned the SPA shell instead of data. Fix cut as `rk-123`, at the CloudOps seat now. |
| Will the page be right once that lands? | **Mostly -- but three things will still be wrong**, and none of them is the CDN: 0 of 5 tabs can show an error, the Lead Panel's headline slot is a hardcoded literal, and one overlay tile is mislabelled. |
| Can Andrew find a company by name? | **No.** The search box is exact-identifier only. "Lenovo" and "Boeing" cannot match anything. |
| Is the page writing prose at us? | **Almost never.** 11 of 12 Lead Panel slots are deterministic; exactly one can carry generated prose, it is second choice behind a vendor field, and it is always badged `machine`. |

---

## 1. THE PAGE'S SHAPE

**Route:** `portal/src/App.tsx:447-448` mounts `/security-analysis` and `/security-analysis/:securityKey`, both behind
`<ProtectedRoute requireDev requireAdmin>`; the nav item at `:119` carries `requiresAdmin: true, requiresTier:
'internal', requiresDev: true`. **That is the gating Andrew asked for on 2026-09-22 and it is in place.**

**Five tabs**, declared once at `constants.ts:72-78` and rendered at `SecurityAnalysis.tsx:84-88`: Thesis (default,
`:45`), Exec Management, Peers, Model, Posture. `types.ts:1023` declares exactly those five -- **type and constant
agree.** A sixth, Coverage, is **deliberately retired** (`SecurityAnalysis.tsx:16`, `constants.ts:71`) and no
component file for it exists.

**The Lead Panel is not a tab.** It is mounted at `SecurityAnalysis.tsx:60`, `sticky top-0 z-40` (`:59`), outside the
tab content area **so it survives a tab change** (`:20-21`). Print export is likewise not a tab: it is an action in
the header slot (`:56`).

**Denominators for the page tree:** 30 `.ts`/`.tsx` modules, **29 reachable**; the one that is not is
`__rendercheck__/renderCheck.tsx`, a verification driver. 12 of 12 components are rendered; **0 orphan components.**
One orphan exists at HOOK level: `useCoverageSet` (`hooks/useLeadPanelApi.ts:135-143`) is called by no component --
its client function and the whole `CoverageSet` type tree are dead in the UI.

---

## 2. WHAT CONNECTS TO WHAT -- the wire, panel by panel

Every call goes to `const BASE = '/api/scoped/amgt'` (`api/endpoints/amgt-lead-panel.ts:47`).

### The Lead Panel fetches for itself -- 6 route-keys

| what | path | reads from |
|---|---|---|
| ranked list | `/lead-panel/rankings/{movement}/{subject}?limit=10` | **DynamoDB** `opal-harvest-security-metrics`, GSI `axis-rank-index` (`scoped_amgt.py:141`, `:144`) -- not S3 |
| rank series | `/lead-panel/timeseries/{mv}/{sub}?tickers=...&days=30` | same table, point reads |
| starred | `/watchlist` (firm comes from the edge-injected `X-Firm-Id`, not the path) | same table |
| star / unstar | `/watchlist/star`, `/watchlist/unstar` | same table |
| refresh | `/refresh` | **nothing -- see the defect below** |
| security overlay | `/security/{key}/overlay` | model block + description + publication pools + posture + peers + 4 DynamoDB reads |

**Everything else in the header is props.** `HeaderBrief`, `SecurityOverlay`, `RankedList`, `StarredList`,
`RankedChart`, `ProvenanceLine`, `GenerationCaption`, `IdentityLine`, `CheckFaceBadge`, `ThesisDriverChart` make no
calls of their own.

### The five tabs -- three of them share ONE payload

| tab | endpoint | what it reads out of it |
|---|---|---|
| Thesis | `/security/{key}/thesis` | drafted sections, drafting status, thesis driver + chart, held uncited counts, provenance |
| Exec Management | **the same `/thesis`** | `data.management` only |
| Model | **the same `/thesis`** | fiscal-year figures, check face, model status, cases, scores |
| Peers | `/security/{key}/peers` | basis, members, CSC columns, vintages |
| Posture | **`/thesis` AND `/peers`, TWICE EACH** -- once for the subject, once for the comparable | `data.posture` + both sides' bundles to resolve citations |

React Query dedupes on `['amgt-lead','thesis',key]` (`constants.ts:47`), so **moving between Thesis, Exec Management
and Model costs zero extra network.** Posture alone can issue **four** concurrent reads.

### The backend agrees with the frontend

The handler is `lib/research/api/scoped_amgt.py` (4,012 lines) -- **not** under `infra/aws/lambda/`, which is worth
knowing before anyone goes looking. Its route table is data at `:3982-4012`: **16 routes**, and the Terraform mount
declares the same 16 (`infra/aws/terraform/harvest/scoped-amgt-api.tf:315-335`).

- **Frontend calls with no handler: 0 of 11.** Nothing the page asks for is unimplemented.
- **Handler routes no frontend code calls: 5 of 16** -- `/freshness`, `/lists`, `/security/{k}/ledger`,
  `/security/{k}/versions`, `/security/{k}/compare`. The handler's own docstring says so honestly at `:3796-3799`.
- **Plus one half-orphan:** `/security/{k}/coverage` has a client function AND a hook, and no component calls it.
- So: **10 of 16 routes are exercised by mounted UI.**

⚠ A stale comment at `amgt-lead-panel.ts:25-31` still warns that routes are not declared at the edge. **That
caveat is now obsolete** and should be struck so a later reader does not chase it.

---

## 3. WHY NOTHING DISPLAYED -- and what will STILL be wrong after the fix

The cause is settled and is not in this tree: **no CloudFront behavior existed for `/api/scoped/amgt/*`**, so all
16 mounted routes fell through to the SPA default and returned `200 text/html`. Measured live by this seat with two
positive controls (row `Z-S226`); fix cut as `rk-123`, at `0.7.0_AE_CloudOps`.

**Three defects will survive that fix.** None is the CDN; each is in the page or its wire.

### (a) 0 of 5 tabs can report an error -- and this is why the page looked DEAD rather than BROKEN

Every tab destructures `{ data, isLoading }` and renders `{!isLoading && data && ...}`. On a settled error React
Query gives `isLoading=false, data=undefined`, so **the tab renders a titled panel with an empty body and no
message.**

| tab | `isError` branch | loading | empty-data |
|---|---|---|---|
| Thesis (`:129`) | **NO** | YES `:161`, `:177` | YES, 3 layers |
| Exec Management (`:209`) | **NO** | YES `:235` | YES, 3 layers |
| Peers (`:141`) | **NO** | YES `:164` | YES, 2 layers |
| Model (`:183`) | **NO** | YES `:204` | YES, 3 layers |
| Posture (`:338`) | **NO** (nor on the comparable's 2 extra queries) | YES `:379` | YES, 4 layers |

⭐ **The empty-data handling is excellent -- 2 to 4 distinct layers per tab, each naming WHY and often WHO owns the
absence.** The gap is exactly one branch wide, and the fix already exists in this codebase: **the Lead Panel HAS a
full error path** (`LeadPanel.tsx:229`; `RankedList.tsx:141-160` renders a read-failure block that explicitly makes
no producer claim, and `:26-38` documents it as the remedy for a measured defect where error and empty rendered
byte-identically). **That fix was applied to the Lead Panel and never propagated to any tab.** Row `Z-S227`.

### (b) The Lead Panel's headline slot is a hardcoded literal

`RankedList.tsx:256-258` renders the string `"no headline yet"` for **every row, unconditionally**. It is bound to
no data field. The rationale is in the file (`:11-14`): the article store measured empty on 2026-09-11. **It is
honest, and it is also now a permanent literal that no data can ever replace** -- when articles land, the slot will
not notice. This should become a real binding or an explicit absent-state.

A sibling dead branch: `RankedList.tsx:66-72` declares an `emptyReason` prop and `:190-194` renders a richer empty
sentence **with its denominator** -- and `LeadPanel.tsx:373-395` never passes it, so that branch is unreachable.

### (c) One overlay tile is mislabelled, and check faces never reach the overlay

`SecurityOverlay.tsx:134` labels the right tile **"Breakout (price)"** while `:135` and `:141` read the **TRENDING**
row (the server sets `price` from TRENDING_PRICE, `scoped_amgt.py:1948`, comment `:1887-1890`). **The tile labelled
Breakout shows Trending.** The server produces all 4 crossed axis reads (`:1915-1934`); the overlay renders 2 of 4,
and one of those 2 is mislabelled. *Undetermined:* whether that label was ratified as shorthand.

Separately, `SecurityOverlay.tsx:116` renders `ProvenanceLine` with no `verdict` and no `reason`, so
`ProvenanceLine.tsx:44-58` always computes `isRefused=false` and never draws a check-face badge. **A REFUSED figure
shows as a bare number on the Lead Panel while the same figure shows as a refusal on the Model tab**
(`ModelTab.tsx:48-53`). The overlay bundle does not carry `check_face` at all (`scoped_amgt.py:1936-1951`) -- **a
wire gap, not a prop omission.**

### (d) A fourth, smaller: the Refresh button is a no-op with no surface

The client type says `{queued: boolean}` (`amgt-lead-panel.ts:114-119`). The server returns
`{refresh:"declared", security_key, carrier:{...}, note}` and **enqueues nothing** (`scoped_amgt.py:3915-3932`,
whose own `note` says so). The button (`LeadPanel.tsx:333-343`) fires and forgets with no success or failure
surface. **The client type is a fiction.** Nothing is broken by it today; it will mislead the next reader.

---

## 4. THE LEAD PANEL, against Andrew's deterministic rule

His ~18:2xZ word: *"I don't think we need generated prose in Lead Panel, most likely Lead Panel has a very short
excerpt from each of the underlying panels in a structured form (deterministic, no new inference required)."*

**The panel is ALREADY almost entirely deterministic**, which means his rule is close to satisfied rather than a
rebuild:

- **Ranked rows** are pure numeric formatting off producer values (`RankedList.tsx:111-120`), and the module header
  at `:5-7` states no sort, score or re-rank happens client-side.
- **The Posture header line** (`LeadPanel.tsx:135-160`) is a client-side `switch` over the server's verdict enum
  producing fixed English -- **template text over a machine verdict, not generated prose.** It carries a `machine`
  badge (`:189-195`) and a fixed closing clause: *"a machine's view for a person to accept or reject, never an
  instruction"* (`:199`).
- **GenerationCaption, ResolutionNote, StarredList counts, overlay figures** -- all fixed strings with interpolated
  values.

**Exactly ONE slot can carry generated prose:** `HeaderBrief.tsx:49-57` renders `description.text`. The server's
route order (`scoped_amgt.py:2925-2934`) makes route 1 a **Bloomberg header scalar** (`CIE_DES`), returned
`generated: False`; **route 2 is the first sentence of the LLM-drafted company description**, marked `machine` and
gated by a content test (`:2346`, `:2977`). When route 2 serves, the component draws a `machine` badge first.

⚠ **So the gap between the page today and his rule is ONE slot, and the structured per-panel excerpt he described
does not exist yet at all.** That excerpt is an `AMGT_RESAPP` addendum item, not a defect.

---

## 5. SEARCH -- why "Lenovo" finds nothing

One box, `LeadPanel.tsx:321-332`, placeholder `"Search any ticker"`, present in both modes. **No submit button, no
clear, no dropdown, no typeahead, no debounce, no result list** -- Enter is the only trigger.

`handleSearchSubmit` (`:251-257`) passes `searchInput.trim()` **verbatim** to `onSelectSecurity`, which only stores
it (`useSecurityAnalysisState.ts:52-54`, whose comment at `:45-51` is explicit that nothing on the page converts one
identifier form into another). The string is spent as a path segment and resolved server-side only
(`scoped_amgt.py:3860-3861` -> `resolve_identity` `:1751-1853`), against **two** surfaces and no third:

1. **`crosswalk/v1`**, an **exact dictionary hit** on a whitespace-collapsed, uppercased token
   (`crosswalk.py:902`, `:769-770`), indexed over exactly **5 form classes** -- `bloomberg`, `display_ticker`,
   `model_key`, `bloomberg + " Equity"`, and persisted association keys (`:773-783`). ⛔ **No company-name field is
   indexed, and no substring, prefix, edit-distance or token matching exists anywhere in the path.**
2. A landed artifact looked up **by filename verbatim** (`scoped_amgt.py:1773-1774`, `:1819-1822`).

A miss returns `UNRESOLVED` with the raw string echoed and the crosswalk's record count as the reason; an ambiguous
form is **refused, never guessed** (`crosswalk.py:889-901`). The page then renders `UNRESOLVED: {requested}` plus
*"no canonical security matches this identifier"* (`IdentityLine.tsx:41-49`, `:67-71`).

**In plain terms: Andrew must type `BA US`, `BA US Equity`, `BA_US_Equity` or a harvester association key. Case and
whitespace are the only forgiveness the system offers.** Row `Z-S228`. A name index is an addendum item.

---

## 6. WHAT IS TYPED ON BOTH SIDES AND DROPPED AT THE COMPONENT BOUNDARY

`types.ts` is 1,023 lines, **76 exported types, 301 distinct declared field names**. **86 of 301 (28.6%) appear in
no runtime module.**

*Method limit, stated so the number can be discounted:* textual matching of field names across runtime modules with
comments stripped and harness files excluded. A field consumed only via a spread or `Object.entries` would be a
false positive. None was found; none can be ruled out.

⭐ **The pattern is the finding, not the count. What is systematically unrendered is the PROVENANCE AND AUDIT
layer** -- the fields that say *which object, read how, from where, and why this one was chosen*:

| cluster | what is dropped |
|---|---|
| the whole Coverage tree | ~17 fields (`types.ts:492-549`) -- served, typed, hooked, never mounted |
| Posture comparable selection | `comparable_held`, `rung_reached`, `log_cap_distance`, `preset`, `held_basis`, `weight_by_book`, `elements` -- **the entire record of WHY this comparable** (`:778-846`) |
| Peer member attributes | 8 of 12 `PeerMember` keys, incl. `country`, `sector`, `rung_name`, `cap_ratio_to_subject` (`:412-425`) |
| CSC registry metadata | `registry_name`, `in_registry`, `relation`, `derivable_from`, `subtraction` (`:427-455`) |
| Management provenance | 9 fields incl. `filing_source_accession`, `absence_reason_class`, `officers_with_tenure` (`:717-764`) |
| Ranking read audit | `payload_hash`, `rows_read`, `read_attempts`, `rank_sort`, `unread_pointer_count` (`:96`, `:151-153`, `:191-197`) |
| price-row detail | `px_start`, `px_end`, `trading_days_observed` -- **the dates render, the prices do not** (`:173-176`) |
| pool-read audit | `object_key`, `read_completed`, `store` -- the "which absence is this" evidence (`:400-408`) |

**The value layer is rendered; the show-your-work layer is carried all the way to the component and discarded.**
That is directly relevant to the analysis layer: `AMGT_CORPUS`/the addendum will add MORE provenance, and it will
land in the same place unless the page grows somewhere to put it.

---

## 7. INTENDED BUT NOT BUILT

- **The timeline section spec** -- `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~8/SPEC_SECTION_timeline.md`, merged @`a8fe955b24`: intended behaviour for **this** page, awaiting Andrew's approval, **no `.tsx` written** (named by `2.0.0_SA_COO~Y`, msg 24388).
- **The deterministic per-panel excerpt** for the Lead Panel's Security toggle view (Andrew ~18:2xZ) -- not started.
- **The analysis layer's prose slots** on Exec Management, Peers and Model; the Posture synthesis swap; the Export under the brand law -- all addendum, none built.
- **A name/ticker search index** -- not started.
- **5 served routes with no consumer** (`/freshness`, `/lists`, `/ledger`, `/versions`, `/compare`). *Undetermined:* whether they are meant for this page or another surface; the handler names outcomes but no consumer, and no PRD in the portal tree names a panel for them.

---

## 8. WHAT I COULD NOT DETERMINE

1. **Whether the mounted routes return data in the deployed environment.** No network call was made for this
   document; the 16-vs-16 route agreement is textual. The live behaviour this seat DID measure is the edge fault
   (`Z-S226`), separately.
2. Whether the 5 dark routes are for this page.
3. Whether `"Breakout (price)"` is a defect or ratified shorthand.
4. Whether `useCoverageSet` is a deliberate hold pending the header-feed decision (`constants.ts:71` retires the
   Coverage tab) or an oversight.

---

## 9. WHAT THIS SUGGESTS, ranked -- proposals only, nothing cut

1. **The tab error branch** (defect a). One shared component, five call sites, and the pattern already exists in
   `RankedList`. It is the difference between a page that says what is wrong and a page that looks dead -- which is
   what Andrew saw.
2. **The overlay's check-face wire and the Breakout label** (defect c). A refused figure currently renders as a
   plain number in the most prominent position on the page.
3. **The headline literal** (defect b) and the unreachable `emptyReason` branch.
4. **The Refresh button's contract** (defect d) -- either wire the queue or make the button say what it does.
5. **A name index for search** -- addendum; the crosswalk's 5 form classes are the place it would go.
6. **Somewhere to put provenance** (section 6) before the analysis layer adds more of it.

-- `1.0.0_SA_CTO~Z`
