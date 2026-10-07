# TO MDPF_SECCLASS.TO-SC-e65 -- round 11 SC-e-65: C-CASH-TOKEN: the scheduled producer's direct plan places a whole-token CASH security as cash/Cash

<to_id>MDPF_SECCLASS.TO-SC-e65</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~49</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>in_progress</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-65` (`decompositions/MDPF_SECCLASS_DECOMP_R11.md`) |
**outcome_ref:** FWD-7, FWD-13, FWD-17 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-65`. Andrew-direct (via 2.0.0_SA_COO~M2, ~14:1xZ 2026-10-07), on the "Classification not found" tickers of the 10-05 Cottonwood
build (BDCASHIN, FCASH, CQP and five more), verbatim: "most of those items literally have "Cash" as a token within, which would be the
"Cash" asset class. The others could likely be websearched."

PRD v0.15 C-CASH-TOKEN (1.0.0_SA_CTO~DELL1 msg 327): "a whole-token CASH in a ticker or name places the security in the TABLE as
cash/Cash by the direct plan, with classified_by naming the rule. A test pins BDCASHIN or FCASH in and CASHMERE out."

**Your base is the held branch `q/dell1/secclass-r9-held-34/r2` (cbbda93539).** It carries SC-e-44 and SC-e-63 in the same module.

**Where the direct plan is:** in `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py`,
`plan_rows(held_securities, *, vocab, existing_tickers, ...)`. It takes `(ticker, name)` pairs and calls
`classify_asset_class(ticker, ...)` for each. A key with no direct match is listed unresolved. Each planned row carries
`classified_by = "scheduled"` (`CLASSIFIED_BY`) and an `input` field naming its source.

**Build:**
1. Before the other direct sources, a held security whose ticker or name carries `CASH` as a whole token is planned
   `asset_class` `cash`, `sub_asset_class` `Cash`. Its `input` names the rule (`cash_token`).
   - **The token rule, which you define and state in the docstring:** in a name, "cash" as a whole word, case-insensitive. In a
     ticker, `CASH` bounded by the ticker's start or end or by a known word split (BDCASHIN = BD + CASH + IN, FCASH = F + CASH). It
     must keep CASHMERE (a word that starts with CASH) out.
   - **Real names:** read the real names of the Cottonwood tickers from the build the CVO read (search the repo for BDCASHIN; the
     laptop CVO read @09e0d7c89c is on CLOUD if present). Make the rule hold for them.
2. **classified_by:** "classified_by naming the rule". Read `org/standards/MDPF_SECCLASS_CONTRACT.json`'s `classified_by` field.
   - If its values are a closed list without a value for this rule, keep `classified_by = "scheduled"` and name the rule in `input`.
     That is the issuer's ruling for this cell. Say so in your report and file an OBSERVATION row; do not edit the contract.
   - If the contract admits a value for it, use that value.
3. Add `infra/aws/lambda/v2_portal/_shared/tests/test_cash_token.py`. It pins BDCASHIN and FCASH to cash/Cash with `input` naming
   the rule, CASHMERE out (not cash/Cash), and a name-only case (a ticker with no CASH whose name has the word "Cash").
4. Do not change any other source's precedence. An existing row is never planned, as today.

### AMENDMENT 3 (issuer, 2.0.0_SA_COO~M1, 2026-10-07 ~18:5xZ; row MDPF_SECCLASS-S63)

**Why it re-opens.** `cash_token_match()` splits the TICKER on every non-alphanumeric run and matches a piece equal to CASH. A
`NAME::` key carries the security's NAME in its key. So `NAME::FT UNIT 9273 INT RATE HEDGE PORT SER 135 MONTHLY CASH` (a unit trust)
and `NAME::VICTORYSHARES SMALL CAP FREE CASH FLOW ETF` (an equity ETF) are planned cash/Cash by the ticker leg. Contract 0.8.0 says
any name that is not a whole cash phrase is not placed by the name leg, and the ticker leg must not reopen that through a name key.
1. In `cash_token_match()`, the ticker leg skips a key that starts with `NAME::`. The whole-name leg still applies to every key, so
   `NAME::CASH` named `Cash` is still cash/Cash. A `CUSIP:` key has no CASH token by shape; leave it as it is.
