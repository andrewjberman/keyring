# DSGN_IRPTV1 -- FAST pins graded after the fact, 2026-09-28 (`3.0.0_SA_CVO`)

**Interval:** FAST under `2.0.0_SA_COO~D`, lease `org/mcp/drive-mode.log` ARM 2026-09-28T17:47:43Z (expires 19:47:43Z,
surface `portal/src/pages/InvestorReporting`). **Seating:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_180xZ_SEATING_CVO.md`
@4cfdc2bd49. **Rule:** spine Closer, FAST mode, as carried by `.claude/skills/closer-drive/SKILL.md:46-47`: the CVO grades
each landed pin after the fact on the real run's artifact; a FAIL becomes the next item; nothing waits on the grade.

**Claim class:** the artifact is a `/ui-walk` on localhost:5174 signed in as the walker service account (real backend,
real data), not a driver fixture. The walk directory is gitignored (`.gitignore:89` `tmp/`), so each graded PNG is
bound here by md5.

**Tally:** 4 pins handed over. 1 PASS (`a47d3a75`). 1 PARTIAL FAIL (`528acdcd`: the source-age half passes; the
"label alone" half fails on the Analysis stage line, next item N1). 1 PARTIAL PASS (`bfafa6c0`: the drill half passes
on a real run; the Asset Category Views half is NOT GRADED, unit only). 1 NOT GRADED (`921e6808`, no real run). Pins 5 (`38986671`) through 9 (`816eeb58`): NOT GRADED on a real run
(none exists; walker runs paused); their unit evidence holds.

## Grades

| # | pin (portal DEV) | claim | evidence read | grade |
|---|---|---|---|---|
| 1 | `a47d3a75` FAST item 1 (UIC-10/12/13, row S30) | a negative account is a labelled line, never a wedge; a wedge under 5% carries no inside label and the legend names every slice; OVER WHAT shows every account whole | (a) `tmp/ui-walk/20260928T182319Z/shots/017-cowdin-holdings.png` md5 `40889b2f1f5647349615908e19324815`, opened and read; (b) `.../006-identity-cowdin-open-Show-all-11-accounts.png` md5 `ac6bc4df73e874635b5850a0b7e59abf`, opened and read; (c) the pin's own test re-run by this seat: `bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-72.holdings-any-count.test.tsx` at portal HEAD `a47d3a75` -> 1 pass, 0 fail, `VERDICT: HOLDINGS-ANY-COUNT-OK`, controls printed (old-feed signed sum -530212.96; three-account control unchanged); (d) CI on the commit: `CI - Build & Validate` completed/success (`gh run list --commit`) | **PASS** |

Detail for pin 1, read off shot 017 (Cowdin, Anna & Adam; 11 accounts; HOW MUCH $3,689,679.21):
- UIC-12: the pie draws 10 wedges; the one negative account prints below it as "****8774 / UTMA: -$169,336.52 (a
  negative balance, not drawn in the pie)", and the caption states "each share is of their combined total". The
  inside labels were recomputed here against the table: drawn total = 3,689,679.21 + 169,336.52 = 3,859,015.73;
  1,301,545.14 -> 33.73%, 1,175,866.16 -> 30.47%, 610,604.39 -> 15.82%, 317,527.01 -> 8.23%. All four match the
  shot. S30 (the pie drew nothing on this client) does not reproduce.
- UIC-10: 4 inside labels, all on wedges of 8.23% or more; the next wedge (163,139.24 -> 4.23%) is unlabelled; the
  legend carries 10 entries, one per drawn wedge.
- UIC-13: shot 006 shows all 11 OVER WHAT rows with no inner scroll and a "Show fewer" toggle; the shot's name records
  the "Show all 11 accounts" control the walker clicked.

| 2 | `528acdcd` FAST item 2 (UIC-09, row S29) | no source-age words before a source exists; a loading or refused panel reads its label alone | (a) the four re-goldened test files re-run by this seat at portal HEAD `528acdcd`: 18 pass, 0 fail (iv-e-69 prints `VERDICT: PERFORMANCE-FINISHED-ANSWER-OK`); (b) `tmp/ui-walk/20260928T190559Z/shots/012-cowdin-performance-Account-8774-UTMA-15-8.png`, opened and read: a real refusal face reads one plain sentence with no source-age words; (c) CI `CI - Build & Validate` completed/success; (d) `src/pages/InvestorReporting/tabs/analysis/StageDisplay.tsx:60-63` read | **PARTIAL FAIL** |

Detail for pin 2:
- **Source-age half: PASS.** Unit render (a) and the real refusal face (b) carry no "No source age yet". The walk's
  `findings.json`/`summary.md` cannot confirm an absence: the earlier walk 20260928T182319Z also counts 0 for the phrase,
  yet its shot 006 shows "Loading / No source age yet" on the page. The grade rests on (a) and (b), not on the walk's
  zero.
- **"Label alone" half: FAIL on the Analysis stage line.** `StageDisplay.tsx:62` appends the envelope's
  `publicReasonCode` in parentheses on every state. The pin's own fe-s-34 run prints it:
  `StageDisplay QUEUED business_date ABSENT -> "Loading (STATE_REPORTED)"`, and still marks the line "label alone ...
  yes", because the assertion tests only for source-age words. The UIC-09 target (brief `:45`) reads "Loading is a
  loading state with no system words". Claim class: FIXTURE. Whether the served envelope carries a
  `public_reason_code` on a loading state was not measured; the walk's `netlog.tsv` holds no bodies. The line predates
  this pin, but the pin claims "label alone" for the loading panel.

| 3 | `bfafa6c0` FAST item 3 (UIR-32/49, IV-e-71 mask half) | a strategy under an account reads the account's tail in the header's one masking style, in the drill rows, breadcrumb and Asset Category Views | (a) `tmp/ui-walk/20260928T195357Z/shots/017-thiessen-holdings-Account-9237-BROKERAGE.png` md5 `6c223ed90252bed874eed46a206ac288`, opened and read; (b) `.../026-thiessen-holdings-open-Rebalancer-strategy-Ann.png` md5 `f9f4acb5dee2bddddca5ffed7136302b`, opened and read; (c) `bun test iv-e-71.strategy-tail.test.tsx` re-run by this seat at portal HEAD `921e6808` (a descendant): 1 pass, `VERDICT: STRATEGY-TAIL-OK`, controls printed; (d) CI completed/success | **PARTIAL PASS** |
| 4 | `921e6808` FAST item 4 (UIC-23 residue, S32) | each Analysis history row names its date in client words and never a raw request id | (a) `bun test iv-e-80.history-date.test.tsx iv-e-62.request-history.test.tsx` re-run by this seat at `921e6808`: 2 pass, 0 fail, `HISTORY-DATE-OK`, `REQUEST-HISTORY-OK`; (b) CI completed/success (re-read before commit); (c) no real run exists (commit body: "No real run") | **NOT GRADED** |

| 5 | `38986671` FAST item 5 (UIC-11 residue) | no account wedge is near-white on the white Holdings panel | (a) `bun test iv-e-81 iv-e-70` re-run by this seat at portal HEAD `4ded3791` (a descendant): `ACCOUNT-PALETTE-VISIBLE-OK` (lightest `#cbd5e1` 1.485:1, control `#f5f5f5` 1.090:1) and `MODEL-VS-CLASS-COLOUR-OK` (worst internal dE00 6.7642); (b) both contrast ratios recomputed by hand from the WCAG luminance formula: 1.09:1 and 1.48:1, matching; (c) CI completed/success; (d) no real run | **NOT GRADED** (real run) |
| 6 | `4ded3791` FAST item 6 (UIC-20, IV-e-75) | a required-field message shows only after the user tries to generate, never on load | (a) `bun test iv-e-82` re-run by this seat at `4ded3791`: `REQUIRED-AFTER-ATTEMPT-OK` (load: no message, Generate enabled; after one press: the message shown, 0 submitter calls); (b) walk 20260928T190559Z shot 031, opened and read, is the before; (c) CI in progress at grading; (d) no real run after the change | **NOT GRADED** (real run) |

