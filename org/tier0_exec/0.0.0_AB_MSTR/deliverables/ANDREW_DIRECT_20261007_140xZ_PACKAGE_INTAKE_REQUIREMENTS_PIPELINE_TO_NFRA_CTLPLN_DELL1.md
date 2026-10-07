# ANDREW-DIRECT 2026-10-07 ~14:0xZ at the 0.0.0_AB_MSTR~DELL1 terminal -- package intake: requirements.txt as the approved list, a request pipeline and review, folded into NFRA_CTLPLN

**Recorder:** 0.0.0_AB_MSTR~DELL1. **For:** laptop 1.0.0_SA_CTO (placement, PRD), laptop 4.0.0_SA_CRO (L1), laptop 2.0.0_SA_COO~C (C-KIT owner, NFRA_CTLPLN).

## Andrew's words, verbatim

At this terminal, ~14:0xZ, after the recommendation in section 3:

> "Ok i like this policy, particularly the framework around approved packages being included on requirements.txt. I think there should be some kind of request pipeline for additions to requirements.txt and a review process. I would issue all of this information to the laptop, as it is all work that should be researched, designed, and folded in to NFRA_CTLPLN"

Earlier the same day, at this terminal, ~13:5xZ:

> "Check in with MSTR~DELL2, I do not mind webbrowsing if necessary for research purposes, however we do not do downloads. They have the details on the matter."

And at the dell2 terminal to 4.0.0_SA_CRO~DELL2, ~13:39Z (record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261007_133xZ_DOWNLOAD_RISK_TIERS_RED_SCRIPTS_YELLOW_PACKAGES_LAPTOP_VETS_TAILDROP.md` @50df0c2e97, on `q/dell2/record-download-tiers/r1`), as relayed verbatim by 0.0.0_AB_MSTR~DELL2:

> "High risk downloads include any kind of script/executable (unless it is from a tailnet device, sent over taildrop or via git), these are red and should never, ever be downloaded off the raw internet. Libraries/packages are yellow, I don't really want any npm/npx packages. Python libraries are also yellow. What is preferable is if there is a true dependency, a library that is absolutely needed, it is preferable for the laptop device to check it out first, and if clean and clear, it can be taildropped."

and (@e031cd6991): "Websearch is fine, but downloading needs to be gated".

## 1. What he asked for

The package-intake policy below is to be **researched, designed and folded into NFRA_CTLPLN**, including:

- `requirements.txt` as the **approved list**: a package at an exact version is installable on a box only if it is listed there.
- A **request pipeline** for additions and version changes to `requirements.txt`.
- A **review process** for those requests.

This record carries the word and the analysis; it decides no design. Design is the laptop CTO's (L2-L4), the brief the CRO's (L1).

## 2. The evidence from today (2026-10-07)

| Box | Event | Kind | Record |
| --- | --- | --- | --- |
| dell1 | 2.0.0_SA_COO~M1's provisioning ran `wk-provision.sh --node-modules install` -> `bun install`, ~487 npm packages fetched (~08:07Z) | npm via bun | row MDPF_SECCLASS-S54 |
| dell1 | worker 0.9.0_WK_MDPF_SECCLASS~26 `pip install ruff==0.15.11` from PyPI to pass the commit gate (~08:42Z) | PyPI | row MDPF_SECCLASS-S49 |
| dell2 | 4.0.0_SA_CRO~DELL2 scratch render outside portal/ -> bun auto-installed react + react-dom (~08:08 local) | npm via bun | `CRO_FINDING_BUN_AUTO_INSTALL_EGRESS_DELL2_20261007.md` @fd0c709235 |
| dell2 | a disarm probe's bare `import "left-pad"` fetched left-pad (~08:12 local) | npm via bun | relayed by 0.0.0_AB_MSTR~DELL2 |

The friction the other way: dell1's ruff was 0.16.10 against the gate's 0.15.11 pin, refusing every existing `.py` edit until the laptop Taildropped 0.15.11; `pandas_market_calendars` is absent on both Dells (the trading-calendar fallback incident). Neither is in `requirements.txt`.

## 3. The analysis put to Andrew (as given, for the brief)

**Python is not malware-free.** Lower volume than npm, but real: PyTorch nightly pulled a malicious `torchtriton` by dependency confusion (Dec 2022); `ultralytics` shipped a crypto miner after a release-pipeline compromise (Dec 2024); PyPI routinely purges typosquat batches and has paused new sign-ups to stop campaigns.

**Why it matters more on these boxes.** Each Dell holds an AWS identity that writes `opal-*` S3 and updates Lambda code, reads firm data, and holds a git token. An install runs the package's code with all of that.

**The agent-specific risk.** Agents sometimes produce plausible package names that do not exist; attackers pre-register such names ("slopsquatting"). An agent `pip install`-ing a name it guessed is the realistic way in.

**The frequent cost is drift, not malware.** Today's two real breakages were version mismatches (ruff 0.16 vs the 0.15 pin; per dell1's handoff, mcp 2.x broke `org/mcp/server.py`).

**Recommendation as accepted:**
1. A package may be installed only if it appears in `requirements.txt` at an exact version (blocks typosquats and invented names).
2. Wheels only (`--only-binary :all:`) so no setup script runs at install.
3. Adding or changing an entry is a reviewed commit to `requirements.txt`, ideally with hashes (`--require-hashes`).
4. npm / npx / bun package fetching stays blocked (his "I don't really want any npm/npx packages").
5. Delivery per his dell2 word: the laptop fetches and checks, then Taildrops to the Dells; the kit verifies each delivered package against the recorded hash. Only one box touches PyPI.

## 4. Questions for the design (open, not decided here)

- Who files a request, where (a carrier file, not a broker message), and what it must carry (package, exact version, why no stdlib or existing package will do -- the build ladder, the importing file).
- Who reviews, against what checklist (maintainer and release history, typosquat distance to popular names, wheels available for cp314 win_amd64, transitive dependencies, licence).
- Hash pinning: one `requirements.txt` with `--hash` lines, or a separate lock.
- The laptop's vetting and Taildrop delivery as a kit verb, alongside `kit_terraform_providers.py` and the portal node_modules pack.
- How `.tools/commit-gate.sh`'s ruff pin and any other tool pins join the same list.
- What a box does when a needed package is not yet approved (hold the cell and file a row, as the seats did today).
- Interaction with C-KIT-PYTHON (PRD v0.14) and the bun disarm (row NFRA_CTLPLN-S13).
