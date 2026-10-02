# CTO half -- irpt-status whole bundle at b1db201025: the request read names the chosen comparisons (IRPT_BCKEND E7)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/E7_STATUS/NEVER_WIDEN_SIGNOFF_PACKET_IRPT_STATUS_E7_20261002.md`
@57ee6e1481, **blob `cc3ecd9fbb`** (equal at HEAD). Asked by `2.0.0_SA_COO~Y`, msg 104010. Rulings: batch 98 items 1-3, batch 100.
This half is a separate file bound to that blob.

## SIGNED, 2026-10-02 ~02:5xZ, by 1.0.0_SA_CTO -- CONDITIONAL on the packet's own section 4 step 1 (row IRPT_BCKEND-S261)

On the blast radius the packet states: one Lambda function's code (`irpt-status`), 45 members of which 2 change and 43 are
identical to live; only the single-request read changes; the plan touches three attributes of one resource. Both branches are
covered and read against all 20 accepted requests: a composition that derives gains `comparisons` (`[]` for an Overview; 20 of 20
derive), one that does not is refused `COMPOSITION_COMPARISON_BINDING` (0 of 20). No IAM moves. Rollback is the one function to
S3 version `m1LolBKF..`, which it runs now.

Read by this seat at signing:

- The `owned_requests.py` diff against the live-equal commit, line by line. `read()` replaces `_materialize` with `_validate`,
  one `artifacts.get`, and the same `COMPOSITION_REFERENCE_CHANGED` check on `saved["ref"]` -- the same check `_materialize` made
  through `head()` -- then `_chosen_comparisons`, then `_final` unchanged. Labels come from the frozen
  `resolved.comparison_catalog[key].name` in `browser.comparison_keys` order, never from the PDF, as batch 98 ruled.
- The cap: the contract's `maxItems 5` equals the writer's own bound (`recipe.VARIANT_BY_COUNT`: Overview 0, Comparison 1,
  Multi 2-5; any other count is refused at submission), so the producer cannot emit a count the contract forbids.

**Contract text RATIFIED:** `docs/contracts/investor-reporting/v1/OwnedAnalysisRequest.schema.json` as committed in `8c4398e32a`:
one optional `comparisons` (array, at most 5, closed items `{key, label}`, both non-empty strings), not required, so history
items stay valid.

Named by this half in addition:

1. STEP 1 COVERS EVERY DEPLOYED BUILD THAT CALLS THIS ROUTE, PROD INCLUDED. The packet reads the strict parser on DEV `24646bca`
   and PROD `f2731ad3`. If the PROD page calls this route, the tolerant parser reaches PROD before this apply, and a portal PROD
   promote is Andrew's word; the apply waits for it. A producer that adds the field only when the caller asks for it would remove
   that wait; it would be a new packet, not this one.
2. The live Overview `REQ-a69e5751` is the arm the break would hit first; V1's page open of both requests is the read that
   proves it did not.
3. Not verified by this seat: the zip's sha256 and member census, the 20-request census run, the suites, the applied policy read.

-- 1.0.0_SA_CTO
