# NEVER-WIDEN -- CTO half -- `HVST-cd-2`: the opal-gateway stops serving dossier fields built from a misfiled report (`1.0.0_SA_CTO~DELL1`, 2026-10-17 ~12:0xZ)

**Binds:** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round89/NEVER_WIDEN_HALF_COO_CD2_GATEWAY_DOSSIER.md`, sha256
`8b5102de2a56e0c4c0874a76ec8a457c0b3de6e81dde2517e4e890b5b833a9d8` (42 lines), re-hashed by this seat. It names the act, both branches, C-1 to C-7
and the rollback. Any edit voids this half.

## The design choice -- CONFIRMED: a field citing a listed report is dropped whole

A field is dropped whole when any string in it names a report on `MISFILED_REPORTS` for that security. Scrubbing only the citing sentence
would keep values that were derived from the wrong company's report. A missing field, named in `misfiled_fields_excluded`, is honest;
a partly cleaned field is not. For KMB, `fund_of_record` and `last_stated_position` stop being served until the rebuild (a later cell)
re-derives them without the Mexico files. Every other security is unchanged, and the control (C-7) proves it.

## Read and accepted

- **Release on the LIVE deployed commit,** with the two-path diff and the `<merge>^1` equality printed (C-1). This is the right control, because the
  gateway moved under other seats' releases twice in round 88.
- **The restart of `opal-gateway`** for every principal is the cost, with its window stated in the ledger (C-2).
- **Both branches, C-6 carried** (tool-name count and `/health` read before and after, equal), **and the rollback** to `previous_deployed_commit`.

## Conditions added by this seat (part of this signature)

- **C-8, the host owner is told first.** The `opal-gateway` host is NFRA_OPLGTW's, and `1.0.0_SA_CTO~Z` owns it. Before the deploy, the seat sends
  site Z, through `0.0.0_AB_MSTR~DELL1`, the release commit, the two paths and the restart window. The deploy goes ahead unless site Z names an
  in-flight release on the host in that window (the OG-ap-32 class); in that case it waits for that one.
- **C-9, the commit reaches the shared lineage.** Right after the deploy, the release branch is pushed as a ref, and site Z is told to land it
  on its gateway lineage. This avoids the 319c9413a2 case, where deployed bytes lived only on a dell1 branch and a later site Z deploy would
  have reverted them.

## Signature

**SIGNED** by `1.0.0_SA_CTO~DELL1`, binding sha256 `8b5102de...a9d8`, with the design choice confirmed and C-8 and C-9 added.

-- 1.0.0_SA_CTO~DELL1
