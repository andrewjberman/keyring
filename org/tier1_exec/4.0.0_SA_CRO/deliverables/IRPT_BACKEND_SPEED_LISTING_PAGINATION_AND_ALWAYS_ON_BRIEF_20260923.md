# IRPT backend speed: why the client list is slow, how pagination works, what is behind the Analysis tab, and whether an always-on EC2 helps

**Prepared by:** `4.0.0_SA_CRO`, 2026-09-23 ~19:5xZ.

**For:** Andrew and `1.0.0_SA_CTO` (Codex, IRPT governor).

**Scope:** a read-only investigation. Nothing was invoked, deployed, started or stopped, except the two authorized
YCharts calls recorded in `ANDREW_DIRECT_20260923_YCHARTS_TICKER_LOOKUP_TEST_PER_USE_AUTHORIZATION.md`.

**Vintages:**
- workspace CLOUD `b475b96309` -> `94904048d0`;
- portal DEV `10141b6d0b`;
- AWS account 313476888478, read ~19:15Z, with the 7-day window ending then.

**Method:** two read-only research passes. Their scratch outputs, including the Logs Insights queries and the offline
benchmark, are in the session scratchpad (`listing_trace/`, `topology_trace/`). This seat re-checked the load-bearing
numbers on a second instrument (section 7).

## 0. Andrew's words, verbatim (2026-09-23)

> Sure why dont you take a look at the current backend setup of the "Analysis" tab on IRPT, Investor Reporting portal
> page. See what they have going on for this function. It may end up that for speed sake we want a small ec2 running
> perpetually for this rather than the ec2 cookie crawl/lambda cookie grab and REST, for speed sake for this function
> and for loading clients. I notice the clients load is very very slow, would be curious to better understand that
> aspect as well and why that is. With that said, proceed through the 2-call testing, and more broadly an investigation
> into the dynamics of the backend server/serverless setup, primarily because I'm wondering if we can make the client &
> account listing for all of this be way faster. With that said, I want to understand how the client data is currently
> paginated, because the idea with paginating is to make things faster, not clunky and annoying, so def will want an
> analysis on the pagination function specifically as well for the loads.

## 1. The answer

1. **The client list takes ~7.4 s warm and 10-16 s cold. The cause is repeated backend work, not "serverless" as such.**
   - Every request reads the firm's whole client directory (49 Financial: **6.46 MB, 4,576 entries**) **three times**
     from S3, plus the ownership map three times. That is 9 S3 reads, each through a brand-new S3 client.
   - It re-hashes and re-sorts all 4,576 entries.
   - It runs on a 512 MB Lambda (about 0.29 of a CPU).
   - Nothing is kept between requests.
   - "Global" then resolves the three firms one after another, and the browser waits for that before it even asks for
     the first page.
2. **Pagination currently makes it worse.**
   - 25 rows per page, and every page re-downloads and re-sorts the whole firm, so page 2 costs as much as page 1
     (~1-2.8 s).
   - 49 Financial needs 184 clicks to see everyone.
   - The "Load more" button sits outside the dropdown.
   - Rows arrive in firm blocks, not alphabetically.
   - Every keystroke blanks the list.
   - Any failure wipes it.
   - The whole workspace, list included, is rebuilt whenever the login token refreshes (about every 10 minutes while
     active).
3. **Code and config fixes should cut it to under a second.** The biggest four:
   - read once per request;
   - cache the parsed directory per version;
   - raise the Lambda to ~1.7 GB;
   - start the first page at the same time as resolve.

   None of these needs new infrastructure. Section 2 gives the lever list with estimated effects.
4. **The Analysis tab's report generation does not work end to end today, on any host.** Three independent breaks:
   - the submit Lambda runs an older build that writes to the queue, but its role has **no `sqs:SendMessage`**;
   - **nothing consumes** the generation queue;
   - the YCharts session store is empty and the runner app is not deployed.

   Separately, the upload route and the request-list routes are not live (3 of 17 declared routes).
5. **An always-on EC2 would not fix client loading.** That delay is S3, CPU and serial calls inside Lambdas, and an
   always-on box would still have to re-check entitlements per request. **It is the right answer for the YCharts
   side:**
   - one small dedicated host (t3.small ~$19.5/month, t3.medium ~$35/month) that owns the YCharts session and consumes
     the generation queue, with **no inbound port**;
   - it replaces the "start EC2 -> crawl cookie -> stop" dance for every job.

   Ticker lookups need no session at all: `securities_info` is open (measured today).

## 2. The client and account list

### 2.1 What happens when a user opens the list (warm, measured ~18:53Z)