| 7 | `84519ede` FAST item 7 (UIC-22, IV-e-75) | Analysis shows a loading state until the holdings snapshot read answers; "none held" only after it answers | `bun test iv-e-83` re-run by this seat at portal HEAD `816eeb58`: `SNAPSHOT-LOADING-OK` (unanswered "Holdings snapshot: Loading"; answered refusal "none held -- Unavailable (SOURCE_UNAVAILABLE)"); CI success; no real run | **NOT GRADED** (real run) |
| 8 | `c77b693b` FAST item 8 (UIC-19, IV-e-75) | the default report title names the client and the variant, never one account or a comparison key | `bun test iv-e-84` re-run at `816eeb58`: `TITLE-CLIENT-VARIANT-OK` ("Coastal Ridge Trust -- Overview / Comparison / Multi-Comp" at 0/1/2 comparisons); CI success; no real run | **NOT GRADED** (real run) |
| 9 | `816eeb58` FAST item 9 (UIC-18, IV-e-75) | a picked variant card is visibly selected; the form asks for what that variant needs, with no system sentence | `bun test iv-e-85` re-run at `816eeb58`: `VARIANT-ASKS-OK` (3 cards, 1 ringed, 1 "Selected"; five asks in client words, e.g. "Add at least two Opal models to compare against."); CI success; no real run | **NOT GRADED** (real run) |

Detail for pins 7-9 (from the tests' own printed text; outside each pin's claim):
- Pin 7's refused arm prints "none held -- Unavailable (SOURCE_UNAVAILABLE)": the N1 raw-code class again, on the
  Holdings-snapshot line. Its held control prints "as of 2026-09-09 ReadyNeeds correction: ...": a raw ISO date, and
  "Ready" run into "Needs" in the test's text read (the DOM may separate them; a render is the check).

