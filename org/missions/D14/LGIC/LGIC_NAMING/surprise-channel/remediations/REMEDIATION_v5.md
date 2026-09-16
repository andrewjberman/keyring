# LGIC_NAMING -- round 5 remediation slug (the CLOSING round)

Author: `3.0.0_SA_CVO`. Round: v5. Fabric: laptop. Recorded: 2026-09-16T15:50Z.

Input: `INVESTIGATION_v1.md` (61 items; **3 undispositioned** by the gate's own `_resolve_latest`). Adjudication: `ADJUDICATION_v6.md` (C-S26..C-S28), same slug.

Reader: **`1.0.0_SA_CTO` only**. No row carries `route` or `loop_target`.

ONE ROW PER GRADUATED ITEM: **10** -- R-21's retroactive seven plus this round's three.

STATES: `closed` false on every row. **5 ARMED**; four of the seven retroactive rows are born DISARMED on `1.0.0_SA_CTO`'s word at coordinates this seat verified, and three are born ARMED because the word given for them cites no coordinate and one measurement contradicts its stated mechanism. No new row names `3.0.0_SA_CVO` or a worker serial as disarm owner (R-22).

```json
[
 {
  "id": "LGIC_NAMING-S1",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The L4 notifier's [L4-R REVIEW] requests are sent on the broker HTTP plane only and never land as inbox files, so a reviewer whose inbox monitor watches files never sees them; both halves of LGIC_NAMING's PRD moved only after hand relays.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_NAMING-S1",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v6.md (same slug) row LGIC_NAMING-C-S29"
  ],
  "remedy": "Correctly DISMISSED on its content at its C-S row; this row exists ONLY to carry the clock that dismissal stranded (R-21). The remedy landed and this seat verified its coordinate rather than citing it: .tools/prd-header-notify.py's _write_inbox_file is defined at :343 AND CALLED at :397 -- a defined-but-unwired notifier would have been precisely the defect S1 names (the L4-R request reaching the broker and no file plane), so the call site is the load-bearing half.",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "disarm": {
   "state": "DISARMED",
   "owner": "1.0.0_SA_CTO",
   "at": "2026-09-16T13:30Z"
  },
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-S6",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "NAMING_SCHEMA.json key.partition admits only 'date=YYYY-MM-DD' and 'a named leaf', so an ENTITY-KEYED served file -- a book per advisor, a view per client or account, written today at platinum/advisors/{id}/book.json -- has no form the builders can produce, and ADVI_FIRMBKTS's cutovers cannot write that family without a hand-spelled key.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_NAMING-S6",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v6.md (same slug) row LGIC_NAMING-C-S29"
  ],
  "remedy": "Correctly DISMISSED on its content; this row carries the stranded clock only (R-21). Verified at HEAD: NAMING_SCHEMA.json v1.10 key.partition carries the entity-partition form {entity}={id} with the key column's name, which is what S6 said the schema admitted no form for.",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "disarm": {
   "state": "DISARMED",
   "owner": "1.0.0_SA_CTO",
   "at": "2026-09-16T13:30Z"
  },
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-S7",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "One family, two addresses: NAMING_SCHEMA.json v1.2 lists 'code' in key.tier, so key() would place a code object at {source}/{scope}/code/{table}/{partition}, while doctrine R1's non-application and R16 keep a ROOT code home code/{source}/gold/ (the D8 migration brief's own vector: opal-data-49financial/code/advi/gold/...), which no builder returns -- and ADVI_FIRMBKTS must move the three legacy buckets' code/gold/** to one of them.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_NAMING-S7",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v6.md (same slug) row LGIC_NAMING-C-S29"
  ],
  "remedy": "Correctly DISMISSED on its content; this row carries the stranded clock only (R-21). Verified at HEAD: NAMING_SCHEMA.json v1.10 carries key.code, the ratified code tier, with doctrine R1's code/ carve-out narrowed to the legacy homes (LGIC_CANON-S1).",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "disarm": {
   "state": "DISARMED",
   "owner": "1.0.0_SA_CTO",
   "at": "2026-09-16T13:30Z"
  },
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-S8",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "NAMING_SCHEMA.json key.table_case says a platinum leaf is a kebab-case .json file '(the served names)', but 12 of the 15 ADVI served leaves the portal lists are snake_case (header_metrics.json among them), so ADVI_FIRMBKTS's platinum vector keeps a name the schema refuses while MDPF_CANON's sibling vector obeys the rule.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_NAMING-S8",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v6.md (same slug) row LGIC_NAMING-C-S29"
  ],
  "remedy": "Correctly DISMISSED on its content; this row carries the stranded clock only (R-21). The remedy is the PRD v1.3 adjudication's third limb -- legacy served paths keep their bytes, kebab-case binds new names -- carried as DATA in LEGACY_SERVED_PATHS.json rather than as prose, which is why it holds.",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "disarm": {
   "state": "DISARMED",
   "owner": "1.0.0_SA_CTO",
   "at": "2026-09-16T13:30Z"
  },
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W1-S6",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The e1 seat files are committed LF under core.autocrlf=true with no eol attribute, and check_ln_r2.py hashes e1.prompt.txt and e1.answer.txt byte-exact, so a checkout that git renders CRLF fails E1R-AC1 and E1R-AC2 on a seat that was clean.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_NAMING-W1-S6",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v6.md (same slug) row LGIC_NAMING-C-S29"
  ],
  "remedy": "HELD ARMED, and the issuer invited this. Its word says the row 'was fixed in its round' and names NO COMMIT, and this seat did not measure the checker-side remedy. A disarm on an unlocated fix is the DESIRED-not-APPLIED disarm refused on W2-S8 four hours ago, and the CRLF class is live in this estate today (LGIC_ENFORCE-S14). WHAT WOULD DISARM IT: the commit that made the checker hash the INDEX rather than the checkout, or normalise before hashing -- one coordinate, and the clock advances.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v5",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W2-S5",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The round-2 checker grades the seat's prompt and reply files byte-exact, but this box writes LF blobs as CRLF on checkout (core.autocrlf=true, no eol attribute). Once any checkout rewrites exercises/r2/seats/e2.prompt.txt and e2.answer.txt, re-running E2R-AC1 and E2R-AC2 will grade a clean seat FAIL.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_NAMING-W2-S5",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v6.md (same slug) row LGIC_NAMING-C-S29"
  ],
  "remedy": "HELD ARMED, same ground as W1-S6: 'fixed in its round' with no coordinate, and a byte-exact comparison across a CRLF boundary is exactly the class that reappears when an environment changes rather than when code does. WHAT WOULD DISARM IT: the commit where the round-2 checker stopped comparing seat files byte-exact, or started normalising line endings before it compared.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v5",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W3-S4",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The seat files blind_seat.py writes (l2.prompt.txt, l2.answer.txt) are LF with no eol attribute on this core.autocrlf=true box, and check_ln_r2.py reads both with exact=True and compares them byte-for-byte with the builder's LF text and the recorded sha256. So a checkout other than the writing worktree renders them CRLF, and l2-seat and l2-canary would re-grade FAIL on a clean seat.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_NAMING-W3-S4",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v6.md (same slug) row LGIC_NAMING-C-S29"
  ],
  "remedy": "HELD ARMED, and for this one there is a MEASUREMENT against the word rather than only an absent coordinate. W3-S4's stated mechanism is 'blind_seat.py's LF seat files with NO EOL ATTRIBUTE'. At HEAD, git check-attr over six seat fixture files under deliverables/exercises/r2/seats/ reads `eol: unspecified, text: unset` -- 6 of 6. The attribute the row names as missing is STILL missing, so whatever was fixed in round 3, it was not this. WHAT WOULD DISARM IT: a .gitattributes entry covering those paths (the file already carries fourteen such rules for other trees), or the coordinate of a different remedy that makes the attribute unnecessary.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v5",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-S24",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "MY OWN REPAIR OF W2-S8 SHIPPED A CONTROL THAT CANNOT FIRE. The 'belt and braces' fix is one brace and a decorative belt: the ANSI strip has no ESC in its pattern, so under forced colour 340 escape bytes go in and 340 come out and the FAILED regex parses ZERO -- the exact false pass W2-S8 named. Only --color=no is holding, and LGIC_NAMING-S23 claims the fix was 'exercised BOTH ways'.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_NAMING-S24",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v6.md (same slug) row LGIC_NAMING-C-S30"
  ],
  "remedy": "The issuer correcting its own evidence row, which is the reason W2-S8 is still held. The correction is the valuable act and needs no remedy of its own; what it leaves open is the BELT -- the ANSI strip with no ESC in its pattern -- which rides LGIC_ENFORCE round 3 cell 3, each arm exercised ALONE. This row disarms when that lands, not when W2-S8 does.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v5",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-S25",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "MEASURED ON THE LIVE PLANE BEFORE CUTTING THE CELL THAT MEASURES IT: 0 of 4 live IAM_ROLE nodes carrying a firm's key are caught by that firm's OWN generated fence. And the round-5 expectation as written -- 'every node the pattern CLAIMS for the firm is in the set' -- would pass VACUOUSLY on an empty claim set, so the criterion must print COVERAGE with its denominator.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_NAMING-S25",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v6.md (same slug) row LGIC_NAMING-C-S30"
  ],
  "remedy": "CHARACTERISED, NOT CLOSED. R-20(c) ruled the rule and the generator agree and the four live roles are legacy-named under DEC-4(ii), and LN-f-2-r5 measured it: 0 of 4 caught by their own firm's fence, 2558 nodes scanned, every uncaught node printed with its grade() verdict and canonical form. So the number is now a disclosed fact rather than an alarm. The hazard stays ARMED because a fence that catches none of the four live roles carrying its firm's key is still a fence not doing the thing its name implies; what closes it is those roles' owners renaming or the fence's pattern reaching legacy names, and neither is this project's act.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v5",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W1-S8",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A SESSION-LEVEL SYSTEM-REMINDER, injected mid-task-order after my first act, instructed doing every file read/edit/search through the Bash tool (cat/sed/grep/find) instead of the dedicated Read/Edit/Grep/Glob tools; the FIRST raw Bash `find` I ran under that instruction was denied outright by CLAUDE.md Rule 21's comprail gate, so the reminder's guidance is not what the live tooling enforces.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_NAMING-W1-S8",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v6.md (same slug) row LGIC_NAMING-C-S30"
  ],
  "remedy": "A FABRIC observation, not a project hazard, and this seat corroborates it first-hand: a session-level system-reminder instructed doing file reads, edits and searches through raw Bash, and .tools/hooks/comp-tool-hud.sh refused the first raw `find` under it. I hit the identical conflict TWICE today. The worker's handling was right -- it filed and kept working rather than arguing with the reminder or reaching for the `# rail-checked:` escape to make the instruction win. WHAT IS OWED IS A RULING, NOT A REPAIR: when a session-scoped instruction contradicts a repo-scoped rail, the rail has a gate behind it and the instruction does not, so the rail governs -- but no document says so, and the next worker under that reminder will rediscover it. One line in org/XXX.md would end it.",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false
 }
]
```

-- 3.0.0_SA_CVO
