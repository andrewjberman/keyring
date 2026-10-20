# TO NFRA_SCHWABBF.TO-BF-e4 -- the equality tool captures old-form silver before the cutover and reads firm-form silver after it

<to_id>NFRA_SCHWABBF.TO-BF-e4</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~3</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-e-4` (`decompositions/NFRA_SCHWABBF_DECOMP_R4.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-e-4`, PRD C-EQUAL and C-TIERS. FWD-5 ACCEPT: "The day after the change, nobody can find a holdings, balance or activity figure for an already stored day that differs from the day before." C-EQUAL: read once at the change, never a standing comparator (Andrew's veto). With C-TIERS the silver itself moves for 08403355: before the cutover its silver is `schwab/08403355/silver/{T}/date={D}/data.parquet`; after it, `schwab/49financial/silver/{T}/date={D}/08403355.parquet` (the same bytes, renamed, by the move; and rewritten by the converter when bronze is re-created). The comparison must therefore capture in one form and read in the other.

**What exists (read first).** `data/canonical/schwab/keyform/equal_sample.py` (round 1, merged `39f21f2064`, rework `_source_file` ruling): `capture --master M --days D1,D2 --tables T1,T2 --out FILE`, `compare --before FILE`, an injectable reader, `content_sha256` that excludes the single column `_source_file`, `source_file_values_sha256` recorded and not compared, and a no-loop/no-scheduler property. Its silver address is built at about line 66-70 as `address("schwab", master, "silver", table, "date=" + day, object="data.parquet")`.

**Build (edit the tool and its test only).**
1. A `--form old|firm` option on `capture` and on `compare`. `old` (the default for `capture`) reads `address('schwab', M, 'silver', T, 'date=D') + '/data.parquet'` exactly as today. `firm` reads `address('schwab', F, 'silver', T, 'date=D') + '/' + M + '.parquet'` where F is the master's firm from `infra/logic/registry/scopes.json` (the scope row whose `masters` lists M); a master that is not a firm-form master (only 08403355 and the four Cottonwood masters are) is REFUSED for `--form firm` with `EQUAL-REFUSED master=M has no firm form`, rc 3, before any S3 call.
2. The capture file records `form` (the form it read). `compare --before FILE` reads the AFTER state in the form `--form` names (default: the form the capture recorded), so the cutover run is `capture --form old` before and `compare --before FILE --form firm` after. Cells, figures, `content_sha256` and the `_source_file` exclusion are unchanged, so a renamed-but-byte-identical object compares EQUAL.
3. Output lines unchanged, plus `FORM before=<old|firm> after=<old|firm>` printed by `compare`. A partition absent in the after form is a DIFF as today.
4. Tests (fake store): capture old then compare firm on a fake store holding the same figures under the two key shapes -> `EQUAL-OK` rc 0; a changed figure -> `EQUAL-DIFF` rc 1; the firm object missing -> DIFF; `--form firm` for 08335338 -> `EQUAL-REFUSED` rc 3; every round-1 arm stays green; the module text still has no scheduling or loop construct.

### ACCEPTANCE

<criterion id="BF4-e4-AC1" cell_refs="BF-e-4"><invocation>python -m pytest data/canonical/schwab/tests/test_equal_sample.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF4-e4-AC1` -- the round-1 arms (15 passed at the base) and the cross-form arms.

<criterion id="BF4-e4-AC2" cell_refs="BF-e-4"><invocation>python data/canonical/schwab/keyform/equal_sample.py capture --master 08403355 --days 2026-10-16 --tables dim_balance --form old --out C:/Users/AndrewBerman/AppData/Local/Temp/bf_e4_capture_probe.json</invocation><expect>^CAPTURED cells=1 missing=0$</expect></criterion>
`BF4-e4-AC2` -- the seam probe against the REAL neighbor: the live, read-only capture of the real old-form `dim_balance` partition. The only write is the scratch file named in the invocation.

<criterion id="BF4-e4-AC3" cell_refs="BF-e-4"><invocation>python data/canonical/schwab/keyform/equal_sample.py capture --master 08403355 --days 2026-10-16 --tables dim_balance --form firm --out C:/Users/AndrewBerman/AppData/Local/Temp/bf_e4_capture_firm_probe.json</invocation><expect>^CAPTURED cells=1 missing=1$</expect></criterion>
`BF4-e4-AC3` -- the negative arm on the real store: before the cutover the firm-form object does not exist, so the same capture in the firm form records the typed absence (`missing=1`), not a failure and not a pass. Read-only.

<expected_criteria>BF4-e4-AC1,BF4-e4-AC2,BF4-e4-AC3</expected_criteria>

Dry-run at the base: AC1 `15 passed` (PASS as expected: a control that must stay green); AC2 and AC3 fail (the `--form` option does not exist: argparse error) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **LOCAL.** The only AWS calls are read-only gets in AC2 and AC3. No write to S3. If the real reads are refused, stop on AC2/AC3, write a surprise row naming the refusal, and do not weaken the criteria.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W3-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; read `org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md` for the highest `W3-S<k>` and use the next), and do not weaken the test to pass.

<paths>
data/canonical/schwab/keyform/equal_sample.py
data/canonical/schwab/tests/test_equal_sample.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R4.md</decomp_doc> (round 4), cell `BF-e-4`.
<owned_cells>BF-e-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF4-e4-AC1, BF4-e4-AC2, BF4-e4-AC3. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~3/NFRA_SCHWABBF.TO-BF-e4.equality-silver-forms.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF4-e4-AC1,BF4-e4-AC2,BF4-e4-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the two CAPTURED lines, the pytest summary line, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the tool is one-shot by construction.
comp-iam: RUN -- decomposition battery scanned silver.tf and monolith-iam.tf (2 Terraform files); reads only under the seat's own identity, no grant added; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- the standing-comparator veto stays graded by the no-loop test arm; decomposition finding 4 (compare across the rename) is the cell.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.9 C-EQUAL, C-TIERS; decomposition round 4 cell BF-e-4; round-1 merge `39f21f2064`.
