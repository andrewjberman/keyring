# TREE HYGIENE — untracked-file census + disposition (Andrew-direct, 2026-07-29 ~13:0xZ)

**Author:** 3.0.0_SA_CVO · **archetype:** SCRIBE
**Trigger:** Andrew at my terminal: *"are there 61 dirty files on the tree? ... I would like to take
this quiet moment to clean up our tree."* Measured: 160 dirty entries (1 = portal submodule pointer,
159 collapsed untracked = **209 real files** via `-uall`). After my authorized deletions: **144.**

## DELETED (Andrew-authorized, this session — junk/scratch with no owner value)

Root: `` `0`] `` (0-byte botched-redirect artifact) · `nm_check.json` · `cot_ma.parquet` ·
`cot_hold.parquet` · `.runtmp_deployed_dim.py`. Plus `org/mcp/liveness.json.corrupt` (07-06),
`.tools/hooks/_bench_{old,new}.sh`, 6 `deck_generation/prompts/_preview_test_*.deck.md` +
`prompts/_test/` (3 test decks) + `deck_generation/.qa_tmp/` (QA pptx/png renders). Also the stray
`C:\cygdrive\` tree from this morning's shim path-mangle (4 scratch JSONs).

## HELD — recent, P0-adjacent; deliberately NOT touched (owner disposes post-MDPF)

| item | why held | owner |
|---|---|---|
| `.mdpf_restore/` (07-28: DDB day snapshots, per-scope chk_*.json) | MDPF P0 restore point; live until D1-D4 certify | AE/COO |
| `.fedobs_tmp/` (07-28: fstab-fix note + live-aws derive JSONs) | active fedobs/site-Z work residue | MSTR |
| `.runtmp_rm.py` (07-28: byte-preserving EC2_MANIFEST github-actions-runner removal) | recent surgical tool; its own docstring records a mojibake incident | AE |
| `comp/` (COMP_LEARNS bench: judges, httpx target, ab_cache — NOT junk) | live program tree; commit-or-gitignore is its owner's call | COO (COMP_LEARNS) |

## COMMIT-CLASS — records that belong in git, each to its OWNER's author line (sweep hazard: I commit none of these)

1. **`org/critical_paths/change_management/` — 24 files** (23 surface-check approval receipts
   07-23→today + 1 deploy-completion ledger 07-24) + `org/critical_paths/.open_findings/` — 2 fresh
   MDPF closeout-drift JSONs (05:30Z today). → **COO** (ledger hygiene, WO-0 class).
2. **Live machinery, untracked since April:** `.tools/check-inbox`, `.tools/inbox-watch`,
   `.tools/cl-*`, `.tools/prd-delta.py` + `prd-delta-report.py` (the `/prd-delta` SKILL is also
   untracked at `.claude/skills/prd-delta/`), `.tools/frontend-dev`, misc. **This is the untracked-
   oracle class MSTR named on my audit-log finding, and it overlaps MSTR~Z's ACTIVE portability
   census (19-referenced-by-live-machinery floor @b9acb07c7a)** → route through that census, do not
   ad-hoc commit around it. → **CTO/MSTR~Z.**
3. **`infra/aws/ec2/canonical-schwab-si2/` — 14-file SDD tooling suite** (07-10→12) → **0.6.2 AE**
   (EC2 code standard says these belong in the repo→S3 path). `requirements.txt` (auto-generated
   estate inventory 07-10) → **CTO** (commit or regen-on-demand).
   ⚠ `infra/aws/terraform/shared-infra/infrastructure-alerts-durable-limb.tf.proposed` (07-09):
   **recommend DELETE — it proposes alert machinery predating the 07-28 moratorium.** → CTO ruling.
4. **Agent-lane residue** (each owner commits or deletes their own): CTO session logs 06-26/07-13 +
   NFRA_MSBEFF `nl_structured/` chunks (~2.5MB) + NFRA_COMPCLOSE report · DT `posn_bmkviz_qa/` PNGs ·
   DS drafts/scripts/motif-prep + `data/inf/.../tests/__init__.py` · AE 0.5.0/0.6.x/0.7.0/0.8.0 logs,
   drafts, TOs, SES case draft · `org/tier1_exec/2.1.0_SA_COO/` TO (nonstandard serial dir — COO to
   adopt or fold) · `org/modules/` compproof solver views + heatmap `ms_heat_index.json` (3MB) +
   debtscan motifs · `infra/aws/globgrph/` launcher/ledger/fallback bits · `org/threads/handoff/` ·
   deck_generation real decks + `data/find/dualbiz` GA-targets analysis (06-26; Andrew's call:
   commit as record or archive).

## The structural note (one line, for the RETIRECOND/D8 queue, not machinery)

24 of the 209 were **gate-emitted records** (approval receipts, ledgers, findings) that no gate
requires to be committed — a receipt that only exists on one machine's disk is one `git clean` away
from never having existed. Same class as the gitignored audit log. Pricing belongs to CTO/COO.

— 3.0.0_SA_CVO
