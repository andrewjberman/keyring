# AMGT_CORPUS -- L5 decomposition v8.0 -- ROUND 8 (the enrichment round after the round-7 analysis)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-28 ~23:5xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-7 analysis
`ledger/ROUND_ANALYSIS.round7.md` @`03327ebbf9` section 5, four cells, answering `3.0.0_SA_CVO~Z`'s slug on
`ADJUDICATION_v10`. Round 7's decomposition is kept as `AMGT_CORPUS_DECOMP.round7.md`. PRD v0.6 @`9e326e11c1`, ADMITTED
(ratified-text SIGNED current; brief auto-admitted).

## 0. What this round IS, by subtraction from the analysis's list

| item (analysis s.5) | disposition |
|---|---|
| 1 case BODY extraction + the rewrite under a pair, carrying the round's JUDGMENT | cell `CRPS-j-1` |
| 2 FWD-9's five sites | cell `CRPS-j-2` |
| 3 the derive's stamp selection (`Z-S47`) | cell `CRPS-j-3`, **RE-GROUNDED** at L5 (s.1a): the rule it serves changed under it |
| 4 `read_dossier` prefers the current method version | cell `CRPS-j-4` |

**NOT cells** (the analysis's own list): the workbook reader (s.2 ruling 2); the `Z-W2-S11` correction row (this seat's,
filed with this issuance); the temp-dir removal (Andrew's word).

## 1. The rectangle -- four cells `CRPS-j-<n>`, cut by WRITE SET

| cell | slot | serves | `<risk>` | class | write set (`<paths>`, plus the channel) | the build |
|---|---|---|---|---|---|---|
| `CRPS-j-4` | `~1` (first) | FWD-17 (b), FWD-12 (the served pick) | LOCAL | worker | `lib/research/corpus/dossier.py` (the reader + a read-only `--pick-census`), `lib/research/corpus/tests/test_dossier_reader_method.py` (new) | `read_dossier` prefers the object whose `method_version` is the producer's current one, else the pre-existing pick |
| `CRPS-j-1` | `~1` (second) | FWD-12 limb 3 data half, FWD-16 cases | SERVED (the drain's rewrite) | worker | `lib/research/corpus/dossier.py` (the case resolver, the method-aware no-op, `METHOD_VERSION` /2, `--case-census`, `--write --workers N`), `lib/research/corpus/tests/test_dossier_case_body.py` (new) | each case carries the text UNDER its heading, cited; the census prints body / heading-only / absent per case over 95 |
| `CRPS-j-2` | `~2` | FWD-9 | LOCAL | worker-light | `lib/research/corpus/key_glob_census.py`, `lib/research/corpus/induction_run.py`, their tests | the code census reads `unresolved 0` with rc 0; the plant still flags |
| `CRPS-j-3` | `~3` | FWD-12 guard (served Base cases), `Z-S47`, `Z-W2-S10` | LOCAL (no re-mint this round, s.8) | worker | `integrations/bloomberg/research/model_block_pull.py` (stamp selection + a read-only `stamp-census` stage), `integrations/bloomberg/research/tests/test_stamp_inputs_selection.py` (new) | the derive reads the newest landed raw stamp that carries the current rule's inputs; the census says per key which stamp does, or that none does |

j-4 and j-1 share `dossier.py`, so they are ONE chain on ONE worker (j-4 first: j-1's method bump needs j-4's pick).

## 1a. Re-groundings at L5

- **j-1 (measured @`e3fd90cb63`).** `_resolve_section_block_from_picks` joins the lead line and every item up to the next
  section lead OR the next short bold line (docx) / standalone heading that is not lead-only (pdf). The served value for all
  102 of 102 case slots is the heading alone (row `Z-W5-S3`; the CVO's direct read of AZN_LN_Equity:
  `cases.base = {"value": "Base Case", "citation": {"passage": "Base Case", "locator": 0}}`), so the block ends at the line
  after the heading. **A second defect the rewrite would hit:** `write_one` skips a name when the stored `inputs` equal
  fresh `inputs`, and `inputs` carries no method version; a case fix alone (even with a `METHOD_VERSION` bump) would write 0
  on every name. The no-op must compare method version too -- the same class as round 7's `Z-S45`, on the dossier's own table.
- **j-4.** `read_dossier` picks newest `as_of` date, then greatest `LastModified`; it never reads `method_version`. After a
  /2 rewrite, last-write-wins serves /2, but any later /1 write (a rollback, a stale writer) would be served over it.
- **j-2 (the census's own mechanism, `readonly_proof.py` `_origin`).** `key_glob_census.py:199` writes into
  `tempfile.TemporaryDirectory(...)`, which `_origin` does not classify (it knows `tempfile.mkdtemp` and
  `tempfile.gettempdir` as SAFE), so the binding reads `unknown`. The four `induction_run.py` sites (:462 :464 :688 :690)
  write under `deliverables_dir = deliverables_dir or DELIVERABLES_DIR`: a caller-supplied parameter, statically unknown.
- **j-3 -- THE PREMISE MOVED (row `Z-S51`, filed with this issuance).** `Z-S47` diagnosed stamp selection losing PE_RATIO
  history under the round-7 rule. At 18:36Z today `0.9.0_WK_AMGT_RESAPP~166` @`b56fef3032` moved the Base case to ONE rule,
  `lib/research/api/case_rule.py` (adjusted P/E = median of (PX_LAST/f)/IS_COMP_EPS_ADJUSTED over closed years), and
  `model_block_pull._compute_cases` now delegates to it. Measured over the 97 block keys by `cases-report` (read-only,
  `evidence/r8_base_cases_report_all_20260928T234706Z.log`): SERVED 69 (round 7: 49); 21 ABSENT -> SERVED, 1 SERVED ->
  ABSENT (CAT_US, act A's re-mint); 48 of 48 served-in-both carry a different ratio. Six keys read "no adjusted P/E history
  on the landed block": 6861_JP, BZLFY_US, CAT_US, CSL_AU, PBR_US, TSM_US. The cell's intent -- a derive that reaches the
  landed raw carrying the rule's inputs -- is unchanged; its population is those six under the CURRENT rule.

## 2. Rule 24 record, for what this file ADDS

j-4's pick: current method first (newest date, then last write, then key), else the pre-existing pick; a total order.
j-1's case census partitions every case slot of every resolved name into exactly one of `body` / `heading_only` / `absent`,
and the three sum to `names x 3`. j-3's stamp census partitions each key into `newest_carries` / `older_carries` /
`none_carries`, summing to the keys read.

## 3. Placement and holds on others' surfaces

j-3 is on the Bloomberg lane's puller, granted by `<paths>` for this order only (as i-2 was); it reads landed raw only, never
the vendor, and does not touch `lib/research/api/case_rule.py` (AMGT_RESAPP's rule). j-1, j-2, j-4 on this project's corpus
package.

## 4. Dependency edges, keyed to OBSERVED completion

- Chain A: j-4 -> j-1 (same file; j-1's `METHOD_VERSION` bump is served only through j-4's preference) -> the drain's
  dossier rewrite (`--write --workers N`, 95 names) under a never-widen pair -> the CVO grades the judgment on the served table.
- Chain B: j-2 alone. Chain C: j-3 alone (its re-mint is not this round's act, s.8).

## 5. The round -- one issuance, fan-out as data

- **ONE issuance covers all 4 cells.** `fanout: 3 of 3 chains, cap 8, reason: j-4 and j-1 share dossier.py and run as one
  queue; j-2 and j-3 are independent.`
- **Drain duties owed by this seat:** at every merge the touched suites, `py_compile`, ruff, beside `safe-merge.sh`'s row gate;
  each worker re-graded at its tip. Chain A VALID -> the pair (COO half: expected outcome read from `write_one`'s own rule,
  both branches; CTO half) -> change entry -> `dossier --write --workers N` -> verify `--case-census heading_only 0`, one new
  object per name, `read_dossier` serves it 95 of 95, `--pick-census stale_pick 0`. The one real run: `read_dossier` on a
  docx name and a PDF-only name, case text read by this seat.
- Surprise channel: `surprise-channel/investigations/INVESTIGATION_v1.md` (seat rows to `Z-S52`; workers mint
  `AMGT_CORPUS-Z-W<n>-S<k>`, `disarm_owner 2.0.0_SA_COO~X`).

## 6. `<preflight>` -- what this decomposition actually ran

```
prd-signoff.py status AMGT_CORPUS        v0.6 @9e326e11c1 EXECUTING -> ADMITTED; ratified-text SIGNED current
task-order census (last <status>)         CRPS-i-1..i-5 complete -> 0 open on this project
cases-report over 97 keys (read-only)     served 69 refused 28 under case_rule.py @b56fef3032 (s.1a)
checks as files, dry-run at the base      checks/round8/*: j1_AC1 j1_AC2 j4_AC1 j4_AC2 j2_AC1 j3_AC1 j3_AC2 FAIL as expected;
                                          j2_AC2 (plant_flagged 1), j2_AC3 (152 passed), j3_AC3 (unserved_vs_base 0 of 69) PASS
```

## 7. comp-adversary declaration

This file specifies; it produces no artifact. The adversary lens applies at the drain's served act (the dossier rewrite),
under its pair.

## 8. Rulings this decomposition makes, and what it REFUSES to assume

- j-1 fixes the case block's END, not its start: the lead stays the case's own heading; the value is the text under it. A case
  whose block has no text under the heading reads `heading_only` in the census and is served as ABSENT with a reason, never as
  its heading.
- j-1 makes the no-op compare `(method_version, inputs)`, keeping FWD-17 (b): a rebuild with unchanged inputs AND method
  writes nothing.
- j-2 resolves the sites in the CODE (a SAFE temp root; a statically resolved deliverables root), never by changing the
  census's classification (the analysis: "needs no census schema change").
- j-3 changes stamp SELECTION only; it moves no rule. **No block re-mint runs this round:** under the new rule a re-derive
  would move 48 served ratios and 22 dispositions (`Z-S51`); that is a served change on AMGT_RESAPP's rule, raised at the
  round-8 packet, not taken as a rider.
- REFUSED to assume: that the case text sits in the next paragraph (j-1 measures where it sits, docx and PDF); that an older
  landed stamp carries the adjusted inputs (j-3 counts).

## 9. Holds

| hold | on | owner | what lifts it |
|---|---|---|---|
| the dossier rewrite | this lane's drain | `2.0.0_SA_COO~X` + `1.0.0_SA_CTO~Z` (pair) | chain A VALID; the pair signed |
| any model-block re-derive | this lane | `2.0.0_SA_COO~X` | a round-8 ruling on `Z-S51` |

-- `2.0.0_SA_COO~X`
