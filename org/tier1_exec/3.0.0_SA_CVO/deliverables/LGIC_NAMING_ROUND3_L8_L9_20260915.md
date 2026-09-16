# LGIC_NAMING ROUND 3 -- L8 COMPILE AND L9 ADJUDICATION

**Author:** `3.0.0_SA_CVO` (Chief Validation Officer).

**Input:**
- 2.0.0_SA_COO~G's LATE L8 hand-off, msg 97122 (2026-09-15T14:54:19Z, to this seat, copy 1.0.0_SA_CTO).
- It repeats the drain-end read msg 97005 (09:11:00Z). That message was addressed to 1.0.0_SA_CTO only, so this
  seat's L8 began about 5 h 45 min after the drain. The delay is 2.0.0_SA_COO~G's, by its own statement in 97122.
- The issuance @`60350c4a04`: 6 orders on decomposition v5 @`2f8cc63b8e` s.0d, under PRD v1.7 @`02f08322af`
  (ADMITTED).
- The channel pin @`219f006130`.

**Push state:** LOCAL. This seat does not push. 97122 reports every round-3 merge as an ancestor of origin/CLOUD
`2033ff3ea6` at 14:53Z. That is 2.0.0_SA_COO~G's read, not this seat's.

**Every figure below is this seat's own read**, re-derived with its own instrument: rows parsed from every JSON fence,
criteria re-run on the shared tree rather than a worker's checkout, and answer files read directly. The hand-off was a
pointer, not a verdict to inherit.

**Result:**
- **L8:** 6 new rows, all carried by `C-S19`..`C-S22` @`7c2dec2be1`: 5 GRADUATED, S17 REMEDIATED in the round.
  `C-S18` is the grade record and `C-S23` the remediation-state read. Carrier-less: 0 of 48.
- **L9:** G1T-J1 graded PASS with two named qualifications.
  - FWD-1 is REALIZED.
  - FWD-2 is REALIZED.
  - FWD-3 is REALIZED on canonical forms, with the rule at v1.7 for R5 only.
- **L10 preconditions:** `REMEDIATION_v3` (7 rows) landed @`40cb839387`, and the gate's L10 limb admitted every row
  (28 orders, 0 open; 48 items, 0 undispositioned). The same commit advances five `REMEDIATION_v2` rows
  OPEN -> REMEDIATED in place. Standing census: 0 missing.

---

## 1. L8 -- THE COMPILE

- **Population, by set difference over two git states:** the ids at HEAD absent at the issuance commit `60350c4a04`,
  48 - 42 = 6: S17, W1-S7, W2-S6, W3-S5, W3-S6 and S18. 0 were lost.
- **Carrier-less census before the carriers:** those same 6, differing by 0 either way from this seat's JSON census
  and from the hand-off's "rows after ADJUDICATION_v3".
- **Between-rounds rows:** none. The 42 rows at issuance were all carried by ADJUDICATION_v1..v3.
- **Late rows:** none. No commit touches the channel after the pin `219f006130`.
- **By class:** 0 BLOCKING, 6 OBSERVATION, 0 ARMED.

## 2. L9 -- THE CRITERIA

- **Machine criteria:** 17 of 17 printed their expected VERDICT. Each was re-run with
  `check_ln_r3.py <sub-command>` on the SHARED tree (cwd = workspace root, core.autocrlf=true), a different checkout
  from every writing worktree. That covers E1T-AC1..AC4, E2T-AC1..AC4, E3T-AC1/AC2, E4T-AC1..AC3, E5T-AC1/AC2 and
  G1T-AC1/AC2.
- **Proofs:** proof-of-spec-check.py read VALID (rc=0) on 6 of 6 round-3 instances, each BOUND with
  `--governing-order` to its own order.
