# ADVI_FIRMBKTS -- ROUND 6, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-13 ~08:0xZ)

**Input:** `3.0.0_SA_CVO` slug msg 4702, `surprise-channel/remediations/REMEDIATION_v7.md` @db0c7f9805. MAY-CLOSE, 2 of 2 complete.

## 1. Graded

- **FWD-1: correctness MET, and the agreement arm is NOT met** (D1-C-S45). One fresh reader, under one face, reproduced 150 of 150 equal to the key. The PRD clause asks for two
  readers who AGREE WITH EACH OTHER, and the key is the issuing seat's own mapping, not a second reader.
  - **Ruling: a second fresh reader, not a reinterpretation.** Key-equality is not "two readers agree": the key's author is not independent of the issuer, and the clause is
    Andrew-confirmed text. One more read of the same 150 costs one worker. FWD-1 grades REALIZED when reader 2 agrees with reader 1 on 150 of 150, and any disagreement is
    named.
- **FWD-4:** unchanged; PARKED on the first organic non-admin validator line (D1-S41, owner this seat).

## 2. The exec-summary trigger: a cause SUPPORTED by the code, and a fix that also makes the cause measurable (D1-W65-S1, D1-S44)

FB-i-2 (D1-C-S46) reads `REGION_UNSET`: `gold_dispatch.sh:850` runs `aws events put-events` with no `--region`, and the dispatcher and boot scripts set none. That fits CloudTrail
holding no PutEvents in 90 days: a CLI with no region fails BEFORE any API call. **But the cause is not measured,** because `:850` pipes the CLI's output into `grep -q`
and the WARN line discards the error text. That is why the earlier read was INDETERMINATE.

**The round-7 fix cell, under a never-widen pair:**
1. **Measure first (no write):** on the runner host, run the identical `put-events` command with the dispatcher's environment and no region, and capture its error text. The
   expectation is a "You must specify a region" class error with no API call. That converts the inference into a measurement, or refutes it.
2. **The code:**
   - the `put-events` call takes the region from the ONE variable the chain's other AWS calls use, never a second typed literal;
   - on failure, the WARN line prints the CLI's error text (the first 300 characters, with no credentials).
3. **The pair's served effect:** the first chain after the deploy regenerates up to 158 client-facing exec summaries (round-3 ADDENDUM 12).
   - The pair names the key set.
   - A SAMPLE of regenerated summaries is read BEFORE they serve.
   - The prior VersionIds are the rollback.
   - Andrew may read the sample if he chooses.
4. **Close:** the first chain after the deploy logs "EventBridge chain-complete emitted". CloudTrail shows the PutEvents. The generator is invoked, and its outputs are read
   against the sample. D1-W65-S1 disarms on that read.

## 3. ENRICHMENT LIST (round 7, ONE issuance by `2.0.0_SA_COO~B1`)

1. **FWD-1:** a second fresh reader over the same 150 (section 1).
2. **The exec-summary trigger fix** (section 2), with the measurement first and the pair before the deploy.
3. **Carried:** D1-S41 / FB-h-5 (parked); D1-S43 (NFRA_CTLPLN, on the laptop).

## 4. ACTS ONLY ANDREW CAN DO (cited)

None. **Information:** the regenerated client summaries' sample is his to read if he chooses, before they serve.

-- 1.0.0_SA_CTO~DELL1
