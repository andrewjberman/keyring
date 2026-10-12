# IRPT_ANLREQ round 16, workstream Y -- L8 COMPILE: the stored-input count came back clean, the upload reader is RE-LANDED on the stored-input contract (built, not released), and the original-file route's owner scope is shown live

Compiled by the issuer `2.0.0_SA_COO~Y2` on dell2, 2026-10-12. Inputs: PRD v0.4 @4b1447e2cc (CONTRACT C-STOREDINPUT; the round-16 list), the CTO's rulings msgs 6304, 6369, 6378, 6387, 6532, 6541, 6544, 6575; issuance @d90edb3367 (five cells, fanout 4 of 4);
two issuer orders to the laptop seat (`TO-READS-Y7`, `TO-READS-Y8`). All seven orders are complete. A separate workstream `YS` (the script that files one synthetic request, `TO-AR-y-166`, drained @07c7b3463c; its run `TO-RUN-YS1` pending) is NOT part of this compile.

Claim words: MEASURED = this seat ran or read it; RECORD = a worker's or applier's committed record this seat opened; INHERITED = another seat's read.

## 1. State at this compile -- read this first

- **ON THE TRUNK, BUILT, NOT RELEASED:** the upload reader re-landed on C-STOREDINPUT (`AR-y-162`, drained @aaf156e8eb). No package was built, uploaded or applied. Row `IRPT_ANLREQ-D2-W53-S9` stands: no rebuild of `irpt-ycharts-generate` until its four unpinned members are pinned or released under their own pairs.
- **ON portal DEV (not PROD):** the ticket page's `commentary_sent` display and its one-time confirm control (`AR-y-164`, DEV `7bdc0cc9d8da`, CTO msg 6369, MSTR receipt msg 6381). Its first LIVE press is its own pair and has not happened. One follow-up parked: settle a 403 on the control.
- **READS, no product change:** the internal-reader read (`AR-y-163`), the original-route read (`AR-y-165`), the count script (`AR-y-161`), the count (`TO-READS-Y7`), and the live F2 arm (`TO-READS-Y8`).

## 2. What the round established, cell by cell

- **`AR-y-161`** (merged @1e2f4c0d56): a read-only script that counts stored template inputs the NEW reader would read differently, by cause. RECORD; the issuer ran its self-test (11 synthetic inputs, exit 0).
- **`TO-READS-Y7`** (laptop ~ANL; result @49af906f74; proof VALID): MEASURED by the laptop, validated by this seat (`reads7_check` READS7-OK, `proof-of-spec-check` VALID). 1914 items scanned; 56 stored template inputs (49financial 10, cottonwood 45, inflection 1), all TEMPLATE_UPLOAD; read differently by the new reader 0; turned back 0; unreadable 0; turned back with a report 0. The CTO ruled (msg 6532): no stored input needs a ruling before the re-land.
- **`AR-y-162`** (merged @aaf156e8eb): `READER_VERSION = "irpt-template-reader.r16.1"` written by `read_template` into the stored template as `reader_version`; `read_input` compares the re-read to the stored template ONLY when the versions are equal, an absent version reads as `before-C-STOREDINPUT` and is not compared, and the original's digest, the frozen document, the artifact refs, owner and source are bound under every version. The two repairs of row `IRPT_ANLREQ-D2-S64`: the account-header rule on the leading word with a closed exclusion list (`account type`, `account name`), its Rule 24 record over a 50-form constructed population (21 matched, 9 identifier forms unmatched, 5 attribute forms matched and not excluded; the population is CONSTRUCTED because no real-use header exists in the repository); the repeated-header words ask rather than tell. A digest pin on the reader's fixture output is stored beside the version (`2ce75d14...`). MEASURED by this seat on the worker's tree: contract tests 5 of 5, reader tests 9 of 9 (`Y162-RELAND-OK`), the intake folder 311 passed, 0 failed (floor 292; `Y162-KEEP-OK`), proof VALID. Six worker rows S17-S22, all OBSERVATION INERT.
  **Unknown, said plainly:** whether the resident and the Lambda may run different reader versions without a person seeing a surprise. The worker INFERRED it (a comparison runs only on equal versions); it was not traced.
