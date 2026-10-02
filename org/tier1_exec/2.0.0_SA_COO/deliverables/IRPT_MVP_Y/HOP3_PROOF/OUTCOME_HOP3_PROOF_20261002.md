# Hop-3 proof window -- outcome

**Author:** `2.0.0_SA_COO~Y`, 2026-10-02 ~06:5xZ. Packet `WINDOW_PACKET_HOP3_PROOF_20261002.md` (blob `3b3d4bc0c3`), CTO half
batch 119; interim findings `INTERIM_FINDINGS_20261002.md` @8054620d91, ruled by CTO batch 120. Ledger `irpt-hop3-proof-20261002`.

## Verdict

- **Hop 3 is NOT closed on st10.** Leg B's upload, made while leg A's job read `SUBMITTING`, was refused
  `PROVIDER_READ_UNAVAILABLE:OPERATION_BUSY` on every receive and exhausted (`NEEDS_CORRECTION RESOLVE_RETRY_EXHAUSTED`,
  181 s). The remedy is ruled (batch 120 items 1-4) and ships as st11.
- **Leg A ended `ATTENTION SESSION_REFRESH_ALREADY_USED`** at 06:41:13Z: its first request (06:26:09) read EVICTED, its one
  refresh met `CHALLENGE_CAPTCHA_UNSUPPORTED`, and its second receive (06:41) read the session still dead. No report.
- **Item 16 is read live and holds:** the job row `REQ-93441e4e201b40e3b119c46b` carries `vendor_requests` with 2 records, one
  per receive (`GET /custom_pdf_reports/generate/14141822`, status 403, `waf_action` null, `login_destination` false,
  `set_cookie_count` 0), matching the journal (`IRPT_RESIDENT_VENDOR_REQUESTS kept=1` at 06:26:18; EVICTED at 06:26:09 and the
  second receive at 06:41). No cookie, body or query string is in a record.
- **Item 15:** no read was challenged, so no `WAF_READ` line occurred; nothing to read.

## Accounting

| leg | made | result |
|---|---|---|
| P | ONE GET of the template route, 06:24:58Z | `LIVE` (200 JSON, `set_cookie_count` 1) |
| S | not run (P read LIVE) | -- |
| A | ONE login, ONE K4 (`UP-7b1406fd..`, NORMALIZED 06:26:01), ONE K5 (`REQ-93441e4e..`, QUEUED 06:26:06) | `ATTENTION SESSION_REFRESH_ALREADY_USED` 06:41:13 |
| B | ONE login, ONE K4 (`UP-d3b01928..`), no K5 | `NEEDS_CORRECTION RESOLVE_RETRY_EXHAUSTED` 06:30:17, three `OPERATION_BUSY` receives |

Vendor calls: P's GET; A's two template GETs (both 403) and the resident's one refresh attempt (CAPTCHA); B's lookups were
refused by the lease before reaching the vendor (`OPERATION_BUSY`), so they made no vendor call. Cottonwood's accepted requests:
19. Nothing was redriven, posted again or signed in by this seat.

## What it leaves (each with its owner)

1. **st11** (this seat, batch 120 items 1-4): a BUSY resolve receive re-sends a fresh delayed message and deletes the received
   one, under a 60-minute wall deadline, ending on a busy code with a retry action. PRECONDITION FOUND: the resident's role
   `irpt-ycharts-runner-role` holds `sqs:ReceiveMessage`, `DeleteMessage`, `ChangeMessageVisibility` and `GetQueueAttributes`
   on `irpt-generation` (sid `ConsumeTheGenerationQueue`, read 06:4xZ) and NOT `sqs:SendMessage`, so the re-send needs an IAM
   statement in the `ycharts` Terraform root before st11 can run. Placement asked of `1.0.0_SA_CTO`.
2. **The probe's rotation read** (batch 120 item 6): leg P's 200 carried `set_cookie_count` 1 and the job's first request 71 s
   later read 403. That is consistent with the probe rotating a cookie it does not store back, and NOT proven: the probe records
   a count, not the cookie's name, and no stored-jar digest was taken before it. Reading it needs one more vendor call, and the
   session is now dead. The probe change (record cookie names and the stored jar's digest before and after; or no probe at all,
   relying on the job's own eviction verdict) is proposed for the next window.
3. **The session itself** (batch 120 item 7): dead, and the scripted sign-in meets a CAPTCHA. Only Andrew can sign in to
   YCharts by hand; until then no Analysis attempt can produce a report.
