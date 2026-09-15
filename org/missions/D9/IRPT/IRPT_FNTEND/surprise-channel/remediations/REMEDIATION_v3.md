# IRPT_FNTEND -- round 7 remediation slug

Author: 3.0.0_SA_CVO. Round: v7. Fabric: laptop. Recorded: 2026-09-15T02:21:10Z.

Input: `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@32855486f0` (10 rows compiled at this L8). Adjudication: `ADJUDICATION_v2.md` (C-S93..C-S98), same slug. Record: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND7_L8_L9_20260915.md`.

Reader: **1.0.0_SA_CTO only**. No row carries `route` or `loop_target`; the recut is the COO's. One row per graduated item (5); the 5 dismissed rows (C-S94, C-S95) are not here. Every row is OPEN.

```json
[
 {
  "id": "IRPT_FNTEND-W1-S69",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "F45-AC10 names `process.release.name` = `node` as the proof that the dev server runs on node, but bun reports `process.release.name` = \"node\" too. The named field reads the same under both runtimes, so by itself it cannot tell the two apart; the test had to add a discriminator the order did not name.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@32855486f0#IRPT_FNTEND-W1-S69",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S96",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND7_L8_L9_20260915.md (same slug) section 2",
   "C:/Users/AndrewBerman/.bun/bin/bun -e (process.release.name, process.versions.bun) -> {\"rel\":\"node\",\"bun\":\"1.3.9\",\"exec\":\"C:\\\\Users\\\\AndrewBerman\\\\.bun\\\\bin\\\\bun.exe\"}; node -e the same -> {\"rel\":\"node\",\"exec\":\"C:\\\\Program Files\\\\nodejs\\\\node.exe\"}",
   "NODE_OPTIONS='--require \"<WS>/.scratch/rtprobe.cjs\"' node -e 1 -> 'FE45_RUNTIME {...\"release\":\"node\",\"bun\":null...}'; the same under bun -e 1 -> no line, rc 0"
  ],
  "remedy": "A criterion that names a runtime names a reading that DIFFERS under the other runtime (the listener's image name, process.versions.bun absent), never process.release.name alone -- the cut's clause (2.0.0_SA_COO~F) and the adjudication's bar 2 wording (1.0.0_SA_CTO). F45-AC10's verdict stands on the test's added discriminator.",
  "owner": "1.0.0_SA_CTO",
  "round": "v7",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v7"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W3-S33",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Two tests outside FE-s-42's grant sometimes run past bun's 5000 ms default test timeout: F40-AC5 (fe-s-40/window.test.ts) and F41-AC2 (fe-s-41/one-writer.test.ts). Their content passes, but a cell's whole-suite census can then read 1 or 2 fail that it cannot fix inside its own grant.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@32855486f0#IRPT_FNTEND-W3-S33",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S96",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND7_L8_L9_20260915.md (same slug) section 2",
   "Baseline whole suite at workspace 4d11c008c2 with portal 35797660 unmodified, IRPT_FE_DEV_PORT=5269 measured closed: 547 pass, 16 skip, 2 fail of 565, in 49.91 s. The two fails: 'F40-AC5 -- the portal calendar agrees with lib/trading_calendar.py, day by day > every day of the covered years, re-derived from the frontier with is_trading_day [5172.00ms] ^ this test timed out after 5000ms.' and 'F41-AC2 -- the Global map has one writer > CONTROL -- a seeded second writer is found, directly and through a wrapper; a seeded reader is not [5875.00ms] ^ this test timed out after 5000ms.' Each first printed a passing reading: 'TRADING CALENDAR AGREES WITH lib/trading_calendar.py: 1461 of 1461 days (2024-2027)', and the seeded controls found 2 of 149 writers.",
   "Same base, the two files run on their own: 14 pass, 1 fail of 15. F40-AC5 timed out again, at 5735 ms. F41-AC2 passed."
  ],
  "remedy": "Give F40-AC5 (fe-s-40/window.test.ts) and F41-AC2 (fe-s-41/one-writer.test.ts) an explicit per-test timeout sized to their measured cost, in a cell granted those two files, so a loaded box cannot turn a later cell's census red (2.0.0_SA_COO~F at the next cut).",
  "owner": "2.0.0_SA_COO~F",
  "round": "v7",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~F",
   "round": "v7"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W6-S1",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "At base 4d11c008c2 the census of record (F44-AC5, FE-s-37's test_governing_binding.py) read 11 of 12 green. test_seeded_limb.py hit the census's own 560 s per-battery bound (rc=124) while the box was shared. Run alone on 051379eac7, the same battery took 275 s and the census read 12 of 12, with neither tool changed. A load timeout prints RED in the same row shape as a regression.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@32855486f0#IRPT_FNTEND-W6-S1",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S96",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND7_L8_L9_20260915.md (same slug) section 2",
   ".tools/tests/test_governing_binding.py @4d11c008c2 :272 bat_futs = [(p, pool.submit(_run, [sys.executable, str(p)], WORKSPACE, 560)) for p in run] -- the per-battery bound; :85 returns 124, 'TIMEOUT after %d s'.",
   "base run at 4d11c008c2, concurrent: '  RED   rc=124  560 s  test_seeded_limb.py   TIMEOUT after 560 s' / 'EVERY .tools BATTERY THAT CALLS EITHER TOOL: 11 of 12 green' / 'governing-binding battery: 18 of 19 arm(s) as expected (621 s wall)', rc=1."
  ],
  "remedy": "The .tools census (test_governing_binding.py) prints a TIMEOUT distinctly from RED in its summary and sizes its per-battery bound to the lone runtime under load, so rc=124 is never read as a regression (1.0.0_SA_CTO, FE-s-37's checker lineage).",
  "owner": "1.0.0_SA_CTO",
  "round": "v7",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v7"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W3-S35",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A whole v1 directory-search body with NO status member, parsed by the real parseIrEnvelope, yields a DirectoryEntry that the portal's own validateContract refuses: 'availability: state UNCERTAIN carries NEITHER partialReason NOR publicReasonCode'. status is optional on this route, so this is the common path.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@32855486f0#IRPT_FNTEND-W3-S35",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S97",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND7_L8_L9_20260915.md (same slug) section 2",
   "The first draft of __tests__/fe-s-42/every-site.test.ts built its directory body with no status. Run at workspace 4d11c008c2 with portal 35797660, on the committed wire instance fixtures/wire/DirectoryEntry.valid.json['instance'] with only advisory_status changed, validateContract('DirectoryEntry', <adapted entry>) returned [\"DirectoryEntry.availability: state 'UNCERTAIN' carries NEITHER partialReason NOR publicReasonCode\"].",
   "portal@35797660 contracts/adapt.ts:167 EXPLICIT_UNKNOWN_STATE = 'UNCERTAIN'. :228-231 wireEnvelope sets state: parts.state ?? EXPLICIT_UNKNOWN_STATE, with partialReason and publicReasonCode ?? null. contracts/envelope.ts:187 reads statusRequired from RESPONSE_STATUS_REQUIRED, and the comment at :229-232 says '`status_required` is false on ten of the twelve response contracts, so this branch is the COMMON one'."
  ],
  "remedy": "Rule which rule gives on the no-status directory path -- the adapter supplies a reason with its explicit unknown, or validate admits the explicit unknown -- after reading whether any production path runs validateContract on an adapted document (1.0.0_SA_CTO); the recut is 2.0.0_SA_COO~F's.",
  "owner": "1.0.0_SA_CTO",
  "round": "v7",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v7"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W4-S16",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "THE CANONICAL-FLOW SKILL STILL DOCUMENTS THE ONE-ARGUMENT RECEIVING CALL AND THREE VERDICTS. After FE-s-43 (e21a8c6116) a proof-of-spec instance received that way reads NOT-BOUND (rc 1) and nothing runs; the skill needs the --governing-order form for L7->L8 and a NOT-BOUND verdict row. Exact change below, for the skill's owner.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@32855486f0#IRPT_FNTEND-W4-S16",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row IRPT_FNTEND-C-S98",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND7_L8_L9_20260915.md (same slug) section 2",
   ".claude/skills/canonical-flow/SKILL.md:352-354 @4d11c008c2 -- the one documented call, `.tools/receiving-check.py <the artifact your limb consumes>`",
   ".claude/skills/canonical-flow/SKILL.md:368-374 @4d11c008c2 -- 'THE THREE VERDICTS', table rows ACCEPT / HAND BACK / UNCHECKED"
  ],
  "remedy": "Apply the row's three edits to .claude/skills/canonical-flow/SKILL.md Step 3b: the --governing-order line for L7->L8, a NOT-BOUND verdict row, and 'THE FOUR VERDICTS' (the skill's owner, 1.0.0_SA_CTO).",
  "owner": "1.0.0_SA_CTO",
  "round": "v7",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v7"
  },
  "closed": false
 }
]
```