```
page open (internal user, firm = Global)
  POST /directory/resolve  (Global = 49F -> Cottonwood -> Inflection, IN SERIES)   ~4.6 s   (dev sends it twice)
      | only after it returns
      v
  GET /directory/browse?limit=25  x3 firms, in parallel                               ~1.1 s small firms,
                                                                                      ~2.4 s 49 Financial
  => first full list visible                                                          ~7.4 s  (cold: ~16 s)
typing (250 ms debounce)  -> the list is blanked, all 3 firms re-browsed              ~2.5 s per keystroke burst
"Load more clients"       -> each firm re-reads and re-sorts its whole directory      ~1-2.8 s per click
click a client            -> POST /selections                                         ~1.2-3.0 s, then holdings (called twice)
login-token refresh (~10 min, or return to the tab after 8 min) -> the workspace remounts -> all of the above again
```

**Evidence:**
- frontend: `portal/src/pages/InvestorReporting/index.tsx:43-83,108-131` and
  `header/ClientSearch.tsx:47-95,127,179` @`10141b6d0b`;
- backend: `infra/aws/lambda/investor-reporting/_authz/served.py:662-684`, `enforce.py:317-319`, `loaders.py:4-5,35-37,61-63,148-177`,
  `selection.py:19-22`, and `directory/entry.py:257-289,335-345` at the DEPLOYED pins (below);
- timings: Lambda REPORT lines matched to the edge log's arrival times.

**Deployed code is ahead of CLOUD.** The live `irpt-directory-search` (deployed 17:46:25Z) runs `entry.py` and
`served.py` from `6cd8adb582` and `bc3727b3a3`. The Global / `selected_tenant` code that is running is **not on CLOUD
HEAD**. That is recorded drift, from P's integration branch.

### 2.2 Why it is slow, ranked (MEASURED unless marked)

| # | Cause | Size of effect |
|---|---|---|
| 1 | Directory and ownership map read 3x each per request (9 S3 reads, a fresh boto3 client each); the whole directory re-hashed and re-sorted per request; nothing cached between warm calls (`loaders.py:4-5,35-37` forbids caching grants, on purpose) | small firms ~1.1 s warm on ~28 ms of CPU, so the floor is S3 round trips (INFERRED); 49 Financial adds 3 x 6.46 MB of downloads |
| 2 | Serial chain: Global resolves 3 firms one after another; browse waits for resolve | ~7.4 s warm to the first full list |
| 3 | 512 MB = ~0.29 vCPU; peak memory 153 MB, so CPU is the limit | 49 Financial warm p50 ~2.4 s |
| 4 | Cold starts, multiplied by fan-out (3 parallel browses per action; dev double-resolve; superseded searches not cancelled) | 18% of calls cold; cold calls 2.3-6.7 s |
| 5 | Pagination design (section 3) | every page costs the same as page 1 |
| 6 | Login-token refresh remounts the workspace | the full reload repeats about every 10 minutes |
| 7 | The API authorizer runs on every call, with no result caching | authorizer p90 0.2-0.5 s; cold ~0.9 s |

**Live numbers:**
- `irpt-directory-search` since the 17:46Z deploy: 73 calls, p50 **2.4 s**, p90 **4.8 s**, max **6.7 s**.
- The CloudWatch Duration metric agrees: 77 samples by 19:30Z, average 2.6 s, max 6.7 s.
- Config: 512 MB, no VPC, no layers, no alias or version, so provisioned concurrency is impossible as deployed.
- Other IRPT Lambdas are fast when warm (performance 76 ms, status 157 ms) but slow on their first call per container
  (0.7-4.4 s).
- The portal's browser keep-warm hook covers only `/advisor-intelligence` and `/portfolios`
  (`portal/src/hooks/useLambdaKeepWarm.ts:30`). **IRPT is not covered.**

### 2.3 Levers (estimated effects INFERRED; owners per IRPT contract v1.3)

