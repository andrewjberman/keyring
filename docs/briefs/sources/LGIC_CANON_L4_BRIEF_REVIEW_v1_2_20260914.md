# LGIC_CANON v1.2 — L4-R brief review

Author: `4.0.0_SA_CRO` · UTC: 2026-09-14 ~18:40Z · request: CTO messages 96678 (delivery) and 96679 (change note).

**VERDICT: REFUSED, brief half.** One ground, R1. DEC-2's criterion was restated at v1.2, but its consuming cell C2
still carries v1.1's criterion word for word. So this half now states two different acceptance bars for FWD-1, and
one of them is the bar v1.2's own note says the ledger cannot meet. The vocabulary correction itself is right and is
accepted below. The fix is one table cell plus the version note's last sentence.

## Exact inputs and scope

- PRD: `org/missions/D14/LGIC/LGIC_CANON/prd/LGIC_CANON_PRD.md@d9977a0f40a2a25b42a42271c0fad58aa7e07044`, v1.2,
  346 lines, 31,850 bytes. At review, HEAD and worktree both matched the pinned bytes (`cmp` against `git show`, and
  `git diff --quiet`).
- Brief: `docs/briefs/d14-pipeline-canon-brief-20260912.md@a4cc0cb681b7fde2b7fa0f9f92a27ee77b0435e3`, the same pin as
  the v1.1 review. Heading denominator re-measured at the pin this session: **18 headings**, the same as v1.1.
- Reviewed brief-half SHA-256: `5443fa0e7bc0a448e80ca0423e1bc701d61280bb226d0eb699dd7bc175fd326a`, computed by
  `prd_signoff_lib.half_hashes` on the pinned bytes. It matches the notifier's `5443fa0e7bc0`.
- Ratified-text half, identified but not signed here: `43fa46d2a86f5474d6600060010bdf51a99d449299cb0a0415008df3faa1620b`.
  It is identical to the value recorded in the v1.1 review, which corroborates the CTO's statement that ENDPOINT and
  CONTRACTS are byte-unchanged.
- Prior review: `docs/briefs/sources/LGIC_CANON_L4_BRIEF_REVIEW_v1_1_20260914.md@ff2766b31663f1c1cb526be5a1afd8b5ba5b8b2c`,
  which SIGNED v1.1 at brief half `ef2339f180c10169817df8a1aca23789b358781c02c073cf10f30b20fce77fd7`.
- Conformance ledger read at the PRD pin: `infra/logic/06_CONFORMANCE_LEDGER.md@d9977a0f40`, v0.3, 169 lines.
- Decomposition read at HEAD (not pinned; it is the COO's artifact, cited only for the observation):
  `org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md`.

## The change, v1.1 to v1.2

`git diff 56608aadd4 d9977a0f40` on the PRD: 1 file, 12 insertions, 2 deletions, in the `prd_version` header and two
hunks. The hunks are the version note (lines 60–66) and DEC-2's tree bullet (lines 171–173).

**Accepted, with the checks that support it:**

1. **The ledger has no CONTRADICTS value.** Word-boundary token census of the ledger's bytes at the pin:
   CONFORMANT 24 · MIGRATE 35 · RETIRE 20 · DECLARED EXCEPTION 3 · AWAITING 4 · **CONTRADICTS 0**. The instrument
   was a regex over `git show` output at the pin. It differs from the CTO's 18:2xZ read of the reports directory, so
   this is corroboration, not repetition.
2. **The brief supports the restatement.** Brief O1 (lines 38–45) asks whether a tree "conforms, departs, or is a
   declared exception". In the brief, CONTRADICTS appears only in O3's contradiction-report vocabulary (lines 11, 57
   and 59) and in two provenance lines (159 and 249). The ledger's values are O6's vocabulary (lines 79–80). So v1.2's
   "a row where the tree breaks a canon rule" is closer to O1's "departs" than v1.1's wording was.
3. **The v1.2 criterion is meetable from the ledger as written, inside one pipeline.** MDPF has MIGRATE rows at ledger
   :98 (bronze) and :100 (gold destination), and exception X1 is GRANTED and PERMANENT at :130. Separately, the
   ledger's own §7 counts ETFs under "MIGRATE (format only)" (:147). So by the ledger's classification, :102 is a
   rule-breaking row.

## R1 — C2 still carries the v1.1 criterion (the refusal ground)

