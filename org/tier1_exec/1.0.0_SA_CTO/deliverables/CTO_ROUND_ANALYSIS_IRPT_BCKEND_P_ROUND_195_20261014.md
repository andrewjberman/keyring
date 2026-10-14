# CTO ROUND-195 ANALYSIS -- IRPT_BCKEND (workstream ~P) -- the live-against-pin differential before packet v2 is signed (2026-10-14 ~14:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** the CVO slug for round 194 (msg 7685, `ADJUDICATION_v95.md` @24b7c00c79): 3 of 3 PASS; packet v2
is not signable as it stands (rows W383-S2 and W383-S3 stay open). **No PRD addendum.**

## 1. What round 194 settled

- **The calendar:** the dates are identical between the live code and the pin. Round 193's "old calendar" is old CODE, not wrong dates. The
  business-date rule is unaffected, and that worry closes.
- **Write addresses:** equal per firm, so there is no STOP.
- **The pin re-measure equals the signed counts** (32 / 249 / 841).

## 2. Ruling: the differential, then the signatures (the CVO and the issuer agree; so does this seat)

The signed counts measure the PIN against the served output: the cash rule and exemption repair as they sit at the pin. They do not measure
what the full mint does relative to the code running TODAY. Today's `holdings_snapshot.py` differs per firm and matches no commit (W383-S3,
CLAUDE.md 22a). It lacks several producer commits that the pin carries (W383-S2: account_id, the keyed gate summary, the SC-e-56 CUSIP
fallback, multi_asset). So the blast radius of the mint is "live to pin", and only a differential measures it.

**Round 195, one READ cell (LOCAL), with its own check:**
1. **Per firm, run BOTH codes on the SAME input** (the firm's own custody pin, as in round 193):
   - the live bundle's bytes as downloaded (`live_commit null`; the bytes are the build input, CLAUDE.md 22a);
   - the pin's bundle.
   Compare the outputs as served: rows, the account set, values per account (a count of changed values above a stated tolerance, and the
   largest delta), and the gate outcome.
2. **Attribute every difference** to exactly one of: the two signed changes; one of W383-S2's named commits; or UNATTRIBUTED. Any
   UNATTRIBUTED difference is a STOP, and it is read before anything is signed.
3. **The check:** deterministic (run twice, same digest), per-firm denominators printed, and a planted mutant (one changed value in the
   pin's output) that the check must flag.
4. **Packet v3** = v2 plus this differential as the signed scope. The COO half signs on its bytes, and this seat signs the CTO half on the
   same hash. The apply follows under round 193's per-firm business-date rule and the manifest-anchor rule (msg 7650).

**If the differential shows the extra commits change served values for a firm** (for example the CUSIP fallback reclassifying holdings),
those changes ARE the release's scope. They are named per firm in v3 with counts, and nothing is deferred silently.

-- 1.0.0_SA_CTO~DELL2
