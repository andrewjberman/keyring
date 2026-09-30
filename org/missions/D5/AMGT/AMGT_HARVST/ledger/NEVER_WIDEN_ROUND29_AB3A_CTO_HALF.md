# NEVER-WIDEN -- CTO HALF -- AMGT_HARVST round 29, `HVST-ab-3` PHASE A (backfill batch 1: 10 names x {bbg, wsj, sa} + Lenovo x {barrons, ft}) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~16:2xZ

**Against:** `deliverables/2.0.0_SA_COO_H/round29/NEVER_WIDEN_HALF_COO_AB3.md` @`6b3b243c4e` (msg 27255, READ-acked; read to EOF, 6,619 B).
**Authority:**
- R-21 @`b390c36444`, scripted;
- Andrew-direct @`e1b5fd6d8c`: credentials in AWS Secrets, trust tokens first, crawl last, rate limit is not expiry, backoff
  (PRD v0.9 `C-HV-TRUST-TOKEN`);
- his quota word, handled by measuring first (round-28 ruling 3);
- the Seeking Alpha correction @`7db0a2f4d3`.

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT

- **Before-state, re-listed on S3:** bbg 1,007, wsj 84, sa 106, barrons 30, ft 28, `run_record` 2, `chatter_daily` 10,
  `article_security_mention` 8. This equals the COO half on all 8 roots.
- **Code pin:** `git diff --stat ffe564672b HEAD -- lib/opal_data_harvest lib/research/harvest` is empty.
- **The half meets every standing requirement:**
  - it names each command that reaches a put (12 run records, one upload);
  - it reads the config defaults, including the throttle bounds;
  - it cites stub evidence;
  - it names each publisher's token source (the CVO's build note);
  - it covers both branches per job;
  - it runs a pre-run print (800 pages, basis DEFAULT on 32 of 32).
  This batch IS the measurement that re-bases that DEFAULT.

## 2. CONDITIONS

1. **The act-start gate** (`ab-3.before.py`) prints `ACT-START GATE: OK`, and the pin diff is empty, or STOP.
2. **The sa probe runs FIRST and alone.** A 402 that persists after the one in-job fresh sign-in is a FINDING. Its kept body is read
   before anything is asked of Andrew, and sa leaves steps 2-3.
3. **A sign-in that meets an MFA prompt or an interactive challenge STOPS that publisher's leg.**
   - No retry, and no second sign-in.
   - The challenge is recorded with its class. A code or approval is Andrew's act (his login), never guessed or bypassed.
   - This applies to every automated sign-in the trust-token rule permits (bbg's Google credentials included).
4. **A 429 is a rate limit, never expiry** (his word): back off within the configured bound, keep the token, and end the job
   `throttled`. A throttled job is not a refusal.
5. **The outbox guard:** a pending count above 5,000 before the upload is a STOP (the half's own limb).
6. **After the act:**
   - 12 run records;
   - no write to `chatter_daily` or `article_security_mention`;
   - AC2 prints the MEASURED pages per publisher, the re-based ceiling, and the names REACHED. That is phase B's input and batch
     2's basis.

## 3. ROLLBACK

The COO half stands: forward only, never-overwrite. A delete is Andrew's act.

## 4. NOT COVERED

- phase B (the schedule), which is signed separately after the after-reads;
- batch 2;
- any gold rebuild;
- any other security.
