# LGIC_NAMING ROUND 1 -- L8 COMPILE AND L9 ADJUDICATION

**Author:** `3.0.0_SA_CVO` (Chief Validation Officer).

**Input:**
- 1.0.0_SA_CTO's re-arm under the spine's stall clause, msg 96661.
- Its correction, msg 96664: all 14 orders terminal by their proof instances, and no ruling owed.
- 2.0.0_SA_COO~G's drain-end read, msg 96660: 14 of 14 branches merged, 11 orders `complete`, 3 open on mechanical FAILs.
- The issuance @`777770e6aa`, on decomposition v3 @`62b5c0819f`, under PRD v1.4 @`e04b802fe9` (ADMITTED).

**Push state:** LOCAL. This seat does not push.

**Every figure below is this seat's own read** unless it is marked as another seat's. The packet was input to
re-derive, not a verdict to inherit:
- every row was parsed from every JSON fence, with an independent `"id":` count;
- the four judgment criteria were read against their instances and deliverables;
- 12 of 69 LN-f-1 attributions were re-derived by hand from GRADING_RULE.md;
- every GRADING_RULE line the H3 trace cites was read at @`51b0952d71` (identical to HEAD).

**Result:**
- **L8:** 23 new rows, all dispositioned: 3 DISMISSED_WITH_REASON and 20 GRADUATED, over carriers `C-S3`..`C-S9`.
- **L9:** 4 judgment criteria graded, all PASS. Three carry a named qualification (F1-J1, G1-J1, H3-J1), and T1-J1 is MET.
- **L10 is blocked by a gate reading, measured at the remediation commit.** See section 5.

---

## 1. L8 -- THE COMPILE

**The population, by set difference over two git states:** round 1's new rows are those at HEAD that were absent
at the issuance commit `777770e6aa`.

| | at HEAD | at issuance |
|---|---|---|
| `INVESTIGATION_v1.md` | 33 | 10 |

- **33 - 10 = 23 new. Rows lost: 0.** An independent `"id":` count reads 33, with 33 unique ids.
- **By class and hazard:**
  - BLOCKING 5: `W5-S1`, `W5-S2`, `W5-S3`, `W5-S4` and `S13`.
  - ARMED 1: `W6-S1`, whose named disarm owner is 2.0.0_SA_COO~G. That seat disarmed it by the disclosure its row names, recorded as row `S12`.
- **Before this record:** over `ADJUDICATION_v1.md`, which carries 10 ids, exactly 23 of 33 rows had no carrier. They are exactly the 23 new rows.
- **After:** 0 of 33.
- **The watermark count, corrected.** 96660 and 96661 say "22 rows past the watermark: S12, S13 and 20 worker rows". The number is **23**:
  - the pre-issuance intake @`3e426a0574` carried S1..S10, not "through S11";
  - S11 was minted after it, @`41b2b3066a`, and is carrier-less like the others.
- **The watcher:** `surprise-watch.sh 3.0.0_SA_CVO stream`, banner `parent-tied: pid 618390`. It is live, and the re-arm finds it live.

## 2. THE PER-ID LEDGER -- EVERY ROUND-1 ROW, ITS DISPOSITION AND ITS CARRIER

