# TO ADVI_COTBKF.TO-CB-be-1.bond-accrual-measure -- round 57 CB-be-1: does a bond's stored close carry accrued interest, for Cottonwood's bond holdings

<to_id>ADVI_COTBKF.TO-CB-be-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~84</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>57</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-be-1` (`decompositions/ADVI_COTBKF_DECOMP.round57.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**RULE (CTO containment ruling @0e8209c33c, item 6): no client account id, balance, fee or flow in ANY tracked file.** Counts, sha256,
file-and-line citations, security identifiers of bonds (CUSIPs are not client data) and reason codes only, in your record, report,
commit messages and rows. Never an account id, never a position size or dollar value of an account.

**This is a MEASUREMENT. You change no code, no test, no config and no served key. No AWS call is needed or allowed.**

**Why (CTO msg 4061).** Cottonwood's measured account-days are about to be minted stamped `method_version` 3. Method row 3's income
basis was measured TRUE for cash-posted income (dividends and interest enter value at the pay date; record
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~91/ROW3_VS_COTTONWOOD.json` -- read it first). One thing was left
open: **whether a bond's stored close carries accrued interest.** If the close is a DIRTY price (it includes accrued interest) while
coupons are also posted as cash income, coupon income is counted in the value before the pay date and the row's income basis is not
true for bonds as stated. If the close is a CLEAN price, value drops nothing at the pay date and income appears only when cash posts.

**Your item.**

1. **Where the bond close comes from.** With file and line, in `data/assets/scripts/silver/commonwealth_daily_valuation.py` (and
   what it imports): which source supplies the close used for a bond position, which field, and how the value is computed from it
   (per 100 of par, a factor, a multiplier). Name the stored price files it reads.
2. **What the stored close is.** For Cottonwood's bond holdings inside the MEASURED rows (not the held ones), decide clean or dirty
   from evidence, not from a vendor's reputation. Usable evidence, each with its count:
   - the source's own field name or documentation string in the stored file or the code that pulls it;
   - the price path of a coupon bond across a coupon pay date: a dirty price falls by about the coupon on the ex or pay date and
     climbs between; a clean price does not. Report, for the bonds you can test, how many show the saw-tooth and how many do not,
     with the denominator;
   - whether a coupon cash posting exists on those dates in the transaction classes the return form treats as income.
3. **Counts, with denominators:** distinct bond securities held in the measured rows; measured account-days that hold at least one
   bond; the same two counts for the 988 held account-days (`HELD_SOURCE_UNDER_REVIEW`), for scale. State how you identified a bond
   (which field or rule), with file and line.
4. **Verdict:** `CLEAN` (the stored close excludes accrued interest for these holdings), `DIRTY` (it includes it), `MIXED` (say the
   split and the rule that separates them), or `NOT_ESTABLISHED` (say exactly which read would settle it). Then one sentence: with
   that verdict, is row 3's income basis true for Cottonwood's bond rows, false, or not established.
5. **Write the record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~84/BOND_ACCRUAL_MEASURE.json` and a short `.md` beside it. The JSON has exactly these top-level keys: `verdict`,
   `income_basis_for_bonds` (`TRUE`, `FALSE` or `NOT_ESTABLISHED`), `bonds_in_measured_rows`, `measured_days_with_a_bond`,
   `bonds_in_held_rows`, `held_days_with_a_bond`, `sawtooth_tested`, `sawtooth_shown`, `evidence` (a list of
   `{"claim": "...", "file": "...", "line": 0}`), `settling_read` (empty unless `NOT_ESTABLISHED`).

**Inputs.** Local data lives in the base checkout, not in your worktree: `C:/dev/ajb_workspace/.scratch/advi_cotbkf/` (read-only for
you). Any commonwealth script you run needs the variable in its command line:
`COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json python ...`. Write scratch output under
your own worktree `.scratch/w84/` only.

### ACCEPTANCE

<criterion id="CB57be1-AC1" cell_refs="CB-be-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~84/BOND_ACCRUAL_MEASURE.json',encoding='utf-8'));assert d['verdict'] in ('CLEAN','DIRTY','MIXED','NOT_ESTABLISHED') and d['income_basis_for_bonds'] in ('TRUE','FALSE','NOT_ESTABLISHED');print('BOND-ACCRUAL-RECORD verdict=%s income_basis_for_bonds=%s bonds=%d measured_days=%d sawtooth=%d/%d evidence_rows=%d'%(d['verdict'],d['income_basis_for_bonds'],d['bonds_in_measured_rows'],d['measured_days_with_a_bond'],d['sawtooth_shown'],d['sawtooth_tested'],len(d['evidence'])))"</invocation><expect>BOND-ACCRUAL-RECORD verdict=</expect></criterion>
`CB57be1-AC1` -- the record exists with a verdict from the closed set, its counts and its evidence count.

<criterion id="CB57be1-AC2" cell_refs="CB-be-1" judgment="true"/>
`CB57be1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded:
- the verdict follows from the cited lines and counts, and each citation resolves at the cited line;
- the counts carry their denominators and the bond rule is stated;
- `income_basis_for_bonds` follows from the verdict; a `NOT_ESTABLISHED` names the read that would settle it.

<expected_criteria>CB57be1-AC1,CB57be1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **Do NOT touch:** any code, test, config, manifest or other project's file; anything under `C:/dev/ajb_workspace/` (read only).
- **No AWS call, no S3 read or write, no deploy, no push.**
- **No gate override** of any kind and no `--force`. If a gate refuses a commit, stop and report its exact refusal line.
- **Do not open or print** anything under `C:/dev/_cotbkf_private_evidence_20261009/`; scripts read the config themselves.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report (counts only) and a NEW surprise row
  (id `ADVI_COTBKF-D2-W84-S<k>`, `"fabric": "dell2"`, carrying no account id).

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round57.md</decomp_doc> (round 57), cell `CB-be-1`.
<owned_cells>CB-be-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB57be1-AC1, CB57be1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~84/ADVI_COTBKF.TO-CB-be-1.bond-accrual-measure.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB57be1-AC1,CB57be1-AC2` BEFORE the flip. Mechanical: CB57be1-AC1. A
judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:**
- the verdict and `income_basis_for_bonds`, each with its two or three deciding citations or counts;
- the four counts with denominators and the bond rule;
- the saw-tooth test: tested, shown, and what the untested bonds lacked;
- the `BOND-ACCRUAL-RECORD` line;
- commits; every gate refusal, verbatim; anything you could not read.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local files and code.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the verdict set admits MIXED and NOT_ESTABLISHED so a thin read is not forced into CLEAN; the saw-tooth test carries its denominator; the verdict is graded by the CVO, not by the worker or the issuer; BLIND: a bond whose coupon dates fall outside the stored price window, and a price source this project did not store.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` msg 4061 (and msgs 4037, 4039); `2.0.0_SA_COO~D2` msg 4055 (IRPT_DASHBD.TO-DB-b-116 @2f0664fab0); row IRPT_DASHBD-D2-W89-S1; CTO round-54 analysis @0ac41554df section 3, row D2-W66-S1.
