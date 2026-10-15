# NEVER-WIDEN -- CTO half: J359 satellite characteristics by the Models' method (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~18:4xZ)

**Pairs with:** `org/tier1_exec/2.0.0_SA_COO~J1/deliverables/NEVER_WIDEN_J359_SATELLITE_CHARACTERISTICS_COO_HALF.md` @e1dfba9db8 (branch `wk-remote-J359`, on origin;
`2.0.0_SA_COO~J1`, GIVEN; msg 5685). **Spec:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/J359_SATELLITE_FACTSHEET_EDITS_SPEC_20261014.md` @fcf39274d6 (Andrew's words
verbatim). **CVO grade:** `org/tier1_exec/3.0.0_SA_CVO/deliverables/J359_SATELLITE_FACTSHEET_GRADE_20261014.md` @021d94b53b (v2 PASS, with the sequence condition).

## Read by this seat before signing

- **The package drift this seat raised (msgs 5679, 5681) is answered by measurement,** in the COO half's s.3:
  - four of five members differ from the deployed manifest (pin `102b2b29d3`);
  - the classifier's only called method (`get_classification`) is AST-identical;
  - `prev_trading_day` reads 0 of 136 days differing;
  - `compute_returns` differs, and its one exercised holding (GLD) reads 8 of 8 windows identical at 2026-10-13 (arm D). Arm D's own limit is stated: one holding, one as-of, not a
    closed-market day.
  - SH-t-24's held `frontier_returns` rides the package and is NOT called by this producer. Its hold (the SECHIST CTO half C1) is about the Positioning PRODUCER's apply, and is not
    breached by its bytes sitting unused here.
- **Writers N = 1** (one `put_object`, one IAM write statement pinned to the key); the denominator of 41 search hits is printed.
- **The IAM edit** is one READ element (`s3:GetObject` on `registry.json`), given as a patch with its sha256. The plan must show exactly that element plus the function's artifact fields.
- **Both branches** are read from the producer's own rule. The refusal states (a registry row missing, the registry unreadable) write nothing.

## Signed for, exactly as the COO half states

The act (a): the code; (b): the artifact and ONE read grant, through `safe-apply` with the ledger opened first; (c): one dry-run and ONE driven invoke. The blast radius is the one key
`platinum/satellites/characteristics.json`. The rollback is per key: `copy_object` from the prior VersionId read at the cut, plus the function re-pointed to `CodeSha256 IQP6I8Ex...`, plus the
grant reverted. The new reachable states of s.2. Branch A and Branch B of s.7. A different pin or build re-opens the pair.

## Conditions (this half's own)

1. **The sequence (CVO v2), as s.6a writes it, is a STOP, not an order of preference:** the producer is live and its served read MET (arm A's table over the inputs the run
   printed, and the Satellites mode against the factsheet's four numbers) BEFORE any portal promote of `cand/dell1/satellite-factsheet`. Andrew's word "Ok get this pushed when done via
   0.4.0_DT" (record `ANDREW_DIRECT_20261014_J359_PUSH_VIA_DT.md` @d7d9a9ed1a) is his word for that promote; "when done" is read as after step 3.
2. **The served read also prints the windows for every Bloomberg-sourced holding at the run's `bbg_as_of`, old rule against new.** Arm D measured GLD on one day, and the driven run's day
   may differ. Any window that moves is named in the ledger with its cause (a C-GAP or C-MMF day is expected and stated; anything else is Branch B).
3. **Tonight's dell1 restart at 21:00Z** (Andrew's word): no leg straddles it. A ledger opened before 21:00Z and not closed is read across every live worktree before re-execution
   (CLAUDE.md NEVER-2).

**CTO HALF: SIGNED**, with conditions 1-3. The commit carrying this file is the signature's vintage.

-- 1.0.0_SA_CTO~DELL1
