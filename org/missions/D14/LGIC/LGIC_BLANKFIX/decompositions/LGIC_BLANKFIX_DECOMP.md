# LGIC_BLANKFIX decomposition -- ROUND 1, the thread: one folder of infrastructure, every line actionable (issuer 2.0.0_SA_COO~G; cut 2026-10-07)

**Status: CUT for one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** PRD v0.2 @47ef4c98cc, ADMITTED (`python .tools/prd-signoff.py status LGIC_BLANKFIX`: ratified-text SIGNED by
`3.0.0_SA_CVO`, current; brief half admitted because `4.0.0_SA_CRO` wrote the brief). Receiving check: `prd-manifest` OK, 1 ACCEPT.
Brief `docs/briefs/d14-naming-check-blank-fixes-brief-20261007.md` @af5d8b6df4.

**The rectangle is the PRD's section 2 (THREAD), seven hops, on ONE root.** Nothing of the section 3 backlog is cut here.

## Measured at the base (HEAD ce2f42661d, 2026-10-07, laptop; repo plane only, no live pull)

Instrument: `opal_naming.census_repo()` then `grade()` per item, each `RaiseDefect` caught, the 462 inherited cards
(`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/NOT_JUDGED_R13.json`) applied. Denominator: 1,962 repo items =
1,622 judged + 333 carded + 7 raising.

1. **The check has no root scope.** `census` takes `--names`, `--live`, `--repo`, `--report`, `--budget`, `--not-judged` and nothing
   else (`lib/opal_naming.py:2899-2906`). Manifest row S01 is confirmed: a scoped run is a build.
2. **No Terraform root holds a storage key with a blank in its own `.tf` files.** Of the 111 repo-plane key and bucket blanks, 110 sit
   in source files (Lambda sources and `config.py`), 1 in a root (`investor-reporting`, a bucket). So "one root that holds all four
   groups" is only satisfiable when a root is read WITH the Lambda source folders it deploys. That reading is this cut's, stated
   here; `BF-t-1` builds it and prints how each source folder was tied to its root.
3. **`bd-pipeline` read that way holds all four groups.** `infra/aws/terraform/bd-pipeline/`: 96 judged, 12 `{system}` blanks, 9
   `{cadence}` blanks, 0 raising, 0 carded. `infra/aws/lambda/bd-pipeline/`: 37 judged, 16 `{source}/{scope}` blanks, 0 raising, 6
   carded. The brief's proposed root stands on this measurement; `BF-t-1` re-measures it with the built scope and records the pick
   (PRD ruling 4). `inf-pipeline` is the only other pair holding all four (60 / 10 / 32, plus 12 pattern rows) and is three times the
   size.