| Pinned line (v1.2) | Text |
|---|---|
| 171–173, DEC-2 | "The tree is chosen from the conformance ledger so that it carries at least one row where the tree breaks a canon rule (a MIGRATE or RETIRE row; the ledger has no CONTRADICTS value, which is the contradiction reports' word) and one DECLARED EXCEPTION." |
| **272, CELL CANDIDATES, C2, inputs column** | "a real pipeline tree chosen from the ledger with at least one CONTRADICTS and one DECLARED EXCEPTION" |
| 66, version note | "Nothing else moved." That is accurate as a description of the diff, and it is the defect. |

**Why this binds the brief half.**
- C2 is FWD-1's consuming cell and carries brief O1 (coverage row 3).
- CELL CANDIDATES sits in the brief half: `prd_signoff_lib.RATIFIED_SECTIONS` is `('ENDPOINT', 'CONTRACTS')`, and the
  brief half is everything else.
- The standard for this review is that the brief's content reaches the consuming cell. Here the cell carries the
  criterion v1.2 itself says "could not be met from the ledger as written", while DEC-2 now says something else.
- A task order's worker face inlines cell text, and the L9 grader grades against the cell. Either reader can pick up
  the unmeetable bar.

**Fix, returned by pinned line:**
- v1.2:272, C2's inputs column. Replace it with: "a real pipeline tree chosen from the conformance ledger with at
  least one row where the tree breaks a canon rule (MIGRATE or RETIRE) and one DECLARED EXCEPTION".
- v1.2:66. Replace "Nothing else moved" with a sentence naming C2 as the second carrier.
- No other line needs to change.

**Every place the half uses the term.** Every `CONTRADICT` occurrence in v1.2:
- lines 62–65: the version note
- line 141: the O3 contradiction-report contract (correct; this is the reports' own word)
- line 172: DEC-2 (correct)
- line 188: DEC-4, IRPT_BCKEND's three CONTRADICTS (correct; contradiction-report vocabulary)
- line 272: C2 — **stale**

Only line 272 is stale.

The decomposition also quotes DEC-2's v1.1 wording (`LGIC_CANON_DECOMP.md:61`) and flags the reading (its §0.5 and
§8 choice 3). That file is not in this half and is not a refusal ground.

## Unchanged since v1.1

Apart from the two hunks above, the brief half is byte-identical to v1.1. So the v1.1 review's audit of all 28
coverage entries (18 headings plus 10 bold findings IV.1–IV.10) stands, except for R1. No coverage row changed.

## Observation, not a refusal ground (filed as `LGIC_CANON-S2`)

The decomposition (`LGIC_CANON_DECOMP.md:59-65, :179, :333-334`) chooses the ETFs tree: the rule-breaking row at :102
(`opal-data-etfs/gold/`, 32 JSON objects against R11) plus X4 GRANTED at :133. The ledger does not put those in one
tree:
- X4's pipeline column reads "Pathfinder, TrueShares".
- The ledger places their planes in the monolith (:52–54, `pathfinder/…` and `trueshares/…`, under §1), not in
  `opal-data-etfs`.
- The `opal-data-etfs` tree's own exceptions are OWED: X3 (:132) and X5 (:134). Its rows read "DECLARED EXCEPTION X3
  once the reason is written … until then AWAITING" (:101) and "AWAITING X5" (:103).

If DEC-2's "the same real pipeline tree … carries" means one tree, the chosen pairing may cross pipelines. MDPF meets
the bar inside one pipeline (:98 and :100 MIGRATE, X1 GRANTED at :130). Choosing the tree is the decomposition's job
and grading it is L9's, so this is recorded as a surprise row, not as a refusal ground. Whether "the ETFs pipeline"
spans Pathfinder/TrueShares ingest was not measured here.

## Verification and limits

This is requirements acceptance only. It does not claim that the renderer exists, that blind readers ran, or that any
ledger count was re-derived by script. The ledger itself says its §7 counts were "re-derived by hand" (:157–158).

Per 96679 (relaying Andrew's ~18:2xZ word, 96672 item 3, which this seat did not read), LGIC_CANON has no issuer, so
this refusal blocks no issuance. Once R1 is fixed, a v1.3 whose only other changes are the two lines named above
needs no re-audit beyond those two lines.

The delivered notices 96678 and 96679 were opened and READ-acked on the broker ledger. This seat performs no push,
deploy or cloud mutation. Push state is measured and stated in the completion message to `1.0.0_SA_CTO`.
