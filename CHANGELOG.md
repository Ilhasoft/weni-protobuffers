## [Unreleased]

## [1.2.17] - 2022-08-31
- Add new fields in the channel listing

## [1.2.16] - 2022-08-05
- Add channel_id field to Channel class in billing

## [1.2.15] - 2022-06-09
- Add some details to Message endpoint

## [1.2.14] - 2022-06-08
- Add ChannelWACCreate endpoint
- Add WhatsApp cloud channel endpoint to connect

## [1.2.13] - 2022-05-02
- Added permission type to Users objects related to a specific org.

## [1.2.12] - 2022-04-18
This patch does not have any changes, it aims to resolve conflicts between pypi and the tags of this repository

## [1.2.11] - 2022-04-05
### Added
- README.md

## [1.2.10] - 2022-03-23
### Added
- `project_uuid` to ChannelListResponse

## [1.2.9] - 2022-18-03
### Added
- Add new message named ChannelListRequest
- Update user on weni academy

## [1.2.8] - 2022-01-20
### Refactored
- Some billing endpoint nomenclatures

## [1.2.7] - 2021-12-17
### Added
- Whatsapp router channel.proto

## [1.2.6] - 2021-12-13
### Added
- Add retrieve organization endpoint (#53)

## [1.2.5] - 2021-12-07
### Added
- name, config, and address fields to CreateChannelResponse on connect

## [1.2.4] - 2021-12-01
### Added
- Add Retrieve and List endpoints to Channel service
- Added new fields to channel generic endpoint

## [1.2.3] - 2021-11-16
### Added
- Generic endpoint to create channels on connect

## [1.2.2] - 2021-11-11
### Added
- Generic endpoint to create channels by channeltype_code

## [1.2.1] - 2021-10-28
### Added
- channel release endpoint (#42)

## [1.2.0] - 2021-10-26
### Added
- project_uuid to CreateChannelRequest on connect (#40)

### Fixed
- Add org to message WeniWebChatCreateRequest (#39)

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
