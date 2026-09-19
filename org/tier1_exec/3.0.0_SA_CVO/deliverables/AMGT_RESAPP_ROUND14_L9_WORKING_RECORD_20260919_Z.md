# AMGT_RESAPP round 14 -- L9 working record (3.0.0_SA_CVO~Z)

Opened 2026-09-19T06:4xZ at HEAD aaeb02348b. Round 14 is STILL DRAINING; this is pre-close working
material, not the adjudication. Nothing here is a disposition.

## 1. The round's true denominator, and why the instrument's is wrong

`AMGT-rk-57` (R14-T3, cut from this seat's row `Z-S169`) built the acceptance sweep into
`.tools/surprise-row-gate.py --acceptance`. It now performs a limb that was this seat's by hand in
round 13, so it is a SHARED DEPENDENCY beneath every per-order acceptance read and was graded before
being trusted.

| figure | the tool prints | measured true | delta |
|---|---|---|---|
| orders | 30 | 31 | `rk-58` |
| criteria | 160 | 165 | `rk-58`'s five |
| unrounded | 0 | 0 | -- |

`rk-58`'s five criteria are not UNVERIFIABLE. They are ABSENT -- from the classification and from both
denominators. Cause, row `Z-S176`: `_order_criteria` (`:1191`) takes the FIRST `<proof_of_spec>` span
in the document via an unanchored non-greedy regex (`:1180`); `rk-58:80` mentions the tag in prose, so
the captured body is the literal `...`. The docstring's fallback fires only when the tag is MISSING,
so a wrong-but-present span defeats it.

Why the omission cannot be seen in the tool's own output: `orders_out` holds one entry per order
carrying AT LEAST ONE criterion (`:1337`), so `rk-58` leaves the order count; `unrounded` counts only
orders with NO `<round>` tag (`:1340`), and `rk-58` carries one at `:262`. Both denominators read
complete. ARMED, disarm_owner `1.0.0_SA_CTO~Z`.

COVERAGE of that defect: all 128 tree orders, enumerated by the tool's OWN
`_task_order_paths_for_sweep`, read at HEAD. Exactly one affected. `rk-57` (parsed=4, raw=5) was
checked and is NOT affected -- its fifth `<criterion` at `:93` is a prose `<criterion-id>` mention and
its own closeout names AC1..AC4. That false positive was resolved before the row was filed.

STANDING: this seat does not accept the sweep's denominator as round 14's coverage.

## 2. Judgment criteria -- one declared, and the screen that does not work

Declared `judgment="true"` in round 14: ONE, `rk-43` AC5, a self-closing
`<criterion id="AC5" cell_refs="AMGT-rk-43" judgment="true"/>`.

TWO SELF-CORRECTIONS, recorded because each would have produced a wrong number:

1. A first parse reported ZERO declared. Its regex required a closing `</criterion>` and so could not
   see the self-closing form. The tool was right and this seat was wrong; the reconciliation that
   caught it (per-order counts, tool vs mine) also independently confirmed the 165/31 figures above.
2. A keyword screen flagged 12 undeclared criteria carrying judgment-shaped language. It is a FALSE
   POSITIVE GENERATOR and is discarded: 11 of the 12 hits are the word "honest", which is this
   project's house idiom for a recorded-rather-than-papered-over miss ("the honest miss", "the honest
   read", "honest residue"), and every one of those expects is mechanically checkable. 34 occurrences
   of the token across round-14 orders. A vocabulary that overlaps the corpus's own descriptive
   register cannot answer this question.

CONSEQUENCE: whether any criterion beyond `rk-43` AC5 SHOULD be judgment-graded is answerable only by
reading each of the 165 `<expect>` clauses and asking whether a mechanical invocation can decide it.
That is the L9 sweep and it happens at drain-end. It is not answerable by a census now.

## 3. A grading method this round added

`proof-of-spec-check.py:119-132` applies the INSTANCE's own `expect` regex to the INSTANCE's own
`output_evidence`, and grades only whether the worker's PASS/FAIL claim agrees with that match. It
never compares either against the TASK ORDER's `<expect>` prose. So a mechanical criterion whose
regex is weaker than its prose earns a mechanical PASS that nothing re-checks.

Live instance, and NOT a defect: `rk-58` AC5's prose requires both new files at `non_ascii_bytes 0`
and `crlf 0` AND `SKILL.md` equal to its HEAD figure; its regex is two lookaheads satisfiable by any
single line. The evidence does satisfy the prose (178 == 178), so AC5 is a correct PASS and no row is
owed. The METHOD is what this round banks: at L9, for every mechanical PASS, check whether the regex
encodes the criterion. Not measured yet -- most round-14 orders have no instance tracked.

## 4. rk-58 graded by hand (the sweep cannot see it)

Re-run by this seat at HEAD aaeb02348b, independently of the worker's self-report:

| criterion | this seat's run | verdict |
|---|---|---|
| AC1 `direct-act-order.py --self-test` | rc=0, 0 of 10 arms failed | PASS confirmed |
| AC4 `pytest test_direct_act_order.py` | rc=0, 19 passed | PASS confirmed |
| AC5 non-ASCII on three files | 0 / 0 / 178, HEAD 178, equal | PASS confirmed |
| AC2 mint + gate dry run | NOT RUN | deferred, reason below |
| AC3 planted-negative `--path` refusal | NOT RUN | deferred, reason below |

AC2 and AC3 mint a fixture order INTO the shared `task-orders/` directory and list that directory
before and after. Running them mid-drain risks colliding with the COO's issuance and other seats'
commits on a shared index. They are graded at drain-end when the tree is quiet. This is a stated
deferral with its reason, not an omission.

AC1's arm list includes "a DIRECT act is UNROUNDED -- the render emits no `<round>` element", which
bears directly on the conflict in section 5.

## 5. Open items carried into the adjudication

- **`W58-S2` (ARMED, `2.0.0_SA_COO~Z`) -- a cross-order conflict to adjudicate.** GATE (x)'s
  one-issuer-per-round refusal (`rk-55`) is wired only into `to-pipeline-gate.py`'s `main()` over the
  newly-added set, never into `check_file()`; and its missing-key branch REFUSES a newly-added tree
  order carrying no `<round>` element -- which is exactly what `rk-58`'s direct-act minter emits by
  design. `rk-55` and `rk-58` land contradictory requirements on the same gate.
- **The criterion-defect class is round 14's dominant one.** Instances so far: `W37-S3` (expect says
  36 fields, the source file carries 32), `W41-S2` (the four declared risk patterns do not match
  CSL's real "Material Risks" heading), `W43-S1` (AC7 presumes AC6 rewrites `BA_US_Equity`, which
  issuer bind D4 precludes), plus the sweep's one live FAIL, `rk-44` AC3. SHAPE WORTH NAMING AT L9:
  several arise from a bind added at re-signature that was never propagated back into an earlier
  criterion's expect text -- the act moved, the expectation did not. Rule 27's warning that a
  MODIFICATION is ungraded is this exact exposure.
