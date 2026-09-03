# Session log -- NFRA_CLDGRPH CG-s-4 serving plane

**Seat:** `0.7.0_AE_CloudOps~T`  
**Task:** `NFRA_CLDGRPH.TO-CG-C-1` / cell `CG-s-4`  
**State at this entry:** complete; deployed and exercised through C1-AC6, with the final proof VALID and the task status flipped for the exact-path co-commit.

## Work record

- Loaded the exact seat and executed the repository-local startup sequence. Read the committed C1 face at issuer commit `68d7f16a6c51851d81a85d71dc3fd9899a10a83b`.
- Before writing, ran the mandated `comp-read` on `nessie.tf` and `projection_worker.py`, then `comp-find --corpus aws 'opal-globgrph'`.
- Implemented the pointer-only service, seven focused tests, the COPY-only image entrypoint, and seven Terraform resources. Committed the first artifact as `8f0dff109f940f295ce707146c33a1e0b4be0930` with exact ~T authorship. ~S independently confirmed the four-path diff, seven tests, and Terraform validation.
- Measured the live 47,964,160-byte artifact in a real Kuzu 0.11.3 read-only open: baseline RSS 52,957,184 B; open RSS 138,268,672 B; query/peak RSS 143,536,128 B; count result 27,225. Chose 512 CPU / 1,024 MiB.
- Opened NEVER-2 ledger `cldgrph-cgs4-serving-plane` before the first plan. Targeted plan: 7 add / 0 change / 0 destroy. Built CodeBuild image `72336fae-740c-491b-a962-e44bc76bd925`; ECR digest `sha256:68c822ff9cc4784f6fa8eb83fcde513f6ef1a1659f0220f44a2b78c9fcbd12b5`. Safe-apply: 7 added / 0 changed / 0 destroyed.
- Ran the one explicit unscoped re-plan. Saved-plan JSON asserted exactly the three Glue partition items plus the excluded email SNS subscription, with no C1 address.
- Refreshed the applied IAM census at 18:43:46Z. The census and direct IAM read show one inline policy, no attached policies, and exactly V-2(ii). Live SG `sg-0e85dd853fbe5584e` admits TCP 8181 from `172.31.0.0/16` only.
- ECS task `c18ee8b40e4a4bf3993f8f78cc2f98a6` reached HEALTHY on the image digest above. Gateway SSM command `2e708112-9eec-44ef-9e65-4eeded137343` resolved `projection.opal-globgrph.local` to `172.31.9.108`; the count query returned 27,225 rows-count, the pointer-equal `17:01:08.128628Z` vintage and all disclosure fields in 0.026205 s. Health returned in 0.002202 s.
- Reran the planted backward pointer through the local watcher seam: `REFUSED=backward pointer refused...`, zero loader calls, served vintage unchanged. No S3 write occurred.
- COO Msg 93888 accepted progress through AC4. Msg 93889 ruled that C2's deployed revision-3 writer supplies the authentic forward advance; this seat waits without writing a marker/pointer and without touching B2/C2.
- AC6 handoffs are written. Pre-final push measurement: local HEAD `83df35d75f2a3da00f53062c09281dd1543ce396`, origin/CLOUD `351f309e0a6ded1a5a5bdf3aacec18a5f9f8dbee`, local-is-ancestor rc 1. This seat does not push.
- C2 writer task `f8b288ad95ec42dab2d17ef5a33cbd29` authentically advanced the pointer from `2026-09-03T17:01:08.128628+00:00` to `2026-09-03T19:02:18.412096+00:00`, manifest `751b870534c474298e0e968390f143e325b4741a4a4fc471c3bf341cd39c0b58`, after verifying 27,225 nodes and 58,606 edges.
- The C1 watcher swapped in process. Gateway SSM command `62213ecc-b319-4d23-b91b-37e765b0f2fc` returned HTTP 200, 27,225 and the new vintage in 0.003664 s; health returned `last_swap=2026-09-03T19:03:42.191303+00:00` in 0.002624 s. Task ARN `c18ee8b40e4a4bf3993f8f78cc2f98a6`, `startedAt=1788460967.358`, task definition and image digest did not change.
- Reran the backward seam after that real advance: the backward pointer was refused, `LOADER_CALLS=0`, and the served vintage was unchanged. Closed L5 and then closed all five legs of NEVER-2 ledger `cldgrph-cgs4-serving-plane`.
- Final pre-validation push measurement: local HEAD `86b4ecc2656c3bb0319e777b230c82f9b68802fe`, origin/CLOUD `351f309e0a6ded1a5a5bdf3aacec18a5f9f8dbee`, local-is-ancestor rc 1. No push.

## Close sequence

Finalized the result/proof/log after the authentic swap. Seven tests and the
two-file commit gate passed; the checker reported six acceptance rows, zero
violations and `VALID`; then the task face was flipped. This log, the face,
result, proof and closed ledger ride one exact-path co-commit. After it, origin
is measured again and every criterion is reported to the COO. No push.
