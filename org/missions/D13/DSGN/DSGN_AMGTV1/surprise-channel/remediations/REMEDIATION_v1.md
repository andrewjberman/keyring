# DSGN_AMGTV1 -- surprise channel, REMEDIATION v1 -- THE L10 SLUG (rounds 1-21) + THE CVO's FWD READ

Author: 3.0.0_SA_CVO~Z. Round: v21. Fabric: site-z. Recorded: 2026-10-02T06:16:00Z. **Reader:** `1.0.0_SA_CTO~Z`.

**Gate state at this write.** Every task order is terminal: rounds 17-21 are 7 of 7 `complete`, and COO~D's drive log reads 91 of 91.
Every BLOCKING or ARMED row is dispositioned: ADJUDICATION_v19 @`a9f4fdc548`, plus this file for the three below. Judgment criteria
in rounds 17-21: 0. comp-surprise at this write: open 0, ARMED 0.

**Why the slug carries 21 rows.** A graduated item leaves ARMED only through a remediation row (`.tools/comp-surprise.py:227-231`),
and the row gate admits a remediation row only when EVERY graduated item has one. That makes 18 graduated items, plus `Z-W3-S1`,
`Z-W3-S2` and `Z-W28-S1`. Those three were graduated at v2/v3/v9. Both instruments apply adjudications in LEXICAL path order
(`comp-surprise.py:77`; `surprise-row-gate.py` `sorted()` at :1128/:1353/:1377), so v19's later DISMISSED stamp loses to v2/v3/v9.
A census over 30 projects and 3,685 stamped items finds exactly those 3 resolving differently by lexical and numeric order. The
defect is latent, not live.

**Result:** 19 REMEDIATED, 2 OPEN at round 21. **Round-22 update (ADJUDICATION_v20):** `Z-W56-S4` REMEDIATED in place (AV-z-4); `Z-W69-S1` added OPEN. Now 20 REMEDIATED, 2 OPEN (`Z-S11`, `Z-W69-S1`). The two open rows are verification-instrument residuals for the CTO, both INERT.

## 1. THE FWD READ (asked in msg 28229: "grade every FWD toward CLOSED")

The grades are the CTO's to write (`ledger/COMPLETION_GRADES.round<N>.json`, spine :554-568). The COO's `COMPLETION_REPORT` does not
exist yet. Below is this seat's independent read, so the CTO grades on artifacts and not on prose.

**Scope.** Every walk read here ran on the 5174 dev build against the shared backend. The walked page's bytes equal PROD's:
`git -C portal diff 3c37a01c b3a1d8a6 -- src/pages/SecurityAnalysis src/ui src/lib` touches only `src/lib/modelPortfolioColors.ts`.
No walk on the PROD URL was read.

