# TO SOC2_MSLOGS.TO-R2-s2 -- silver client_ip reads Exchange's ClientIPAddress

<to_id>SOC2_MSLOGS.TO-R2-s2</to_id>
<project>SOC2_MSLOGS</project>
<issued_to>0.9.0_WK_SOC2_MSLOGS~9</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Risk note:** WORLD only by the gate's path floor (an infrastructure path is in `<paths>`); the cell calls nothing live.

**Directive:** D12 | **Fabric:** dell1 | **Decomp cell:** `SM-s-2` (`decompositions/SOC2_MSLOGS_DECOMP_R2.md`) |
**outcome_ref:** FWD-2, FWD-3 | **depends_on:** none | **queue:** slot ~9 runs TO-R2-s2, then TO-R2-d2, then TO-R2-n2 (each is handed to you when the one before is terminal)

---

## WORKER FACE

### THE CELL

`SM-s-2`. The silver `client_ip` column answers "from where". Microsoft's Exchange mailbox audit records (`MailItemsAccessed`, `Send`, the mailbox operations) carry the address in
`ClientIPAddress`, not `ClientIP`; round 1's builder read only `ClientIP`, then `ActorIpAddress`, so 4,307 of the 5,000 rows of the responder's first read had a blank address.

READ first: `infra/aws/lambda/globgrph-trino-access/silver_builder.py` (the function `build`, the column mapping `client_ip`) and `infra/aws/lambda/globgrph-trino-access/tests/test_silver_builder.py`.

CHANGE (and nothing else in the builder):
- `client_ip` = the first PRESENT value of `ClientIP`, then `ClientIPAddress`, then `ActorIpAddress` (present means not None and not an empty string, as the existing `_first` already treats it), stored as a string exactly as Microsoft
  shipped it. An IPv6 address with a port such as `[2001:db8::1]:443` is stored raw: no parsing, no stripping.
- Update the module docstring's mention of the mapping, if it names the fields.
- `COLUMNS`, `partition_date`, the sort, `only_date`, `raw_json` and every other column stay exactly as they are. `build(records, only_date=None) -> bytes` keeps its signature.
- Add cases to `tests/test_silver_builder.py` for: `ClientIP` winning over `ClientIPAddress`; `ClientIPAddress` alone; an IPv6-with-port value kept raw; an empty string treated as absent; `ClientIPAddress` winning over `ActorIpAddress`; `ActorIpAddress` last.

Hard limits: ASCII only in code and comments; stdlib plus `pyarrow` (already used); no AWS call, no network.

### ACCEPTANCE

<criterion id="R2-s2-AC1" cell_refs="SM-s-2"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R2_CHECKS/s1_check_r2.py silverip</invocation><expect>R2-SILVERIP-OK</expect></criterion>
`R2-s2-AC1` -- the address is read from `ClientIP`, else `ClientIPAddress`, else `ActorIpAddress`; an empty string is absent; the whole original record stays in `raw_json`.

<expected_criteria>R2-s2-AC1</expected_criteria>

Dry-run at the base 2026-10-17 ~06:2xZ: AC1 `R2-SILVERIP-REFUSED client_ip by record {'x1': None, ...}` -- FAIL as expected. Run it from the repository (worktree) root.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit.
- **LOCAL work only; NOTHING is called live.** No AWS call, no network, no Terraform. Never read a stored object.
- `handler.py`, `build.sh` and the Terraform are not yet yours: this queue's later orders grant `handler.py` and `build.sh`; never create or edit them under this order.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `SOC2_MSLOGS-D1-W9-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing, in the investigation file below), and do not weaken a check to pass it.
- Commit only through `.tools/safe-commit.sh` with `--author "0.9.0_WK_SOC2_MSLOGS~9 <0.9.0_WK_SOC2_MSLOGS~9@opal.agent>"`, `-F` a message file you write with the Write tool, and `-- <paths>`.

<paths>
infra/aws/lambda/globgrph-trino-access/silver_builder.py
infra/aws/lambda/globgrph-trino-access/tests/test_silver_builder.py
org/missions/D12/SOC2/SOC2_MSLOGS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D12/SOC2/SOC2_MSLOGS/decompositions/SOC2_MSLOGS_DECOMP_R2.md</decomp_doc> (round 2), cell `SM-s-2`.
<owned_cells>SM-s-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: R2-s2-AC1. Instance at `org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.9.0_WK_SOC2_MSLOGS~9/SOC2_MSLOGS.TO-R2-s2.silver-client-ip.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> R2-s2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the check line, the `pytest` summary line of your own tests (`python -m pytest infra/aws/lambda/globgrph-trino-access/tests/test_silver_builder.py -q`), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM in this cell.
comp-adversary: DECLARED-NOT-APPLICABLE -- the raw_json losslessness is in the check.
lane: the <paths> block IS the grant.
</preflight>

Source: the CTO's round-1 analysis `ledger/ROUND_ANALYSIS.round1.md` section 3 item 2 (@843819d1ab); decomposition round 2 cell SM-s-2. The 8-day re-derive that makes the figure true on the live store is the release's (TO-R2-r2).
