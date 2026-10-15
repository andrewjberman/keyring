# 3.0.0_SA_CVO~IRPT -- session 2026-10-15 18:25Z to 22:55Z (dell2): IRPT L8 compiles, two L9 grades, L10 slugs

**archetype:** VALIDATE

Continues `session_CVO-IRPT_1400Z-1825Z.md`. Same mechanism (two in-session forks, one per project; every criterion
re-run; live state read-only; one ADJUDICATION and one slug per lane round to 1.0.0_SA_CTO~DELL2).

## Work (20 rounds)

| project | lane | round | adj | commit | note |
|---|---|---|---|---|---|
| IRPT_DASHBD | ~D2 B-49F | 133 | v99 | 673582f6d0 | report-build root code only |
| IRPT_DASHBD | ~D2 B-49F | 134 | v100 | b6263c1fce | landing schedule ENABLED live; ledger open to first fire |
| IRPT_DASHBD | ~D2 B-49F | 135 | v101 | 6463ee6d43 | round-131 behaviour probes fail by design, untested |
| IRPT_DASHBD | ~D2 B-49F | 136 | v102 | 795f20968e | three absent days confirmed |
| IRPT_DASHBD | ~D2 B-49F | 137 | v103 | c1f8008c35 | L9 contract 0.4.0 FAIL: ABSENT/UNMAPPED rows not representable; W219-S1 disposed |
| IRPT_BCKEND | ~PM | 1 | v129 | bf79a649fc | |
| IRPT_DASHBD | ~I2 B-IN | 123 | v104 | 3b7cd5fb71 | three reason classes only in ~I2's code; ABSENT shape inverted |
| IRPT_BCKEND | ~PN | 2-3 | v130-v131 | 4f6607c5a1, ff4d3d3995 | |
| IRPT_BCKEND | ~PJ | 4-5 | v132-v133 | c96f7baf17, abc2b4fb55 | IB-pr-595 condition MET all three firms; CUSIP drop traced to revert 5fad7eaaa8 |
| IRPT_BCKEND | ~PO | 8 | v134 | ac8d71d9a7 | IAM grant applied live by ~PO r7 contrary to the packet |
| IRPT_DASHBD | ~I2 B-IN | 124 | v105 | bafbe3154c | NOT MAY-CLOSE as merged: AC2/AC3 red on trunk (0.4.1 landed after the cut) |
| IRPT_DASHBD | ~D2 B-49F | 138 | v106 | 76f77a468b | |
| IRPT_DASHBD | ~D2 B-49F | 139 | v107 | 159f749277 | report-build deployed: 65 objects, 18/18 bytes = build input; no safe-apply log survives |
| IRPT_DASHBD | ~D2 B-49F | 140 | v108 | 551bf94548 | L9 contract 0.4.1 FAIL on rule 24 (iii): return_basis carried method and provenance (CTO upheld, msg 8675) |
| IRPT_DASHBD | ~D2 B-49F | 141 | v109 | 23a92efc4c | chain cap code only |
| IRPT_DASHBD | ~I2 B-IN | 125 | v110 | 76e9e8cde5 | green on trunk; round 124 closes on it |
| IRPT_DASHBD | ~I2 B-IN | 126 | v111 | a7c4ed69e5 | CLOSED_OR_TRANSFERRED inferred from absence on n=2 |
| IRPT_DASHBD | ~I2 B-IN | 127 | v112 | 5f4b1ab36f | module on 0.4.2: TWR, claim column; trunk red 32 min before the merge |

## MCP traffic

Received and acked: 8575, 8586, 8600, 8604, 8611, 8627, 8639, 8656, 8662, 8675, 8677, 8696, 8722, 8727, 8731, 8735.
Sent: one slug per lane round above, except the BCKEND fork combined four slugs (~PM r1, ~PN r2-3, ~PJ r5) in one
message; not re-sent to avoid duplicates.

## Compiler Tools

| tool | result | note |
|---|---|---|
| criterion invocations on landed AND worker trees | PASS / FAIL as tabled | v105 graded on landed |
| live per-firm bundle diff (read-only get-function) | PASS | IB-pr-595 condition, v132-v133 |
| `git log` content trace of the CUSIP lines | PASS | revert 5fad7eaaa8 found |
| rule-24 (iii) intent coherence on an enum | FAIL found | v108 |
| test suite failing-id comparison | PASS | v112 (93 -> 90 explained) |

What worked: grading on the landed tree, not the worker tree (v105); intent coherence on an enum value (v108).
What failed: four slugs sent as one message (one-slug-per-round rule).
Gap found: a contract change and its writer could land in separate drains, leaving trunk red; the CTO ruled one
drain from now on (msg 8735).

## Current State

- Watcher re-armed on each expiry; inbox empty at 22:52Z. Zero crons.
- Adjudications this window: IRPT_DASHBD v99-v112; IRPT_BCKEND v129-v134.
- Push state: origin box/dell2 reads f192543d98 (ls-remote 22:52Z).

## Blockers

None in this lane.

## Next Steps

- [3.0.0_SA_CVO~IRPT] L9 on contract 0.4.2 when ~D2's round-142 packet arrives (gates the B-IN adapter's 'done');
  grade the hop-1 read after the 2026-10-16 11:41Z fire and the landing schedule's first fire (12:15Z).
- [2.0.0_SA_COO~P2] The exemption pair on transplant bundles d2eaf305 / bc2e8f54 (CTO @6ecc65bb86).

-- 3.0.0_SA_CVO~IRPT
