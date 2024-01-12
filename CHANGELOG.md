# [1.11.0](https://github.com/novuhq/novu-python/compare/v1.10.0...v1.11.0) (2023-12-12)


### Features

* **deps:** update actions/setup-python action to v5 ([921c47d](https://github.com/novuhq/novu-python/commit/921c47db0dd5fdeea1fc4d29d7715d58ae6da793))
* **deps:** update dependency bandit to v1.7.6 ([4f7ed46](https://github.com/novuhq/novu-python/commit/4f7ed46d816b4bf0534418cc64d622481653442e))
* **deps:** update dependency black to v23.11.0 ([6e9f6ef](https://github.com/novuhq/novu-python/commit/6e9f6efe97514823ac4d3d8741739accebb8c75c))
* **deps:** update dependency black to v23.12.0 ([e0d784d](https://github.com/novuhq/novu-python/commit/e0d784d33de9958dacdc7684d3e000e10d935464))
* **deps:** update dependency mypy to v1.7.0 ([8958fa8](https://github.com/novuhq/novu-python/commit/8958fa8b70891bbb56eb54eee2f7c71da544457f))
* **deps:** update dependency mypy to v1.7.1 ([cbf2bab](https://github.com/novuhq/novu-python/commit/cbf2babc56a7adb10fdd48f667a89cb311d38b03))
* **deps:** update dependency pylint to v3.0.3 ([b1c3dd7](https://github.com/novuhq/novu-python/commit/b1c3dd74388e1029158225de21636bae7d73150f))
* **deps:** update dependency sentry-sdk to v1.34.0 ([9450a69](https://github.com/novuhq/novu-python/commit/9450a699d4db70d53725871eaad4523ff64d5da7))
* **deps:** update dependency sentry-sdk to v1.35.0 ([d51928a](https://github.com/novuhq/novu-python/commit/d51928aa3f5d34b0fab84913417223d83496c01a))
* **deps:** update dependency sentry-sdk to v1.38.0 ([313f13c](https://github.com/novuhq/novu-python/commit/313f13cef5329ff4d1a4488fae2412964413344e))
* **deps:** update dependency sphinx-rtd-theme to v2 ([9c17380](https://github.com/novuhq/novu-python/commit/9c17380c66116ae3bcf29910d2872549ffad5284))
* **deps:** update pre-commit hook alessandrojcm/commitlint-pre-commit-hook to v9.10.0 ([61b846d](https://github.com/novuhq/novu-python/commit/61b846d1eab159fc02c6e0f6da7357706790360c))
* **deps:** update pre-commit hook alessandrojcm/commitlint-pre-commit-hook to v9.6.0 ([366f56c](https://github.com/novuhq/novu-python/commit/366f56c6fa157869a09766c0039d388b7bb1c026))
* **deps:** update pre-commit hook alessandrojcm/commitlint-pre-commit-hook to v9.8.0 ([261dcae](https://github.com/novuhq/novu-python/commit/261dcae23de1ac9d4a29aac3d4399f3a00bd1ac8))
* **deps:** update pre-commit hook ambv/black to v23.11.0 ([50becb8](https://github.com/novuhq/novu-python/commit/50becb8cf98726d8cedfa2a6c53b70d6d4916cde))
* **deps:** update pre-commit hook ambv/black to v23.12.0 ([3521382](https://github.com/novuhq/novu-python/commit/3521382100b5bebc3c5640fcd6831be8aa1c2d30))
* **deps:** update pre-commit hook pre-commit/mirrors-mypy to v1.7.0 ([31578d8](https://github.com/novuhq/novu-python/commit/31578d81673f4b2320f7171d9ff7d0933b26a684))
* **deps:** update pre-commit hook pre-commit/mirrors-mypy to v1.7.1 ([7eb477d](https://github.com/novuhq/novu-python/commit/7eb477d80fe195b06c573c9a897c975fd53f819d))
* **deps:** update pre-commit hook pycqa/bandit to v1.7.6 ([376a3a6](https://github.com/novuhq/novu-python/commit/376a3a6c2d06e1f65bbc60e4e7239896808329ff))
* **deps:** update pre-commit hook pycqa/isort to v5.13.1 ([d675166](https://github.com/novuhq/novu-python/commit/d67516633e600cb7a85978c7a23038818411fe61))

# [1.10.0](https://github.com/novuhq/novu-python/compare/v1.9.1...v1.10.0) (2023-11-01)


### Bug Fixes

* [#148](https://github.com/novuhq/novu-python/issues/148) make webhook_url and channel optional in SubscriberChannelSettingsCredentialsDto ([a334e48](https://github.com/novuhq/novu-python/commit/a334e4874bfa4ef8b7cfe57f5de696045c568bd3))


### Features

* **api:** add transaction id param to  MessageApi list method ([4fc5dad](https://github.com/novuhq/novu-python/commit/4fc5dad80f7d2ecbb6a8fc983f99d30654bae874))
* **deps:** update dependency sentry-sdk to v1.33.0 ([939e10d](https://github.com/novuhq/novu-python/commit/939e10de2c9c546341cb8c51a197871622e68d4c))
* **deps:** update dependency sentry-sdk to v1.33.1 ([7d0f327](https://github.com/novuhq/novu-python/commit/7d0f327183fdd06eaac960e662d9ddbcc27f0d48))
* **deps:** update dependency sphinx to v7.2.6 ([f430a40](https://github.com/novuhq/novu-python/commit/f430a40a68d1d0b73bab1ed97ec445537de67bfa))

## [1.9.1](https://github.com/novuhq/novu-python/compare/v1.9.0...v1.9.1) (2023-10-27)


### Bug Fixes

* **subscriber:** prevent errors using bulk_create ([5d29027](https://github.com/novuhq/novu-python/commit/5d290271d24bc2441ccdd9d9adf5ac7fd2f41dda))

# [1.9.0](https://github.com/novuhq/novu-python/compare/v1.8.0...v1.9.0) (2023-10-27)


### Features

* added missing delete topic method in TopicApi ([2e1219d](https://github.com/novuhq/novu-python/commit/2e1219d5c408e2638e43cb68111b51daf9341d18))
* **deps:** update abatilo/actions-poetry action to v2.3.0 ([13dc292](https://github.com/novuhq/novu-python/commit/13dc292ea0131ef0202c1f22e6159d5246623339))
* **deps:** update actions/checkout action to v4 ([0bc3aff](https://github.com/novuhq/novu-python/commit/0bc3affd1066b4eefbf80ff990c8ae5be60a38c2))
* **deps:** update actions/setup-python action to v4 ([c76ed15](https://github.com/novuhq/novu-python/commit/c76ed15e3b9fc4322dac51d1824cd505a961df66))
* **deps:** update dependency black to v23.10.0 ([1cd0805](https://github.com/novuhq/novu-python/commit/1cd0805f68c6353c4004eea0198ab3289196b0a0))
* **deps:** update dependency black to v23.10.1 ([2651b2c](https://github.com/novuhq/novu-python/commit/2651b2c3415d66e0ef403ee9ba147d39e9601d92))
* **deps:** update dependency mypy to v1.6.1 ([c7d7899](https://github.com/novuhq/novu-python/commit/c7d7899a5cb20aa551e66662bc1df2979dc1c738))
* **deps:** update dependency pre-commit to v3 ([a0d7020](https://github.com/novuhq/novu-python/commit/a0d7020903c98f49fa9c686b9407dadf3314dede))
* **deps:** update dependency pylint to v3 ([2739d9e](https://github.com/novuhq/novu-python/commit/2739d9e41f8f03e196ad72ff827fe50b570cc85d))
* **deps:** update dependency pylint to v3.0.2 ([e6289ac](https://github.com/novuhq/novu-python/commit/e6289acbade6f508aa56d1110ca117a87360b965))
* **deps:** update dependency pytest to v7.4.3 ([8fa399f](https://github.com/novuhq/novu-python/commit/8fa399fa5a3260bfc05072f0edb8f712355e1872))
* **deps:** update dependency sphinx to v7 ([4b55b00](https://github.com/novuhq/novu-python/commit/4b55b00e3f8f1df14d2e1e8fb268a4b65afee78a))
* **deps:** update dependency sphinxcontrib-mermaid to ^0.9.0 ([0c1aeca](https://github.com/novuhq/novu-python/commit/0c1aeca37716b240cf857b5654e0b29fd4476873))
* **deps:** update pre-commit hook alessandrojcm/commitlint-pre-commit-hook to v9.5.0 ([fdf285e](https://github.com/novuhq/novu-python/commit/fdf285e428c80994f1d25400833d3efdc71bc80a))
* **deps:** update pre-commit hook ambv/black to v23 ([6c320c9](https://github.com/novuhq/novu-python/commit/6c320c92f29a688bfa13f9c11deb45cf5602eb08))
* **deps:** update pre-commit hook ambv/black to v23.10.0 ([78cc46a](https://github.com/novuhq/novu-python/commit/78cc46aa30d5d65aa0cce8230506fc0036880dda))
* **deps:** update pre-commit hook ambv/black to v23.10.1 ([4c53350](https://github.com/novuhq/novu-python/commit/4c53350bc1866fd0fe15f69a7bd2926f13f41a13))
* **deps:** update pre-commit hook asottile/pyupgrade to v3.15.0 ([824a0fd](https://github.com/novuhq/novu-python/commit/824a0fdf5ebdef5f7d736960e718e265a394ad64))
* **deps:** update pre-commit hook asottile/pyupgrade to v3.3.2 ([30df8a9](https://github.com/novuhq/novu-python/commit/30df8a96f2d890fe7d9c6d6f2d5bfece32166b71))
* **deps:** update pre-commit hook codespell-project/codespell to v2.2.6 ([51b3448](https://github.com/novuhq/novu-python/commit/51b3448d54e183e0d46452c9fb2651db58edf458))
* **deps:** update pre-commit hook lucas-c/pre-commit-hooks-safety to v1.3.2 ([e122efa](https://github.com/novuhq/novu-python/commit/e122efa6faabadf2cf9ab9079adfe9133b623878))
* **deps:** update pre-commit hook pre-commit/mirrors-mypy to v1.0.1 ([0e4c5ca](https://github.com/novuhq/novu-python/commit/0e4c5ca47eca79cb4efae37f2882662a843e99b5))
* **deps:** update pre-commit hook pre-commit/mirrors-mypy to v1.6.0 ([5d1916a](https://github.com/novuhq/novu-python/commit/5d1916a371557701799e09ed292a4dcde0f18010))
* **deps:** update pre-commit hook pre-commit/mirrors-mypy to v1.6.1 ([029e0c7](https://github.com/novuhq/novu-python/commit/029e0c708fe0c859765a4371a7118b89ee1dab83))
* **deps:** update pre-commit hook pre-commit/pre-commit-hooks to v4.5.0 ([939836f](https://github.com/novuhq/novu-python/commit/939836f761057833d32aa9126ff78110a00a90dc))
* **deps:** update pre-commit hook pre-commit/pygrep-hooks to v1.10.0 ([fe1d9cf](https://github.com/novuhq/novu-python/commit/fe1d9cf2cb06522d4d8c8a54f12b70a3b3bc4ecb))
* **deps:** update pre-commit hook pycqa/bandit to v1.7.5 ([58cd4d4](https://github.com/novuhq/novu-python/commit/58cd4d41b6bce6b3b3f497f465de29f694816ae8))

# [1.8.0](https://github.com/novuhq/novu-python/compare/v1.7.0...v1.8.0) (2023-10-16)


### Bug Fixes

* upgrade dependencies for dev environnements ([064e6d0](https://github.com/novuhq/novu-python/commit/064e6d0f13b9777e1f2b07e57472c889b07e9aff))


### Features

* added missing regenerate api key method in Environments ([#99](https://github.com/novuhq/novu-python/issues/99)) ([01585c9](https://github.com/novuhq/novu-python/commit/01585c947e9a8cedd9fb40da67c4f44657bdc2c6))
* **integration:** [#70](https://github.com/novuhq/novu-python/issues/70) - add set_primary method in Integration API ([cfbb7cd](https://github.com/novuhq/novu-python/commit/cfbb7cd3388bb6d604b4d645c9354e75b5698953))

# [1.7.0](https://github.com/novuhq/novu-python/compare/v1.6.0...v1.7.0) (2023-10-14)


### Features

* **blueprint:** add blueprint api ([0e885ea](https://github.com/novuhq/novu-python/commit/0e885ea55c9fec7cd70892f4c1935e92f15e1e21))
* **subscriber:** [#59](https://github.com/novuhq/novu-python/issues/59) - add bulk create for subscribers ([9b5983d](https://github.com/novuhq/novu-python/commit/9b5983d506a020b0361bc03d218196602aa3c857))
* **subscriber:** added the delete_credentials method to the SubscriberApi ([d6ffc98](https://github.com/novuhq/novu-python/commit/d6ffc98c0c448cf6bbe8326f3c3864a8431d0c50))

# [1.6.0](https://github.com/novuhq/novu-python/compare/v1.5.0...v1.6.0) (2023-10-14)


### Features

* **event:** [#94](https://github.com/novuhq/novu-python/issues/94) - support tenant in event api ([50116d6](https://github.com/novuhq/novu-python/commit/50116d68a7475f56ca5f74e37e5de397fd86abd3))

# [1.5.0](https://github.com/novuhq/novu-python/compare/v1.4.0...v1.5.0) (2023-10-14)


### Bug Fixes

* **change:** promoted path parms is required for listing ([#86](https://github.com/novuhq/novu-python/issues/86)) ([9758660](https://github.com/novuhq/novu-python/commit/975866055a0aaab201d27c7fb7f466dd57e46a35))
* **notification:** list notifications should return a paginated response ([#87](https://github.com/novuhq/novu-python/issues/87)) ([1b47e10](https://github.com/novuhq/novu-python/commit/1b47e10deee9be3a015e826d8111e5e8f312e0fb)), closes [#88](https://github.com/novuhq/novu-python/issues/88)


### Features

* added missing methods in notification group class ([#83](https://github.com/novuhq/novu-python/issues/83)) ([951d893](https://github.com/novuhq/novu-python/commit/951d8938ceaca68e211ed3991c0efb93f543b72b))
* **subscriber:** add channels fields on DTO ([#53](https://github.com/novuhq/novu-python/issues/53)) ([b8809b5](https://github.com/novuhq/novu-python/commit/b8809b5b4b342f4fff15fa515b60599d3079fdba))

# [1.4.0](https://github.com/novuhq/novu-python/compare/v1.3.1...v1.4.0) (2023-09-13)


### Bug Fixes

* **#54:** SubscriberApi.list() not returning credentials, field email is missing in SubscriberDto ([#55](https://github.com/novuhq/novu-python/issues/55)) ([5d67f52](https://github.com/novuhq/novu-python/commit/5d67f52c3b844821ad5191a1d840a0d1e464ee12)), closes [#54](https://github.com/novuhq/novu-python/issues/54)
* **feed:** delete a feed doesn't return any data ([84c3ccb](https://github.com/novuhq/novu-python/commit/84c3ccb2ae9848f2b35475147ef1f9353c901acb))


### Features

* **#9:** add notifications resource in wrappers ([f33a32f](https://github.com/novuhq/novu-python/commit/f33a32fc788085516515ba7a3fa54181248e43bf)), closes [#9](https://github.com/novuhq/novu-python/issues/9)
* **tenant:** introduce Tenant API ([330cb19](https://github.com/novuhq/novu-python/commit/330cb19a679f1284487acd8f6beabd3edc681448))

## [1.3.1](https://github.com/novuhq/novu-python/compare/v1.3.0...v1.3.1) (2023-08-30)


### Bug Fixes

* **#47:** prevent error when no page or pageSize are provided for LayoutApi list ([#50](https://github.com/novuhq/novu-python/issues/50)) ([f89feae](https://github.com/novuhq/novu-python/commit/f89feae29c259693f0b22f4924c3338de1b4bf6e)), closes [#47](https://github.com/novuhq/novu-python/issues/47)

# [1.3.0](https://github.com/novuhq/novu-python/compare/v1.2.0...v1.3.0) (2023-06-02)


### Bug Fixes

* allow Novu's enums to be JSON-serializable ([#31](https://github.com/novuhq/novu-python/issues/31)) ([368733e](https://github.com/novuhq/novu-python/commit/368733e4e173288076901c3a1f6d1ec431ec204e)), closes [#26](https://github.com/novuhq/novu-python/issues/26)
* **integration:** ``credentials`` are optionals for an integration ([284c2fd](https://github.com/novuhq/novu-python/commit/284c2fd00b45045e7d49cd910afde051e94c3b46))


### Features

* add function to bulk trigger events ([53a80b7](https://github.com/novuhq/novu-python/commit/53a80b765c9761fae6fade04a4e578885d61ec59))
* **api:** add the inbound-parse api ([#35](https://github.com/novuhq/novu-python/issues/35)) ([ad606eb](https://github.com/novuhq/novu-python/commit/ad606eba9d5be9d022bc553a3941609392ed326a)), closes [#8](https://github.com/novuhq/novu-python/issues/8)
* **api:** allow to override the timeout of `requests` module ([bec1671](https://github.com/novuhq/novu-python/commit/bec1671d8133aa9c337a7bd4864e6f76321e54ac))
* **api:** allow users to provide a `requests` Session ([#34](https://github.com/novuhq/novu-python/issues/34)) ([faf6f7f](https://github.com/novuhq/novu-python/commit/faf6f7f225d5feb4781c9f0c8a8b58f05462ed90)), closes [#25](https://github.com/novuhq/novu-python/issues/25)

# [1.3.0-alpha.2](https://github.com/novuhq/novu-python/compare/v1.3.0-alpha.1...v1.3.0-alpha.2) (2023-06-01)


### Features

* **api:** add the inbound-parse api ([#35](https://github.com/novuhq/novu-python/issues/35)) ([2962d51](https://github.com/novuhq/novu-python/commit/2962d51d415bfa095b7ca3bf452d31b9e34c4e38)), closes [#8](https://github.com/novuhq/novu-python/issues/8)
* **api:** allow to override the timeout of `requests` module ([e1a5064](https://github.com/novuhq/novu-python/commit/e1a5064c23db2564d2ce4dcbdf99e63b3940d3d6))
* **api:** allow users to provide a `requests` Session ([#34](https://github.com/novuhq/novu-python/issues/34)) ([75fdaf6](https://github.com/novuhq/novu-python/commit/75fdaf615273dcafc386cdb7bbc4d09f7be1607d)), closes [#25](https://github.com/novuhq/novu-python/issues/25)

# [1.3.0-alpha.1](https://github.com/novuhq/novu-python/compare/v1.2.1-alpha.1...v1.3.0-alpha.1) (2023-05-25)


### Features

* add function to bulk trigger events ([f9f787e](https://github.com/novuhq/novu-python/commit/f9f787e71c70eeba3be0e4b560a62a42e7a5b3c8))

## [1.2.1-alpha.1](https://github.com/novuhq/novu-python/compare/v1.2.0...v1.2.1-alpha.1) (2023-05-25)


### Bug Fixes

* **integration:** ``credentials`` are optionals for an integration ([0bfe13f](https://github.com/novuhq/novu-python/commit/0bfe13f402a1115bf4a04d3c064815ed47bc8779))

# [1.2.0](https://github.com/novuhq/novu-python/compare/v1.1.0...v1.2.0) (2023-04-13)


### Features

* migration from SpikeeLabs to NovuHQ org ([10d3ead](https://github.com/novuhq/novu-python/commit/10d3ead5f8914b9965461276a27083d6294f10a1))

## [1.1.1-alpha.1](https://github.com/novuhq/novu-python/compare/v1.1.0...v1.1.1-alpha.1) (2023-04-13)


### Bug Fixes

* upgrade dev deps to latest versions ([c6daddb](https://github.com/novuhq/novu-python/commit/c6daddbec611fd23b479ba234131281613434b73))


### Reverts

* remove usage of SEMANTIC_RELEASE_BOT in semver_tag workflow ([3d6e4a6](https://github.com/novuhq/novu-python/commit/3d6e4a6de42bacf06e74775d95ab73341ecb224f))
* rename the 'novu' package to 'novu-python' ([fc2a4ed](https://github.com/novuhq/novu-python/commit/fc2a4edc2b0c659b01f82d4c4d3f918622c7f096))

# [1.1.0](https://github.com/novuhq/novu-python/compare/v1.0.0...v1.1.0) (2023-03-15)


### Features

* rename the 'novu' package to 'novu-python' ([13ad261](https://github.com/novuhq/novu-python/commit/13ad2612266e4d5c44c2e11149ed576f14c8ba03))

# 1.0.0 (2023-03-02)


### Bug Fixes

* typo and remove sentry from dependencies ([8bc2d58](https://github.com/novuhq/novu-python/commit/8bc2d5860bc8bb763f0ecd0cbdcdf0ae0cf206f7))


### Features

* **changes:** add Change DTO definitions and wrappers ([349e370](https://github.com/novuhq/novu-python/commit/349e370494dccb351b06ce98879bea740b1d6333))
* **environments:** add dto and wrapper ([7fac2e9](https://github.com/novuhq/novu-python/commit/7fac2e947526fa51a27b89dde046097ece6fc743))
* **execution-details:** add dto, enums and wrapper ([0aa12ec](https://github.com/novuhq/novu-python/commit/0aa12ec133bf4efa087296581bf6c687a6d1e915))
* **feeds:** setup dto and wrapper ([ba45b62](https://github.com/novuhq/novu-python/commit/ba45b622440c14e9874862838ca4e4c55b057e00))
* **field:** update field DTO after reading Novu codes ([9274408](https://github.com/novuhq/novu-python/commit/927440880898e8064cd50ffc5c250adb092b103f))
* initial setup of the repository ([d25cbd6](https://github.com/novuhq/novu-python/commit/d25cbd646ef01f694df513af390b7b0969ef9a03))
* **messages:** handle dto and wrapper ([f46aa7d](https://github.com/novuhq/novu-python/commit/f46aa7d1e3418a7c9361272e13621ccdb2fbabd4))
* **notification-groups:** setup notification groups DTO and wrapper ([e989788](https://github.com/novuhq/novu-python/commit/e989788227991634e6ffade54d7ea1cdaa953927))
* **notification-templates:** setup enum, dto and wrapper ([e6855ea](https://github.com/novuhq/novu-python/commit/e6855ead4e806f102408da74c71b0bfc30697f8a))

# [1.0.0-alpha.8](https://github.com/novuhq/novu-python/compare/v1.0.0-alpha.7...v1.0.0-alpha.8) (2023-03-01)


### Bug Fixes

* typo and remove sentry from dependencies ([cee5a03](https://github.com/novuhq/novu-python/commit/cee5a03e2178246ec379aaf8b2d3f4459f476ba5))

# [1.0.0-alpha.7](https://github.com/novuhq/novu-python/compare/v1.0.0-alpha.6...v1.0.0-alpha.7) (2023-02-18)


### Features

* **field:** update field DTO after reading Novu codes ([71fba2e](https://github.com/novuhq/novu-python/commit/71fba2eb24e829fe4c99f613b8b8b068365754f0))