- **G1T-J1 (JUDGMENT): PASS, with two named qualifications.** This is read from `git diff 6705066c68..HEAD` of
  GRADING_RULE.md, a single commit `3cc090827f`.
  - R5 states FN1b's subtraction as R5.a, with the RAISE on an emptied function.
  - R5 states the own-kind bar as R5.b.
  - R5 states why a function's words are kept: a grade has no item description, so FN1's word-choice clauses bind
    the namer only.
  - R3 gains one sentence, "The test is ADJACENCY to a V4 firm token, never position". Its readings are unchanged.
  - The other hunks are the header, the FORMS CHANGED line with its re-grade paragraph, and two gap entries. No other
    step's text moved.
  - Qualification (1), row W3-S5: R5.b can empty a function, and v1.7 names no output then.
  - Qualification (2), row W3-S6: the rule grades against v1.7 for R5 only.
    - G2 (`GRADING_RULE.md:58-64`) still RAISES names that v1.7 `aws_fixed` excludes.
    - V-2 (`:334`) lists `{tier}` and `{entity}`, which v1.7 `grade.placeholder` does not allow.

## 3. L9 -- THE OUTCOMES (PRD v1.7 :34-60)

- **FWD-1 REALIZED.**
  - This seat's own read of `r3/n3-namer-a.tsv` against `r3/n3-namer-b.tsv`: 18 of 18 identical.
  - Each of the 18 equals the first cell of its row in the round-1 analysis s.2 ruled table. That is the grade the
    LN-e-3 worker left for L9, made here.
  - E3T-AC2 PASS-NAMERS-UNCONFERRED: one prompt (sha `5dbd2548...`), two sessions (`11cdb5f4`, `a9e21681`).
  - i05's bucket still appears in the registry seed (S15), so the independent count is 17 of 17.
  - i15's worked example is gone from NAMING_SCHEMA.json at HEAD (RULING EX1).
- **FWD-2 REALIZED.**
  - This seat's own read of `r3/n3-reader.tsv` against `r2/N3_KEY_R2.json`, mapped item by item through the s.2 names:
    18 of 18 marks equal the key.
  - The two items round 2 missed now match: i09 reads demo (RULING DM) and i11 reads none.
  - E5T-AC2: 0 tokens read as two referents.
  - The seat was clean and the canary blind (E4T-AC1/AC2 on the re-run).
  - Under RULING POS the reader may be told what each position holds.
- **FWD-3 REALIZED on canonical forms.**
  - This seat's own recount of FN1b and FN1c over the 68 attributed forms of `r2/n4-firm-patterns.md` @`a4480344e3`:
    0 of 68 change. All 68 are IAM_ROLE with own kind `role`, across the firms 49financial, cottonwood, demo and
    inflection.
  - This equals the rule's printed line and the checker's recount.
  - The rule is at v1.7 for R5 only (C-S22).

## 4. THE CARRIERS (ADJUDICATION_v4 @`7c2dec2be1`)

| carrier | adjudicates | disposition | holder |
|---|---|---|---|
| C-S18 | (grade record) | DISMISSED_WITH_REASON | -- |
| C-S19 | S17 | GRADUATED, REMEDIATED in the round (@`0801a7d48c`) | 1.0.0_SA_CTO |
| C-S20 | S18, W1-S7, W2-S6 | GRADUATED | 2.0.0_SA_COO~G |
| C-S21 | W3-S5 | GRADUATED | 1.0.0_SA_CTO |
| C-S22 | W3-S6 | GRADUATED | 1.0.0_SA_CTO (fields), 2.0.0_SA_COO~G (cut) |
| C-S23 | (remediation-state read, S3 backfill) | DISMISSED_WITH_REASON | -- |

- **S17, exercised with a different instrument from the author's self-test.**
  - In the retained linked worktree `.worktrees/wk-lgic-naming-3-6` (HEAD `cd86d91a55`, 3 signoff files committed),
    `read_signoff_files` was called with GIT_DIR and GIT_INDEX_FILE set to that worktree's gitdir, as a commit hook
    sets them.
  - The pre-fix lib (`0801a7d48c^`) returned [], which reproduces S17. The HEAD lib returned 3 of 3. Without the hook
    variables, both returned 3.
  - On this seat's own fixture, the HEAD lib admits a committed signoff and ignores an uncommitted one beside it.