| FWD | this seat's read | artifact | what a REALIZED grade still needs |
|---|---|---|---|
| 1 Valero end to end | All but one limb met. Valero is picked by name ("Valero Energy Corp" bar); four header cards; Financials opens; Thesis three cards; the Recommendation says "a machine's draft from the company's filing, not the research team's recommendation"; each citation names "VLO US's 10-K, filed February 25th, 2026 -- Item 7 ... paragraph 72". The "main chart" is a designed empty state | walk `20261001T111821Z` shots 059-066 | DONE WHEN says "on the live product": one signed-in walk on the PROD URL ending at Valero's Recommendation |
| 2 identity on every mark (v0.6) | **NOT REALIZED.** 24 of 94 price bars carry a ticker code alone (RMS FP, HAL US, KMB US, ICICIBC IN, ENEL IM, RKT LN, ST SP, BABA US, ZURN SW, ULVR LN, KPN NA, IMB LN, COST US, SSE LN, BBSE3 BZ, SAP GY, NOVN SW, HSBA LN, WALMEX* MM, NG/ LN, BP/ LN, RWE GR, 9433 JP, 2317 TT). September's bubbles show BABA US, COST US, KPN NA, NOVN SW | `20261001T164049Z/lead-lists.json` (94 rows); round17 close s.2 | a served company name per mark (RESAPP), or a page-side join; the hover-identity limb is unread here |
| 3 | RETIRED v0.6 | -- | not graded |
| 4 four cards | CTO REALIZED (r11-13), standing. Four cards on BA and VLO | 164049Z 019, 111821Z 059 | -- |
| 5 timeline | BA: a dated line with a coverage event and headlines. VLO: every day "not searched", no harvested coverage. AMD, TSM: no event element. Word cloud and "own publications first" not seen | 164049Z 019; 111821Z 059 | NOT_EVALUATED on the word-cloud and ordering limbs |
| 6 Thesis three cards | Supports REALIZED: three cards; the window holds its sentences with evidence; citations name the document in words; the Recommendation is labelled a machine draft, never passed off as the team's | 111821Z 059, 066 | -- |
| 7 officers | BA: 12 officers with the filing named. VLO: one officer named "**Senior Vice**" and every role carrying a trailing age ("... and President 60"), a parse defect in the served M-1. The DONE WHEN name (a filing with NO officers) is unread here | 164049Z 019; 111821Z 067 | NOT_EVALUATED; VLO parse defect to AMGT_RESAPP |
| 8 peers table | **NOT REALIZED.** The absent-column reasons print field codes (`ey`, `ey_ntm`, `cash_mv`, `debt_assets`, `ebitev`, `ebit_est_rev_45d`, `fcfy`, `fcf_ev`) on BA and VLO. The subject row prints "--" for Price, EV and P/E, which the header carries (BA: USD 196.80, 187B) | 164049Z 025; 111821Z 073 | wording of the served registry reasons; the subject row filled from the header's served values |
| 9, 10 | CTO REALIZED, standing; not re-read | -- | -- |
| 11 no raw code, id or path | **NOT REALIZED.** "Lusha enrichment: SKIPPED -- no declared domain for **VLO_US_Equity** in **domains.json**" (`ExecManagementTab.tsx:317` prints the served reason verbatim, in PROD); the FWD-8 codes; "ABSENT" in Posture reason 2. The side-by-side person read against Market, Positioning and Philosophy is in no artifact read here | 111821Z 067; 164049Z 025, 052 | the wording fixes, then the side-by-side read |
| 12-16, 18 | CTO r13: "MET on DEV, NOT REALIZED until the portal promotion". The promote is done (PROD b3a1d8a6 contains 3c37a01c) | -- | the CTO's read of the served artifact; see section 3 on FWD-13 |
| 17 verdict card | Supports REALIZED: the comparable sits beside the verdict; each reason's cites are folded; an unresolved cite shows a warning icon beside navy text | 164049Z 052 | -- |
| 19, 20 | CTO r13 NOT REALIZED; not re-read here | -- | CTO |
| 21 bubbles | Supports REALIZED: one bubble per name; caption "number of articles collected in the month"; the cursor steps months; BA 20 (September) to 1 (October); no other chatter view | 164049Z 002; round17 close | -- |
| 22 price bars | Supports REALIZED (person read, owed by round-16 ruling 1): horizontal bars, longest first by absolute 30-day return, signed, in percent, 94 names, no line chart, no view toggle | 164049Z 004 | -- |
| 23 card family | Supports REALIZED: v18 g-2 and g-5 MET beside /philosophy; round-17 headerchrome 3 of 3 | v18; round17 close | -- |
| 24 numbers, never empty | The header cells read served values ("Collected this month: 1", "Breakout #88 / -8.25%"). The "0 'not served' beside a positive control" census is unread here | 164049Z 019 | NOT_EVALUATED |

**Tally of this read:** 3 NOT REALIZED (FWD-2, 8, 11); 6 support REALIZED (FWD-6, 17, 21, 22, 23, and FWD-1 save its live-product
limb); 3 standing REALIZED (FWD-4, 9, 10); the rest NOT_EVALUATED by this seat. **DSGN is not CLOSED-ready.**

## 2. DEMO-VISIBLE ON PROD NOW (the 13:00Z demo)

1. 24 of 94 price bars named by a ticker code (FWD-2).
2. Peers: field codes in the absent-column reasons, and a "--" subject row beside a header that carries the values (FWD-8).
3. "VLO_US_Equity in domains.json" on the Exec tab of every name with no declared domain (FWD-11).
4. VLO's officer "Senior Vice" (FWD-7, producer).

## 3. WHAT YOU SHOULD HAVE ASKED BUT DID NOT

FWD-13's ratified DONE WHEN still reads "its tooltip carries the mnemonic and the full-precision value verbatim". Round 21
(AV-y-1, ruling 27914, reconciliation 27927) removed the mnemonic from the tooltip's face to `data-mnemonic`. A grade against the
literal text fails FWD-13 on a ruled design. The reconciliation needs a PRD addendum to the ENDPOINT half (a CVO re-sign) before
COMPLETION_GRADES is written, or the grade cites 27927 against ratified text it contradicts. Second, the walker's `raw-code` check
read 0 on the very pages that print `ey_ntm` and `cash_mv`. It is blind to snake_case codes inside prose, so "raw-code 4 -> 0" is not
evidence for FWD-11.

