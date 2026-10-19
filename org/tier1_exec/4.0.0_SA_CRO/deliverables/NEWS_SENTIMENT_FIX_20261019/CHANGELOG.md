# News Scanner sentiment repair - 4.0.0_SA_CRO~D1CDX

**archetype:** IMPLEMENT
**Status:** IN PROGRESS
**Authority:** Andrew at this terminal, 2026-10-19 (America/New_York).

## Verbatim instruction

> Ok you are in charge of the fix, you have full egress to do what must be done to implement the fix. Please include a testing and validation sequence in your work and rigidly log every change + include rollback solution if needed, start nopw.

This authorizes implementation and egress for this repair. No unrelated work is included.

## Baseline

- Workspace: box/dell1 at 2a4e7e67b13edcb4bb44fac6941d776ad8207b84. Origin/box/dell1 observed 35bd0d37a3740a90480c819cc3ffff07d1e735c3. Push state LOCAL.
- Portal: DEV at d1f9ca29675bd9012284272806afc9c587ef55f0. Origin/DEV observed f70745362d8baa34d78c50b8246a5f98ba7c8862. Push state LOCAL.
- Existing unrelated dirty files are excluded from all pathspecs.
- Live October 19 topic: South Korea Returns to Coal as LNG Crisis, bearish-5, raw FinBERT mean +0.5461; cluster judge bearish because rising coal prices indicate supply issues and energy crisis.
- Nikkei duplicate URL on October 14/15: positive 0.9444, empty summary. Six displayed entries, five distinct URLs.
- Full October 13-19 partition census: 6,046 scored rows; 1,449 empty summaries; 4,597 nonempty summaries, median 138 characters, maximum 500. All 352 Nikkei and 1,080 Seeking Alpha rows empty. No separate body fields.
- Deployed ingestion keeps RSS summary or NewsAPI description, at most 500 characters. Deployed batch sends title + summary; FinBERT confidence becomes a signed number. Nonzero scores bypass GPT gap-fill. Portal independently averages article scores and contradicts the cluster's market direction.

## Intended changes and acceptance

1. Acquire article text with explicit body/excerpt/headline coverage and failure provenance; do not bypass access controls or call an inaccessible page a full body.
2. Preserve raw FinBERT separately. Contextual assessment uses a broad-market perspective, names sector beneficiaries, supports mixed/insufficient outcomes and cites evidence present in its input.
3. Deduplicate canonical URLs before analysis. One URL contributes one vote.
4. Carry topic direction/reason and article assessments through curation, publisher and portal. Group, arrow and modal agree; unavailable assessments are not invented from raw confidence.
5. Keep changes reversible and record exact deployed packages, revisions, data before-images and validation results.

## Testing sequence

- Offline regression cases: coal supply shock, easing costs, recession-led price decline, sector benefit versus broad-market pressure, mixed/insufficient text, duplicate URLs, paywall/blocked extraction, malformed model response, network failure and rollback integrity.
- Live retrieval and model assessment on a bounded representative set, including the exact Nikkei URL and its cluster companions; record coverage and classifications, including failures.
- Python gate, frontend type check/build and rendered component validation against captured payload.
- Before production: snapshot exact code/configuration and affected data; compare pinned changes to deployed baseline.
- Deploy only completed units; read back package hashes and exercise actual outputs. On failed acceptance restore before-images and previous code/configuration within the same session.

## Change journal

1. Established source/live baseline and created this authority, test and change record before implementation. No production mutation yet.

## Rollback design

Persist original Lambda packages/configurations and changed DynamoDB/S3 records under ignored `.runtime/news-sentiment-fix-20261019/backup/`, with a committed hash manifest (no credentials or raw publisher bodies). Code rollback restores original package bytes using revision checks. Data rollback restores only fields/objects changed by this repair after verifying they still match our after-image; refuse to overwrite a subsequent writer. Portal rollback is the inverse of the exact repair commit through the existing release mechanism. Do not rely solely on expiring S3 versions.
