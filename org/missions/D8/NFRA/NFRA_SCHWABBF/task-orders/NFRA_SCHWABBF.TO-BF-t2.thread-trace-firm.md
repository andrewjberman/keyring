# TO NFRA_SCHWABBF.TO-BF-t2 -- thread hop 6: the trace oracle in the FIRM form

<to_id>NFRA_SCHWABBF.TO-BF-t2</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~4</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-t-2` (`decompositions/NFRA_SCHWABBF_DECOMP_R2.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-t-2`, FWD-1's DONE WHEN: "one trace: the oldest day pulled from Schwab, stored at the builder's address, converted the existing way, and the balances read." Andrew-direct 2026-10-20 ~14:3xZ: the builder's address is the vendor/firm form ("schwab vendor and 49 firm for the 0840").
This tool is the trace the issuer runs after the real pull. It asks the BUILDER and the REGISTRY where a master's day should be, so it cannot agree with the key function it grades; it never imports the key-function files.

**What exists.** `data/canonical/schwab/keyform/thread_trace.py` (merged `c98271602c`, 12 tests) is the round-1 MASTER-form version: bronze prefix `address('schwab', <master>, 'bronze', 'acc', 'date=D')`. Keep its CLI, hops, output lines, exit codes, balance printing and no-identifier rule; change where it looks.
- Firm form: bronze for master M and day D is the objects under `address('schwab', <firm of M>, 'bronze', 'acc', 'date=D')` whose file NAME starts with `{M}.`. The partition is SHARED by masters, so a count that does not filter by name counts another master's file as this master's. The firm of M is read at run time from `infra/logic/registry/scopes.json` (the scope row whose `masters` names M): 49financial = 08242234, 08335338, 08403355; cottonwood = 08719286, 08134043, 08165601, 08480305.
- Old (second) form for FWD-4: `schwab/{M}/bronze/acc/YYYYMMDD/` (master form, the pre-cutover layout). Real example: `schwab/08403355/bronze/acc/20261016/08403355.CRS20261016.ACC.zip`.
- Silver is unchanged by this round: `address('schwab', M, 'silver', 'dim_balance', 'date=D') + '/data.parquet'` (real: `schwab/08403355/silver/dim_balance/date=2026-10-16/data.parquet`). Silver scope is open at Andrew; read it where it is today.

**Build (edit `thread_trace.py` and its test only).**
1. `--form builder|legacy|any` keeps its meaning with `builder` = the FIRM form. Hop lines: `HOP bronze: HELD n=<files for THIS master> prefix=<the firm address>`; `HOP second-form: NONE|FOUND n=<k> prefix=<old master-form prefix>` as before. Under `--form builder` a found second form still makes the verdict FAIL.
2. Typed absence unchanged: no bronze in any layout and no silver prints `NOT-HELD master=M day=D cause=no-bronze-no-silver`, exit 2. A day where ANOTHER master's file is in the firm partition but not this master's is NOT-HELD for this master (name the cause `cause=other-master-only` when silver is also absent).
3. Tests `data/canonical/schwab/tests/test_thread_trace.py` (fake store), rewritten for the firm form, including: firm form held with silver -> `THREAD-OK`; legacy only under `--form builder` -> FAIL; legacy only under `--form any` -> OK naming the form; both forms -> FAIL naming the second form; a partition holding only 0833's file when tracing 0840 -> NOT-HELD, not OK; no account number in any output line.

### ACCEPTANCE

<criterion id="BF2-t2-AC1" cell_refs="BF-t-2"><invocation>python -m pytest data/canonical/schwab/tests/test_thread_trace.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF2-t2-AC1` -- the trace on a fake store in the firm form, including the shared-partition case.

<criterion id="BF2-t2-AC2" cell_refs="BF-t-2"><invocation>python data/canonical/schwab/keyform/thread_trace.py --master 08403355 --day 2026-10-16 --form any</invocation><expect>^THREAD-OK master=08403355 day=2026-10-16</expect></criterion>
`BF2-t2-AC2` -- the seam probe against the REAL neighbor: the real 0840 day 2026-10-16 (bronze still in the old master layout, silver present) traces under `--form any`.

<criterion id="BF2-t2-AC3" cell_refs="BF-t-2"><invocation>python data/canonical/schwab/keyform/thread_trace.py --master 08403355 --day 2026-10-17 --form any</invocation><expect>^NOT-HELD master=08403355 day=2026-10-17 cause=no-bronze-no-silver</expect></criterion>
`BF2-t2-AC3` -- the negative arm on a real Saturday (no bronze, no silver in any layout).

<expected_criteria>BF2-t2-AC1,BF2-t2-AC2,BF2-t2-AC3</expected_criteria>

Dry-run at the base 2026-10-20: the round-1 tool and test pass (AC1 `12 passed`, AC2 THREAD-OK form=legacy, AC3 NOT-HELD): all three are controls today. FIRST rewrite the test for the firm form and run AC1: the firm-form arms must FAIL against the master-form tool; only then change the tool.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **LOCAL.** The only AWS calls are read-only list/get in AC2 and AC3. Nothing is written to S3. If the real reads are refused, stop on AC2/AC3, write a surprise row naming the refusal, and do not weaken the criteria.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test to pass.

<paths>
data/canonical/schwab/keyform/thread_trace.py
data/canonical/schwab/tests/test_thread_trace.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R2.md</decomp_doc> (round 2), cell `BF-t-2`.
<owned_cells>BF-t-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF2-t2-AC1, BF2-t2-AC2, BF2-t2-AC3. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~4/NFRA_SCHWABBF.TO-BF-t2.thread-trace-firm.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF2-t2-AC1,BF2-t2-AC2,BF2-t2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the THREAD-OK and NOT-HELD lines, the pytest summary line, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the trace is read-only and one-shot.
comp-iam: RUN -- decomposition battery scanned 2 Terraform files (monolith-iam.tf, iam.tf) and 3 enumerated masters; reads under the seat's own identity, no grant added; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- the oracle independence and the shared-partition master filter (decomposition finding 1) are design constraints in the face.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.5 FWD-1, FWD-4, C-KEYFORM; decomposition round 2 cell BF-t-2; round-1 merge `c98271602c`.
