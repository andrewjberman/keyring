# /self-drive ~O fabric -- ticks 71-72 (14:58Z-15:31Z), 1.0.0_SA_CTO~O

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d
**Why written:** a governance fork pitched and ruled, and the gate fix landed.

## Row NFRA_OPLGTW-Z-S1: diagnosed, ruled, fixed, disarmed

- **Diagnosis:**
  - `prd_signoff_lib.evaluate()` on the exact files at 22e06eabdf reads `admitted=False` (ratified-text REFUSED), so the
    rule is right;
  - `read_signoff_files` reads git HEAD, which held the stamp;
  - the cause is `to-pipeline-gate.py` `check_file` `:2690-2711`: a `# pipeline-override:` line returned `([], notes)`
    for the WHOLE file, so LIMB 6 never ran. OG-e-1 carries one (order line 104; audit log 13:53:47Z / 13:54:13Z).
- **Governance fork, pitched to `3.0.0_SA_CVO~O`** (REC: NO, the override must not bypass LIMB 6). **Verdict: NO**
  @c6d6f60d62 (row Z-C-S1): "The override's only written scope is pipeline shape (gate `:511`, `:1994`), and CLAUDE.md 27
  names no exception. An issuer's own line must not void another seat's L4-R refusal."
- **Fix @f4ce2702ab:** the override branch runs `check_prd_signoff` and returns its violations. Self-test 0 failed of 100;
  two new arms run the REAL `check_file` with LIMB 6 stubbed (REFUSED -> refused; SIGNED -> admitted). **Negative control:**
  on a copy with only the fix reverted, 1 failed of 100. The first commit was refused by ruff E401 (two imports on one
  line) and re-landed after the split; one Bash call was refused by the commit-message hook, a false match on
  `python -m ruff` beside `safe-commit`.
- **Disarm:** row Z-S2 @04b8bfa3fb (DISMISSED_WITH_REASON, adjudicates Z-S1). CVO~O and COO~O were told; the COO needed
  to know because its overrides no longer skip LIMB 6.

## Verdict ledger

One CVO~O verdict this span (c6d6f60d62), executed the same span.

## Calls, completion

One card at Andrew: Alyssa's portal-only grant locks her out of her own tools (REC (a) keep); it also gates R2-k SERVED
step 2. COO~O has not cut R2-k's build yet (the PRD reads ADMITTED since @2e371ea304).

NOT DONE -- 0 of 4 projects `complete`. All REACHABLE.

state: ARMED

## Compiler Tools

`prd_signoff_lib.evaluate()` on git-shown files; `check_prd_signoff` on a scratch root; the gate's `--self-test`; a
negative-control copy of the gate.
