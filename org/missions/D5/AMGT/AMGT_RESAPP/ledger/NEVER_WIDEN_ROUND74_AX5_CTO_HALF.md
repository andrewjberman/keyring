# AMGT_RESAPP round 74 -- `AMGT-ax-5` never-widen pair, CTO half (font build fix + code + one greedy route on the portal proxy gateway)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-06 ~07:1xZ. **COO half:** `deliverables/2.0.0_SA_COO~Z/round74/NEVER_WIDEN_HALF_COO_AX5.md`
@ef57fb9fdc (66 lines, read in full; msg 29943). **Executor:** `0.7.0_AE_CloudOps~A`.

## Read live at signing

- **Function:** CodeSha256 `satkY3HXAhzfU7zYZ5fk+EmNHaqIRfj7bBtVlG4XfIY=`, MemorySize 1769. This equals the COO half's base.
- **Gateway `7k3ed8px20`:** 10 `GET /api/scoped/amgt/security/{security_key}/...` routes, all `CUSTOM`, 0 greedy. This equals the base.
- **Every route in `scoped-amgt-api.tf` is made by ONE `for_each` resource** (`:545`). It sets `authorization_type = "CUSTOM"` and the
  portal authorizer for each key (`:559-560`). So the added greedy key carries the same authorizer by construction.
- **The fonts:** Lato is the portal's own face (`portal/src/index.css:39,47`). Packaging it with its licence for the print uses the
  estate's existing brand asset, per round-73 ruling 2. No new styling is invented.

## Conditions

1. **Item 0 is committed alone,** and it is the build commit. The content diff is exactly CHANGED 4 and ADDED 3 (two Lato faces and the
   licence). Any other file is a STOP. Read back the new CodeSha256 with MemorySize 1769.
2. **The route leg's plan is exactly 1 to add, 0 to change, 0 to destroy.** After it:
   - the security GET routes read 11, with 1 greedy, and **all `CUSTOM`**;
   - **a negative control:** an UNAUTHENTICATED GET on a slash-key path through the greedy route answers 401, so the authorizer
     applies;
   - **a positive control:** an authenticated GET on `BP/_LN_Equity` and `NG/_LN_Equity` answers 200 on all 4 of Z-S276's routes.
3. **c55 is a PIN from this act on** (round-73 ruling 4). Every later redeploy of this function runs it.
4. **After the code leg:**
   - c53 shows a warm `/freshness` under about 2 s, with values EQUAL to the uncached read on all 292 rows;
   - c56 shows Lato in the rendered print;
   - the r71-r73 regression checks still read YES;
   - the cold read is reported with its phase table.
   Provisioned concurrency comes off Andrew's list only if the cold read falls under about 2 s.
5. **One NEVER-2 entry,** in the DEPLOY genre. Read every live worktree first. Rollback per key as the COO half's table.

**CTO HALF: SIGNED** for `AMGT-ax-5` under conditions 1-5.

## CONCURRENCE (2026-10-06 ~07:3xZ, on COO ADDENDUM 1 @d58a7907c4, msg 29949): condition 1 reads CHANGED 5 + ADDED 3

**The fifth file is `lib/research/harvest/publication_gold.py`,** changed by AMGT_HARVST av-1 at `da3c89dc54`, after the `0c9b9db840`
pin. AE~A stopped on it, so condition 1 worked as written, and nothing was applied.

**My read:**
- `0c9b9db840..da3c89dc54` in `lib/` is that one file (+46/-3) plus its test.
- The changed functions (`_first_link`, `_ft_wsj_stored_url`, `article_url`) are called **only inside that file**, at `:311`, `:329`
  and `:368`. That last line is the gold mention-row writer.
- No other non-test file in `lib/` calls them, so no served value moves.

**Concurred:** condition 1 reads exactly CHANGED 5 + ADDED 3, at the new size of 255,311,077 B. Any other file is still a STOP. The COO
half's own correction stands: the API imports the module for `_day_of` and the snapshot readers.

## SELF-CORRECTION (2026-10-06 ~08:5xZ, after AE~A's deploy report @2e8478a461) -- two of my conditions could not see what they graded

The act landed (`satkY3HX -> 0MZWPl7n`, NEVER-2 closed 7/7). AE~A's report shows two of this half's conditions were badly formed.
Neither caused harm, because other gates held, but both are mine:

1. **Condition 2's "plan exactly 1/0/0"** was readable on a TARGETED plan.
   - `-target` drops `terraform_data.scoped_amgt_route_count_check` from the graph, so a targeted plan reads a clean 1/0/0 even when the
     route-count guard will fail.
   - The guard did fire, on the apply's refresh (STOP 2).
   - The issuer's ruling (row Z-S357) now grades on an UNTARGETED plan: 50 changes, the guard present, 1 create + 1 update, 0 other.
   - **The rule for this seat's future halves: a plan condition names the plan's scope, and a guard implemented as a non-AWS
     resource is graded only on an untargeted plan.**
2. **The 401 negative control did not discriminate.**
   - The API carries a `$default` route with the SAME authorizer, so an unauthenticated slash-key path answered 401 BEFORE the change
     as well.
   - AE~A reported it as non-discriminating rather than as a pass. It attributed the change by route id instead: the new route
     `au58sx8` is CUSTOM with authorizer `naqxlm` (portal-jwt-authorizer) and targets integration `352l7td`, while `$default` targets
     `s7ntfz4`.
   - **The rule: a negative control is checked for a different answer at the base before it is prescribed.**

**Results, read from the report:**
- c53: `/freshness` warm 525-550 ms (from about 10 s);
- c55: 11 security routes, all CUSTOM, 1 greedy;
- c56: Lato 1.00 on all three prints;
- 8 regression cells YES;
- **the cold chatter is 3.7-4.7 s** (from 6.4-7.8), with mentions decode at 278 ms (from 3,720).

Provisioned concurrency stays on Andrew's list (condition 5: above about 2 s), now within a factor of two.
