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
