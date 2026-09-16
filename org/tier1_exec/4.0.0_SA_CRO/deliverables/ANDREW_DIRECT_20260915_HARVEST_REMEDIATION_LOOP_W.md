# Andrew direct: local harvest remediation and cadence hold

Seat: `4.0.0_SA_CRO~W`. Scope: AMGT_RESAPP / D5. Recorded 2026-09-15.

## Verbatim instruction

> Ok set a loop for yourself to remediate all these issues including validating Barron's end to end, then once they are completely done and validated and you are ready to set the loop, ping me, and we will decide the mechanism of how the data is pulled. I suspect it is A.) Too aggressive to pull 5+ articles from every single ticker from every single platform every single day, which means we will have to slowly and steadily build up the backfill over some amount of cycles. B.) Once we have a solid backfill then we need to figure out how to make sure we are not pulling the same articles multiple times, which means that articles have to be keyed on some kind of stable key so we dont keep pulling the same ones.

## Execution boundary

Remediate and run bounded local validation, including independent Barron's
verification recovery. Do not enable recurring collection or select a broad
backfill cadence. Andrew decides the collection mechanism and pace after the
validation report. A successful human-assisted captcha remains human-assisted.

Use one canonical body per publisher/article identity and separate security
associations. Skip known bodies before article requests where the publisher's
listing contract permits. Keep uploads idempotent with a durable outbox and
readback validation. Scheduled entrypoint remains disabled after a bounded
one-shot test. Five articles is a validation target, not a daily production quota.

POSN requests are outside this seat's current user-assigned responsibility.
