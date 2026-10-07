# MDPF_SECCLASS row S60 -- dell1's check after the proxy fix: PASS on the laptop's localhost:5174

**archetype:** VALIDATE

Author: `3.0.0_SA_CVO` (laptop), 2026-10-07 ~17:5xZ, on `1.0.0_SA_CTO` msg 106481. A FILE; no row is minted here.

## Result: PASS

The check as stated: through `localhost:5174` the walker gets 200 on a 49 Financial client `platinum-summary`, and a
signed-out request still gets 401.

| path (each with `?firmId=49financial`) | walker | signed out |
|---|---|---|
| `/api/scoped/partners/books/advisor/dawson_moses/platinum-summary` | 200, 113,367 bytes | 401 |
| `/api/scoped/partners/books/relationship/z08373330/platinum-summary` | 200, 11,675 bytes | 401 |
| `/api/scoped/partners/books/relationship/z0893406/platinum-summary` | 200, 24,694 bytes | 401 |
| `/api/scoped/partners/books/relationship/z08123628/platinum-summary` | 200, 8,410 bytes | 401 |

Probes at 17:56:08Z to 17:56:10Z, walk output `tmp/ui-walk/20261007T175553Z` (gitignored; no 2xx body is kept).
DISARM printed REFUSED.

## The server it ran on

- `C:\tmp\portal-5174` at `3b8c292f47`, 0 changed files; the dev server processes started 17:50:08Z (they had been up
  since 14:08Z before the restart); the root answered 200.
- `vite.config.ts` line 142-143 now targets `https://d2n2nzpeqf34ge.cloudfront.net` for `/api/scoped/partners`. At
  `fc18e50b` it targeted the API Gateway host.
- Before the fix the same advisor path answered 403 (`MDPF_SECCLASS_S60_WALKER_403_CAUSE_20261007.md` @f77d1c8d7e).

## Two readings on the way, so nobody repeats them

- With no firm parameter, or with `?firm=bd`, the same four paths answer **404** "File does not exist:
  platinum/advisors/dawson_moses/summary.json" (17:52Z and 17:54Z walks). The data function falls back to the
  signed-in user's own firm when `firmId` is absent, and the walker's firm is opal-capital. The page itself sends
  `?firmId=<the selected partner>` (`src/api/endpoints/advisor-intelligence.ts` lines 627-632), so this is the probe's
  mistake, not a defect: the parameter is `firmId`, not `firm`.
- The three named clients are now reachable for a render (Books, the advisor, the client). No client page was
  rendered here: dell1's standing ask was changed to the firm view (@616a6f85e8) and nothing new was asked.

-- 3.0.0_SA_CVO
