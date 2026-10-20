# TO NFRA_SCHWABBF.TO-BF-t4 -- the trace reads and checks silver on both forms

<to_id>NFRA_SCHWABBF.TO-BF-t4</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~4</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-t-4` (`decompositions/NFRA_SCHWABBF_DECOMP_R4.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-t-4`, FWD-1's DONE WHEN ("converted the existing way, and the balances read") and FWD-4 ("never finds the same day stored two different ways") with PRD v0.9 C-TIERS: after the cutover the silver of 08403355 sits at `schwab/49financial/silver/{T}/date={D}/08403355.parquet`, and before it at `schwab/08403355/silver/{T}/date={D}/data.parquet`. The trace must find it in either place, say which, and flag the day if the same silver is stored in both after the old keys should be gone.

**What exists (read first).** `data/canonical/schwab/keyform/thread_trace.py` (round 3, merged `25a713cd88`; 22 tests): it asks the BUILDER and the REGISTRY (never the key-function files) where bronze should be; `--form builder|legacy|any` governs bronze and the second-form check; silver is read from `address('schwab', master, 'silver', 'dim_balance', 'date=D') + '/data.parquet'` (about lines 52 and 109); it refuses masters outside the five (`TRACE-REFUSED`, rc 3); prints `HOP bronze`, `HOP second-form`, `HOP silver: READ rows=... table=dim_balance`, `BALANCES`, and the verdicts `THREAD-OK`, `THREAD-FAIL`, `NOT-HELD ... cause=...` (rc 0, 1, 2).

**Build (edit the tool and its test only).**
1. Silver is located by the same `--form` rule as bronze: `builder` -> only the firm key `address('schwab', F, 'silver', 'dim_balance', 'date=D') + '/' + M + '.parquet'` with F from `infra/logic/registry/scopes.json`; `legacy` -> only the old key (`.../schwab/M/silver/dim_balance/date=D/data.parquet`); `any` -> both, preferring the firm key, and say which form held it.
2. Output: `HOP silver: READ rows=<n> table=dim_balance form=<builder|legacy>` (the form suffix is new; every other line is unchanged). `THREAD-OK master=M day=D form=...` keeps the bronze form it prints today.
3. A silver SECOND FORM line: `HOP silver-second-form: NONE` or `FOUND form=<legacy|builder>`: under `--form builder`, a silver object also present at the old key makes the verdict FAIL naming it (the old keys should be gone after the cutover); under `legacy` or `any` it is reported, not failed.
4. The balances and the no-identifier rule are unchanged. A Cottonwood master reads its silver under `schwab/cottonwood/silver/...` by the same rule.
5. Tests (fake store): silver at the firm key only -> OK under `builder`; at the old key only -> OK under `legacy` and `any` (form named), FAIL under `builder`; at both -> FAIL under `builder` naming the second form; absent in both with no bronze -> `NOT-HELD` rc 2 as today; a firm folder holding two masters' silver objects -> only the traced master's is read; no account number in any output line. Every round-3 arm stays green.

### ACCEPTANCE

<criterion id="BF4-t4-AC1" cell_refs="BF-t-4"><invocation>python -m pytest data/canonical/schwab/tests/test_thread_trace.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF4-t4-AC1` -- the round-3 arms (22 passed at the base) and the silver-form arms.

<criterion id="BF4-t4-AC2" cell_refs="BF-t-4"><invocation>python data/canonical/schwab/keyform/thread_trace.py --master 08403355 --day 2026-10-16 --form any</invocation><expect>^THREAD-OK master=08403355 day=2026-10-16</expect></criterion>
`BF4-t4-AC2` -- the seam probe against the REAL neighbor: the real day 2026-10-16, still entirely in the old forms, traces under `--form any` and its silver is read from the old key. Read-only.

<criterion id="BF4-t4-AC3" cell_refs="BF-t-4"><invocation>python data/canonical/schwab/keyform/thread_trace.py --master 08403355 --day 2026-10-16 --form builder</invocation><expect>^THREAD-FAIL master=08403355 day=2026-10-16</expect></criterion>
`BF4-t4-AC3` -- the negative arm on the real store: before the cutover the strict firm-form trace of the same real day FAILS (bronze and silver are not at the firm addresses yet). Read-only.

<expected_criteria>BF4-t4-AC1,BF4-t4-AC2,BF4-t4-AC3</expected_criteria>

Dry-run at the base: AC1 `22 passed` (PASS as expected: a control that must stay green); AC2 passes today (a control: the real day traces); AC3 passes or fails today by the bronze alone (the strict firm trace already FAILs on bronze) -- run it first and record what it prints; the `HOP silver ... form=` suffix and the silver second-form line are what your tests add.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **LOCAL.** The only AWS calls are read-only list/get in AC2 and AC3. Nothing is written to S3. If the real reads are refused, stop on AC2/AC3, write a surprise row naming the refusal, and do not weaken the criteria.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; read `org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md` for the highest `W4-S<k>` and use the next), and do not weaken the test to pass.

<paths>
data/canonical/schwab/keyform/thread_trace.py
data/canonical/schwab/tests/test_thread_trace.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R4.md</decomp_doc> (round 4), cell `BF-t-4`.
<owned_cells>BF-t-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF4-t4-AC1, BF4-t4-AC2, BF4-t4-AC3. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~4/NFRA_SCHWABBF.TO-BF-t4.trace-silver-both-forms.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF4-t4-AC1,BF4-t4-AC2,BF4-t4-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the THREAD-OK and THREAD-FAIL lines, the pytest summary line, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the trace is read-only and one-shot.
comp-iam: RUN -- decomposition battery scanned silver.tf and monolith-iam.tf (2 Terraform files); reads under the seat's own identity, no grant added; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- oracle independence from the key-function files is kept; decomposition finding 2 (shared folder, filter by file name) is a test arm.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.9 C-TIERS, FWD-1, FWD-4; decomposition round 4 cell BF-t-4; round-3 merge `25a713cd88`.
