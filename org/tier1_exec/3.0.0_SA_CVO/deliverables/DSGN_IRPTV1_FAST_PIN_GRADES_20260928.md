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

## Grades, 2026-10-01 ~06:2xZ -- items 42 to 54 (asked by `1.0.0_SA_CTO` 103508; DSGN_IRPTV1 and IRPT_DASHBD workstream F)

**Leases:** FAST `DSGN_IRPTV1` until 12:31:43Z and FAST `IRPT_DASHBD~D` until 12:32:19Z (`drive-mode.py status`, 05:51Z).
**Pins:** all twelve (`20f95f79`, `ffc3c346`, `c98fa91e`, `c63553cf`, `57cf660e`, `63fb6318`, `970d5c75`, `e9a37ac1`,
`7c354824`, `772dcdd8`, `a75e6a29`, `54bd4224`) are ancestors of portal HEAD `54bd4224`, which equals origin DEV
(ls-remote by this seat). **CI:** runs 36822129829 (`54bd4224`) and 36821411702 (`a75e6a29`) read `completed success`
(`gh run view`). **This seat's own run at portal HEAD:** `bun test` over twelve pinned files, 12 of 12 pass (iv-e-113,
117, 119, 120, 121, 122, 123, 124, 125, 126, 127, 47; 1.37 s); portal dirty count 15 before and after. **Claim class of
every real run below:** fixture plane on 5174 or a synthetic series; nothing reached the live backend. Each PNG named
was read by this seat.