**Backend** (COO~P's surface; config changes through `safe-apply`):

| Lever | Estimated effect | Note |
|---|---|---|
| B1 read the directory and ownership map ONCE per request | 49F ~2.5 -> ~1.2 s; small firms -> ~0.5 s | no conflict with authorization |
| B2 one reusable S3 client per container | -0.2 to -0.6 s per call | none |
| B3 cache the PARSED directory and its hash per artifact version between warm calls; keep re-reading the pointer, ownership and policy every call, so revocation is still immediate | 49F warm -> ~0.3-0.5 s | touches the no-cache rule `loaders.py:35-37`; **needs a CTO ruling** |
| B4 sort once per directory version, and only filter by entitlement per request | removes the per-page sort | none |
| B5 resolve Global's 3 firms in parallel | Global = the slowest firm, not the sum | none |
| B6 memory 512 -> ~1,769 MB (config only) | ~3.5x CPU; 49F -> ~1.0-1.3 s; cost trivial at ~100 calls/day | none |
| B7 extend the browser keep-warm to IRPT routes (the estate's preferred cold-start fix, `docs/architecture/ADHC_KEEPWARM_PRD.md:15-20`) | removes most cold starts while a user is active | ~$0 |
| B8 authorizer result caching (a TTL) | one fewer Lambda hop per call | shared portal-wide; security/CloudOps owns it |

**Frontend** (COO~P):

| Lever | Estimated effect |
|---|---|
| F1 stop the remount on token refresh: key the session cache on identity and claims, not on the access token itself (`index.tsx:43-45`); the comment calls the rotation intentional, so **it needs a CTO call** | no 10-minute reloads |
| F2 fire the first browse together with resolve (browse re-authorizes on the server anyway) | saves one full round trip, ~2.5-4.5 s |
| F3 100 rows per page (both sides allow it; the server cost is the same); infinite scroll INSIDE the dropdown; prefetch the next cursor | 4x fewer round trips |
| F4 merge the firms' rows alphabetically | readable Global list |
| F5 filter loaded rows instantly as the user types; 2-character minimum (already defined, unused, `search.ts:246`); cancel superseded requests; stop blanking the list | instant-feeling search |
| F6 cache browse pages by tenant, fingerprint, revision, query and cursor; give resolve a staleTime | no 4.5 s Global re-resolve on window focus |
| F7 (dev only) fix the StrictMode double resolve | fewer parallel cold starts |

**Not recommended:** a shared CloudFront cache of browse pages. The pages are per-user entitlement, and a shared cache
could serve rows after access is revoked. F6's per-session cache is the safe version.

**Expected outcome with B1-B7 and F2-F6:** the first list in roughly **1 s** warm, typing that feels instant on loaded
rows, and each further page at ~0.3-0.5 s (INFERRED, to be measured after the change).

## 3. Pagination: what it is, and what it should be

**Today** (`directory/entry.py:259-289` @`6cd8adb582`; `ClientSearch.tsx` @`10141b6d0b`):
- **Cursor:** base64 `{binding, offset}`, where the binding hashes the principal, firm, directory content hash,
  entitlement revision, scope fingerprint, query and limit.
- **Order:** normalized name, then masked tail, then entry id.
- **Size and count:** 25 per page (server maximum 100); no total count.
- **Cost:** every page re-downloads, re-parses and re-sorts the whole firm, so it is **as slow as page 1**.
- **Layout:** the "Load more clients" button is outside the dropdown; rows are appended in firm blocks; a stale cursor
  after a directory refresh is refused and wipes the list.

**What "fast, not clunky" looks like** (all within the existing authorization model):
1. The server sorts each directory version ONCE (B3/B4). A page is then a slice, so the offset cursor becomes cheap.
   There is no need to change the cursor format.
2. 100 rows per page, infinite scroll inside the dropdown, the next page prefetched as the user nears the end (F3).
3. One alphabetical list across firms for Global (F4), with the firm as a label on each row.
4. Type-ahead filters the loaded rows immediately and asks the server only for what is not loaded (F5).
5. Pages are cached per revision in the browser session (F6). A directory refresh shows "list updated", not an empty
   list.
6. For 49 Financial (4,576 entries), 100 per page is 46 pages. Most users find a client by typing, so fast type-ahead
   matters more than page count.

## 4. What is behind the Analysis tab (deployed, measured)

| Piece | State |
|---|---|
| Routes | 17 declared in `portal/src/api/endpoints/investor-reporting.ts:196-214`: **14 live**, **3 not live** (`POST /analysis/inputs`, `GET /analysis/requests`, `GET /analysis/requests/{id}`). `POST /analysis` -> `irpt-ycharts-generate`; `/analysis/{jobId}/sections` and `/status*` -> `irpt-status` |
| Submit (`irpt-ycharts-generate`) | deployed build = `47f21dab95`'s `entry.py`, **not HEAD**; it sends to the queue, but its role has **no `sqs:SendMessage`** (only Receive/Delete/GetQueueAttributes; the live inline policies and the Terraform-declared policy agree). INFERRED: a real submit is refused at the send. `IRPT_LIVE_YCHARTS_CALL` is absent from its environment. Last run 09-19 |
| Generation queue | `irpt-generation` (+ DLQ): 0 messages ever; **0 of the account's 6 event-source mappings** consume it |
| YCharts session | `ycharts/session/current` holds no session; the `irpt-ycharts-runner` app is not deployed (the SSM run failed rc 127); `ycharts/credentials` (legacy) is live |
| An existing prober | EventBridge `ycharts-session-probe-schedule` is **ENABLED**, `cron(0 */6 * * ? *)` -> Lambda `ycharts-session-probe`: 28 calls in 7 days. It probably keeps the legacy cookie alive (INFERRED). Any always-on design must REPLACE it, never run beside it (the no-shadow rule) |
| Ticker lookup | `securities_info` works with **no session** (2 calls today, both HTTP 200 with no cookie and a junk cookie), so lookups are sessionless and fast (0.07-0.53 s) |
| Report time at YCharts | 26.76 s measured for an Overview (`infra/aws/terraform/investor-reporting/ycharts/generate.tf:199-200`), near the 29 s API and 30 s CloudFront caps, so generation must stay a queued job whatever the host |

## 5. The always-on EC2 question

| Option | Speed | Fragility | Cost/month | Effort |
|---|---|---|---|---|
| A. As designed: Lambda + on-demand runner EC2 (start -> sign in -> stop per refresh) | a boot and a browser capture on every refresh | many moving parts (lease, fence, start, stop, SSM); no single point of failure | ~$0 idle | high: nothing is wired yet (section 4) |
| **B. Keep-warm IRPT + backend/frontend fixes (section 2.3)** | fixes client loading | low | ~$0 | small |
| **C. One dedicated always-on small EC2: owns the YCharts session, consumes `irpt-generation`, NO inbound port; Lambdas keep lookups and listing** | generation starts immediately; eviction is seen on the next call; no browser boot per job | a single point of failure plus patching; Alyssa can still evict it; needs a standing vendor-call word | t3.small ~$19.5, t3.medium ~$35 (on-demand from the AWS Price List API, 2026-09-01; disk and IP estimated) | medium: deploy the runner app, flip its declared STOPPED state (`ycharts/instance.tf:9-25`), wire the consumer, fix submit IAM and entry |
| D. Co-host on `opal-gateway` | same as C | **high**: it holds every user's M365 refresh tokens; 2 GB arm64, single worker; no portal path; breaks the co-tenancy rule in `ycharts/instance.tf:3-7` | ~$0 extra | medium-high |
| E. Provisioned concurrency on the 7 request Lambdas | removes cold starts only | low | ~$49 (ESTIMATE) | small; does nothing for YCharts |

**Recommendation:**
- **B now** for client and account loading.
- **C** for the Analysis/YCharts side. The runner host `irpt-ycharts-runner` (t3.medium, running now) is the natural
  box, and it needs no inbound port because it pulls work from the queue.
- **C replaces A's per-job start/stop, and replaces the separate 6-hourly `ycharts-session-probe`,** under the no-shadow
  rule: one session owner, one prober.
- **Reject D.**
- **Whatever the host, fix section 4's three breaks first.** A faster host in front of a queue nobody reads changes
  nothing.

## 6. Owners (IRPT contract v1.3 section 3)

- COO~P: listing backend (B1-B6), frontend (F1-F7), routes/IaC, the keep-warm hook.
- COO~Y: generation worker and consumer wiring.
- CTO rulings: B3 (the grant-cache doctrine) and F1 (token rotation).
- Security/CloudOps: B8.
- The session host (C): P owns the runtime, per the CTO's 18:39Z routing of the self-heal delta.

## 7. Evidence checks this seat ran itself

- **The listing Lambda config and timings,** read again directly: 512 MB, 15 s, no VPC, 0 layers; provisioned
  concurrency refused because there is no alias or version. The CloudWatch `Duration` metric since 17:46Z gives 77
  samples, average 2,596 ms, max 6,698 ms. That matches the Logs Insights max exactly, with the p50 in the same range.
- **The generate role,** read through the repo's IAM tool (`comp-iam service irpt-ycharts-generate`, the
  Terraform-declared policy): `sqs:DeleteMessage`, `GetQueueAttributes`, `ReceiveMessage` only. That agrees with the
  research pass's live read of the inline policies.
- **Event-source mappings:** 6 in the account; the queues are `37.404`, 3 x `*-served-guard-recheck`,
  `partner-etl-ops-queue` and `opal-globgrph-incremental-events`. None is an IRPT queue.
- **The probe rule:** `ycharts-session-probe-schedule` ENABLED, `cron(0 */6 * * ? *)`, target Lambda
  `ycharts-session-probe`.
- **Keep-warm:** `LAMBDA_BACKED_PREFIXES = ['/advisor-intelligence', '/portfolios']` (`useLambdaKeepWarm.ts:30`).

## 8. What this brief does not claim

- The per-lever effects are estimates, from an offline benchmark on this laptop plus the live timings. They must be
  re-measured after each change.
- Matching Lambda containers to firms (by peak memory) and browser actions to Lambda calls (by timestamps) is
  inferred.
- "A real submit is refused at the send" is inferred from IAM. The generate Lambda logs no application lines, so no
  refusal was observed.
- What `ycharts-session-probe` actually sends to YCharts was not read.
- No browser session was run, so the user-visible timings are reconstructed from server logs, not from a stopwatch.
