# ANDREW-DIRECT 2026-10-05 ~20:4xZ -- full PROD deploy now; identify why it failed so we never half-send again

- **Channel:** the site-Z terminal of `2.0.0_SA_COO~D` (session 6c9ea2f7-a212-40bf-aefa-ce51b8750285), typed by Andrew.
- **Context:** `/prod-deploy` pushed portal PROD `c69b4747 -> ce6f0721` (v2.1.200, record @166eada4b9). Its "Deploy to Production" run
  37368605578 failed before any step ran: "The job was not acquired by Runner of type hosted even after multiple attempts". Build
  Production Assets was queued 20:15:29-20:30:31Z and then cancelled; Deploy to S3 + CloudFront and Tag were skipped. The PROD branch moved;
  the served site did not (half-landed, NEVER-2). This seat re-ran the run (attempt 2) and told the CTO and MSTR~Z (msgs 29782, 29783).
- **Recorded by:** `2.0.0_SA_COO~D`, same turn.

## Verbatim

"that has never happened before to my knowledge. first of all we need full prod deploy issued now, but we need to identify why it failed
so that we dont half send again"

## What it sets

1. **Now:** the full PROD deploy of `ce6f0721`, carried through to `conclusion: success`, the served site and the peeled tag.
2. **Then:** the root cause of the runner failure, and a way the promote stops half-sending (the branch moving while the site does not).
   The cause is measured, not inferred, and lands as a record.
