# CTO ROUND ANALYSIS -- IRPT_BCKEND round 8 -- 2026-09-21 ~22:0xZ

**Against:** `3.0.0_SA_CVO~B`'s L10 slug `surprise-channel/remediations/REMEDIATION_v2.md` @`9d7a369b38`, and
L9 `ADJUDICATION_v4.md` (C-S124..C-S144, same commit). This is the second of the three L10 acts (slug -> CTO
analysis -> COO recut), per Rule 27. Round 9 is cut by `2.0.0_SA_COO~B` in ONE issuance after this lands.

## Coverage read -- round 8 closes; no PRD addendum

Terminality: 0 open of 87 on the canonical refuser. This was measured independently by this seat, COO~B and
CVO~B, and all 329 investigations are dispositioned. Six judgments:
- R76-AC2 PASS
- R83-AC3 PASS
- R85-AC3 PASS
- R80-AC2 FAIL
- R77-AC2 NOT_EVALUATED
- R81-AC2 NOT_EVALUATED

No outcome was claimed REALIZED:
- **FWD-2** is SPLIT and NOT_REALIZED. Serving reached 3 of 3 firm routes; submit still raises NOT_READY.
- **FWD-11**'s backend half ADVANCED but is NOT_REALIZED. Bucket recovery and IaC reconciliation are enabling
  work, not the Global report/export proof.
- **FWD-5**: no claim this round.

None of this reveals an outcome the endpoint mis-stated, so there is no SCOPE_CHANGE and no PRD addendum. The gaps
are cells to cut.

## Carried into round 9 -- ONE issuance, ordered for parallel fan-out

**Wave 1 (independent; run in parallel):**
1. **Capture-tool repair: C-S125, C-S126, C-S127** (R80-AC2 FAIL). Three fixes:
   - the printed port-forward command is executable verbatim, and the README matches it (S125)
   - a POSITIVE authenticated-readiness signal for the intended route; error, redirect and 5xx pages are
     refused, so absence of a password field never counts as success (S126)
   - the portal origin is enforced, not just conventional (S127)

   Acceptance must include CVO~B's own VM diagnostic
   (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R8_CAPTURE_DIAGNOSTIC.cjs` @`06fe4f1848`): its
   HTTP500 and arbitrary-origin counterexamples must now REFUSE, and its password-positive control must still
   pass. No host start, credential or live login in this cell.
2. **S102: the ycharts missing-source build defect.** CVO confirms it is NOT fixed (S111's denominator was);
   cut it.
3. **L4 negative control: 0 of 2 exercised. The instrument is revised by this ruling (below).**
4. **C-S144: re-issue R77's judgment with a SUBSTANTIVE, discriminating bar.** The issued face gave an id and the
   word "judgment" with no bar, so it could not be graded; no retroactive PASS.
5. **Premise corrections on COO~B's own faces:** W3-S51 and W1-S46. Fix the text the next reader relies on; do
   not flip disclosed failures to complete.

**Wave 2 (gated on wave 1 item 1 AND a human session):**
6. **rth-2 re-cut** with its stated precondition: the capture tool is fixed, then the host is started, then an
   authorized session is captured and verified by the fixed tool (ruling @`438312b085` + addendum
   @`e73c8e2f71`). After that, rth-2's original bounded latency measurement re-runs. W2-S62, W3-S52 and W1-S43
   (submit wiring) ride with it. Authentication and render latency stay SEPARATE questions: a 900 s budget
   does not prove a render cannot finish inside 29 s. **The sync-vs-async contract is decided by this seat on
   the measured number, not before.**

**Do NOT re-dispatch** W1-S48, S111, S112, S113, W7-S2 or W8-S2: they are REMEDIATED in-round.

## RULING -- the L4 negative-control instrument (the decision CVO~B routed here)

The instrument as it stood is **REVISED**. CVO~B is right on both counts:
- `i-02448edb624a7a7cf` is MDPF's daily runner, not the capture host.
- A bare AccessDenied from a principal whose IAM does not grant the target action proves only IAM, never the
  bucket-policy fence.

A negative control is DISCRIMINATING only if the same attempt could have succeeded were the fence absent.
**For each of the 2 buckets, the cell records:**
- **(a) THE PRINCIPAL:** an EXISTING identity, NOT on the fence's exemption list, whose IAM ALREADY allows the
  exact action on the exact key pattern tried. It is named with its ARN and the policy statement granting it.
- **(b) POSITIVE ARM:** that same principal, same action, succeeds on a control target inside its grant but
  outside the fence. This proves the call can succeed.
- **(c) NEGATIVE ARM:** the fenced bucket's key is denied, and the denial is ATTRIBUTABLE to the bucket policy.
  Attribution comes from S3's own error context (a denial naming an explicit deny in a resource-based policy)
  and/or the CloudTrail record, never the bare error code.
- **(d)** The denied attempts and permitted controls, printed with the actual identity, action and key.

**Constraints:**
- No grant is widened to make the test possible.
- No host is started for it; use an identity assumable from where the seat already runs.
- If no existing principal satisfies (a), the cell's honest result is **"L4 cannot be discriminatingly exercised
  without a new grant."** That is a finding routed back here, not a PASS and not a reason to create a grant.

## Outside IRPT's chain -- named, not cut here

- **S116** (the `fence_patterns()` role-name hyphen) and **W1-S47** (the naming diagnostic premise) sit on
  `lib/opal_naming.py` / the naming gate. That is this seat's own lane, under LGIC_ENFORCE's chain, not
  IRPT_BCKEND's. CVO~B is right that an IRPT cell must not write another project's chain. **This seat owns
  resolving them in that lane**, queued behind IRPT per the device priority. They stay carried as external
  findings until then.
- **Break-glass role deletion:** COO~B reports the CRO's own condition is met. That decision is the CRO's and
  Andrew's; nothing here authorizes it.
- **The 150 older remediation rows carried by rth-4:** an owner census is not hazard resolution. They stay open
  in this seat's read; no bulk close.

## The frontend dependency -- why round 9's ordering matters

IRPT_FNTEND's completion grade (@`4030dac`) left 7 of its 8 outcomes NOT_EVALUATED because each needs
IRPT_BCKEND's served half: FWD-1, 3, 4, 5, 6, 8, 11. Round 9 wave 1 does not close those directly, but S102 (the
ycharts build) and the rth-2 chain are the backend work FWD-4's export chain needs. **Every other open item waits
on the human session, so the parallel wave-1 cells are where this round buys time.** Andrew asked for more
parallelization from COO~B.

**PUSH STATE:** LOCAL on CLOUD; only `0.0.0_AB_MSTR` pushes.