4. **The 12 `{system}` rows of the root split 5 / 7 on data the registry already holds.** Lead word in `systems.json`
   `refused_keys.purpose_word` (`s3`, `cloudwatch`, `invoke`): 4 rows; one PascalCase inline policy name
   (`AdditionalPermissions`): 1 row. Those 5 are group A. Lead word in `refused_keys.generic_noun` (`pipeline`, `runner`, `gold`,
   `events`, `cloudfront`): 7 rows, group B. `events` and `cloudfront` are AWS service words filed under `generic_noun`, so Andrew's
   ruling 3 does not reach them through the existing lists; moving a word between those lists is registry vocabulary
   (`4.0.0_SA_CRO`'s lane) and no cell does it.
5. **The cadence vocabulary cannot name every schedule in the root.** V6 is `1min`, `5min`, `daily`, `hourly`, `monthly`, `weekly`.
   The root's expressions include `rate(15 minutes)` (`bd-49f-interim.tf:151`), weekday-only crons (`MON-FRI`, `MON-SAT`) and one
   rule with an `event_pattern` and no schedule (`bd-49f-session-chain.tf:246`). C-CADENCE's unmeasured question has a first answer:
   the expression alone does not always yield a V6 word. `BF-t-4` lists every such row; it adds no vocabulary.
6. **The root has no brace pattern; it has one `%s` pattern** (`silver/%s/`, group D). All 15 brace rows of the estate are elsewhere
   (12 under `infra/aws/lambda/inf-pipeline/`).
7. **LGIC_ENFORCE's tests are not green at the base.** `python -m pytest lib/tests/test_opal_naming.py -q`: 6 failed, 87 passed. The
   six: `test_grade_agrees_with_every_worked_case` for `inf-silver-chain|LAMBDA`, `opal-portal-data-proxy-api|API_GW`,
   `Inflection-SilverChain-DimConversionFailure|CW_ALARM`, `wsb-49f-model-aua-pull-daily|SCHEDULE`, `inf/otp-relay/token|SECRET`; and
   `test_lambda_plane_consumers_is_import_aware_not_a_bare_substring`. C-CHECK says those tests "must stay green"; the bar a cell can
   meet is "no failure outside these six". Filed as row `LGIC_BLANKFIX-S1`.
8. **Who reads a verdict value** (native search for `OUT-OF-PATTERN` over tracked code and data, snapshots and scratch excluded):
   `lib/opal_naming.py`, `lib/tests/test_opal_naming.py`, `lib/opal_lgctfm.py`, `.tools/naming-gate.py`,
   `.tools/naming-apply-gate.py`, `.tools/safe-apply.sh`, `infra/logic/render_naming_section.py`,
   `infra/logic/registry/exemptions.json`, `org/standards/NAMING_SCHEMA.json`. A fourth value reaches all nine.
9. **A new registry-side file moves no generated view unless a target reads it.** Each generated file's mark is scoped to the
   registry files that target reads (`_target_registry_files`, `lib/opal_naming.py:140`). The root map of hop 4 is read by no
   generated target, so landing it is not a deploy under C-GENERATED. `BF-t-3` confirms this with `generate` into a scratch folder.

## Rule 24 record

**The cell set.** Domain: the seven hops of the PRD's THREAD on one root. Subtraction from the printed hop list:

| hop | cell |
|---|---|
| 1 Pick, 2 Run | `BF-t-1` |
| 3 Group A | `BF-t-2` |
| 4 Group B | `BF-t-3` |
| 5 Group C | `BF-t-4` |
| 6 Group D | `BF-t-5` |
| 7 Read | `BF-t-6` builds the one line per name; the read itself is the issuer's one real run at the close |

Seven hops, six cells, none uncovered. Same grain: each cell is one module with one test file. One intent each. State: a cell's
status is one of `NOT_EVALUATED`, `PASS`, `FAIL`, `REFUSED`; every cell is `NOT_EVALUATED` at the cut.

**The line kinds `BF-t-6` prints** (a schema this cut authors). Domain: every name the scoped run meets.

| kind | meaning | counted as broken |
|---|---|---|
| `RIGHT` | the name is correct as written | no |
| `FIX` | wrong, and the complete correct name follows | yes |
| `NOT-ASKED` | this kind of name is not asked to carry the missing part, with the reason | no |
| `PATTERN` | a code pattern with a variable part, shown as a pattern | no |
| `CARDED` | skipped by a card the repository already holds, the card named | no |
| `HOLE` | none of the above could be completed; what is missing is named | yes |

MECE by precedence in that order of test: `CARDED`, `PATTERN`, then the grade (`RIGHT` / `NOT-ASKED` / `FIX`), and `HOLE` for a
`FIX` whose name still carries a blank or a name that raises. Same grain (one name). One intent (what the reader is told). State:
only `HOLE` fails the run. FWD-1's ACCEPT names three kinds; `PATTERN` and `CARDED` are the two this cut adds so that no line is
silently dropped, and whether each is an acceptable line under FWD-1 is the CTO's grade, not this cut's.

**The key classes `BF-t-5` assigns.** Domain: every storage-key item of the root whose graded form carries `{source}` or `{scope}`.
`PATTERN` (the key has a variable segment: a brace, `%s` or `*`), `LEGACY` (it matches an entry of
`infra/logic/registry/legacy_addresses.json`), `ADDRESS` (source and scope filled from the root's map entry), `UNDECIDED` (none
applies; the reason named). Tested in that order, so the classes are disjoint and `UNDECIDED` is the remainder.

**The fourth verdict value (C-VERDICT) is NOT set by this cut.** The PRD assigns its four-postulate record and token census to
`1.0.0_SA_CTO` "at the cell's cut". Draft for that seat, with the census this seat ran:
- Proposed value: `NO-SYSTEM-ASKED`. Domain: every `(name, type)` `grade()` returns a verdict for. It takes the names whose lead
  token is in `refused_keys.purpose_word`, PascalCase single-token policy names, and `LAMBDA_LAYER` names, when no later token
  and no registry row resolves a system: the population that today returns `OUT-OF-PATTERN` with `{system}` (base, repo plane:
  80 + 4 purpose-word, 19 PascalCase, 3 layers = 106 of 141).
- MECE: the four values partition on two questions asked in order: is a system asked of this kind of name, then does the grammar
  hold. Same grain. Intent: one axis, the grade. State: a registry row never moves a `NO-SYSTEM-ASKED` name; only a rename does.
- Token census: `NO-SYSTEM-ASKED`, `NOT-SYSTEM-BEARING`, `SYSTEM-EXEMPT`, case-insensitive, over the working tree: the only hits are
  5 files matching the looser `no-system` (three IRPT briefs, one DSGN_AMGTV1 order and its proof), none in naming code or data. An
  exact word-boundary count over all 60,806 tracked files timed out at 20 s and is owed with the record.
- The schema text that says "there is no fourth" (`grade.unplaceable`, `grade.not_graded`) moves with the row.

`BF-t-2` is cut STAGED on that record.

## The cells

The root throughout: `infra/aws/terraform/bd-pipeline/` with the Lambda source folders it deploys (base: `infra/aws/lambda/bd-pipeline/`).

| cell | what | serves | hop | placement | risk | status |
|---|---|---|---|---|---|---|
| `BF-t-1` | the root scope: given a Terraform root, the names the check reads for it (the root's `.tf` names plus the names in the Lambda source folders that root deploys, each folder's tie to the root printed); and a table of every root with its counts of the four groups, raising names and carded names. Records the pick. | FWD-1 | 1, 2 | laptop | LOCAL | NOT_EVALUATED |
| `BF-t-2` | the fourth verdict: `grade()` returns it for a group-A name with no blank in its printed form; the schema row; the two naming gates handle it; a group-B name still returns `OUT-OF-PATTERN` | FWD-1 hop 3, FWD-3 | 3 | laptop | LOCAL | NOT_EVALUATED, STAGED |
| `BF-t-3` | the root map reader: one map entry says which system, firm and source a root's names belong to, with named exceptions; a group-B name of the root reads its system from it. Proposes the `bd-pipeline` entry, checked against the registry rows that already place names of that root. | FWD-1 hop 4, FWD-7 thin | 4 | laptop | LOCAL | NOT_EVALUATED |
| `BF-t-4` | the cadence word: for each schedule and event rule of a root, read its own expression from the `.tf` and give the V6 word, or list the row with the expression and why no word fits | FWD-1 hop 5, FWD-4 thin | 5 | laptop | LOCAL | NOT_EVALUATED |
| `BF-t-5` | the key classes: each storage key of the root classed `PATTERN`, `LEGACY`, `ADDRESS` or `UNDECIDED`, an `ADDRESS` printed whole with the source and firm from the root's map entry | FWD-1 hop 6, FWD-4 and FWD-8 thin | 6 | laptop | LOCAL | NOT_EVALUATED |
| `BF-t-6` | the root check: one line per name of the root in one of the six kinds, the fills of `BF-t-2` to `BF-t-5` applied, a count per kind, exit non-zero when any line is a `HOLE` | FWD-1 | 2, 7 | laptop | LOCAL | NOT_EVALUATED |

Risk is `LOCAL` by the act (code, tests and records; no cell deploys, renames or writes the registry). Where the L6 gate's floor for
an infrastructure path in `<paths>` reads higher, the order carries the gate's class and says the act is read-only.

## Interfaces fixed at the cut

`BF-t-6` is built against these; a cell that cannot meet its line refuses and files a row.

- `lib/opal_naming_scope.py`: `root_items(root) -> (items, stats)`; `items` are `census_repo()`'s dicts (`plane`, `type`, `current`,
  `where`); `stats` carries `root`, `tf_files`, `source_dirs` and, per source folder, the basis that ties it to the root.
  `root_table() -> list[dict]`, one per root. CLI: `python lib/opal_naming_scope.py table` and `... items <root>`.