| # | pin (portal DEV) | project | evidence read | grade |
|---|---|---|---|---|
| 42 | `20f95f79` + `ffc3c346` (W2-22 remainder, a model becomes the tab's scope) | DSGN_IRPTV1 | unit iv-e-119 MODEL-SCOPE-OK. Shot `item42/w2-22.fast-run.png`: the scope line "Showing only Core Growth Model -- back to all models" and the Sleeve select reading "Core Growth Model" are present; the map still draws three tiles (the model at 100.0% beside two "not supplied" tiles at 60.0% and 40.0%) and the table reads "No securities match these filters." The seat's own driver verdict is FAIL and STATUS says so (the injected MODEL node is not adapted as a model) | PASS on the unit claim; **NOT_EVALUATED on a real run: the one artifact shows a scoped tab with an unscoped map and an empty table** |
| 43 | none (probe, W2-16) | DSGN_IRPTV1 | `item43/measurements.json`: five widths (1440, 1180, 1024, 820, 390), `scrollWidth` equal to the viewport and `nextClipped: false` at the four read in full | PASS as a probe: the clip is not reproduced |
| 45 | `c98fa91e` (vendor view regenerated) | DSGN_IRPTV1 | iv-e-117 green; `python lib/opal_naming.py validate` reads OK (51 system rows, 0 refusals, registry@f56fa0ff8d7f4235). The registry mark has moved since the pin's `31046c489fdb4a1c`; whether the committed view still equals a fresh builder run was not re-generated | PASS; row NFRA_TRNSPT-S4's refusal is gone |
| 46 | `c63553cf` (FCASH joins the Cash row) | DSGN_IRPTV1 | unit iv-e-113 SECURITIES-FOLD-OK. Shot `item46/fcash.fast-run.png`: the Securities table shows ONE Cash row, 6.00%, $12,000.00; the map draws CASH 2.5% and FCASH 3.5% as two tiles, as STATUS says | PASS on the fixture-plane real run |
| 47 | `57cf660e` (coverage words) | IRPT_DASHBD F | unit iv-e-120: parity failures 0, a planted contract member fails parity | PASS on a test run; no page mounts it |
| 48 | `63fb6318` (window math) | IRPT_DASHBD F | unit iv-e-121 WINDOW-MATH-OK | PASS on a test run; no page mounts it |
| 49 | `970d5c75` (search ranks held rows) | DSGN_IRPTV1 | unit iv-e-122 and iv-e-47 green; no real-run artifact was found under the lane's deliverables (no `item49` folder; STATUS says "screenshot read" without a path) | PASS on the unit claim; NOT_EVALUATED on a real run |
| 50 | `e9a37ac1` (W2-06 words) | DSGN_IRPTV1 | unit iv-e-123 CORRECTION-WORDS-OK. Shot `item50/w2-06-words.fast-run.png`: "Job status: Needs correction" then "This request could not be resolved while other work was in flight. Nothing is wrong with your file; submit the request again." outside Technical details; no code or id on the face | PASS on the fixture-plane real run; the served CORRECT action is unread (hop 10's walk) |
| 51 | `7c354824` (SERIES contract read) | IRPT_DASHBD F | unit iv-e-124: parity failures 0, a planted contract key fails parity | PASS on a test run; no page mounts it |
| 52 | `772dcdd8` (dashboard Performance chart) | IRPT_DASHBD F | unit iv-e-125 DASHBOARD-PERFORMANCE-OK. Shot `item52/dashboard-performance.design-look.png`, headed "DESIGN LOOK ONLY -- synthetic series": the title "Total return, before advisory fees", five presets and two date fields, a brush, the headline 13.80% with three coverage sentences, a visible gap in the curve, and the refusal panel with its sentence | PASS as a design look; NOT_EVALUATED for FWD-1 (no served file, no page mounts it), as STATUS says |
| 53 | `a75e6a29` (W2-15 class totals) | DSGN_IRPTV1 | unit iv-e-126 CLASS-TOTALS-OK. Shot `item53/class-totals.fast-run.png`: "Held positions by asset class", Cash 1.00%, Fixed Income 2.70%, Equity 6.00%, then under a rule "No position detail 90.30% $180,600.00" and both sentences; the four lines sum to 100.00% and $200,000.00 | PASS on the fixture-plane real run; the served blocks are unread (the route does not serve them yet) |
| 54 | `54bd4224` (holdings NOT_READY in words) | DSGN_IRPTV1 | unit iv-e-127 HOLDINGS-NOT-READY-OK. Shot `item54/holdings-not-ready.fast-run.png`: "This account's holdings have not arrived yet." and one detail line on a white panel, a closed Details disclosure, no code and no danger icon | PASS on the fixture-plane real run. The "Back to all accounts" half of the commit is not in the shot: not graded |

## Observations (not grades)

- **O-42a, the one item with no passing real run rides the PROD promote.** STATUS "Open at Andrew" routes a promote of
  DEV `c63553cf`, which contains `20f95f79`. Item 42's only artifact shows the scope line with an empty table. One
  real run on a snapshot that carries a real MODEL node (a served 49 Financial selection has them) would settle it
  before the promote; the choice is `1.0.0_SA_CTO`'s and `2.0.0_SA_COO~D`'s.
- **O-53a.** On the item-53 fixture the block and the table describe different money: the table lists two positions
  worth 60.00% and 40.00% of the total, while the block above it says 90.30% has no position detail. A fixture
  artifact (the blocks were injected); on served data the two must be read together at `2.0.0_SA_COO~M`'s after-read.
- **O-46a.** On the item-46 fixture the card totals $212,000.00 while the identity strip reads $200,000.00, and the
  table's weights sum to 106.00%. A fixture artifact (cash added over the custody total), but it shows the table
  weights and the card use different denominators whenever positions and custody disagree. `2.0.0_SA_COO~M`'s census
  found that case in 3,891 of 7,565 accounts at 49 Financial when target-basis nodes are counted.
- **O-52a.** The item-52 look prints "193 trading days measured" for 2026-01-01 to 2026-09-30. Synthetic input; on
  the served file the count should be read against the trading calendar (`lib/trading_calendar.py`).

## Not verified by this seat

The live backend on any of these faces; the 5174 process; the item-50 and item-54 control shots; the wire
regeneration; DEV CI for the ten earlier pins (two runs read).

-- 3.0.0_SA_CVO

## Grades, 2026-10-01 ~07:3xZ -- item 55 (portal `486b07fd`), and item 42 re-graded on a real run

**Why:** CTO 103537 ruled one real run of item 42 before the PROD promote. `2.0.0_SA_COO~D` ran it signed in on the
local build against the real backend (`deliverables/2.0.0_SA_COO~D/REAL_RUNS_20261001.md` section 1, five walks):
item 42 FAILED at `20f95f79` on a client-directed holding row and is fixed at `486b07fd`. **Pin:** `486b07fd` is
portal HEAD and origin DEV (ls-remote by this seat). **This seat's run at HEAD:** `bun test` iv-e-119, iv-e-113,
iv-e-126: 3 of 3 pass. The walk output is local and gitignored (client data); no client is named here.

| # | pin | claim | evidence read | grade |
|---|---|---|---|---|
| 42 | `20f95f79` | a model picked in the card scopes the map and the table | walk 20261001T064300Z `model-scope.json`: `pick_offered: true` on a row that is a client-directed holding, not a model; the seat's record reads the scoped table as "No securities match these filters." | **FAIL as shipped** (the shape this seat graded NOT_EVALUATED at 06:2xZ) |
| 55 | `486b07fd` | the pick is offered only on a row the Securities table can scope to | walks 20261001T065700Z and 20261001T070802Z `model-scope.json`: `pick_offered: false` on the holding row (2 of 2), `true` on a model row. Walk 070802Z shot 033, read by this seat, real backend, a two-account Cottonwood client with one account in focus: the scope line "Showing only Opal Conservative Growth -- back to all models"; three model chips with the picked one pressed; the Sleeve select reading the model; the Securities table listing 16 securities whose weights sum to 60.70 percent, equal to the model's $15,762,101.69 over the account's $25,967,218.59; the footers read "Source: Black Diamond." | **PASS on a live real run.** Item 42's claim holds at `486b07fd`; the promote candidate is `486b07fd` or later (CTO batch 67 item 6) |

## Observations from the live shot (not grades)

- **O-55a, a before-read for the narrowed classes.** At 07:11Z the served Holdings page classes `GLD` as Alternatives /
  Gold and `VXX` as Alternatives / Volatility for this Cottonwood client. `2.0.0_SA_COO~M`'s leg H5 expects the
  narrowed classes after the 14:15Z `irpt-holdings-snapshot` fire (commodities / Metals for the metals funds). This
  shot is the before state on the page.
- **O-55b.** Item 41's words are now live on a real snapshot: the three footers read "Source: Black Diamond." with no
  injected key. Item 41 was graded on the fixture plane; this is its first real-backend read.
- **O-55c.** The portal checkout carries one tracked edit not in `486b07fd` (`header/ClientSearch.tsx`, modified at
  07:2xZ). It is `2.0.0_SA_COO~D`'s work in progress; the local build a person smokes is therefore not exactly the
  promote candidate until it lands or is stashed.

## Not verified by this seat

DEV CI for `486b07fd` (the `gh run list` read returned another repository's runs); the first three walks' screenshots;
the hop-10 walk (section 2 of the seat's record), which is graded with IRPT_BCKEND.

-- 3.0.0_SA_CVO

## Grades, 2026-10-01 ~08:3xZ -- items 56, 57, 58

**Pins:** `8a814fd2`, `74d27b1b`, `437bef28`, each an ancestor of portal HEAD `437bef28`, which equals origin DEV
(ls-remote by this seat). **This seat's run at HEAD:** `bun test` over ten pinned files (iv-e-128, 122, 126, 119, 39,
34, 40, 118 and two neighbours): 10 of 10 pass. No client is named here.

| # | pin | claim | evidence read | grade |
|---|---|---|---|---|
| 56 | `8a814fd2` | the Global client list shows each firm's rows as that firm answers | unit iv-e-128 SEARCH-PROGRESSIVE-OK. Walk 20261001T074316Z `search-timings.json`: two typed names, first match at 2,113 ms and 1,488 ms, and `answered_ms` equal to `first_match_ms` in both | PASS on the unit claim and no regression on a live run. The progressive path itself is NOT_EVALUATED live: every firm answered together, as STATUS says |
| 57 | `74d27b1b` | OBJECT_NOT_COVERED on the Performance tab reads "Performance is not available for this client yet." | unit iv-e-39 and its neighbours green. STATUS: not looked at on the page because no served answer carried the code. That has changed: since 08:20:26Z the adapter answers OBJECT_NOT_COVERED for a refused vendor use (this seat's log read, 4 of 4) | PASS on the unit claim; the face is now readable on the real backend and has not been read |
| 58 | `437bef28` | (1) a selection with no class line heads its block "Position detail"; (2) the two selects leave room for their arrow | unit iv-e-126 arm (c2) green. Shot `item58/class-totals-and-selects.fast-run.png`: the block with three class lines and the remainder (the item-53 face), and both selects drawn with their arrow clear of the text "All". The whole-remainder face of (1) is not in the shot, and no long locked name is shown for (2) | PASS on the unit claim; the two faces the item changes are NOT_EVALUATED on a run, as STATUS says for (1) |

-- 3.0.0_SA_CVO

## Grade, 2026-10-01 ~09:4xZ -- item 59 (IRPT_DASHBD workstream F)

| # | pin | claim | evidence read | grade |
|---|---|---|---|---|
| 59 | portal `2879d65b` (portal HEAD and origin DEV by this seat's ls-remote) | the coverage words follow gold contract 0.2.0: the `guard_state` axis added, HOLDINGS_INCOME_FALLBACK dropped | `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` reads 0.2.0 at CLOUD HEAD; `bun test` iv-e-120, 121, 124, 125 at portal HEAD: 4 of 4 pass, parity failures 0, the planted-key control fails as it must | PASS on a test run; no page mounts the words module and no served file exists, as STATUS says |

-- 3.0.0_SA_CVO

## Grades, 2026-10-01 ~11:2xZ -- items 60, 61

**Pins:** `353b93dd` and `5f30a98d`; the second is portal HEAD and origin DEV (ls-remote by this seat, 11:23Z) and
the first is its ancestor. No client is named here.

| # | pin | claim | evidence read | grade |
|---|---|---|---|---|
| 60 | `353b93dd` | a refused account focus on the Performance tab is shown in words and never left on Loading; the refusal stays bound to the account it was refused for; Refresh re-attempts | this seat's `bun test` over eight pinned files (iv-e-129 new, iv-e-34 x3, 39, 40, 45, 118): 8 of 8 pass, 68 expects. The lane's real run was on the fixture plane; the signed-in page was the walk that found the defect, not a walk after the fix | PASS on a test run; the fixed face on the signed-in page NOT_EVALUATED |
| 61 | `5f30a98d` | a one-member level's tile takes the card's width: one predicate decides both the pie and the grid template | this seat's `bun test` over seven pinned files (iv-e-130 new, 42, 113, 119, iv-t-4, 111): 6 pass, 1 fail. The failure is iv-e-111 arm 3 alone, which diffs `src/pages/ModelPortfolios.tsx` against a base commit pinned inside the test (72fe8393) and finds 2,180 bytes of another lane's change; the commit states this failure in advance | PASS on a test run |

**One thing for the lane, not a grade:** iv-e-111 arm 3 is a stale instrument. It reads red on every run for a reason
unrelated to the behaviour it pins, so a real regression of arms 1 or 2 now hides behind an expected failure. The
repair is the test's (drop the pinned-base diff or move its base), owner `2.0.0_SA_COO~D`.

**Why the server refused the focused account's selection is still not explained** (the commit says so). The
answer is in the function's log, which is `2.0.0_SA_COO~P`'s surface; this seat did not read it.

-- 3.0.0_SA_CVO

## Grade, 2026-10-01 ~16:2xZ -- item 62

| # | pin | claim | evidence read | grade |
|---|---|---|---|---|
| 62 | portal `2bb367ef` (portal HEAD; origin DEV at 16:17Z by fetch) | the request list reads row statuses at most three at a time, starts no row read while an opened request is reading, and reads the pressed row next; a row whose read never reported is read again | this seat's `bun test`: the new pin iv-e-131 1 of 1; its neighbours (iv-e-62, 66, 74, 80, 116, 123 and `tabs/analysis/tests`) 24 of 24 across 9 files. The lane's real run was on the fixture plane; the signed-in re-walk with hop timing is owed, as the commit says | PASS on a test run; the timing on the signed-in page NOT_EVALUATED |

-- 3.0.0_SA_CVO

## Grade, 02:xZ 2026-10-02 -- NFRA_TRNSPT FWD-7 (2.0.0_SA_COO~D, `33176972f0`)

| claim | this seat's read | grade |
|---|---|---|
| `pull.py` lands admitted messages only by default; a near miss's PDF is never requested | `data/transcripts/scripts/tests` at HEAD (no drift from the pin): 165 passed. Negative control in a scratch tree with the parent's `pull.py`: `test_a_near_miss_keeps_its_message_and_list_and_none_of_its_documents` FAILS; with the pin's `pull.py` it passes; the other 5 scratch-environment failures are equal in both | PASS on a test run. Source only: no `--apply` run and no schedule, as the commit says |
| the released listing route (`GET /hx/mail/messages`) passes the four checks from the laptop | `r3_listing_checks.py` re-run 02:4xZ: check 1 equal (sha16 `75573170f29d64c9` on both routes); check 2 403, then 200 with 0 rows, then 400; check 3 7 pages, 6 rows, 6 distinct, same order, ascending; check 4 401 and 401. `LISTING-CHECKS-OK n=4` | PASS, SERVED (`mcp.opalinvest.dev`) |

**Limits.** The bearers of the other prefixes (site Z's arm) and the route's deployed commit were not read.

-- 3.0.0_SA_CVO

## ~D item 63 (E7 page half, portal DEV `281b03c6`), read 03:xZ-04:xZ 2026-10-02

| claim | this seat's read | grade |
|---|---|---|
| `readOwnedRequest` accepts the optional `comparisons` (at most 5, exact {key, label}) | the real readers run standalone in a scratch copy (type-only imports stubbed). PROD `b3a1d8a6`: two-field reads; the served E7 shape REFUSED `Invalid owned request projection`. DEV `281b03c6`: two-field reads; the served shape READS both comparisons in order; an extra field in a comparison REFUSED `Invalid owned request comparison` | PASS. Row S261's cause reproduced on PROD's bytes and removed on DEV |
| tests | `iv-e-132.request-comparisons.test.ts` at DEV (IR tree equal to `281b03c6`): 7 pass, 0 fail, 21 expects | PASS on a test run |
| CI | `CI - Build & Validate` at head `281b03c6`: success (02:52Z) | PASS |
| PROD | `origin/PROD` `b3a1d8a6`, `owned-requests.ts:23` still the exact two-key check | stated: PROD refuses the served shape until promoted; irpt-status E7 is HELD, so no request read breaks today. Order: PROD promote, then irpt-status D1 (row S261) |

**Limits.** No page walk and no served route; the comparisons line was not seen on a signed-in page.

-- 3.0.0_SA_CVO

## NFRA_TRNSPT FWD-7 additions (~D `84a59c91e6`, record `4b9ab98dd2`), read 03:xZ-04:xZ 2026-10-02

| claim | this seat's read | grade |
|---|---|---|
| landed_dates, absence through the writer's listing, builder names | `data/transcripts/scripts/tests` at HEAD: 174 passed; NAMES.json 4 of 4 names equal `lib/opal_naming.py name()` output | PASS on a test run; source only, nothing applied |
| bronze: 4 new objects under `date=2026-10-01` | listing of `bronze/analysis_commentary/` (auto-paginated): 8 objects; the 4 new ones (LastModified 02:07:21Z-02:07:23Z) have sha256 heads equal to the record (`44f12728..`, `de169e66..`, `bd776250..` %PDF-, `04d0bc6f..`); sidecar `id_source` internetMessageId | PASS |
| silver: 1 row, not held out | `silver/.../date=2026-10-01/analysis_commentary.parquet`: 14,533 bytes, aws:kms, LastModified 02:16:01Z; 1 row, 19 columns; ingest true, held_out false, sender_role author, pii_residual_flags []; 0 `@`, 0 e-mail addresses, 0 8-digit tokens. Control: the 2026-09-30 key 404 | PASS |

**Limits.** A seat started the run; it is not the schedule. client_recipient=false is recorded, not graded.

-- 3.0.0_SA_CVO

## NFRA_TRNSPT FWD-7 mail pull schedule APPLIED (~D, ledger `nfra-trnspt-mail-pull-schedule-20261002`), read 04:2xZ 2026-10-02

Opened `cdb5f18527`, closed `0af795349a`; halves COO `c19926eeae` (blob `62442e760f`), CTO `1062de89b1` (batch 109).

| claim | this seat's read | grade |
|---|---|---|
| V1: the function runs the signed zip | functions scanned 225; exactly 1 carries `CodeSha256` `teStghgdPZn8urHt8+IzpRM1HqZLiae6QN0LHvNwT3c=`: `outlook-global-transcripts-pull-lambda`, LastModified 04:01:35Z, Active; handler `mail_handler.lambda_handler`, python3.11, 600 s, 1024 MB, layer `pandas-pyarrow-layer`, env keys BEARER_SECRET_NAME, KMS_KEY_ARN, WINDOW_DAYS. Equal to `mail_pull.tf:98-112` at HEAD | PASS |
| V1: the schedule and its one target | rule `outlook-global-transcripts-pull-daily`, `cron(30 23 * * ? *)`, ENABLED, 1 target | PASS |
| V1: the role's one policy and the KMS grant | role `outlook-global-transcripts-pull-role`: 1 attached policy, 0 inline; statements: Get/Put on `opal-data-transcripts/outlook/transcripts/*`, List on the bucket, GetSecretValue on the gateway mail bearer, log writes. The transcripts key: 1 grant, to this role (Decrypt, DescribeKey, Encrypt, GenerateDataKey) | PASS |
| Q1: one ad hoc invoke, QA only | log group: 1 stream, last event 04:04:04Z; REPORT 19,853 ms, max memory 99 MB, no error line. `state/pull_runs/run=20261002T040405Z/run.json` and `silver.json` written 04:04:25Z (2 of 14 objects under the prefix); run.json: listed 13, candidates 12, near_miss 12, landed 0, ingest 0, admitted_only true, no_person true | PASS. As the lane says, QA is not FWD-7's evidence: the first scheduled fire (23:30Z) is |
| ledger | completion record CLOSED 3 of 3 legs; the JSON removed from `.open_deploys` in the close | PASS |

**Limits.** The Terraform state and the apply output were not re-read; the nine resources were read live except the
log group's retention and the Lambda permission's source condition (the rule's target is read). The 23:30Z fire is the
acceptance and is not read.

-- 3.0.0_SA_CVO

## Grades, 08:xZ-09:xZ 2026-10-02 -- portal DEV items 64-71, IRPT_DASHBD hop 5 item 5, and the Cottonwood re-point reader

PROD: none of the 10 pins is an ancestor of origin/PROD `b3a1d8a6`. NEG = the pin's test file run against the parent
commit's source.

| pin | claim | this seat's read | grade |
|---|---|---|---|
| b188be1f (64) | rows stop printing the header's client | OwnedRequestHistory.tsx:370 the row starts "Requested <date>"; the client slot and the useHeaderSelection import removed. iv-e-74 1/1, iv-e-80 1/1; NEG 0/1 each. CI 36963864012 success | PASS on a test run |
| 455ca18d (65) | the account drill is not a reload | HoldingsTab.tsx:161 focusDisplay keeps the all-accounts view while an account is "opening"; :379 "Opening"; :413 DrillTree keyed on shownAccountKey; accountPrefetch.ts:30. iv-e-133 6/6; NEG fails only at import. CI 36968044167 success | PASS on a test run |
| ed6fa7b2 (66) | the ticker stays in its column | HoldingsBreakdownTable.tsx:426 `truncate block` only when the ticker has no whitespace; title holds the full code. iv-e-134 1/1; NEG 0/1. Covered by run 36971124369 (2511f762), success | PASS on a test run |
| 3ca6c53a (67) | unclassified gets its own colour, lime900 | chartColors.ts:86 lime900 #365314; :626 MIX_PIE.unclassified; mixPieColor :630 also resolves "Unclassified". iv-e-136 1/1, iv-e-70 4/4; NEG 0/1. CI 36974686323 success. Its "IVE49-AC1 order-dependent" note is wrong: row DSGN_IRPTV1-S45 | PASS on a test run |
| 24e9032e (68) | resolved before it is added; rows named | GenerateComposer.tsx:344 resolveComparison runs before :351 addComparison. iv-e-137 6/6; NEG 4 pass / 2 fail (arms d, f) | PASS on a test run |
| 49cc08a3 (68) | the envelope parser adapts the catalogue | envelope.ts:170 the 'comparison-catalogue' adapter. FE-s-47 8/8; NEG 7/1 (F47-AC7). fe-s-13/14/47/57: the same 18 failing names at 3ca6c53a and at DEV (47 pass / 18 fail here; the commit says 55/10, difference not explained). CI 36977672706 success | PASS on a test run |
| c4e0d744 (69) | the card opens the picker; no loose input | VariantCards.tsx:110 directSelect; GenerateComposer.tsx:400 directSelect={catalogueRead==='ok'}; :478-488 Done sets the card; the input only in the non-live branch. iv-e-138 7/7 at DEV; no NEG run | PASS on a test run |
| 8df9e3d3 (71) | three picker faults fixed | GenerateComposer.tsx:320 heading "Compare with (n of 1 or 5)"; row remove gated `live ? null`; picker footer border-t px-6 py-4. iv-e-138 7/7; NEG 6/1 (arm g). CI 36982259587 success | PASS on a test run |
| item 70 | the signed-in walk of c4e0d744 | no portal commit; a walk record only (workspace 963baa82bb) | NOT_EVALUATED |
| 39b7a0fc (IRPT_DASHBD hop 5) | a served manifest shows the dashboard figure, as-of on the face | ReportingTab.tsx:444 dashboardFor binds the answer to the focused account; :746 period controls off; :754 DashboardPerformance replaces the report body; reportingRead.ts:44-47 a refusal reads "absent"; DashboardPerformance.tsx:241 "Data through". iv-e-135 8/8; NEG fails only at import. CI 36973315959 success. The FWD-1 signed-in run has not happened | PASS on a test run |
| eb90f2ad (~M) | no reader drops a served class | every served class mapped in PartnerAnalytics and AdvisorAnalytics; composition.ts CANONICAL_CLASSES includes unclassified; AdvisorAnalytics.tsx:669, :724 mixPieColor; ConsolidatedOverviewPanel.tsx:391. cot-unclassified 1/1; NEG 0/1. iv-e-46 1 pass, 1 fail (IVE49-AC1), the same at 2bb367ef and at the parent | PASS on a test run |

**Limits.** bun 1.3.9 in a detached scratch worktree of origin/DEV `8df9e3d3` under %TEMP%, removed after;
`git -C portal status --porcelain` equal before and after. CI runs lint, the provenance guard, typecheck and build, no
unit tests, so a CI success is not test evidence. The NEG runs for 455ca18d and 39b7a0fc fail at import, not on
behaviour; c4e0d744 has none. No page was looked at. The branch-filtered CI listing answered stale on 3 of 7 calls
(row ESTATE_GOVERNANCE-S36); every run above was read by id with its headSha.

-- 3.0.0_SA_CVO

## Grades, 12:xZ 2026-10-02 -- portal DEV items 72-81

PROD: none of the 10 pins is an ancestor of origin/PROD `b3a1d8a6`. NEG = the pin's source diff reversed on origin/DEV
`3bbf3914` with its test kept; MUT = a one-line planted mutant where the reversal broke only at import.

| pin | claim | this seat's read | grade |
|---|---|---|---|
| 0531cc65 (72) | the picker shows a dashboard account's own YTD with basis words; mixed lists name each basis (RULINGS batch 128 item 1) | pickerSuffix.ts:28-34 the body's own YTD plus "total return, before advisory fees, data through"; :41 the other account's figure plus "price return, as of <end>"; :54 no served account returns undefined (picker unchanged); ReportingTab.tsx:571-574 background reads only once one account is served, 2 at a time. All three clauses present. iv-e-139 4/4, iv-e-40 1/1, iv-e-58 1/1; NEG 2/2 fail of 4 (arms c, d). CI 36990470109 success. The suffix's date source: row IRPT_DASHBD-S20 | PASS on a test run |
| 06bc6f85 (73) | one date format on the Performance charts | PerformanceChart.tsx:55 dayWords via formatPageDate; :115 tickFormatter; DashboardPerformance.tsx:261. iv-e-140 3/3; NEG 1/2. CI 36991598167 success | PASS on a test run |
| 243f17b1 (74) | the pie folds past the 9 largest into "Other accounts (n)" | CategoryViewTree.tsx:1202-1220 folds only past keep+1; chartColors.ts:406 slate400; DrillTree.tsx:894 foldAccountsPast={9}. iv-e-141 4/4; NEG fails at import only | PASS on a test run |
| 7f9cf54a (75) | an Analysis print fetches by ?request= | PrintEntry.tsx:147-151 printReportRef; :209 refuses by name. iv-e-142 3/3; MUT 1/2. CI 36995066413 success | PASS on a test run |
| b618efc9 (76) | an Analysis print gates on its request's status | PrintEntry.tsx:160-165, :220 getJobStatus first, :224 a non-answer status fetches no sections; AnalysisDocument.tsx:70-72. iv-e-143 3/3; fe-s-54 3/3; NEG fails at import only. CI 36997787741 success | PASS on a test run |
| ad5c6e06 (77) | the picker numbers shared labels as the card does | AccountFilter.tsx:116-122 via uniqueLabel; :297. iv-e-144 2/2, iv-e-39 1/1; MUT 0/2. CI 36999982267 success | PASS on a test run |
| bf38f6c9 (78, row S45) | Mix cash green, 36.4 dE00 from commodities | chartColors.ts:616 MIX_PIE.cash = PALETTE.green300 #86efac, the same token as ASSET_CLASS.cash :207 (Andrew's C1); commodities yellow500 :629; 3e2233de did not move cash, so no new hue is minted. IVE49-AC1 alone: 1 pass, dE00 36.4025 (bar 20); NEG (amber500) 9.8943, 0/1. iv-e-46 class-readers 2/2. CI 37002638845 success | PASS on a test run; row S45 remediated on a test run |
| b46e6c36 (79) | the request read asks include=comparisons | investor-reporting.ts:1426; OwnedRequestHistory.tsx:49. iv-e-145 3/3; NEG 1/2. CI 37002252695 success | PASS on a test run |
| ebceef5b (80, row S40) | the catalogue joins the operation table | investor-reporting.ts:185, :229. fe-s-13/14/57 (12 files): 52 pass / 5 fail at DEV; NEG 44/13 (the commit clears 8). Of the 5, "three routes no consumer" is the one named; the other 4 fail on both arms, two of them contract drift: row IRPT_BCKEND-S269. The commit's 84/85 on 17 files is not reproduced. CI 37004059688 success | PASS on a test run |
| 3bbf3914 (81, row S48) | D1-inv-4 adds back the negative balances the card leaves off | CategoryViewTree.tsx:162-167; :1428-1429; :1447. iv-e-146 4/4; MUT 2/2. CI 37005333394 success | PASS on a test run |

**Limits.** bun 1.3.9 in a detached scratch worktree of origin/DEV `3bbf3914`, removed after; `git -C portal status
--porcelain` identical before and after. The fe-s tests read `../docs` and `../infra`; an archive of workspace CLOUD
`10d2b1c445`'s contracts was placed beside the worktree (without it they fail on file-not-found, which plausibly
explains item 68's unexplained 47/18). CI runs no unit tests. No page was looked at.

-- 3.0.0_SA_CVO

## Portal PROD promote portal-v2.1.194, read 14:xZ 2026-10-02

| pin | claim | this seat's read | grade |
|---|---|---|---|
| f76b02ac (head, tag) | PROD carries the promote | origin/PROD `f76b02ac` (ls-remote) tagged portal-v2.1.194 (13:46:09Z); parents `b3a1d8a6` (v2.1.193) and DEV `fa529337`; its tree equals `fa529337` (0 diff lines); `b3a1d8a6` has 0 non-merge commits outside `fa529337` | PROMOTED |
| merge message | Andrew-direct card 1, "at the DEV head after VALGATE" | names eb90f2ad, DEV `fa529337`, rollback `b3a1d8a6`, 0.0.0_AB_MSTR on "all recs approved" (CTO 104260); VALGATE run 37013653214 success, headSha `fa529337` | MATCHES the word |
| commit set | items 64-83 plus eb90f2ad | 48 commits (32 non-merge): 21 by ~D (items 63-69, 71-82, hop 5), `eb90f2ad`, 10 DSGN_AMGTV1. Items 64-82 are ancestors of PROD; `a134adb1` (item 83) is NOT (committed 13:39Z, pushed via `415f50db` 13:52Z). Controls: `2bb367ef` in PROD; origin/DEV not an ancestor of PROD | 64-82 YES; 83 NO |
| CI | Deploy to Production | run 37014885102 success, headSha `f76b02ac`; Build, Deploy to S3 + CloudFront, Tag all success | PASS |
| CTO `7c7bd9b4c9` | "PROD f76b02acb6 carries eb90f2ad" | `eb90f2ad` is an ancestor of `f76b02ac`: the BD r3 re-land's condition (CTO half `a1deb42063`) now holds | TRUE |
| submodule pointer | bumped on CLOUD | the gitlink is still `24646bca` on origin/CLOUD and on local HEAD; the /prod-deploy step is owed (the integrator's; pushes held per 0.0.0_AB_MSTR 104299) | NOT BUMPED |

-- 3.0.0_SA_CVO

## Grades, 14:xZ 2026-10-02 -- portal DEV items 82-83

| pin | claim | this seat's read | grade |
|---|---|---|---|
| a134adb1 (83, row S269) | the export reader takes exactly one reference | adapt.ts:1188 reads `narrative_packet_ref` only when present, else `analysis_report_ref.report_id`; :1195 adds analysisReportRef; :1413 the write side emits exactly one; wire/ExportBundle.ts an exactly-one union whose source sha256 equals the CLOUD HEAD schema. iv-e-147 4/4; NEG 0/4 (arm a throws the original TypeError at adapt.ts:1186). The content pin's "no longer REQUIRED ... unconditionally" is gone at DEV and returns under NEG. CI 37016314237 success | PASS on a test run; row S269 remediated on DEV, NOT on PROD |
| 18d18464 (82, row S53) | the consumer-uncalled pin derives from routes.json | routes.test.ts:126-142; the S53 test 1/1 at DEV; NEG (parent's test) 0/1; MUT (catalogue row removed) 0/1. routes.test 9/9 against the pre-PDF-route contracts, 5/9 against CLOUD HEAD (the 4 failures are the PDF route: row S273). The header at :28-33 still says "CONSUMER-UNCALLED ROUTES: 3". CI 37009030133 success | PASS on a test run |

**Limits.** bun 1.3.9 in a scratch worktree of origin/DEV `415f50db` under %TEMP%, removed after, with archives of
the workspace contracts beside it. The shared portal tree gained 28 modified files and an untracked test during the run
(mtimes 14:08Z-14:50Z): another seat's uncommitted multi_asset work; every write of this read ran in %TEMP%. CI runs no
unit tests; no page looked at.

-- 3.0.0_SA_CVO

## Grade, 17:xZ-19:xZ 2026-10-02 -- portal DEV item 84 (the multi_asset readers) and PROD v2.1.195

| pin | claim | this seat's read | grade |
|---|---|---|---|
| 262be0a4 (84) | the Investor Reporting readers render Multi-Asset in its own colour | chartColors.ts:92 yellow900 `#713f12`, :241, :648; adapt.ts:1001; index.ts:800; wire/HoldingsSnapshot.ts:104/:163/:173 (source sha256 equal to origin/CLOUD's schema); assetClass.ts:45/:63/:79; SecurityList.tsx:424; HoldingsTreemap.tsx:639; HoldingsTreemapChart.tsx:31. Nearest dE00 29.62 (unclassified), 30.07, 31.10. iv-e-148 6/6; NEG (its 8 source files at parent `415f50db`) 0/6. 13 fail / 243 pass across 184 files, the 11 failing files failing the same with item 84 reverted. CI 37035545923 and 37038081706 success | PASS on a test run |
| PROD | -- | origin/PROD `dcdc89b1`, tag portal-v2.1.195, merges DEV `ec65c5d6` (0 diff lines) and names 262be0a4; run 37041815698 success, headSha `dcdc89b1` | ON PROD |
| every reader of the mix | -- | the Advisor Intelligence half (`ed40c8ee` / candidate `6245e92d`, CTO batch 180 PASS) is on no origin branch; at DEV multi_asset is absent from composition.ts, PartnerAnalytics.tsx, AdvisorAnalytics.tsx, ConsolidatedOverviewPanel.tsx, TenantLayoutConfig.ts; Positioning groups by ASSET_CLASS_ORDER unchanged. 0 of 2,841 table rows are multi_asset, and batch 180 item 3 holds the rows until these readers are on PROD | IR YES; Advisor Intelligence and Positioning NO -- gated, no served move |
| census 37fd00f133 | the portal readers | names 2 portal readers (composition.ts, wire HoldingsSnapshot.ts); item 84 changed 7 files it never names | short: row MDPF_SECCLASS-S17 |

**Limits.** bun 1.3.9 in a scratch worktree of origin/DEV `ec65c5d6` under %TEMP%\cvo84; the worktree is unregistered but
its directory remains on disk (git reported "Filename too long"; a recursive delete waits on Andrew's confirmation, and it
holds nothing of the repo's). iv-e-148 arm (f) passes its own extraClasses rather than reading HoldingsTreemap.tsx:639;
SecurityList.tsx:424 is untested. CI runs no unit tests. No page looked at. DEV moved to `16c6690e` (item 85), not graded.

-- 3.0.0_SA_CVO

## Grades, 22:xZ 2026-10-02 -- portal DEV items 85, 87, 88 and DSGN_REBRND round 3 E4

| pin | claim | this seat's read | grade |
|---|---|---|---|
| 16c6690e (item 85; content 97cd8dea) | every security is its own map tile, each hoverable for name, value, weight, class | HoldingsTreemap.tsx:425 grouping retired; :464 the Value row; :558 drawSmallTiles; HoldingsTreemapChart.tsx:167-169, :378. iv-e-105/-114/-44/-61 1/1 each; NEG (reversed) 0/4 ("11 tiles, expected 14"). CI 37046875364 success | PASS on a test run |
| 4742a4b9 (item 87, row IRPT_BCKEND-S280) | a Sleeve/Account choice the new snapshot does not offer reads as All | SecurityList.tsx:205-207 effectiveFilter, :366-367 applied, :394/:412. iv-e-149 3/3; NEG 0/1 (import); MUT (wiring reverted) 3/3 -- the test does not reach the component (row DSGN_IRPTV1-S54); a scratch render with a stale choice: DEV lists rows, reverted reads "No securities match these filters". CI via 85162beb run 37064853264 success | PASS on a test run (by render); row S280 remediated on DEV, not on PROD |
| b0e59116 (item 88) | an uploaded prospect picks comparisons and the picks ride the submission | ProspectComposer.tsx:128-138, :143-147, :244 passes comparisonKeys; AnalysisTab.tsx:223. iv-e-150 5/5; NEG 2/5; MUT (:244 sends []) 5/5 -- the payload is untested (row S54). CI 37067700578 success | PASS on a test run (display); the payload NOT_EVALUATED |
| fb5d6116 (REBRND E4 part 1) | Positioning Summary fills move onto opaque named rungs | PositioningSummary.tsx:1130, :1145, :1219, :1232, :1261, :1548; no colour or contrast assertion exists; white on the tile rung 12.31:1 by arithmetic (was 12.93:1). CI 37069778437 success | NOT_EVALUATED |
| fe461611 (REBRND E4 part 2) | Breakdown subtotal and total rows take the tile and selected rungs | HoldingsBreakdownTable.tsx:237-242; HoldingsTab.tsx:1038-1111; no colour assertion; white on selected 8.50:1; the total's dash ink 4.23:1 (below 4.5); subtotal against body 1.22:1 (was 1.35:1) -- row DSGN_REBRND-S5. CI 37071013216 success | NOT_EVALUATED; one ink below the floor by arithmetic |
| full suite | -- | DEV fe461611: 935 pass / 43 fail / 9 errors (1,005 tests, 349 files, 26 failing files); the same 26 with the five pins reversed: the pins add no failure | -- |

Item 86 (workspace b6e3b75e56) is a 332-line Playwright page-walk harness and README under
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/yh/`, `node --check` only, not run live; item 88's real
run cites it. None of the five portal pins is on PROD (dcdc89b1).

**Limits.** bun 1.3.9 in a scratch worktree of origin/DEV fe461611 under %TEMP%\c88 with contract archives beside it;
removed after (Remove-Item on the long path; Test-Path False; 0 worktree entries); `git -C portal status --porcelain` 15
lines before and after. Contrast is arithmetic on index.css values, not a measured page. DEV moved to b66b6dac (item
89) during the read, not graded. CI runs no unit tests.

-- 3.0.0_SA_CVO

## Grades, 00:xZ-01:xZ 2026-10-03 -- DSGN_REBRND round 3 E4 (5 pins) and rows S5-S8 (handoff 104479)

PROD: all five E4 pins are on PROD 6169edd9 (Deploy run 37084775165 success; is-ancestor rc 0 for 5 of 5; content
control: the PROD dash is white/70 and toOklab present).

| pin / row | claim | this seat's read | grade |
|---|---|---|---|
| 661e49b3 | the Models view's interactive text clears 4.5:1 | HoldingsTab.tsx:80 AGG chip indigo400 #818cf8 on band 5.94 (was 4.22) by arithmetic; no test. CI 37079617916 success | NOT_EVALUATED by test; the ink PASS by arithmetic |
| 44d6a215 | a highlighted name keeps its colour on a band ground; OKLab ramp | PositioningSummary.tsx:42-46, :1462-1466; bookColors.ts:57-85. Canon on band: UST 6.33, ST 8.26, INT 6.99, LT 4.82, ULT 4.71; #a775a5 4.84 (was 3.86). No test. CI 37080785301 success | PASS on the walk's computed styles; NOT_EVALUATED by test |
| b23917f7 (S5's remedy) | dash white/70, pinned by iv-e-152 | HoldingsBreakdownTable.tsx:240; iv-e-152 3/3; NEG (white/60, test kept) 2/3, arm (a) fails at 4.23. Arithmetic: selected rung L 0.07350, white/70 composite L 0.58302: 5.13:1; tile rung 6.91:1. CI 37081937697 success | PASS on a test run; S5 REMEDIATED (arithmetic, not pixels) |
| E4 re-grade (fb5d6116, fe461611) | the rungs carry their text | iv-e-152 hardcodes subtotal = tile and total = selected and never reads subRow/totRow or PositioningSummary; MUT (both pins' rung classes reversed, white/70 kept): still 3/3 | fe461611: inks PASS by arithmetic, rung choice unpinned; fb5d6116 NOT_EVALUATED |
| full suite | -- | DEV b23917f7 877 pass / 67 fail / 18 errors (969 tests); the three pins reversed: same counts; the pins add no failure | -- |
| S6 (W2-S8 on /positioning) | every canon mark on the band, 316 pairs, 0 under | W2-S8 asked about canon hexes under 3:1 on WHITE grounds; Positioning has 0 white or light grounds; the walk (getComputedStyle, interactive controls only, 316 rows, min 4.72, bar 4.5) has 48 canon-ink rows, all on the band; bars on the tile rung clear 3:1 (UST 4.39 ... ULT 3.27) | supports the disarm for /positioning; the walk covers text controls only (row S10) |
| S7 (W1-S11 latent) | no code selects dark mode | `dark-mode`: 8 hits in 3 files, 0 setters | latent CONFIRMED for html.dark-mode; a second, OS-driven dark path exists (row S9) |

**Limits.** bun 1.3.9 in a scratch worktree of origin/DEV b23917f7 at %TEMP%\c90, removed after (Test-Path False);
`git -C portal status --porcelain` 15 lines before, 19 after -- the 4 new are the live lease's E2 work (DESIGN.md,
Positioning.tsx, PageEnd.tsx and its test), not this read. Contrast is arithmetic and computed styles, not pixels. DEV
moved to c9d303db during the read, not graded.

-- 3.0.0_SA_CVO

## Grades, 03:5xZ-04:4xZ 2026-10-03 -- portal DEV items 89, 89 follow-up, 90, 91, DSGN_REBRND E2, IRPT_DASHBD S20 fix

Graded at origin/DEV `84f2424f` in a scratch worktree (removed after; Test-Path False). CI ("Build & Validate") runs
lint, provenance, typecheck and build, and no unit tests.

| pin | claim | this seat's read | grade |
|---|---|---|---|
| b66b6dac (item 89) | the prospect upload and submission carry `selected_tenant` | `investor-reporting.ts:1085`; iv-e-151 3/3; NEG (client half) fails; NEG (composer call sites) 16/16 still pass; CI 37074525848 success; on PROD | PASS on a test run (client half only); row S55 |
| 39aa21c2 (89 follow-up) | the composer takes the tenant from the selected scope | `AnalysisTab.tsx:225`; no test; scratch render `data-tenant-known` yes, reverted no; CI 37076948990 success; on PROD | PASS by render; row S55 |
| c9d303db (REBRND E2 contract) | DESIGN.md C10 gains the PAGE END | `DESIGN.md:387-401`; no test reaches it; CI 37085750211 success; not on PROD | NOT_EVALUATED |
| 8526dacb (REBRND E2) | /positioning ends on its PAGE END | `PageEnd.test.tsx` 2/2; mutants on the date format and `data-page-end` fail; NEG (page wiring) still 2/2, so the render carries the wiring: scratch render ends "End of Positioning.", reverted does not; CI 37086651757 success; not on PROD | PASS on a test run + PASS by render |
| c32ef52a (item 90) | a NAME_PROXY finding is answered by re-posting with corrections | iv-e-153 4/4; NEG 2 fail; mutants on the gate and the 20-item cap fail; MUT on the re-post line passes 4/4; CI 37088374567 success; not on PROD | PASS on a test run; the re-post NOT_EVALUATED (row S55) |
| de3eca94 (item 91) | holdings asks for the TARGET fold, shown apart, never summed | iv-e-154 and 5 re-goldened files 22/27, the 5 reds also red with the pin reverted (routes.json 19 vs client table 18); NEG and 4 mutants fail; CI 37090356749 success; not on PROD | PASS on a test run |
| 84f2424f (IRPT_DASHBD S20) | the picker and the body read one date, `series.as_of` | iv-e-156/139 and fe-s-30 13/13; NEG 2 fail; MUT (picker reads `manifest.as_of`) fails; no `manifest.as_of` read left in `src`; CI 37092338048 success; not on PROD | PASS on a test run; S20's remedy landed on DEV: remediation state OPEN -> REMEDIATED in REMEDIATION_v2, closed stays false until PROD carries it |
| full suite | -- | DEV head 1052 pass / 34 fail / 2 errors (1113 tests); the 7 pins' non-test changes reverted: 1037 / 45 / 6; 0 tests fail at head and pass reverted; the pins add no failure | -- |

**Known classes, not new rows:**
- A full `bun test` rewrites tracked wire files through iv-e-26 (row W41-S2).
- A CRLF checkout fails iv-e-116's source check: 66 fail / 18 errors, against 34 / 2 on the committed LF bytes (rows W4-S3,
  W26-S2).

**Limits.**
- Static render only; no clicks and no live page.
- The workspace contracts are CLOUD HEAD's committed bytes.
- DEV moved to 936424c3 / 209e4903 during the read, not graded.
- `git -C portal status --porcelain`: 19 lines before, 15 after. The difference is ~D's own two commits; the reflog shows
  no write by this seat.
- Read by a delegate of this seat.

-- 3.0.0_SA_CVO

## Grades, 08:5xZ-10:3xZ 2026-10-03 -- portal DEV 936424c3 through 46aeea17 (12 pins; ~D msgs 104593, 104602, 104604)

Graded in a scratch worktree of origin/DEV (a sparse workspace copy with the portal nested, so the tests' workspace paths
resolve), removed after. None of these pins is on PROD (6169edd9). Every CI run concluded success; CI runs no unit tests.

| pin | claim | this seat's read | grade |
|---|---|---|---|
| 936424c3 (IRPT_DASHBD) | NOT_SPANNED/BREAK say "Not measured" in body and picker | `DashboardPerformance.tsx:247`, `pickerSuffix.ts:39`; 2/2; NEG and 3 MUTs fail; CI 37094927372 | PASS on a test run |
| 209e4903 (IRPT_DASHBD) | a custom range opening before the history is NOT_SPANNED | `:79`; 2/2; NEG fails; CI 37097260187; leaves the "shortened" note branch unreachable | PASS on a test run |
| 102c15e0 (item 92) | a needs-attention request offers the refill | `OwnedRequestHistory.tsx:49,226`; 2/2; NEG fails; 3 MUTs survive (the Generate gate, the new request id, the client seed); a render probe shows the client seed | PASS on a test run + by render; the refill submit NOT_EVALUATED |
| 25b7a59d / f4bad219 | land and revert | `git diff 25b7a59d^ f4bad219` is 0 bytes | nets to zero |
| 9bd6517d + 3ff86a54 (item 93) | Download opens the signed URL; the parser reads the pdf envelope | `ReceiptPanel.tsx:102`, `adapt.ts:1359`, `download.ts:68`, `envelope.ts:165`; iv-e-161 1/1; NEGs and 3 MUTs fail; a MUT at `investor-reporting.ts:1087` survives the test but fails a LiveClient probe; CI 37108254305 | PASS on a test run + by probe |
| 201bfe69 (REBRND E6) | comments only | 23 of 28 files have identical comment-stripped ASTs, 2 are non-code, and 3 change string literals only (one demo file undisclosed); readers 34/34 | NOT_EVALUATED (no logic change) |
| d7141e5a (REBRND E3) | a NO-PERMISSION panel instead of a bounce | `ProtectedRoute.tsx:121`; 1/1; NEG and 2 MUTs fail; F49-AC4 32/32 at the parent, 31/32 from this pin on | PASS on a test run; adds 1 failure (row DSGN_REBRND-S13) |
| d8d236a0 (REBRND S10) | Equity blue400 5.89:1, Structured pink400 5.65:1 | `chartColors.ts:545-549`; 4/4; NEG and both hex MUTs fail; this seat's WCAG on #192643: 5.886 and 5.650 (old #3b82f6 4.069) | PASS on a test run; row S10 remedied on DEV |
| 71a946e3 (REBRND 4b) | secondary ink 8.14:1 footer, 6.87:1 body | `PanelFooter.tsx:102`; 1/1; NEG and 2 MUTs fail; the served token is #A8B1C2 (`design/themes/opal-capital.css:28`), not the cited #A8B0C0: 8.19 strip, 6.91 body, 5.69 tile; white/40 0 times in Positioning's 15 source files | PASS on a test run |
| 46aeea17 (REBRND 4c) | Satellites footers use the footer date format | `formatPanelTimestamp` (`dateUtils.ts:527`), as Models and ETFs already did; 1/1; NEG fails; MUT `formatPanelTimestamp(null, null)` at `HoldingsTab.tsx:307` survives (arm (a) is a source regex) | PASS on a test run (the formatter); footer render NOT_EVALUATED |
| full suite | -- | DEV 46aeea17 1077 pass / 31 fail / 0 errors (1135 tests); all pins' non-test changes reverted: 1065 / 43 / 3; 0 tests fail at head and pass reverted. The revert cannot see the committed-blob tests, so d7141e5a was checked against its parent separately | -- |

**Other observations.**
- Untested legs, row S55's class: item 92's refill submit, item 93's live-client read, and the value 46aeea17 passes to
  the formatter.
- fe-s-90 CONTROL 3 failed once and passed at three later heads (flaky).

**Limits.**
- Tests, static renders and probes only; no clicks.
- The workspace contracts are CLOUD HEAD 2cc72c270e's.
- DEV moved to fb5534f8 during the read, not graded.
- `git -C portal status` reads 15 lines before and 15 after.
- Read by a delegate of this seat.

-- 3.0.0_SA_CVO

## Grades, 10:5xZ-12:3xZ 2026-10-03 -- portal DEV fb5534f8 through b0b3c524 (6 pins; ~D msgs 104605-104610)

Graded in scratch worktrees (a sparse workspace copy with the portal nested), removed after. None of these pins is on PROD
(6169edd9). Every CI run concluded success; CI runs no unit tests.

| pin | claim | this seat's read | grade |
|---|---|---|---|
| fb5534f8 | with 6+ books the percentage labels sit beside the bar; the five-book layout is byte-identical | `PositioningSummary.tsx:1188,1380`; 1/1; NEG fails both arms; render probe: 5- and 4-book markup byte-identical at parent, pin and tip, 8-book differs in exactly 16 elements; CI 37116673391 | PASS |
| cbfbb77a | daylight saving decided for New York, not the viewer's zone | `dateUtils.ts:333-344`; 1/1 under UTC, Los Angeles, New York, Tokyo; NEG fails; 3 MUTs killed; 17 dates across the March and November changeovers (2026, 2027) against an independent New York check: 0 wrong at the pin, 4-9 wrong at the parent; CI 37117501484 | PASS; the message's "US-zone viewer unchanged" is false on changeover days, where the change corrects them |
| 55560835 | RSI and Fear & Greed show ERROR; the endpoint no longer fabricates 50 | 1/1; NEG fails; MUT "endpoint returns 50" killed; MUT on the gauge's `: 50` survives; CI 37118751941 | PASS on the claim; its process-wide `mock.module` of React Query errored 4 tests in 4 files (iv-e-101, -16, -38, -57) until b0b3c524 |
| a7b16628 | Daily Cloud, Trending, Performers show ERROR; the keyword endpoint no longer returns [] | arms a-f pass; NEG fails d-f; 4 MUTs killed; page wiring `failed={false}` survives; CI 37119845342 | PASS |
| 564a8f95 | the RSI hook no longer invents 50 | no committed test; probe through RSIBars and the real hook: a missing class gives ERROR at the pin, 50 drawn (and a TypeError on a missing segment) at the parent; a full summary draws 3 bars at both; CI 37120582863 | PASS by probe; unpinned |
| b0b3c524 | a failed Models load is ERROR in all three /positioning panels; the market mocks are restored | 1/1; NEG fails; 2 MUTs killed; the market arms are unchanged; both pin files pass in both orders; CI 37122027543 | PASS; ends the 55560835 leak |
| full suite | -- | b0b3c524: 1079 pass / 33 fail / 0 errors (1139); six pins' non-test files reverted: 1074 / 38; at 46aeea17: 1074 / 34; every failure at head also fails at the parent (one FE-s-90 timing flake) | -- |

**Rows and notes.**
- DSGN_IRPTV1-S56: F47-AC6 has failed since b618efc9 (on PROD).
- W3-S4's remaining sites at the tip: 20 `?? 50` / `|| 50` sites.
  - Values: `MarketRegimeIndicator.tsx:182-184,202-204,267`, `RSIModal.tsx:192,1002,1004,1015`, `RSIBars.tsx:52-53`.
  - Colour or label only: `MarketRegimeModal.tsx`, `FearGreedModal.tsx`.
  - `getAAIILatest` (`sentiment.ts:819`) fabricates 33.3/33.3/33.3 but has no live caller.
- Untested wiring, row S55's class: `MarketPerformance.tsx` `failed`, `Positioning.tsx` `loadFailed`, and HoldingsTab.

**Limits.**
- Server-side markup probes only; no viewport or pixels.
- bun on Windows ignores TZ, so the zones were set through a preload.
- Process note: the delegate's `git config` wrote `core.autocrlf=false` into the shared workspace `.git/config` at
  10:51:47Z and removed it about two minutes later. This seat re-read it at ~12:3xZ: no local value; the system true
  applies; 0 commits landed in 10:49-10:57Z.
- Read by a delegate of this seat.

-- 3.0.0_SA_CVO

## Grades, 16:5xZ-18:2xZ 2026-10-03 -- portal DEV b0b3c524..e862b0c4 (15 pins; ~D msgs 104612-104630)

Graded in scratch worktrees, removed after. The shared portal status reads 35 lines before and after; no git config was
written. None of the pins is on PROD (6169edd9). Every CI run concluded success; CI runs no unit tests.

| pin | claim | this seat's read | grade |
|---|---|---|---|
| 94c055e8 | /attribution ERROR and LOADING | `StylePolicyComparison.tsx:161`; 1/1; NEG and MUT fail; probe: failed -> ERROR, pending -> LOADING (parent EMPTY both) | PASS |
| c3e1d7b9 | /portfolio-management placeholders, one ERROR | 1/1; NEG fails (0.00 x28); MUT fails; the wiring `PortfolioManagement.tsx:433` is unpinned (`serviceFailed={false}` passes), the probe shows it right | PASS; pin gap |
| 3d8cce99 | /ticket-center one ERROR, Try again, no raw JSON | no pin; probe at pin and parent; MUT caught | PASS by probe |
| 30f7fca1 | /data-refresh History and Rollback ERROR | no pin; probe of the hook and both tabs; MUT caught; no rollback hunk | PASS by probe |
| 075d33fa | Advisors one ERROR | probe; a no-data control is EMPTY; MUT caught | PASS by probe |
| 10fca02d | "Connected" only once data arrives | probe on 4 partner pages; the with-data arm rendered on Cottonwood only | PASS by probe |
| 1754d9c1 | RSI: no marker, "not published" for a missing period change | probe; the Fixed Income control still drawn | PASS by probe |
| 4a40a0ff | RSI modal "Not published"; a real 0 stays 0 | probe: null -> "Not published", 0 -> "Oversold" (parent "Neutral" both); MUT caught | PASS by probe |
| 6e31c220 | /positioning notices are PanelError / PanelEmpty | probe on 2 of 6 notices | PASS by probe (2 of 6) |
| 1b8fccfd | Assets Overview ERROR | probe on 4 arms; MUT caught | PASS by probe |
| e2563c17 | F49-AC4 counts the NO-PERMISSION panel | fe-s-49 10/10 at the pin, 9/10 at its parent; MUT 6/10 | PASS; row DSGN_REBRND-S13 answered |
| 2da1eaaf | F47-AC6 classifies PrintEntry :83, :162 | fe-s-47 8/8 at the pin, 7/8 at its parent; MUT fails | PASS; row DSGN_IRPTV1-S56 answered |
| 7e7f9aa2 | component tests for items 87 and 88 | 10/10; this seat's two S54 mutants (accountFilter = ownAccountFilter; sending []) both fail | PASS; row S54 answered |
| 525c9404 | S55 four arms | 1/1; each named mutant fails its arm; the catalogue-read mutant passes (disclosed) | PASS; row S55 answered for the four arms |
| e862b0c4 | Holdings card follows the /portfolios canon | 2/2; NEG and MUT fail; the `undrawnCardRows` rename (`DrillTree.tsx:600`) untested | PASS |
| full suite | -- | 1145 tests: head 1088 pass / 30 fail; the pins reverted 1084 / 34 (the 4 extra are the pins' own); the same 30 fail in both | -- |

**Rows.**
- Answered in code on DEV: DSGN_REBRND-S13, and DSGN_IRPTV1-S54, S55 (four arms; the catalogue tenant still blind) and S56.
- W3-S4 holds on every route this range touched.
- All of these are recorded at the next compile of each channel.

**Notes.**
- iv-e-26 regenerates `contracts/wire/ExportBundle.ts` and `ExportReceipt.ts` from the workspace contract, which now
  carries `frozen_as_of`, so the committed wire types lag the contract. This is row W41-S2's class, and the likely source
  of the "uncommitted wire-contract edits" row S59 attributes elsewhere.
- Ticket Center shows "No open tickets." on its first render, before the load starts.

**Limits.**
- Server-render probes only.
- The /attribution empty-data case (0.00 weights) was not re-measured.
- Read by a delegate of this seat.

-- 3.0.0_SA_CVO

## Grades, 18:4xZ-19:2xZ 2026-10-03 -- the B2 PROD promote (98a98e70, portal-v2.1.197) and DEV to 7b265fc4

PROD 98a98e70 (merged 18:33:53Z by 0.0.0_AB_MSTR on Andrew's word) has a tree equal to 2f326afc. Deploy to Production run
37144813955 succeeded; the site's index.html was rewritten at 18:38:19Z; the shipped JS carries the summary route,
`performance_source`, `frozen_as_of`, `version_id` and "Sleeve: ".

| pin | claim | this seat's read | grade |
|---|---|---|---|
| 19796bc0 (B1 merge) | lands the P-3/P-6 branch unchanged | a scratch re-merge gives an identical tree; 8 clean auto-merges; 24 files = the 6 commits' files; on PROD | PASS |
| 0410f358 (P-3) | the picker reads the client summary, falling back to the account manifests | iv-e-155 1/1; NEG 0/1; MUTs at `pickerSuffix.ts:94` and on the fallback killed | PASS |
| 79e7cfc8 (P-6 print) | a print naming its account reads PATH B | iv-e-158 2/2; NEG fails; MUT on the dispatch killed | PASS |
| 16f5c8ea (P-6 export) | the export sends `performance_source`, naming no retained report | iv-e-159 1/1; NEG fails only as an import error; MUT dropping the field killed | PASS (the MUT carries it) |
| c16a31e9 | the export's print reads the frozen version | NEG 0/2; MUT killed | PASS |
| b847c9f0 | the receipt shows the frozen as_of | iv-e-162 1/1; NEG and MUT fail | PASS |
| 426761e4 | iv-e-162 typecheck | test-only; CI success | PASS |
| 2f326afc (Andrew-direct) | chips read "Sleeve:", plus "Sleeve: Client" | 3/3; NEG and MUT 0/3; on PROD | PASS |
| 3a842221, a6a77e31, 6cb31b54, cc1d7cc6, 7b265fc4 (DEV only) | regime no-reading; wiring tests (this seat's untested-wiring note); auth error state; /factor-tilts one state; merge | each 1/1 or 2/2 with NEG and MUT failing; clean re-merge | PASS |
| full suite | -- | DEV head 991 pass / 35 fail / 7 errors (partial checkout); the code changes reverted 981 / 45 / 9; 0 regressions | -- |

**What a PROD viewer gets (read via read-only AWS, no signed-in walk).**
- The summary route (`entry.py:92`, `:373`) is live on the gateway behind irpt-49f-reporting-read-lambda, whose deployed
  hash equals the workspace's. S3 holds 4,241 client summaries.
- The account route, with `version_id` on the series read, is live.
- The export submit, receipt and download routes are live on irpt-export-render, which handles `performance_source` and
  `frozen_as_of`.
- No UI path calls an undeployed route.
- B3 (PATH A retired for 49F) is not deployed: irpt-performance-adapter still runs the old code, so PATH A remains a
  fallback.

**Rows and notes.**
- IRPT_DASHBD-S23: routes.json omits both live reporting routes.
- cc1d7cc6 converts `FactorTilts.tsx` CRLF to LF, so a 41-line fix diffs as 507 lines.
- The wire-regeneration class is row W41-S2's.

**Limits.**
- No signed-in walk; the edge validator :22 and the render grant come from the ledger.
- Some NEGs ran at the commit, because the revert did not apply at head.
- Read by a delegate of this seat.

-- 3.0.0_SA_CVO

**Correction (19:2xZ).** Row IRPT_DASHBD-S23's `surfaced_at` reads 2026-10-03T19:25:00Z, ahead of the clock: the row was
committed at about 19:18Z (d040623b6e). Nothing in the row changes.

-- 3.0.0_SA_CVO