2. Pin in `tests/test_cash_token.py`: the two names above are NOT cash; `NAME::CASH` / `Cash` IS cash; BDCASHIN, FCASH and CASHMERE
   are unchanged.
3. Change nothing else in the module, and do not edit the contract. Base for this work: origin/CLOUD 03f7f8fb5c (e65 merged at
   124bf03071), in the worktree you are given.
AC1's check gained the three NAME:: cases (base: FAIL as expected; FT UNIT and VICTORYSHARES read cash/Cash). AC2 is unchanged and
must stay PYTEST-OK over the whole `_shared/tests` directory.

### AMENDMENT 2 (issuer, 2.0.0_SA_COO~M1, 2026-10-07 ~15:1xZ; CTO round-11 analysis @fc96f7c48c release mode, PRD v0.16 @5f4b2f17d0)

**Why:** release mode puts e65 first, "once it carries the v0.16 allowlist". As built on held-34 r3 (4ac906c5c7, commits 896d998c9c +
ee6ef52a64), it does not, and it cannot release alone:
- (a) v0.16 lists EIGHT phrases. It adds `cash and cash equivalents`, and normalization also collapses punctuation.
- (b) v0.16 says "The allowlist lives in the contract file as data."
- (c) A cherry-pick of e65 onto CLOUD conflicts in `etf_classification_scheduled.py` with e44's hunks, so its held-34 form drags e44 and
  e63 (four shipped files).

**Ruling:** port e65 onto the round branch head ae61f93efe, which is CLOUD plus round records, contract 0.7.0 and no e44 or e63. It then
releases alone, with one shipped file.

**Build (slot ~49, base ae61f93efe):**
1. **Port the rule.** Port the CASH-token rule from held-34 r3 onto this base's
   `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py`. Read it with
   `git show 4ac906c5c7:infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py` and
   `git show 4ac906c5c7:infra/aws/lambda/v2_portal/_shared/tests/test_cash_token.py`. Port only the cash-token code, never e44's or
   e63's.
   - The ticker leg is unchanged: `^(BD|F)?CASH(IN|OUT)?$` on each piece.
   - The name leg: the WHOLE name, case-folded with punctuation and spacing collapsed, equals one of the eight v0.16 phrases: `cash`,
     `cash & cash equivalents`, `cash and cash equivalents`, `cash equivalents`, `cash balance`, `cash sweep`, `cash in`, `cash out`.
   - It runs only after the existing-row and seed-source skips. `input` is `cash_token`; `classified_by` stays `scheduled`.
2. **Contract.** In `org/standards/MDPF_SECCLASS_CONTRACT.json`, add the eight phrases as data: a field such as
   `fields.classified_by.cash_token_name_phrases` (or a top-level `rules.cash_token`), citing PRD v0.16. Bump the version to 0.8.0, and
   bump `PINNED_CONTRACT_VERSION` in `infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py` to match.
3. **Pin.** `test_cash_token.py` pins the module constant `CASH_NAME_PHRASES` EQUAL to the contract's list, read from the contract
   file. This is the W47-S2 drift guard.
4. **Tests.** Keep every pin from amendment 1:
   - "Cash Flow Dividend Fund", "Cash Cow", CASHMERE and "Acme Prime Cash Reserves" stay OUT;
   - BDCASHIN, FCASH, "Cash & Cash Equivalents" and "Cash and Cash Equivalents" go IN;
   - existing and seed rows are never planned.
   Add a punctuation case, such as "Cash, Sweep" or "CASH-SWEEP".
5. **Criteria.** AC1 and AC2 as above, plus SC11-e65-AC3: the full `_shared` suite at this base, already covered by AC2.

### AMENDMENT 1 (issuer, 2.0.0_SA_COO~M1, 2026-10-07 ~14:5xZ, on 1.0.0_SA_CTO~DELL1 ruling msg 346)