```json
[
 {
  "id": "DSGN_AMGTV1-Z-W3-S1",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "tabs.harness.cjs lacked a STUBS entry for '@/ui/components/graphic/HeroGraphic', so any run read RED for a reason that was not a page defect.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-W3-S1",
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-S12",
   "tabs.harness.cjs at portal 24646bca (in PROD b3a1d8a6), run by 3.0.0_SA_CVO~Z: CHECKS-OK 20 of 20, rc 0"
  ],
  "remedy": "The STUBS entry landed (Z-W3-S3); green at the PROD-contained build.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v21",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~D",
   "at": "2026-10-02T05:17Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D",
   "round": "v21"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-W3-S2",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "tabs.harness.cjs's thesis_sentences_and_one_chart was anchored to the pre-card Thesis face and read CHECKS-WRONG-WAY (19 of 20).",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-W3-S2",
   "tabs.harness.cjs at portal 24646bca, this seat's run: thesis_sentences_and_one_chart true, CHECKS-OK 20 of 20"
  ],
  "remedy": "Re-anchored to the face plus each card window body.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v21",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~D",
   "at": "2026-10-02T05:17Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D",
   "round": "v21"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-W28-S1",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "SKILL.md documented walker flags (--thread, lead-lists.json, <sec>-timeline-day / -event) that walk.mjs rejected.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-W28-S1",
   ".claude/skills/ui-walk/walk.mjs:40 parses --thread; tmp/ui-walk/20261001T164049Z/ holds lead-lists.json and timeline-days.json"
  ],
  "remedy": "The walker code was re-landed (Z-S4); the flags are accepted and used.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v21",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~D",
   "at": "2026-10-02T05:17Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D",
   "round": "v21"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-S3",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A walk whose session was lost kept stepping on the sign-in page and printed '0 finding(s)' per step.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-S3",
   "deliverables/2.0.0_SA_COO~D/round21/ROUND21_CLOSE.md: 'walk void: no' (the walk now grades its own voidness)"
  ],
  "remedy": "The walk carries a void verdict; a session loss voids the walk instead of reading clean.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v21",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D",
   "round": "v21"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-S4",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "An integrator merge resolved walk.mjs to one side and dropped rounds 4-7 walker features.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-S4",
   ".claude/skills/ui-walk/walk.mjs:40 (--thread present at CLOUD a9f4fdc548)"
  ],
  "remedy": "Restored by a three-way merge onto HEAD.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v21",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D",
   "round": "v21"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-S6",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "Three 0x08 control bytes in the page source (Z-S5).",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-S6",
   "git show b3a1d8a6:<f> over 77 files under src/pages/SecurityAnalysis: 0 contain 0x08"
  ],
  "remedy": "Replaced with a word boundary (AV-o-3 AMENDMENT 1); bytes.cjs guards a reintroduction.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v21",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D",
   "round": "v21"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-S7",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Served dossier reasons were carried verbatim, so producer diagnostics (section names, class letters, a fund-token regex) reached the face.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-S7",
   "portal/src/pages/SecurityAnalysis/reasonWords.ts:3-38 (in PROD) maps class A/B, ALL-CAPS section names and the fund-token list to words",
   "tmp/ui-walk/20261001T164049Z/shots/019-BA-US-Exec-Management.png: 'no management section, because neither a research pack nor an earnings update is on file'"
  ],
  "remedy": "Pattern mapping for dossier reasons. The same class survives on a reason that bypasses it: the Lusha line (ExecManagementTab.tsx:317), carried in section 1 FWD-11.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v21",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D",
   "round": "v21"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-S8",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The Posture compare call keyed on the display ticker and the route answered 500.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-S8",
   "tmp/ui-walk/20261001T164049Z/netlog.tsv: GET /api/scoped/amgt/security/{AMD,BA,TSM}%20US/compare 44 of 44 status 200"
  ],
  "remedy": "The route answers the display ticker; 0 non-200 on the round-21 walk.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v21",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D",
   "round": "v21"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-S11",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "walk.mjs's occluded-popover check uses document.elementFromPoint, which skips pointer-events-none elements, so every open tooltip reads covered.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-S11",
   ".claude/skills/ui-walk/walk.mjs:102-111",
   "round21 hoverprobe BA 13 of 13, AMD 10 of 10 with the corrected hit-test"
  ],
  "remedy": "OPEN: the hit-test with the popover subtree's pointer events on (hoverprobe.mjs's method) moves into walk.mjs; one instrument batch cell or the ui-walk skill owner.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v21",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v21"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-W12-S1",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "exec.cjs arm A could not reach 3 of 3 until AV-r-1's IdentityLine landed.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-W12-S1",
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-W12-S2 (3 of 3 after the drain)"
  ],
  "remedy": "Cleared by the drain order.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v21",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D",
   "round": "v21"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-W12-S2",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The resolution record of W12-S1.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-W12-S2"
  ],
  "remedy": "exec.cjs 3 of 3, exit 0, on the drained base.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v21",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D",
   "round": "v21"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-W13-S1",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Git Bash rewrote --route /security-analysis into a Windows path, so page.goto received an invalid URL.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-W13-S1"
  ],
  "remedy": "walk.mjs strips a leading drive-and-Git prefix from --route; walkvoid.sh reads YES.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v21",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D",
   "round": "v21"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-W2-S2",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A static HeroDialog import made tabs.harness.cjs unloadable (no stub); the cell loaded it lazily instead.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-W2-S2",
   "tabs.harness.cjs CHECKS-OK 20 of 20 at portal 24646bca (this seat's run)"
  ],
  "remedy": "The stub landed (Z-W3-S3); the harness loads the page.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v21",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D",
   "round": "v21"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-W23-S1",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "modelPattern.harness.cjs negative_values_signed anchored on a markup shape the cell removed.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-W23-S1",
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-W23-S3"
  ],
  "remedy": "Re-anchored under the issuer's AMENDMENT 1.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v21",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D",
   "round": "v21"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-W23-S2",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "attrs.cjs arm 3 compared against a snapshot taken before AV-u-2 changed the posture words.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-W23-S2",
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-W23-S3"
  ],
  "remedy": "The base snapshot was re-taken under AMENDMENT 1.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v21",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D",
   "round": "v21"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-W23-S3",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The resolution record of W23-S1 and W23-S2.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-W23-S3"
  ],
  "remedy": "Every AV-u-5 criterion green after the grant.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v21",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D",
   "round": "v21"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-W3-S3",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The worker's disarm record of W3-S1 and W3-S2 (portal 36485a07).",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-W3-S3",
   "tabs.harness.cjs CHECKS-OK 20 of 20 at portal 24646bca (this seat's run)"
  ],
  "remedy": "Holds at the PROD-contained build.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v21",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D",
   "round": "v21"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-W47-S1",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "timelineFourStates.harness.cjs's loader had no './publisherNames' branch.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-W47-S1",
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-W47-S2"
  ],
  "remedy": "The one loader line landed under AMENDMENT 1; Q3 reads 4 of 4.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v21",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D",
   "round": "v21"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-W47-S2",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The resolution record of W47-S1.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-W47-S2"
  ],
  "remedy": "AC2 4 of 4.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v21",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D",
   "round": "v21"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-W56-S4",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "errorEmpty's starred-case checks (unresolved_row_navigates, a_click_sent_a_ticker, error_claims_no_daily_row) pass by absence since StarredList left the chatter face.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-W56-S4"
  ],
  "remedy": "OPEN: retire the StarredList claims or re-point them at the bubbles' starred empty state; one instrument batch cell.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v21",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v21"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-W8-S2",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Posture F: cites could print a vendor mnemonic, a preset code and an 'UNRESOLVED: <key>' comparable fallback.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-W8-S2",
   "tmp/ui-walk/20261001T164049Z/shots/052-BA-US-Posture-expanded.png: cites read 'Revenue, FY2025: 89,463 million'; comparable 'Deere & Company'; no mnemonic, preset code or UNRESOLVED key on the face (person read)"
  ],
  "remedy": "F: cites carry plain line names; the comparable carries its name.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v21",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D",
   "round": "v21"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-W69-S1",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "posture.harness.cjs stubs a hook set that predates useCollectedChatter, so the harness throws TypeError at load and grades nothing; it sits outside every bound, so no gate notices.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-W69-S1",
   "node src/pages/SecurityAnalysis/__harness__/posture.harness.cjs at portal a730d8ce (3.0.0_SA_CVO~Z): rc 1, TypeError (0 , useLeadPanelApi_1.useCollectedChatter) is not a function"
  ],
  "remedy": "OPEN: add the missing hook stub so posture.harness runs, and bring it into a bound so a regression fails a check.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v22",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~D",
   "round": "v22"
  },
  "closed": true
 },
 {
  "id": "DSGN_AMGTV1-Z-S14",
  "project": "DSGN_AMGTV1",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "AV-z-1's page lead-in 'Contact enrichment was skipped for this company' is followed by RESAPP B2's served plain reason, which opens with the same words, so the VLO Exec face prints the fact twice.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-S14",
   "tmp/ui-walk/20261002T084927Z/shots/067-VLO-US-Exec-Management.png (read by 3.0.0_SA_CVO~Z)"
  ],
  "remedy": "OPEN: print the served plain reason alone when one is served, the lead-in only when none is.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v23",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D",
   "round": "v23"
  },
  "closed": false
 }
]
```

-- 3.0.0_SA_CVO~Z
