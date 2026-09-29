# AMGT_CORPUS -- L5 decomposition v7.0 -- ROUND 7 (the enrichment round after the round-6 analysis)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-26 ~18:xxZ. **Source:** `1.0.0_SA_CTO~Z`'s round-6 analysis
`ledger/ROUND_ANALYSIS.round6.md` @`1e53f322f3` (glyph fix @`ffcadcbc0b`) section 6, six items, cut from `3.0.0_SA_CVO~Z`'s
`ADJUDICATION_v9` @`37a8542a71`. Round 6's decomposition is kept as `AMGT_CORPUS_DECOMP.round6.md`. PRD v0.6 @`9e326e11c1`,
both halves SIGNED current (ADMITTED). Delivered by file while the MCP send path is down fabric-wide.

## 0. What this round IS, by subtraction from the analysis's six items

| item | disposition |
|---|---|
| 1 `Z-S45`'s reader build, BLOCKING | cell `CRPS-i-1`: the continuation readers select on `method_version` |
| 2 the 0.33 floor -- earn it or state it UNCALIBRATED | cell `CRPS-i-2`: the served Base case carries its band WITH ITS CLAIM (ceiling measured, floor uncalibrated). Earning it is not possible from this population: no name sits within 0.2 of 0.33 on either side (h-2 @`6d18367755`) |
| 3 AC4's workbook half | cell `CRPS-i-3`: h-2's producer captures the value BESIDE the label (196 of 200 Base-labelled cells had an empty `right` list) and SELECTS the team's written Base-case cell by a stated rule, cited by coordinate |
| 4 `Z-W2-S10`'s three pre-`g-1` blocks | inside `CRPS-i-2`'s drain: the re-derive that serves the band claim re-mints every block key, these three with it |
| 5 `Z-S39`'s `*` case | cell `CRPS-i-4`: a standing census that no glob/fnmatch pattern is built from a security key, with a positive control |
| 6 a fresh 19-outcome pass | cell `CRPS-i-5`, spawned AFTER the drains of i-1 and i-2 (a pass that reads before the fixes land repeats g-4's vintage hole) |

**NOT cells:** FWD-12 limb 3's render and FWD-11's render (AMGT_RESAPP's; FWD-11 owned there by FWD-31 @`c2c6c507d6`), and
FWD-10/FWD-15's render halves (same seam). No machine formula for any case is cut.

## 1. The rectangle -- five cells `CRPS-i-<n>`, cut by WRITE SET (no two cells write one file)

| cell | slot | serves | `<risk>` | class | write set (`<paths>`, plus the channel) | the build |
|---|---|---|---|---|---|---|
| `CRPS-i-1` | `~1` | FWD-18 (Z-S45) | SERVED (the drain's continuation + dossier rewrite) | worker | `lib/research/corpus/continuation.py`, `lib/research/corpus/substrate.py`, `lib/research/corpus/tests/test_continuation_reader_method.py` (new) | both input-matching readers prefer the object whose `method_version` is the producer's current one; among equals, the last write |
| `CRPS-i-2` | `~3` | FWD-12 guard (floor), Z-W2-S10 | SERVED (the drain's re-derive of every block key) | worker-light | `integrations/bloomberg/research/model_block_pull.py`, `integrations/bloomberg/research/tests/test_band_basis.py` (new) | SERVED and `outside_band` Base cases carry an additive `band_basis` naming each bound's value and calibration claim; `cases-report` prints it |
| `CRPS-i-3` | `~2` | FWD-12 AC4 workbook half | LOCAL | worker | `deliverables/0.9.0_WK_AMGT_CORPUS~2/case_evidence.py`, `CASE_EVIDENCE_ROUND7.json`, `CASE_EVIDENCE_ROUND7.md` | right-hand neighbours captured; one selected Base-case cell per workbook by a stated rule, cited by coordinate, beside the served Base case |
| `CRPS-i-4` | `~4` | Z-S39 | LOCAL | worker-light | `lib/research/corpus/key_glob_census.py` (new), `lib/research/corpus/tests/test_key_glob_census.py` (new) | a read-only census of glob/fnmatch/rglob/iglob call sites under `lib/research`, flagging a pattern built from a security key, with a planted positive control |
| `CRPS-i-5` | `~5` | FWD-1..FWD-19 | LOCAL | worker | `deliverables/0.9.0_WK_AMGT_CORPUS~5/FWD_EVIDENCE_ROUND7.json`, `.md` | one evidence row per outcome against served state AFTER the i-1 and i-2 drains; no grade |

## 1a. Re-groundings at L5

- **i-1:** `continuation.read_latest` and `substrate._pick_stored` both return the FIRST sorted key whose `inputs` equal
  current inputs; `inputs` carries no method version; object names are `sha16({method_version, inputs})`. Census
  @`070cf35da9`: a /2 rewrite would be served on 49 of 95 and not on 46. `_pick_stored` serves four tables (continuation,
  sector template, fund form, typecast); each carries `method_version` on its documents.
- **i-2:** `CASE_BAND_LOW = 0.33`, `CASE_BAND_HIGH = 3.0` (`model_block_pull.py:1076-1077`); a SERVED base today carries
  `ratio_to_px_last` and `band: [0.33, 3.0]` with no claim. h-2 @`6d18367755`: 2 names inside 2.5-3.0 and NFLX 0.043
  outside (the ceiling discriminates); the 0.33-0.5 bin EMPTY, nearest accept RWE_GR 0.537, the only sub-floor name BA_US
  refused for a different cause (the floor has never refused anything).
- **i-3:** `case_evidence.py` reads `ws.max_column` in openpyxl `read_only` mode, where the sheet's stored dimension is
  commonly stale; 196 of 200 Base-labelled cells came back with `right == []` (ADJUDICATION_v9 s.2(A)). The CTO's adjudication
  @`bfc179c2ea` rules that quoting a number the team wrote, with its locator, is extraction, not generation.
- **i-4:** Z-S39: three of 89 keys carry a metacharacter (`BP/_LN_Equity`, `NG/_LN_Equity`, `WALMEX*_MM_Equity`); the `/`
  is escaped as `-SLASH-` on the paths measured, the `*` is not; zero key-interpolating glob sites existed when filed.
- **i-5:** 19 outcomes FWD-1..FWD-19 in the PRD header; the round-5 pass @`95b6f068ed` read 10 REALIZED (after correction A2).

## 2. Rule 24 record, for what this file ADDS

i-1's pick is a total order over input-matching objects: current method first, then last write, then key name. i-2's
`band_basis` carries two claims over one closed pair of values (`measured` / `uncalibrated`), each with its basis; it moves no
served number and no disposition. i-3's selection rule is printed on every selected row and the neighbourhood stays beside it.
i-4 flags; it changes no key. i-5's `state` enum is the round-5 one (`met` / `unmet` / `unmeasurable`).

## 3. Placement and holds on others' surfaces

i-2 on the Bloomberg lane's puller, granted by `<paths>` for this order only (as e-2, f-2 and g-1 were). i-1 and i-4 on this
project's corpus package; i-3 and i-5 in their workers' deliverables. `Z-S46` holds every `continuation --write` at this seat
until i-1 drains.

## 4. Dependency edges, keyed to OBSERVED completion

- i-1, i-2, i-3, i-4 are independent at build time; i-5 is ISSUED with them and SPAWNED after the i-1 and i-2 drains land.
- i-1 -> the census `stale_pick 0` -> the continuation rewrite (95 names, METHOD_VERSION /2) under a never-widen pair -> the
  dossier rewrite for the names whose continuation moved -> `Z-S46` lifts.
- i-2 -> the re-derive of every block key from landed raw (no vendor call) under a derive-pair addendum -> verify: every
  SERVED base carries `band_basis`, no served value and no disposition moved, and the three `Z-W2-S10` keys carry band and
  currency fields.
- i-3 -> laid out for the CVO at L8 (AC4, judgment).

## 5. The round -- one issuance, fan-out as data

- **ONE issuance covers all 5 cells.** `fanout: 5 of 5 chains, cap 8, reason: five cells by write set; i-5 waits on two
  drains by edge, not by a second issuance.`
- **Drain duties owed by this seat, in order, every verify leg reading CONTENT (R-5):**
  1. At every merge: the suites, `py_compile`, ruff, beside `safe-merge.sh`'s row gate; each worker re-graded at its tip.
  2. i-2 VALID: `cases-report` over every block key (read-only) -> the expected outcome for the addendum; re-derive under a
     change entry; verify on the served reader: values and dispositions unchanged by key, `band_basis` present on every served
     base, Z-W2-S10's three carrying band and currencies.
  3. i-1 VALID: the census; a never-widen pair for the continuation rewrite and the dossier rewrite, expected outcome read
     from the producers' rules; verify `stale_pick 0` with `current_method_available 95`, and every served pillar carrying
     `terms`.
  4. Spawn i-5 on the post-drain state; i-4's census last.
  5. The COO's one real run of each outcome; the packet prints `graded this round / graded ever / endpoint denominator` (R-4).
- Surprise channel: `org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md` (seat rows to
  `Z-S46`; workers mint `AMGT_CORPUS-Z-W<n>-S<k>`, `disarm_owner 2.0.0_SA_COO~X`).

## 6. `<preflight>` -- what this decomposition actually ran

```
prd-signoff.py status AMGT_CORPUS        v0.6 @9e326e11c1; both halves SIGNED current; ADMITTED
task-order status census (last <status>)  34 of 34 complete on this project -> 0 open
cases-report (SAN FP, CAT US)             'cases SAN_FP_Equity base SERVED ratio 2.566...', 'cases_report served 2 refused 0'
continuation pick census                  @070cf35da9: /2 would be served 49, /1 46 (Z-S45)
checks as files                           org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round7/*, each run once at the base
```

## 7. comp-adversary declaration

This file specifies; it produces no artifact. The adversary lens applies at the drain's served acts (the re-derive, the
continuation and dossier rewrites), each under its pair in section 5.

## 8. Rulings this decomposition makes, and what it REFUSES to assume

- i-1 selects on method version in the READER; it does not add `method_version` to `inputs` (that would move every dossier's
  inputs a second time).
- i-2 moves no bound and no served number; the claim is a disclosure, and "earn the floor" stays open for a population that
  has names near it.
- i-3's selection is extraction of a number the team wrote, never a computed case; the CVO grades whether it reads as the
  team's Base case.
- REFUSED to assume: that the empty `right` lists are a sheet layout rather than a reader defect (i-3 measures it); that the
  `*` key is exploited anywhere (i-4 counts).

## 9. Holds

| hold | on | owner | what lifts it |
|---|---|---|---|
| every `continuation --write` (`Z-S46`) | this seat | `2.0.0_SA_COO~X` | i-1 VALID and its census |
| the continuation + dossier rewrite | this lane's drain | `2.0.0_SA_COO~X` + `1.0.0_SA_CTO~Z` (pair) | i-1 drained; `stale_pick 0` |
| the block re-derive | this lane's drain | `2.0.0_SA_COO~X` + `1.0.0_SA_CTO~Z` (addendum) | i-2 VALID; the addendum signed |

-- `2.0.0_SA_COO~X`
