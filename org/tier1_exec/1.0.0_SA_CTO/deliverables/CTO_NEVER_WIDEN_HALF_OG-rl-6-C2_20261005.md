# CTO never-widen half -- OG-rl-6 C2 (r17c: /yearinreview OWNER-ONLY on live e91819e281)

**By:** 1.0.0_SA_CTO~O, 2026-10-05 ~14:0xZ.
**Against:**
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-6-C2_20261005.md` @f6fdd4047b (ask msg
29581). Release HEAD `37be3485db` on branch `rel-nfra-oplgtw-r17c`.
- **Spec:** R15 (round-16 analysis section 7, @16f729348e).
- **Andrew-direct:** "Visible to me only" (record @121b7b016e).
- **Supersedes:** my half on `14e0af86fa` (@0fba676f84), which lapsed on that word as it stated.

**VERDICT: SIGNED, no condition.** The act may touch the keys in the ask's section 2 and the manifest, including the
ONE added `.env` key. The rollback is `/c/tmp/og-rb12` at `e91819e281`.

## My reads, independent of the worker and the issuer (~14:0xZ, git only, no host reads)

1. **Ancestry and census.** `git merge-base --is-ancestor e91819e281 37be3485db` is yes. `git diff --stat` lists 6 files:
   - `config.py` (+8);
   - `server.py` (+5/-2);
   - `yearinreview_view.py` (new);
   - `static/yearinreview/index.html` (new);
   - `deploy-to-ec2.sh` (+2/-1);
   - `tests/test_yearinreview_view.py`.
2. **Equal where it should be.** `server.py` and the page are byte-equal to r17b `14e0af86fa`, whose server diff I read
   line by line for @0fba676f84. The delta from r17b is config, the view's gate, the template line and the tests.
3. **The template.** Parsed in Python from both revisions, the `.env` printf goes from 50 to 51 key names.
   - Added: exactly `YEARINREVIEW_VIEW_ALLOWED_EMAILS`. Removed: none.
   - With `YEARINREVIEW_VIEW_ALLOWED_EMAILS=andrew@opalinvest.com\n` removed once, the line is identical to live's.
   - No secret value is added.
4. **The gate, the producer's own rule (R15).**
   - `_allowed` is `bool(roster) and email in roster`, so an empty or missing roster admits nobody.
   - `config.py` parses the key like `/sprint`'s (lowercased, comma-split), as its own key.
   - The handler order is identity (401), then roster (403, audited `DENIED`/`roster`), then the page.
   - The GuardMiddleware branch is still `/sprint`'s, which is verified-header, blocklist, email-deny and fail-closed.
   - Every branch of property (a) refuses, except the owner.
