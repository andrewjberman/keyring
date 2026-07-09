# FILED (post-NFRA fixes / NFRA-adjacent sweep) -- CLASS: region-mismatched dead grant + fail-silent reader

**STATUS:** CLASS identified 2026-07-09 (WRITE-root behaviour-exercise + CVO grounding). The SWEEP (detect all instances) is NFRA-adjacent -> freshness-integrity program (CTO+CVO). The per-instance FIXES are post-NFRA (non-NFRA feature planes; NFRA-first holds). Owner-assign per instance when the NFRA wave clears.
**Andrew:** CTO flags the class (market-update SEV2 anchor + siblings). Frame as a CLASS, not isolated incidents.

## The mechanism
An IAM grant scoped to the WRONG REGION (secret/log in us-east-2, but the lambda + the actual secret are us-east-1) is DEAD -- the read implicitDenies. If the consumer FAILS SILENT on that denial (returns mock/empty/404 instead of erroring), the degrade is invisible. Cousin classes: [[feedback_fail_silent_fabricate_on_dependency_denial]] (producer fabricates) + [[feedback_freshness_monitor_mtime_proxy_content_blind]] (monitor content-blind). The region-mismatch is the trigger; the fail-silent is the amplifier.

## Instances found (3, touching a SUBSET of roles -> sweep for more)
1. **market-update-data-aggregator** -- SEV2 latent (fabricate-on-exception: INVENTED CPI/FOMC at HTTP 200). Warning log also dead (us-east-2 logs grant) = invisible-by-construction. See [[FILED_market_update_feature_dark_postNFRA]]. CTO Andrew-flags.
2. **daily-agenda-generator** (news-ingestion-lambda-role) -- **LIVE**: agenda built WITHOUT private-repo data. github-token/newsapi/openai grants in us-east-2; zero secrets there; lambda us-east-1. AccessDenied -> GitHub 404 -> private repo invisible. Ran 10h ago; CVO live-confirmed (simulate implicitDeny). FIX = repoint SecretsManagerAccess grant to us-east-1. Same class as inf $1.44M AUA. **Owner: news/agenda-plane (assign post-NFRA).**
3. **yang-generate-volatility** -- LATENT (empty VIX on denial, but last ran 175d ago = not a live break). Stated precisely, not conflated.

## The SWEEP (freshness-integrity program, NFRA-adjacent -- routed CTO+CVO 110417Z)
Prove-the-universe: simulate secret-reads (+ logs:PutLogEvents region) across ALL roles -> flag region-mismatched / dead grants; cross-ref the fail-silent-reader census (0.5.0: 9/15 readers fail silent). Find every LIVE fail-silent data-integrity degrade, not the 3 stumbled on. daily-agenda = canonical reference instance.

## The RULE (freshness-integrity program, per CVO)
element-1 non-empty + fail-loud-not-silent: a reader on a dependency-failure must ERROR, never mock/empty/404-swallow. A grant must be region-correct (or the reader must fail loud when it's dead).
