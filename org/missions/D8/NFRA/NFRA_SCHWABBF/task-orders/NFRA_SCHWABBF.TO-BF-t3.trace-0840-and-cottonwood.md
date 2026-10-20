# TO NFRA_SCHWABBF.TO-BF-t3 -- the trace covers 0840 and Cottonwood only; any other master refuses

<to_id>NFRA_SCHWABBF.TO-BF-t3</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~4</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-t-3` (`decompositions/NFRA_SCHWABBF_DECOMP_R3.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-t-3`, FWD-1 at PRD v0.7 (the 0840 Tax SMA account is the thread: "one trace: the oldest day pulled from Schwab, stored at the builder's address, converted the existing way, and the balances read"). Andrew-direct ~16:3xZ: "I dont care about that 0824, I want the new Cottonwood accounts taken care of and the 0840 tax sma account sorted out."
`data/canonical/schwab/keyform/thread_trace.py` (round 2, merged `e26bd321b2`) asks the BUILDER and the REGISTRY where a master's day should be and never imports the key function. It applies the firm form to every master in the registry. Under v0.7 only the firm-form masters (08403355 and the four Cottonwood masters 08719286, 08134043, 08165601, 08480305) have a firm form; 08242234 and 08335338 stay on today's key and are out of scope.

**Build (edit `thread_trace.py` and its test only).**
1. A trace of 08242234, 08335338 or any master outside the five prints `TRACE-REFUSED master=M out of scope (PRD v0.7 C-SCOPE)` and exits 3 BEFORE any S3 call. Everything else (hops, `--form builder|legacy|any`, balances, no-identifier rule, `NOT-HELD` exit 2, `THREAD-OK`/`THREAD-FAIL`) is unchanged for the five.
2. The five-master list is a literal in the tool (the tool must not import the key-function files), and a test proves it equals: the firm-form masters named in the contract below, each present in `infra/logic/registry/scopes.json` under the firm shown.
3. Rework `data/canonical/schwab/tests/test_thread_trace.py` accordingly: keep the firm-form arms for 0840 (and one Cottonwood master); replace any arm that traces 0833 or 0824 with the refusal arm (rc 3, no S3 client created).

Contract: 08403355 -> `49financial`; 08719286, 08134043, 08165601, 08480305 -> `cottonwood`.

### ACCEPTANCE

<criterion id="BF3-t3-AC1" cell_refs="BF-t-3"><invocation>python -m pytest data/canonical/schwab/tests/test_thread_trace.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF3-t3-AC1` -- the trace on a fake store for the five masters, and the refusal for the others.

<criterion id="BF3-t3-AC2" cell_refs="BF-t-3"><invocation>python data/canonical/schwab/keyform/thread_trace.py --master 08335338 --day 2026-10-16 --form any</invocation><expect>^TRACE-REFUSED master=08335338 out of scope</expect></criterion>
`BF3-t3-AC2` -- the refusal on the real tool for a master that stays on today's key.

<criterion id="BF3-t3-AC3" cell_refs="BF-t-3"><invocation>python data/canonical/schwab/keyform/thread_trace.py --master 08403355 --day 2026-10-16 --form any</invocation><expect>^THREAD-OK master=08403355 day=2026-10-16</expect></criterion>
`BF3-t3-AC3` -- the seam probe against the REAL neighbor: the real 0840 day 2026-10-16 (bronze still in the old master layout, silver present) still traces under `--form any`. Read-only.

<expected_criteria>BF3-t3-AC1,BF3-t3-AC2,BF3-t3-AC3</expected_criteria>

Dry-run at the base: AC1 passes against the round-2 tests (control, `18 passed`); AC2 FAILS (the round-2 tool traces 0833 rather than refusing); AC3 passes (control).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **LOCAL.** The only AWS calls are read-only list/get in AC3. Nothing is written to S3. If the real reads are refused, stop on AC3, write a surprise row naming the refusal, and do not weaken the criterion.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; read `org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md` for the highest `W4-S<k>` and use the next), and do not weaken the test to pass.

<paths>
data/canonical/schwab/keyform/thread_trace.py
data/canonical/schwab/tests/test_thread_trace.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R3.md</decomp_doc> (round 3), cell `BF-t-3`.
<owned_cells>BF-t-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF3-t3-AC1, BF3-t3-AC2, BF3-t3-AC3. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~4/NFRA_SCHWABBF.TO-BF-t3.trace-0840-and-cottonwood.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF3-t3-AC1,BF3-t3-AC2,BF3-t3-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the refusal line, the THREAD-OK line, the pytest summary line, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the trace is read-only and one-shot.
comp-iam: RUN -- decomposition battery scanned 2 Terraform files (monolith-iam.tf, iam.tf) and 3 enumerated masters; reads under the seat's own identity, no grant added; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- the oracle independence is a design constraint kept from round 2.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.7 C-SCOPE, FWD-1; decomposition round 3 cell BF-t-3; round-2 merge `e26bd321b2`.
