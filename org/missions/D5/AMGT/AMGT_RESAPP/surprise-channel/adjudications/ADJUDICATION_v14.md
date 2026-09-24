# AMGT_RESAPP rounds 14-15: CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-21T15:4xZ; evidence read between HEAD `7328e6d7f6` and `dfc382cb7a`,
resolver simulated over this document at `dfc382cb7a`. LOCAL on SITEZ.
**Inputs:** the channel census by `.tools/surprise-row-gate.py` `_latest_dispositions` (27 carriers, 446 items, 0
unknown targets); the round-14 and round-15 L8 packets; the COO's round-16 candidate census
(`ledger/ROUND16_CANDIDATE_CENSUS_20260921.md` @`a0d593560c`) and its drafters' HEAD reads; three read-only
evidence passes run from this seat at `7328e6d7f6`; this seat's working record
`org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND14_L9_WORKING_RECORD_20260919_Z.md`; and this seat's
R4 ruling `org/tier1_exec/3.0.0_SA_CVO/deliverables/CVO_RULING_AMGT_RESAPP_R4_GRADE_VS_TERMINALITY_20260921.md`
@`335faf48fe`.

## Why this document is late, and what it corrects

Round 14's L9 (`ledger/ROUND14_L9_ADJUDICATION_20260921.md` @`4b28d18bbc`) filed NO channel rows. The resolver
therefore read **62 items UNDER_INVESTIGATION** after two drained rounds, and the COO's subtraction over 26 carried ids
found the gap before this seat did. The COO's disarm rows (`Z-S181`-`Z-S190`) moved `hazard_standing`; only an
adjudication or remediation row moves `disposition`, and both are this seat's. **All 62 are dispositioned or
explicitly held here.**

Three corrections to this seat's own round-14 record, stated plainly:

1. **The round's declared judgment criterion is `rk-43` AC5, not `rk-61` AC2.** The round-14 adjudication s.1 called
   `rk-61` AC2 "the round's one declared JUDGMENT criterion"; it carries no `judgment` attribute. This seat's working
   record s.2 had named `rk-43` AC5 correctly and the adjudication dropped it, so the one declared judgment went
   ungraded and `1.0.0_SA_CTO~Z` ratified the mislabel (`ROUND_ANALYSIS.round14.md` s.1). Found by an evidence pass
   from this seat, reading `--acceptance --round 14`'s UNVERIFIABLE list. `rk-43` AC5 is graded in row C-S322.
   The ruling on `rk-61` AC2 itself stands, re-labelled: an L9 classification of a criterion whose literal bar became
   unmeetable outside the cell, not a declared-judgment grade.
2. **`W60-S3` was not "unrepaired".** Round-14 adjudication s.4 item 7 said so. The remove verb was fixed at
   `3795d4f487` (2026-09-19 03:54 -04:00), two days BEFORE that document, and the repair commit `fae9316edb` this seat
   read the same session says "AC5 stands" -- which this seat misread as "the defect stands". Row C-S340.
3. **No channel rows.** Above.

## Round state

Orders: 5 open of 131 (`_open_tos_for_project`): `rk-32`, `rk-49`, `rk-50`, `rk-51`, `rk-52`, all on reserved words.
Round 15: 3 of 3 terminal. Round 16: issued (4 cells), not drained.