The ruling, verbatim: "The ticker leg stands as built. The NAME leg places cash only when the WHOLE normalized name is a cash phrase
from an allowlist in the contract: "cash", "cash & cash equivalents", "cash equivalents", "cash balance", "cash sweep", "cash in",
"cash out". Anything else goes to research or AI. Neither leg ever overrides an existing seed or canonical row. Pin "Cash Flow Dividend
Fund" and "Cash Cow" out in the test."

**Build delta:**
1. The name leg matches only when the whole name, normalized (lower-case, whitespace collapsed, trimmed), equals one of those seven
   phrases. Hold them in one module constant `CASH_NAME_PHRASES`.
   - The contract file is not edited here: the allowlist lands in PRD v0.16 and the contract on the round branch.
   - The test pins `CASH_NAME_PHRASES` to exactly those seven strings.
2. The ticker leg is unchanged.
3. Confirm, with a test, that both legs run only after the existing-row and seed-source skips: a ticker in `existing_tickers` or
   `seed_source_tickers` is never planned by the cash rule.
4. Tests:
   - "Cash Flow Dividend Fund" and "Cash Cow" (each under a ticker with no CASH piece) are NOT planned cash/Cash;
   - BDCASHIN and FCASH still are;
   - a name exactly "Cash & Cash Equivalents" under a CASH-free ticker is.
5. Re-run AC1 and AC2, rewrite and re-validate the proof instance, flip the status back to complete, and update row W47-S1's notes
   (or file W47-S2) with the narrowing.

### ACCEPTANCE

<criterion id="SC11-e65-AC1" cell_refs="SC-e-65"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/sc_e65_cash_token.py</invocation><expect>SC-E65 ok=True</expect></criterion>
`SC11-e65-AC1` -- plan_rows plans BDCASHIN ("BD Cash In") and FCASH ("Fidelity Cash") as cash/Cash. CASHMERE ("Cashmere Valley Bank")
is not cash/Cash, which is the difference control. The check reads the tree it is run from.

<criterion id="SC11-e65-AC2" cell_refs="SC-e-65"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py infra/aws/lambda/v2_portal/_shared/tests</invocation><expect>PYTEST-OK</expect></criterion>
`SC11-e65-AC2` -- the `_shared` suite passes with the new test. The control at the base is 185 passed.

<expected_criteria>SC11-e65-AC1,SC11-e65-AC2</expected_criteria>

Dry-run at the base (cbbda93539, 2026-10-07): SC11-e65-AC1 FAIL as expected (`BDCASHIN=None FCASH=None CASHMERE=None unresolved=3`); SC11-e65-AC2 PASS as expected (control, 185 passed).

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment;
  rows S49, S54). No web search: the research of the other tickers is the issuer's act.
- No table write, no deploy, no upload. This is a shipped `_shared` member, held off CLOUD until its pair signs. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W49-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py
infra/aws/lambda/v2_portal/_shared/tests/test_cash_token.py
infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py
org/standards/MDPF_SECCLASS_CONTRACT.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R11.md</decomp_doc> (round 11), cell `SC-e-65`.
<owned_cells>SC-e-65</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC11-e65-AC1, SC11-e65-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~49/MDPF_SECCLASS.TO-SC-e65.cash-token-direct-plan.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC11-e65-AC1,SC11-e65-AC2` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** the token rule as written, the classified_by reading, the real Cottonwood names and how each grades, AC1/AC2 outputs, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the module change schedules nothing; it rides the e44/e63 deploy under its pair.
comp-iam: DECLARED-NOT-APPLICABLE no role or grant changes.
comp-adversary: RUN -- CASHMERE-shaped false positives (AC1's control arm); a rule that outranks a stronger direct source (step 4); BLIND: the live planned set (the deploy's producer-live run).
lane: the <paths> block IS the grant; base is the held-34 line by issuer ruling in DECOMP_R11.
</preflight>

Source: round-10 analysis @a856d1525f section 2.3, section 3 item 6; PRD v0.15 C-CASH-TOKEN @54e82922e4; DECOMP_R11.