- `lib/opal_naming_rootmap.py`: `load_map(path) -> dict`; `resolve(map, root, name, type) -> dict | None` with `system`, `scope`,
  `source`, `basis` (`root-default` or `exception`). The map's path is an argument; no default path is baked.
- `lib/opal_naming_cadence.py`: `cadences(root) -> list[dict]` with `type`, `current`, `where`, `expression`, `word` (or `None`),
  `basis`.
- `lib/opal_naming_keyfill.py`: `fill_keys(items, root_entry) -> list[dict]` with `current`, `where`, `class`, `canonical` (or
  `None`), `basis`.
- `lib/opal_naming.py` `grade(name, type)`: signature unchanged; the fourth value is returned as the verdict.
- `lib/opal_naming_rootcheck.py`: `check_root(root, map_path, not_judged=None, out=print) -> int`. CLI: `python
  lib/opal_naming_rootcheck.py <root> --map <path>`.

## Dependency edges

- `BF-t-3 -> BF-t-5`: a key's source and firm come from the root's map entry.
- `BF-t-1 -> BF-t-6`, `BF-t-2 -> BF-t-6`, `BF-t-3 -> BF-t-6`, `BF-t-4 -> BF-t-6`, `BF-t-5 -> BF-t-6`: the root check consumes each.

