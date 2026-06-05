# work-cycle 0018 — donut PROD close (CF-flush v2.1.115) + producer blend-split revert to granular (Andrew FE-side ruling)

**archetype:** DEPLOY (CF-flush) **secondary:** REVERT, VALIDATE, COORDINATE
**Date:** 2026-06-05 ~2012-2026Z
**Trigger:** Andrew FE-side blend ruling (DE 86f7e8da); DT v2.1.115 PROD promote GO (CF-flush); COO URGENT S3-correction (crossed)

## A. Producer blend-split REVERTED to granular (Andrew "not the producer")
Andrew chose FE-side blend rollup (DE shipped portal DEV 86f7e8da: VALUE 50/50-split, COUNT full-to-each archetype). DS's producer-side blend-split (c61a45a05 + comment-fix be788e8d4) became redundant. My S3 deploy of those (370ff9d8) had crossed DE's HOLD.
REVERTED s3 runner copy to granular pre-blend-split: sha 3c31f8ea (0 _BLEND_GLOBAL_SPLIT), byte-identical to repo c61a45a05^. Verified the pre-blend bytes 3 ways (saved deployed copy == repo c61^ == post-revert pull). Honors Andrew literal "on the frontend, not the producer" + keeps artifact granular for analysis (DE preference).
COO git-reverted repo too (4386bdc2d, DS serial) -> repo HEAD == deploy == 3c31f8ea. FULL COHERENCE: repo==deploy==granular. COO's later URGENT (re-deploy correction) was reading my pre-revert ACK; re-verified live S3 already 3c31f8ea -> no action needed (replied with before/after SHA).

## B. Donut/aum-metrics PROD close — CF-flush DONE
DT shipped portal v2.1.115 to PROD (merge 131d081d, tag portal-v2.1.115; deploy.yml run 27038063420 SUCCESS): carries 62767be0 (Global Count union 7095) + 253045ec (Global VALUE MDPF re-point $1.808B) + 86f7e8da (50/50 blend FE-roll). CI invalidated FE assets (ICQPUZFLF2I8JDTXVKQIGDJT0J).
Fired the DATA-API flush CI doesn't cover (PowerShell per leading-slash/MSYS banked note):
  dist EVTSA9VEHNZVH, paths /api/general/portfolios/* + /api/general/mdpf/*
  invalidation I28A6LWFSQID3J22I48YVNMD3X = COMPLETED.
Origin artifacts re-verified ($1.808B donut identity exact; account-distribution 7,301/$1.492B; aggregate-aua granular). Edge now == fresh origin. DT co-verifying rendered PROD -> RAVC2 COO.

## Root-cause recap (cyc0017): donut $1.71B
Global Total AUA is FE-computed = modelAUM (aum-metrics by_model, Inflection PRESENT) + non_model_assets.non_model_aum. PROD served an Inflection-blind non_model_assets.json (~$218M) -> $1.71B. Fix = fresh non_model_assets.json (non_model $315.8M incl inflection $90.9M) -> $1.808B. NOT a model-side producer drop.

## Lessons reinforced
- A "comment-only re-deploy" can silently carry logic: be788e8d4 was a comment fix ATOP c61a45a05 (blend-split) -> deploying it = blend logic + comment. Always diff against the intended-baseline, not assume "comment = harmless."
- Cross-message races under multi-agent load: my deploy crossed DE's HOLD; COO's URGENT read my pre-revert ACK. Resolution = re-verify LIVE state (not memory/ACK), report before/after SHA. Pairs feedback_verify_against_served_artifact_not_partial_proxy.

## Compiler tools
sha256 byte-verify (x5, deployed-vs-repo-vs-c61^), git show <commit>:path baseline extract, git pull/merge-base, aws s3 cp deploy+revert, cloudfront create-invalidation + get-invalidation (PowerShell, Completed-confirm).
