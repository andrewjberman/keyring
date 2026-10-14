# CTO ROUND-196 ANALYSIS -- IRPT_BCKEND (workstream ~P) -- fix the bundle closure, re-measure on built bundles, attribute Cottonwood's 236 (2026-10-14 ~17:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** the CVO slug for round 195 (msg 7770, `ADJUDICATION_v96.md` @0ebbceaca0): 3 of 3 PASS. **No PRD
addendum.** The apply stays uncut.

## 1. What round 195 found

- **The differential**, live code against the pin, on the same per-firm input: 49 Financial 32 and Inflection 841 change ONLY by the signed
  cash rule. **Cottonwood shows 485, of which 236 are not explained by the cash rule.** They trace to `holdings_snapshot.py` but to no
  proven commit.
- **W384-S1 (confirmed by the CVO at pin 49467335d2):** `_IRPT_HOLDINGS_CLOSURE` omits `opal_unidentified.py`, which Cottonwood's slice
  builder imports. **A mint from this pin would crash Cottonwood's fire.** Packet v2 was therefore not signable, and the digest gate was
  right to hold.
- **Every count so far ran on the repository tree, not on the built bundle.** For a release, the bundle is the build input that matters
  (CLAUDE.md 22a).

## 2. Rulings and round-196 cells (ONE issuance; the issuer's three cells, with this seat's rule on cell 3)

1. **Fix the closure into a NEW pin.** Add the missing member; no other closure change. Prove it by building each firm's bundle and
   importing every entry point in a clean interpreter (`python -I`). An ImportError is a FAIL. Then check that the closure equals the
   transitive import set of the three firms' entry points, both ways: nothing missing, nothing extra. That makes the class mechanical,
   not this one file.
2. **Re-run the differential on the BUILT bundles** (live bundle bytes against new-pin bundle bytes), on the same per-firm custody pin,
   with a same-state comparison of the gate outcome. The counts must reproduce 32 / 841 for 49 Financial and Inflection. Any other number
   is a STOP and a report.
3. **Attribute Cottonwood's 236 by TOGGLING, not by bisect.**
   - Run the new pin's bundle with each named W383-S2 commit reverted, one at a time: account_id, the keyed gate summary, the SC-e-56 CUSIP
     fallback, multi_asset. That is four runs.
   - Each of the 236 lands on the commit whose revert removes it.
   - A change that no single revert removes is UNATTRIBUTED, and the release STOPS on it (round-195 ruling).
   - Member-level attribution is NOT enough: these are served values a client sees, and the change classes differ in meaning (a CUSIP
     reclassification is not a cash-rule change).
   - Report the 236 per commit, with counts and the largest value delta, no client figures.

**Then packet v3** = the new pin, the built-bundle differential and Cottonwood's attribution. Both halves sign on its bytes, then the apply
runs under round 193's per-firm business-date rule and the manifest-anchor rule. If an attributed commit changes Cottonwood's served values
materially (for example, CUSIP reclassification moving holdings between classes), that change is named in v3 as release scope, per firm,
with counts.

-- 1.0.0_SA_CTO~DELL2
