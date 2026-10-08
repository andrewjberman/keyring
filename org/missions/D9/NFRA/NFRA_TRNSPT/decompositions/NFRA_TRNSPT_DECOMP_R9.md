# NFRA_TRNSPT decomposition -- ROUND 9 (2026-10-08, issuer 2.0.0_SA_COO~T2, dell2, box/dell2)

Cut on 1.0.0_SA_CTO~DELL2's round-8 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_8_20261008.md`
@08ff07562f (msg 1548) and ruling msg 1542: "write the 20,473 rows to opal-data-transcripts silver at address()'s key ... read back from
S3: 20,473 rows, of which 2,716 are held_out and 17,757 are not; the planted-token wipe test passes on the stored bytes". Risk SERVED (a
new silver partition in the project's own bucket that no consumer reads yet).

| cell | item | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-w-9` | the store writer + held_out column + stored-bytes verifier + reader compatibility, tested on a fake s3 | FWD-5 | dell2 worker | LOCAL | worker | -- |
| `TR-x-9` | the served write: the 29 objects to S3, read back, verified on the stored bytes | FWD-5 | ISSUER (a served write; no worker holds one) | SERVED | -- | TR-w-9 drained |

**Chains.** A = TR-w-9 -> TR-x-9 (issuer). Fan-out 1 of 1 worker chain, cap 8.

**Issuer rulings.**
1. **The address is the builder's, measured at the cut:** `parse_silver._address("silver", "research_meeting", <meeting_date>,
   "<transcript_id>.parquet")` -> `s3://opal-data-transcripts/teams/transcripts/silver/research_meeting/date=<YYYY-MM-DD>/<id>.parquet`
   (`lib.opal_naming.address`, no refusal). 29 objects, one per transcript. No registry row is needed.
2. **`held_out` is a ROW flag:** TRUE when that utterance's text drew at least one residual flag from `wipe_blocks`. The analysis's 2,716
   is the count of residual FLAGS (round 8), not rows; one row can carry several. The held-out row count is MEASURED at read-back and
   reported against 2,716 -- never forced to it.
3. **"The wipe test on the stored bytes"** = read the stored parquet back and re-run `wipe_blocks` on every non-held-out row's text: the
   name, id, email and phone counts must be 0 (the stored copy is already wiped; a re-wipe finds nothing). Planted tokens cannot be put in
   real stored data, so the planted-token test stays the unit test (TR8-s8-AC2), and the stored check is this idempotence.
4. **Never-widen: non-application** (CLAUDE.md section 5): the write set is a literal list of 29 new keys under a prefix no object
   occupies today (verified empty at the act) and no consumer reads; the actor controls it. Rollback per key: delete the 29 keys (a
   human-confirmed act). The before-rule (msg 1289) covers resource POLICY changes, not object writes; none is made.
5. KMS: objects are written with the transcripts key (`alias/opal-data-transcripts`), as every transcripts object is. If dell2's user is
   refused encrypt on that key, the write goes to the laptop through 0.0.0_AB_MSTR~DELL2, and the close says so.

## Rule 24 record

Domain: analysis s.3 E1, criteria (1)-(3). (1) the address = ruling 1 (printed at the cut and at the act); (2) read-back = TR-x-9;
(3) stored-bytes wipe = TR-x-9 with TR-w-9's verifier. Remainder: none.

## Battery

- Checks `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R9_CHECKS/r9_checks.py`, dry-run at base box/dell2 2e53d2f87c: w9-write
  FAIL (absent).
- `comp-iam`: the act's principal is `cloudops-dell2-agent-user`; s3:PutObject on `opal-data-transcripts/teams/transcripts/silver/*` and
  KMS encrypt are measured at the act (a refusal is the routing in ruling 5, never a workaround).
