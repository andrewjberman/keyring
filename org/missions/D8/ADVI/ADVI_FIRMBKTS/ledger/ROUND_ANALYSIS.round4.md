# ADVI_FIRMBKTS -- ROUND 4, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-13 ~06:2xZ)

**Input:** `3.0.0_SA_CVO` slug msg 4648, `surprise-channel/remediations/REMEDIATION_v5.md` @ae75a8b46d (on origin) and ADJUDICATION_v5.
- 47 orders are complete with valid proofs, TO-FB-g-6 is withdrawn, nothing is parked, and `round-close-check` reads MAY-CLOSE.
- L9 re-ran all 111 criteria and read every WORLD act live.
- 5 criteria are NOT readable from dell1: the SMS attributes, the IAM simulations, and the inf-pipeline plans. They are named, not assumed.

## 1. Graded

**The cutover landed:**
- act 4: the IRPT leg 14:03-14:13Z, the edge leg 15:15:10Z, and the split closed;
- acts 2, 3, 3b, 3c and 4b/4c as signed.
Step 7's performance adapter reads "evidence write NOT EXERCISED; canonical read simulated allowed" (act-4 half, ADDENDA 8-9). The latent Inflection fence gap is cured and
confirmed on the product path (ADDENDA 10-12, FB-f-21: 11 of 11 GETs answered 200).

| FWD | Verdict | Read |
|---|---|---|
| FWD-1 | **PARTIAL** | 139 of 150 agree (D1-C-S29). The 11 that do not agree are named in round 5 and each is fixed or ruled. |
| FWD-4 | **PARTIAL** (stage APPLIED) | The validator's canonical ownership read was never compared on the accounts and relationship paths (D1-C-S37). |
| FWD-2, 3, 5, 6, 7, 8 | as graded in ADJUDICATION_v5 | This analysis moves none of them. |

- **4b, the exec-summary fence: NOT EXERCISED.** The generator has not run since 2026-05-04 (round-3 ADDENDUM 12). That is graded as not exercised and is never inferred.
- **D1-S17 is DISARMED.** Its remediation stays open until the validator read (D1-C-S37) is exercised.

## 2. This seat's rows (D1-S28, D1-S32..S34, D1-W60-S3) and the new D1-C-S33

- **D1-W60-S3** (the naming gate exempts `/tests/` but not `test/`): ROUTED to the gate's owner, LGIC_ENFORCE. The ruling: the test-path exemption covers both spellings, by an
  explicit list, never a substring.
- **D1-S28** (`check_fence_scoped_rows.py` reads `ok=False`: `before_strip` fails `one(list)` at init, and a cp1252 `UnicodeEncodeError` occurs unless
  `PYTHONIOENCODING=utf-8`): ROUTED to the instrument's owner (shared-infra fence, lane ANY, which makes it the integrator's).
  - The ruling: every reader and writer becomes explicit `encoding='utf-8'`, per the non-ASCII law, and the init failure gets a scratch-root fixture.
  - Close: `ok=True` at HEAD with no environment override.
- **D1-S32, S33 and S34 (Black Diamond pricing):**
  - S32: the T-1 median is weighted by portfolio-group repeats.
  - S33: an unstable sort decides the same-date price tie.
  - S34: three served readers key on the transactions FILE day, not `trade_date`.
  These are real correctness findings on a pipeline FIRMBKTS MOVED, not defined. No active project owns that pipeline's pricing rules. **Round 5 carries ONE read-only
  cell that QUANTIFIES each one on served values:** the dollar and date counts that would change under the corrected rule, with each rule's writer named. A non-zero result goes
  to the CRO for a brief under its own project; a zero closes the row as not material.
- **D1-C-S33** (the `auth-validator-edge` spec fails 1 of 6 at HEAD: its dormancy expectation predates the flip): a test-only fix, as FB-g-37 did for the router and guard.

## 3. ENRICHMENT LIST (round 5, ONE issuance by `2.0.0_SA_COO~B1`)

1. **FWD-1's 11 disagreements:** name each, then fix it or rule it.
2. **FWD-4 / D1-C-S37:** a deliberate comparison of the validator's ownership decisions on the accounts and relationship paths.
   - Offline: replay the decisions against the legacy map and against the canonical map, which are byte-equal, so the decisions must be equal.
   - Live: one signed non-admin session read on those paths.
   D1-S17's remediation closes on it.
3. **D1-C-S33:** the validator spec, test-only.
4. **The exec-summary DIAGNOSIS** (read-only, round-3 ADDENDUM 12): the `put-events` error text, the bus and rule, and the dispatcher's `events:PutEvents` grant. The fix is a
   later cell under its own pair.
5. **The BD pricing quantification** (section 2), read-only.
6. **Act 2's first scheduled chain read** (the 2026-10-13 ~04:00Z chain), if it is not already in the packet: the producers wrote only the canonical home, and the maps
   stayed byte-equal.

## 4. ACTS ONLY ANDREW CAN DO (cited)

None for the round. **Information:** 49 Financial's client exec summaries have not refreshed since 2026-05-04. When the generator's fix lands, its regeneration serves up to 158
client-facing summaries. This seat recommends Andrew reads a sample first (round-3 ADDENDUM 12, item 4).

-- 1.0.0_SA_CTO~DELL1
