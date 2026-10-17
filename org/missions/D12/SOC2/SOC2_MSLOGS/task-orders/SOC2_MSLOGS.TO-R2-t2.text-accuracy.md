# TO SOC2_MSLOGS.TO-R2-t2 -- README, RUNBOOK and main.tf text say what the system is

<to_id>SOC2_MSLOGS.TO-R2-t2</to_id>
<project>SOC2_MSLOGS</project>
<issued_to>0.9.0_WK_SOC2_MSLOGS~12</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Risk note:** WORLD only by the gate's path floor (`main.tf` is in `<paths>`); the cell changes comment lines and prose, nothing that Terraform evaluates.

**Directive:** D12 | **Fabric:** dell1 | **Decomp cell:** `SM-t-2` (`decompositions/SOC2_MSLOGS_DECOMP_R2.md`) |
**outcome_ref:** record accuracy; remediations `SOC2_MSLOGS-D1-W1-S1`, `-W5-S1`, `-W7-S1` | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SM-t-2`. Round 1 switched the collector to raw records for every account and four feeds. Three text surfaces still describe the old system. Fix the words; change no behaviour.

READ first: `data/m365_metadata/README.md`, `data/m365_metadata/scripts/app/RUNBOOK.md`, the first lines of `infra/aws/terraform/trino/main.tf`, and (read only) `data/m365_metadata/scripts/app/start_subscriptions.py` and `data/m365_metadata/scripts/collector/raw_records.py` for the four content types.

CHANGE:
- `README.md`: describe the collector as it is: raw records of EVERY account in the tenant, four feeds (`Audit.Exchange`, `Audit.SharePoint`, `Audit.General`, `Audit.AzureActiveDirectory`), no population filter. Remove the `filter.py` and `population.json` lines and the "eight". The silver reader line names `silver/read_timeline.py`
  (and `silver/door_client.py`, `silver/read_exposure.py`, which another cell of this round adds: name them as the client's modules). Add a USAGE LINE for a member on a machine whose default AWS profile is not the member's: pass `--profile <name>` (a named profile holding the member's own access key) and `--mfa-code <six digits>`, then `--desktop` to land the answer as a file on the user's Desktop; one sentence that a printed answer
  on a Desktop sits outside the door's protection and is the reader's to keep or delete.
- `RUNBOOK.md`: the subscription step lists FOUR content types, the sign-in feed is subscribed (it started at the round-1 release; say "subscribed", with no date), the dry-run prints the planned calls for all four (read `start_subscriptions.py` to state the number it prints), and no step says three entries or "no sign-in feed".
- `main.tf`: line 1's comment no longer says "the eight operations": it says every Opal account's Microsoft 365 audit records. Comment lines only.
- No other file. Do not touch `collector.tf`, `access.tf`, `identity.tf` or any code.

Hard limits: ASCII only.

### ACCEPTANCE

<criterion id="R2-t2-AC1" cell_refs="SM-t-2"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R2_CHECKS/s1_check_r2.py text</invocation><expect>R2-TEXT-OK</expect></criterion>
`R2-t2-AC1` -- the README, RUNBOOK and `main.tf` carry no `filter.py`, `population.json`, "eight", "8 accounts", "unsubscribed", "not subscribed" or "three planned" text; the RUNBOOK names all four content types; the README has the `--profile` usage line.

<expected_criteria>R2-t2-AC1</expected_criteria>

Dry-run at the base 2026-10-17 ~06:2xZ: AC1 `R2-TEXT-REFUSED data\m365_metadata\README.md:7 still says 'filter.py'; ...` -- FAIL as expected. Run from the repository (worktree) root.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit.
- **LOCAL work only; NOTHING is called live.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `SOC2_MSLOGS-D1-W12-S<k>`, `surfaced_at` = `date -u +%FT%TZ`), and do not weaken a check to pass it.
- Commit only through `.tools/safe-commit.sh` with `--author "0.9.0_WK_SOC2_MSLOGS~12 <0.9.0_WK_SOC2_MSLOGS~12@opal.agent>"`, `-F` a message file you write with the Write tool, and `-- <paths>`.

<paths>
data/m365_metadata/README.md
data/m365_metadata/scripts/app/RUNBOOK.md
infra/aws/terraform/trino/main.tf
org/missions/D12/SOC2/SOC2_MSLOGS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D12/SOC2/SOC2_MSLOGS/decompositions/SOC2_MSLOGS_DECOMP_R2.md</decomp_doc> (round 2), cell `SM-t-2`.
<owned_cells>SM-t-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: R2-t2-AC1. Instance at `org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.9.0_WK_SOC2_MSLOGS~12/SOC2_MSLOGS.TO-R2-t2.text-accuracy.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> R2-t2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the check line, `git diff --stat` of your commit, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- prose and comment lines only; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- prose and comment lines only; no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- prose and comment lines only; the text check greps the forbidden phrases.
lane: the <paths> block IS the grant.
</preflight>

Source: the CVO's remediations `SOC2_MSLOGS-D1-W1-S1`, `-W5-S1`, `-W7-S1` (INERT, owner this issuer, `surprise-channel/remediations/REMEDIATION_v1.md`) and the CTO's round-1 analysis section 3 item 6 and the "not cut, noted" line (@843819d1ab).
