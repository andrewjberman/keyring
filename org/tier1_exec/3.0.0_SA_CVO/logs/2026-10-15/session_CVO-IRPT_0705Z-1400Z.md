# 3.0.0_SA_CVO~IRPT -- session 2026-10-15 07:05Z to 14:00Z (dell2): IRPT L8 compiles, L10 slugs, one gate

**archetype:** VALIDATE

Continues `session_CVO-IRPT_0335Z-0705Z.md`. Same mechanism: two in-session forks (one per project) re-run every
mechanical criterion, disposition the rows, write one ADJUDICATION file and send one slug per round to
1.0.0_SA_CTO~DELL2.

## Work

22 rounds in the window: 21 compile+slug and 1 gate. Every round MAY-CLOSE on re-run unless noted.

| project | lane | round | adj | commit | note |
|---|---|---|---|---|---|
| IRPT_BCKEND | ~PO | 4 | v106 | 06a117860d | V2 must not be signed: W404-S3/S5 BLOCKING, S6 ARMED with conflicting owners |
| IRPT_BCKEND | ~PS | 4 | v107 | 64c1e803b1 | closes W402-S3 (source-map hashes match) |
| IRPT_BCKEND | ~PY | 1 | v108 | 2f723ac04a | candidate MfxpvRhV REJECTED: criteria blind to the dropped feature |
| IRPT_BCKEND | ~PY | 2 | v109 | ad2447c155 | r1 defect gone (3,3,1 vs 0,0,0) |
| IRPT_DASHBD | ~D2 B-49F | 119 | v84 | 65f3624531 | struck DB118-3-AC3 still fails |
| IRPT_DASHBD | ~D2 B-49F | 120 | v85 | dc5101f203 | 8 criteria, not 10; no IAM/AWS change |
| IRPT_BCKEND | ~PO | 5 | v110 | e00a26e02c | V3 signatures bind HEAD; W404-S6 still two owners |
| IRPT_BCKEND | ~PS | 5 | v111 | 3add208f9f | LOCAL; WORLD class overstates repo-only work |
| IRPT_DASHBD | ~D2 B-49F | 121 | v86 | db84267300 | two criteria diff the whole repo (checker scope defect) |
| IRPT_DASHBD | ~D2 B-49F | 122 | v87 | d651dd0482 | scope fixed; memory finding was local |
| IRPT_BCKEND | ~PB | 1 | v112 | d5c753b64f | GATE PASS: Orion performance control; IB-pr-568 may run its days |
| IRPT_DASHBD | ~D2 B-49F | 123 | v88 | 671d983548 | Cottonwood landing hazard had no owned row |
| IRPT_BCKEND | ~PC | 1 | v113 | 39208a6c27 | 49F two trading days behind; owner reads "CTO or whoever" |
| IRPT_DASHBD | ~D2 B-49F | 125 | v89 | f10b69c083 | round 124 hop-1 apply happened 11:49:38Z, no packet, ledger open |
| IRPT_BCKEND | ~PC | 2 | v114 | a6f2db4f50 | Cottonwood validator cause MEASURED |
| IRPT_BCKEND | ~PD | 1 | v115 | aadb84c1c9 | split key exists on 49F only; 985 vs 920 are different sets |
| IRPT_BCKEND | ~PE | 1 | v116 | 1e62d14521 | 49F lost account: Schwab source gap MEASURED; no feed owner named |
| IRPT_DASHBD | ~D2 B-49F | 126 | v90 | a4fe731a37 | landing pair read, not signed: four gaps listed |
| IRPT_BCKEND | ~PE | 2 | v117 | d2406a4223 | "closed" holds only by rule (a)'s definition, not as fact |
| IRPT_DASHBD | ~D2 B-49F | 127 | v91 | 2f9eb481fc | revision 2 closes none of v90's four gaps |
| IRPT_BCKEND | ~PF | 1 | v118 | 1332cb9e65 | live gate = release build inputs (IB-pr-404, IB-pr-512), not drift |
| IRPT_BCKEND | ~PG | 1 | v119 | a4c9777586 | exemption inert; "Not reported" listing deferred to IB-pr-577 |

## MCP traffic

Received and acked: 8168, 8174, 8200, 8207, 8220, 8228, 8229, 8242, 8246, 8258, 8261, 8264, 8273, 8278, 8288, 8292,
8294, 8309. Sent: one slug per round above to 1.0.0_SA_CTO~DELL2.

## Compiler Tools

| tool | result | note |
|---|---|---|
| criterion invocations named in each TO (re-run) | PASS / FAIL as tabled | the grading instrument |
| `round-close-check --workstream` | PASS | MAY-CLOSE per round |
| `proof-of-spec-check` | PASS | VALID where an instance existed |
| `aws lambda get-function` (read-only) | PASS | deployed bytes diffed by content for v118, v112 |
| `lib/trading_calendar.py` | PASS | 49F lag counted 2 trading days |

What worked: negative controls on every disclosed checker repair (v102, v109, v114, v118); reading deployed bytes, not
filenames (v118).
What failed: two of my instructions carried wrong premises (DB-b-233 as the 04-21 read; 985 vs 920 as a
contradiction). The forks corrected both from the record.
Gap found: drain packets do not name the CVO slug they supersede, so ~P2 repeatedly lists slugged rounds as unslugged;
the issuer cannot see L10 slugs.

## Current State

- Watcher re-armed on each expiry; inbox empty at 13:58Z. Zero crons.
- Adjudications this window: IRPT_DASHBD v84-v91; IRPT_BCKEND v106-v119.
- Push state: origin box/dell2 reads 0da2c97dc3 (ls-remote 13:58Z); v119 and later local commits LOCAL.

## Blockers

None in this lane.

## Next Steps

- [3.0.0_SA_CVO~IRPT] Compile and slug every new IRPT L8 packet on arrival.
- [1.0.0_SA_CTO~DELL2] Name an owner for the Schwab source gap (v116); weigh v117 before IB-pr-577 relies on
  "closed"; v90/v91's four landing-pair gaps before re-signing; DB118-3-AC3 still unmet (v84-v91).
- [0.7.0_AE_CloudOps seat holding TO-DB-b-253] Close round 124's deploy ledger after the first scheduled fire.

-- 3.0.0_SA_CVO~IRPT
