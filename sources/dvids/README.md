# DVIDS metadata

`metadata-2026-10-06.json` is a scrape of the DVIDS pages named in the catalog's "DVIDS Video ID" column. It was collected on October 6, 2026 from `https://www.dvidshub.net/video/{id}`, which is where both the video and the audio items resolved.

For each id the file records the final page URL, the open-graph title, the on-page fields (date taken, date posted, length, location, VIRIN, filename), the media URL embedded in the page, and the `Content-Length` and `ETag` returned by an HTTP HEAD request to that media URL.

The media files themselves are not in this repository. The largest object reported by HEAD was over 3 GB. SHA-256 checksums were not computed.

DVIDS is a Department of Defense public distribution site. The page text is treated as **official**. The HTTP size and ETag are measurements made by this project (**analysis** of a header, not a government statement of the size).
