## [Unreleased]
### Fixed
- Add org to message WeniWebChatCreateRequest

## [1.1.1] - 2021-10-18
### Fixed
- Return UUID on Weni Web Chat Channel endpoint (#35)
- Rename channel create return to "uuid" (#36)

## [1.1.0] - 2021-10-05
### Added
- weni.connect.project.ProjectController.CreateChannel
- weni.connect.project.CreateChannelRequest
- weni.connect.project.CreateChannelResponse
- weni.integrations.user Protocol Buffers
- Updated python package with Connect Protobufs

## [1.0.1] - 2021-08-31
### Added
- weni.flows.channel Protocol Buffers
- Python package with protobufs

### Changed
- Added `user_email` field to weni.connect.project.ClassifierDestroyRequest 
- Protobuf files moved to `src/weni/protobuf` folder

## [1.0.0] - 2021-08-10
### Added
- weni.bothub Protocol Buffers
- weni.connect Protocol Buffers
- weni.flows Protocol Buffers