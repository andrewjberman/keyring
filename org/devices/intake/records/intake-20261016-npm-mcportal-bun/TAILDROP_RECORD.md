# Taildrop record -- batch intake-20261016-npm-mcportal-bun to dell1 (2.0.0_SA_COO~C)

- Pack folder (laptop): `C:/Users/AndrewBerman/tdrop/out/intake-20261016-npm-mcportal-bun` -- 151 files: MANIFEST.json, and per package the .tgz, its .check.json and its .delivery.txt (50 packages).
- Verified before sending: `intake_receive.py verify --from <pack> --ecosystem npm --lockfile org/tier0_exec/0.0.0_AB_MSTR/deliverables/MCPORTAL_c66ca82952_bun.lock` read `INTAKE-VERIFY ... tarballs=50 verified=50 checked=50 stray=0 ok=True`.
- Check 8: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_CHECK8_NFRA_CTLPLN_INTAKE_NPM_MCPORTAL_BUN_20261016.md` @a9b68b6612, 50 of 50 `verdict=checked`, 50 released. Condition carried: dell1's install uses bun's default lifecycle policy (no --trust, no trustedDependencies widening).
- Target: dell1 (tailnet address 100.79.95.44, `tailscale file cp --targets` read at send time, online). Command form, one call per file: `tailscale file cp "<file>" dell1:`.
- Result: TOTAL calls=151 nonzero=0. First call 2026-10-16T23:35:01Z, last call 2026-10-16T23:35:39Z (UTC, read AFTER each call; the exit code is the tool's own, not an inferred delivery).
- DELIVERY IS NOT PROVEN by an exit code: the receiving box's own act (its `intake_receive.py verify` and the precheck) is the oracle. MANIFEST.json sha256 = 8377506a1aacf4f7c094e4a9f21cb09e2966a8c9386e84ca5858446394bd8600

## sha256 of the 50 tarballs as sent

| sha256 | file |
|---|---|
| fa8b176fa0b5d1d72b41ad33443f1f4f75933157a45010dffb51719f40c19c67 | babel__code-frame-7.29.7.tgz |
| 0cf63b5ed704654bdc7574be035883b2eb3f8872c795a6b8dbb690cb7a3d54b9 | babel__compat-data-7.29.7.tgz |
| 46dd458b3d2bc29daa0e9e01f13b399ab544a8013f27ac6c51b56b831c8a0ed3 | babel__core-7.29.7.tgz |
| b5ced4fd7c23a580549182676c43c03a8731b9625e66270f443ab27cd21b502d | babel__generator-7.29.8.tgz |
| 5b5446f3d32b10ba38cb308af5f65e76afcddaacd7b817e71055a6de6ab934e0 | babel__helper-compilation-targets-7.29.7.tgz |
| 94fb962c489aae2c4e5581f1494721083dc76dddd7c703314dd4d7ff965d2a3f | babel__helper-globals-7.29.7.tgz |
| 4bdf46cf597b875ce16770f151159ca34f96c20ba3c112dc8d7f6c6d6cce770c | babel__helper-module-imports-7.29.7.tgz |
| dbb3b9b10b0a2828f5af58a6317685b1a150464c6bd54995069c526aba45e6e4 | babel__helper-module-transforms-7.29.7.tgz |
| 00824ca9e3a146e73a071849b085668ae2012b7fff58056442ab9d33d1e357e8 | babel__helper-plugin-utils-7.29.7.tgz |
| 124565ecd300d7187973060ba6b1d1c4f296e55f0489ddfd6af794f516fed127 | babel__helper-string-parser-7.29.7.tgz |
| 7a31904bc45f1bb232d5e5dd797d12296f4a27fb4bf0f6d517827700f997dc1f | babel__helper-validator-identifier-7.29.7.tgz |
| e32d8ff2cc0455c5210f92f0844d2cb6e1d61b83ee17d7b328fe410f9021e4cd | babel__helper-validator-option-7.29.7.tgz |
| 87dcd8372e8f2d0225de852c9f810c23712616cc2681556f8f4292535b7e42c6 | babel__helpers-7.29.7.tgz |
| 8f3b9fbc531e0c08e2c329cf1ff57bbe121e2d10061b65a05614a25b2255cc43 | babel__parser-7.29.9.tgz |
| fdbe8ac6d7d22e28bd2f013496c233de0906a261cc7e1a7b3eee9bb5fcc70bf0 | babel__plugin-transform-react-jsx-self-7.29.7.tgz |
| 8afa100bf1bafc073813b589980414576b20c66bf3598af229d30b92183fa1a9 | babel__plugin-transform-react-jsx-source-7.29.7.tgz |
| 5e0ee28d5536e986cf5ff2da0f096fb84810d9136c2a64c6c78a6b495a0e7764 | babel__template-7.29.7.tgz |
| cf16861f356fd766361ba4d85d5462b6320e0e59f05cb55c762d8f5dff83e234 | babel__traverse-7.29.8.tgz |
| 514a4ed09355fe1417f03e89c5a5f518745e2eb75a4069d25b55a3e7298069de | babel__types-7.29.8.tgz |
| a5042f06b070d7c07a797bac9dc19676a966f4d11b96648db38d6eb043d3b8f4 | baseline-browser-mapping-2.11.26.tgz |
| ee4a67e56de790dcbd6950170081c0781d785011b469f2b5e543fcf6dcd0086c | browserslist-4.29.1.tgz |
| 2e40d8d93343d5540979a6087943d7fd4604fecbdd02102c26a25cd6218d6240 | bun-types-1.4.2.tgz |
| 61a964ee6800f1a2d5193f88e10ff0093c2d72553bc131cd680abc9f967e6083 | caniuse-lite-1.0.30001812.tgz |
| 0e9342b066986722098d9b108b238033862eae90b3d53ff90581538264d91b60 | cookie-1.1.1.tgz |
| 04f3efe7f0d123260258e89ef45b4a11c7b0793cc7975b6f5bd31c776a480ee3 | electron-to-chromium-1.5.439.tgz |
| e045f94c235c7adc50e77ba2a579c7bec41b496b6b47c3a7845f7c1e19959a88 | esbuild-0.28.2.tgz |
| 7286c3611b6f1f4c4d9ec90adcbc478407ff0d28ead96567f361d53e67613e19 | esbuild__win32-x64-0.28.2.tgz |
| f30a35f6af8c347d01b8ff2f8662272f7d986cf21b916704d86c249a90b97e25 | jridgewell__sourcemap-codec-1.6.0.tgz |
| 4e371b71e3d5081fa0052356d5c1904e7a60e049864c26f0724cfd32dc303849 | nanoid-3.3.19.tgz |
| 3e9f5e0ee1b0a00ce6272e0a7f2d7937fd71ef886080812250aafdf02dcf6d18 | node-releases-2.0.57.tgz |
| 697b463be3cdbd9ffc8f4194fd5019a69ddf95875fb703d78b2b115cc9e740a8 | picomatch-4.0.7.tgz |
| f63d6d9bce28989cd083add85af717c0264e44323d35c909ae99ac934e9641a6 | postcss-8.5.28.tgz |
| 5a4024110c49476e1538a70fd65b9e59d038fcc280b78eb933c24e10453afbf9 | react-19.3.0.tgz |
| dbeffb1e6cdbbbba07f799da4635333d0e20c210a32278dded85441ec4cb6a17 | react-dom-19.3.0.tgz |
| b94544d8041d1588f7f4b93861bfce5c6489c2cb26af0dd797137f2a54faba2d | react-router-7.18.4.tgz |
| 3f8352715d12d307c1f9adc8d47a8a001642110958e85861afafe247c924d6a6 | react-router-dom-7.18.4.tgz |
| 255dac841a66e5a3c89d1595252fa1e6f00bde28f7d8ccc58e7d216e2b81c27c | rollup-4.63.5.tgz |
| 99d291a1356f1e428938a575d8bde8a1ab29261a5ce0f0bbb9419e2ca7a6f68d | rollup__rollup-win32-x64-gnu-4.63.5.tgz |
| 015c446785a131ac670c4b6015a895f4297a523e6597468f029e0aeffcaf2975 | rollup__rollup-win32-x64-msvc-4.63.5.tgz |
| 302995d590e3c0a11eeb40d1d0f299c1df1800135d599d85cdd5faeb614f32d6 | scheduler-0.28.0.tgz |
| afb4afae9175f8b873ac13e1d21cea0997a0bcb40c3598613a834490058cb562 | tinyglobby-0.2.17.tgz |
| b51c55fcc7130237d8d7cf6ecba3d18d17a77abf5cb2a389c653d5b04887b731 | types__bun-1.4.2.tgz |
| ec8f3c0dfb21497db5a3480c45a6cf6f9b18d3b337b2ea4d03e3ef2a9c2bb358 | types__estree-1.0.9.tgz |
| 755b5147491e323c24541830f8eba438c1d1ef8931de725fc613b5439708464a | types__node-24.13.6.tgz |
| ffa77ffdbdc82e5f67a0fd74d750990375a7dfd8685ec7f10a27c0db128f7766 | types__react-19.3.0.tgz |
| 0782e1cd4af4a6a030843235a48e55dc690c36f9428b0b672dc53350806dcf21 | types__react-dom-19.3.0.tgz |
| 4d92799b0e619468a30f70eff033c1a27e713134a4ff353e1a6794f67e425497 | undici-types-7.18.2.tgz |
| 5e345675666e58e36e8c8385e442a18e7815e36ab6b6470835f12a61a80fec6b | update-browserslist-db-1.3.3.tgz |
| c90bd3ea5e6a301d6aac20d22b314fad893a7ac7b010b91a4ac65bb68dd947a6 | vite-7.3.6.tgz |
| 4c3e61fbb4f8648a1ad363fb6e8d1c8407443b7088d2e869217cdc0c2b268011 | vitejs__plugin-react-5.2.0.tgz |

Receiver steps (SC1, dell1, HVST-cc-7): `intake_receive.py verify --from <pack dir> --ecosystem npm --lockfile <bun.lock>` then `intake_receive.py install --ecosystem npm --pack <pack dir> --lockfile <bun.lock> --target <bun cache dir> --by <serial> --receipt-dir <dir>`; receipt = `infra/aws/ec2/opal-gateway/ops/bun_cache_precheck.py <bun.lock> <cache>` reading `77 of 77` (the 50 tarballs plus the packages the cache already holds).
