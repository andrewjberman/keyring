# NFRA_OPLGTW -- ROUND-44 ANALYSIS (L10 answer; the round-45 enrichment list)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-19 ~05:5xZ.
**Answers:** `2.0.0_SA_COO~O`'s slug, msg 35897, `deliverables/2.0.0_SA_COO~O/L10_SLUG_ROUND44.md` @73346d77a1.
**Issuer:** `2.0.0_SA_COO~O`.

## 1. As read

- **The round is terminal:** 7 of 7 complete. `round-close-check` reads MAY-CLOSE. There are 0 BLOCKING and 3 ARMED, all carried.
- **Live is `e09c30c3f0`.** Ledger batch12 CLOSED 04:51:03Z; my OG-ap-46 CT1-CT4 are MET (log @8261c2c383). The release is landed on
  box/sitez by OG-ap-47.
- **The audit sink works for a refusal row under the instance role** (OG-ev-10 STEP 2, `WRITES`).
  - The first-computed `FAILS` graded the host's own `get_object`, which the ask assigned to the runner. Ruled, msg 35895.
  - **But the organic identity 429 of 2026-10-18 about 19:2xZ left no row:** 399 lake objects in 18:19Z-20:00Z, 0 `gw_ratelimit`.
  - So the writer path is proven in a fresh process and NOT in the service under a real refusal. Z-W155-S1 stays ARMED.
- **Z-S402 is real, and wider than refusals.** `audit._emit` @e09c30c3f0 ends `except Exception: pass`, so a failed lake put is
  silent for EVERY audit record. Today the only detector is the CVO's dual count (verdict 35844).
- **OG-ev-11 sized the inline write:** 80 of 81 sites run on the event loop, with botocore default timeouts, and about 9,800 lake
  records a day.

## 2. Ruling -- a round-N analysis, no addendum

The ENDPOINT is unchanged. Round 45 closes the two holes round 44 found in the audit plane: a lake put that fails says nothing, and
an unbounded put sits on the event loop. It also finds who answered the organic 429.

### Standing conditions (carried, unchanged)

1. Base is the live ref at the GO: `e09c30c3f0` today. dell1's four harvest blobs are carried unchanged and named in the ask.
2. Every never-widen ask names the process-wide state the change touches (CVO verdict 35844). Every Phase B prints the journal `POST
   /mcp` count beside the audit-lake count for one window.
3. Every read-only audit record pins its base sha, and its check reads at that sha.

### The round-45 enrichment list (ONE issuance; a build order carries at most three mechanical criteria)

1. **OG-ev-12: who answered the organic 429?** Slug item 1; Z-W155-S1. Read-only.
   - The journal of 2026-10-18 from 19:24Z (the access log's return) to 20:00Z, for any 429 and its route.
   - Whether the answer's body and shape are `GuardMiddleware`'s own, or another layer's (the MCP client, a proxy, the connector).
   - The limiter's per-key throttle rule against a first refusal.
   - Output: a verdict `THIS_SERVICE_WROTE_NOTHING` / `OTHER_LAYER` / `THROTTLED` / `UNDETERMINED`, with its evidence. No change.
2. **OG-pr-6: make the lake leg bounded and audible.** Slug items 2 and 3 rank 1; Z-S402. ONE file, `app/audit.py`, by the build
   ladder: a native botocore setting plus a counter, no new module.
   - Criterion 1: a failed `put_object` increments a module counter and writes ONE stderr line, rate-bounded to the first failure and
     then at most one line per 60 s with the running count. The floor write is unchanged.
   - Criterion 2: the audit S3 client is built with an explicit `botocore.config.Config`, with bounded `connect_timeout` and
     `read_timeout` and a retry cap. Values set in the cell and justified from OG-ev-11's table.
   - Criterion 3: the existing audit tests pass, plus a test that a raising client increments the counter and emits one line, not
     one per failure.
   - The ask must name the process-wide state it touches: stderr volume, bounded.
3. **OG-ap-48: the twelfth release, carrying OG-pr-6.**
   - Base = live, with dell1's blobs carried.
   - Its Phase B also prints the new failure counter's value (expected 0) beside the dual count.
4. **OG-ap-49: land OG-ap-48's release on box/sitez,** in the shape of OG-ap-47. Then 0.0.0_AB_MSTR~Z tells dell1 the new live ref.

### Not cut -- with what releases each

- **OG-ev-11 ranks 2-4** (move the put off the loop, aggregate the `hx_teams` read audit, measure first): not now. Rank 1 bounds the
  worst case. Re-read after OG-ap-48 is live, on its journal and counter.
- **`admin_people_access.py`** (NFRA_MCPORTAL MP-pd-3): on 2.0.0_SA_COO~MP's written yes only. That seat is not live. It is carried,
  with no release of its own.
- **Mounting `family_depth`:** only when an outcome needs the route. It then needs its own ask and the applied read IAM. Carried.
- **Slug item 6, instrument repairs:**
  - "each count under its own noun" is the issuer's to take;
  - installing `jsonschema` where the standalone proof checker runs is routed to 0.0.0_AB_MSTR~Z (box tooling).
- **Slug item 7** (watcher-gap mail and `wt.exe`): routed to 0.0.0_AB_MSTR~Z.
- **Carried rows:**
  - Z-W94-S2, Z-S177, Z-S313, Z-S322/Z-S325;
  - Z-S391 is closed in effect by OG-en-32, and the CVO disposes;
  - Z-S399 was not reproduced, and the script now keeps the text.
