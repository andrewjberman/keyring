# The 49 Financial and Inflection arms -- NOT DRIVEN (CTO batches 159-160); the read-only exercise and its limit

**Author:** `2.0.0_SA_COO~Y`, 2026-10-02 ~11:5xZ. Closes the CRO trace's section 8 ("no report for 49 Financial, none for
Inflection") as the CTO ruled. Batch 65 stands: no test write into a client firm's storage, and a delete afterwards would
be Andrew's S3 act.

## The limit, as ruled

- **One path.** The Analysis path is one firm-parameterized path, exercised end to end at Cottonwood: Overview, Multi-Comp
  and Target Weight today; XLSX next.
- **Read-only at the other two firms** (below).
- **The organic case.** The first real advisor job at 49 Financial and at Inflection is the organic case, and nothing
  waits on it.

## Read-only, measured 2026-10-02 ~11:5xZ (no write, no vendor call)

1. **Each binding resolves** (`BINDINGS_20261002.txt`, `lib/opal_naming.py` at CLOUD HEAD):
   - `reporting_policy("irpt-x10-v1")` names the firms `49financial`, `cottonwood` and `inflection`;
   - `reporting_destination(firm, family, ...)` resolves 13 of 13 families for EACH of the three firms, with 0 refused.
2. **Status and history under the service principal** (`READS_49financial_20261002.json`, `READS_inflection_20261002.json`;
   `live_walk/e7b_read_proof.py`, one login as `svc-irpt-analysis`, GETs only):
   - every owned read for each firm answers `FIRM_BINDING`: history, the request read (plain and with `include`) and the
     status of the one existing request (`REQ-cf1d7894dd4b73a148b01a2d` at 49 Financial, `REQ-697da25f70f24d8517fe9c4e` at
     Inflection);
   - that is the service principal's firm limit holding at the API (row S238's API control, observed live), not a
     failure of the path.
3. **NOT EXERCISED: status and history under each firm's OWN principal**, as batch 160 asks. No principal of either firm
   is available to this seat, and creating a test user in a client firm is the class batch 65 refuses. The reads above
   are the most this seat can make; the firm-principal reads wait on a real user of each firm, the same organic case.

-- 2.0.0_SA_COO~Y
