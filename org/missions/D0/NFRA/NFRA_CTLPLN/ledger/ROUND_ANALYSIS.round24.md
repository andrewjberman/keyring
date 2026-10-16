# NFRA_CTLPLN -- ROUND-24 ANALYSIS (1.0.0_SA_CTO, 2026-10-16 ~03:0xZ)

**On:**
- the issuer's L8 packet `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND24.md` and `ROUND24_INPUTS_FOR_ROUND_ANALYSIS.md`
  @52567a1a41;
- `round-close-check`: MAY-CLOSE (24 orders, 2 judgment criteria, both graded, 0 self-graded). No CVO judgment was owed
  this round (packet section 1).

**PRD:** v0.31 (ADMITTED).

## 1. FWD coverage

No grade moves this round. The table is round 23's: REALIZED 5 (1, 3, 5, 24, 28); ADVANCED 19; PARKED 1 (9); MOVED 3
(13, 20, 26).

`CT-an-1` advanced FWD-15's tool half. Every `prove` and `install` receipt now names its pip log (file name, SHA-256,
bytes), and the log shows the inherited `PIP_INDEX_URL` and `PIP_FIND_LINKS` removed. The issuer's real run used a synthetic
wheel on the laptop. dell1 has not pulled it yet.

## 2. Rulings

1. **FWD-16's absent-package arm is DRIVEN DELIBERATELY. It is neither retired nor qualified as a wait.**
   - My round-23 ruling made the arm wait on a lane that organically needs an absent package. dell1 answered NONE (049f). An
     organic wait is exactly what the L2 law forbids: "NO FWD IS A WAIT ... a mechanism driven deliberately, the organic case
     kept as the negative arm". I correct my own ruling here.
   - The deliberate drive:
     - The issuer reads `requirements.txt` and prints the check.
     - It picks the smallest pure-Python wheel ABSENT from that file.
     - A laptop project lane of NFRA_CTLPLN requests it for one stated one-off read in the project's own tooling. The read is
       named in the request; the request is a test act and says so.
     - The status verb is read three times: before the decision ("not approved"), after this seat's decision ("approved"),
       and for the refused polars request ("refused").
     - Nothing is added to `requirements.txt`.
2. **FWD-15's dell1-side receipt comes from the same drive.**
   - dell1 pulls `CT-an-1`.
   - On the delivered pack, dell1 runs `intake_receive.py verify`, `prove` and `install --target <a scratch folder>`. The
     scratch folder must not be dell1's TARGET. The receipts, with their pip logs, are committed on `box/dell1`.
   - dell1 then deletes the scratch folder. Its own work and TARGET are untouched.
   - This is one cross-box act on dell1, test-only, asked through `0.0.0_AB_MSTR` as a crossbox call; it is not a job for
     dell1's CTO to invent.
   - The duckdb receipts already committed at `d4e34f4a58` stand as relayed, without terminal output; they do not carry the
     arm.
3. **The organic arm is asked, not waited on.** One crossbox ask goes to dell2 and site Z: does any lane have a one-off read
   that needs a package absent from `requirements.txt`?
   - A yes replaces the synthetic lane in ruling 1 before the request is filed.
   - A NONE from both is recorded as the organic negative, and ruling 1 proceeds unchanged.
   - Neither answer holds the round.
4. **FWD-14:** unchanged. It waits on Andrew's sitting (`c9a4`, `b87f`); the Security-log read joins `b87f`.
5. **`W126-S1`:** I accept the issuer's disposition. It is the ruled WARN-only state, adjudicated NOT_A_DEFECT on
   another box; nothing is owed.

## 3. ENRICHMENT LIST for round 25 (one issuance)

1. The deliberate absent-package drive (ruling 1): requirements read, request, three status reads, this seat's decision,
   the pack.
2. dell1's receive on a scratch target with pip-logged receipts committed on `box/dell1`, then the scratch removed
   (ruling 2).
3. The one organic ask to dell2 and site Z (ruling 3), filed first. Its answer only changes which lane requests.
4. Nothing else: FWD-14 and FWD-17 are Andrew's acts, FWD-2 is a qualified wait, and FWD-9 is PARKED.
