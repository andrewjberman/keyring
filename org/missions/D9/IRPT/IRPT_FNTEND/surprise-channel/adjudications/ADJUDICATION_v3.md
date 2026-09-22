# IRPT_FNTEND round 9 -- CVO adjudication (L9)

Author: `3.0.0_SA_CVO`. Round: 9. Fabric: laptop. Input: the L8 hand-off msgs `99139` (corrected by
`99140`) from `2.0.0_SA_COO~F` -- 11 cells (`FE-s-50`..`FE-s-60`) terminal, both waves drained, decomposition
cut `6f56917cef`, issuance `07faf174d2`. File v3 because v1 (88,734 bytes) and v2 (198,485 bytes) both rolled
past ~190 KB; `_vN` is a file-rollover counter and never a round number. Workspace HEAD at write time
`be8101cd50`; portal DEV (frozen) `f4c9ec46`.

## 1. Terminality, verified on two independent instruments

- `python .tools/to-check.py --project IRPT_FNTEND` reads **0 active TOs** (the issuer's own reading).
- `surprise_row_gate._open_tos_for_project('.', 'IRPT_FNTEND')` reads **`([], 60, '')`** -- 0 open of 60
  scanned, empty note (no widening flag, no terminality caveat).

Both agree, cleanly: round 9 is genuinely terminal. No hygiene note is owed (unlike IRPT_BCKEND round 7's
proof-vs-status-word gap; nothing analogous was found here).

## 2. The eleven JUDGMENT criteria

Each criterion below is a judgment call a task order could not reduce to an invocation and an expectation;
none was self-graded by its worker. Independently re-verified against live `portal/` source at HEAD
(`f4c9ec46`) rather than trusted from worker or COO prose -- the whole-suite claim (612 pass / 22 skip / 0
fail) and `tsc -b --noEmit` (rc=0) were both re-run and matched exactly.

| criterion | cell | verdict | basis |
|---|---|---|---|
| F50-AC5 | gen-wire CRLF-independent hash | **PASS** | `stableTextForHash()` at `gen-wire.ts:118-125` is the single normalization point, called at all 4 sites (`:304,376,384,498`); regenerated wire diff is exactly the `Source sha256:` lines. Own test: 4/4 SAME HASH AT CRLF AND LF. |
| F51-AC5 | carried-hunks ancestry-aware | **PASS** | Reuses the file's existing git-read helper; `admin-gate.test.ts:591-594` fails loudly on any unrelated hunk neither branch names, confirmed with a mutant control (inverted ternary fails as expected). |
| F52-AC6 | 5 lint errors, portal DEV green | **PASS, with a caveat named at W3-S43** | The 5 named errors (alias-probe, unused import, ExportButton immutability, 2 SentimentGauge imports) are genuinely fixed and behaviorally sound. `bun run lint` itself is NOT a stable signal on this box right now -- 66 unrelated errors from `.vite/deps_temp_*` bundle noise, independently reproduced live; this is `W3-S43`, escalated to INCIDENT below, and does not fail this cell's own delivered fix. |
| F53-AC5 | status envelope NO_STATUS_REASON | **PASS** | `adapt.ts:602` carries the exact fix; the worker's own correctly-refused residual (matching a since-fixed sibling) is confirmed resolved upstream by an independent 35-test re-run (0 fail). |
| F54-AC6 | status document's own stated state | **PASS** | First-act trace found 0 production render sites for the named functions (confirmed); real gap traced one level up into `carryAvailabilityFromStatus`; fix (`IR_STATUS_DOCUMENT_OPERATIONS` / `effectiveStatus`, `envelope.ts:173,268-270`) is grounded in that trace. |
| F55-AC7 | Holdings non-authoritative -> withheld | **PASS** | `slices.ts:121-123` returns `withheld` on all three axes for a non-authoritative classification; `withheld` and an asserted `unknown` do not collapse anywhere in the render path checked. |
| F56-AC6 | fe-s-14 control re-point + fixture prose | **PASS** | Fixture prose at `fixtures/index.ts:77` corrected; the genuinely stale control was in the sibling POSITIVE CONTROL test (not the main diff assertion), fixed by adding the `0\t3` refused-shape assertion, verified with a mutant. A well-executed catch a shallower read would have missed. |
| F57-AC8 | unprojected_grant parse-and-carry | **PASS** | `carryUnprojectedGrant` (`adapt.ts:348-355`) genuinely mirrors `carryAvailabilityFromStatus`'s shape; `UnprojectedGrant` (`index.ts:111`) and the throw/carry logic (`envelope.ts:200,278-282`) confirmed; no `.tsx` touched (rendering correctly deferred to wave B); independent 278/2/0 re-run. |
| F58-AC7 | StatusPanel badge, Global-mode confirmed | **PASS** | `StatusPanel.tsx:88-91` reuses the exact same class idiom as the adjacent pre-existing `reason-code` slot (`:70`) -- literally the same idiom, not merely asserted; Global-mode positive control independently re-verified via the 612/22/0 whole-suite run. |
| F59-AC6 | ScopeSummary badge | **PASS** | `ScopeSummary.tsx:69,111-112` renders as a genuine sibling of the Fact grid via `PartialDisclosureFact` (a real structural separation, not a CSS-only difference); the unrelated `fe-s-48` self-test failure was correctly refused and is disarmed below (`W9-S1`). |
| F60-AC6 | PeriodInContextPage badge, one render both consumers | **PASS, with a color-law question left open by design** | `PeriodInContextPage.tsx:100-109` -- preview and PDF (`PerformanceDocument.tsx`) render strings are byte-identical, mechanically confirming one shared render path. The worker disclosed it has no screenshot capability and used the file's own pre-existing muted-grey classes rather than asserting compliance it could not verify -- correctly disclosed, not papered over. This is left as a genuine open question for the round-9 analysis, not a defect in execution. |

## 3. Two OBSERVATION rows required a CVO read beyond mechanical closure

### 3a. `IRPT_FNTEND-W3-S43` -- ESCALATED FROM EXPOSURE TO INCIDENT

Filed by the round-9 worker: `eslint.config.js`'s `globalIgnores` does not exclude `.vite/**`, so a
transient, gitignored Vite dev-server build cache gets scanned by `bun run lint` and produces spurious
"Definition for rule ... not found" errors. **This seat's own independent re-run, live, at HEAD, found it
firing**: `bun run lint` returned 166 problems (66 errors, 100 warnings), every error sited under
`.vite/deps_temp_*/...js`. Per CLAUDE.md Rule 22's negative mirror -- a hazard that is real is an EXPOSURE
until measured whether it fired, and only then an INCIDENT -- this was measured firing at this L9, not
merely inherited as a claim. Reclassified INCIDENT. Disarm owner unchanged from the filer's own naming
(`1.0.0_SA_CTO`; `eslint.config.js` sits outside this round's grant). Remediation carrier minted in
`REMEDIATION_v6.md`.

### 3b. `IRPT_FNTEND-W8-S2` -- disposition accepted on the merits, filer's citation corrected

`2.0.0_SA_COO~F`'s own drain note (msg 99139) attributes `fe-s-42/_captures.ts`'s deliberate whole-tree,
unscoped `git status --porcelain` read to "RULING X." Independently checked against the file's own header
comment: it names **"RULING AC,"** not RULING X -- RULING X governs an unrelated round-7 test-scoping
census in this same project. The substantive judgment itself (a deliberate design trade-off favoring
false-positive safety over precision under concurrent writes to `deliverables/`, not a code bug) is
corroborated by the file's own docstring independent of which ruling letter is cited, so the disposition
**stands accepted as filed** -- the citation is wrong and is corrected here for the record, not the
underlying call. Left ARMED (a standing, accepted characteristic that will keep occasionally false-failing
under future concurrent writes; nobody intends to fix it, which is a fact about the remedy, not about
whether the hazard is live). Disarm owner: `2.0.0_SA_COO~F` (its own row). Remediation carrier minted in
`REMEDIATION_v6.md`.

## 4. Remediation closures -- four round-8 OPEN rows CLOSE this round

Recorded as an in-place clock advance on `REMEDIATION_v5.md` itself (the gate's own admitted move:
`remediation.state` OPEN -> REMEDIATED, `closed` false -> true, nothing else changed) -- not new rows here.

| row | owner | remedy (as filed) | closes via |
|---|---|---|---|
| `IRPT_FNTEND-S68` | CTO | normalize CRLF before hashing the schema; regenerate wire headers | `FE-s-50`'s `stableTextForHash()`, `gen-wire.ts:118-125` |
| `IRPT_FNTEND-W4-S19` | CTO | rule whether RULING W reaches Holdings' non-authoritative classification | `FE-s-55`'s `slices.ts` `withheld` fix |
| `IRPT_FNTEND-W4-S20` | COO~F | reword the stale fixture prose | `FE-s-56`'s `fixtures/index.ts:77` update |
| `IRPT_FNTEND-W2-S35` | COO~F | re-point F14-AC3's positive control | `FE-s-56`'s added `0\t3` refused-shape assertion |

`IRPT_FNTEND-W3-S41` (CTO, `.tools/proof-of-spec-check.py` lookbehind fix) does **not** close -- no round-9
cell touches that file. Stays OPEN, unchanged.

## 5. FWD status -- no movement claimed, none warranted

Neither the L8 hand-off nor any round-9 investigation row makes an FWD outcome claim, and this project's
prior L9 record (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md`) carries
zero FWD mentions -- unlike IRPT_BCKEND, this project's CVO record has not graded FWD per round. Nothing is
asserted here; inventing movement round 9 never claimed would be exactly the failure mode CLAUDE.md Rule 24
warns against (a claim wider than its evidence).

## 6. What round 9 actually dispositioned (the 17 new rows)

Seven rows were BLOCKING and answered within the round itself (no L9 action needed beyond disposition);
five OBSERVATION rows were INERT at filing and stay INERT; three rows (`W5-S9`, `W8-S1`, `W9-S1`) were
disarmed directly by the issuer, independently confirmed at portal `21d71733` -- `fe-s-32`'s stale `unknown`
assertions now accept `withheld` (F32-AC3/AC5, 2/0) and `fe-s-48`'s positional self-test is re-pinned to its
own landing commit `a06252ee` instead of floating HEAD (4/0), matching the commit's own post-fix number
(606/21/0, consistent with 612/22/0 once F59/F60 added 6 more tests). `W5-S9` and `W8-S1` share one root
cause and one commit, disarmed together.

```json
[
 {
  "id": "IRPT_FNTEND-C-S109",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-21T19:00:39Z",
  "one_line": "ROUND-9 L9, DISMISSED_WITH_REASON -- seven BLOCKING rows, all answered within the round itself: W5-S8 fixed upstream by FE-s-51 (carried-hunks residual), W7-S1/W7-S2 resolved by amendments 1+2 (portal b8c5df09/15ceef79), the remaining four (W3-S42, W4-S21, W4-S22, W4-S77) confirmed INERT by both the issuer and this seat's independent re-check.",
  "class": "OBSERVATION",
  "spec_asserts": "COO~F's L8 hand-off (msg 99139, corrected 99140): '7 BLOCKING, all INERT (all answered within the round)'.",
  "world_is": "Independently re-checked: W7-S1/W7-S2's row text still literally reads hazard_standing ARMED (rows freeze at filing time; they are not self-updating), but the round's own progression is confirmed real -- W7-S1 pre-amendment F57-AC7 failed 52/1err, W7-S2 post-amendment-1 residual down to 5/1err ('status stays open pending further grant widening'), and this seat's own live re-run of the fe-s-57/fe-s-1/fe-s-14 scope at HEAD came back 0 fail, consistent with amendment 2 (W7-S3, portal b8c5df09) closing the remaining residual. W5-S8's upstream fix by FE-s-51 is consistent with F51-AC5's own PASS grade above. Terminality (section 1) confirms 0 open TOs on two independent instruments, so nothing here is silently deferred.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@1605b02ff8#IRPT_FNTEND-W3-S42",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@1605b02ff8#IRPT_FNTEND-W4-S21",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@1605b02ff8#IRPT_FNTEND-W4-S22",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@1605b02ff8#IRPT_FNTEND-W4-S77",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@1605b02ff8#IRPT_FNTEND-W5-S8",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@1605b02ff8#IRPT_FNTEND-W7-S1",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@1605b02ff8#IRPT_FNTEND-W7-S2",
    "2.0.0_SA_COO~F msg 99139/99140 (this L9's own input)",
    "3.0.0_SA_CVO verification fork, live re-run of fe-s-57/fe-s-1/fe-s-14 scope at HEAD, 2026-09-21: 278 pass, 2 skip, 0 fail"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W3-S42",
   "IRPT_FNTEND-W4-S21",
   "IRPT_FNTEND-W4-S22",
   "IRPT_FNTEND-W4-S77",
   "IRPT_FNTEND-W5-S8",
   "IRPT_FNTEND-W7-S1",
   "IRPT_FNTEND-W7-S2"
  ],
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "GRADUATED is reserved for an item that gets a remediation row as its landing surface (the gate's own slug-time rowlessness check). These seven were fully answered within round 9 itself -- no live hazard remains and nothing is carried forward -- so DISMISSED_WITH_REASON is the honest disposition, not GRADUATED.",
  "hazard_standing": "INERT"
 }
]
```

```json
[
 {
  "id": "IRPT_FNTEND-C-S110",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-21T19:00:39Z",
  "one_line": "ROUND-9 L9, DISMISSED_WITH_REASON -- five OBSERVATION rows, INERT at filing and confirmed INERT: W1-S76, W6-S2, W7-S3, W10-S1, W10-S2.",
  "class": "OBSERVATION",
  "spec_asserts": "COO~F's L8 hand-off (msg 99139, corrected 99140): '10 OBSERVATION: 5 INERT (W1-S76, W6-S2, W7-S3, W10-S1, W10-S2) + 5 ARMED [at filing]'.",
  "world_is": "Row text for all five confirmed present in the channel and INERT by this seat's own verification fork, cross-read against the round's terminal test state (612 pass / 22 skip / 0 fail, independently re-run). Nothing in any of the five bears on a judgment criterion graded in section 2 or a remediation closure in section 4.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@1605b02ff8#IRPT_FNTEND-W1-S76",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@1605b02ff8#IRPT_FNTEND-W6-S2",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@1605b02ff8#IRPT_FNTEND-W7-S3",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@1605b02ff8#IRPT_FNTEND-W10-S1",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@1605b02ff8#IRPT_FNTEND-W10-S2",
    "2.0.0_SA_COO~F msg 99139/99140 (this L9's own input)"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W1-S76",
   "IRPT_FNTEND-W6-S2",
   "IRPT_FNTEND-W7-S3",
   "IRPT_FNTEND-W10-S1",
   "IRPT_FNTEND-W10-S2"
  ],
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "GRADUATED is reserved for an item that gets a remediation row as its landing surface. These five were INERT at filing and remain INERT -- no live hazard, nothing carried forward -- so DISMISSED_WITH_REASON is the honest disposition.",
  "hazard_standing": "INERT"
 }
]
```

```json
[
 {
  "id": "IRPT_FNTEND-C-S111",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-21T19:00:39Z",
  "one_line": "ROUND-9 L9, DISMISSED_WITH_REASON -- W5-S9 and W8-S1 (one root cause, disarmed together): fe-s-32's stale 'unknown' assertions for a non-authoritative classification now accept 'withheld', matching FE-s-55's contract change.",
  "class": "OBSERVATION",
  "spec_asserts": "COO~F's L8 hand-off: 'W5-S9 + W8-S1 (disarm_owner this seat, same root cause): fe-s-32/holdings-in-a-browser.test.ts's F32-AC3/F32-AC5 held a stale unknown expectation FE-s-55 (this round) made false ... Disarmed directly, portal 21d71733.'",
  "world_is": "Independently verified at portal 21d71733: fe-s-32's F32-AC3/F32-AC5 assertions updated to accept withheld, now 2 of 0. Commit's own author line confirmed 2.0.0_SA_COO~F; commit's own post-fix number (606/21/0) is consistent with the later 612/22/0 total at f4c9ec46 once F59/F60 added 6 more tests.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@1605b02ff8#IRPT_FNTEND-W5-S9",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@1605b02ff8#IRPT_FNTEND-W8-S1",
    "portal 21d71733 (author 2.0.0_SA_COO~F): fe-s-32/holdings-in-a-browser.test.ts F32-AC3/AC5 now 2/0",
    "3.0.0_SA_CVO verification fork's independent re-run of the commit's diff and post-fix count"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W5-S9",
   "IRPT_FNTEND-W8-S1"
  ],
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "GRADUATED is reserved for an item that gets a remediation row as its landing surface. Both were disarmed directly this round (portal 21d71733) -- no live hazard remains -- so DISMISSED_WITH_REASON is the honest disposition.",
  "hazard_standing": "INERT"
 }
]
```

```json
[
 {
  "id": "IRPT_FNTEND-C-S112",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-21T19:00:39Z",
  "one_line": "ROUND-9 L9, DISMISSED_WITH_REASON -- W9-S1: fe-s-48/withheld.test.ts's F48-AC4 compared a fixed ancestor against floating HEAD by raw positional index; re-pinned to its own landing commit a06252ee instead, disarmed directly, portal 21d71733.",
  "class": "OBSERVATION",
  "spec_asserts": "COO~F's L8 hand-off: 'W9-S1 (disarm_owner this seat): fe-s-48/withheld.test.ts's F48-AC4 compared a fixed ancestor against floating HEAD by raw positional index, so any future line-count change to ScopeSummary.tsx fails it regardless of correctness. Disarmed directly, portal 21d71733 (pinned to FE-s-48's own landing commit instead).'",
  "world_is": "Independently verified at portal 21d71733: the self-test's ancestor ref is now the literal commit a06252ee rather than a floating HEAD reference, and the test reads 4 of 0. This also removes the mechanism that produced F59-AC5's unrelated failure noted against FE-s-59 in section 2 above.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@1605b02ff8#IRPT_FNTEND-W9-S1",
    "portal 21d71733 (author 2.0.0_SA_COO~F): fe-s-48/withheld.test.ts pinned to a06252ee, 4/0",
    "3.0.0_SA_CVO verification fork's independent re-run"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W9-S1"
  ],
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "GRADUATED is reserved for an item that gets a remediation row as its landing surface. Disarmed directly this round (portal 21d71733) -- no live hazard remains -- so DISMISSED_WITH_REASON is the honest disposition.",
  "hazard_standing": "INERT"
 }
]
```

```json
[
 {
  "id": "IRPT_FNTEND-C-S113",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-21T19:00:39Z",
  "one_line": "ROUND-9 L9, GRADUATED, ARMED -- W3-S43 ESCALATED FROM EXPOSURE TO INCIDENT: eslint.config.js's globalIgnores does not exclude .vite/**, and this seat independently reproduced 66 live lint errors from transient .vite/deps_temp_* bundle noise at HEAD, right now, not inherited from the filer.",
  "class": "OBSERVATION",
  "spec_asserts": "COO~F's L8 hand-off: 'W3-S43 (disarm_owner 1.0.0_SA_CTO): eslint.config.js's .vite/deps file-matching gap ... Untouched by me, correctly.' CLAUDE.md Rule 22's negative mirror: a hazard that is real is an EXPOSURE until measured whether it fired; only then is it an INCIDENT.",
  "world_is": "3.0.0_SA_CVO's own verification fork ran `bun run lint` at HEAD, live: 166 problems (66 errors, 100 warnings), all 66 errors sited under .vite/deps_temp_*/...js -- a real, currently-firing defect, not a theoretical gap. eslint.config.js's globalIgnores(['dist','.runtmp/**','.frontend-dev/**']) has no .vite exclusion despite portal .gitignore:17 ignoring .vite. The 5 lint fixes FE-s-52 delivered (F52-AC6, graded PASS above) are unaffected -- this defect sits in the scan surface, not in the delivered fix.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@1605b02ff8#IRPT_FNTEND-W3-S43",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/remediations/REMEDIATION_v6.md (same slug) row IRPT_FNTEND-W3-S43",
    "3.0.0_SA_CVO verification fork, live at HEAD, 2026-09-21: cd portal && bun run lint -> 166 problems (66 errors, 100 warnings), all under .vite/deps_temp_*"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W3-S43"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO"
 }
]
```

```json
[
 {
  "id": "IRPT_FNTEND-C-S114",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-21T19:00:39Z",
  "one_line": "ROUND-9 L9, GRADUATED, ARMED -- W8-S2 accepted on the merits, filer's citation corrected: fe-s-42/_captures.ts's whole-tree unscoped git-status read is a deliberate design choice under 'RULING AC' (not 'RULING X' as the drain note cited), independently confirmed against the file's own header comment.",
  "class": "OBSERVATION",
  "spec_asserts": "COO~F's L8 hand-off: 'W8-S2 ... that check's whole-tree-unchanged design is declared deliberate in its own header ... this instance is a narrow concurrent-write race ... not a standing code defect. Surfacing for adjudicates rather than closing unilaterally.'",
  "world_is": "3.0.0_SA_CVO's verification fork read _captures.ts's own header comment directly: it names RULING AC ('THE PROOF, READ FROM THE WORKING TREE ON PURPOSE -- the defect is dirt in the working tree'), not RULING X, which governs an unrelated round-7 test-scoping census in this project. The underlying judgment -- deliberate whole-tree read, favoring false-positive safety over precision under concurrent writes -- is corroborated by the docstring independent of the citation error, so the disposition stands ACCEPTED AS FILED. Left ARMED: this will keep occasionally false-failing under future concurrent writes to deliverables/, which is a fact about the hazard, not about whether anyone intends to fix it.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@1605b02ff8#IRPT_FNTEND-W8-S2",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/remediations/REMEDIATION_v6.md (same slug) row IRPT_FNTEND-W8-S2",
    "__tests__/fe-s-42/_captures.ts header comment, read by the verification fork: 'RULING AC', not 'RULING X'",
    "2.0.0_SA_COO~F msg 99139 (the mis-cited drain note)"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W8-S2"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~F"
 }
]
```

```json
[
 {
  "id": "IRPT_FNTEND-C-S115",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-21T19:00:39Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A GRADE RECORD, not an item: it adjudicates nothing and opens nothing. The enum has no record value and this row proposes none, per the grades field's own instruction.",
  "one_line": "L9 round 9: the eleven JUDGMENT criteria F50-AC5 through F60-AC6 all graded PASS by 3.0.0_SA_CVO, each independently re-verified against live portal/ source and the round's own re-run test suite rather than trusted from worker or COO prose.",
  "spec_asserts": "Spine v3 L9: a criterion a task order could not reduce to an invocation and an expectation is NEVER self-graded by the worker and never graded by the checker. The CVO reads the proof-of-spec instance against the specification that issued it, and the verdict lives in the grades field.",
  "world_is": "None of the eleven was self-graded, which is the rule working. All eleven PASS on independent re-derivation (section 2 above has the per-criterion basis); two carry a disclosed caveat that does not fail the cell: F52-AC6's lint signal is destabilized by W3-S43 (a scan-surface defect, not this cell's own fix), and F60-AC6's color-law question is genuinely open by the worker's own honest disclosure of a capability gap, not papered over.",
  "grades": [
   {
    "criterion": "F50-AC5",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-50.gen-wire-crlf-independent-hash.proof_of_spec.json@e573b2fe77",
    "verdict": "PASS",
    "reason": "Bar: the fix is at the read boundary (one normalization point), not scattered per-callsite logic, and the regenerated headers are the ONLY diff in contracts/wire/. stableTextForHash() at gen-wire.ts:118-125 is the single point, called at all 4 sites (:304,376,384,498); own test 4/4 SAME HASH AT CRLF AND LF, independently re-run."
   },
   {
    "criterion": "F51-AC5",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-51.carried-hunks-ancestry-aware.proof_of_spec.json@1b099a4b54",
    "verdict": "PASS",
    "reason": "Bar: reuses the file's existing git-read helper and still fails loudly on any unrelated hunk carried that neither branch names. admin-gate.test.ts:591-594 verified against both named refs plus a mutant control (inverted ternary fails as expected)."
   },
   {
    "criterion": "F52-AC6",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-52.five-lint-errors-portal-dev-green.proof_of_spec.json@6f640fb3aa",
    "verdict": "PASS",
    "reason": "Bar: ExportButton's DOM hide/restore is genuinely relocated into useExportAnchor; SentimentGauge's touch is minimal. Independently confirmed in source (ExportButton.tsx:217-248, SentimentGauge.tsx:1-10). CAVEAT, not a failure of this cell: bun run lint at HEAD independently re-run returns 166 problems from unrelated .vite bundle noise (W3-S43, escalated to INCIDENT at C-S113) -- the 5 named errors this cell fixed are confirmed gone and behaviorally sound."
   },
   {
    "criterion": "F53-AC5",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-53.status-envelope-no-state-reason.proof_of_spec.json@16f2d5bf7b",
    "verdict": "PASS",
    "reason": "Bar: the read that located the gap is sound and the fix is minimal, touching no other adapter. adapt.ts:602 confirmed as the exact fix; the worker's own correctly-refused residual independently re-verified resolved upstream (35 tests, 0 fail)."
   },
   {
    "criterion": "F54-AC6",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-54.status-document-own-stated-state.proof_of_spec.json@42be143d4d",
    "verdict": "PASS",
    "reason": "Bar: the first-act trace is real and any fix made is grounded in what that trace found. Independently confirmed 0 production render sites for the traced functions; the real gap (carryAvailabilityFromStatus) and its fix (envelope.ts:173,268-270) match the trace exactly."
   },
   {
    "criterion": "F55-AC7",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~5/IRPT_FNTEND.TO-FE-s-55.holdings-non-authoritative-withheld.proof_of_spec.json@aab5da95b2",
    "verdict": "PASS",
    "reason": "Bar: withheld and an asserted unknown never collapse into each other anywhere in the render path. slices.ts:121-123 confirmed to return withheld on all three axes for a non-authoritative classification."
   },
   {
    "criterion": "F56-AC6",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~6/IRPT_FNTEND.TO-FE-s-56.fe-s-14-control-repoint-and-fixture-prose.proof_of_spec.json@3ba2eb93c4",
    "verdict": "PASS",
    "reason": "Bar: the prose fix accurately describes current behavior, and the control search is grounded in what the tests actually assert. fixtures/index.ts:77 confirmed corrected; the genuinely stale control was found in the sibling positive-control test (not the obvious main assertion) and fixed with a verified mutant -- a real catch, not a shallow pass."
   },
   {
    "criterion": "F57-AC8",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~7/IRPT_FNTEND.TO-FE-s-57.unprojected-grant-parse-and-carry.proof_of_spec.json@322ed57945",
    "verdict": "PASS",
    "reason": "Bar: carryUnprojectedGrant genuinely mirrors carryAvailabilityFromStatus's shape and this cell renders nothing. Confirmed at adapt.ts:348-355 / index.ts:111 / envelope.ts:200,278-282; independently re-run 278 pass/2 skip/0 fail; no .tsx touched in this cell's own commits."
   },
   {
    "criterion": "F58-AC7",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~8/IRPT_FNTEND.TO-FE-s-58.status-panel-unprojected-grant-badge.proof_of_spec.json@032baeed3d",
    "verdict": "PASS",
    "reason": "Bar: the badge idiom matches color law and F58-AC5's Global-mode control genuinely exercises a different code path than F58-AC2. StatusPanel.tsx:88-91 confirmed to reuse the SAME class as the adjacent pre-existing reason-code slot (:70), literally, not merely asserted; whole-suite 612/22/0 independently re-run."
   },
   {
    "criterion": "F59-AC6",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~9/IRPT_FNTEND.TO-FE-s-59.scope-summary-unprojected-grant-badge.proof_of_spec.json@c65a625e71",
    "verdict": "PASS",
    "reason": "Bar: the badge idiom matches color law and the cohort-block separation is genuine, not merely a different CSS class on the same container. ScopeSummary.tsx:69,111-112 confirmed as a real structural sibling via PartialDisclosureFact. The unrelated fe-s-48 self-test failure was correctly refused and is disarmed at C-S112 (W9-S1)."
   },
   {
    "criterion": "F60-AC6",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~10/IRPT_FNTEND.TO-FE-s-60.period-in-context-unprojected-grant-badge.proof_of_spec.json@fd6394c12b",
    "verdict": "PASS",
    "reason": "Bar: the badge idiom matches color law and this file's own ir-* class conventions, and F60-AC4 genuinely proves one shared render path. PeriodInContextPage.tsx:100-109 confirmed: preview and PDF render strings are byte-identical, mechanically proving the shared path. The color-law question is left genuinely open -- the worker disclosed no screenshot capability rather than asserting compliance it could not verify; this is a legitimate item for the round-9 analysis, not an execution defect."
   }
  ],
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "Each criterion's own proof-of-spec instance, pinned in its grades entry.",
    "The task orders' <expected_criteria>, none self-graded by any worker.",
    "3.0.0_SA_CVO verification fork's independent re-run of the full portal test suite (612 pass/22 skip/0 fail) and typecheck (rc=0) at HEAD f4c9ec46, plus per-criterion source citations (file:line) rather than trusting worker or COO prose."
   ]
  }
 },
  {
    "id": "IRPT_FNTEND-C-S116",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-21T23:16:00Z",
    "one_line": "Round 10's four judgment criteria: two record-grades PASS, two NOT_EVALUATED because named visual evidence is missing.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The spine assigns all judgment grades to independent L9, against each issued criterion and a pinned proof instance.",
    "world_is": "Four bound proofs are structurally VALID, but that does not grade visual truth. The available artifacts support two record-grades and cannot show every surface named by the other two criteria.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND10_L8_L9_20260921.md (co-committed; independent evidence and limitations)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~11/IRPT_FNTEND.TO-FE-s-61.closing-pass-header-and-reporting-tab.proof_of_spec.json@0a28a5d1b4",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~12/IRPT_FNTEND.TO-FE-s-62.closing-pass-analysis-and-holdings-tabs.proof_of_spec.json@0a28a5d1b4",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/IRPT_FNTEND.TO-FE-s-63.closing-pass-export-and-print-page.proof_of_spec.json@0a28a5d1b4",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~14/IRPT_FNTEND.TO-FE-s-64.closing-pass-component-census-and-colour-law-refresh.proof_of_spec.json@0a28a5d1b4"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only; opens no additional investigation item. The evidence gaps and defects are carried separately.",
    "grades": [
      {
        "criterion": "F61-AC5",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~11/IRPT_FNTEND.TO-FE-s-61.closing-pass-header-and-reporting-tab.proof_of_spec.json@0a28a5d1b4",
        "verdict": "NOT_EVALUATED",
        "reason": "F61-AC5 names summary cards, chart, period results and the ScopeSummary partial-disclosure fact. All are absent in the available supplementary captures; no visual grade of their unseen state is possible. The source-confirmed reused control and both-width period-control BEFORE/AFTER fix are positively supported but cannot stand for the whole criterion. See the co-committed round-10 report."
      },
      {
        "criterion": "F62-AC9",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~12/IRPT_FNTEND.TO-FE-s-62.closing-pass-analysis-and-holdings-tabs.proof_of_spec.json@0a28a5d1b4",
        "verdict": "NOT_EVALUATED",
        "reason": "F62-AC9 names request list, input review, stage display and withheld rendering. Supplementary captures show an unavailable list/no-declared-route and authoritative ADVISORY, not these required renderings. Source confirms reuse and a real table and both-width typography fixes, but the remaining visual artifacts are unavailable. No whole-criterion pass from a subset."
      },
      {
        "criterion": "F63-AC8",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/IRPT_FNTEND.TO-FE-s-63.closing-pass-export-and-print-page.proof_of_spec.json@0a28a5d1b4",
        "verdict": "PASS",
        "reason": "Record-grade only: F63-AC8 requests the export/print read plus the rendered period-note question, not a blanket conformance declaration. Both-width captures and the note crop exist and were independently read. The note is rendered and source #595959 on white yields 7.0047:1. No named print-sheet palette role was found; generic C1/C9/C11 still speak. The visible C3/C8 export defects graduate separately. FWD-12 realization is not graded."
      },
      {
        "criterion": "F64-AC6",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~14/IRPT_FNTEND.TO-FE-s-64.closing-pass-component-census-and-colour-law-refresh.proof_of_spec.json@0a28a5d1b4",
        "verdict": "PASS",
        "reason": "Record-grade only: F64-AC6's refreshed denominator, both baseline comparisons, eight additions/zero removals, every NEW name with a dispute point, and the historical census test result are present. Independent comparison confirms 73=28 REUSED+45 NEW. W14-S2 separately graduates the copied reason and missing demonstration that existing components cannot meet each need. This is not approval of those NEW components or of FWD-12 realization."
      }
    ]
  },
  {
    "id": "IRPT_FNTEND-C-S117",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-21T23:16:00Z",
    "one_line": "The named fe-s-10-global, fe-s-6-ready and fe-s-7-smartx fixtures use retired operation-name keys, while consumed.ts names directory/resolve, performance/{accountSetId} and holdings/{accountSetId}",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FE-s-61 and FE-s-62 name fixtures as answering the scoped route for the visual closing pass.",
    "world_is": "The named fe-s-10-global, fe-s-6-ready and fe-s-7-smartx fixtures use retired operation-name keys, while consumed.ts names directory/resolve, performance/{accountSetId} and holdings/{accountSetId}. The recorded runs match zero of four keys but still pass their canvas/click checks. Supplementary wire-keyed captures are useful evidence, not repair of these ordered invocations.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/contracts/wire/consumed.ts:40-52@243089eb",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~11/smoke_1440.txt@0a28a5d1b4",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~12/closing-pass-analysis-and-holdings-tabs.result.md@0a28a5d1b4"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_FNTEND-W11-S1",
      "IRPT_FNTEND-W12-S1"
    ],
    "notes": "Repair or explicitly retire the stale fixtures and give the next visual criteria wire-match AND named-content expectations; preserve the failed-state evidence. A canvas or CLICKED line alone is not the content bar."
  },
  {
    "id": "IRPT_FNTEND-C-S118",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-21T23:16:00Z",
    "one_line": "The two supplementary Reporting captures show period controls and an Uncertain status panel, not the required answer-bearing body; their scope strip also has no partial-disclosure fact",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "F61-AC5 requires summary cards, chart, period results and the ScopeSummary partial-disclosure fact to be read in both captures.",
    "world_is": "The two supplementary Reporting captures show period controls and an Uncertain status panel, not the required answer-bearing body; their scope strip also has no partial-disclosure fact. Source and before/after captures support the period-control fix but cannot supply a visual grade for content not rendered.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~11/fe-s-61_reporting_1440_live-fixture_AFTER.png@0a28a5d1b4",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~11/fe-s-61_reporting_390_live-fixture_AFTER.png@0a28a5d1b4",
        "portal/src/pages/InvestorReporting/header/ScopeSummary.tsx@243089eb"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_FNTEND-W11-S2"
    ],
    "notes": "Supply scoped, answer-bearing Reporting evidence at 1440 and 390 with the required cards, chart, period results and partial-disclosure fact present; assert CONTENT and independently read it, not only ground colour."
  },
  {
    "id": "IRPT_FNTEND-C-S119",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-21T23:16:00Z",
    "one_line": "index.tsx renders scope failure as red-only text",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DESIGN.md C12 requires an error icon with navy text; C8 permits one persistent filled-purple action per view.",
    "world_is": "index.tsx renders scope failure as red-only text. StatusPanel maps safe actions to filled-primary buttons; the supplied Reporting capture shows Reload alongside the Export primary. These are grounded C12/C8 defects on surfaces outside FE-s-61's grant.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/index.tsx:105@243089eb",
        "portal/src/pages/InvestorReporting/tabs/StatusPanel.tsx:96-108@243089eb",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~11/fe-s-61_reporting_1440_live-fixture_AFTER.png@0a28a5d1b4"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_FNTEND-W11-S3"
    ],
    "notes": "Bring scope-error and safe-action presentation under C12/C8, with one coherent shared-surface grant and state-specific before/after evidence; retain status meanings and actions."
  },
  {
    "id": "IRPT_FNTEND-C-S120",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-21T23:16:00Z",
    "one_line": "FirmDropdown and ModelPortfolios both import PageSurfaceControl and share the old class string, including font-semibold, rounded-lg and shadow-sm",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FWD-12 requires reuse, while DESIGN.md C1/C11 restrict weight, radius and shadows.",
    "world_is": "FirmDropdown and ModelPortfolios both import PageSurfaceControl and share the old class string, including font-semibold, rounded-lg and shadow-sm. Real reuse does not waive current design law. ScopeSummary's cohort classes and slate inks are source-level residuals; the supplied captures do not render a cohort, so no visual cohort claim is made.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/header/FirmDropdown.tsx:29-48@243089eb",
        "portal/src/pages/ModelPortfolios.tsx:49,1272-1277@243089eb",
        "portal/src/pages/InvestorReporting/header/ScopeSummary.tsx:125@243089eb"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_FNTEND-W11-S4"
    ],
    "notes": "Resolve the shared dropdown style and its exact-class tests coherently across both consumers; review cohort/ink styles under the same current clauses without breaking semantics or manufacturing a separate look-alike."
  },
  {
    "id": "IRPT_FNTEND-C-S121",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-21T23:16:00Z",
    "one_line": "The reused CategoryViewTree appears as a dark gradient container nested in a white Holdings panel at both widths, contradicting C3",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DESIGN.md C3 forbids a dark card inside a light panel; C8 limits UI accents but explicitly exempts chart data colour.",
    "world_is": "The reused CategoryViewTree appears as a dark gradient container nested in a white Holdings panel at both widths, contradicting C3. Scope correction: the chart legend's data colours are not inherently forbidden by C8; the purple A-0001 breadcrumb comes from DrillTree.tsx, not CategoryViewTree, so the entire row cannot be attributed to the shared component.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~12/supp_holdings_observed_1440.png@0a28a5d1b4",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~12/supp_holdings_observed_390.png@0a28a5d1b4",
        "portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx:60,181,222@243089eb"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_FNTEND-W12-S2"
    ],
    "notes": "Review the shared CategoryViewTree container against C3 and the local breadcrumb against C8; retain canonical data colours and separate the actual owning files. Reuse itself is confirmed."
  },
  {
    "id": "IRPT_FNTEND-C-S122",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-21T23:16:00Z",
    "one_line": "GenerateComposer and DrillTree carry red-only error text, visibly confirmed in the Analysis captures and contrary to C12",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DESIGN.md C12 names the ERROR presentation; FWD-12 requires usable narrow-width chart/table equivalents.",
    "world_is": "GenerateComposer and DrillTree carry red-only error text, visibly confirmed in the Analysis captures and contrary to C12. The table's right edge is not fully visible in still captures, but SliceTable uses overflow-x-auto and min-w-[640px], so permanent clipping or inaccessible data is NOT proved. C10 does not literally say the quoted 'no clipped content'.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/tabs/analysis/GenerateComposer.tsx:237,280,346@243089eb",
        "portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx:234@243089eb",
        "portal/src/pages/InvestorReporting/tabs/holdings/SliceTable.tsx:90-107@243089eb",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~12/supp_analysis_frozen_1440_AFTER.png@0a28a5d1b4",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~12/supp_holdings_observed_390.png@0a28a5d1b4"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_FNTEND-W12-S3"
    ],
    "notes": "Correct the grounded C12 error presentation. Exercise horizontal table access and preserve withheld/unknown semantics before prescribing a layout change; a cropped initial viewport alone is insufficient to condemn overflow."
  },
  {
    "id": "IRPT_FNTEND-C-S123",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-21T23:16:00Z",
    "one_line": "The original invocation lacked required route coordinates and used dead fixtures",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "The originally issued F63-AC5/AC6 must resolve the print document, not render the refusal page.",
    "world_is": "The original invocation lacked required route coordinates and used dead fixtures. Issuer amendment 84077faa2d and replacement fixtures at portal 243089eb now produce the four-page document and matching proof output at both widths. The independent parser probe additionally shows that the separately tried fe-s-16-print-narrative fixture already had correct route keys and failed on missing unprojected_grant, not on those keys.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-63.closing-pass-export-and-print-page.md@0a28a5d1b4",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/fe-s-63_print_1440.png@0a28a5d1b4",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/fe-s-63_print_390.png@0a28a5d1b4",
        "portal/src/pages/InvestorReporting/contracts/envelope.ts:277-278@243089eb",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND10_CHECKS_20260921.ts (co-committed, exercised rc=0)"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_FNTEND-W13-S1"
    ],
    "notes": "Already remedied for this order by amendment plus the two authored fixtures and second-pass evidence. Preserve the cause correction; do not imply every older shared fixture was repaired."
  },
  {
    "id": "IRPT_FNTEND-C-S124",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-21T23:16:00Z",
    "one_line": "The print route's silver screen ground was fixed at portal 8894e765, confirmed by its before/after captures and current print.css",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "The visual smoke check is used as a ground-colour discriminator for the route being reviewed.",
    "world_is": "The print route's silver screen ground was fixed at portal 8894e765, confirmed by its before/after captures and current print.css. However ui-smoke's CANVAS measurement read the app page field even when .ir-print-root was silver. The localized colour defect is disarmed; the same row's future false-positive measurement mechanism remains armed and is not discharged by changing the page CSS.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/fe-s-63_fix1_before_print_ground_1440.png@0a28a5d1b4",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/fe-s-63_fix1_after_print_ground_1440.png@0a28a5d1b4",
        "portal/scripts/ui-smoke.mjs CANVAS measurement@243089eb",
        "portal/src/pages/InvestorReporting/render/print.css:138-140@243089eb"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_FNTEND-W13-S2"
    ],
    "notes": "Keep the landed print-ground fix. Make the relevant visual criterion inspect the actual route/container ground with a wrong-ground control, or explicitly limit the generic CANVAS line and require the separate check. No claim that all route grounds are measured today."
  },
  {
    "id": "IRPT_FNTEND-C-S125",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-21T23:16:00Z",
    "one_line": "The second-pass four-page print and page-2 crop render '1 of 5 events not yet reflected in this narrative.' Source ties it to ir-note ir-muted on the white sheet",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "F63-AC8(2) requires the period-in-context partial-disclosure note to be rendered and read.",
    "world_is": "The second-pass four-page print and page-2 crop render '1 of 5 events not yet reflected in this narrative.' Source ties it to ir-note ir-muted on the white sheet. Source-colour contrast #595959/#FFFFFF is 7.0047:1. No named print-sheet palette role was found; this does not erase the generic C1/C9/C11 clauses or certify all print styling.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/fe-s-63_print_1440_period_note_crop.png@0a28a5d1b4",
        "portal/src/pages/InvestorReporting/render/narrative/PeriodInContextPage.tsx:100-110@243089eb",
        "portal/src/pages/InvestorReporting/render/print.css:272-287@243089eb",
        "portal/DESIGN.md:C1,C3,C9,C11@243089eb"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_FNTEND-W13-S3"
    ],
    "notes": "The named rendering blocker is resolved by the second-pass fixtures and captured note. Retain the distinction between readable contrast and a complete print-brand review; no new print palette is invented."
  },
  {
    "id": "IRPT_FNTEND-C-S126",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-21T23:16:00Z",
    "one_line": "census.test.ts:2-10 explicitly tells the caller to regenerate if needed and says it grades WRITTEN OUTPUT",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FE-s-64 asks for a refreshed census plus a separately recorded pinned census test and a row if that test fails.",
    "world_is": "census.test.ts:2-10 explicitly tells the caller to regenerate if needed and says it grades WRITTEN OUTPUT. It correctly reads the committed 70-component historical file; the separately refreshed record has 73. Never cite its pass as a live freshness test.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/__tests__/fe-s-11/census.test.ts:2-20@243089eb",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~14/closing-pass-component-census-and-colour-law-refresh.result.md@0a28a5d1b4"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The test explicitly grades written historical census output, not live-tree freshness. The order's conditional 'if it fails' never promised it would discover live drift. Both vintages are disclosed and separately compared, so this is a record of scope, not a defect in the test's documented contract.",
    "adjudicates": [
      "IRPT_FNTEND-W14-S1"
    ],
    "notes": "The test explicitly grades written historical census output, not live-tree freshness. The order's conditional 'if it fails' never promised it would discover live drift. Both vintages are disclosed and separately compared, so this is a record of scope, not a defect in the test's documented contract."
  },
  {
    "id": "IRPT_FNTEND-C-S127",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-21T23:16:00Z",
    "one_line": "The refreshed record has 45 NEW entries",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FWD-12 requires a stated need the existing component set cannot meet for each NEW component.",
    "world_is": "The refreshed record has 45 NEW entries. Its role labels and grouped domain needs do not establish why existing components cannot meet those needs; the worker expressly did not compare wider equivalents. UnnamedReasonCodeFlag demonstrably repeats PageSheet's unrelated frame reason. Wrapper classification and self-use inclusion require a clear census definition, not automatic rejection.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~14/component-census.json@0a28a5d1b4",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~14/closing-pass-component-census-and-colour-law-refresh.result.md@0a28a5d1b4",
        "portal/src/pages/InvestorReporting/render/Page.tsx:110-115@243089eb"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_FNTEND-W14-S2"
    ],
    "notes": "Correct the copied reason and document reviewable component-specific needs against existing candidates. State the inventory's self-use/wrapper boundary explicitly; do not treat a nonempty role label as proof of the PRD's reuse constraint."
  },
  {
    "id": "IRPT_FNTEND-C-S128",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-21T23:16:00Z",
    "one_line": "ReceiptPanel.tsx:42-44 synthesizes LOADING whenever receipt is null, including the idle state before Create export",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "ReceiptPanel's header says the receipt drives job state; DESIGN.md C12 distinguishes empty from loading.",
    "world_is": "ReceiptPanel.tsx:42-44 synthesizes LOADING whenever receipt is null, including the idle state before Create export. Both export captures show Loading beside the still-available Create export button and a Ready preview. Post-click nontermination is not measured. A new shared enum is not established as the only possible remedy.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/export/ReceiptPanel.tsx:40-47@243089eb",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/fe-s-63_export_1440.png@0a28a5d1b4",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/fe-s-63_export_390.png@0a28a5d1b4"
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "IRPT_FNTEND-S69"
    ],
    "notes": "Distinguish idle/no receipt from an in-flight export using actual submission state and the intended empty-state presentation; exercise idle, submitting and received states. Determine the smallest correct surface before widening the shared state contract."
  },
  {
    "id": "IRPT_FNTEND-C-S129",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-21T23:16:00Z",
    "one_line": "Supplementary Analysis captures show 'UNAVAILABLE: analysis requests are not available (no-declared-route)' and no input-review/stage panels; Holdings captures show an authoritative out-of-enum ADVISORY token, not withheld",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "F62-AC9 requires request list, input review, stage display and withheld rendering, not merely a populated composer and authoritative Holdings.",
    "world_is": "Supplementary Analysis captures show 'UNAVAILABLE: analysis requests are not available (no-declared-route)' and no input-review/stage panels; Holdings captures show an authoritative out-of-enum ADVISORY token, not withheld. The existing API explicitly rejects listAnalysisRequests with NoDeclaredRoute. The delivered subset cannot grade all named visual surfaces.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~12/supp_analysis_frozen_1440_AFTER.png@0a28a5d1b4",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~12/supp_analysis_frozen_390_AFTER.png@0a28a5d1b4",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~12/supp_holdings_observed_1440.png@0a28a5d1b4",
        "portal/src/api/endpoints/investor-reporting.ts:listAnalysisRequests@243089eb"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Name which requested states are reachable under the current contract, obtain both-width evidence for each reachable named state including withheld, and explicitly resolve the unavailable-list limitation through the existing contract boundary. Do not invent a backend list route to satisfy a screenshot."
  },
  {
    "id": "IRPT_FNTEND-C-S130",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-21T23:16:00Z",
    "one_line": "ExportModalPanel mounts Panel variant=chart and uses filled-primary selected Branding chips; both current export screenshots display the dark nested container and purple Opal chip beside Create export",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DESIGN.md C3 requires light panels and C8 forbids filled-purple options in a segmented control; FWD-12 extends brand consistency to export.",
    "world_is": "ExportModalPanel mounts Panel variant=chart and uses filled-primary selected Branding chips; both current export screenshots display the dark nested container and purple Opal chip beside Create export. This is a real C3/C8 conflict. The old colour-law scan allows any Panel anchor and is not a current design-conformance grade. Preview overflow is explicitly horizontal-scroll in source; permanent clipping is not proved.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/export/ExportModal.tsx:180-212@243089eb",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/fe-s-63_export_1440.png@0a28a5d1b4",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/fe-s-63_export_390.png@0a28a5d1b4",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-11/colour-law.test.ts:8-34@243089eb"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Bring export container and branding-selection presentation under C3/C8 with before/after reads at both widths; review shared Dialog/Panel constraints under an appropriate grant. Preserve approved-asset and export semantics, and verify preview scrolling rather than infer clipping."
  },
  {
    "id": "IRPT_FNTEND-C-S131",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-21T23:16:00Z",
    "one_line": "Correct the old diagnostic fixture's failure attribution with a one-field parser discriminator; qualify the print-colour inference.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The amended FE-s-63 order requires identifying the rejecting step for the separately tried fe-s-16-print-narrative fixture; a same-turn multi-field replacement is not a causal isolation.",
    "world_is": "Both original and replacement maps already carry performance/ and narrative/ keys. parseIrEnvelope rejects the original on missing unprojected_grant. Adding only that field makes it parse UNCERTAIN; deleting only it from the replacement reproduces refusal. Complete original browser path not rerun. C9's generic actual-backdrop bar remains usable despite no named print-sheet palette role; source #595959/white is 7.0047:1, not a physical-print measurement.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND10_CHECKS_20260921.ts (co-committed, rc=0)",
        "portal/src/pages/InvestorReporting/contracts/envelope.ts:277-278@243089eb",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~13/diag_print_1440.out@0a28a5d1b4",
        "portal/DESIGN.md:C9@243089eb"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Causal correction and interpretation record; the original order defect/remedy remains carried by the W13-S1 adjudication, not reopened as a duplicate item."
  },
  {
    "id": "IRPT_FNTEND-C-S132",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T04:55:32Z",
    "one_line": "Missing second click in the delay criterion.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "F65-AC16 expected a delayed export POST after clicking Export.",
    "world_is": "Export opens the dialog; Create export sends the POST. Amendment 6100a2fc06 supplies the second click and the final proof records DELAYED.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@d20200b92c#IRPT_FNTEND-W15-S1",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md (co-committed, independent read)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W15-S1"
    ],
    "disposition": "GRADUATED"
  },
  {
    "id": "IRPT_FNTEND-C-S133",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T04:55:32Z",
    "one_line": "An announced amendment was not yet present at its claimed pin.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The worker was directed to execute an amendment said to be in the repository.",
    "world_is": "The worker read the claimed c71fad69a4 bytes and refused the absent amendment; 6100a2fc06 subsequently carried it. The final order and proof agree.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@d20200b92c#IRPT_FNTEND-W15-S2",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md (co-committed, independent read)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W15-S2"
    ],
    "disposition": "GRADUATED"
  },
  {
    "id": "IRPT_FNTEND-C-S134",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T04:55:32Z",
    "one_line": "The visual instrument dependency was omitted from a ready root.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "spec_asserts": "FE-s-66 is a ready root while its common instrument clause says FE-s-65 already exists in its base.",
    "world_is": "Issuance 730c75ee87 makes 65,66,73 concurrent roots. FE-s-66 refused missing flags, then replacement evidence after 65 landed matched 3 of 3 twice. That recovery is not proof that the original dependency ordering was valid.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@d20200b92c#IRPT_FNTEND-W16-S1",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md (co-committed, independent read)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W16-S1"
    ],
    "disposition": "GRADUATED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S135",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T04:55:32Z",
    "one_line": "The revision-mismatch guard is not browser-reachable through the current wire adapter.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FE-s-67 leaves the DrillTree mismatch capture open unless a truthful fixture can exercise it; no invented contract field.",
    "world_is": "adaptHoldingsSnapshot assigns one sourceSetRevision to every node and the snapshot. The guard was wrapped with PanelError but no truthful wire fixture can produce the mismatch. Component/source evidence is not browser coverage.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@d20200b92c#IRPT_FNTEND-W17-S1",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md (co-committed, independent read)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W17-S1"
    ],
    "disposition": "GRADUATED"
  },
  {
    "id": "IRPT_FNTEND-C-S136",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T04:55:32Z",
    "one_line": "The existing Holdings driver takes positional arguments and emits DRIVER OK.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "F67-AC10 originally supplied flag arguments and expected SAVED or scrollLeft.",
    "world_is": "The driver rejected that invocation. Amendments 5cad and b570ecf546 corrected invocation/output expectations; the worker's 390 scrolled image exposes Supervision, Advisory and Provenance.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@d20200b92c#IRPT_FNTEND-W17-S2",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md (co-committed, independent read)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W17-S2"
    ],
    "disposition": "GRADUATED"
  },
  {
    "id": "IRPT_FNTEND-C-S137",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T04:55:32Z",
    "one_line": "default.json still lacks the now-required envelope field on every response.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "spec_asserts": "F67-AC3 treated fixtures/smoke/default.json as a successfully resolving scope control.",
    "world_is": "All 12 entries still omit unprojected_grant at portal 5c8a9ba9. The criterion was repointed to fe-s-18-frozen; that fixes the ordered control, not default.json. Independent read-only probe confirms 12 of 12.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@d20200b92c#IRPT_FNTEND-W17-S3",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md (co-committed, independent read)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W17-S3"
    ],
    "disposition": "GRADUATED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S138",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T04:55:32Z",
    "one_line": "The blanket PanelError import instruction conflicts with the named safe-action pattern.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "HOW asks PanelError in all four touched files, while the cell specifically calls for buttonClass in StatusPanel.",
    "world_is": "Three error text surfaces reuse PanelError; StatusPanel reuses buttonClass secondary canvas sm. Importing unused PanelError there would not meet the substantive reuse requirement.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@d20200b92c#IRPT_FNTEND-W17-S4",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md (co-committed, independent read)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W17-S4"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "No extra import or renderer is warranted."
  },
  {
    "id": "IRPT_FNTEND-C-S139",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T04:55:32Z",
    "one_line": "An amendment supplied prose where the invocation required a declared executable placeholder.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Every acceptance invocation must be runnable with only declared placeholders.",
    "world_is": "The first driver amendment still contained bracketed prose; b570ecf546 replaced it with executable arguments and the final bound proof validates.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@d20200b92c#IRPT_FNTEND-W17-S5",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md (co-committed, independent read)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W17-S5"
    ],
    "disposition": "GRADUATED"
  },
  {
    "id": "IRPT_FNTEND-C-S140",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T04:55:32Z",
    "one_line": "The cohort-chip source still requests a six-pixel radius.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DESIGN.md C11 admits 2/3/4px or pill, not rounded-md; FE-s-68 orders this out-of-grant finding filed.",
    "world_is": "ScopeSummary's cohort-chip retains rounded-md. Available fixtures leave that chip absent, so the grounded fact is source-level, not an observed computed 6px capture.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@d20200b92c#IRPT_FNTEND-W18-S1",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md (co-committed, independent read)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W18-S1"
    ],
    "disposition": "GRADUATED"
  },
  {
    "id": "IRPT_FNTEND-C-S141",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T04:55:32Z",
    "one_line": "The original ground selector measured the Eyebrow wrapper rather than the card.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "spec_asserts": "F70-AC2/3 must measure CategoryOverview's actual card.",
    "world_is": "The old selector matched an element, not zero elements: it hit the first Eyebrow wrapper and inherited white. ea18c43025 selects the second child/card instead. The targeting correction is real; the separate gradient blind spot W20-S2 remains.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@d20200b92c#IRPT_FNTEND-W20-S1",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md (co-committed, independent read)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W20-S1"
    ],
    "disposition": "GRADUATED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S142",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T04:55:32Z",
    "one_line": "Ground reads ignore the gradient that visibly paints the old dark card.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "spec_asserts": "The four-part visual rule requires discriminating the real card ground, including the pre-fix dark state.",
    "world_is": "groundColor reads backgroundColor only. GraphicPanel paints a dark backgroundImage over transparent backgroundColor; the walk reaches white. The worker's real-browser dark mutant still passes, and the independent production-function probe reproduces white for both light and dark-gradient inputs. It also skips an opaque OKLCH background.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@d20200b92c#IRPT_FNTEND-W20-S2",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md (co-committed, independent read)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W20-S2"
    ],
    "disposition": "GRADUATED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S143",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T04:55:32Z",
    "one_line": "Headless dialog portal invalidated the ancestor selector and a summary regex reversed output order.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "F71-AC2/3/5/10 expected a dialog below export-modal and ground summary before style.",
    "world_is": "The portal renders outside export-modal. 61a3203648 removes that ancestor for ground and aligns summary order. Solid-silver control now reads its actual wrong colour, not null. AC10's separate Close selector remains defective, carried in C-S146.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@d20200b92c#IRPT_FNTEND-W21-S1",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md (co-committed, independent read)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W21-S1"
    ],
    "disposition": "GRADUATED"
  },
  {
    "id": "IRPT_FNTEND-C-S144",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T04:55:32Z",
    "one_line": "The three slate text readings are gradeable under existing C3/C9; OKLCH is not a contract exemption.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "spec_asserts": "The worker/TO framed requests-unavailable, holdings-classification-gap and slice-supervision OKLCH readings as lacking a DESIGN.md clause.",
    "world_is": "Source selects slate-600/800/700. C3 already limits body/title ink to navy and secondary panel text to darkGray; C9 applies to every resolved actual pairing regardless of CSS encoding. These noncanonical roles are gradeable now. No numeric contrast failure is inferred without conversion and backdrop measurement.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@d20200b92c#IRPT_FNTEND-W22-S1",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md (co-committed, independent read)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W22-S1"
    ],
    "disposition": "GRADUATED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S145",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T04:55:32Z",
    "one_line": "The broader PageSurfaceControl weight is parked outside this product round.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "C1 disallows the shared primitive's font-medium 500, but CTO's issuance ruling explicitly excludes restyling all six consumers.",
    "world_is": "The shared surfaceBase remains unchanged; FE-s-69 adds a token used by the two named firm dropdowns only. This is the intended scope boundary, not an assertion that weight 500 conforms.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@d20200b92c#IRPT_FNTEND-S70",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md (co-committed, independent read)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-S70"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Parked under the existing CTO scope ruling; no broad shared-primitive edit authorized here."
  },
  {
    "id": "IRPT_FNTEND-C-S146",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T04:55:32Z",
    "one_line": "Style inequality passes when its selector finds nothing.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "THE INSTRUMENT defines a computed-style assertion of the first matched element; F71-AC10 claims Close is not purple.",
    "world_is": "firstComputedStyle returns null on no match and the != branch evaluates null !== expected as true. The independent production-function probe prints PASS null; the final F71 result records exactly PASS null for the invalid export-modal-descendant Close selector.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/scripts/ui-smoke.mjs@5c8a9ba9",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~21/export-modal-chrome-and-receipt-idle-submitting-received.result.md@d20200b92c",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_PROBES_20260922.mjs",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md (co-committed)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "IRPT_FNTEND-C-S147",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T04:55:32Z",
    "one_line": "A URL-hit count does not enforce the four-part rule's wire-contract premise.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "Every visual criterion's part (a) says keys equal consumed.ts operation keys and all N are matched.",
    "world_is": "matchFixture uses arbitrary URL-substring matching; independent production-function probe accepts /api/ as 1 of 1 without contract validation. The specific FE-s-66 classifier checks smoke templates, not every fixture family. Forced failures and delayed submissions can honestly record M<N (F71 in flight 3/4; F72 legacy nine-key fixture 3/9), despite the common N/N promise.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/scripts/ui-smoke.mjs@5c8a9ba9",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-65.the-instrument-content-style-ground-assertions.md@d20200b92c",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_PROBES_20260922.mjs",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md (co-committed)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "IRPT_FNTEND-C-S148",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T04:55:32Z",
    "one_line": "The modal's inversion criterion is not met by the delivered slate equivalents.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "F71-AC17 requires every changed white ink/boundary idiom to become a navy equivalent per C5, before/after captured, and actual horizontal reachability.",
    "world_is": "ExportModal now uses text-slate-900/500/400 and slate borders rather than the ordered navy-role transformation. The worker explicitly supplies source-before instead of the requested before screenshot, and calls scrollWidth 1056/clientWidth 264 plus overflowX auto proof of actual reachable scrolling without a scroll displacement. Nested white variant and distinct receipt states are confirmed, but the conjunction fails.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/export/ExportModal.tsx@5c8a9ba9",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~21/export-modal-chrome-and-receipt-idle-submitting-received.result.md@d20200b92c",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md (co-committed)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "IRPT_FNTEND-C-S149",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T04:55:32Z",
    "one_line": "The new light CategoryViewTree keeps a forbidden purple panel rule.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "DESIGN.md C8 permits the primary action and six named identity accents, not a generic panel border or unrestricted accent link.",
    "world_is": "CategoryViewTree:936 retains an indigo top rule, visible in both f70_irpt widths. Lines 563-570 and 665-666 assert an invented one-accent-link allowance. This is not the exempt data palette; the lilac/teal/amber chart data remain outside this finding.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/components/CategoryViewTree.tsx:563-570,936@5c8a9ba9",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~20/f70_irpt_1440.png@d20200b92c",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~20/f70_irpt_390.png@d20200b92c",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md (co-committed)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "IRPT_FNTEND-C-S150",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T04:55:32Z",
    "one_line": "The newly visible Reporting body still has surface/ink/shape residuals, not a blanket brand pass.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "F68-AC11 requires reading the answer-bearing captures against DESIGN.md; C3 names navy ink and C11 forbids drop shadows.",
    "world_is": "The report body is now visible. Source uses ir-page ink #0A1733 and print.css:520 adds a screen box-shadow, visible on the sheet; purple UNAVAILABLE text persists. At 390 the metric/chart/account content extends beyond the visible area; the static image alone does not establish permanent clipping or usable scroll. Cards intentionally read UNAVAILABLE under the ordered wire shape.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/render/print.css:520@5c8a9ba9",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~18/f68_answer_1440.png@d20200b92c",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~18/f68_answer_390.png@d20200b92c",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md (co-committed)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "IRPT_FNTEND-C-S151",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T04:55:32Z",
    "one_line": "Received export presents two filled-purple actions at once.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "DESIGN.md C8 permits exactly one persistent filled primary action per view; FE-s-71 addresses modal C8.",
    "world_is": "The received-state screenshot visibly contains both Download and Create export as filled purple buttons. ReceiptPanel's download styling and ExportModal's submit styling account for the simultaneous spend. Distinct idle/submitting/received states do not establish accent compliance.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/export/ReceiptPanel.tsx@5c8a9ba9",
        "portal/src/pages/InvestorReporting/export/ExportModal.tsx@5c8a9ba9",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~21/f71_received_1440.png@d20200b92c",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md (co-committed)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "IRPT_FNTEND-C-S152",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T04:55:32Z",
    "one_line": "Round-11 nine JUDGMENT grades: seven PASS, F65-AC18 and F71-AC17 FAIL.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9 assigns the nine non-instrumentable criteria to CVO; proof validation is not their substantive grade.",
    "world_is": "All nine bound instances structurally validate across 116 criteria. Independent source, supplied capture and production-function review yields the grades below, bounded to their actual bars.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md (co-committed)",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-71.export-modal-chrome-and-receipt-idle-submitting-received.md@d20200b92c"
      ]
    },
    "grades": [
      {
        "criterion": "F65-AC18",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~15/IRPT_FNTEND.TO-FE-s-65.the-instrument-content-style-ground-assertions.proof_of_spec.json@d20200b92c",
        "verdict": "FAIL",
        "reason": "F65-AC18 / THE INSTRUMENT requires the nearest self-or-ancestor nonzero-alpha background colour. Production groundColor ignores opaque OKLCH and returns the white ancestor. Independent function probe reproduces the error. The declared flag spellings, legacy output lines and recorded negative arms are present, but those successes do not cure the semantic contradiction; gradient limits and absent-selector inequality are separately carried."
      },
      {
        "criterion": "F66-AC9",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~16/IRPT_FNTEND.TO-FE-s-66.fixture-classification-and-answer-bearing-authoring.proof_of_spec.json@d20200b92c",
        "verdict": "PASS",
        "reason": "F66-AC9 evidence bar: 16 deleted fixtures have no runtime consumers in the reviewed portal source/scripts/public surfaces; the only source reference is a historical comment. Worker census quotes 41 matching files, 40 prose plus one comment, not total scanned files. Two three-key answer-bearing maps and final 3/3 lines are recorded. Classifier checks consumed.ts templates, with not-a-real-route control failing. PASS applies to this bounded fixture family, not universal wire-match certification."
      },
      {
        "criterion": "F67-AC12",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~17/IRPT_FNTEND.TO-FE-s-67.c12-error-presentation-shared-surfaces.proof_of_spec.json@d20200b92c",
        "verdict": "PASS",
        "reason": "F67-AC12: source reuses PanelError for the three actual red-text surfaces and existing secondary buttonClass for StatusPanel. The conflicting blanket import instruction is dismissed at W17-S4. Breadcrumb purple/navy choice is explicitly left to CTO. Default-fixture residue and unrenderable revision mismatch remain named open, not passed off as browser coverage; corrected Holdings driver supplies an actually scrolled image."
      },
      {
        "criterion": "F68-AC11",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~18/IRPT_FNTEND.TO-FE-s-68.reporting-answer-bearing-and-scope-strip.proof_of_spec.json@d20200b92c",
        "verdict": "PASS",
        "reason": "F68-AC11 is a record/read criterion, not a conformity verdict. Answer-bearing full captures at 1440/390 and the ordered partial capture at 1440 disclose UNAVAILABLE summary cards as the specified wire shape. Ink, sheet shadow, narrow-width cut-off and residual AnswerStatus colours are not hidden; C-S150 and W18-S1 carry remaining work. No fabricated populated values or blanket C3/C9 pass."
      },
      {
        "criterion": "F69-AC9",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~19/IRPT_FNTEND.TO-FE-s-69.shared-dropdown-class-token.proof_of_spec.json@d20200b92c",
        "verdict": "PASS",
        "reason": "F69-AC9: additive class export leaves surfaceBase/controlVariants unchanged; only FirmDropdown and ModelPortfolios import it. Before/after 1440 Model Portfolios images show the restyled control with otherwise unchanged visible layout. The 390 control lies off the visible right edge and has no before pair: no additional all-width regression clearance is inferred."
      },
      {
        "criterion": "F70-AC9",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~20/IRPT_FNTEND.TO-FE-s-70.categoryviewtree-light-variant-for-drilltree.proof_of_spec.json@d20200b92c",
        "verdict": "PASS",
        "reason": "F70-AC9 is the additive/data-preservation bar: existing component adds default-dark ground prop; DrillTree's change for this cell is ground=light; data hues and percent labels are not restyled. Light IRPT and default-dark Model Portfolios captures agree with the source. This does not grade the false ground discriminator or C8 panel accent, which remain open."
      },
      {
        "criterion": "F71-AC17",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~21/IRPT_FNTEND.TO-FE-s-71.export-modal-chrome-and-receipt-idle-submitting-received.proof_of_spec.json@d20200b92c",
        "verdict": "FAIL",
        "reason": "F71-AC17's conjunction fails: changed modal ink/boundaries use slate rather than the ordered navy C5 equivalents; result admits no before screenshot; scrollWidth/clientWidth plus overflowX demonstrate capacity, not exercised horizontal reachability. Existing nested variant and genuinely distinct idle/submitting/receipt states are confirmed. S69 closes narrowly; modal styling/scroll evidence does not."
      },
      {
        "criterion": "F72-AC11",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~22/IRPT_FNTEND.TO-FE-s-72.holdings-withheld-and-reachable-analysis-states.proof_of_spec.json@d20200b92c",
        "verdict": "PASS",
        "reason": "F72-AC11 explicitly separates browser-reachable requests-unavailable/composer and Holdings withheld from five test-seeded Analysis components. Source listAnalysisRequests unconditionally rejects NoDeclaredRoute; no invented route. Withheld is visibly distinct from out-of-enum ADVISORY. These worker captures predate sibling styling and are not merged-HEAD visual certification."
      },
      {
        "criterion": "F73-AC10",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~23/IRPT_FNTEND.TO-FE-s-73.census-reasons-component-specific.proof_of_spec.json@d20200b92c",
        "verdict": "PASS",
        "reason": "F73-AC10: all 45 NEW entries state component-specific needs against named candidates; own-comment versus file fallback, self-use and thin-wrapper boundaries are explicit. Four control tests pass in the independent full suite; prior census lacks needs and repeats PageSheet's reason. This grades the pinned historical 73/28/45 census, not current freshness, architectural optimality, or a mandate for 45 new components."
      }
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only; defects have their own graduated carriers and remediation rows."
  }
]
```

## Round 10 appended by 3.0.0_SA_CVO~F (2026-09-21)

Input COO~F message 99314; issuance fcf38f866b; intake HEAD 0a28a5d1b4.
C-S116..C-S131: four machine-readable grades, every one of thirteen incoming
items dispositioned, two additional CVO findings and a causal correction record.
Detailed independent read and its limits:
`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND10_L8_L9_20260921.md`.
Original round-9 rows are unchanged. Round-10 slug: REMEDIATION_v7.md.
