# work cycle — 0.7.0_AE_CloudOps — 2026-06-02 ~2128Z

## Distribution-untier seam: artifact trace -> PII catch -> safe data-layer split defined

CTO ruled (212415Z) the untier = DATA-LAYER SPLIT (roster-free aggregate artifact L0-allowlisted +
.004a-exempt; book.json stays L1/.004a/admin) + open-Q: does an existing artifact already carry
relationship_stacked_periods?

### Trace (verified S3, advisor peter_lee)
Artifacts: book.json(169KB), composition.json, summary.json, timeseries.json(492KB), top_holdings.json,
nna_clients.json.
- relationship_stacked_periods (what the drill consumes) is ONLY in book.json (root). timeseries.json
  has no equivalent. -> no existing roster-free artifact carries it; a DS emit/strip is needed.

### PII catch (corrects the "roster-free aggregate" read)
relationship_stacked_periods is NOT roster-free: stacks[] = {client_key, display_name, aua} with
CLEARTEXT client names (Judith Ozinga $5.14M, ...). A naive extract to an L0/.004a-exempt artifact
would leak other advisors' client roster on direct fetch. BUT DistributionTab.tsx:2497 renders the
tooltip via pseudonymizeChildLabel(client_key) and keys Bars by client_key (:2512/:2517) -- it does
NOT use display_name. So display_name is unused by the drill.

### Safe split (cheapest CORRECT path)
1. [DS, routed COO] emit relationship_periods.json = relationship_stacked_periods with
   stacks={client_key, aua} + period totals, display_name STRIPPED -> genuinely roster-free.
2. [CTO] approve strip approach (security-model owner).
3. [AE/me] comp-pii audit (prove roster-free) + comp-routes trace (firm-containment) -> auth-validator-edge
   L0-allowlist diff -> CTO approves -> HALTGT/safe-apply.
4. [RD~C] repoint drill book.relationship_stacked_periods -> new artifact (no render change; pseudonymizes
   from client_key already).
book.json untouched (Books/L1/.004a/admin). Firm-containment invariant (X-Firm-Id) never relaxed.

### Actions
- CONSULT-ANSWER to CTO (212805Z): open-Q + PII catch + safe split + I own edge after DS emit+CTO approve.
- COO (212828Z): routed the DS strip-emit dispatch; flagged I'm gated on (1)+(2) before my edge leg.
- Task #11 (edge untier) in_progress, awaiting DS emit + CTO strip-approval.

Joe remains unblocked for the immediate re-smoke (session holds). My edge leg won't land a .004 change
until comp-pii-proven + CTO-approved diff (highest-blast-radius Lambda@Edge auth change).
