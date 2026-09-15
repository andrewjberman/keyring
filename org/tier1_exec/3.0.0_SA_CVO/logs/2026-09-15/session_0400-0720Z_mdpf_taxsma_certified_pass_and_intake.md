# 3.0.0_SA_CVO -- session 2026-09-15 ~04:00Z to ~07:20Z -- MDPF_TAXSMA atom run certified PASS (attempt 01); intake

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE

**Continues:** `session_0245-0400Z_open_calls_irpt_fntend_backfill_and_the_index_lock_hold.md` (@c8345657d2).

**Watchers:** no crons. Both Monitors were re-armed from the main root at each 30-minute expiry and confirmed with
TaskOutput. Now: inbox `b7ia7orf1`; the surprise intake is the latest re-arm.

## DONE (every act committed; LOCAL -- ls-remote ~07:03Z, origin/CLOUD = 6a5b276f8b)

### MDPF_TAXSMA -- run `mdpf-taxsma__20260915T0510Z`, attempt 01: PASS

1. **Scheduling and GO.** 1.0.0_SA_CTO~A sent a scheduling note at 05:36Z and the GO at 05:59Z (sender unverified).
   Before engaging, the parent verified the packet:
   - seal b7848ae964 and packet d97ae3f905 are both by 1.0.0_SA_CTO~A, in HEAD, and the seal commit is an ancestor
     of the packet commit;
   - the run dir holds the allowlisted 18 of 18 files, with 0 unexpected;
   - run.json reads DRY, with cycles 3 and 4 zero-change.

   The receipt ACK went out (96943).
2. **Pre-open phase, by a fork**, committed @f6c4cd256c in the foreground:
   - `SIGNED_ASSESSMENT.md`: 24 of 24 cells, 23 COHERENT and 1 nominated.
   - `semantic_refusal.patch.json`: 1 change.
   - `K2_RECONSTRUCTION_ATTESTATION.md`.
   - The nomination is `S4-valuation.recorded_observation` value.interpretation. It claims that six matched accounts
     make "the complete eight-account Tax SMA total", against C3, the cell's own missing_endings (4809, 5591), its
     own boundary, S2, and RESEARCH.md :11/:114.
3. **The parent re-read every discriminator** before the seal request (96948 / 96949).
4. **Seal-open at 06:59Z**, measured by this seat over raw bytes:
   - the seal sha256 a051d354... equals the public commitment, and the dry, plant and verifier hashes equal the seal's
     fields;
   - the verifier file is byte-identical to the final rectangle;
   - the sealed cell and its 'after' text equal the nomination verbatim;
   - dry against final differs at exactly 1 path.
5. **Verdict: PASS**, certification.json @9af8072cd8 (96950 / 96951). This seat's patch is WITHDRAWN from derivation.
   - Dry already carries the author's true sentence. Merged onto dry, the patch would swap it for this seat's
     paraphrase (validator rc=0, 1 path changed).
   - So the consumable is dry alone.
   - Caveat N-a: binding C's distinct lenses are not verifiable from run.json.
6. **Closure** 4ff8d9bdaa was verified by 11 of 11 own reads:
   - the certified rectangle is byte-identical to dry;
   - the withdrawn patch is kept byte-identical to the signed one;
   - run.json reads DRY and points at the record.

   certification.json was placed in the run home @b79ced9360 (96954 / 96955).

### Intake and inbox

- **Cottonwood category-views freeze** (Andrew-direct ~04:0xZ via 2.0.0_SA_COO~D, 96886).
  - This seat searched 2871 rows in 106 files for an existing carrier. Its one lead, POSN_ASTTAX-Z-W14-S3 (a second
    writer to the ETF classification table), was flagged as a LEAD, not as evidence.
  - It was ruled out: 2.0.0_SA_COO~D's trace (96899) found a cent-rounded pair-identity gate that also skips the
    Global fold.
- **IRPT_FNTEND-S66** (Investor Reporting is not Opal-admin gated). It landed at 05:22Z, after round 8's issuance at
  04:30Z (@57cb17e329), so it is a round-8 row and needs no between-rounds carrier.
  - The added cell FE-s-49 carries the gate. 2.0.0_SA_COO~D builds the same gate on the DSGN_REBRND branch; the
    coordination is theirs.
  - To check at round 8's L9: the gate requires the internal tier, not the role alone.
- **LGIC_ENFORCE:** 65 rows. Every ARMED row seen so far names 2.0.0_SA_COO~G, and each has a disarm or disposition
  row (S10-S15), except W1-S17, whose fix (S13) is not yet exercised.
  - W8-S3: D2-AC2's check reads a field the worker writes. At L9 it is graded on independent evidence, not on its own
    PASS.
- **READ-acked:** 96879, 96886, 96894, 96897 and 96908, all from 2.0.0_SA_COO~D (DSGN_REBRND Andrew-directs).

## OPEN

- **LGIC_ENFORCE round 1:** L8/L9 at drain-end. Count rows by id and content (S9's duplicate ids). Grade EN-s-1 and
  EN-s-2 together on the census that judged almost no names (W7-S1, W7-S4). Carry S5 against RULING DM.
- **IRPT_FNTEND round 8:** L8/L9 at drain-end, including S66 and the admin-plus-internal gate, and W4-S18 to S20.
- **Backfill (b):** the next project, as its gap between rounds admits it.
- **MDPF_TAXSMA PRD:** this seat's L4-R ratified-text half, when 1.0.0_SA_CTO writes it.
