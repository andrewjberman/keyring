# TO ADVI_COTBKF.TO-CB-d-3 -- round 4 CB-d-3: FWD-8 -- in-kind exits scored whatever their date; the near-matches listed for Andrew, never applied

<to_id>ADVI_COTBKF.TO-CB-d-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~14</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~C</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `CB-d-3` (`decompositions/ADVI_COTBKF_DECOMP.round4.md`) | **outcome_ref:** FWD-8 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-d-3`, FWD-8: "for each Commonwealth account, a person sees the matching current Cottonwood account, or a plain statement that it is not
yet matched, and why." Round 3's crosswalk (`data/assets/scripts/silver/commonwealth_crosswalk.py`, read it first) scores an account only if
its last activity is on or after 2026-04-22 (the start of current holdings history), so 758 rows read `CLOSED_BEFORE_CURRENT_HISTORY`
without being scored -- including acct#a2618be7, which left IN KIND on 2026-04-07 (row ADVI_COTBKF-W10-S4). CTO ruling 4: **score every in-kind
exit whatever its date**; and the near-matches (score at least 0.65 and below the 0.8 bar; 17 in round 3) are **NOT decided by a seat** --
FWD-9's ACCEPT says a link is never guessed. They are listed for Andrew to put to Cottonwood, each with its two accounts and the evidence, and
stay "not matched, awaiting a person". You prove it on the real tables into a LOCAL directory. You write NOTHING to S3.

**The change:**
1. An account whose end is an in-kind exit (transfer-out rows on its last activity, the same exit reading round 3's links use: its holdings
   just before the exit) is SCORED against every current account's first holdings, with no date cutoff; round 3's R2 rule and 0.8 bar are
   unchanged. Only an account that ends to cash, holds no security, or never exits in kind keeps an unscored reason -- say which.
2. A row scoring in [0.65, 0.8) gets `status NOT_MATCHED`, `reason_code AWAITING_PERSON`, its best candidate and score; it is NEVER matched.
   `--out` also writes `near_matches.csv` and `near_matches.md`: one entry per such row with the Commonwealth account, the candidate current
   account, the score, the compared positions (CUSIP, quantity each side), the exit and first-holdings dates, and the advisor ids -- written
   so a person who was not told the method can put each to Cottonwood.

**Output:** `--out <dir>` (crosswalk parquet + csv + the two near-match files); `--apply` unchanged in place (writes at `address(...,
'silver', 'crosswalk', 'date=2026-06-23')`; never run by you). Keep the LAST line's existing fields and append three:
`CROSSWALK commonwealth_accounts=<n> every_account_listed=<b> matched=<m> not_matched=<u> ambiguous=<a> ... in_kind_unscored=<k> near_matches_applied=<z> near_matches=<q>`
where `in_kind_unscored` counts accounts that exit in kind and carry no score (it must be 0) and `near_matches_applied` counts near-match rows
whose status is MATCHED (it must be 0).

**Tests** in `data/assets/scripts/silver/tests/test_commonwealth_crosswalk.py` -- keep round 3's; add tests whose names contain `r4`
(an existing test already matches `near`, so the selector is `-k r4`): an in-kind exit dated before current history is scored; a cash close keeps its reason; a 0.7 score is AWAITING_PERSON and unmatched
and appears in the near-match list; a 0.85 score still matches.

### ACCEPTANCE

<criterion id="CB4d3-AC1" cell_refs="CB-d-3"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_crosswalk.py -k r4</invocation><expect>passed</expect></criterion>
`CB4d3-AC1` -- the date-free scoring and the never-applied near-match on fixtures.

<criterion id="CB4d3-AC2" cell_refs="CB-d-3"><invocation>python data/assets/scripts/silver/commonwealth_crosswalk.py --out .scratch/advi_cotbkf/crosswalk_r4</invocation><expect>in_kind_unscored=0 near_matches_applied=0</expect></criterion>
`CB4d3-AC2` -- the real tables: every in-kind exit scored; no near-match applied.

<criterion id="CB4d3-AC3" cell_refs="CB-d-3" judgment="true"/>
`CB4d3-AC3` -- JUDGMENT, graded by `3.0.0_SA_CVO` at L9: the near-match list is readable by Andrew without the method and each entry's
evidence is right; acct#a2618be7's row now says what happened to it.

<expected_criteria>CB4d3-AC1,CB4d3-AC2,CB4d3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Local output and caches under `.scratch/`, uncommitted.
- **No S3 write, no `--apply`;** S3 READS only of this project's silver tables and Cottonwood's own current accounts and holdings (the
  sources round 3 read); never `opal-data-bd` or `opal-data-inf`.
- **Never apply a near-match.** Within 120 seconds for CB4d3-AC2 (cache under `.scratch/`, warmed once untimed, and say so).
- **Rule 13:** a DS-lane script; your commit is a candidate.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W14-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_crosswalk.py
data/assets/scripts/silver/tests/test_commonwealth_crosswalk.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round4.md</decomp_doc> (round 4), cell `CB-d-3`.
<owned_cells>CB-d-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB4d3-AC1, CB4d3-AC2, CB4d3-AC3 (judgment: UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO; never PASS or
FAIL). Instance at `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~14/ADVI_COTBKF.TO-CB-d-3.crosswalk-in-kind-and-near-matches.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB4d3-AC1,CB4d3-AC2,CB4d3-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the `CROSSWALK` line against round 3's, the reason counts, the near-match count and three entries, acct#a2618be7's row, commits;
copy `near_matches.md` into your deliverables folder.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time builder.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; reads under the laptop profile.
comp-adversary: RUN -- never-guess (near-matches unapplied, counted); same-firm reads only; BLIND: Cottonwood's answer to the near-match list (a person's act, Andrew's).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: CTO analysis ruling 4 (msg 105940); row W10-S4; CVO grade CB3c3-AC3; decomposition round 4 (measured constraint 4).
