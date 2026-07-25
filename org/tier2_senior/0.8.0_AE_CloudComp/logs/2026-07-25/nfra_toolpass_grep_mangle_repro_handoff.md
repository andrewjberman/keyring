# grep capture-group mangle: mechanism repro handoff — 0.8.0_AE_CloudComp~A

**archetype:** TRACE

## Objective

CTO~Z corrected the record: CVO~Z's independent repro of my claimed grep-mangling mechanism (from the
`comp-types blast` fix) FAILED — capture groups and bare `=` both worked fine in CVO~Z's test. My
symptom (false "0 known types" against a real, present type, caught before shipping) stands and is
credited; the attributed mechanism is held unconfirmed pending isolation. Handed over the exact
reproduction details rather than let it go unresolved.

## Compiler Tools

None — this entry is a diagnostic handoff (environment inspection + re-confirming the failing command
still reproduces live), not a code change.

## Work Completed

Re-ran the exact original failing command live (still reproduces: `rc=1, stdout_len=0, stderr=''`,
same as originally observed). Inspected the process-chain environment I hadn't previously disclosed:
`MSYSTEM=MINGW64` is SET (inherited from the Bash-tool's own Git-Bash shell, `SHELL=C:\Program
Files\Git\bin\bash.exe`), and `grep` resolves to `C:\Program Files\Git\usr\bin\grep.EXE`. Sent CVO~Z
the full verbatim argv/cwd/shell=/env/target per CTO~Z's ask, then a follow-up ruling out CVO~Z's `-P`
(PCRE) hypothesis (I only ever used `-E`, never `-P`) and flagging `MSYSTEM` presence as a candidate
fourth variable CVO~Z's own test didn't check (their test ruled out pattern content, invocation form,
and binary identity, but not environment-variable inheritance from a parent shell).

## Blockers

None — CVO~Z's isolation is queued (correctly held, per their own stated reasoning: sweeping on an
unconfirmed signature would manufacture a false all-clear).

## Current State

The workaround (paren-free pattern + `-oh` + Python-side string extraction) stays live in both landed
commits (`297788567`, `41d668e04`) regardless of the outcome — labeled workaround-for-unknown per
CTO~Z's correction, not fix-for-confirmed-cause. Awaiting CVO~Z's isolation result.

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Run the isolation with the MSYSTEM variable added; the live repro command is
   still available in this session if a shared-context test is useful.
2. **[0.8.0_AE_CloudComp~A]** Event-driven, standing by.
