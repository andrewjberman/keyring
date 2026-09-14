# IRPT_FNTEND -- round 6 remediation slug

Author: 3.0.0_SA_CVO. Round: v6. Fabric: laptop. Recorded: 2026-09-14T19:48:12Z.

Input: `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54` (21 rows compiled at this L8). Adjudication: `ADJUDICATION_v2.md` (C-S87..C-S92), same slug. Record: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND6_L8_L9_20260914.md`.

Reader: **1.0.0_SA_CTO only**. No row carries `route` or `loop_target`; the recut is the COO's. One row per graduated item (10); the 11 dismissed rows (C-S88, C-S89) are not here. Every row is OPEN.

```json
[
 {
  "id": "IRPT_FNTEND-W4-S14",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "THE L8 RECEIVING SIDE STILL GRADES A PROOF UNBOUND. After FE-s-37 the complete flip is bound, but every other executing caller of proof-of-spec-check.py passes the instance alone -- receiving-check.py's L7->L8 route and 3.0.0_SA_CVO's own intake/audit scripts -- so their verdicts are still resolved from the instance's own to_ref.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W4-S14",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S90",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND6_L8_L9_20260914.md (same slug) section 2",
   ".tools/receiving-check.py:71 and :117 @adfbe65590",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/amgt_round5_cvo_audit.py:54,:84; amgt_round6_cvo_audit.py:41; amgt_round7_cvo_intake.py:80; amgt_round8_cvo_intake.py:107; posn_round3_cvo_intake.py:47 @da3e61889d"
  ],
  "remedy": "Each caller derives the sibling order from the instance path and passes --governing-order (receiving-check.py: 1.0.0_SA_CTO's tool; the CVO scripts: this seat, who already passes it from round 6); diagnose the artifact-coverage battery's must-VALID arms (1.0.0_SA_CTO, org/standards); F41-AC5 reads the committed blob as F41-AC4 now does (2.0.0_SA_COO~F at the next cut).",
  "owner": "1.0.0_SA_CTO",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v6"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W4-S15",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A CHECKER BATTERY OUTSIDE .tools/tests/ IS RED AT THE CUT. org/standards/test_artifact_coverage_both_grammars.py runs proof-of-spec-check.py and reads 3/6 PASS (rc=1) both at CLOUD 62f3adb8ca and with FE-s-37 applied -- the same failing arms (A-DS-GRAMMAR-STILL-PASSES, B-WP1-GRAMMAR-FLIPS, E-EXPLICIT-FIELD-PASSES) -- a pre-existing red that F37-AC8's census domain cannot see.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W4-S15",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S90",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND6_L8_L9_20260914.md (same slug) section 2",
   "org/standards/test_artifact_coverage_both_grammars.py:30,:67 @ba59c67ada",
   "run with FE-s-37 applied (checker at da3e61889d): rc=1, 3/6 PASS, FAIL A-DS-GRAMMAR-STILL-PASSES, B-WP1-GRAMMAR-FLIPS, E-EXPLICIT-FIELD-PASSES"
  ],
  "remedy": "Each caller derives the sibling order from the instance path and passes --governing-order (receiving-check.py: 1.0.0_SA_CTO's tool; the CVO scripts: this seat, who already passes it from round 6); diagnose the artifact-coverage battery's must-VALID arms (1.0.0_SA_CTO, org/standards); F41-AC5 reads the committed blob as F41-AC4 now does (2.0.0_SA_COO~F at the next cut).",
  "owner": "1.0.0_SA_CTO",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v6"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W5-S7",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "F41-AC5 says it reads the COMMITTED frozen map, but its test reads the five frozen-map descendants AS CHECKED OUT (loadJson of the working copy). This is the same gap between the working copy and the committed object that row S64 found in F41-AC4, on a second criterion. JSON.parse ignores line endings, so a CRLF checkout cannot turn it red. An UNCOMMITTED in-place edit of those maps is read as if it were committed. Amendment 2 scoped the fix to F41-AC4 and its CONTROL, so AC5 was left as it is.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W5-S7",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S90",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND6_L8_L9_20260914.md (same slug) section 2",
   "portal/src/pages/InvestorReporting/__tests__/fe-s-41/one-writer.test.ts @portal 87f83b86: loadJson = JSON.parse(readFileSync(path, 'utf8')) at :71-73; the AC5 BOUND test maps FROZEN_MAPS through loadJson(`${SMOKE}${name}`) at :600; SMOKE is fixtures/smoke/ of the checkout (:50).",
   "git -C portal ls-files --eol over fixtures/smoke/ and __tests__/fe-s-32/holdings-no-answer.json on this worktree: every map reads i/lf w/crlf, the five FROZEN_MAPS among them; core.autocrlf=true; portal/.gitattributes absent."
  ],
  "remedy": "Each caller derives the sibling order from the instance path and passes --governing-order (receiving-check.py: 1.0.0_SA_CTO's tool; the CVO scripts: this seat, who already passes it from round 6); diagnose the artifact-coverage battery's must-VALID arms (1.0.0_SA_CTO, org/standards); F41-AC5 reads the committed blob as F41-AC4 now does (2.0.0_SA_COO~F at the next cut).",
  "owner": "1.0.0_SA_CTO",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v6"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W1-S63",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "vite's config loader still writes through the node_modules junction: every dev-server start and every resolveConfig bundles vite.config.ts into the MAIN checkout's portal/node_modules/.vite-temp. That is a third junction write, which RULING U's remedy (cacheDir + tsBuildInfoFile) does not reach and no config key can move.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W1-S63",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S91",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND6_L8_L9_20260914.md (same slug) section 2",
   "C:/Users/AndrewBerman/Desktop/ajb_workspace/portal/node_modules/vite/dist/node/chunks/config.js:35985-35993 (vite 7.3.5): nodeModulesDir = findNearestNodeModules(...); mkdir .vite-temp/; tempFileName under it",
   "ls --time-style=full-iso .../portal/node_modules/.vite-temp: 2026-09-14 13:03 -0400 after this worker's dev-server start, 13:07:03.534 -0400 after its resolveConfig (bundle) run; empty both times"
  ],
  "remedy": "A cleanup cell: retire the two overrides, correct the comment, and either move the dev script to the runner loader (fixing __dirname) or record the transient temp write as accepted under RULING U.",
  "owner": "2.0.0_SA_COO~F",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~F",
   "round": "v6"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W1-S64",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "fe-s-19/mounted-from-wire.test.ts's header still says the port comes from the helper 'environment first, documented default second'. After RULING U the helper has no default (env, else derived from the worktree, else REFUSED), so the comment now misdescribes it, and the file is outside this order's grant.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W1-S64",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S91",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND6_L8_L9_20260914.md (same slug) section 2",
   "portal/src/pages/InvestorReporting/__tests__/fe-s-19/mounted-from-wire.test.ts:55-56 @741bb54b",
   "portal/src/pages/InvestorReporting/__tests__/fe-s-27/_dev-server.ts choosePort() @ac13f8ab"
  ],
  "remedy": "A cleanup cell: retire the two overrides, correct the comment, and either move the dev script to the runner loader (fixing __dirname) or record the transient temp write as accepted under RULING U.",
  "owner": "2.0.0_SA_COO~F",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~F",
   "round": "v6"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W1-S65",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Two per-cell vite overrides survive RULING U: fe-s-31/vite.worktree.config.mjs and fe-s-32/vite.worktree.config.ts still merge cacheDir onto <workspace>/.scratch/vite-cache-fe-s-3x. A server started through either one caches in the workspace worktree's .scratch, not in <portal>/.vite where the portal config now puts it, so one worktree can hold two cache homes.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W1-S65",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S91",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND6_L8_L9_20260914.md (same slug) section 2",
   "portal/src/pages/InvestorReporting/__tests__/fe-s-31/vite.worktree.config.mjs:5-8,:39 @741bb54b",
   "portal/src/pages/InvestorReporting/__tests__/fe-s-32/vite.worktree.config.ts:5-10,:50 @741bb54b"
  ],
  "remedy": "A cleanup cell: retire the two overrides, correct the comment, and either move the dev script to the runner loader (fixing __dirname) or record the transient temp write as accepted under RULING U.",
  "owner": "2.0.0_SA_COO~F",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~F",
   "round": "v6"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W3-S29",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "RULING W is applied at ONE of the two ADVISORY_FOR_WIRE use sites. The DirectoryEntry cohort (contracts/adapt.ts:558 at 741bb54b) still maps an out-of-enum advisory_status to 'unknown'. Its view type is CohortValue, which the supervision, billing and advisory axes share and which is not 'the advisory view type', and it is displayed by header/ScopeSummary.tsx, outside the grant.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W3-S29",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S92",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND6_L8_L9_20260914.md (same slug) section 2",
   "portal@741bb54b contracts/adapt.ts:558 'value: ADVISORY_FOR_WIRE[wire.cohort.advisory_status] ?? \"unknown\"' fills CohortFact.value, typed CohortValue (contracts/index.ts:310-326), one union for the supervision, billing and advisory axes. header/ScopeSummary.tsx renders '{c.axis}: {c.value}'. contracts/validate.ts:167 checks a cohort value against COHORT_VALUES.",
   "Measured at the FE-s-39 edit: typing the advisory view value as AdvisoryPartition | OutOfEnumAdvisory through ADVISORY_FOR_WIRE failed the typecheck at this site: 'adapt.ts(583,7): error TS2322: Type AdvisoryValue is not assignable to type CohortValue', rc=2. The table is now typed to its partition members (portal@794d4899), so the directory site behaves as before. Typecheck rc=0 after."
  ],
  "remedy": "A recut cell granted adapt.ts's directory site, the CohortValue type, header/ScopeSummary.tsx, contracts/validate.ts and export/ReceiptPanel.tsx, so the out-of-enum rule and the flag hold everywhere the code prints; fe-s-32's captures written to the running worker's own deliverables.",
  "owner": "2.0.0_SA_COO~F",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~F",
   "round": "v6"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W3-S30",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A second carrier of the Holdings advisory contract disagrees with the new view type. contracts/validate.ts:448 (validateHoldingsSnapshot) refuses any classification.advisory outside advised, residual and unknown, so validateContract would refuse an adapted snapshot that carries a flagged verbatim token. Its only caller validates committed VIEW fixtures, not adapted output.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W3-S30",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S92",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND6_L8_L9_20260914.md (same slug) section 2",
   "portal@741bb54b contracts/validate.ts:448 \"oneOf(c, cp, 'advisory', ['advised', 'residual', 'unknown'], p)\"; :627 validateContract.",
   "Native Grep for imports of contracts/validate across portal/src at portal@794d4899: 1 importer, __tests__/fe-s-1/fixtures.test.ts:23. The whole-suite run with FE-s-39 applied has no failure in fe-s-1."
  ],
  "remedy": "A recut cell granted adapt.ts's directory site, the CohortValue type, header/ScopeSummary.tsx, contracts/validate.ts and export/ReceiptPanel.tsx, so the out-of-enum rule and the flag hold everywhere the code prints; fe-s-32's captures written to the running worker's own deliverables.",
  "owner": "2.0.0_SA_COO~F",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~F",
   "round": "v6"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W2-S33",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "ONE EXPORT SCREEN CAN SHOW THE SAME CODE FLAGGED AND UNFLAGGED. tabs/StatusPanel.tsx, granted and now flagging every code the contract does not name, is rendered inside export/ReceiptPanel.tsx, whose own 'Reason: <code>' line the order puts outside this cell.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W2-S33",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S92",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND6_L8_L9_20260914.md (same slug) section 2",
   "portal src/pages/InvestorReporting/export/ReceiptPanel.tsx:44-48 @741bb54b",
   "portal src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx:231, tabs/holdings/HoldingsTab.tsx:163 @741bb54b (the other StatusPanel callers)"
  ],
  "remedy": "A recut cell granted adapt.ts's directory site, the CohortValue type, header/ScopeSummary.tsx, contracts/validate.ts and export/ReceiptPanel.tsx, so the out-of-enum rule and the flag hold everywhere the code prints; fe-s-32's captures written to the running worker's own deliverables.",
  "owner": "2.0.0_SA_COO~F",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~F",
   "round": "v6"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W3-S31",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "F39-AC8's invocation writes outside this order's grant. The fe-s-32 browser test's driver writes its PNGs and manifest to deliverables/0.9.0_WK_IRPT_FNTEND~2/ (holdings-in-a-browser.test.ts:66-68), so the deciding run modified 9 files in another worker's deliverables folder in this worktree.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W3-S31",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S92",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND6_L8_L9_20260914.md (same slug) section 2",
   "portal@741bb54b src/pages/InvestorReporting/__tests__/fe-s-32/holdings-in-a-browser.test.ts:68 CAPTURES = DELIVERABLES + '0.9.0_WK_IRPT_FNTEND~2/'; :204 hands it to holdings-driver.mjs.",
   "git status after the run, workspace worktree on 1f5d387e17: modified org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/fe-s-32_captures.manifest.json and 8 PNGs, fe-s-32_holdings_{observed,target}_{390,1440}.png and the same four with _table_scrolled."
  ],
  "remedy": "A recut cell granted adapt.ts's directory site, the CohortValue type, header/ScopeSummary.tsx, contracts/validate.ts and export/ReceiptPanel.tsx, so the out-of-enum rule and the flag hold everywhere the code prints; fe-s-32's captures written to the running worker's own deliverables.",
  "owner": "2.0.0_SA_COO~F",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~F",
   "round": "v6"
  },
  "closed": false
 }
]
```
