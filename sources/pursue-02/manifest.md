# PURSUE Release 02

**Label: official** for counts taken from the catalog. **Label: analysis** for the notes.

Cleared for release May 22, 2026, as printed on the [archived war.gov/UFO page](https://web.archive.org/web/20261004165250/https://www.war.gov/UFO/) (live page: https://www.war.gov/UFO/).

This folder lists every catalog row whose Release Date is this tranche in the September 29, 2026 spreadsheet (`release=6v5`). There are **64** rows. **54** have the catalog redaction flag set (84.4% of this release).

Press release: [live](https://www.war.gov/News/Releases/Release/Article/4499305/department-of-war-publishes-second-release-of-unidentified-anomalous-phenomena/) and [archived copy](https://web.archive.org/web/20260522135306/https://www.war.gov/News/Releases/Release/Article/4499305/department-of-war-publishes-second-release-of-unidentified-anomalous-phenomena/).

Download bundles linked from the October 4, 2026 archived PURSUE page. These zips were not downloaded. The page states these sizes:

- Documents: 70.1 MB — https://www.war.gov/medialink/ufo/052226/release_02/release_02_document_bundle.zip
- Videos: 5.6 GB — https://d34w7g4gy10iej.cloudfront.net/uap052226.zip

Agencies on the catalog rows:

- Department of War: 52
- NASA: 7
- Department of Energy: 3
- CIA: 1
- Office of the Director of National Intelligence: 1

File types, after stripping a trailing space that the catalog left on six Release 01 PDF cells:

- audio: 7
- document: 6
- video: 51

## Catalog versions

The counts above are the September 29, 2026 snapshot (`release=6v5`). That is the snapshot the record pages are built from. Earlier copies of the same spreadsheet are stored in [`sources/catalog/`](../catalog/). A release does not have one number.

| Snapshot | Rows in this release | Flagged redacted | PDF | VID | IMG | AUD | Rows in the whole file |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| September 18, 2026, 11:39 UTC (`release=6`) | 64 | 54 | 6 | 51 | 0 | 7 | 446 |
| September 18, 2026, 15:56 UTC (`release=6v3`) | 64 | 54 | 6 | 51 | 0 | 7 | 447 |
| September 19, 2026, 20:49 UTC (`release=6`) | 64 | 54 | 6 | 51 | 0 | 7 | 447 |
| September 29, 2026, 12:00 UTC (`release=6v5`) | 64 | 54 | 6 | 51 | 0 | 7 | 450 |

The row count for this release does not change across the September snapshots stored here: 64 rows, 51 of them videos.

Many of those video descriptions say that on March 6, 2026, eight members of the House asked for 51 records. That sentence is the catalog's. It is not Rep. Anna Paulina Luna's letter. Her letter is a different document, dated March 31, 2026, with 46 numbered items covering 50 videos and a deadline of April 14, 2026. A copy is in [sources/house-oversight](../house-oversight/README.md). The catalog's PR050 title matches item 1 of that letter, and PR051 matches item 2. See [the Syria case](../../cases/syria-instant-acceleration.md).

## DVIDS

For each video and audio row, [manifest.json](manifest.json) has the DVIDS title, date taken, date posted, duration, the description quoted from the page, every download-popup resolution with the size text DVIDS printed, the HLS renditions, and a SHA-256 when the public MP4 was downloaded on October 6, 2026. Those media files are not in this repository. Every download-menu URL on this release returned HTTP 403, so the exact byte length of those renditions was not measured.

DVIDS ids flagged on this release:

- [dow-uap-pr057a-spherical-uap-in-clouds](../../records/dow-uap-pr057a-spherical-uap-in-clouds.md): This DVIDS page matches this catalog row. The same id 1007720 is also on: DOW-UAP-PR057b, "[Platform] Observes UAP in East China Sea 05 JAN 2023 INDOPACOM". On those rows the id points at this file, not at that catalog entry. The id was not changed.
- [dow-uap-pr057b-platform-observes-uap-in-east-china-sea-05-jan-2023-indopacom](../../records/dow-uap-pr057b-platform-observes-uap-in-east-china-sea-05-jan-2023-indopacom.md): DVIDS id 1007720 points at DOW-UAP-PR057a, "Spherical UAP in clouds" (https://www.dvidshub.net/video/1007720/dow-uap-pr057a-spherical-uap-clouds), not at this catalog entry (DOW-UAP-PR057b, "[Platform] Observes UAP in East China Sea 05 JAN 2023 INDOPACOM"). The id was not changed. No corrected DVIDS id is proposed. On 2026-10-06 the public DVIDS video sitemaps (13 files from https://www.dvidshub.net/sitemap.xml) contained 173 URLs with 'uap' in the path. URLs containing '057b': none. URLs containing '057': https://www.dvidshub.net/video/1007720/dow-uap-pr057a-spherical-uap-in-clouds.

| Archive id | DVIDS id | DVIDS title | Date taken | Duration | SHA-256 |
| --- | --- | --- | --- | --- | --- |
| [dow-uap-pr050](../../records/dow-uap-pr050.md) | `1007706` | DOW-UAP-PR050, "4 UAP Formation Iran 26 Aug 2022 over water [CALLSIGN]" | 08.26.2022 | 00:00:09 | b542f90ec73780e22740561c5fa4c6bc929505019f69a318e1267a686e9be3b2 |
| [dow-uap-pr051](../../records/dow-uap-pr051.md) | `1007707` | DOW-UAP-PR051, "Syrian UAP instant acceleration" | 01.01.2021 | 00:05:02 | 034759dfc01cb87c718968f3012a57d89acae7baed3a52d60041a59098df2007 |
| [dow-uap-pr052](../../records/dow-uap-pr052.md) | `1007708` | DOW-UAP-PR052, "UAP USO Formation [CALLSIGN] (Mission)" | 06.01.2024 | 00:08:15 | e67b3a3b3d863ef88cc8c4e6b73e9c9bff896506a2962956ed70f508fd8815f5 |
| [dow-uap-pr053](../../records/dow-uap-pr053.md) | `1007709` | DOW-UAP-PR053, "Cigar Shaped or Fast Spherical UAP clip 15 OCT 22" | 10.15.2022 | 00:00:21 | 49b8d56100d62b5add67c9577e3398364777babefe14a99ed21ced6dfbc66a28 |
| [dow-uap-pr054](../../records/dow-uap-pr054.md) | `1007711` | DOW-UAP-PR054, "Spherical UAP Erratic movement [CALLSIGN] (Mission) 2022" | 08.01.2022 | 00:03:57 | dc7f11bf9ccb567929b22350dd7cc117c03f90b98a73335b056bd714fdabe58d |
| [dow-uap-pr055](../../records/dow-uap-pr055.md) | `1007713` | DOW-UAP-PR055, "Spherical UAP over AFG in and out of clouds 23 Nov 2020" | 11.23.2020 | 00:00:47 | 39948c8102f6bdeba4baeff7239ca83a810eb7d5ee686934234965a49f8571a7 |
| [dow-uap-pr056](../../records/dow-uap-pr056.md) | `1007718` | DOW-UAP-PR056, "Spherical UAP pulsing over water [CALLSIGN]" | 06.01.2024 | 00:03:32 | 6a10e2dca088a004a2e9a6fc5983bdbfc3a579ec918c74e755dd49eda557c0b3 |
| [dow-uap-pr058](../../records/dow-uap-pr058.md) | `1007723` | DOW-UAP-PR058, "[CALLSIGN] (Mission) UAP" | 06.24.2024 | 00:10:48 | b7ab972764d15cf742dc417102003d72fa15e0fcbad06f914efd6384ab714db2 |
| [dow-uap-pr059](../../records/dow-uap-pr059.md) | `1007727` | DOW-UAP-PR059, "NAG UAP 1 Jun 20" | 06.01.2020 | 00:04:51 | 11698020b966a3b38178f9ab66272f49d4400feb178fb269229009fbb08b3365 |
| [dow-uap-pr060](../../records/dow-uap-pr060.md) | `1007734` | DOW-UAP-PR060, "Spherical UAP [CALLSIGN] 2021/04/12 obj 2" | 04.12.2021 | 00:04:50 | f9a8e68e747fb91bb9378f7f37179cae2b31eede0702e99468afdf1335bc8129 |
| [dow-uap-pr061](../../records/dow-uap-pr061.md) | `1007735` | DOW-UAP-PR061, "Spherical UAP [CALLSIGN] 2021/04/12 vid 0" | 04.12.2021 | 00:04:46 | 935993ad9d4acc8cc8cb75b059f9dd9f92b7a4a4fae328ef400406e08510d5d4 |
| [dow-uap-pr062](../../records/dow-uap-pr062.md) | `1007739` | DOW-UAP-PR062, "Spherical UAP [CALLSIGN] 2021/04/12 vid 1" | 04.12.2021 | 00:04:49 | 951b0da58cab77ef2aa2de357df6126cccc9c03823072189f6d83c8da7e5f850 |
| [dow-uap-pr063](../../records/dow-uap-pr063.md) | `1007740` | DOW-UAP-PR063, "Spherical UAP [CALLSIGN] 2021/04/12 vid 2" | 04.12.2021 | 00:04:49 | be12d502f9b2e1fb19cd042cf4142e18fe225ecb73e4b78a061f9b06c6db92b3 |
| [dow-uap-pr064](../../records/dow-uap-pr064.md) | `1007741` | DOW-UAP-PR064, "AFSOC Kabul UAP Jul 2017" | 07.01.2017 | 00:00:17 | 915d855cc6f83aa0b0700d9acb23b2804f8fb53dcc20941a51c4b30a994c5cd8 |
| [dow-uap-pr065](../../records/dow-uap-pr065.md) | `1007777` | DOW-UAP-PR065, "USCG C-144 Tyndall UAP 2 TIC TAC IR hot 24 April 2024" | 04.24.2024 | 00:00:39 | db2a52321cacb248dcaf4733a99e42001ec6ac791395d78ad2a1da694e1c51c4 |
| [dow-uap-pr066](../../records/dow-uap-pr066.md) | `1007778` | DOW-UAP-PR066, "USCG C-144 Tyndall UAP 1 TIC TAC IR hot 24 April 2024" | 04.24.2024 | 00:00:48 | dcbdda58cad58f91118dfe399b734361a8e5e35e68090fb0fc654658cc5f51dd |
| [dow-uap-pr067](../../records/dow-uap-pr067.md) | `1007779` | DOW-UAP-PR067, "Multiple Spherical UAP USO near Sub. [CALLSIGN] 2022/03/25 in and out of water" | 03.25.2022 | 00:04:50 | 1db3d8e9407cb17df33f525eecbe93bf1ba5ab4f55f49ca9a4b67829aca12a11 |
| [dow-uap-pr068](../../records/dow-uap-pr068.md) | `1007780` | DOW-UAP-PR068, "IIR 1 666 S0151 23/Video Footage of Unidentified Aerial Phenomenon (UAP) captured by fifth generation aircraft on 20 Jan 23" | 01.23.2020 | 00:01:03 | c27f2a409eff7af286be2f54d43cdbcbf41ded6713dfb4224e0c0a7e673d5395 |
| [dow-uap-pr069](../../records/dow-uap-pr069.md) | `1007781` | DOW-UAP-PR069, "F/A-18 FLIR UAP" | 01.01.2022 | 00:00:29 | 7e81fd782a5b98af5cb941b6e5cce865f15324dea41b8c4cf4577f3d02c3fd66 |
| [dow-uap-pr070](../../records/dow-uap-pr070.md) | `1007783` | DOW-UAP-PR070, "IIR 1 655 S0301 23/Eglin AFB Aircrew Observed Unidentified Aerial Phenomena (UAP) on 13 Feb 23" | 02.13.2023 | 00:00:30 | 80c8e1fc5ac44395d54468b5ef86b5cd9723ea568e9a9d6e5cf95e7265be6457 |
| [dow-uap-pr071](../../records/dow-uap-pr071.md) | `1007784` | DOW-UAP-PR071, "USAF ANG F-16C (callsign [CALLSIGN]) Shoots Down UAP over Lake Huron with [Weapon System], 12 Feb 2023" | 02.12.2023 | 00:00:46 | a803a6933a92da2cb64a7e98ae3e96e31c4aade6455c9ccea463656fee04adce |
| [dow-uap-pr072](../../records/dow-uap-pr072.md) | `1007788` | DOW-UAP-PR072, "ADMINISTRATIVE REVISION: IIR 1777 J0032 22 Kazakhstan - UAP in the vicinity of Karaganda International Airport" | 03.01.2022 | 00:00:17 | 4346f0c05f98430ed8d0ba552a65dcdad234a0918fddcf10d615795be5e08667 |
| [dow-uap-pr073](../../records/dow-uap-pr073.md) | `1007790` | DOW-UAP-PR073, IIR 1 655 S0053 23/Several Unidentified Aerial Phenomenon Encountered In The Vicinity of Columbus OH" | 11.01.2022 | 00:01:28 | 19538301dd75d63746d3a3cc2da7cdd0418f0372130984b68030a4bb1eb7f48e |
| [dow-uap-pr074](../../records/dow-uap-pr074.md) | `1007791` | DOW-UAP-PR074, "[CALLSIGN] (Mission)HD_20220613" | 06.01.2022 | 00:04:45 | d0b8800146dfc84e7d1fd40ff400c5d813cb8139dc7cfcf9b9e1ea189c6e8b47 |
| [dow-uap-pr075](../../records/dow-uap-pr075.md) | `1007795` | DOW-UAP-PR075, "09JUN2021 [Platform] observed UAP in the ECS" | 06.09.2021 | 00:00:23 | f97c19f0ba2ba284c2a86cf2e6c20c0b3908f213d2d1e2b2e3c58f4b57807e34 |
| [dow-uap-pr076](../../records/dow-uap-pr076.md) | `1007804` | DOW-UAP-PR076, "03 January 2021 [CALLSIGN] (Mission) observes UAP" | 01.03.2021 | 00:04:57 | de46a047b742c12692c28cd084569a793f2272ab450b47604043cc8ee3d7e901 |
| [dow-uap-pr077](../../records/dow-uap-pr077.md) | `1007809` | DOW-UAP-PR077, "2 November 2020 [CALLSIGN] [CALLSIGN] Observes and tracks UAP 1 of 2" | 11.02.2020 | 00:04:58 | 972fab6a1268e2566d520410e79689935c6dba01594141caa9fa29145d9e4b17 |
| [dow-uap-pr078](../../records/dow-uap-pr078.md) | `1007812` | DOW-UAP-PR078, "2 November 2020 [CALLSIGN] [CALLSIGN] Observes and tracks UAP 2 of 2" | 11.02.2020 | 00:04:58 | 67b8f03488db6af8687bcef779910ecf4e0663d2902013ebd6f6194bd7c10858 |
| [dow-uap-pr079](../../records/dow-uap-pr079.md) | `1007816` | DOW-UAP-PR079, "29 October 2020 [CALLSIGN] (Mission) observes 3 fast moving UAP's | 10.29.2020 | 00:04:00 | 88279ac587d31a8b1129426eea91175f193015a420e3774966ec3ab4e013ceb3 |
| [dow-uap-pr080](../../records/dow-uap-pr080.md) | `1007803` | DOW-UAP-PR080, "20 October 2020 [CALLSIGN] [CALLSIGN] Observes UAP | 10.20.2020 | 00:04:54 | 2ad200be8b01587371f16d1fbe1b95e58f88e2df934543e1430667ca1fda8dd1 |
| [dow-uap-pr081](../../records/dow-uap-pr081.md) | `1007805` | DOW-UAP-PR081, "18 Oct 2020 [CALLSIGN] observes UAP | 10.18.2020 | 00:04:59 | 55243cef00347eb77df83d47fc05aab35e3a24e35b5e8d254c7482ec6d0a03fd |
| [dow-uap-pr082](../../records/dow-uap-pr082.md) | `1007807` | DOW-UAP-PR082, "16 OCT 2020 [CALLSIGN] views UAP | 10.16.2020 | 00:04:57 | 33b24c0198c14d0d11f9b5781f582bf354e2f2b6d88f9fd9235dfb25071d2782 |
| [dow-uap-pr083](../../records/dow-uap-pr083.md) | `1007808` | DOW-UAP-PR083, "7 October 2020 [CALLSIGN] observes UAP | 10.07.2020 | 00:04:34 | 25da235c0b86f451f6a82e4589459707ad0897533d9aa8e4c8c57b099bb55b63 |
| [dow-uap-pr084](../../records/dow-uap-pr084.md) | `1007810` | DOW-UAP-PR084, "17 Sept 2020 [CALLSIGN] observes UAP | 09.17.2020 | 00:04:13 | 87da3b7cdf6a29638dde7bc5fc575a6f80e8b0408da24dd39b8816a74db4210a |
| [dow-uap-pr085](../../records/dow-uap-pr085.md) | `1007796` | DOW-UAP-PR085, "16 Sept 2020 [CALLSIGN] [CALLSIGN] observes UAP | 09.16.2020 | 00:04:44 | 7ac6790ac1640115d2c8549359af5e86d64c2188b3b68caca508bdea9d02b6b3 |
| [dow-uap-pr086](../../records/dow-uap-pr086.md) | `1007797` | DOW-UAP-PR086, "UAP from Dec 2019 (East Coast) | 12.01.2019 | 00:00:34 | e9dacf0d1dc8c57056f7bf8dae95dfd71dac00535a51ec0c79190ea64ef5c748 |
| [dow-uap-pr087](../../records/dow-uap-pr087.md) | `1007799` | DOW-UAP-PR087, "05 September 2020 [CALLSIGN] UAP | 09.05.2020 | 00:04:54 | d22071e7f8ff90e25dc1a424e20b68c33269b5a748db42f3d0ae18189ad96306 |
| [dow-uap-pr088](../../records/dow-uap-pr088.md) | `1007800` | DOW-UAP-PR088, "31 AUG [CALLSIGN] [CALLSIGN] Observes UAP | 08.31.2020 | 00:04:58 | 0e961dd8c5d4417c8a7319411674a5a3057fae0fd28c341aa2829b6cfc396a96 |
| [dow-uap-pr089](../../records/dow-uap-pr089.md) | `1007712` | DOW-UAP-PR089, "31 AUG [CALLSIGN] [CALLSIGN] Observes UAP part2" | 08.31.2020 | 00:04:58 | e892c8e1e4f814217c1be94a56f50f9c036ce9916458675517ebab5e3a4a19c5 |
| [dow-uap-pr090](../../records/dow-uap-pr090.md) | `1007719` | DOW-UAP-PR090, "24 AUG 2020 [CALLSIGN] (Mission) Observes UAP | 08.24.2020 | 00:04:58 | 72064ff4b0b221a386db7ce76b97043feadc9b436d9ceaa019b381a986c12d51 |
| [dow-uap-pr091](../../records/dow-uap-pr091.md) | `1007716` | DOW-UAP-PR091, "21 AUG [CALLSIGN] Observes UAP in Persian Gulf | 08.21.2020 | 00:04:48 | 7a9da5c7ffb2aefb581535d28a5d14a204f4a0f28a36aea537119b2159d5d224 |
| [dow-uap-pr092](../../records/dow-uap-pr092.md) | `1007715` | DOW-UAP-PR092, "08 AUG 2020 [CALLSIGN] [CALLSIGN] UAP observation | 08.08.2020 | 00:04:52 | de961a4f0052573eaf0a057aed7ab5441ed5c7a7d1f84294b1241ff38517dcb6 |
| [dow-uap-pr093](../../records/dow-uap-pr093.md) | `1007721` | DOW-UAP-PR093, "May 05 2020 Gulf of Arabia [CALLSIGN] (Platform) Dual UAP | 05.05.2020 | 00:00:30 | 7de3ce8f070cdb2379e51a4b571cedc974a1b53921b5adb53d7ff0e264d0e2b4 |
| [dow-uap-pr094](../../records/dow-uap-pr094.md) | `1007722` | DOW-UAP-PR094, "[CALLSIGN] (Mission) - HD 2020-02-13 | 02.13.2020 | 00:04:59 | c80786caac8ee1c1bd769ea864002a9a70e8e728f0510ee745a780f0e39b741a |
| [dow-uap-pr095](../../records/dow-uap-pr095.md) | `1007725` | DOW-UAP-PR095, "May 05 2020 Gulf of Arabia [CALLSIGN] (Platform) Dual UAP" | 05.05.2020 | 00:04:48 | 3169d36bfb5779b697b90d7e1df45daeadbd0a0c305e1b2c071d3055a4a11106 |
| [dow-uap-pr096](../../records/dow-uap-pr096.md) | `1007726` | DOW-UAP-PR096, "HH11 03 July 2018 UAPs | 07.03.2018 | 00:01:19 | fd3cf94325a88b398c89f91df052ea1669d7953506adf79e7de1da23057aeb9a |
| [dow-uap-pr097](../../records/dow-uap-pr097.md) | `1007728` | DOW-UAP-PR097, "Hi-Res: [CALLSIGN] Observes UAP on 25SEP19 at 2135Z" | 09.25.2019 | 00:04:59 | 0a3fa02a7ce357649d1a5d5b4bebc0a323b64101981fa10997eb0b579c710e90 |
| [dow-uap-pr098](../../records/dow-uap-pr098.md) | `1007737` | DOW-UAP-PR098, "UFOs in formation over Persian Gulf? | 01.01.2019 | 00:17:36 | f6d489d9ef68878adc1302219ee99801b6d932785f835812652b661a0215a579 |
| [dow-uap-pr099](../../records/dow-uap-pr099.md) | `1007738` | DOW-UAP-PR099, "Hi-Res: [CALLSIGN] Observes UAP on 25SEP19 at 1715Z | 09.23.2019 | 00:04:51 | b885581a342cf9c00b7ecb541f0f9bd98c8e6cabb54f0dba45f674746ca15809 |
| [nasa-uap-d008](../../records/nasa-uap-d008.md) | `1007870` | NASA-UAP-D008, Apollo 12 Medical Debriefing - Tape 12, 1969 | 12.31.1969 | 00:07:50 | 8aab9b6be1602823a49e0b579bb184ef2eb17cffa7ee4f26e0a84553708bc774 |
| [nasa-uap-d009](../../records/nasa-uap-d009.md) | `1007872` | NASA-UAP-D009, Apollo 17 Audio Excerpt, December 7, 1972 | 12.07.1972 | 00:04:35 | cb0c1525b58f80510b9409c2ea980065370750d7cb9303f9b8684f710cb1deb9 |
| [nasa-uap-d010](../../records/nasa-uap-d010.md) | `1007874` | NASA-UAP-D010, Mercury Atlas 9 Audio Excerpt, May 15, 1963 | 05.15.1963 | 00:03:00 | 392c58d3ebec32241cbaac7b27a1437be827432cf94dcc458e4367dec9eb4a30 |
| [nasa-uap-d011](../../records/nasa-uap-d011.md) | `1007876` | NASA-UAP-D011, Mercury Atlas 9 Audio Excerpt, May 15, 1963 | 05.15.1963 | 00:08:14 | 7f18288e28384224cde647f873b0a1c9f287885a08153bc637c9785e80c59fcb |
| [nasa-uap-d012](../../records/nasa-uap-d012.md) | `1007877` | NASA-UAP-D012, Mercury Atlas 8 Audio Excerpt, October 3, 1962 | 10.03.1962 | 00:03:31 | 8ca2ca5186265864f68f89f493ddbfc9c9cd55c7efebef4a8c6c0d00370180b1 |
| [nasa-uap-d013](../../records/nasa-uap-d013.md) | `1007879` | NASA-UAP-D013, Mercury Atlas 7, May 24, 1962 | 05.24.1962 | 00:01:48 | 732bfabceb63164a17f3c1b9760da9122378c0b5cb8448ef74c3c9d9178325d9 |
| [nasa-uap-d014](../../records/nasa-uap-d014.md) | `1007878` | NASA-UAP-D014, Mercury-Redstone 4, July 21, 1961 | 07.21.1961 | 00:00:26 | d7727da5cae8faef90f1e3bd77ee5cb9933ff34c6741b7ba2c4903c953c89a06 |
| [dow-uap-pr057a-spherical-uap-in-clouds](../../records/dow-uap-pr057a-spherical-uap-in-clouds.md) | `1007720` | DOW-UAP-PR057a, "Spherical UAP in clouds" | 01.01.2023 | 00:01:10 | 43d114fa153fa86523832e35bc9731883a67dd6bc9ea1d34c7afd5a83fe5e570 |
| [dow-uap-pr057b-platform-observes-uap-in-east-china-sea-05-jan-2023-indopacom](../../records/dow-uap-pr057b-platform-observes-uap-in-east-china-sea-05-jan-2023-indopacom.md) | `1007720` (wrong file) | DOW-UAP-PR057a, "Spherical UAP in clouds" | 01.01.2023 | 00:01:10 | not computed |

The machine-readable list, including these version counts, is [manifest.json](manifest.json). Each item also has a page in [`records/`](../../records/).

| Archive id | Official id | Type | Redaction flag | Agency | Title |
| --- | --- | --- | --- | --- | --- |
| [cia-uap-d001](../../records/cia-uap-d001.md) | CIA-UAP-D001 | document | flagged | CIA | CIA-UAP-D001, Intelligence Information Report, USSR, 1973 |
| [doe-uap-d001](../../records/doe-uap-d001.md) | DOE-UAP-D001 | document | flagged | Department of Energy | DOE-UAP-D001, Enhanced PANTEX Imagery |
| [doe-uap-d002](../../records/doe-uap-d002.md) | DOE-UAP-D002 | document | flagged | Department of Energy | DOE-UAP-D002, James Tuck Correspondence, 1970s |
| [doe-uap-d003](../../records/doe-uap-d003.md) | DOE-UAP-D003 | document | flagged | Department of Energy | DOE-UAP-D003, Pajarito Astronomers Invitation, 1986 |
| [dow-uap-d017](../../records/dow-uap-d017.md) | DOW-UAP-D017 | document | not flagged | Department of War | DOW-UAP-D017, UAP Reported at Sandia Base, 1948-1950 |
| [dow-uap-pr050](../../records/dow-uap-pr050.md) | DOW-UAP-PR050 | video | flagged | Department of War | DOW-UAP-PR050, "4 UAP Formation Iran 26 Aug 2022 over water [CALLSIGN]" |
| [dow-uap-pr051](../../records/dow-uap-pr051.md) | DOW-UAP-PR051 | video | flagged | Department of War | DOW-UAP-PR051, "Syrian UAP instant acceleration" |
| [dow-uap-pr052](../../records/dow-uap-pr052.md) | DOW-UAP-PR052 | video | flagged | Department of War | DOW-UAP-PR052, "UAP USO Formation [CALLSIGN] (Mission)" |
| [dow-uap-pr053](../../records/dow-uap-pr053.md) | DOW-UAP-PR053 | video | flagged | Department of War | DOW-UAP-PR053, "Cigar Shaped or Fast Spherical UAP clip 15 OCT 22" |
| [dow-uap-pr054](../../records/dow-uap-pr054.md) | DOW-UAP-PR054 | video | flagged | Department of War | DOW-UAP-PR054, "Spherical UAP Erratic movement [CALLSIGN] (Mission) 2022" |
| [dow-uap-pr055](../../records/dow-uap-pr055.md) | DOW-UAP-PR055 | video | flagged | Department of War | DOW-UAP-PR055, "Spherical UAP over AFG in and out of clouds 23 Nov 2020" |
| [dow-uap-pr056](../../records/dow-uap-pr056.md) | DOW-UAP-PR056 | video | flagged | Department of War | DOW-UAP-PR056, "Spherical UAP pulsing over water [CALLSIGN]" |
| [dow-uap-pr058](../../records/dow-uap-pr058.md) | DOW-UAP-PR058 | video | flagged | Department of War | DOW-UAP-PR058, "[CALLSIGN] (Mission) UAP" |
| [dow-uap-pr059](../../records/dow-uap-pr059.md) | DOW-UAP-PR059 | video | flagged | Department of War | DOW-UAP-PR059, "NAG UAP 1 Jun 20" |
| [dow-uap-pr060](../../records/dow-uap-pr060.md) | DOW-UAP-PR060 | video | flagged | Department of War | DOW-UAP-PR060, "Spherical UAP [CALLSIGN] 2021/04/12 obj 2" |
| [dow-uap-pr061](../../records/dow-uap-pr061.md) | DOW-UAP-PR061 | video | flagged | Department of War | DOW-UAP-PR061, "Spherical UAP [CALLSIGN] 2021/04/12 vid 0" |
| [dow-uap-pr062](../../records/dow-uap-pr062.md) | DOW-UAP-PR062 | video | flagged | Department of War | DOW-UAP-PR062, "Spherical UAP [CALLSIGN] 2021/04/12 vid 1" |
| [dow-uap-pr063](../../records/dow-uap-pr063.md) | DOW-UAP-PR063 | video | flagged | Department of War | DOW-UAP-PR063, "Spherical UAP [CALLSIGN] 2021/04/12 vid 2" |
| [dow-uap-pr064](../../records/dow-uap-pr064.md) | DOW-UAP-PR064 | video | flagged | Department of War | DOW-UAP-PR064, "AFSOC Kabul UAP Jul 2017" |
| [dow-uap-pr065](../../records/dow-uap-pr065.md) | DOW-UAP-PR065 | video | flagged | Department of War | DOW-UAP-PR065, "USCG C-144 Tyndall UAP 2 TIC TAC IR hot 24 April 2024" |
| [dow-uap-pr066](../../records/dow-uap-pr066.md) | DOW-UAP-PR066 | video | flagged | Department of War | DOW-UAP-PR066, "USCG C-144 Tyndall UAP 1 TIC TAC IR hot 24 April 2024" |
| [dow-uap-pr067](../../records/dow-uap-pr067.md) | DOW-UAP-PR067 | video | flagged | Department of War | DOW-UAP-PR067, "Multiple Spherical UAP USO near Sub. [CALLSIGN] 2022/03/25 in and out of water" |
| [dow-uap-pr068](../../records/dow-uap-pr068.md) | DOW-UAP-PR068 | video | flagged | Department of War | DOW-UAP-PR068, "IIR 1 666 S0151 23/Video Footage of Unidentified Aerial Phenomenon (UAP) captured by fifth generation aircraft on 20 Jan 23" |
| [dow-uap-pr069](../../records/dow-uap-pr069.md) | DOW-UAP-PR069 | video | flagged | Department of War | DOW-UAP-PR069, "F/A-18 FLIR UAP" |
| [dow-uap-pr070](../../records/dow-uap-pr070.md) | DOW-UAP-PR070 | video | flagged | Department of War | DOW-UAP-PR070, "IIR 1 655 S0301 23/Eglin AFB Aircrew Observed Unidentified Aerial Phenomena (UAP) on 13 Feb 23" |
| [dow-uap-pr071](../../records/dow-uap-pr071.md) | DOW-UAP-PR071 | video | flagged | Department of War | DOW-UAP-PR071, "USAF ANG F-16C (callsign [CALLSIGN]) Shoots Down UAP over Lake Huron with [Weapon System], 12 Feb 2023" |
| [dow-uap-pr072](../../records/dow-uap-pr072.md) | DOW-UAP-PR072 | video | not flagged | Department of War | DOW-UAP-PR072, "ADMINISTRATIVE REVISION: IIR 1777 J0032 22 Kazakhstan - UAP in the vicinity of Karaganda International Airport" |
| [dow-uap-pr073](../../records/dow-uap-pr073.md) | DOW-UAP-PR073 | video | flagged | Department of War | DOW-UAP-PR073, IIR 1 655 S0053 23/Several Unidentified Aerial Phenomenon Encountered In The Vicinity of Columbus OH" |
| [dow-uap-pr074](../../records/dow-uap-pr074.md) | DOW-UAP-PR074 | video | flagged | Department of War | DOW-UAP-PR074, "[CALLSIGN] (Mission)HD_20220613" |
| [dow-uap-pr075](../../records/dow-uap-pr075.md) | DOW-UAP-PR075 | video | flagged | Department of War | DOW-UAP-PR075, "09JUN2021 [Platform] observed UAP in the ECS" |
| [dow-uap-pr076](../../records/dow-uap-pr076.md) | DOW-UAP-PR076 | video | flagged | Department of War | DOW-UAP-PR076, "03 January 2021 [CALLSIGN] (Mission) observes UAP" |
| [dow-uap-pr077](../../records/dow-uap-pr077.md) | DOW-UAP-PR077 | video | flagged | Department of War | DOW-UAP-PR077, "2 November 2020 [CALLSIGN] [CALLSIGN] Observes and tracks UAP 1 of 2" |
| [dow-uap-pr078](../../records/dow-uap-pr078.md) | DOW-UAP-PR078 | video | flagged | Department of War | DOW-UAP-PR078, "2 November 2020 [CALLSIGN] [CALLSIGN] Observes and tracks UAP 2 of 2" |
| [dow-uap-pr079](../../records/dow-uap-pr079.md) | DOW-UAP-PR079 | video | flagged | Department of War | DOW-UAP-PR079, "29 October 2020 [CALLSIGN] (Mission) observes 3 fast moving UAP's" |
| [dow-uap-pr080](../../records/dow-uap-pr080.md) | DOW-UAP-PR080 | video | flagged | Department of War | DOW-UAP-PR080, "20 October 2020 [CALLSIGN] [CALLSIGN] Observes UAP" |
| [dow-uap-pr081](../../records/dow-uap-pr081.md) | DOW-UAP-PR081 | video | flagged | Department of War | DOW-UAP-PR081, "18 Oct 2020 [CALLSIGN] observes UAP" |
| [dow-uap-pr082](../../records/dow-uap-pr082.md) | DOW-UAP-PR082 | video | flagged | Department of War | DOW-UAP-PR082, "16 OCT 2020 [CALLSIGN] views UAP" |
| [dow-uap-pr083](../../records/dow-uap-pr083.md) | DOW-UAP-PR083 | video | flagged | Department of War | DOW-UAP-PR083, "7 October 2020 [CALLSIGN] observes UAP" |
| [dow-uap-pr084](../../records/dow-uap-pr084.md) | DOW-UAP-PR084 | video | flagged | Department of War | DOW-UAP-PR084, "17 Sept 2020 [CALLSIGN] observes UAP" |
| [dow-uap-pr085](../../records/dow-uap-pr085.md) | DOW-UAP-PR085 | video | flagged | Department of War | DOW-UAP-PR085, "16 Sept 2020 [CALLSIGN] [CALLSIGN] observes UAP" |
| [dow-uap-pr086](../../records/dow-uap-pr086.md) | DOW-UAP-PR086 | video | flagged | Department of War | DOW-UAP-PR086, "UAP from Dec 2019 (East Coast)" |
| [dow-uap-pr087](../../records/dow-uap-pr087.md) | DOW-UAP-PR087 | video | flagged | Department of War | DOW-UAP-PR087, "05 September 2020 [CALLSIGN] UAP" |
| [dow-uap-pr088](../../records/dow-uap-pr088.md) | DOW-UAP-PR088 | video | flagged | Department of War | DOW-UAP-PR088, "31 AUG [CALLSIGN] [CALLSIGN] Observes UAP" |
| [dow-uap-pr089](../../records/dow-uap-pr089.md) | DOW-UAP-PR089 | video | flagged | Department of War | DOW-UAP-PR089, "31 AUG [CALLSIGN] [CALLSIGN] Observes UAP part2" |
| [dow-uap-pr090](../../records/dow-uap-pr090.md) | DOW-UAP-PR090 | video | flagged | Department of War | DOW-UAP-PR090, "24 AUG 2020 [CALLSIGN] (Mission) Observes UAP" |
| [dow-uap-pr091](../../records/dow-uap-pr091.md) | DOW-UAP-PR091 | video | flagged | Department of War | DOW-UAP-PR091, "21 AUG [CALLSIGN] Observes UAP in Persian Gulf" |
| [dow-uap-pr092](../../records/dow-uap-pr092.md) | DOW-UAP-PR092 | video | flagged | Department of War | DOW-UAP-PR092, "08 AUG 2020 [CALLSIGN] [CALLSIGN] UAP observation" |
| [dow-uap-pr093](../../records/dow-uap-pr093.md) | DOW-UAP-PR093 | video | flagged | Department of War | DOW-UAP-PR093, "May 05 2020 Gulf of Arabia [CALLSIGN] (Platform) Dual UAP" |
| [dow-uap-pr094](../../records/dow-uap-pr094.md) | DOW-UAP-PR094 | video | flagged | Department of War | DOW-UAP-PR094, "[CALLSIGN] (Mission) - HD 2020-02-13" |
| [dow-uap-pr095](../../records/dow-uap-pr095.md) | DOW-UAP-PR095 | video | flagged | Department of War | DOW-UAP-PR095, "May 05 2020 Gulf of Arabia [CALLSIGN] (Platform) Dual UAP" |
| [dow-uap-pr096](../../records/dow-uap-pr096.md) | DOW-UAP-PR096 | video | flagged | Department of War | DOW-UAP-PR096, "HH11 03 July 2018 UAPs" |
| [dow-uap-pr097](../../records/dow-uap-pr097.md) | DOW-UAP-PR097 | video | flagged | Department of War | DOW-UAP-PR097, "Hi-Res: [CALLSIGN] Observes UAP on 25SEP19 at 2135Z" |
| [dow-uap-pr098](../../records/dow-uap-pr098.md) | DOW-UAP-PR098 | video | flagged | Department of War | DOW-UAP-PR098, "UFOs in formation over Persian Gulf?" |
| [dow-uap-pr099](../../records/dow-uap-pr099.md) | DOW-UAP-PR099 | video | flagged | Department of War | DOW-UAP-PR099, "Hi-Res: [CALLSIGN] Observes UAP on 25SEP19 at 1715Z" |
| [nasa-uap-d008](../../records/nasa-uap-d008.md) | NASA-UAP-D008 | audio | not flagged | NASA | NASA-UAP-D008, Apollo 12 Medical Debriefing - Tape 12, 1969 |
| [nasa-uap-d009](../../records/nasa-uap-d009.md) | NASA-UAP-D009 | audio | not flagged | NASA | NASA-UAP-D009, Apollo 17 Audio Excerpt, December 7, 1972 |
| [nasa-uap-d010](../../records/nasa-uap-d010.md) | NASA-UAP-D010 | audio | not flagged | NASA | NASA-UAP-D010, Mercury Atlas 9 Audio Excerpt, May 15, 1963 |
| [nasa-uap-d011](../../records/nasa-uap-d011.md) | NASA-UAP-D011 | audio | not flagged | NASA | NASA-UAP-D011, Mercury Atlas 9 Audio Excerpt, May 15, 1963 |
| [nasa-uap-d012](../../records/nasa-uap-d012.md) | NASA-UAP-D012 | audio | not flagged | NASA | NASA-UAP-D012, Mercury Atlas 8 Audio Excerpt, October 3, 1962 |
| [nasa-uap-d013](../../records/nasa-uap-d013.md) | NASA-UAP-D013 | audio | not flagged | NASA | NASA-UAP-D013, Mercury Atlas 7, May 24, 1962 |
| [nasa-uap-d014](../../records/nasa-uap-d014.md) | NASA-UAP-D014 | audio | not flagged | NASA | NASA-UAP-D014, Mercury-Redstone 4, July 21, 1961 |
| [odni-uap-d001](../../records/odni-uap-d001.md) | ODNI-UAP-D001 | document | not flagged | Office of the Director of National Intelligence | ODNI-UAP-D001, USPER Narrative, Senior USIC Official |
| [dow-uap-pr057a-spherical-uap-in-clouds](../../records/dow-uap-pr057a-spherical-uap-in-clouds.md) |  | video | flagged | Department of War | DOW-UAP-PR057a, "Spherical UAP in clouds" |
| [dow-uap-pr057b-platform-observes-uap-in-east-china-sea-05-jan-2023-indopacom](../../records/dow-uap-pr057b-platform-observes-uap-in-east-china-sea-05-jan-2023-indopacom.md) |  | video | flagged | Department of War | DOW-UAP-PR057b, "[Platform] Observes UAP in East China Sea 05 JAN 2023 INDOPACOM" |
