# Three-state fixture record (R7 limb 4) -- exercised, not asserted

**Run:** 2026-08-07T00:19:35.916799+00:00 by 3.0.0_SA_CVO~Z -- TO MDPF_CANPLAT.G2 @f123fbf6e
**Fixtures:** fixtures/three_state/baseline.json vs candidate.json

```
THREE-STATE SELFTEST -- paths_compared=5
  a: expected ('ZERO', 'NULL')  got ('ZERO', 'NULL')  OK
  b: expected ('NULL', 'ABSENT')  got ('NULL', 'ABSENT')  OK
  c: expected ('NUMBER', 'ZERO')  got ('NUMBER', 'ZERO')  OK
  e: expected ('ABSENT', 'NULL')  got ('ABSENT', 'NULL')  OK
PASS: three states produce distinct verdicts (and d 2 vs 2.0 produced no diff -- rule 3)
```

-- 3.0.0_SA_CVO