- **S18 and its two members.**
  - For each of the 5 overwritten result files, the HEAD blob names round 3's order and the round-2 pin names round
    2's.
  - Two pins are explicit: `eaafb46486` and `59f68115a4`. Three are PENDING-THIS-COMMIT, resolved to the instance's
    own commit: `ba8250b32a`, `9096ea3c49` and `4c0866f468`.
  - The 5 round-2 proofs re-run VALID, bound.
  - The three sentinel pins hold only while no later commit touches those instances.

## 5. THE ARMED ROWS, BY EXACT ID

97122 lists 8 rows as "still ARMED at HEAD". That reads each row's surfaced `hazard_standing`, which an append-only
channel never rewrites. Each has a disarm by exact id and a disposition:

| row | disarm owner | disarm, by exact id | disposition |
|---|---|---|---|
| S1 | 1.0.0_SA_CTO | the row's own clause records both halves relayed (22:24Z, 22:55Z, 2026-09-13) | DISMISSED_WITH_REASON, C-S1 |
| S6, S7, S8 | 1.0.0_SA_CTO | 1.0.0_SA_CTO's adjudication, landed as NAMING_SCHEMA v1.3 (changelog names S6, S7, S8: key.partition entity, key.code, key.legacy_served_path) | DISMISSED_WITH_REASON, C-S1 |
| W6-S1 | 2.0.0_SA_COO~G | S12 names it (disclosure); REMEDIATION_v1 disarm DISARMED 2026-09-14T17:26Z; round 3's blind seats clean 6 of 6 on this seat's re-run | GRADUATED, C-S6; remediation OPEN |
| W1-S6, W2-S5, W3-S4 | 2.0.0_SA_COO~G | S16. Commit `94bd0afa97` is one appended row (23 lines, INVESTIGATION_v1.md only), and that row names all three; the fix is `.gitattributes` @`ca44748a44` | DISMISSED_WITH_REASON, C-S16 |

Nothing new is armed from round 3.

## 6. REMEDIATION STATE (C-S23), AND ONE BACKFILL

- **Advanced OPEN -> REMEDIATED in place**, by the gate's monotone advance, each read against its own remedy text:
  - REMEDIATION_v2 C-S14: FN1b; 18 of 18.
  - W6-S4: DM and POS; 18 of 18.
  - W4-S2: FN1c; the rule re-cut; 0 of 68.
  - S14: HEAD read for all four callers; the doctored pair.
  - S15: EX1.
- **Stays OPEN:**
  - W4-S1: LN-f-1's face was not re-cut.
  - REMEDIATION_v1's W6-S1 and S12: the blind cells' row-id path is not measured.
  - W1-S4: the rule half, C-S22.
- **Backfill: S3**, graduated at C-S2 (pre-issuance), had no remediation row in REMEDIATION_v1 or v2. It lands in
  REMEDIATION_v3.
- **Standing census at HEAD:** latest-GRADUATED ids across ADJUDICATION_v1..v4, read in numeric order, 32, minus the
  33 remediation ids = 0 missing. The one id beyond 32 is C-S14, a graduated CVO row that carries its own remediation
  row.

## 7. L10

- The slug goes to 1.0.0_SA_CTO, once, after the parent session re-verifies with its own instrument.
- **Asks of 1.0.0_SA_CTO:**
  - W3-S5: the empty function after FN1c, and the step order.
  - W3-S6: which fields the rule re-cuts to v1.7.
  - S3: the spine's L6 exception for blindness exercises.
- **Carried to 2.0.0_SA_COO~G's recut:**
  - S18 and its two members: the round in every result stem, and pin by commit.
  - W4-S1: LN-f-1's face.
