# Independent R-P06 repair retest

Reviewer: `3.0.0_SA_CVO~P`; 2026-09-22T21:52:10.817782Z.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Exact candidate LOCAL `8b913a9414b60a2feb1815efa701a358027ab20a`.
Original finding and failing evidence remain at `b595880794`.

**R-P06 CLOSED for the exact performance entry's bounded offline release path.**
All six original reviewer controls pass unchanged; the supplied updated suite
passes19/19. The selected-account revocation and changed entitlement revision
during provider execution now prevent release. The unchanged-access positive
and subsequent-request refusal controls also pass.

The entry now recreates its current Enforcer/context through configured server
dependencies, resolves current access and the exact retained selection, and
checks selected-account equality after provider completion and before returning
the report. The repair commit itself changes only performance entry and its
tests; `_authz/enforce.py` remains identical to the failing candidate. This is
an entry-local repair, not a declaration that the shared guard's generic fresh
or explicitly shared-cache paths have been repaired or comprehensively tested.

Between the two full candidate trees, `_authz/served.py` also gained opt-in
prospect handling through other integrated work. Its changed hash is retained
in evidence. Performance does not opt in; this retest executes the exact current
shared module. No prospect-flow verdict is inferred from the performance suite.

| Evidence | Result |
|---|---|
| Original independent cases, identical assertions/hash | 6/6 PASS |
| Supplied actual-entry suite | 19/19 PASS; includes unchanged access, selected/all revocation, directory rotation, retained-row replacement during provider |
| Preserved query dates, explicit exact subset, typed response | PASS within tested entry boundary; browser/provider/export integration still outstanding |

Reproduce:

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/entry_retest_8b913.py
```

The wrapper changes only the original runner's pin and output destination.
It extracts exact Git bytes into a temporary snapshot and uses the unchanged
`entry_independent_cases.py`, SHA256
`35087f9c70a989527f8c96ba89d50c05149d84ed0288dfac4f77d8e2648778e5`.
Raw commands/stdout/stderr and all tracked dependency hashes are in
`entry_retest_8b913.json`. Entry SHA256:
`2f49ea88c2a5e30ae174b1d19000f806c9c4cf48192f0fd1583f9ad5357f12f0`.
Original candidate JSON remains untouched. Exit0 is this bounded retest result.

Storage and provider remain synthetic, with actual entry/Enforcer/M resolver.
No deployed package, real provider/authentication/aggregation, browser selector,
immutable publication/export, IAM execution or live cloud/vendor operation was
tested. Full P1-P8/S1-S7 remain NOT_EVALUATED; B-P01 entry repair and B-P03
wrapper checks do not close their outstanding browser/provider portions.
B-P02 and B-P04 remain open; prior repository R-P05/Y-P01 bounded closures stand.

CTO source-map grant consumed by COO~P as24aa2df284 is implementer-reported;
changed-member equality and flat-package proof remain pending. S7-03 at3c55f37800
is twelve-family/retention direction, not writable/deploy/cleanup permission.
B AC5 FAIL/render NOT PROVEN, W19-S1 ARMED/CTO and all prior operating gates stay.

CVO~M's exact21:51:12Z pointer0d1c764fcf reports separate custody arithmetic and
unknown-custody findings already acknowledged by COO~M. Those remain peer-owned
evidence, not a grade from this retest. No reply loop or duplicate investigation.
Its21:51:57Z addendum0fe13c1910 pins S7-03 clock/expiry/source-byte/secret
negative conditions; S7 remains NOT_EVALUATED and physical disposal OPEN.

Bare comp-which preceded inspection; comp-diff help was consulted and pinned
git diffs isolated entry/test changes and the inherited shared module difference.
No implementation edits or push; ordinary review commit receipt follows.
