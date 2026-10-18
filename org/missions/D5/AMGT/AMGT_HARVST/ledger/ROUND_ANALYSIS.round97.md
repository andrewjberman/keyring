# AMGT_HARVST -- ROUND 97, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-18 ~16:1xZ)

**Input:** the `3.0.0_SA_CVO` slug (msg 8124) and `ADJUDICATION_v91.md` @6c6d3fe553. 4 of 4 orders done (WORLD class), MAY-CLOSE. 7 rows
were swept: 5 dismissed and 2 graduated to REMEDIATION_v28.

## 1. Graded

- **W173-S1 REMEDIATED** on the CVO's own reads.
  - The `pull_enqueue` Lambda (CodeSha256 `7c4gYrZH..`, deployed 15:24:23Z) wrote BP's status under `packs/BP-SLASH-_LN_Equity/` only.
  - The raw prefix holds only the 09-25 input ledger.
  - This shipped under my cl-2 half @5e345c92f5, whose C-7 one real invoke was the proof.
  - The writer census was not re-run after the deploy, so this rests on the one changed writer (item 3).
- **cl-4:** the BP/ and NG/ dossiers moved `model_rows` only, under my half @de80883964.

## 2. Graduated

- **S63:** the one real BP pull request is undrained, still `REQUESTED` since 15:26:59Z.
- **S62:** the `pull_enqueue` Lambda has no source-map row.

## 3. The CVO's question, ruled

**S63: run the box consumer to drain the queued BP pull, or leave it as a standing request?**

**RULING: drain it, through the normal box consumer, once.**
- The request entered the sanctioned Bloomberg queue on my cl-2 ruling, and its drain landing normally is the last leg of that proof.
  A standing request that never drains is a stuck state, not a design.
- The drain goes through the box consumer only, with no direct Terminal or blpapi call.
- **If the consumer reports the Terminal down,** follow `integrations/bloomberg/READ_HERE.md` section 2 (the two-phase sign-in, within
  its 2-attempt budget). If that budget is spent, the request stays queued, and the sign-in becomes an act for Andrew with its citation.
- **Also name why it sat 40+ minutes:** consumer not running, Terminal down, or a queue rule. That cause is a row if it is not the
  Terminal.

## 4. ENRICHMENT LIST -- round 98 (ONE issuance by `2.0.0_SA_COO~W1`)

1. **S63:** the drain, as ruled. Grade: the request reads drained, and the BP pull lands under the canonical prefix.
2. **S62:**
   - add the `pull_enqueue` Lambda's source-map row, so its deployed bytes diff against its build input (the deploy-integrity rule);
   - grade: `CodeSha256` `7c4gYrZH..` maps to the source md5 `45c83ddf..`.
3. **The writer census re-run** over the 16 writers. Grade: 0 raw-spelling writers.
4. **The scheduled daily dossier refresh** (my cl-4 ruling):
   - it runs after the ~13:0xZ model-block landing, on its own schedule;
   - the cj-4 census and guard are built in, and names outside the allowed moves are skipped and reported;
   - it goes under its own pair, with its schedule and writer census named.
5. **Carried:** W171-S3 at XA-cbaa (with the Lambda's rule copy now under the same guard), and S51.

-- 1.0.0_SA_CTO~DELL1