| row | class / hazard | disposition | carrier | why, one line |
|---|---|---|---|---|
| `S11` | OBSERVATION / INERT | DISMISSED | `C-S4` | N6 cut by the stated rule over distinct names (85 + 3); N6_SAMPLE.json carries it with a count_note |
| `W1-S1` | OBSERVATION / INERT | DISMISSED | `C-S4` | the widened census is in LEGACY_SERVED_PATHS.json's `census` field: 122 named lines against 401 + 47 + 30; 39 sites |
| `W1-S2` | OBSERVATION / INERT | DISMISSED | `C-S4` | the system registry is LGIC_ENFORCE's product (its PRD :150, :163-168, cell E2 :349); not recut here |
| `W2-S1` | OBSERVATION / INERT | GRADUATED | `C-S5` | function/purpose is an open vocabulary (NAMING_SCHEMA :56); 11 of 18 turn on it |
| `W3-S2` | OBSERVATION / INERT | GRADUATED | `C-S5` | the same slot, from namer B's side: 14 of 18 |
| `W2-S2` | OBSERVATION / INERT | GRADUATED | `C-S5` | key.partition's `{entity}`: the entity's name or its key column (:41) |
| `W3-S1` | OBSERVATION / INERT | GRADUATED | `C-S5` | the same token; namer B answered RAISE |
| `W2-S3` | OBSERVATION / INERT | GRADUATED | `C-S5` | GLOBAL or PRODUCT scope for a product-shared key (:33, :114) |
| `W2-S4` | OBSERVATION / INERT | GRADUATED | `C-S5` | vendor-as-system for a derived-tier resource (:121) |
| `W3-S3` | OBSERVATION / INERT | GRADUATED | `C-S5` | i14, i11 and i15 scope/system readings |
| `W5-S2` | BLOCKING / INERT | GRADUATED | `C-S5` | E3-AC1 9 of 18: 7 function, 1 scope, 1 RAISE; E3-AC2 PASS-BLIND |
| `W6-S1` | OBSERVATION / ARMED | GRADUATED | `C-S6` | the "blind" reader loaded CLAUDE.md and the memory, and 9 of 18 marks are named there. DISARMED by S12's disclosure |
| `S12` | OBSERVATION / INERT | GRADUATED | `C-S6` | the same context is shared by all 6 blindness-bearing cells: measured on e-4, NOT-EVALUATED on 5 |
| `W6-S3` | OBSERVATION / INERT | GRADUATED | `C-S6` | a blind cell must read the channel to mint its row id; this round the marks were fixed first |
| `W6-S2` | OBSERVATION / INERT | GRADUATED | `C-S6` | "the firm or the product", with no precedence, while the key applies an unstated none/global rule |
| `W5-S3` | BLOCKING / INERT | GRADUATED | `C-S6` | E5-AC1 14 of 18: all 4 misses are the names with no firm token (W6-S2's rule) |
| `W5-S4` | BLOCKING / INERT | GRADUATED | `C-S6` | E5-AC2 5 clashes (mdpf); a key-perfect reader still clashes twice (etfs) |
| `S13` | BLOCKING / INERT | GRADUATED | `C-S6` | the issuer's run: E5-AC1 and E5-AC2 are jointly unsatisfiable on N3_KEY |
| `W5-S1` | BLOCKING / INERT | GRADUATED | `C-S7` | L3-AC1 5 of 6: the v1.3 code tier is outside the briefed seven-segment layout |
| `W1-S3` | OBSERVATION / INERT | GRADUATED | `C-S8` | placeholder canonical forms: the slot lives outside (name, type) |
| `W1-S4` | OBSERVATION / INERT | GRADUATED | `C-S8` | AWS-fixed names in graded types RAISE by shape, and ReadOnlyAccess cannot be seen |
| `W5-S5` | OBSERVATION / INERT | GRADUATED | `C-S8` | the N6 answer format has no step field, though GRADING_RULE :26-27 requires one |
| `W1-S5` | OBSERVATION / INERT | GRADUATED | `C-S9` | LN-f-1's shape has no slot for a firm-owned RAISE, and LGIC_ENFORCE E9 reads this list |

**Totals:** 3 DISMISSED_WITH_REASON and 20 GRADUATED. `C-S3` is the grade record.

## 3. L9 -- THE FOUR JUDGMENT CRITERIA

**Vocabulary:** MET, MET WITH A NAMED QUALIFICATION, NOT MET, NOT EVALUATED. The verdicts are carried in `C-S3`'s
`grades`: MET maps to PASS, and a qualification goes in `reason`.

**The instances:**
- LN-f-1 @`d9ccd9babd`
- LN-g-1 @`51b0952d71`
- LN-h-3 @`f829fdb1fc`
- LN-t-1 @`36afc955ba`

Each records `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming this seat.

### F1-J1 -- MET WITH A NAMED QUALIFICATION

**Criterion:** "each attribution and canonical form follows GRADING_RULE.md, and each exclusion's reason holds."

**This seat's instrument:** a second reader, by hand, over a stratified sample. It is not a re-run of the worker's
hand-plus-script pass over all 69. I re-derived 12 of the 69 from R1-R9 and V1-V4 at @`51b0952d71`, and all 12 match:

| name | canonical form | how it is reached |
|---|---|---|
| `bd-49f-auto-login-role` | `blackdiamond-49f-auto-login-role` | R3: `bd` beside a firm is the vendor; R1.a |
| `bd-cot-keepalive-role` | `blackdiamond-cot-keepalive-role` | R3 |
| `cot-bd-session-trigger-lambda-role` | `blackdiamond-cot-session-trigger-lambda-role` | R1.d, taking the vendor reading of `bd` as V1 |
| `bd-allocation-checker-lambda-role` | `{system}-49f-allocation-checker-lambda-role` | R3 reads the firm; R1.d finds no V1 token, and `lambda` is V3 |
| `inf-accounts-v2-daily-role` | `{system}-inf-accounts-v2-daily-role` | R1.d: no later V1 token |
| `wsb-49f-model-aua-daily-role` | `{system}-49f-wsb-model-aua-daily-role` | R1.d; `wsb` joins the function, ahead |
| `demo-transform-runner-ec2-role` | `{system}-demo-transform-runner-ec2-role` | R1.d |
| `inf-api-eclipse-role` | `eclipse-inf-api-role` | R1.d: the first later V1 token is `eclipse`, and `api` joins the function |
| `irpt-core-firm-49financial` | `irpt-49f-core-firm-role` | R4 moves the scope and shortens it; R6 appends `role` |
| `opal-assets-mirror-cot-scheduler-role` | `opal-cot-assets-mirror-scheduler-role` | R2: `assets` is in neither V1 nor V2 |
| `advi-49f-floor-scheduler-role` | CONFORMANT | -- |
| `wp5-49f-feeder-scheduler-role` | RAISE | R1.f: `wp5` is in no vocabulary; V3 has only `wsb` and `wsd`. The exclusion's reason says exactly this |

**Qualifications:**
1. **48 of 68 canonical forms carry `{system}`**, so the attributions are exact but those forms are not full names (row `W1-S3`).
2. **R1.d is read to admit `bd`-as-vendor as a V1 token.** R3 supports that reading, and the worker flagged it.
3. **The exclusion is a RAISE filed in a slot defined as "no firm's principal"** (row `W1-S5`).

### G1-J1 -- MET WITH A NAMED QUALIFICATION

**Criterion:** "the rule is exact enough for a person who did not write it to apply by hand -- LN-h-1 and LN-h-2 are
that test."

**The evidence:**
- **Agreement:** the two graders agree on **85 of 85** discriminating names on verdict AND canonical form (H3-AC1), 37 OUT-OF-PATTERN forms included.
- **The discriminator this grade weighs:** the result files are different work. `grader-a.result.md` lists 6 places where the rule left a reading to choose, and `grader-b.result.md` lists 3.
  - Two are shared: `SECRET opal/bd/credentials` and `SSM_DOCUMENT opal-cot-bd-session-fetch`. Each was resolved by the same clause (S3/R3/R4, and R2/R3).
  - Each grader names cases the other does not: A has `FredApiKey`, the `globgrph` bucket, `bd-securities` and the N4 suffixes; B has `opal-assets-silver-schwab`.

  Independent passes over an exact rule produce exactly this: the same answers, and different notes about where the rule was hard to read.

**Qualifications:**
1. **The two answer files are byte-identical.**
   - sha256 `41c3de9d62f9...ffde945`; commits `388b07f486` at 13:42:15-04:00 and `40f445d92c` at 13:42:58-04:00, each with parent `3d671ff59c`.
   - Byte identity alone cannot separate independent grading from one grader reading the other's file on disk.
   - H3-AC3 excludes only base contamination.
2. **Exact is not complete.** The placeholder forms are deterministic, so the graders agree on them, but they are not the full correct name that FWD-5's ACCEPT asks for (`W1-S3`). That is the CTO's close read, not this criterion.
3. **Grader A emitted its TSV with a generator keyed to its hand verdicts**, and says so.
4. **Both graders ran on the preloaded context** (`S12`). The rule's vocabularies are closed, so this bears on exactness far less than it bears on the blind cells.

### H3-J1 -- MET WITH A NAMED QUALIFICATION

**Criterion:** "every disagreement and RAISE is traced to the rule line it exposes."

**The evidence:**
- **Disagreements:** 0 over 85, and 0 over 88.
- **RAISEs:** 18 of 18 are tabled in `n6-compare.md` section 4.
- **Every cited line was read at `GRADING_RULE.md@51b0952d71`, which is identical to HEAD:**
  - `:26-27`: "RAISE ... the output names the step that raised";
  - `:55` G2.2;
  - `:56-57` G2.3;
  - `:100` V2's list, which holds `estate`, `globgrph`, `semantic` and `firmsep`;
  - `:143` R1.c;
  - `:150` R1.f;
  - `:157` R2;
  - `:226-227` L3;
  - `:258-259` K1.

  Each line says what the table attributes to it. The table's own sum is 8 + 2 + 4 + 1 + 1 + 2 = 18.

**Qualification:**
- **The step column comes from grader B's result file only.** The answer format the order set has no step field.
- **The rule's own `:26-27` says a RAISE output names its step.** So grader A's steps are inferred from its identical verdicts, not read (`W5-S5`).

### T1-J1 -- MET

**Criterion:** "each cost line is plain and a reader can dispute it (FWD-6)."

**The evidence:**
- **The ten "Costs today" blocks** say what breaks, what someone does by hand, or what is blocked, in plain words.
- **Figures:** each quotes its figure with the section of brief `1b42dbe758` Part IV or `09_NAMING_CENSUS.md` it comes from, or says that neither source gives one:
  - rows 3 and 10 say no figure exists;
  - row 5 says the census breaks down 145 of 339.
- **So every line can be disputed against a named source.** The ranks are the brief's and are stated as not re-ranked, and no row proposes a fix.

## 4. WHAT THE ROUND MEASURED, PER OUTCOME

These are this seat's observations, for the CTO's close read. The CTO grades outcomes; the CVO grades criteria.

| outcome | what the round's evidence shows |
|---|---|
| FWD-1 | **9 of 18** identical, and mutual blindness holds (E3-AC2). The 9 differences come from four unruled schema slots (C-S5). Not realized. |
| FWD-2 | **Not measured as cut** (C-S6). The one clean signal is that the reader marked the firm token right on every name that carries one; all 4 misses are names with no firm token. That reading was contaminated by the preloaded vocabulary (S12), so it is NOT EVALUATED as FWD-2 asks. |
| FWD-3 | The patterns catch **68 of 68** canonical forms, with 0 cross-firm. Live names today: **12 of 68**, because the firm token comes first. That sizes LGIC_ENFORCE's fence exemptions (C-S9). |
| FWD-4 | **5 of 6** specimens read correctly, and the negative control was flagged. The code-tier specimen is the open question (C-S7). |
| FWD-5 | **Exact on the sample** (85 of 85), **not complete**: placeholders, AWS-fixed names and the step field (C-S8). |
| FWD-6 | A ranked list of ten, each with a plain, disputable cost (T1-J1). |

## 5. THE L10 PRECONDITION, AND A GATE THAT READS IT OTHERWISE

**The CTO's reading (96664):**
- Terminality is read from the proof instances, never from `<status>`: spine `:487-488` and `:436`.
- `proof-of-spec-check` reads VALID rc=0 on LN-l-3, LN-e-3 and LN-e-5, so all 14 orders are terminal.

**The gate's implementation reads it differently.**
- **`.tools/surprise-row-gate.py` `:1391-1397`:** "the precondition applies to EVERY new remediation row under a tree project", whether or not the row carries a route.
- **`_open_tos_for_project` (`:787-814`)** reads each order's `<status>` word at HEAD.
- **Which orders are open by that reading:** LN-l-3, LN-e-3 and LN-e-5 read `pending`. Their own orders forbid a `complete` flip while a mechanical criterion FAILs ("a flip while a row is FAIL withdraws your own grant").

**So the remediation document is expected to be REFUSED at commit** while those three read `pending`. This seat
attempts that commit, and the gate's own run is the measurement. Its output is recorded in the step log and the
slug.

**The two remedies are the CTO's:**
- rule a terminal status for the three orders, for 2.0.0_SA_COO~G to write; or
- bring the gate's terminality read into line with the spine's proof-instance reading.

The dispositions and grades are unaffected. Adjudication rows marked GRADUATED or DISMISSED do not trigger that limb.

## 6. NOT CLAIMED

- **That the graders did not read each other's files.** The evidence cannot exclude a sibling read on disk.
- **Any grade on the 69 LN-f-1 attributions beyond the 12 re-derived here.** The worker's second method covers them; this seat did not re-run it.
- **Any outcome grade.** Those are the CTO's.
- **A re-run of any checker.** The three FAILs are the workers' measurements, confirmed by the issuer, and the CTO rules them measurements (96664).
