# TO TCKT_MTADTA.TO-MD-x3 -- the first-content read: counts only, for one day, through the door

<to_id>TCKT_MTADTA.TO-MD-x3</to_id>
<project>TCKT_MTADTA</project>
<issued_to>0.9.0_WK_TCKT_MTADTA~7</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Directive:** D7 | **Fabric:** dell1 | **Decomp cell:** `MD-x-3` (`decompositions/TCKT_MTADTA_DECOMP_R2.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none (you build to the DOOR CONTRACT v2)

---

## WORKER FACE

### THE CELL

`MD-x-3`, the FIRST-CONTENT READ. When the first real content lands, Andrew (a member of the access group) runs one script that tells him, for a day, in COUNTS
ONLY: how much each of the eight did, what kinds of events the tenant emits, and how many events were dropped because their only actor field was a GUID (an
id-only actor; the CTO's round-1 analysis item 4 and row D1-S2). The script reads through the door; it holds no S3 client. Nothing it prints names a file, a
folder, a site, a recipient or a subject.

### THE DOOR (what you call; another cell builds the far side)

`invoke(payload) -> dict`; the member alias answers:
- `{"op": "get_day", "person": <UPN>, "date": "YYYY-MM-DD"}` -> `{"ok": true, "rows": [..]}` (silver rows with `operation`, `workload`, `file_name`, `folder`, `site`, `participants`, ...).
- `{"op": "list_state", "prefix": "m365-metadata/trino/gold/collection_coverage/date=YYYY-MM-DD/"}` -> `{"ok": true, "keys": [..]}`.
- `{"op": "get_state", "key": <one of those keys>}` -> `{"ok": true, "body_b64": <base64 of a JSON document>}`; the document is
  `{"day", "fire", "records": [{"content_type", "listed", "fetched", "events", "dropped": {workload: n}, "dropped_id_only": n, ...}]}`.
- A refusal is `{"ok": false, "error": ...}`.

### BUILD (Python 3.9+; stdlib; `boto3` imported lazily inside `main` only)

1. **`data/m365_metadata/scripts/silver/first_content.py`** --
   - `EIGHT`: the eight UPNs (`andrew`, `alyssa`, `bobby`, `manav`, `yang`, `menachem`, `jim`, `jeanette`, each `@opalinvest.com`).
   - `report(invoke, date) -> str`: calls `get_day` once for each of the eight; lists the day's coverage keys and reads each; returns plain text of COUNTS only: a title
     line with the date; one line per person with the number of events (`<UPN>  <n> events`); a histogram of `workload operation count` lines over all eight; the line
     `id-only actors dropped: <N>` where N is the sum of `dropped_id_only` over every record of every coverage object of the day (a day with no coverage objects reads
     `no activity collected (no coverage objects)`); and, when all eight have zero events, the line `no activity collected`. Never blank.
   - `report` raises `RuntimeError` when the door answers `ok: false` to any call.
   - It must NEVER put a file name, folder, site, participant, subject hash or recipient into its output.
   - `main(argv)`: `--date YYYY-MM-DD` (default: yesterday, Eastern); builds the real invoker with `boto3.client("lambda")` inside `main` only, invoking the function named by
     `lib.opal_naming.name('globgrph', None, 'trino-access', 'lambda')` with `Qualifier="member"`; prints `report(...)`. Not exercised in round 2 by any worker.
2. **`data/m365_metadata/scripts/tests/test_first_content.py`** -- pytest: counts per person; the histogram; the id-only sum across two coverage objects; a quiet day; a refused door raises; a planted file name,
   folder and subject hash never appear in the output.

### ACCEPTANCE

<criterion id="MD2-x3-AC1" cell_refs="MD-x-3"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_x3.py reads</invocation><expect>X3-READS-OK</expect></criterion>
`MD2-x3-AC1` -- volume per person, the event-type histogram and the summed id-only count are printed, and no file name, folder, site, participant or subject hash is.

<criterion id="MD2-x3-AC2" cell_refs="MD-x-3"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_x3.py quiet</invocation><expect>X3-QUIET-OK</expect></criterion>
`MD2-x3-AC2` -- a day with nothing reads as quiet, never blank, and a refused door raises.

<expected_criteria>MD2-x3-AC1,MD2-x3-AC2</expected_criteria>

Dry-run at the base 2026-10-16 ~08:3xZ: both `X3-*-REFUSED missing ...first_content.py` -- FAIL as expected; both were also driven GREEN against a throwaway reference outside the
repository. Run from the repository (worktree) root.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit.
- **LOCAL; NOTHING is run live.** No AWS call, no S3 access, no Lambda invoke. SYNTHETIC rows only; no real address, subject, IP or file name enters the repository.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `TCKT_MTADTA-D1-W7-S<k>`), and do not weaken a check to pass it.
- Commit only through `.tools/safe-commit.sh` with `--author "0.9.0_WK_TCKT_MTADTA~7 <0.9.0_WK_TCKT_MTADTA~7@opal.agent>"`, `-F` a message file you write with the Write tool, and `-- <paths>`.

<paths>
data/m365_metadata/scripts/silver/first_content.py
data/m365_metadata/scripts/tests/test_first_content.py
org/missions/D7/TCKT/TCKT_MTADTA/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_MTADTA/decompositions/TCKT_MTADTA_DECOMP_R2.md</decomp_doc> (round 2), cell `MD-x-3`.
<owned_cells>MD-x-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: MD2-x3-AC1, MD2-x3-AC2. Instance at `org/missions/D7/TCKT/TCKT_MTADTA/deliverables/0.9.0_WK_TCKT_MTADTA~7/TCKT_MTADTA.TO-MD-x3.first-content-read.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> MD2-x3-AC1,MD2-x3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the two check lines, the `pytest` summary line, one sample of the printed report on the synthetic day (counts only), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no principal; the script runs under a member of the access group.
comp-adversary: DECLARED-NOT-APPLICABLE -- the counts-only rule is the guard, proved by AC1.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-1 analysis item 4 (msg 6588); row D1-S2; decomposition round 2 cell MD-x-3 and the DOOR CONTRACT v2.
