# IRPT_FNTEND -- round 8 remediation slug

Author: 3.0.0_SA_CVO. Round: v8. Fabric: laptop. Recorded: 2026-09-15T09:57:19Z.

Input: `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@be5a2a5441` (the 18 rows compiled at this L8 against issuance 57cb17e329, plus IRPT_FNTEND-S68, a between-rounds row). Adjudication: `ADJUDICATION_v2.md` (C-S99..C-S107, and C-S108 for S68), same slug. Record: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md`.

Reader: **1.0.0_SA_CTO only**. No row carries `route` or `loop_target`; the recut is the COO's. One row per graduated item (10); the 9 dismissed rows (C-S100..C-S102) are not here.

STATES: 8 rows OPEN. 2 read REMEDIATED -- W1-S74 and W3-S40, the two ARMED rows, whose remedy this seat read in code at portal DEV 90d71d9e; each carries `disarm` DISARMED at that commit's committer time, 2026-09-15T07:51:46Z, under its own row's disarm owner. `closed` stays false on every row: the CTO's round-8 analysis grades the round.

```json
[
 {
  "id": "IRPT_FNTEND-W1-S74",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "F46-AC3's bar can be met only while every recorded cost of a test stays at or under 20000 ms: the timeout must be at least 3 times that cost and at most 60000 ms. On this box F41-AC5's control recorded 8375, then 15234, then 18891 ms, so its timeout (56673 ms) is 3327 ms under the cap. fe-s-46/timeouts.test.ts counts every run it makes as recorded and is itself in every later whole-suite census. A heavier load can therefore read F46-AC3 red there with no file changed, the load-dependent red W3-S33 removes from the two files.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W1-S74",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S103",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md (same slug) section 2",
   "<WS>/.scratch/ac-run-1.txt (timeouts.test.ts at portal 01e5cf3d, rc=1, 228 s): 'IN THE SET :791 ... highest 15234 ms (F46-AC5 AFTER run 3 p0); timeout 25125 ms against floor 45702 ms ... NOT SIZED'; 'EXPLICIT TIMEOUT ON EVERY TEST THAT CAN REACH THE DEFAULT: 1 of 8'",
   "<WS>/.scratch/ac-run-2.txt (portal 904b6c4f, rc=1, 141 s): 'IN THE SET :791 ... highest 18891 ms (F46-AC5 BEFORE run 1 p4); timeout 45702 ms against floor 56673 ms ... NOT SIZED'; '7 of 8'"
  ],
  "remedy": "EXECUTED at portal DEV 90d71d9e (FE-s-46 amendment 1): the load and ledger arms run only with IRPT_FE_TIMEOUT_LOAD=1 (timeouts.test.ts:66) and F46-AC3 reads the committed ledger, so a census measures nothing and cannot turn red by load. RESIDUAL for the round-8 analysis: F41-AC5's control has 3327 ms under the 60000 ms cap, so a committed cost above 20000 ms has no legal timeout (reachable only by an opt-in load run and a commit).",
  "owner": "2.0.0_SA_COO~F",
  "round": "v8",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~F",
   "at": "2026-09-15T07:51:46Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~F",
   "round": "v8"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W3-S40",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "F41-AC5's CONTROL (__tests__/fe-s-41/one-writer.test.ts:791) timed F47-AC9's whole-suite census out at bun's 5000 ms default on 3 of 4 runs, and again when fe-s-41 ran alone. Run 4, at the final portal HEAD f4b9ce89, read 0 fail. Whether a whole-suite census on this base passes depends on the box's load, and fixing that is FE-s-46's cell.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W3-S40",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S103",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md (same slug) section 2",
   "Every run below used IRPT_FE_DEV_PORT=5263, measured closed (ECONNREFUSED) before the run.",
   "Run 1, portal 8243b44b: 564 pass, 18 skip, 3 fail of 585. The three were F41-AC5's CONTROL [6000 ms]; fe-s-13 'producer fixtures' [5265 ms]; and F47-AC6 [10828 ms]. F47-AC6 is this order's own test and is fixed at fffb8454, which reads each committed blob once."
  ],
  "remedy": "EXECUTED at portal DEV 90d71d9e (FE-s-46): F41-AC5's control (one-writer.test.ts:869) carries '}, 56673)' = 3 x its highest ledger cost 18891 ms, as do the other 7 tests that can reach the default.",
  "owner": "2.0.0_SA_COO~F",
  "round": "v8",
  "disarm": {
   "state": "DISARMED",
   "owner": "0.9.0_WK_IRPT_FNTEND~1",
   "at": "2026-09-15T07:51:46Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~F",
   "round": "v8"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-S66",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "Investor Reporting is not Opal-admin gated in the portal at DEV. Both routes and the nav item admit any signed-in user the firm allowlist passes, and FIRM_ALLOWED_PATHS lists /investor-reporting for three partner firms (49financial, inflection, cottonwood). ProtectedRoute's requireAdmin tests role only, so an admin-only gate would still admit a partner firm's admin. Andrew's prod-deploy condition 2 ('Opal Admin gated, no clients') fails until round 8's added cell FE-s-49 lands.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-S66",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S104",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md (same slug) section 2",
   "git show DEV:src/App.tsx (portal DEV 1f3ce9f0): :94 { path: '/investor-reporting', label: 'Investor Reporting', icon: FileText }; :421 <Route path=\"/investor-reporting\" element={<ProtectedRoute><InvestorReporting /></ProtectedRoute>} />; :573 the print route, same shape; :482 <ProtectedRoute requireAdmin> (the admin form); :128 /data-refresh carries requiresAdmin: true; :305-320 the nav filter: firm allowlist, requiresDev, requiresAdmin (role), requiresTier via hasAccess.",
   "git show DEV:src/components/ProtectedRoute.tsx: :19 requireAdmin = false by default; :39-40 if (requireAdmin && user?.role !== 'admin') -> Navigate /market; :44-45 if (requireInternal && claims?.firmId !== 'opal-capital') -> Navigate /market; :57 isPathAllowedForFirm."
  ],
  "remedy": "PORTAL HALF EXECUTED and verified at DEV 10c2f07d (FE-s-49 amendment 1; both routes and the nav carry the CTO's predicate, 0 of 3 partner allowlist entries remain). OPEN HALF: the backend is a FIRM wall, not an admin wall -- a partner firm's admin resolves FIRM_OPERATIONS (resolve.py:186) and would be served its own firm once IRPT_BCKEND B15 builds the routes. 1.0.0_SA_CTO rules, with Andrew's word on condition 2, whether the investor-reporting routes must refuse a non-Opal principal before B15 serves them; no PRD names that outcome today, so a yes is new scope for IRPT_BCKEND.",
  "owner": "1.0.0_SA_CTO",
  "round": "v8",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v8"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W3-S37",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "If a response's status member omits its REQUIRED state, the status's OWN availability keeps wireEnvelope's explicit unknown with no partialReason, and parsed.status.state is undefined. The carry gives the DOCUMENT the reason. The status member is outside FE-s-47's grant, and the F47-AC6 census subtracts this site with the residue printed.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W3-S37",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S105",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md (same slug) section 2",
   "F47-AC6 at portal 8243b44b: \"F47-AC6 RESIDUE (off-contract) a status with no state: parsed.status.state undefined; parsed.status.availability {\\\"state\\\":\\\"UNCERTAIN\\\",\\\"partialReason\\\":null,\\\"publicReasonCode\\\":\\\"SOURCE_PARTITION_INCOMPLETE\\\"}\".",
   "portal@8243b44b contracts/envelope.ts:191 adapts ANY record status with adaptStatusEnvelope. adapt.ts:552 passes wireEnvelope state: STATE_FOR_WIRE[wire.state], and adapt.ts:559 sets the top-level state from the same lookup. wireEnvelope's default is adapt.ts:237."
  ],
  "remedy": "Rule whether a status member with no state carries NO_STATUS_REASON on its own availability (a change to adaptStatusEnvelope, outside FE-s-47's grant) -- the round-8 analysis, as amendment 1 routed it.",
  "owner": "1.0.0_SA_CTO",
  "round": "v8",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v8"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W3-S38",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "On status-summary and status-job with no envelope status, the carry replaces the StatusEnvelope document's own state on its availability with UNCERTAIN. validateContract then reports \"state 'PARTIAL' disagrees with availability.state 'UNCERTAIN'\". The no-status reason now sits on a document whose own data says PARTIAL.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W3-S38",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S105",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md (same slug) section 2",
   "F47-AC7 at portal 8243b44b, for both operations: \"OTHER PROBLEMS (printed, not graded; row IRPT_FNTEND-W3-S38): [\\\"StatusEnvelope[0]: state 'PARTIAL' disagrees with availability.state 'UNCERTAIN'\\\"]\". The availability's partialReason is NO_STATUS_REASON, and its publicReasonCode is SOURCE_PARTITION_INCOMPLETE.",
   "portal@1f3ce9f0 contracts/adapt.ts:290: 'state: status?.state ?? EXPLICIT_UNKNOWN_STATE' replaced availability.state for every operation before FE-s-47, including status-summary and status-job (envelope.ts:147-148). FE-s-47 did not change that state rule (adapt.ts:299-301 @8243b44b)."
  ],
  "remedy": "Rule which state wins on status-summary and status-job with no envelope status -- the document's own PARTIAL or the adapter's explicit unknown -- so validateContract stops reporting the disagreement; the round-8 analysis, as amendment 1 routed it.",
  "owner": "1.0.0_SA_CTO",
  "round": "v8",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v8"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W2-S35",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "FE-s-49 amendment 1 keeps fe-s-14's F14-AC3 positive control unchanged, but that control still refuses only the RETIRED expectation (a numstat of '3<TAB>0' against edab15b5), so it no longer bounds the re-pointed diff test, which expects +0 -3 between 1f3ce9f0 and HEAD: a numstat reader stuck at '0<TAB>3' would pass both.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W2-S35",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S106",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md (same slug) section 2",
   "portal 0f674aa9:src/pages/InvestorReporting/__tests__/fe-s-14/allowlist.test.ts:126 expect(line.startsWith('3\\t0\\t')).toBe(false) -- the same line as 1f3ce9f0:src/pages/InvestorReporting/__tests__/fe-s-14/allowlist.test.ts:110",
   "portal 0f674aa9:src/pages/InvestorReporting/__tests__/fe-s-14/allowlist.test.ts:102 the re-pointed test's git form (1f3ce9f0 HEAD, committed trees), against the control's :120 (edab15b5, working copy)"
  ],
  "remedy": "Re-point F14-AC3's positive control in fe-s-14/allowlist.test.ts so it refuses the re-pointed test's own expectation from a constant reader (it refuses '3\\t0\\t' only today), in the next cell granted that file.",
  "owner": "2.0.0_SA_COO~F",
  "round": "v8",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~F",
   "round": "v8"
  },
  "closed": true
 },
 {
  "id": "IRPT_FNTEND-W3-S41",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "proof-of-spec-check's COUNT-BAR limb reads the digit that ends a criterion id as a count. The printed line 'F47-AC2 PROBLEMS: []' matched as the nonzero count '2 PROBLEMS' beside F47-AC2's zero-count bar, and the instance was refused. The test's output label now puts no digit before the noun.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W3-S41",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S106",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md (same slug) section 2",
   "Checker run at workspace e2d9f703e9, checker-vintage da3e61889d, bound with --governing-order to the FE-s-47 order: \"VIOLATION: count-bar[F47-AC2]: the bar 'A NO-STATUS DIRECTORY BODY THROUGH parseIrEnvelope AND validateContract READS 0 PROBLEMS: yes' asserts ZERO of 'problem' and its own search DOES match the evidence -- but the evidence also carries a NONZERO count for that noun: '2 PROBLEMS'.\" Verdict: INVALID (rc=1).",
   ".tools/proof-of-spec-check.py:1529 @e2d9f703e9: pat = re.compile(r\"(?<![0-9.])(?<!of )([0-9]+)[ \\t]+\" + re.escape(stem) + r\"[A-Za-z_()]*\", re.I). A letter before the digit passes both lookbehinds, so 'AC2 PROBLEMS' yields the count '2'."
  ],
  "remedy": "The COUNT-BAR limb's lookbehind (.tools/proof-of-spec-check.py:1529) also excludes a digit preceded by a letter or '-', with a battery arm: 'F47-AC2 PROBLEMS: []' reads clean and '2 PROBLEMS' is still refused (the checker's owner, FE-s-37's lineage).",
  "owner": "1.0.0_SA_CTO",
  "round": "v8",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v8"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W4-S19",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The ruling's reach, one surface over: Holdings renders a NON-AUTHORITATIVE classification's supervision and advisory partitions as 'unknown' (tabs/holdings/slices.ts:100-102 @1f3ce9f0). That is the same withheld-by-authority shape the header now words as 'withheld'. It is not a CohortFact, this order excludes slices.ts, and the contract's own comment mandates 'unknown' there, so it is left as it is and placed here for the ruling's owner.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W4-S19",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S107",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md (same slug) section 2",
   "git cat-file blob 1f3ce9f0:src/pages/InvestorReporting/tabs/holdings/slices.ts :100 `export function renderedClassification(...)`, :102 `return { supervision: 'unknown', advisory: 'unknown', authoritative: false }`",
   "git cat-file blob 1f3ce9f0:src/pages/InvestorReporting/contracts/index.ts :708 `/** False => render every partition above as unknown. */`"
  ],
  "remedy": "Rule whether RULING W reaches Holdings' non-authoritative classification (slices.ts:102 'unknown', mandated by the contract's comment); if it does, the contract comment and slices.ts change in one cell.",
  "owner": "1.0.0_SA_CTO",
  "round": "v8",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO",
   "round": "v8"
  },
  "closed": true
 },
 {
  "id": "IRPT_FNTEND-W4-S20",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The fixture registry still describes directory.unknown-cohort.json as 'a non-authoritative cohort fact -- unknown renders as unknown, never as false and never as Client' (fixtures/index.ts:77). After FE-s-48 the header renders that fixture's three axes as 'withheld'. The prose is stale, and fixtures are outside this order's grant.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W4-S20",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S107",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md (same slug) section 2",
   "git cat-file blob 1f3ce9f0:src/pages/InvestorReporting/fixtures/index.ts :77 (the proves string, verbatim above)",
   "fe-s-48/withheld.test.ts F48-AC2 arm 1: RENDERED \"Cohort (not asserted)\": \"supervision: withheld, billing: withheld, advisory: withheld\""
  ],
  "remedy": "Reword fixtures/index.ts:77's `proves` to the render after FE-s-48 (the header reads the fixture's axes as 'withheld'), in the next cell granted the fixture registry.",
  "owner": "2.0.0_SA_COO~F",
  "round": "v8",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~F",
   "round": "v8"
  },
  "closed": true
 },
 {
  "id": "IRPT_FNTEND-S68",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "F25-AC8 (fe-s-25/generator.test.ts:79) grades the CHECKOUT'S LINE ENDINGS, not the contract. gen-wire.ts hashes the raw worktree text of the schema, and the committed wire header carries the hash of a CRLF checkout (c83ce02d). So the test passes on a CRLF checkout (this seat's untouched pair, 4/0) and fails on an LF one (the main workspace worktree; 0.0.0_AB_MSTR's promote runs, msg 97009), with identical contract content and identical generated types.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@be5a2a5441#IRPT_FNTEND-S68",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S108",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md (same slug) section 2",
   "sha256sum of the schema in both checkouts, and tr -d '\\r' | sha256sum: pair c83ce02d14c1 raw / f06c0029cd20 normalized; main worktree f06c0029cd20 / f06c0029cd20; git ls-files --eol: pair 'i/lf w/crlf', main 'i/lf w/lf'",
   "git show 10c2f07d:src/pages/InvestorReporting/contracts/wire/StatusEnvelope.ts:5 'Source sha256: c83ce02d14c1...'"
  ],
  "remedy": "Cell (A): gen-wire.ts normalizes CRLF to LF before it hashes the schema text, and the committed wire headers are regenerated, so F25-AC8 reads the same on an LF and a CRLF checkout. 2.0.0_SA_COO~F (97028) routed it to 1.0.0_SA_CTO's ROUND-8 ANALYSIS; round 9's one issuance carries it. 1.0.0_SA_CTO (97020): the promote proceeds with F25-AC8 named.",
  "owner": "1.0.0_SA_CTO",
  "round": "v8",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO",
   "round": "v8"
  },
  "closed": true
 }
]
```

## Round 9 closure note (3.0.0_SA_CVO, 2026-09-21T19:00:39Z)

Four rows above (`IRPT_FNTEND-W2-S35`, `IRPT_FNTEND-W4-S19`, `IRPT_FNTEND-W4-S20`, `IRPT_FNTEND-S68`) close this round: `remediation.state` OPEN -> REMEDIATED, `closed` false -> true, nothing else changed (the gate's own admitted move). Full disposition, evidence and the closing cell for each: `ADJUDICATION_v3.md` (same slug), section 4. `IRPT_FNTEND-W3-S41` is untouched -- no round-9 cell reaches `.tools/proof-of-spec-check.py`; it stays OPEN.

Two NEW remediation rows are minted in `REMEDIATION_v6.md` for round 9's own ARMED findings (`IRPT_FNTEND-W3-S43`, `IRPT_FNTEND-W8-S2`) -- new ids, not a mutation of this file.
