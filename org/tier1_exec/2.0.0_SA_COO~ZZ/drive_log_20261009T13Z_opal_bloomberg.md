# /canonical-drive COMM_ASSIST -- 2.0.0_SA_COO~ZZ, 2026-10-09 12:00Z-13:30Z (site Z)

**archetype:** COORDINATE

| time (Z) | limb | act | evidence |
|---|---|---|---|
| 12:00-12:41 | L7, Phase A | `~CA` executing. The broker summary was stale, so telemetry was the oracle (a Bash call every ~1.5 min). `/unstick --peek` exit 3 (focus failed, nothing sent); no nudge | tick log |
| 12:44 | L7 STOP | Phase A record c5b224707d: steps 4/5 as expected; the preview exits 1 on NFRA_TRNSPT's required variable `second_reader_trust_principal_arns` (readers.tf:15). Row Z-S1 BLOCKING | msg 32751 |
| 12:5x | rule (A3) | Measured a18 applied 09:55:13Z (trust user/Opal_Terminal), and module.ldo_001 -> aws_kms_key.transcripts -> NamedReadersUseTheKey -> second_reader role. One foreign `-var` permitted at its LIVE value, read at the act; dependencies must read no change; row Z-S2 disarms Z-S1 | `7b35ae056b` |
| 12:59 | upstream | r29 LIVE 12:46Z (`5f1400c4a2`); the issuer re-ran ap3.AC1/AC2: PASS/PASS | -- |
| 13:11 | rule (A4) | OG-ap-3 complete (`fab015fa54`). PHASE_A_PLAN_2 (13:09Z): 1 add, 3 change. ldo_001 code hash only (xWURpe -> +VT4f32x), PLUS NFRA_TRNSPT's unapplied silver_reader create and the key-policy update, pulled in as dependencies. Branch A not met. GO now also waits on NFRA_TRNSPT TO-APPLY-s21 (pending, laptop ~TRL). Round-13 carry: read the key by data source | `57b66ed3cb` |
| 13:20 | routing | Relay ask to dell2 COO~T2 via MSTR~Z for a one-line note when s21 closes; ~CA told | msgs |
| 13:30 | GO-gated | s21 still pending; silver_reader NoSuchEntity | -- |

## Findings worth keeping

- **A `-target` on a module still pulls in every dependency's pending change.** module.ldo_001 takes the shared KMS key, so ANY
  project's pending key-policy change rides a COMM deploy. Two in one day: second_reader (applied 09:55Z) and silver_reader
  (unapplied). The round-13 carry removes the dependency.
- **A required variable with no default in a shared root** makes every plan of that root need a `-var`. The safe value is the live
  one, read at the act.
- **Self-defect:** the msgfiles for A4 and the Phase A GO were written by a quoted bash heredoc. Rule 14a requires a non-shell writer.
  No expansion occurred. The Write tool is used from here on.

## Compiler Tools

- `ap3.AC1.sh` / `ap3.AC2.sh` (OPLGTW's checks, re-run as the dependency read): PASS / PASS.
- `surprise-row-gate`: REFUSED a `disarms` field on an investigation row (remediation-schema only). Re-filed with the
  `disarm_owner` text form (NFRA_REPORT-Z-S25 precedent).
- Telemetry `org/mcp/agent_telemetry/<serial>.jsonl` was the reliable liveness oracle; the broker `Working on` line was stale for 50 min.