Acceptance, re-run at this seat:
- round 13: PASS 26 / FAIL 3 / UNVERIFIABLE 3 of 32 -- the three FAILs admissible under R4 (C-S308).
- round 14: PASS 126 / FAIL 1 / UNVERIFIABLE 33 of **160 over 30 orders**. The true population is **165 over 31**:
  row `S176` (the sweep drops `rk-58`'s five criteria) is LIVE and its fix is round 17's (C-S323). The one FAIL,
  `rk-44` AC3, is classed a CRITERION defect in C-S336 with the act shown correct on a second instrument.
- round 15: 0 FAIL; no judgment criterion declared in its three orders.

## Judgment grades (row C-S322)

| criterion | verdict |
|---|---|
| rk-43 AC5 | NOT_EVALUATED -- the criterion names a HEADED human session as its instrument; this seat holds none, and no captured render exists |

## Dispositions, by denominator

| the 62 open items | items |
|---|---|
| GRADUATED (remedy named, holder named) | 12 |
| DISMISSED_WITH_REASON | 47 |
| HELD OPEN on a reserved word | 3 -- `W37-S1` (bucket/tenancy), `W49-S2`, `W49-S4` (Bright Data) |
| **total** | **62 of 62** |

Plus **11 disarm records** by `2.0.0_SA_COO~Z` (`S179`-`S184`, `S186`-`S190`) that set `GRADUATED` on their own
rows: re-dispositioned DISMISSED at C-S344, as `S156`'s was at C-S293.

**REMEDIATION rows owed at the true L10 close, 23** (`_graduated_without_row`, simulated over this document before
commit: 34 at HEAD without C-S344, 23 with it):
- this document's 12: `S176`, `S177`, `W54-S2`, `W38-S5`, `W37-S2`, `W40-S1`, `W45-S1`, `W42-S4`, `W45-S2`,
  `W39-S4`, `W42-S5`, `W38-S1`;
- 11 PRE-EXISTING from earlier rounds, carried and not re-adjudicated here: `S3`, `S4`, `W1-S1`, `W1-S4`, `W1-S5`,
  `W2-S3`, `W2-S5`, `W3-S3`, `W3-S5`, `W7-S2`, `W9-S1`.

None is written here: a new remediation row is the route-carrying act GATE (iii) refuses while orders are open (5
today), and the slug-time limb refuses that slug until all 23 carry a row. The eleven old ones are named now so the
slug writer does not meet them for the first time at the refusal.

**Independent of all three words and not in round 16 or 17, for the CTO's next analysis:** `W38-S5`
(`_latest_stamp` has no content check), `W37-S2` (50 production lines name worker folders), `W40-S1` (CSL's filings
leg). `W45-S1` and `W42-S4` wait on Andrew's standing and R3 words respectively.

## Rows
```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S322",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "L9 GRADE RECORD for rounds 14 and 15: the one declared judgment criterion, rk-43 AC5, is NOT_EVALUATED; round 15 declares none. Corrects round 14's adjudication, which graded rk-61 AC2 as the declared judgment and left rk-43 AC5 ungraded.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "judgment census: rk-43:302 carries <criterion id=\"AC5\" cell_refs=\"AMGT-rk-43\" judgment=\"true\"/>; rk-62, rk-63 and rk-64 carry none (checked at e96c2f199e).",
        "surprise-row-gate.py --acceptance AMGT_RESAPP --round 14 lists AMGT-rk-43.management-honest-states:AC5 under UNVERIFIABLE as a judgment criterion graded at L9.",
        "ledger/ROUND14_L9_ADJUDICATION_20260921.md s.1 @4b28d18bbc graded rk-61 AC2 under the heading 'the one declared JUDGMENT criterion'; rk-61 AC2 has no judgment attribute."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: every judgment criterion is graded by the CVO against the specification that issued it, never self-graded.",
    "world_is": "rk-43 AC5's own text names a HEADED human session as the grading instrument, because mandatory MFA blocks every headless authenticated capture (s.3.5). This seat is headless and no captured render of the Exec Management tab exists.",
    "notes": "Grade carrier only. The NOT_EVALUATED grade is not converted into a verdict from payloads (round-12 C-S273 precedent). The instrument gap is already graduated at C-S316.",
    "dismissal_reason": "Grade record: this row carries the rounds-14/15 judgment grades and dispositions no item; the enum has no record value.",
    "grades": [
      {
        "criterion": "AMGTrk43-AC5",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~45/AMGT_RESAPP.TO-AMGT-rk-43.management-honest-states.proof_of_spec.json@12722614b2",
        "verdict": "NOT_EVALUATED",
        "reason": "Bar (rk-43:307-309): the RENDERED Exec Management tab tells the reader the truth about each of the 12 served names -- a zero-officer name shows its reason and no table, a never-searched name says so, no line claims a search that did not run. The named instrument is a headed human session; none has been run and no captured render exists. Limits, carried not converted: the instance's AC4 read three names live after the redeploy (ASML ZERO_OFFICERS, NU NOT_SEARCHED, SAP CONFIRMED); and W45-S1 measured 4 of the 12 served objects (BABA, BA, COST, HD, 2026-09-15) reading CEO_READING_UNREADABLE_OBJECT because they predate absence_class -- an honest generic line, but not the most specific truth the criterion asks for (C-S331)."
      }
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S323",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "GRADUATED: the acceptance sweep drops rk-58's five criteria (unanchored _PROOF_BLOCK_RE binds a prose mention), so round 14 reads 160 over 30 against a true 165 over 31 -- load-bearing for L10 since the R4 ruling.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Measured at 7328e6d7f6: _order_criteria(rk-58 order text) returns 0; --acceptance --round 14 reads 'of 160 criteria over 30 order(s)'.",
        ".tools/surprise-row-gate.py:1180 _PROOF_BLOCK_RE = <proof_of_spec>(.*?)</proof_of_spec> with re.S and no anchor; _order_round two functions below is anchored.",
        "1.0.0_SA_CTO~Z re-verified independently (msg 23929) and ruled it a cell; msg 23932 moved it to round 17 because round 16 had already issued."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The acceptance sweep reads every criterion of every order in the round.",
    "world_is": "An order that quotes its own record-face tag in prose loses all its criteria from both denominators, silently.",
    "notes": "Remedy: round-17 cell S176-anchor (ROUND16_CTO_RULINGS_20260921.md s.2a @006dd1e344; msg 23932). Until it lands, every slug prints the sweep's denominator against the true count from the order files.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S176"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S324",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "GRADUATED: a resolved non-EDGAR winner (doc-<sha16>) is not admitted as an accession and beats the UNRESOLVED-SOURCE placeholder only by sort order; the posture batch still bare-sorts and drops a filed name roster resolves.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lib/research/management/roster.py:831-838 _is_accession_key is stem.isdigit(); a Doc- capital variant picks the placeholder (census s.1 C1).",
        "integrations/bloomberg/research/management_posture_batch.py:105 filed_status takes sorted(keys)[-1]; offline stub: roster -> 000000000000000001.source.json, posture batch -> UNRESOLVED-SOURCE, filed_names [] (census s.5).",
        "filings/v1/6861_JP_Equity/ holds both UNRESOLVED-SOURCE.source.json and doc-1defdb68a7ffd3b7.source.json (read-only list at 7328e6d7f6)."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "A resolved source wins over the placeholder by rule, in every reader.",
    "world_is": "One reader wins by accident of ASCII order; the other loses outright.",
    "notes": "Remedy: round-16 cell C1 (one cell owning the ranking rule in both readers; the batch imports roster's rule). This seat's own Z-S177 filed the composition; its stale code half was disarmed at Z-S179.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S177"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S325",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "DISMISSED onto S177: objects accumulate per key with no supersession (W40-S2), and the roster/shared-census half of W46-S2 -- both are the ranking rule C1 fixes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W40-S2: the pool key derives from each run's outcome; 6861_JP_Equity carries two source objects at 7328e6d7f6. Keeping history is harmless once the picker ranks by rule.",
        "W46-S2 item 1: fixed, roster.py:831-838 and :869-870 (rk-46). Item 2 (the posture batch's bare sort) is C1's second reader."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Each row is its own finding.",
    "world_is": "Both are inputs to the one rule S177 carries.",
    "notes": "Carried by S177 / round-16 C1.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W40-S2",
      "AMGT_RESAPP-Z-W46-S2"
    ],
    "dismissal_reason": "Same mechanism as S177 (C-S324), whose remedy is round-16 cell C1; W46-S2 item 1 already fixed at roster.py:831-838."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S326",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "GRADUATED: the crosswalk read is unpinned -- _read_pool_latest takes sorted(keys)[-1] over crosswalk/v1/ with no key-shape filter, and the page route reads it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lib/research/identity/crosswalk.py:706-723; callers scoped_amgt.py:1729, :1773 and management/batch.py:92 (census s.2 R1).",
        "The population moved 33 -> 36 mid-round when rk-31 wrote crosswalk/v1/2026-09-19.json (working record s.4c)."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "A population read names its vintage.",
    "world_is": "Any key sorting after the dated files (a latest.json) would win silently.",
    "notes": "Remedy: round-16 cell R1-filter (key-shape filter, loud on anything else); policy ruled by 1.0.0_SA_CTO~Z: newest-wins stays, the resolved key is recorded on the answer. run_scores.py's copy is chain P and stays held.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W54-S2"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S327",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "DISMISSED: the five no-lookup-key names (AAPL, NVDA, MSFT, JPM, TSLA) are out of scope by Andrew's standing word; CAT, CSL and Keyence are superseded.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CAT/CSL/Keyence MEASURED in registrations.json @0add9d26c1 (census s.2 R2).",
        "1.0.0_SA_CTO~Z parked R2 on Andrew's standing word 2026-09-18, 'no fleet re-runs until validated' (ROUND16_CTO_RULINGS @dcd88f0acc)."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "The L3 intake's five names are in the crosswalk population.",
    "world_is": "They are not, and adding them is a fleet act Andrew has held.",
    "notes": "Re-opens only on a new word from Andrew; re-asking him is the re-surfacing the RESERVED-vs-ADJUDICABLE rule forbids.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W54-S1"
    ],
    "dismissal_reason": "Answered by Andrew's standing 2026-09-18 word; the three validation names are already MEASURED."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S328",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "GRADUATED (EXPOSURE, never fired): model_block_pull._latest_stamp takes the newest raw/bloomberg stamp with no content check, and two writers put non-raw objects in their own stamps -- derive would crash on NoSuchKey instead of reading absent.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "integrations/bloomberg/research/model_block_pull.py:344-352 has no content check; stage_derive calls it at :904.",
        "Writers of non-raw stamps: the identity landing, and lib/research/management/bloomberg_fallback.py:68 (exec_officers.json).",
        "Live census at 7328e6d7f6: 117 objects, 37 keys, 54 stamps; 8 stamps non-raw; 0 keys whose newest stamp is non-raw (a first pass reported 2 by splitting slash keys BP/_LN_Equity and NG/_LN_Equity on '/'; both carry refdata.json)."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The newest stamp for a key is a pull.",
    "world_is": "The newest stamp is whatever any writer wrote last; one fallback roster run after a pull makes it non-raw.",
    "notes": "Remedy: _latest_stamp requires refdata.json and histdata.json, as build_unit_map.py already does. Holder 2.0.0_SA_COO~Z; independent of all three words, not in round 16 or 17 -- for the CTO's next analysis.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W38-S5"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S329",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "GRADUATED: 50 lines across 25 production .py files still name a worker's deliverables folder (0.9.0_WK_AMGT_RESAPP~<n>) as a config home -- the residue rk-33's C-PRODUCTION-HOME left by design.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Grep over {lib,integrations,infra}/**/*.py at 7328e6d7f6: 55 hits in 30 files, 5 of them tests with one hit each; production 50 lines in 25 files, unchanged from the row. Largest: lib/research/identity/coverage_pass.py (9), crosswalk.py (4), run_reader.py (3). Not classified comment-vs-code."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "PRD C-PRODUCTION-HOME: production code does not depend on a worker's deliverables folder.",
    "world_is": "Twenty-five production files do.",
    "notes": "Remedy: move each file's config beside its producer or behind an address() key (Rule 30), one cell per file or group. Holder 1.0.0_SA_CTO~Z (a PRD contract residue). No incident measured.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W37-S2"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S330",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "GRADUATED: CSL's only entity-tied seed (www.csl.com.au) resets TCP from this box, so the filings crawl never reaches investors.csl.com and CSL serves UNRESOLVED-SOURCE.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-harvest/filings/v1/CSL_AU_Equity/ holds exactly one object, UNRESOLVED-SOURCE.source.json (read-only list at 7328e6d7f6).",
        "The rk-38 worker refused rather than hand-typing a URL (drain 79173538aa) -- correct under the order's own clause."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Each validation name reaches its filings leg.",
    "world_is": "CSL does not, and the served state says so honestly.",
    "notes": "Holder 1.0.0_SA_CTO~Z to rule: another egress path, a second sanctioned seed, or UNRESOLVED by design. A search-primitive seed falls under the Bright Data word.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W40-S1"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S331",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "GRADUATED: 4 of 12 served management objects (BABA, BA, COST, HD, dated 2026-09-15) predate absence_class, so the adapter reads them UNREADABLE_OBJECT rather than the specific searched-state reading.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lib/research/api/scoped_amgt.py:2438-2456 maps only CANNOT_SAY and NOTHING_FOUND; a null absence_class falls through to CEO_READING_UNREADABLE_OBJECT.",
        "Read-only list at 7328e6d7f6: one object per name, management/v1/<key>/2026-09-15.json, modified 15:44-15:48Z that day (4 prefixes, 4 objects). Today's producer sets the field (lib/research/management/enrich.py:465, :469)."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Every served name gets the most specific true reading.",
    "world_is": "Four get an honest generic one, from a data vintage, not a code defect.",
    "notes": "Remedy: backfill the four with the current producer. Holder 2.0.0_SA_COO~Z, held by Andrew's standing 2026-09-18 word ('no fleet re-runs until validated'). Named as a limit on rk-43 AC5 (C-S322).",
    "adjudicates": [
      "AMGT_RESAPP-Z-W45-S1"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S332",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "GRADUATED: the finding-language rule is fixed in the prompt, but Chinese and Korean filings were never exercised -- one live proof per language is owed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The fix is in: analyze.py:226-235, PROMPT_VERSION rj6-two-pass/3 (census s.2 R3). The live sample that found it: 0 of 66 served items in the filing's own script (Keyence)."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Every finding is written in the filing's own language.",
    "world_is": "Proven for Japanese only.",
    "notes": "Remedy: one PASS-1 run per language (~USD 0.45 each), bar VERBATIM-CHARS >= 0.90. Carded to Andrew as R3 (vendor egress is his word alone); holder 1.0.0_SA_CTO~Z.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W42-S4"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S333",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "GRADUATED: worktree provisioning does not cover a targeted terraform apply (no init, no .build artifact); the other two repairs W45-S2 names are now made by wk-provision.sh.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Items 1-2 remedied: .tools/wk-provision.sh:113 creates the portal branch with worktree add -b; :129-135 build the junction via cygpath -w + mklink /J; landed with the rk-60 drain b01a10ed75 and mandated by .claude/skills/dispatch/SKILL.md:173,177.",
        "Item 3: wk-provision.sh has 0 mentions of terraform, .build or init."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "A provisioned worktree can run the order's own named deploy mechanism.",
    "world_is": "It can, except a targeted apply's init and build steps.",
    "notes": "Remedy: an order that does a targeted apply names its init and build steps in the worker face. Holder 2.0.0_SA_COO~Z.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W45-S2"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S334",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "GRADUATED: a worker's Edit call given the main-tree absolute path landed in the shared tree instead of its worktree; caught and reverted, nothing committed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W39-S4: the first HEADER_FIELDS edit landed under C:/Users/Opal Bloomberg/Desktop/ajb_workspace, not C:/tmp/wk-amgt-14-39; the worker reverted it on the next command."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "A worker's writes stay in its worktree.",
    "world_is": "An absolute-path tool call reaches any checkout of the repo.",
    "notes": "Remedy: the worker face names its worktree's absolute root and says every path is under it (CLAUDE.md 14b, 'edit in the worktree where you will commit'). Holder 2.0.0_SA_COO~Z. No mechanism is proposed: a guard would be an agent-made gate.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W39-S4"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S335",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "GRADUATED (class anchor): a criterion's bar was written from someone else's measurement or without measuring the file, and the next document or baseline failed it for content reasons -- round 14's dominant defect, seen again in round 15.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W42-S5: after every fix, rk-40's one affordable live sample reads blocks-per-citation 1/1/2 against a named 1/1/1 and VERBATIM-CHARS 57 of 67 (0.851) against >= 0.90 -- properties of the filing, not the code.",
        "Round-14 packet s.6 finding 1 (three repairs of this shape); round-15 packet s.5.1 (a zero-count bar written for to-pipeline-gate.py, which carries 8 pre-existing non-ASCII bytes).",
        "1.0.0_SA_CTO~Z ruled it a process habit, not a gate (ROUND_ANALYSIS.round15.md s.2)."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "A criterion's bar is a property of the act.",
    "world_is": "Several bars were properties of one document or one baseline.",
    "notes": "Remedy: the cutting seat runs the instrument before writing a number, and a bar names the property and its tolerated deviation. Holder 2.0.0_SA_COO~Z. Instances dismissed onto this row at C-S336.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W42-S5"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S336",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "DISMISSED onto W42-S5: eleven criterion defects of terminal cells -- the bar or the probe was wrong, the act was right, and each criterion was repaired in-round or graded on its qualifying clause. Includes round 14's one sweep FAIL, rk-44 AC3, classed under R4.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W37-S3: expect says 36 fields; the byte-identical source carries 32. W38-S2: the zero bar unreachable until the classification split (162435481b; criterion repaired 361c3aaa90). W38-S3: probe reads a nested model key the Lambda never serves (repaired 361c3aaa90; the silent-constant subtype is CTO round-14 doctrine note 1). W39-S3: same shape, fixed additively in-cell.",
        "W41-S1: D12's figures reproduce only with coverage scoped to the risk item; the worker chose that scope and recorded the others. W41-S2: CSL's heading 'Material Risks' matches none of the four declared patterns. W53-S3: the TRENDING exclusion reason is UNMEASURABLE (movement_gate.py:458), pinned by test_generation.py:389.",
        "W59-S1: fmt no-diff vs pre-existing drift (repaired aec251f0b7). W62-S1: zero-count bar vs 8 pre-existing bytes (disarmed Z-S184). W60-S1: the illustrative branch literal vs the naming in force; mechanism correct (wk-provision.sh:113).",
        "W46-S1 = rk-44 AC3, round 14's one acceptance FAIL. Act shown correct on a SECOND instrument, the live task store at 7328e6d7f6: OpalResearch-ExecManagement Execute is one quoted field, Arguments empty. Positive control on this box: RunPlatformExperienceHelper_Daily stores a quoted space-containing Execute and ran 2026-09-21 08:58 with LastTaskResult 0x0. Control population: 18 of 207 tasks carry a space in Execute, 5 quoted and 13 not -- so 'quoted is Task Scheduler's normal form' is NOT claimed. Limit: the rk-44 task itself has never run (0x41303), disabled by design."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Each criterion's literal expectation.",
    "world_is": "Each expectation was a property of the author's reading, not of the act.",
    "notes": "Under R4 (@335faf48fe) rk-44 AC3's FAIL is ADMISSIBLE: classed CRITERION defect with the act shown correct on another instrument. It is not flipped.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W37-S3",
      "AMGT_RESAPP-Z-W38-S2",
      "AMGT_RESAPP-Z-W38-S3",
      "AMGT_RESAPP-Z-W39-S3",
      "AMGT_RESAPP-Z-W41-S1",
      "AMGT_RESAPP-Z-W41-S2",
      "AMGT_RESAPP-Z-W53-S3",
      "AMGT_RESAPP-Z-W59-S1",
      "AMGT_RESAPP-Z-W62-S1",
      "AMGT_RESAPP-Z-W60-S1",
      "AMGT_RESAPP-Z-W46-S1"
    ],
    "dismissal_reason": "Instances of the class W42-S5 carries (C-S335); each criterion repaired or graded on its qualifying clause, each cell terminal; rk-44 AC3 admissible under R4."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S337",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "GRADUATED (class anchor): rk-34's face names re-derive-with-no-delete as its rollback while both signed halves name delete-the-new-stamp -- a bind changed the act and nothing reconciled the prose. Anchors the round's aged-expectation class.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "rk-34:188-191 (face) vs NEVER_WIDEN_ROUND14_CHAIN_M_COO_HALVES.md:22-24 and the CTO half :48, :79 (working record s.4f). Both deploy entries closed with every leg proven; no rollback was ever needed.",
        "Three instances of a re-signature bind changing an act without its prose (W38-S1, W43-S1, W49-S4); ratified as CTO round-14 doctrine note 2."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "A co-signed act names one rollback, and each criterion describes the world its act runs in.",
    "world_is": "Faces, halves and expectations were each true when written and diverged as binds, peer writes and dates moved.",
    "notes": "Remedy: a re-signature bind carries its edit to every clause it contradicts in the same act; criteria pin their vintages (population, date); a half names the act's shape from the producer's rule (HARD STOPS). Holder 2.0.0_SA_COO~Z. Instances at C-S338.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W38-S1"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S338",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "DISMISSED onto W38-S1: eight expectations that aged between the cut and the run -- across a peer order's write, an issuer bind, a day boundary or a resumed session's own HEAD. The acts were right.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Peer write: W38-S4 and W39-S1 (crosswalk 33 -> 36 by rk-31 at 01:23:43Z; W39-S1 repaired 0f6e7ae2fa), W49-S1 (the validation keys already MEASURED at spawn).",
        "Bind: W43-S1 (AC7 presumes a write issuer bind D4 precluded). Day boundary: W47-S1 (the half described an overwrite of a key that was 404 by the worker's UTC day; the worker executed a create correctly).",
        "Record-face: W57-S1 (negative control now reads PASS/PASS; AC2 re-pointed to rk-20 AC1), W57-S2 (round-13 orders gained <round> tags; --acceptance --round 13 rc 0, unrounded 0; residual R4, now ruled @335faf48fe). Resumed HEAD: W60-S5 (novelty verified against the pre-cell baseline 047aee5478)."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Each criterion's expectation at the cut.",
    "world_is": "Each was true at the cut and false at the run.",
    "notes": "Carried by W38-S1 (C-S337).",
    "adjudicates": [
      "AMGT_RESAPP-Z-W38-S4",
      "AMGT_RESAPP-Z-W39-S1",
      "AMGT_RESAPP-Z-W49-S1",
      "AMGT_RESAPP-Z-W43-S1",
      "AMGT_RESAPP-Z-W47-S1",
      "AMGT_RESAPP-Z-W57-S1",
      "AMGT_RESAPP-Z-W57-S2",
      "AMGT_RESAPP-Z-W60-S5"
    ],
    "dismissal_reason": "Instances of the aged-expectation class W38-S1 carries (C-S337); each act correct, each cell terminal."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S339",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "DISMISSED: sixteen items remedied inside the project and verified -- code fixes, criterion repairs and provisioning fixes, each with its commit.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W39-S2: rk-64 @112dbb5c16; read at this seat: stage_pull(blp, s3, security) is 3 params (model_block_pull.py:371) and pull_consumer.py:98 passes 3.",
        "W39-S5, W45-S3, W49-S3, W61-S1 (the two orphaned test assertions): rk-63 @ec880933eb; re-run at this seat, 24 passed 0 failed.",
        "W58-S2: rk-62 @a495e551de (GATE (x) admits a declared direct act). W58-S1: fixture renamed, repair 7a5c818ff1.",
        "W60-S2, W60-S4: repairs fae9316edb and 928352b513; rk-60 AC3 re-run PASS; disarmed Z-S182/Z-S183. W53-S2: junction built by wk-provision.sh:129-135 (rk-60 drain b01a10ed75).",
        "W42-S3: exclusive end_block_index and multi-block join (census s.4, 2e388452dd, analyze.py:583-607). W42-S7: drafting_build.py:314-317 carries the translation fields (census s.4). W42-S1, W42-S2, W42-S6: rk-40 amendments 1-3 (43566d7, 2aa431b1ea, 2104295c01; cap 3.00 -> 5.00); rk-40 terminal e5f33caeba.",
        "W37-S4: the sanctioned regenerate landed aca8bfebe8; regenerated into scratch at 7328e6d7f6 with zero diff on vectors.json and opal_name.tftest.hcl.",
        "W47-S2: test_13 now plants a third pool object, 2026-09-16 at 7.77, and asserts the NEWEST value against the name's own as_of 2026-09-15 (lib/research/api/tests/test_generation_and_pool_routes.py:490-496 @dfc382cb7a), so it discriminates the retired semantics; recorded by 2.0.0_SA_COO~Z at S190."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Each row's named defect.",
    "world_is": "Each is repaired at HEAD.",
    "notes": "The W42 and W37-S4 lines rest on the COO's drafters' HEAD reads and a scratch regenerate from this seat; W39-S2, W47-S2 and the four test rows on this seat's own reads.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W47-S2",
      "AMGT_RESAPP-Z-W39-S2",
      "AMGT_RESAPP-Z-W39-S5",
      "AMGT_RESAPP-Z-W45-S3",
      "AMGT_RESAPP-Z-W49-S3",
      "AMGT_RESAPP-Z-W61-S1",
      "AMGT_RESAPP-Z-W58-S2",
      "AMGT_RESAPP-Z-W58-S1",
      "AMGT_RESAPP-Z-W60-S2",
      "AMGT_RESAPP-Z-W60-S4",
      "AMGT_RESAPP-Z-W53-S2",
      "AMGT_RESAPP-Z-W42-S3",
      "AMGT_RESAPP-Z-W42-S7",
      "AMGT_RESAPP-Z-W42-S1",
      "AMGT_RESAPP-Z-W42-S2",
      "AMGT_RESAPP-Z-W42-S6",
      "AMGT_RESAPP-Z-W37-S4"
    ],
    "dismissal_reason": "Remedied in-project; each fix cited by commit and verified at HEAD."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S340",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "DISMISSED: W60-S3's remove verb was fixed at 3795d4f487; its live residual -- the self-test's unconditional prune against the real repos -- is round-16 cell C2. Corrects this seat's round-14 adjudication, which called it unrepaired.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/wk-provision.sh cmd_remove :200-248 has no prune; :235 recreates the placeholder (census s.1 C2).",
        "git merge-base --is-ancestor 3795d4f487 4b28d18bbc -> true: the fix predates the adjudication that called it unrepaired by two days.",
        "Residual: cmd_self_test runs git worktree prune (:388) and git -C <nested> worktree prune (:397) against the real superproject and portal."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Round-14 adjudication s.4 item 7: 'W60-S3 carried forward, unrepaired'.",
    "world_is": "Repaired before that sentence was written; the repair commit fae9316edb's own subject says 'never prunes (row W60-S3, AC5 stands)', and this seat read 'AC5 stands' as 'the defect stands'.",
    "notes": "The self-test prune matters more under Andrew's 14:58Z word (wide fan-out means more worktrees a self-test can clear).",
    "adjudicates": [
      "AMGT_RESAPP-Z-W60-S3"
    ],
    "dismissal_reason": "Row's defect fixed at 3795d4f487; the residual hazard is round-16 cell C2."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S341",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "DISMISSED: the chain L CTO half was on file in the estate; only rk-53's worktree was stale, and rk-53's criteria were all offline or in-process, inside the path its own refusal clause permits.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CTO half at HEAD @ce9231d095 with an AMGT-rk-53 section; the worktree lacked it (merge-base --is-ancestor ce9231d095 <worktree HEAD> false). Working record s.4e.",
        "rk-53 order :140-141 permits read-only, offline and in-process criteria with a half absent; all seven criteria are pytest or python -c."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "W53-S1: the chain L CTO half is absent.",
    "world_is": "Absent from one worktree, present in the estate; S178 recorded the resolution.",
    "notes": "No new half was owed.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W53-S1",
      "AMGT_RESAPP-Z-S178"
    ],
    "dismissal_reason": "The pair was complete in the estate; the worker acted only inside its refusal clause's permitted set."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S342",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "DISMISSED: two observations of correct behaviour -- an intended reclassification, and a BOM branch our reader already handles.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W48-S1: rk-46 item 5 reclassifies incorporate-by-reference as UNRESOLVED-SOURCE by design (roster.py:258, :811); management tests 73 passed (census s.5).",
        "W44-S1: lib/research/filings/batch.py:279-310 reads the real bytes and handles the BOM schtasks emits (census s.5)."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Each row's concern.",
    "world_is": "Each describes correct behaviour.",
    "notes": "None.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W48-S1",
      "AMGT_RESAPP-Z-W44-S1"
    ],
    "dismissal_reason": "Correct behaviour at HEAD; no remedy owed."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S343",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "DISMISSED: a ruling record, a corrected headline, and a measurement made moot by a later fix.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S175: a disarm/ruling record by 1.0.0_SA_CTO~Z on W31-S3; W31-S3 reads GRADUATED in the census.",
        "S185: ROUND_ANALYSIS.round15.md corrected in place by its owner @daed5dc57b (34 combined cells, 29 terminal, 5 open).",
        "W61-S2: an unauthenticated 401 cannot tell whether %2F survives; C-S312 removed the question and rk-61's router rejoins every segment and unquotes (scoped_amgt.py:3616-3623). The capture limit is C-S316."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Each row's item.",
    "world_is": "Each is closed by the record it cites.",
    "notes": "None.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S175",
      "AMGT_RESAPP-Z-S185",
      "AMGT_RESAPP-Z-W61-S2"
    ],
    "dismissal_reason": "A record row, a corrected document, and a moot measurement."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S344",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T15:40Z",
    "one_line": "DISMISSED: eleven disarm records by 2.0.0_SA_COO~Z (S179-S184, S186-S190) set disposition GRADUATED on their own rows with no remediation row. They record hazard disarms, not findings; each subject is dispositioned in this document.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Each row's one_line begins DISARMS <target>: S179 Z-S177, S180 W50-S3, S181 W39-S5, S182 W60-S2, S183 W60-S4, S184 W62-S1, S186 W58-S2, S187 W39-S2, S188 W61-S1 and W49-S3, S189 W53-S1, S190 W47-S2.",
        "_graduated_without_row at HEAD before this document: 22 items, these eleven among them; a self-set GRADUATED with no remediation row blocks the next slug's GATE (iii) limb."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Each row carries disposition GRADUATED.",
    "world_is": "Each is a disarm record; disposition is L9's, and the self-set value is superseded, as S156's was at C-S293.",
    "notes": "The disarms stand as hazard records. S180's subject W50-S3 lives only on the held branch wk-amgt-14-50 and arrives with rk-49's drain.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S179",
      "AMGT_RESAPP-Z-S180",
      "AMGT_RESAPP-Z-S181",
      "AMGT_RESAPP-Z-S182",
      "AMGT_RESAPP-Z-S183",
      "AMGT_RESAPP-Z-S184",
      "AMGT_RESAPP-Z-S186",
      "AMGT_RESAPP-Z-S187",
      "AMGT_RESAPP-Z-S188",
      "AMGT_RESAPP-Z-S189",
      "AMGT_RESAPP-Z-S190"
    ],
    "dismissal_reason": "Disarm records, not findings; the self-set GRADUATED is superseded, and every subject is dispositioned above."
  }
]
```