- **`W47-S1` -- a co-signed never-widen half aged out overnight.** The halves were signed 2026-09-18
  describing an IN-PLACE OVERWRITE of "today's" pool key; the worker executed 2026-09-19 UTC, where
  that key is 404. The act is a CREATE and the rollback is delete-object, not re-put. The worker
  handled it correctly. The structural point for L9 and possibly for doctrine: A SIGN-OFF WHOSE TEXT
  IS DATE-RELATIVE HAS A SHELF LIFE, AND IT EXPIRES SILENTLY. Same family as the `NFRA_OUTSET`-S34
  incident already cited in the HARD STOPS section.
- **`W47-S2` (ARMED, `2.0.0_SA_COO~Z`) -- a test that passes coincidentally.** `test_13`'s two fixture
  dates make the retired semantics and the new one agree, so it no longer discriminates. A Rule 22
  DISCRIMINATION failure in the strict sense: the evidence would not differ if the claim were false.
- **`W37-S1` (ARMED, `1.0.0_SA_CTO~Z`)** -- the registry gate firing on the SEC bronze table; the
  tenancy fork is Andrew's and is working as designed.

## 6. Banked checks for the acceptance sweep at drain-end

Carried from earlier in the round, unchanged: `rk-31`'s co-sign pair committed before its first pool
write; `rk-41`'s controls actually discriminating (a legal implementation could take 12 served
documents to INVALID with both controls reading GREEN); write addresses coming from `address()`
output rather than hand-typed, which the naming gate cannot distinguish; which arm of R14-H1 fired
given registry state; `rk-61`'s control proving the adapter rather than the page (the gateway has no
`{proxy+}`); and crosswalk-derived denominators being vintage-pinned, the population having moved
33 -> 36 mid-run.

## 7. L4-R, when the addendum reopens this seat's half

From `1.0.0_SA_CTO~Z` msg 23874 (marked information; acked): a nine-item L4 delta against v0.13,
landing in the addendum that answers round 14's slug, re-opening no cell. Two items touch the
ratified-text half this seat signs: the QUARTERLY GRAIN item, and the two-vendor disagreement
disclosure rule (where two sources disagree, disclose the disagreement and show both constructions
rather than silently serving whichever the reader hit first). One card sits at Andrew -- REF_A issues
a rating and a price target, REF_B states that no rating is issued -- and his words name both without
saying which wins; the CTO's REC is REF_B.

NOTE THE VINTAGE QUALIFIER THE CTO DISCLOSED AND THIS SEAT INHERITS: `git fetch origin` FAILED at the
moment of that verification, so the blobs hashed were already in this device's object store from an
earlier fetch. The three sha256 agreements are that seat's own instrument; the VINTAGE is inherited,
and is re-verified at the next successful fetch.