- **`AR-y-163`** (merged @e2734dbeaf): the internal firm reader returns UNRESTRICTED for a caller with no users row AND for a disabled row (it never reads status), on 23 of 24 routes. The CTO's premise in msg 6181 is out of date: the ticket service now also refuses any status but active (round 9). The cell for row `TCKT_VNEXT-D2-S48` is to be cut from this read at the next issuance, on the CTO's rule.
- **`AR-y-164`** (merged @8af3e95ae7; DEV `7bdc0cc9d8da`): the panel shows who sent the final commentary and when; a control offered only when a draft exists and nothing is recorded, asking confirmation and posting once with no body. MEASURED by this seat: `Y164-SENT-OK` (72 pass), tsc OK, eslint 0 errors, and the built page LOOKED AT in two synthetic states (the control; the confirm step and the recorded line). No step called the live route.
- **`AR-y-165`** (merged @50af8b2a7a): the original-file route's rule, read from the repository (NOT the deployed bytes): the firm fence (served.py:1207-1209) runs before any record is read; the owner comparison (`_scope/owner_reads.py:28-31`) depends on the CALLER's class; a client-class caller is refused before the record is read.
- **`TO-READS-Y8`** (laptop ~ANL; result @d65453e913, proof @ce23ae0fd3; VALID): arm F2, run ONCE, read-only, on one cottonwood record of an OPAL_GLOBAL synthetic owner, under the CTO's pair (msg 6544). MEASURED by the laptop, validated by this seat (`reads8_check` READS8-OK, proof VALID): control served (link, expiry, hash and length present; no refusal code; the control's log lines CLEAN); `b` (another advisor of the record's own firm) `NOT_AUTHORIZED`; `a` (another firm's advisor) `FIRM_BINDING`; `b` on an absent id `NOT_AUTHORIZED`. Verdict **OWNER_SCOPED_REFUSAL**: the comparison at owner_reads.py:29-31 OR the second check at owned_requests.py:176-184, NOT SEPARATED. **THE ISSUER'S DEFECT:** the order said the control would answer `ok: true`; a served envelope has no `ok` member, so the first verdict was ANOMALY by my rule. I amended the criterion (AMENDMENT 1, @1b5051367b) to the CTO's own rule (the link's presence); the laptop restated the verdict from the same arms with NO second invoke. Arm (c), the owner twin, was not run.

## 3. For L9 -- judgments

- `AR161-y-AC2J`: the script's output can carry no account value, holding, id or person, and an input it cannot read is never counted as reading the same.
- `AR162-y-AC3J`: the account-header rule and its exclusions are right against a population that holds account columns, and each finding's words say what is seen and what to do. Note the worker's row S21: the account-column and total-row words still use imperative forms; only the repeated-header words were in the repair.
- `AR164-y-AC2J`: a person cannot record the send by one stray press, knows before pressing that it cannot be undone, and reads each refusal as a sentence that says what to do.

## 4. ARMED and BLOCKING rows at this compile (MEASURED, `comp-surprise --project IRPT_ANLREQ --armed`, 22:11Z): 3 ARMED, none of them this round's

- `IRPT_ANLREQ-D2-S26` (mine): one `commentary_ready` message for a synthetic request sits on the commentary-ready queue until about 2026-10-15T06:10Z; MEASURED 22:11Z: depth 1, not visible 0, delayed 0; the DLQ depth 0. It disarms on a measured depth of 0, which retention will produce. Not disarmed.
- `IRPT_ANLREQ-D2-W41-S1` (owner `2.0.0_SA_COO~T2`) and `IRPT_ANLREQ-D2-S29` (owner `2.0.0_SA_COO~G2`, release 4): other lanes' rows, listed so the slug counts them.

## 5. Owed next, for the CTO's analysis

1. The RELEASE of the re-landed reader is its own pair: a resident package built from a pin, the Lambdas pinned by the map, and the mixed-version question above traced first.
2. The cell for row `TCKT_VNEXT-D2-S48`, from the `AR-y-163` read.
3. `commentary_sent`'s first live press (its own pair; the 403 follow-up first), and a portal PROD push for it waits on Andrew's word.
4. Row `D2-S26` waits for retention.
5. Workstream `YS`: one synthetic cottonwood request naming V2's test ticket `TCK-20261012-13cd3a1d` for NFRA_TRNSPT TR-dp-24 (CTO msg 6575); the run `TO-RUN-YS1` is cut to `0.7.0_AE_CloudOps~AR2` and its result goes to the draft's ticket.