Maximal paths (the spine's chain): `t-1 > t-6`, `t-2 > t-6`, `t-3 > t-5 > t-6`, `t-3 > t-6`, `t-4 > t-6`. Five paths; `BF-t-3`'s two
share a worker. `fanout: 4 of 5 chains, cap 8`: slot `~1` takes `BF-t-1` then `BF-t-6`; slot `~2` takes `BF-t-2` when its record
lands; slot `~3` takes `BF-t-3` then `BF-t-5`; slot `~4` takes `BF-t-4`. `BF-t-6` is handed only after the other five are merged.

## Write sets (disjoint)

- **BF-t-1:** `lib/opal_naming_scope.py`, `lib/tests/test_opal_naming_scope.py`.
- **BF-t-2:** `lib/opal_naming.py`, `lib/tests/test_opal_naming.py`, `org/standards/NAMING_SCHEMA.json` (the verdict row and the two
  sentences that deny a fourth), `.tools/naming-gate.py`, `.tools/naming-apply-gate.py` (each gate's tests are its own `--self-test` arms; neither has a
  separate test file at the base).
- **BF-t-3:** `lib/opal_naming_rootmap.py`, `lib/tests/test_opal_naming_rootmap.py`; the proposed entry is a file in its deliverables.
- **BF-t-4:** `lib/opal_naming_cadence.py`, `lib/tests/test_opal_naming_cadence.py`.
- **BF-t-5:** `lib/opal_naming_keyfill.py`, `lib/tests/test_opal_naming_keyfill.py`.
- **BF-t-6:** `lib/opal_naming_rootcheck.py`, `lib/tests/test_opal_naming_rootcheck.py`.
- Each: its deliverables folder and the investigation file.
- **No cell writes `infra/logic/**`.** `lib/opal_lgctfm.py`, `.tools/safe-apply.sh` and `infra/logic/render_naming_section.py` read a
  verdict and are outside this project's write surface (PRD section 4): `BF-t-2` reads each and files a row for any that mishandles
  the fourth value.

## Battery

Thread round. `comp-schedule`, `comp-adversary` and every catalog lens: `DECLARED-NOT-APPLICABLE` -- "thread round; the lens runs on
the enrichment round that touches its surface". `comp-iam`: `DECLARED-NOT-APPLICABLE` -- the thread reads IAM policy NAMES from `.tf`
text and grants, attaches and simulates nothing. `comp-blast lib/opal_naming.py`: RUN, `SUBJECT_ABSENT_FROM_CORPUS` over 29,531
graph nodes (vintage 2026-10-07 10:41:15 UTC): the graph does not hold `lib/`, so the consumer list is base measurement 8, a text
search, blind to a consumer that builds the verdict string at run time.

## The issuer's acts after the drain

1. **Hookup, one commit:** `census --root <root> [--map <path>]` in `lib/opal_naming.py`'s `main`, dispatching to
   `opal_naming_rootcheck.check_root`. It belongs to no cell.
2. **The map entry goes to `4.0.0_SA_CRO`** (C-REGISTRY): `BF-t-3`'s proposed entry, handed as content; that seat lands the file under
   `infra/logic/**` and names its path. Until it lands, hop 4 is fed by the proposal file and the thread is NOT done.
3. **The one real run:** `python lib/opal_naming.py census --root infra/aws/terraform/bd-pipeline --map <the landed file>`, every
   line read by this seat, the output committed under `deliverables/2.0.0_SA_COO~G/`. It is FWD-1's trace.
4. **Hygiene at each merge:** `python -m pytest lib/tests -q` and `.tools/commit-gate.sh` on the touched files; the bar is base
   measurement 7.

## Carried to the round's close for `1.0.0_SA_CTO` (measured here, decided by no cell)

1. Base measurement 2: a root read without its Lambda sources never shows group D.
2. Base measurement 4: `events` and `cloudfront` lead group-B rows though they are service words.
3. Base measurement 5: `rate(15 minutes)`, weekday crons and a pattern-only rule have no V6 word, so hop 5 will print `HOLE` lines
   on this root unless the vocabulary or the rule moves.
4. The 6 carded names of `infra/aws/lambda/bd-pipeline/` print as `CARDED`, which is none of FWD-1's three kinds.
5. Base measurement 7: the tests C-CHECK relies on are red at the base.