Detail for pins 5 and 6:
- Pin 5 claims the near-white entry only. The rest of UIC-11 (brief `:48`, "a narrow grey ramp; neighbouring slices
  cannot be told apart") is not claimed. After the pin, `ACCOUNT_PALETTE` (`palette.ts:59-73`) is still 13 neutrals
  (slate, stone, zinc, neutral). Its measured separation is dE00 >= 6.76 per pair; whether 11 adjacent grey wedges
  read "distinguishable at a glance" is a judgment on a rendered 11-account pie, which is owed. The lightest entry
  (1.485:1) meets the pin's own 1.4:1 floor, not the 3:1 floor WCAG 2.1 SC 1.4.11 sets for graphical objects. The
  legend names each slice, so colour is not the only carrier.
- Pin 6: shot 031 has no client selected (search box empty), so the "Select a client in the header first." it removes
  on load was a true statement, not a masked selection defect. The body still prints "Client: select a client above"
  and "Holdings snapshot: none held -- Loading" at rest; neither is in the pin's claim.

Detail for pin 3:
- **Drill half: PASS on a real run.** Shot 017 (Thiessen, Anna; account ****9237 / BROKERAGE) shows the breadcrumb
  "All holdings ****9237 / BROKERAGE / Rebalancer strategy: Anna ****9237": the owning account's tail, in the header's
  "****" form. Round 8's grade (ADJUDICATION_v6.md:29) read "Anna *9238" there.
- **Asset Category Views half: NOT GRADED.** The same walk ran before the adapter change. Its ALL CATEGORIES card in
  shot 017 still reads "Rebalancer strategy: Anna *9238" (the wrong tail, the old style), and the modal in shot 026
  reads "Anna *9237". The walk was then killed for low system memory and not re-run, so the post-change face rests on
  the unit arm (c) alone. A real run that opens the ALL CATEGORIES card and its modal is owed.
- The one-slice ALL CATEGORIES pie in shot 017 is IV-e-71's other half, parked outside the lease surface by the pin's
  own commit; not graded here.

Detail for pin 4:
- Unit evidence only. The iv-e-80 fixture gives both rows the same accepted_at ("requested January 15th, 2027, 3:00a
  ET" twice), so it cannot show that each row carries its own date. A real run over a client with two or more
  requests on different dates is owed.
- Outside the claim: the iv-e-62 run prints a history row "Failed -- SOURCE_UNAVAILABLE", a raw code on a row's face
  (the N1 class). Carried with N1.

**Why this seat did not walk pins 3 and 4 itself (20:4xZ):** port 5174 was not listening, 7.0 GB of 31.7 GB was free,
and the previous walk died to the harness's low-memory kill. A walk arms an admin-role account that stays active if
the walk dies. Nothing waits on a FAST grade, so the real runs go to the next walk of this surface.

## Regrades on a real run: walk 20260928T215633Z (22:0xZ)

Client ANTHONY DALE REID (49 Financial, 3 accounts), localhost:5174. The dev server started 21:46:49Z
(`tmp/ui-walk/devserver-20260928T214648Z.log`); portal HEAD from 21:51:01Z to 22:03:24Z was `b0acdee2` (reflog), so the
walk's build holds pins 1-10 (vite serves the working tree; uncommitted edits, if any, are not excluded). Shots opened and
read: `005-identity-...-expanded.png` md5 `065b6c286486ffa5537b0cbb7348cb79`, `011-...-holdings.png`
`bf22a59927104fab7c82b593b9c756c1`, `015-...-analysis-expanded.png` `aceb3c210802a9fdde2f012bc4740542`.

| pin | was | now | on what |
|---|---|---|---|
| 2 `528acdcd` source-age half | PASS (unit + refusal face) | PASS, also on a real loading face | shot 005: the Performance body reads "Loading" alone |
| 5 `38986671` | NOT GRADED | **PASS on its claim** | shot 011: three wedges, none near-white (slate-300, stone-300, zinc-400). UIC-11's glance test is still open: the two pale wedges read close, and all three wedges, legend entries and rows read "****9079 / IRA" (UIR-26) |
| 6 `4ded3791` | NOT GRADED | **PASS at rest**; the after-press arm is not exercised | shot 015: Generate enabled, no red refusal on load; the recipient line is grey helper text, not an error |
| 9 `816eeb58` | NOT GRADED | **PASS on the visible pick**; the ask arms are not exercised (Overview asks nothing) | shot 015: the Overview card ringed and reading "SELECTED" |
| 10 `11c3fa4a` (UIC-17) | not handed before this walk | **PASS** | shot 005: no "SCOPE AS OF" field (was "unknown"); "DIRECTORY AS OF September 24th, 2026" in the page's date format |
| 7 `84519ede`, 8 `c77b693b` | NOT GRADED | still NOT GRADED | shot 015 has no client selected (search box empty), so "Holdings snapshot: Loading" and the title "the selected client -- Overview" do not exercise a read that answers or a client name |

Observation from shot 015: with no client selected, the snapshot line reads "Holdings snapshot: Loading". If no read is
in flight without a client, that is a loading word for a state that is not loading; one shot cannot tell. A render
with a client selected (pins 7, 8) settles both.

## Regrades on a real run: walk 20260928T220437Z (22:5xZ)

Same client, `--deep` (period presets and variant cards pressed). Build: portal `8c6792df` (HEAD 22:03:24Z to 22:22:31Z;
the walk ran 22:04:37Z for 4.6 min), so pins 1-12. Shots opened and read: 011 md5 `87fe1638ba0d6e10661becaf6f9de57d`,
028 `12230fee9d6b0d7ee70f86e2587a2ad6`, 030 `c738f75091129f8a396dc2dc535c8820`, 034
`2fce3883719629e200362fed7d2e32f1`, 037 `0adb4cf3b4fb6c0d72baecef7ab9e8a6`.

| pin | now | on what |
|---|---|---|
| 12 `8c6792df` (UIR-45) | **PASS on its claim** | shot 011: "Requested January 1st, 2026 to September 22nd, 2026 / Answered April 15th, 2026 to September 22nd, 2026". Outside the claim, the same tab still prints raw ISO: "Business date 2026-09-22", "SERIES START 2026-04-15", the axis and the daily-series dates; and raw codes under Report details ("PERFORMANCE_PARTIAL", "TIME_WEIGHTED") |
| 9 `816eeb58` | **PASS**, ask arms now exercised | shot 034: Comparison SELECTED, "Add one Opal model to compare against."; shot 037: Multi-Comp SELECTED, "Add at least two Opal models to compare against." Outside the claim: the summary line stays "Variant Overview (0 comparisons)" (row S38) |
| 8 `c77b693b` | **PASS on the variant half**; the client half not exercised | shots 034/037: title "the selected client -- Comparison" / "-- Multi-Comp"; no client was selected (row S37) |
| 7 `84519ede` | still NOT GRADED | no client on the Analysis tab (row S37) |

Rows filed from this walk (commit below): **DSGN_IRPTV1-S37** (a Holdings dropdown pick resets the page's client and
tab; it is why every walk's Analysis shots are clientless); **DSGN_IRPTV1-S38** (stale "Variant Overview" summary);
**IRPT_BCKEND-S186** (a funded 49F account, ****9079 / IRA with $99,253.73 held, served -100.00% YTD; not one of row
S184's two near-misses; owner `2.0.0_SA_COO~P`).

## Pins 13 and 14 (23:1xZ; no walk after them)

| pin | claim | evidence | grade |
|---|---|---|---|
| 13 `2febba0b` (IV-e-76, UIR-04/13/30, W35-S1) | firm display names come from the registry-generated view, never a title-case guess | `bun test iv-e-89` re-run by this seat at portal HEAD `8d12987e`: `FIRM-NAMES-REGISTRY-OK`; CI success; no real run | **NOT GRADED** (real run) |
| 14 `8d12987e` (UIC-03, CTO ruling 102453) | Report details states method and source in client words; no code, hash or producer name on the face | `bun test iv-e-90` re-run at `8d12987e`: `METHOD-SOURCE-WORDS-OK`; CI success; no real run. The before is walk 20260928T220437Z shot 011 ("PERFORMANCE_PARTIAL", "TIME_WEIGHTED", revision hashes under Report details) | **NOT GRADED** (real run) |

Pin 14 applies ruling 102453 to the Performance face only. At `8d12987e` the three Analysis surfaces of rows S34/S36
still print the code (re-run: "Loading (STATE_REPORTED)", "(SOURCE_UNAVAILABLE)", "Failed -- SOURCE_UNAVAILABLE"),
now against that ruling too. Filed as row DSGN_IRPTV1-S39.

| 15 `d516158f` (AD-03, Andrew-direct via CTO 102455) | Holdings carries no Allocation panel and no Report details / Unique accounts / source-dates card | `bun test iv-e-91` re-run at portal HEAD `d516158f`: `HOLDINGS-PANELS-REMOVED-OK` (control: the drill tree still present); CI success; no real run | **NOT GRADED** (real run) |

Pin 15 changes the Holdings tab that row S37's reset ran through. Whether the dropdown whose pick cleared the client
survives this pin is not read here; the next walk re-tests S37.

## Regrades on a real run: walk 20260929T000244Z (00:1xZ)

Same client. Portal HEAD `1f6612c8` (pins 1-16), but the tree carried UNCOMMITTED product edits to
`tabs/holdings/HoldingsTab.tsx` and `tabs/holdings/DrillTree.tsx` (item 17, parked unlanded; `git -C portal status`
read after the walk). So the Holdings shots are not a landed build, and pins 15-16 are not graded on them. Identity,
Performance and Analysis do not import those two files. Shots opened and read: 007 md5
`fa44f77fb890ef0e3dd1f26dced5078c` (a crop of Report details read at full size), 010 `9820db3b70bd588b1af3fe592998afe7`,
023 `64534b8461cb48c2d05b329e2ab413db`.

| pin | now | on what |
|---|---|---|
| 14 `8d12987e` (UIC-03) | **PASS** | shot 007: Report details reads "Time-weighted, net of fees, cumulative. Values in USD." and "Source: Opal's performance engine, as of September 22nd, 2026."; no code, hash or producer name (the before, walk 220437Z shot 011, showed "PERFORMANCE_PARTIAL", "TIME_WEIGHTED" and revision hashes). Outside the claim: "Business date 2026-09-22" is still raw ISO beside "Partial" |
| 7 `84519ede` (UIC-22) | **PASS on the answered arm** | shot 023, client selected: "Holdings snapshot: as of 2026-09-22 Ready", no "none held". The loading arm is transient and was not caught. The date is raw ISO and "Ready" is a state word |
| 8 `c77b693b` (UIC-19) | **PASS** | shot 023: title "ANTHONY DALE REID -- Overview": the client and the variant, not an account |
| 13 `2febba0b` | NOT GRADED (not discriminating) | shot 023 reads "49 Financial (Client)", as the walks before the pin did; this client's firm does not tell a registry name from the old guess |

- **Row S37 did not reproduce.** After the same select-1 picks ("All", "Opal Long Term", "Opal Ultra Long Term") and the
  select-2 picks, the Analysis tab still holds the client (shot 023). This build carried the unlanded Holdings edits, so
  it does not show that the LANDED build is fixed. S37 stays open for L9 with this negative.
- **Row IRPT_BCKEND-S186 is still live** at 00:0xZ: shot 010 shows ****9079 / IRA ($99,253.73) at "-100.00%" YTD,
  series start 2026-04-15, end 2026-09-22 -100.00%. That is after `~P`'s re-verified pr-191/IB-pr-194 drain
  (`ae8da14d12`). The source still names "opal-gips-engine".

## Pins 17-22 (2026-09-29 04:5xZ; no signed-in walk after 00:12Z)

| pin | claim | evidence | grade |
|---|---|---|---|
| 17 `84854311` (AD-01 remainder, W17-S1) | Holdings is two components; the All Categories card is the drill | commit body: "No real run: walker runs stay paused"; CI success | **NOT GRADED** (real run) |
| 18 `5ff990dc` | Holdings map and table in Positioning's classes, order and colours | commit body: "No real run"; iv-e-94 named; CI success | **NOT GRADED** (real run) |
| 19 `ee949234` (CTO 102510) | one holdings tree map for Positioning and IR, extracted with no visible change | `deliverables/2.0.0_SA_COO~D/item19/README.md` and PNGs read: `before-positioning.png` = `after-positioning.png` byte for byte (md5 `ced60ba2...`), and the control with one holding removed differs (md5 `fc01e7d0...`, bbox (111,670,1377,2037)), so the check can see a change; CI success | **PASS** (refactor identity). Claim class DRIVER-FIXTURE: `ui-smoke.mjs` over the served `opal-data-portal-v2` JSON, not a signed-in walk. IR's live map is not covered (the README says so) |
| 20a `b9d49989` | one holdings breakdown table, extracted | same method: Positioning Characteristics after = before (md5 `ced60ba2...`), Performance view after20 = before20 (md5 `0801c585...`); CI success | **PASS** (refactor identity), same claim class |
| 20b `d6f740cc` | IR's Securities table is Positioning's breakdown table: light ground, navy ink, never sums | `item19/ir-holdings-1440.png` (md5 `5800639d...`), opened and read: the Securities table sits on a white panel in navy ink; the class cells carry colour; no total row; CI success | **PASS on its claim**. Claim class DRIVER-FIXTURE (the Cottonwood Trust $200,000 two-holding fixture) |
| `50eb1d56` | PerformanceReport provider OPAL_HOLDINGS reaches the page (wire regenerated) | IVE17-AC2 REGENERATED-OK per the commit; CI success; no render | NOT GRADED (no render; a contract regeneration) |
| 22 `cabe0d5c` | Analysis is a three-page flow | commit body cites a real render through the IVE20 census driver, but no image is kept; CI success | **NOT GRADED** (no artifact this seat can read) |

| `e5e96606` (W21 part P K8) | the export receipt poll keeps going through a data-less RUNNING read instead of throwing and going idle | `bun test iv-e-95` re-run by this seat: `RECEIPT-RUNNING-DATALESS-OK` (3 reads, only READY reported; control RUNNING-only ends null at the bound, no throw), over the SERVED W21 receipt body (`exr_f3a8ba9c...`, record `w21-part-p-walk-20260929.md`); the commit reports the same test crashing on the old `submit.ts`; CI success | **PASS** (claim class SERVED-BODY REPLAY; the live page not re-walked) |

| 24 `6c163889` (AD-01; ~M 102600) | the served L0 CATEGORY node reaches the page as its own kind (was drawn as a security); source_vendor_keys carried | `bun test iv-e-96` re-run by this seat: `CATEGORY-NODES-OK` through the real adapter over the Cottonwood smoke wire (per the commit: table and map list only the two securities, the card reads Models 120000 / Client 80000 from served amounts, vendor keys served-or-null); CI success; no render | **NOT GRADED** (real run). Unit evidence holds; claim class FIXTURE WIRE |

| 25 `d960e590` (AD-08) | the analysis cards open the canonical modal; Comparison and Multi-Comp take an Opal model or an ETF | `bun test iv-e-97` re-run by this seat: `VARIANT-MODAL-OK`; CI success; the commit cites a real render on 5174 ("screenshot local") that is not kept where this seat can read it | **NOT GRADED** (no readable real-run artifact) |

| 26 `037657da` (AD-07) | the prospect upload: an Upload button, a modal with the reader's rules, and a template the reader accepts unchanged | `bun test iv-e-98` re-run by this seat: `PROSPECT-UPLOAD-OK` (template bytes pinned to the reader-accepted string); CI success; no render named | **NOT GRADED** (real run) |

Observations from `ir-holdings-1440.png`, outside each pin's claim:
- **O-a (a ruling conflict, for 1.0.0_SA_CTO):** the Securities Map and Securities footers read "Source:
  investor_reporting/holdings_publisher." (`slices.ts:344` prints the served `provenance.sourceCoordinate` under IV-e-63
  / R10 101758, "the source line names the actual source"). Pin 14 moved the Performance face off internal producer
  names under ruling 102453 (UIC-03). The two rulings disagree on whether a producer path may be the visible source.
  It is not a regression from pins 19-20; the 09-24 grade read "Opal Capital Analysis" because that snapshot's nodes
  carried no coordinate.
- **O-b:** the page carries five full-width navy bands (IDENTITY, the ALL CATEGORIES card, and the SECURITIES MAP and
  SECURITIES header/footer bands) against C3's one band per page. The ALL CATEGORIES card is navy on Andrew's call
  1(a); the others are the known band-valued Panel variants (portal CLAUDE.md "Known divergence").

## Next items

- **N1 (pin 2's FAIL):** the Analysis stage line prints the raw public reason code beside "Loading"
  (`StageDisplay.tsx:62`). The fe-s-34 assertion that passes it tests for source-age words only. Row S34 carries it.
  Row S35 (`2.0.0_SA_COO~Y`, @810a66317f) measured the served side by source read: every live loading state carries a
  reason (`ANALYSIS_QUEUED` ... `ANALYSIS_CERTIFYING`, `owned_status.py:12-24`), and `STATE_REPORTED` exists only in
  portal fixtures. N1 is therefore live on every Analysis loading face, not only in the fixture (claim class
  SOURCE-READ; no live body read).
- **N2 (owed real runs):** the Asset Category Views card and modal after `bfafa6c0`; the Analysis history over a
  client with two dated requests after `921e6808`; the 11-account Holdings pie after `38986671` (a glance judgment on
  the grey ramp); the Analysis tab at rest and after one Generate press after `4ded3791`; the Analysis snapshot line
  while loading, the default title, and a picked variant with its ask after `84519ede`, `c77b693b`, `816eeb58`. One
  walk of Cowdin (11 accounts) plus Thiessen, with the Analysis tab pressed through, covers all seven. After walk
  20260928T215633Z, still owed: the Asset Category Views card and modal (pin 3); two dated history rows (pin 4); an
  11-account pie (UIC-11 glance); Generate pressed once (pin 6); the Analysis tab WITH a client selected (pins 7, 8).
  Pin 9's ask arms were exercised by walk 20260928T220437Z. A walk that goes to Analysis BEFORE touching the Holdings
  dropdowns (row S37) gets pins 7 and 8.
- **N3 (raw code, the N1 class, second surface):** the Holdings-snapshot line on Analysis prints "(SOURCE_UNAVAILABLE)"
  on a refusal (pin 7's test), as the history row prints "Failed -- SOURCE_UNAVAILABLE" (pin 4's). N1's fix should
  cover every place a reason code reaches the face, not only `StageDisplay.tsx:62`.

## Observations (not grades; each is outside the pin's claim)

Owners below are read from the CRO brief `docs/briefs/irpt-ui-remaining-brief-20260928.md` @c931298153.
- **O1:** every account, legend entry and OVER WHAT row reads the same "****8774 / UTMA", so the legend "names every
  slice" without telling them apart (walk UIW-20260928T182319Z-010, x11). Owned: brief UIR-26 (`:61`),
  `2.0.0_SA_COO~M`.
- **O2:** raw token "HOLDINGS_READY" on the Holdings step (walk UIW-...-008). Owned: brief UIW-0928-04 (`:60`),
  `2.0.0_SA_COO~D`.
- **O3:** shot 006 shows the Performance body at "Loading / No source age yet". Owned: brief UIC-09 (`:45`),
  `2.0.0_SA_COO~D`.
- **O4:** the COHORT (NOT ASSERTED) line "supervision: withheld, advisory: withheld" (walk UIW-...-009,
  `unconnected-field`). No row in the brief names it (read: 0 hits for "withheld"/"cohort"). Carried to this seat's
  next DSGN_IRPTV1 slug, FAST section.

-- 3.0.0_SA_CVO

## Grades, 2026-09-30 ~14:4xZ -- AF-1, AF-2, item 36, item 37 (handed over by `2.0.0_SA_COO~D`, message 103259)

**Lease:** `org/mcp/drive-mode.log` last ARM 2026-09-30T01:40:50Z (STATUS.md @HEAD: "presence-extended since"); the DEV
push of 1d7b8feb at 14:19Z passed the never-rules gate, which admits a DEV push from a live lease's seat only. **Pins:**
all four are ancestors of origin DEV `1d7b8feb3172` (ls-remote and `merge-base --is-ancestor` by this seat, 14:2xZ).
**This seat's own runs at portal HEAD `1d7b8feb`:** `bun test` over the nine pinned files -- 9 of 9 pass
(TREEMAP-VARIOUS-OK, REQUEST-LIST-OK, SECURITIES-FOLD-OK, SECURITIES-MAP-WALK-OK, IVE115-OK, GENERATE-JOURNEY-OK,
DRILL-BASES-OK, SECURITIES-MAP-OK, MAP-CHIPS-OK; 2.62 s); `eslint` on the two item-37 files rc=0; the portal tree's
dirty count was 15 before and after the run (no wire regeneration from these nine).

| # | pin (portal DEV) | claim | evidence read | grade |
|---|---|---|---|---|
| AF-1 | `5c7eead8` (Andrew-direct design feedback ~01:4xZ) | pie ordinal scale with neighbour contrast; the residual Client row grey; the map shows the view's ten largest securities with multi-select chips; the account picker unmounted; Name without the ticker prefix | unit: iv-e-42, iv-e-44, iv-e-61, iv-e-105 green at HEAD (this seat's run); real run: Andrew smoked 5174 on this build and answered with feedback #2 (the AF-2 record), so the build reached its judge; no screenshot or walk artifact exists for this seat to read | PASS on the unit claims; the real-run grade is Andrew's smoke (his ~05:0xZ feedback is the record); NOT GRADED by this seat on an artifact |
| AF-2 | `44fd5f42` (Andrew smoke feedback ~05:0xZ) | one row per security per Sleeve/Account view (Andrew's word as the F7-AC4 exception); tooltip name only, 'Other Securities' tile, 'Client' chip; class order Cash first; account dialog sleeves by value, collapsible | unit: iv-e-113, iv-e-114, iv-e-115, iv-e-105, iv-e-44, iv-e-61 green at HEAD (this seat's run); the class order in `assetClass.ts` read at HEAD (IV-e-115 comment and `CLASS_FOR_SERVED`); no real-run artifact: STATUS lists "Re-smoke DEV a20b5a60" as open at Andrew | PASS on the unit claims; NOT GRADED on a real run (the re-smoke is Andrew's, open) |
| 36 | `a20b5a60` (walk-2 W2-07) | after Generate the ISSUED request opens in the page's own dialog (status in words, Technical details behind one control, report sections when READY) and "Your analysis requests" re-lists from the first page | unit: iv-e-116 GENERATE-JOURNEY-OK at HEAD (this seat's run). Real run, fixture plane (the walk-2 write guard), read by this seat: `deliverables/2.0.0_SA_COO~D/item36/w2-07.fast-run.png` shows the dialog "Your analysis request / Requested September 30th, 2026, 9:52a ET / Job status: Ready / Business date: 2026-09-29 / Check status / Report sections / 2. annualized_return SUPPORTED 0.0712 percent, As of 2026-08-31"; `w2-07.fast-run.netlog.tsv` (276 rows): `POST .../investor-reporting/analysis?account_set_id=sel_bdf98e1d...` exactly 1, `GET .../analysis/requests` 4, POST rows 9 in all (2 auth/refresh, 2 directory/resolve, 3 selections, 1 analytics/ingest, 1 analysis) | PASS on the fixture-plane real run: one POST, the dialog opened on the issued id, the list re-read after the press. The live press stays Andrew's acceptance (STATUS "Limits") |
| 37 | `1d7b8feb` (lint hygiene in surface) | iv-e-106's non-ASCII check is a code-point count; iv-e-116's two wiring regexes use `{2}` / `{4}`; the two remaining repo lint errors are `HeaderBrief.tsx:47-48`, out of surface (row S41) | `eslint` on both files rc=0 (this seat); both tests green; byte read of `src/pages/SecurityAnalysis/components/HeaderBrief.tsx`: line 47 `/^bloomberg\x08/i` and line 48 `/^D-1\x08/` each carry exactly one 0x08 byte; the file is outside the lease surface | PASS; S41's attribution holds on the byte read |

## Observations (not grades; each is outside the pin's claim)

- **O-36a:** the dialog in the item-36 shot carries two "Technical details" disclosure controls, one under Job status
  and one under Report sections. The W2-06 wording is "Technical details behind one control"; whether that means one
  per block or one per dialog is `2.0.0_SA_COO~D`'s to state in the next STATUS.
- **O-36b:** the fixture's report section reads "As of 2026-08-31" beside "Business date: 2026-09-29". A fixture
  artifact, not graded; on Andrew's live press the section as-of should be read against the business date.
- **O-36c:** nine GET rows in the netlog answered 401 (advisor-intelligence `platinum/firm/*.json?firm=bd` and
  `portal-content`) during the page load. They are outside the Analysis surface; if the walker account lacks that
  scope the refusal is the expected one. Not graded here.

## Not verified by this seat

The 920/27/18 suite count on a20b5a60, DEV CI run 36725618787's ESLint step, the live 5174 process, and the lease's
presence-extension record after the reboot. Row S41's fix is DSGN_AMGTV1's and is graded at that project's drain.

-- 3.0.0_SA_CVO

## Grades, 2026-09-30 ~17:0xZ -- items 38, 39, 40, 41 (handed over by `2.0.0_SA_COO~D`, message 103320)

**Pins:** all four are ancestors of origin DEV `e67a03f484` (fetched; `merge-base --is-ancestor` yes for each; portal
HEAD = origin DEV). **This seat's own runs at portal HEAD `e67a03f4`:** `bun test` over the ten pinned files -- 10 of 10
pass (FOOTER-SOURCE-WORDS-OK, NAMED-MISSING-DAY-OK, FOCUS-REFUSAL-EXPORT-OK, PER-ACCOUNT-PERF-OK, PRESET-ASOF-OK,
PICKER-REFUSAL-OK, ACCOUNT-YTD-OK, FACE-BATCH-OK, PICKER-ENTRIES-OK, DATES-SOURCES-OK; 1.26 s); dirty count 15 before
and after. **Claim class of the real runs:** fixture plane on 5174 (the drivers fulfil the IR routes from
`fixtures/smoke/dsgn-irptv1-cottonwood.json`; nothing reaches the live backend), each PNG read by this seat.

| # | pin (portal DEV) | claim | evidence read | grade |
|---|---|---|---|---|
| 38 | `775c4261` (W2-19, absorbs UIC-14) | every Holdings footer reads words, never a producer coordinate; card, map and table are one string | unit iv-e-117, iv-e-45, iv-e-63 green at HEAD (this seat's run). Shot `item38/w2-19.fast-run.png`: three footers on the Holdings tab (card, SECURITIES MAP, SECURITIES) all read "September 23rd, 2026, 5:00p ET \| Source: Opal Capital Analysis." -- one distinct string, no `module.function`, no `build_` | PASS on the fixture-plane real run |
| 39 | `1bcda74c` (W2-19b) | the Performance footer reads source words, never `lineage.sourceCoordinate` | unit iv-e-117 ARM (d) and iv-e-63 green at HEAD. Shot `item39/w2-19b.performance.fast-run.png`: the PERFORMANCE panel footer reads "Source: Opal Capital Analysis."; no coordinate and no function name anywhere on the face. The commit's second line ("Source: Black Diamond, as of September 23rd, 2026.") is not visible in the shot read; the driver's own verdict rule for the Performance tab requires exactly one distinct source string, which the shot satisfies | PASS on the fixture-plane real run |
| 40 | `b1e18782` (W2-01 front residue) | a DEPENDENCY_UNAVAILABLE refusal with a business date names the missing upstream day; the picker never stays "pending" for good | unit iv-e-118 plus iv-e-34/39/40/58 green at HEAD. Shot `item40/w2-01.fast-run.png`: the refusal panel reads "... The latest day that source has answered for this account is September 22nd, 2026; the days after it are the ones missing." and the picker option reads "not supplied -- $200,000.00 -- YTD unavailable" (item 39's shot, taken before this pin, reads "YTD pending" on the same option: the before state) | PASS on the fixture-plane real run |
| 41 | `e266a14a` (W2-19 words) | the registry vendor view lands as builder output and is `holdingsFooterSource`'s default, so a keyed snapshot names its sources in words | `header/vendorDisplayNames.generated.ts` sha256 `4dd7a2728592d2e4` (the commit's `4dd7a272`), 28 entries for 23 vendors (key and long form), header marked `registry@1c951921d4940c85`; `systems.json` at HEAD holds 25 VENDOR rows of which 23 carry `display_name`. iv-e-117 green. Shot `item41/w2-19-words.fast-run.png`: card, map and table footers all read "Source: Black Diamond." -- the driver injected `source_vendor_keys` into the holdings fixture (driver line 39-41, argv[5]), which is how the words path was exercised; the un-injected face reads the fallback, as the commit says | PASS on the fixture-plane real run of the words path |

## Finding (carried to NFRA_TRNSPT's channel as row NFRA_TRNSPT-S4)

`python lib/opal_naming.py generate --target .../vendorDisplayNames.generated.ts` at HEAD is REFUSED: `validate`
reports 2 refusals, `systems.json[48].display_name` (`outlook`) and `[49].display_name` (`sharepoint`), both VENDOR
rows added by `0.9.0_WK_NFRA_TRNSPT~3` @8e9ed1b539 (drained by `2.0.0_SA_COO~T` @fed423d013, 12:58Z) after the CRO's
23 `display_name` rows @cd2ffcca99 (12:10Z). So the committed vendor view cannot be regenerated at HEAD, its mark
predates the two rows, and every other `generate` target refuses with it. Item 41's pin is not at fault; the disarm
is two `display_name` values on the NFRA_TRNSPT rows.

## Observations (not grades)

- **O-39a:** as noted in the table, the shot shows one source line on the Performance face where the commit text
  describes two. If the source-age line renders only with a served source age, the fixture is the reason.
- **O-41a:** the two new VENDOR keys `outlook` and `sharepoint` are absent from the generated view, so a snapshot
  keyed on either would read the fallback until regeneration.

-- 3.0.0_SA_CVO
