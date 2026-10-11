# PURSUE Release 01

**Label: official** for counts taken from the catalog. **Label: analysis** for the notes.

Cleared for release May 8, 2026, as printed on the [archived war.gov/UFO page](https://web.archive.org/web/20261004165250/https://www.war.gov/UFO/) (live page: https://www.war.gov/UFO/).

This folder lists every catalog row whose Release Date is this tranche in the September 29, 2026 spreadsheet (`release=6v5`). There are **158** rows. **105** have the catalog redaction flag set (66.5% of this release).

Press release: [live](https://www.war.gov/News/Releases/Release/Article/4480582/department-of-war-releases-unidentified-anomalous-phenomena-files-in-historic-t/) and [archived copy](https://web.archive.org/web/20260508125016/https://www.war.gov/News/Releases/Release/Article/4480582/department-of-war-releases-unidentified-anomalous-phenomena-files-in-historic-t/).

Download bundles linked from the October 4, 2026 archived PURSUE page. These zips were not downloaded. The page states these sizes:

- Documents: 1.2 GB — https://www.war.gov/medialink/ufo/bundle/Release_1.zip
- Videos: 1.3 GB — https://d34w7g4gy10iej.cloudfront.net/uapvideos.zip

Agencies on the catalog rows:

- Department of War: 79
- FBI: 57
- NASA: 15
- Department of State: 7

File types, after stripping a trailing space that the catalog left on six Release 01 PDF cells:

- audio: 1
- document: 116
- image: 14
- video: 27

## Catalog versions

The counts above are the September 29, 2026 snapshot (`release=6v5`). That is the snapshot the record pages are built from. Earlier copies of the same spreadsheet are stored in [`sources/catalog/`](../catalog/). A release does not have one number.

| Snapshot | Rows in this release | Flagged redacted | PDF | VID | IMG | AUD | Rows in the whole file |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| May 20, 2026, 09:58 UTC (`no query string`) | 158 | 105 | 116 | 28 | 14 | 0 | 158 |
| September 18, 2026, 11:39 UTC (`release=6`) | 158 | 105 | 116 | 27 | 14 | 1 | 446 |
| September 18, 2026, 15:56 UTC (`release=6v3`) | 158 | 105 | 116 | 27 | 14 | 1 | 447 |
| September 19, 2026, 20:49 UTC (`release=6`) | 158 | 105 | 116 | 27 | 14 | 1 | 447 |
| September 29, 2026, 12:00 UTC (`release=6v5`) | 158 | 105 | 116 | 27 | 14 | 1 | 450 |

The table is official catalog rows. Launch-day news is a separate count, and it is **press**.

Launch-day coverage on May 8 counted **162** catalog entries: 120 PDFs, 28 videos, 14 images, and 108 flagged redacted. An independent fact-check on October 5, 2026 found that breakdown in The Next Web, USA Herald, and other write-ups. This archive did not re-open those articles on October 6 (the Next Web URL returned HTTP 404). No CSV from May 8 through May 19 is stored here. Both 162 and 158 are descriptions of catalog rows. They are not a count of files inside the zip bundles. The gap is 4 PDF rows and 3 redaction flags. The video count (28) and the image count (14) in that press breakdown match the May 20 CSV.

An advocate tracker (pursueufotracker.com) says duplicate PDF rows were consolidated on May 11, and it gives 161 then 158 rather than 162. That account is **unverified**. See [unverified claims](../../gaps/unverified-claims.md). Nothing in the snapshots stored here shows a video or image row withdrawn.

NASA-UAP-D003A, the Gemini 7 audio excerpt, is type VID in the May 20 CSV and type AUD from the September 18 morning CSV onward. The September 29 composition of this release is therefore 27 videos and 1 audio, not the launch-week 28 videos and 0 audio.

Two titles also changed spelling after May 20: DOW-UAP-D052 ("Correspondance" to "Correspondence") and NASA-UAP-D007 ("Techincal" to "Technical"). Those fixes, and the VID-to-AUD change, are the Release 01 differences this archive can see between May 20 and September 29. The row count stays 158.

## DVIDS

For each video and audio row, [manifest.json](manifest.json) has the DVIDS title, date taken, date posted, duration, the description quoted from the page, every download-popup resolution with the size text DVIDS printed, the HLS renditions, and a SHA-256 when the public MP4 was downloaded on October 6, 2026. Those media files are not in this repository. Every download-menu URL on this release returned HTTP 403, so the exact byte length of those renditions was not measured.

DVIDS ids flagged on this release:

- [dow-uap-pr049](../../records/dow-uap-pr049.md): This DVIDS page matches this catalog row. The same id 1006111 is also on: FBI Photo A001. On those rows the id points at this file, not at that catalog entry. The id was not changed.
- [fbi-photo-a001](../../records/fbi-photo-a001.md): DVIDS id 1006111 points at DOW-UAP-PR49, Unresolved UAP Report, Department of the Army, 2026 (https://www.dvidshub.net/video/1006111/dow-uap-pr49-unresolved-uap-report-department-army-2026), a video, not at this catalog entry (FBI Photo A001), which is a still image. Catalog Image VIRIN: 260508-O-D0360-1021. The id was not changed. No corrected DVIDS id is proposed. On 2026-10-06 the AARO unit page (https://www.dvidshub.net/unit/AARO) listed 0 images and 173 videos. The 120 public image sitemaps contained 0 occurrences of VIRIN 260508-O-D0360-1021 and 0 occurrences of 'photo-a001'.

| Archive id | DVIDS id | DVIDS title | Date taken | Duration | SHA-256 |
| --- | --- | --- | --- | --- | --- |
| [dow-uap-pr019](../../records/dow-uap-pr019.md) | `1006056` | DOW-UAP-PR19, Unresolved UAP Report, Middle East, May 2022 | 05.01.2022 | 00:00:05 | a38432ae56298abadf50de06103a6fbd591ea539e124ab1db25a4a511468cfb6 |
| [dow-uap-pr021](../../records/dow-uap-pr021.md) | `1006059` | DOW-UAP-PR21, Unresolved UAP Report, Iraq, May 2022 | 05.01.2022 | 00:00:10 | af62b4e40a2eb0fd39f98093be2a6ae50271a011e7d5caca2119b26aaabc1212 |
| [dow-uap-pr022](../../records/dow-uap-pr022.md) | `1006060` | DOW-UAP-PR22, Unresolved UAP Report, Syria, July 2022 | 07.01.2022 | 00:00:14 | 17106a65c823fb0c4c55f41be31f863f18300bd858f536726ea6f9f3cf35ac8c |
| [dow-uap-pr023](../../records/dow-uap-pr023.md) | `1006062` | DOW-UAP-PR23, Unresolved UAP Report, Iraq, December 2022 | 12.01.2022 | 00:00:10 | d6a177a7004837546b8e3ea12ad0e632d9c31eabca427e05ae6eb9d4e4493f47 |
| [dow-uap-pr026](../../records/dow-uap-pr026.md) | `1006063` | DOW-UAP-PR26, Unresolved UAP Report, United Arab Emirates, October 2023 | 10.01.2023 | 00:00:43 | 46fdeec860cdaa6b27b6fcc51d0b7e045347d494832cdc65f2038e702eaa58aa |
| [dow-uap-pr027](../../records/dow-uap-pr027.md) | `1006067` | DOW-UAP-PR27, Unresolved UAP Report, United Arab Emirates, October 2023 | 10.01.2023 | 00:04:57 | 3c510fe34677a0784c656105b9653ce3039d83de46f929f1ee6d6fb820ce3b8c |
| [dow-uap-pr028](../../records/dow-uap-pr028.md) | `1006073` | DOW-UAP-PR28, Unresolved UAP Report, Greece, January 2024 | 01.01.2024 | 00:01:06 | 9aa868828e0b7be178604162a8abc1e11f0ee6e27d9c48eabbee4d032a50fd72 |
| [dow-uap-pr029](../../records/dow-uap-pr029.md) | `1006074` | DOW-UAP-PR29, Unresolved UAP Report, United Arab Emirates, June 2024 | 06.01.2024 | 00:00:21 | 4e1882dcb2a3bd0253a29fce2bb415fdb2f1196e694a3185c31a82e3a8127ba8 |
| [dow-uap-pr031](../../records/dow-uap-pr031.md) | `1006076` | DOW-UAP-PR31, Unresolved UAP Report, Syria, October 2024 | 10.01.2024 | 00:00:05 | 3862ae94ef113a44814a6cc0362ac689333580afd1a307005f51abd0d4b9e3df |
| [dow-uap-pr032](../../records/dow-uap-pr032.md) | `1006078` | DOW-UAP-PR32, Unresolved UAP Report, Syria, October 2024 | 10.01.2024 | 00:00:06 | 74bd47f0b608c19367b673ba186071db725719eebc7c7b251b8ef2b944c6427e |
| [dow-uap-pr033](../../records/dow-uap-pr033.md) | `1006079` | DOW-UAP-PR33, Unresolved UAP Report, Syria, October 2024 | 10.01.2024 | 00:00:05 | 5bdc888fd25014c5519d625764233f66ee0214bfa48c1670aff5d7c00029a5d9 |
| [dow-uap-pr034](../../records/dow-uap-pr034.md) | `1006080` | DOW-UAP-PR34, Unresolved UAP Report, Greece, October 2023 | 10.01.2023 | 00:02:57 | 34eb85ab42bb6ce5d376c02fd2db4eee0211864ed3bcd8a8247a08fe0da8c99e |
| [dow-uap-pr035](../../records/dow-uap-pr035.md) | `1006082` | DOW-UAP-PR35, Unresolved UAP Report, Greece, October 2023 | 10.01.2023 | 00:00:24 | 670077e60bca959cde784ae1595688d645397804d811a7f5a85912c60045d471 |
| [dow-uap-pr036](../../records/dow-uap-pr036.md) | `1006083` | DOW-UAP-PR36, Unresolved UAP Report, Middle East, May 2020 | 05.01.2020 | 00:02:17 | 5f32ce0126de2c9571f2af368b2629c15b4f1cb3582700641ef31c1d1a8ceac8 |
| [dow-uap-pr037](../../records/dow-uap-pr037.md) | `1006087` | DOW-UAP-PR37, Unresolved UAP Report, Middle East, 2020 | 01.01.2020 | 00:00:09 | 5d60cc99eda2223d7509c9ac801aa1b66200ac24572256d306b1cdb754c0ad8a |
| [dow-uap-pr038](../../records/dow-uap-pr038.md) | `1006088` | DOW-UAP-PR38, Unresolved UAP Report, Middle East, 2013 | 01.01.2013 | 00:01:46 | bd3f5269c3f123b90db76c9496f8ddbb145184c66b0c11cd3cfd9e54f5b683b6 |
| [dow-uap-pr039](../../records/dow-uap-pr039.md) | `1006089` | DOW-UAP-PR39, Unresolved UAP Report, Middle East, 2020 | 01.01.2020 | 00:00:05 | b0975d88681b2d0afb31cf83c43d4e63fedef67fec5687795bdec257decb0825 |
| [dow-uap-pr040](../../records/dow-uap-pr040.md) | `1006093` | DOW-UAP-PR40, Unresolved UAP Report, Middle East, 2020 | 01.01.2020 | 00:01:03 | e91f12de19cadaa3af6c324bc3caa83af2ce47c80fefbceeb5e038f5c1866dac |
| [dow-uap-pr041](../../records/dow-uap-pr041.md) | `1006094` | DOW-UAP-PR41, Unresolved UAP Report, Middle East, 2020 | 01.01.2020 | 00:01:34 | ea6b86de5ec070a789e515456fb7ed2ef0bfbe536b30025117ef47cefa59c503 |
| [dow-uap-pr042](../../records/dow-uap-pr042.md) | `1006097` | DOW-UAP-PR42, Unresolved UAP Report, Middle East, 2020 | 01.01.2020 | 00:04:53 | 049ce64e1dcd06c0b054e74c196d339b8fd2778091d82ff9d230e5c83253c0d6 |
| [dow-uap-pr043](../../records/dow-uap-pr043.md) | `1006159` | DOW-UAP-PR43, Unresolved UAP Report, Africa, 2025 | 01.01.2025 | 00:00:11 | 1847cfc831b0a2299b070c958234a1679ebc719489a0eabe032b667eac65588f |
| [dow-uap-pr044](../../records/dow-uap-pr044.md) | `1006104` | DOW-UAP-PR44, Unresolved UAP Report, Middle East, 2020 | 01.01.2020 | 00:05:12 | 9db22223a0384d0439235fe6583cb5be5e7fd38f0d040fec8402ba2edbedd883 |
| [dow-uap-pr045](../../records/dow-uap-pr045.md) | `1006105` | DOW-UAP-PR45, Unresolved UAP Report, Middle East, 2020 | 01.01.2020 | 00:00:58 | 30d4ecc8af56475042a65e52e5910be9d95e3cb08e397293fb52885ba23e9b6e |
| [dow-uap-pr046](../../records/dow-uap-pr046.md) | `1006106` | DOW-UAP-PR46, Unresolved UAP Report, INDOPACOM, 2024 | 01.01.2024 | 00:00:09 | 34ffb5ae5fe4f85871d41579767e4e37bc5c8cbba47fb63a40b8a4e4f39d613d |
| [dow-uap-pr047](../../records/dow-uap-pr047.md) | `1006107` | DOW-UAP-PR47, Unresolved UAP Report, INDOPACOM, 2023 | 01.01.2023 | 00:01:59 | 5d4d87441b6ed4527bfd563900b1534817a751d7897e03e1c61b51b46b95a610 |
| [dow-uap-pr048](../../records/dow-uap-pr048.md) | `1006110` | DOW-UAP-PR48, Unresolved UAP Report, INDOPACOM, 2024 | 01.01.2024 | 00:01:39 | bd1f002f45052b12ee067455a0a4b589b0bdaed40d75874d8da8fbf64eae8dd1 |
| [dow-uap-pr049](../../records/dow-uap-pr049.md) | `1006111` | DOW-UAP-PR49, Unresolved UAP Report, Department of the Army, 2026 | 01.01.2026 | 00:01:49 | dbf0b1a061cc741f88818ac9c938d6752fb5d1c0a3e729b1e6b42f4e859f472f |
| [nasa-uap-d003a](../../records/nasa-uap-d003a.md) | `1006119` | NASA Audio 12/5/1965 Low Earth Orbit | 12.04.1965 | 00:06:11 | 4965639958d9a9dde9c98a17357f1b9818bf2bd36c9e857b69e1d8990fdd095f |

The machine-readable list, including these version counts, is [manifest.json](manifest.json). Each item also has a page in [`records/`](../../records/).

| Archive id | Official id | Type | Redaction flag | Agency | Title |
| --- | --- | --- | --- | --- | --- |
| [dow-uap-d003](../../records/dow-uap-d003.md) | DOW-UAP-D003 | document | flagged | Department of War | DOW-UAP-D003, Mission Report, Arabian Gulf, 2020 |
| [dow-uap-d004](../../records/dow-uap-d004.md) | DOW-UAP-D004 | document | flagged | Department of War | DOW-UAP-D004, Mission Report, Arabian Gulf, 2020 |
| [dow-uap-d005](../../records/dow-uap-d005.md) | DOW-UAP-D005 | document | flagged | Department of War | DOW-UAP-D005, Mission Report, Arabian Gulf, 2020 |
| [dow-uap-d006](../../records/dow-uap-d006.md) | DOW-UAP-D006 | document | flagged | Department of War | DOW-UAP-D006, Mission Report, Arabian Gulf, 2020 |
| [dow-uap-d007](../../records/dow-uap-d007.md) | DOW-UAP-D007 | document | flagged | Department of War | DOW-UAP-D007, Mission Report, Arabian Gulf, 2020 |
| [dow-uap-d008](../../records/dow-uap-d008.md) | DOW-UAP-D008 | document | flagged | Department of War | DOW-UAP-D008, Mission Report, Djibouti, 2025 |
| [dow-uap-d010](../../records/dow-uap-d010.md) | DOW-UAP-D010 | document | flagged | Department of War | DOW-UAP-D010, Mission Report, Middle East, May 2022 |
| [dow-uap-d012](../../records/dow-uap-d012.md) | DOW-UAP-D012 | document | flagged | Department of War | DOW-UAP-D012, Mission Report, Iraq, May 2022 |
| [dow-uap-d014](../../records/dow-uap-d014.md) | DOW-UAP-D014 | document | flagged | Department of War | DOW-UAP-D014, Mission Report, Iraq, May 2022 |
| [dow-uap-d016](../../records/dow-uap-d016.md) | DOW-UAP-D016 | document | flagged | Department of War | DOW-UAP-D016, Mission Report, Syria, July 2022 |
| [dow-uap-d018](../../records/dow-uap-d018.md) | DOW-UAP-D018 | document | flagged | Department of War | DOW-UAP-D018, Mission Report, Iraq, December 2022 |
| [dow-uap-d019](../../records/dow-uap-d019.md) | DOW-UAP-D019 | document | flagged | Department of War | DOW-UAP-D019, Mission Report, Syria, February 21, 2023 |
| [dow-uap-d020](../../records/dow-uap-d020.md) | DOW-UAP-D020 | document | flagged | Department of War | DOW-UAP-D020, Mission Report, Iraq, 2023 |
| [dow-uap-d023](../../records/dow-uap-d023.md) | DOW-UAP-D023 | document | flagged | Department of War | DOW-UAP-D023, Mission Report, United Arab Emirates, October 2023 |
| [dow-uap-d025](../../records/dow-uap-d025.md) | DOW-UAP-D025 | document | flagged | Department of War | DOW-UAP-D025, Mission Report, Greece, January 2024 |
| [dow-uap-d027](../../records/dow-uap-d027.md) | DOW-UAP-D027 | document | flagged | Department of War | DOW-UAP-D027, Mission Report, United Arab Emirates, October 2023 |
| [dow-uap-d028](../../records/dow-uap-d028.md) | DOW-UAP-D028 | document | flagged | Department of War | DOW-UAP-D028, Mission Report, Iraq, September 2024 |
| [dow-uap-d032](../../records/dow-uap-d032.md) | DOW-UAP-D032 | document | flagged | Department of War | DOW-UAP-D032, Mission Report, Syria, October 2024 |
| [dow-uap-d033](../../records/dow-uap-d033.md) | DOW-UAP-D033 | document | flagged | Department of War | DOW-UAP-D033, Mission Report, Greece, October 2023 |
| [dow-uap-d035](../../records/dow-uap-d035.md) | DOW-UAP-D035 | document | flagged | Department of War | DOW-UAP-D035, Mission Report, Greece, October 2023 |
| [dow-uap-d038](../../records/dow-uap-d038.md) | DOW-UAP-D038 | document | flagged | Department of War | DOW-UAP-D038, Range Fouler Debrief, Middle East, May 2020 |
| [dow-uap-d042](../../records/dow-uap-d042.md) | DOW-UAP-D042 | document | flagged | Department of War | DOW-UAP-D042, Range Fouler Debrief, Japan, 2023 |
| [dow-uap-d044](../../records/dow-uap-d044.md) | DOW-UAP-D044 | document | flagged | Department of War | DOW-UAP-D044, Range Fouler Reporting Form, Gulf of Aden, October 2020 |
| [dow-uap-d048](../../records/dow-uap-d048.md) | DOW-UAP-D048 | document | not flagged | Department of War | DOW-UAP-D048, Department of the Air Force Report, 1996 |
| [dow-uap-d049](../../records/dow-uap-d049.md) | DOW-UAP-D049 | document | not flagged | Department of War | DOW-UAP-D049, Launch Summary, Vandenberg AFB, 2000 |
| [dow-uap-d050](../../records/dow-uap-d050.md) | DOW-UAP-D050 | document | flagged | Department of War | DOW-UAP-D050, Email Correspondence, INDOPACOM, April 2025 |
| [dow-uap-d051](../../records/dow-uap-d051.md) | DOW-UAP-D051 | document | flagged | Department of War | DOW-UAP-D051, Email Correspondence, Pacific Time Zone, March 2023 |
| [dow-uap-d052](../../records/dow-uap-d052.md) | DOW-UAP-D052 | document | flagged | Department of War | DOW-UAP-D052, Email Correspondence, NA, August 2024 |
| [dow-uap-d054](../../records/dow-uap-d054.md) | DOW-UAP-D054 | document | flagged | Department of War | DOW-UAP-D054, Mission Report, Mediterranean Sea, NA |
| [dow-uap-d055](../../records/dow-uap-d055.md) | DOW-UAP-D055 | document | flagged | Department of War | DOW-UAP-D055, Mission Report, Syria, November 2016 |
| [dow-uap-d056](../../records/dow-uap-d056.md) | DOW-UAP-D056 | document | flagged | Department of War | DOW-UAP-D056, Range Fouler Debrief, Arabian Sea, August 2020 |
| [dow-uap-d057](../../records/dow-uap-d057.md) | DOW-UAP-D057 | document | flagged | Department of War | DOW-UAP-D057, Range Fouler Reporting Form, Gulf of Aden, September 2020 |
| [dow-uap-d058](../../records/dow-uap-d058.md) | DOW-UAP-D058 | document | flagged | Department of War | DOW-UAP-D058, Range Fouler Debrief, NA, October 2020 |
| [dow-uap-d060](../../records/dow-uap-d060.md) | DOW-UAP-D060 | document | flagged | Department of War | DOW-UAP-D060, Mission Report, Arabian Gulf, August 2020 |
| [dow-uap-d061](../../records/dow-uap-d061.md) | DOW-UAP-D061 | document | flagged | Department of War | DOW-UAP-D061, Mission Report, Arabian Gulf, August 2020 |
| [dow-uap-d062](../../records/dow-uap-d062.md) | DOW-UAP-D062 | document | flagged | Department of War | DOW-UAP-D062, Mission Report, Strait of Hormuz, September 2020 |
| [dow-uap-d063](../../records/dow-uap-d063.md) | DOW-UAP-D063 | document | flagged | Department of War | DOW-UAP-D063, Mission Report, Strait of Hormuz, October 2020 |
| [dow-uap-d064](../../records/dow-uap-d064.md) | DOW-UAP-D064 | document | flagged | Department of War | DOW-UAP-D064, Mission Report, Iran, November 2020 |
| [dow-uap-d065](../../records/dow-uap-d065.md) | DOW-UAP-D065 | document | flagged | Department of War | DOW-UAP-D065, Mission Report, Arabian Gulf, July 2020 |
| [dow-uap-d074](../../records/dow-uap-d074.md) | DOW-UAP-D074 | document | flagged | Department of War | DOW-UAP-D074, Mission Report, Syria, November 2023 |
| [dow-uap-d075](../../records/dow-uap-d075.md) | DOW-UAP-D075 | document | flagged | Department of War | DOW-UAP-D075, Mission Report, Gulf of Aden, July 2024 |
| [dow-uap-pr019](../../records/dow-uap-pr019.md) | DOW-UAP-PR019 | video | flagged | Department of War | DOW-UAP-PR019, Unresolved UAP Report, Middle East, May 2022 |
| [dow-uap-pr020](../../records/dow-uap-pr020.md) | DOW-UAP-PR020 | document | flagged | Department of War | DOW-UAP-PR020, Unresolved UAP Report, Kuwait, May 2022 |
| [dow-uap-pr021](../../records/dow-uap-pr021.md) | DOW-UAP-PR021 | video | flagged | Department of War | DOW-UAP-PR021, Unresolved UAP Report, Iraq, May 2022 |
| [dow-uap-pr022](../../records/dow-uap-pr022.md) | DOW-UAP-PR022 | video | flagged | Department of War | DOW-UAP-PR022, Unresolved UAP Report, Syria, July 2022 |
| [dow-uap-pr023](../../records/dow-uap-pr023.md) | DOW-UAP-PR023 | video | flagged | Department of War | DOW-UAP-PR023, Unresolved UAP Report, Iraq, December 2022 |
| [dow-uap-pr026](../../records/dow-uap-pr026.md) | DOW-UAP-PR026 | video | flagged | Department of War | DOW-UAP-PR026, Unresolved UAP Report, United Arab Emirates, October 2023 |
| [dow-uap-pr027](../../records/dow-uap-pr027.md) | DOW-UAP-PR027 | video | flagged | Department of War | DOW-UAP-PR027, Unresolved UAP Report, United Arab Emirates, October 2023 |
| [dow-uap-pr028](../../records/dow-uap-pr028.md) | DOW-UAP-PR028 | video | flagged | Department of War | DOW-UAP-PR028, Unresolved UAP Report, Greece, January 2024 |
| [dow-uap-pr029](../../records/dow-uap-pr029.md) | DOW-UAP-PR029 | video | flagged | Department of War | DOW-UAP-PR029, Unresolved UAP Report, United Arab Emirates, June 2024 |
| [dow-uap-pr031](../../records/dow-uap-pr031.md) | DOW-UAP-PR031 | video | flagged | Department of War | DOW-UAP-PR031, Unresolved UAP Report, Syria, October 2024 |
| [dow-uap-pr032](../../records/dow-uap-pr032.md) | DOW-UAP-PR032 | video | flagged | Department of War | DOW-UAP-PR032, Unresolved UAP Report, Syria, October 2024 |
| [dow-uap-pr033](../../records/dow-uap-pr033.md) | DOW-UAP-PR033 | video | flagged | Department of War | DOW-UAP-PR033, Unresolved UAP Report, Syria, October 2024 |
| [dow-uap-pr034](../../records/dow-uap-pr034.md) | DOW-UAP-PR034 | video | flagged | Department of War | DOW-UAP-PR034, Unresolved UAP Report, Greece, October 2023 |
| [dow-uap-pr035](../../records/dow-uap-pr035.md) | DOW-UAP-PR035 | video | flagged | Department of War | DOW-UAP-PR035, Unresolved UAP Report, Greece, October 2023 |
| [dow-uap-pr036](../../records/dow-uap-pr036.md) | DOW-UAP-PR036 | video | flagged | Department of War | DOW-UAP-PR036, Unresolved UAP Report, Middle East, May 2020 |
| [dow-uap-pr037](../../records/dow-uap-pr037.md) | DOW-UAP-PR037 | video | flagged | Department of War | DOW-UAP-PR037, Unresolved UAP Report, Middle East, 2020 |
| [dow-uap-pr038](../../records/dow-uap-pr038.md) | DOW-UAP-PR038 | video | flagged | Department of War | DOW-UAP-PR038, Unresolved UAP Report, Middle East, 2013 |
| [dow-uap-pr039](../../records/dow-uap-pr039.md) | DOW-UAP-PR039 | video | flagged | Department of War | DOW-UAP-PR039, Unresolved UAP Report, Middle East, 2020 |
| [dow-uap-pr040](../../records/dow-uap-pr040.md) | DOW-UAP-PR040 | video | flagged | Department of War | DOW-UAP-PR040, Unresolved UAP Report, Middle East, 2020 |
| [dow-uap-pr041](../../records/dow-uap-pr041.md) | DOW-UAP-PR041 | video | flagged | Department of War | DOW-UAP-PR041, Unresolved UAP Report, Middle East, 2020 |
| [dow-uap-pr042](../../records/dow-uap-pr042.md) | DOW-UAP-PR042 | video | flagged | Department of War | DOW-UAP-PR042, Unresolved UAP Report, Middle East, 2020 |
| [dow-uap-pr043](../../records/dow-uap-pr043.md) | DOW-UAP-PR043 | video | flagged | Department of War | DOW-UAP-PR043, Unresolved UAP Report, Africa, 2025 |
| [dow-uap-pr044](../../records/dow-uap-pr044.md) | DOW-UAP-PR044 | video | flagged | Department of War | DOW-UAP-PR044, Unresolved UAP Report, Middle East, 2020 |
| [dow-uap-pr045](../../records/dow-uap-pr045.md) | DOW-UAP-PR045 | video | flagged | Department of War | DOW-UAP-PR045, Unresolved UAP Report, Middle East, 2020 |
| [dow-uap-pr046](../../records/dow-uap-pr046.md) | DOW-UAP-PR046 | video | flagged | Department of War | DOW-UAP-PR046, Unresolved UAP Report, INDOPACOM, 2024 |
| [dow-uap-pr047](../../records/dow-uap-pr047.md) | DOW-UAP-PR047 | video | flagged | Department of War | DOW-UAP-PR047, Unresolved UAP Report, INDOPACOM, 2023 |
| [dow-uap-pr048](../../records/dow-uap-pr048.md) | DOW-UAP-PR048 | video | flagged | Department of War | DOW-UAP-PR048, Unresolved UAP Report, INDOPACOM, 2024 |
| [dow-uap-pr049](../../records/dow-uap-pr049.md) | DOW-UAP-PR049 | video | flagged | Department of War | DOW-UAP-PR049, Unresolved UAP Report, Department of the Army, 2026 |
| [nasa-uap-d001](../../records/nasa-uap-d001.md) | NASA-UAP-D001 | document | not flagged | NASA | NASA-UAP-D001, Apollo 12 Transcript, 1969 |
| [nasa-uap-d002](../../records/nasa-uap-d002.md) | NASA-UAP-D002 | document | not flagged | NASA | NASA-UAP-D002, Apollo 17 Transcript, 1972 |
| [nasa-uap-d003](../../records/nasa-uap-d003.md) | NASA-UAP-D003 | document | not flagged | NASA | NASA-UAP-D003, Gemini 7 Transcript, 1965 |
| [nasa-uap-d003a](../../records/nasa-uap-d003a.md) | NASA-UAP-D003A | audio | not flagged | NASA | NASA-UAP-D003A, Gemini 7 Audio Excerpt, 1965 |
| [nasa-uap-d004](../../records/nasa-uap-d004.md) | NASA-UAP-D004 | document | not flagged | NASA | NASA-UAP-D004, Apollo 11 Technical Crew Debriefing, 1969 |
| [nasa-uap-d005](../../records/nasa-uap-d005.md) | NASA-UAP-D005 | document | not flagged | NASA | NASA-UAP-D005, Apollo 17 Crew Debriefing for Science, 1973 |
| [nasa-uap-d006](../../records/nasa-uap-d006.md) | NASA-UAP-D006 | document | not flagged | NASA | NASA-UAP-D006, Apollo 17 Technical Crew Debriefing, 1973 |
| [nasa-uap-d007](../../records/nasa-uap-d007.md) | NASA-UAP-D007 | document | not flagged | NASA | NASA-UAP-D007, Skylab Technical Crew Debriefing 1973 |
| [nasa-uap-vm001](../../records/nasa-uap-vm001.md) | NASA-UAP-VM001 | image | not flagged | NASA | NASA-UAP-VM001, Apollo 12, 1969 |
| [nasa-uap-vm002](../../records/nasa-uap-vm002.md) | NASA-UAP-VM002 | image | not flagged | NASA | NASA-UAP-VM002, Apollo 12, 1969 |
| [nasa-uap-vm003](../../records/nasa-uap-vm003.md) | NASA-UAP-VM003 | image | not flagged | NASA | NASA-UAP-VM003, Apollo 12, 1969 |
| [nasa-uap-vm004](../../records/nasa-uap-vm004.md) | NASA-UAP-VM004 | image | not flagged | NASA | NASA-UAP-VM004, Apollo 12, 1969 |
| [nasa-uap-vm005](../../records/nasa-uap-vm005.md) | NASA-UAP-VM005 | image | not flagged | NASA | NASA-UAP-VM005, Apollo 12, 1969 |
| [nasa-uap-vm006](../../records/nasa-uap-vm006.md) | NASA-UAP-VM006 | image | not flagged | NASA | NASA-UAP-VM006, Apollo 17, 1972 |
| [18-100754-general-1946-7-vol-2](../../records/18-100754-general-1946-7-vol-2.md) |  | document | not flagged | Department of War | 18_100754_ General 1946-7_Vol_2 |
| [18-6369445-general-1948-vol-1](../../records/18-6369445-general-1948-vol-1.md) |  | document | not flagged | Department of War | 18_6369445_General_1948_Vol_1 |
| [255-413270-ufo-s-and-defense-what-should-we-prepare-for](../../records/255-413270-ufo-s-and-defense-what-should-we-prepare-for.md) |  | document | flagged | NASA | 255_413270_UFO's_and_Defense_What_Should_we_Prepare_For |
| [331-120752-numeric-files-1944-1945-37153-german-armament-equipment-documents](../../records/331-120752-numeric-files-1944-1945-37153-german-armament-equipment-documents.md) |  | document | not flagged | Department of War | 331_120752_Numeric_Files_1944–1945_37153_German_Armament_Equipment_Documents |
| [341-110448-records-relating-to-the-collection-and-dissemination-of-intelligence-1948-1955](../../records/341-110448-records-relating-to-the-collection-and-dissemination-of-intelligence-1948-1955.md) |  | document | not flagged | Department of War | 341_110448_Records_Relating_to_the_Collection_and_Dissemination_of_Intelligence_1948-1955-TS_CONT_No.2_2-5300-2-5399 |
| [341-110677-numerical-file-5-2500](../../records/341-110677-numerical-file-5-2500.md) |  | document | not flagged | Department of War | 341_110677_Numerical_File,_5-2500 |
| [342-hs1-416511228-319-1-flying-discs-1949](../../records/342-hs1-416511228-319-1-flying-discs-1949.md) |  | document | not flagged | Department of War | 342_HS1-416511228_319.1 Flying Discs 1949 |
| [38-143685-box7-incident-summaries-1-100](../../records/38-143685-box7-incident-summaries-1-100.md) |  | document | not flagged | Department of War | 38_143685_box7_Incident_Summaries_1-100 |
| [38-143685-box-incident-summaries-101-172](../../records/38-143685-box-incident-summaries-101-172.md) |  | document | not flagged | Department of War | 38_143685_box_Incident_Summaries_101-172 |
| [38-143685-box-incident-summaries-173-233](../../records/38-143685-box-incident-summaries-173-233.md) |  | document | not flagged | Department of War | 38_143685_box_Incident_Summaries_173-233 |
| [59-214434-sp-16-7-18-1963](../../records/59-214434-sp-16-7-18-1963.md) |  | document | not flagged | Department of State | 59_214434_SP 16 [7.18.1963] |
| [59-64634-711-5612-7-2852](../../records/59-64634-711-5612-7-2852.md) |  | document | not flagged | Department of State | 59_64634_711.5612[7-2852 |
| [65-hs1-101634279-100-de-18221-serial-844](../../records/65-hs1-101634279-100-de-18221-serial-844.md) |  | document | not flagged | FBI | 65_HS1-101634279_100-DE-18221_Serial_844 |
| [65-hs1-101634279-100-de-26505](../../records/65-hs1-101634279-100-de-26505.md) |  | document | flagged | FBI | 65_HS1-101634279_100-DE-26505 |
| [65-hs1-834228961-62-hq-83894-sub-a](../../records/65-hs1-834228961-62-hq-83894-sub-a.md) |  | document | not flagged | FBI | 65_HS1-834228961_62-HQ-83894_SUB_A |
| [65-hs1-834228961-62-hq-83894-section-001](../../records/65-hs1-834228961-62-hq-83894-section-001.md) |  | document | not flagged | FBI | 65_HS1-834228961_62-HQ-83894_Section_001 |
| [65-hs1-834228961-62-hq-83894-section-002](../../records/65-hs1-834228961-62-hq-83894-section-002.md) |  | document | not flagged | FBI | 65_HS1-834228961_62-HQ-83894_Section_002 |
| [65-hs1-834228961-62-hq-83894-section-003](../../records/65-hs1-834228961-62-hq-83894-section-003.md) |  | document | not flagged | FBI | 65_HS1-834228961_62-HQ-83894_Section_003 |
| [65-hs1-834228961-62-hq-83894-section-004](../../records/65-hs1-834228961-62-hq-83894-section-004.md) |  | document | not flagged | FBI | 65_HS1-834228961_62-HQ-83894_Section_004 |
| [65-hs1-834228961-62-hq-83894-section-005](../../records/65-hs1-834228961-62-hq-83894-section-005.md) |  | document | not flagged | FBI | 65_HS1-834228961_62-HQ-83894_Section_005 |
| [65-hs1-834228961-62-hq-83894-section-006](../../records/65-hs1-834228961-62-hq-83894-section-006.md) |  | document | not flagged | FBI | 65_HS1-834228961_62-HQ-83894_Section_006 |
| [65-hs1-834228961-62-hq-83894-section-007](../../records/65-hs1-834228961-62-hq-83894-section-007.md) |  | document | not flagged | FBI | 65_HS1-834228961_62-HQ-83894_Section_007 |
| [65-hs1-834228961-62-hq-83894-section-008](../../records/65-hs1-834228961-62-hq-83894-section-008.md) |  | document | not flagged | FBI | 65_HS1-834228961_62-HQ-83894_Section_008 |
| [65-hs1-834228961-62-hq-83894-section-009](../../records/65-hs1-834228961-62-hq-83894-section-009.md) |  | document | not flagged | FBI | 65_HS1-834228961_62-HQ-83894_Section_009 |
| [65-hs1-834228961-62-hq-83894-section-010](../../records/65-hs1-834228961-62-hq-83894-section-010.md) |  | document | not flagged | FBI | 65_HS1-834228961_62-HQ-83894_Section_010 |
| [65-hs1-834228961-62-hq-83894-serial-130](../../records/65-hs1-834228961-62-hq-83894-serial-130.md) |  | document | not flagged | FBI | 65_HS1-834228961_62-HQ-83894_Serial_130 |
| [65-hs1-834228961-62-hq-83894-serial-153](../../records/65-hs1-834228961-62-hq-83894-serial-153.md) |  | document | not flagged | FBI | 65_HS1-834228961_62-HQ-83894_Serial_153 |
| [65-hs1-834228961-62-hq-83894-serial-164](../../records/65-hs1-834228961-62-hq-83894-serial-164.md) |  | document | not flagged | FBI | 65_HS1-834228961_62-HQ-83894_Serial_164 |
| [65-hs1-834228961-62-hq-83894-serial-220](../../records/65-hs1-834228961-62-hq-83894-serial-220.md) |  | document | not flagged | FBI | 65_HS1-834228961_62-HQ-83894_Serial_220 |
| [65-hs1-834228961-62-hq-83894-serial-403](../../records/65-hs1-834228961-62-hq-83894-serial-403.md) |  | document | not flagged | FBI | 65_HS1-834228961_62-HQ-83894_Serial_403 |
| [65-hs1-834228961-62-hq-83894-serial-438](../../records/65-hs1-834228961-62-hq-83894-serial-438.md) |  | document | not flagged | FBI | 65_HS1-834228961_62-HQ-83894_Serial_438 |
| [65-hs1-834228961-62-hq-83894-serial-449](../../records/65-hs1-834228961-62-hq-83894-serial-449.md) |  | document | not flagged | FBI | 65_HS1-834228961_62-HQ-83894_Serial_449 |
| [fbi-photo-a001](../../records/fbi-photo-a001.md) |  | image | flagged | FBI | FBI Photo A001 |
| [fbi-photo-a002](../../records/fbi-photo-a002.md) |  | image | flagged | FBI | FBI Photo A002 |
| [fbi-photo-a003](../../records/fbi-photo-a003.md) |  | image | flagged | FBI | FBI Photo A003 |
| [fbi-photo-a004](../../records/fbi-photo-a004.md) |  | image | flagged | FBI | FBI Photo A004 |
| [fbi-photo-a005](../../records/fbi-photo-a005.md) |  | image | flagged | FBI | FBI Photo A005 |
| [fbi-photo-a006](../../records/fbi-photo-a006.md) |  | image | flagged | FBI | FBI Photo A006 |
| [fbi-photo-a007](../../records/fbi-photo-a007.md) |  | image | flagged | FBI | FBI Photo A007 |
| [fbi-photo-a008](../../records/fbi-photo-a008.md) |  | image | flagged | FBI | FBI Photo A008 |
| [fbi-photo-b001](../../records/fbi-photo-b001.md) |  | document | flagged | FBI | FBI Photo B001 |
| [fbi-photo-b002](../../records/fbi-photo-b002.md) |  | document | flagged | FBI | FBI Photo B002 |
| [fbi-photo-b003](../../records/fbi-photo-b003.md) |  | document | flagged | FBI | FBI Photo B003 |
| [fbi-photo-b004](../../records/fbi-photo-b004.md) |  | document | flagged | FBI | FBI Photo B004 |
| [fbi-photo-b005](../../records/fbi-photo-b005.md) |  | document | flagged | FBI | FBI Photo B005 |
| [fbi-photo-b006](../../records/fbi-photo-b006.md) |  | document | flagged | FBI | FBI Photo B006 |
| [fbi-photo-b007](../../records/fbi-photo-b007.md) |  | document | flagged | FBI | FBI Photo B007 |
| [fbi-photo-b008](../../records/fbi-photo-b008.md) |  | document | flagged | FBI | FBI Photo B008 |
| [fbi-photo-b009](../../records/fbi-photo-b009.md) |  | document | flagged | FBI | FBI Photo B009 |
| [fbi-photo-b010](../../records/fbi-photo-b010.md) |  | document | flagged | FBI | FBI Photo B010 |
| [fbi-photo-b011](../../records/fbi-photo-b011.md) |  | document | flagged | FBI | FBI Photo B011 |
| [fbi-photo-b012](../../records/fbi-photo-b012.md) |  | document | flagged | FBI | FBI Photo B012 |
| [fbi-photo-b013](../../records/fbi-photo-b013.md) |  | document | flagged | FBI | FBI Photo B013 |
| [fbi-photo-b014](../../records/fbi-photo-b014.md) |  | document | flagged | FBI | FBI Photo B014 |
| [fbi-photo-b015](../../records/fbi-photo-b015.md) |  | document | flagged | FBI | FBI Photo B015 |
| [fbi-photo-b016](../../records/fbi-photo-b016.md) |  | document | flagged | FBI | FBI Photo B016 |
| [fbi-photo-b017](../../records/fbi-photo-b017.md) |  | document | flagged | FBI | FBI Photo B017 |
| [fbi-photo-b018](../../records/fbi-photo-b018.md) |  | document | flagged | FBI | FBI Photo B018 |
| [fbi-photo-b019](../../records/fbi-photo-b019.md) |  | document | flagged | FBI | FBI Photo B019 |
| [fbi-photo-b020](../../records/fbi-photo-b020.md) |  | document | flagged | FBI | FBI Photo B020 |
| [fbi-photo-b021](../../records/fbi-photo-b021.md) |  | document | flagged | FBI | FBI Photo B021 |
| [fbi-photo-b022](../../records/fbi-photo-b022.md) |  | document | flagged | FBI | FBI Photo B022 |
| [fbi-photo-b023](../../records/fbi-photo-b023.md) |  | document | flagged | FBI | FBI Photo B023 |
| [fbi-photo-b024](../../records/fbi-photo-b024.md) |  | document | flagged | FBI | FBI Photo B024 |
| [fbi-september-2023-sighting-composite-sketch](../../records/fbi-september-2023-sighting-composite-sketch.md) |  | document | not flagged | FBI | FBI September 2023 Sighting - Composite Sketch |
| [fbi-september-2023-sighting-serial-003](../../records/fbi-september-2023-sighting-serial-003.md) |  | document | flagged | FBI | FBI September 2023 Sighting - Serial 003 |
| [fbi-september-2023-sighting-serial-004](../../records/fbi-september-2023-sighting-serial-004.md) |  | document | flagged | FBI | FBI September 2023 Sighting - Serial 004 |
| [fbi-september-2023-sighting-serial-005](../../records/fbi-september-2023-sighting-serial-005.md) |  | document | flagged | FBI | FBI September 2023 Sighting - Serial 005 |
| [state-department-uap-cable-001-papua-new-guinea-january-28-1985](../../records/state-department-uap-cable-001-papua-new-guinea-january-28-1985.md) |  | document | not flagged | Department of State | State Department UAP Cable 001, Papua New Guinea, January 28, 1985 |
| [state-department-uap-cable-002-kazakhstan-january-31-1994](../../records/state-department-uap-cable-002-kazakhstan-january-31-1994.md) |  | document | not flagged | Department of State | State Department UAP Cable 002, Kazakhstan, January 31, 1994 |
| [state-department-uap-cable-003-tbilisi-georgia-october-30-2001](../../records/state-department-uap-cable-003-tbilisi-georgia-october-30-2001.md) |  | document | not flagged | Department of State | State Department UAP Cable 003, Tbilisi, Georgia, October 30, 2001 |
| [state-department-uap-cable-004-ashgabat-turkmenistan-november-5-2004](../../records/state-department-uap-cable-004-ashgabat-turkmenistan-november-5-2004.md) |  | document | not flagged | Department of State | State Department UAP Cable 004, Ashgabat, Turkmenistan, November 5, 2004 |
| [state-department-uap-cable-005-mexico-september-16-2003](../../records/state-department-uap-cable-005-mexico-september-16-2003.md) |  | document | not flagged | Department of State | State Department UAP Cable 005, Mexico, September 16, 2003 |
| [usper-statement-about-uap-sighting](../../records/usper-statement-about-uap-sighting.md) |  | document | flagged | FBI | USPER Statement about UAP Sighting |
| [western-us-event](../../records/western-us-event.md) |  | document | not flagged | Department of War | Western US Event |
