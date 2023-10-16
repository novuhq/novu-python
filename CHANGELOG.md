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
